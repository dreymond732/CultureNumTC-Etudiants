#!/usr/bin/env bash
# TD6 — Adminer SQLite dans le Codespace individuel (port privé uniquement).
# Ne jamais publier ce service sur Internet ni servir le répertoire des bases.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/td6/boutique.sqlite"
COPIE="$ROOT/td6/boutique_adminer.sqlite"
PORT=8765
VERSION=6.0.0

if [[ ! -f "$SOURCE" ]]; then
  echo "Base absente : lancez d'abord python3 td6/generer_base.py depuis la racine du projet." >&2
  exit 1
fi
for cmd in php curl python3; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Dépendance manquante : $cmd. Reconstruisez le Codespace avec la configuration de cours mise à jour." >&2
    exit 1
  fi
done
if ! php -r 'exit(extension_loaded("pdo_sqlite") ? 0 : 1);'; then
  echo "Extension PHP pdo_sqlite absente. Reconstruisez le Codespace (Rebuild Container)." >&2
  exit 1
fi

if [[ ! -e "$COPIE" ]]; then
  cp -- "$SOURCE" "$COPIE"
  echo "Copie créée : td6/boutique_adminer.sqlite"
else
  echo "Copie existante conservée, sans écrasement : td6/boutique_adminer.sqlite"
fi
chmod 600 "$COPIE"

# Adminer (PHP) est servi dans un répertoire temporaire distinct du CSV et du SQLite.
# La base de données n'est PAS sous le document root HTTP.
TMP="$(mktemp -d)"
chmod 700 "$TMP"
trap 'rm -rf -- "$TMP"' EXIT
WEB="$TMP/www"
mkdir -p "$WEB/adminer-plugins"

echo "Téléchargement HTTPS du composant Adminer officiel (version figée $VERSION)..."
curl --fail --silent --show-error --location --retry 2 \
  "https://www.adminer.org/static/download/$VERSION/adminer-$VERSION-sqlite.php" \
  -o "$WEB/index.php"
curl --fail --silent --show-error --location --retry 2 \
  "https://raw.githubusercontent.com/vrana/adminer/refs/tags/v$VERSION/plugins/login-password-less.php" \
  -o "$WEB/adminer-plugins/login-password-less.php"

# SQLite n'a pas de compte/mot de passe natif : le plugin protège l'accès à Adminer.
PASSWORD="$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')"
HASH="$(php -r 'echo password_hash($argv[1], PASSWORD_DEFAULT);' "$PASSWORD")"
cat > "$WEB/adminer-plugins.php" <<PHP
<?php
return array(
    new AdminerLoginPasswordLess('$HASH'),
);
PHP
chmod 600 "$WEB/adminer-plugins.php"

echo
echo "TD6 — Ouvrez le port $PORT dans l'onglet Ports de Codespaces et gardez-le PRIVATE."
echo "Dans Adminer : système SQLite 3 ; utilisateur vide ; mot de passe ci-dessous."
echo "Mot de passe temporaire : $PASSWORD"
echo "Base de données (copiez le chemin complet) : $COPIE"
echo "Si l'URL ne s'ouvre pas, utilisez l'action Ouvrir dans le navigateur du port $PORT."
echo "Les exercices SELECT sont réalisés sur cette COPIE ; conservez boutique.sqlite inchangée."
echo "Pour arrêter Adminer : Ctrl+C dans ce terminal. Le mot de passe expirera."
echo

cd "$WEB"
php -S "127.0.0.1:$PORT" -t "$WEB"
