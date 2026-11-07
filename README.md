# TD1 — Mon appareil, Internet et le Web

Bienvenue dans votre espace de travail **GitHub Codespaces**. Il contient les documents nécessaires au TD1 de Culture numérique (BUT3 TC). Vous n'avez pas besoin d'installer Linux, Python ou un serveur Web sur votre appareil.

## Deux environnements indispensables
- **POSTE LOCAL :** votre ordinateur Windows/macOS/Linux, ou celui d'un voisin si vous avez une tablette. Les manipulations locales, notamment les commandes réseau, sont obligatoires.
- **CODESPACES :** un ordinateur Linux distant, accessible depuis votre navigateur. Vous y disposez de fichiers, d'un éditeur, d'un terminal et éventuellement de Copilot. Ses fichiers et son réseau sont **différents de ceux de votre poste local**.

Avec Wix, ces aspects techniques sont habituellement gérés par le service. Ici, vous apprenez à les observer.

## Comment accéder à Codespaces ?
1. Créez un compte personnel sur https://github.com/signup si nécessaire, puis connectez-vous.
2. Ouvrez le dépôt https://github.com/dreymond732/CultureNumTC-Etudiants.
3. Cliquez sur **Code → Codespaces → Create codespace on main** ou sur https://codespaces.new/dreymond732/CultureNumTC-Etudiants.
4. Attendez l'ouverture de l'éditeur. À gauche se trouvent les fichiers ; ouvrez un terminal avec **Terminal → New Terminal**.
5. Si l'éditeur est en anglais, ouvrez la palette (`Ctrl+Shift+P`) puis **Configure Display Language → fr** et rechargez.

**À ouvrir en premier : `rapport-td1.md`. Toutes vos réponses aux exercices sont à rédiger dans ce fichier pendant le TD, pas seulement à la fin.** Il est écrit en Markdown : `##` commence une rubrique ; `- ` une ligne de liste. Ouvrez ensuite `frise-histoire-web.html` lorsqu'une consigne vous le demande.

## Quels autres fichiers sont présents ?
- `frise-histoire-web.html` : page HTML de départ, à voir dans l'éditeur et le navigateur ;
- `donnees/a-lire.txt` et `donnees/produits.csv` : exemples de fichiers ;
- `traces/exemples-reseau.txt` : sorties **fictives** pour apprendre à interpréter les commandes réseau si elles sont bloquées sur le poste local ;
- `.github/agents/tuteur-td1.agent.md` : aide Copilot en français, uniquement si votre compte permet d'utiliser Copilot.

## Deux commandes spécifiques de Codespaces
Pour regarder votre dossier :
```bash
pwd
ls
```

Pour démarrer un serveur HTTP, depuis le dossier contenant la frise :
```bash
python3 -m http.server 8000 --bind 0.0.0.0
```
Ouvrez ensuite **Ports → 8000 → Open in Browser**. Le port doit rester **privé**. Arrêtez le serveur avec `Ctrl+C`.

Les commandes `ping`, `nslookup` et `tracert` / `traceroute` sont étudiées **sur le poste local**. Ne les lancez pas dans Codespaces pour l'exercice réseau : le réseau distant peut les bloquer et il ne représente pas celui de votre ordinateur.

## Fin de séance
Téléchargez une copie de `rapport-td1.md` : clic droit sur le fichier dans l'Explorateur Codespaces → **Download / Télécharger**. Arrêtez ensuite votre Codespace depuis votre compte GitHub pour économiser le quota.

**Vie privée :** aucun nom, numéro étudiant, mot de passe ou jeton ne doit être renseigné dans les fichiers d'exemple ou dans Copilot. Ne créez pas de compte payant ni de moyen de paiement pour réaliser ce TD ; en cas de blocage, demandez une aide à l'enseignant.

Pour retrouver toutes les consignes et le dessin explicatif, ouvrez le **portail pédagogique CultureNumTC**, section « Découvrir Codespaces ».
