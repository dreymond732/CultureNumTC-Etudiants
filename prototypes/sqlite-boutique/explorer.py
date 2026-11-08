#!/usr/bin/env python3
"""Examiner les tables sans demander de requête SQL arbitraire à ce script."""
import argparse
import sqlite3
from pathlib import Path

HOME = Path(__file__).resolve().parent
CHOICES = {
    "clients": "SELECT id_client, code_client, ville FROM clients ORDER BY id_client",
    "produits": "SELECT id_produit, libelle, prix_centimes FROM produits ORDER BY id_produit",
    "commandes": "SELECT id_commande, id_client, date_commande FROM commandes ORDER BY id_commande",
    "lignes": "SELECT id_commande, id_produit, quantite, prix_unitaire_centimes FROM lignes_commande ORDER BY id_commande, id_produit",
    "resume": """SELECT c.code_client, COUNT(DISTINCT cmd.id_commande) AS nombre_commandes
                 FROM clients AS c LEFT JOIN commandes AS cmd ON cmd.id_client = c.id_client
                 GROUP BY c.id_client ORDER BY c.id_client"""
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table", choices=sorted(CHOICES))
    parser.add_argument("--db", type=Path, default=HOME / "boutique.sqlite")
    args = parser.parse_args()
    db = args.db.resolve()
    if not db.is_file():
        parser.error("Base absente. Exécutez d'abord preparer.py.")
    # Mode lecture seule : ce script ne modifie pas la base.
    with sqlite3.connect(db.as_uri() + "?mode=ro", uri=True) as conn:
        cur = conn.execute(CHOICES[args.table])
        columns = [c[0] for c in cur.description]
        print(" | ".join(columns))
        for row in cur.fetchall():
            print(" | ".join(map(str, row)))

if __name__ == "__main__":
    main()
