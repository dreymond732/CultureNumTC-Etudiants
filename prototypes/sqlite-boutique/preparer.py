#!/usr/bin/env python3
"""Préparer la base synthétique SQLite BUT-Boutique (sans dépendance externe).

Usage depuis la racine Codespaces :
    python3 prototypes/sqlite-boutique/preparer.py
Le script ne remplace jamais une base existante.
"""
import argparse
import sqlite3
from pathlib import Path

HOME = Path(__file__).resolve().parent

def creer(destination: Path) -> Path:
    destination = destination.expanduser().resolve()
    if destination.exists():
        raise FileExistsError(
            f"La base existe déjà : {destination}. Conservez-la ou choisissez --output.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(destination))
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript((HOME / "schema.sql").read_text(encoding="utf-8"))
        connection.executescript((HOME / "donnees.sql").read_text(encoding="utf-8"))
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise RuntimeError("Échec de la vérification d'intégrité SQLite")
        if connection.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("Clés étrangères non valides")
        connection.commit()
    except Exception:
        connection.rollback()
        connection.close()
        destination.unlink(missing_ok=True)
        raise
    else:
        connection.close()
    return destination

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HOME / "boutique.sqlite")
    args = parser.parse_args()
    path = creer(args.output)
    print(f"Base créée : {path}")
    print("Consultez avec : python3 -m sqlite3", str(path),
          "\"SELECT * FROM clients;\"")

if __name__ == "__main__":
    main()
