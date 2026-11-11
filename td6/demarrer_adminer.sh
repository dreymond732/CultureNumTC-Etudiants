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

# Adminer est servi dans un répertoire temporaire distinct des bases SQLite.
# Une authentification propre à l'interface est nécessaire : SQLite n'a pas de mot de passe.
# Le code à 8 chiffres est facile à saisir sur tout appareil ; Codespaces port 8765
# doit rester PRIVATE (GitHub authentifie déjà l'accès à ce port).
TMP="$(mktemp -d)"
chmod 700 "$TMP"
WEB="$TMP/www"
mkdir -p "$WEB"
ACCES="$ROOT/td6/ACCES_ADMINER.txt"
trap 'rm -f -- "$ACCES"; rm -rf -- "$TMP"' EXIT

echo "Téléchargement HTTPS d'Adminer officiel (version figée $VERSION)..."
curl --fail --silent --show-error --location --retry 2 \
  "https://www.adminer.org/static/download/$VERSION/adminer-$VERSION-sqlite.php" \
  -o "$WEB/index.php"

# Le code d'accès ne constitue PAS un mot de passe SQLite.
# Le plugin vérifie le code, puis fournit une chaîne vide au pilote SQLite.
# Ainsi, un code erroné n'est pas transmis à SQLite et le message d'erreur
# est explicite, plutôt que « La base de données ne supporte pas les mots de passe ».
CODE="$(python3 -c 'import secrets; print(f"{secrets.randbelow(100_000_000):08d}")')"
HASH="$(php -r 'echo password_hash($argv[1], PASSWORD_DEFAULT);' "$CODE")"
printf '%s' "$HASH" > "$TMP/pin.hash"
printf '%s' "$COPIE" > "$TMP/database.path"
chmod 600 "$TMP/pin.hash" "$TMP/database.path"

cat > "$WEB/adminer-plugins.php" <<'PHP'
<?php
/** Accès pédagogique TD6 : un seul fichier SQLite, un code court.
 * Configuration privée générée lors du lancement du serveur Codespaces.
 */
class TD6AdminerAccess extends \Adminer\Plugin {
    private string $hash;
    private string $db;

    function __construct(string $hash, string $db) {
        $this->hash = $hash;
        $this->db = $db;
    }

    function credentials(): array {
        // La base SQLite n'accepte aucun mot de passe.
        return array(\Adminer\SERVER, "", "");
    }

    function login($login, $password) {
        return password_verify((string) $password, $this->hash)
            ? true
            : "Code TD6 incorrect : recopiez les 8 chiffres affichés dans Codespaces.";
    }

    function database(): ?string {
        return $this->db;
    }

    function loginFormField($name, $heading, $value): string {
        if ($name === "driver") {
            return '<tr><th>Système<td>SQLite 3<input type="hidden" name="auth[driver]" value="sqlite">' . "\n";
        }
        if ($name === "server") {
            return '<input type="hidden" name="auth[server]" value="">' . "\n";
        }
        if ($name === "username") {
            return '<input type="hidden" name="auth[username]" value="">' . "\n";
        }
        if ($name === "password") {
            return '<tr><th>Code TD6<td><input type="password" name="auth[password]" inputmode="numeric" pattern="[0-9]{8}" minlength="8" maxlength="8" autocomplete="off" required autofocus>' . "\n";
        }
        if ($name === "db") {
            return '<tr><th>Base<td>boutique_adminer.sqlite<input type="hidden" name="auth[db]" value="' . htmlspecialchars($this->db, ENT_QUOTES, "UTF-8") . '">' . "\n";
        }
        return $heading . $value . "\n";
    }
}
$base = dirname(__DIR__);
$hash = file_get_contents($base . "/pin.hash");
$db = file_get_contents($base . "/database.path");
if ($hash === false || $db === false) {
    throw new RuntimeException("Configuration TD6 absente.");
}
return array(new TD6AdminerAccess($hash, $db));
PHP
chmod 600 "$WEB/adminer-plugins.php"
php -l "$WEB/adminer-plugins.php" >/dev/null

# Un fichier d'accès temporaire est pratique dans l'éditeur VS Code, sur tout appareil :
# on peut ouvrir ce fichier et sélectionner le code sans parcourir le terminal.
# Il est ignoré par Git et supprimé à l'arrêt (Ctrl+C).
umask 077
cat > "$ACCES" <<TXT
TD6 — ADMINER SQLITE
====================
CODE À SAISIR : $CODE

Ouvrez l'onglet Ports (8765, visibilité PRIVATE), puis Adminer.
Le formulaire contient déjà SQLite 3 et la copie boutique_adminer.sqlite.
Seul le code à 8 chiffres est à saisir. Aucun utilisateur ni chemin de base.

Ce code est temporaire. Ne le publiez pas et ne partagez pas le port.
TXT
chmod 600 "$ACCES"

echo
echo "==============================================================="
echo "TD6 — Adminer sur le port $PORT (visibilité PRIVATE impérative)"
echo "Code à 8 chiffres : $CODE"
echo "OUVREZ td6/ACCES_ADMINER.txt dans VS Code pour retrouver le code."
echo "Le formulaire Adminer contient déjà la base et le système SQLite."
echo "La copie boutique_adminer.sqlite est préservée à chaque relancement."
echo "Ctrl+C pour arrêter le serveur et supprimer le fichier de code."
echo "==============================================================="
echo

cd "$WEB"
php -S "127.0.0.1:$PORT" -t "$WEB"
