#!/usr/bin/env python3
"""Créer un exemple de base relationnelle BUT-Boutique depuis le CSV fictif du TD5.

Ne crée rien en production. Ne remplace jamais une base existante.
"""
import argparse
import csv
import sqlite3
from datetime import datetime
from decimal import Decimal
from pathlib import Path

HERE=Path(__file__).resolve().parent
CSV_SOURCE=HERE.parent/"td5"/"commandes_initiales.csv"
SCHEMA="""
PRAGMA foreign_keys = ON;
CREATE TABLE Clients(id_client INTEGER PRIMARY KEY,nom TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,adresse TEXT NOT NULL);
CREATE TABLE Produits(id_produit TEXT PRIMARY KEY,nom TEXT NOT NULL,
                     prix_centimes INTEGER NOT NULL CHECK(prix_centimes>0));
CREATE TABLE Commandes(id_commande TEXT PRIMARY KEY,date_commande TEXT NOT NULL,
                      id_client INTEGER NOT NULL REFERENCES Clients(id_client));
CREATE TABLE LignesCommande(id_commande TEXT REFERENCES Commandes(id_commande),
                           id_produit TEXT REFERENCES Produits(id_produit),
                           quantite INTEGER NOT NULL CHECK(quantite>0),
                           prix_vente_centimes INTEGER NOT NULL,
                           PRIMARY KEY(id_commande,id_produit));
"""

def creer(destination,source=CSV_SOURCE):
    destination=Path(destination).expanduser().resolve()
    if destination.exists():
        raise FileExistsError("Cette base existe déjà ; ne pas écraser un travail en cours.")
    with Path(source).open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    if not rows:
        raise ValueError("CSV de départ vide.")
    destination.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(destination)
    try:
        con.executescript(SCHEMA)
        clients={}
        products=set()
        orders=set()
        for row in rows:
            email=row["Email_Client"].strip()
            if email not in clients:
                cur=con.execute("INSERT INTO Clients(nom,email,adresse) VALUES (?,?,?)",
                       (row["Nom_Client"],email,row["Adresse_Client"]))
                clients[email]=cur.lastrowid
            product=row["ID_Produit"].strip()
            price=int(Decimal(row["Prix_Unitaire"])*100)
            if product not in products:
                con.execute("INSERT INTO Produits VALUES (?,?,?)",
                            (product,row["Nom_Produit"],price))
                products.add(product)
            order=row["ID_Commande"].strip()
            if order not in orders:
                date=datetime.strptime(row["Date"],"%d/%m/%Y").date().isoformat()
                con.execute("INSERT INTO Commandes VALUES (?,?,?)",
                            (order,date,clients[email]))
                orders.add(order)
            con.execute("INSERT INTO LignesCommande VALUES (?,?,?,?)",
                        (order,product,int(row["Quantite"]),price))
        if con.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("Les liens de la base sont invalides.")
        if con.execute("PRAGMA integrity_check").fetchone()[0]!="ok":
            raise RuntimeError("Échec du contrôle d'intégrité.")
        con.commit()
    except Exception:
        con.rollback()
        con.close()
        destination.unlink(missing_ok=True)
        raise
    con.close()
    return destination

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,default=HERE/"boutique.sqlite")
    args=p.parse_args()
    print("Base de démonstration créée :",creer(args.output))
