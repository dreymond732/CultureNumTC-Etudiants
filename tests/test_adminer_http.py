"""Smoke HTTP de la connexion au vrai Adminer du TD6, lancé par demarrer_adminer.sh.

Prérequis : le serveur est démarré, l'archive SQLite d'essai est créée
et td6/ACCES_ADMINER.txt contient le PIN temporaire. Aucun secret n'est logué.
"""
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import build_opener, HTTPCookieProcessor
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ACCESS = ROOT / "td6" / "ACCES_ADMINER.txt"
DATABASE = str(ROOT / "td6" / "boutique_adminer.sqlite")
URL = "http://127.0.0.1:8765/"

def client():
    return build_opener(HTTPCookieProcessor(CookieJar()))

def request(opener, payload=None):
    post = urlencode(payload).encode("utf-8") if payload else None
    try:
        response = opener.open(URL, data=post, timeout=12)
        return response.status, response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")

def payload(pin):
    return {
        "auth[driver]": "sqlite",
        "auth[server]": "",
        "auth[username]": "",
        "auth[password]": pin,
        "auth[db]": DATABASE,
    }

def main():
    match = re.search(r"CODE À SAISIR : ([0-9]{8})", ACCESS.read_text())
    assert match, "Le fichier temporaire d'accès doit contenir huit chiffres."
    pin = match.group(1)
    assert Path(DATABASE).is_file(), "La copie SQLite doit exister."

    good = client()
    _, form = request(good)
    assert 'inputmode="numeric"' in form, "Le formulaire simplifié manque."
    assert "boutique_adminer.sqlite" in form, "Base non préremplie."
    assert 'name="auth[db]"' in form, "Champ caché de base absent."

    wrong = client()
    request(wrong)
    invalid = "0" * 8 if pin != "0" * 8 else "1" * 8
    _, rejected = request(wrong, payload(invalid))
    assert "Code TD6 incorrect" in rejected, "Code erroné non identifié."

    status, page = request(good, payload(pin))
    assert status == 200, f"Réponse HTTP inattendue : {status}"
    for table in ("Clients", "Produits", "Commandes", "LignesCommande"):
        assert table in page, f"Table absente après connexion : {table}"
    print("ADMINER_TD6_HTTP_OK (formulaire, code, base et quatre tables)")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, URLError) as e:
        print("ÉCHEC :", type(e).__name__, str(e), file=sys.stderr)
        sys.exit(1)
