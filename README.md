# TD1 — Codespaces étudiant

Ce kit contient uniquement les fichiers de travail et le tuteur destinés aux étudiants.
Le portail CultureNumTC présente les consignes complètes du TD.

## Pourquoi Codespaces ?
Il fournit un **ordinateur Linux distant dans votre navigateur**, avec un éditeur, un terminal et un serveur HTTP de démonstration. Il n'y a pas de Python ni de serveur à installer sur votre poste ou votre tablette. Avec Wix, ces composants sont habituellement gérés à votre place.

## Ouverture
1. Connectez-vous à GitHub, puis ouvrez le dépôt étudiant indiqué par votre enseignant.
2. Utilisez **Code → Codespaces → Create codespace on main**.
3. Dans Explorer, ouvrez `frise-histoire-web.html`. Ouvrez un terminal via **Terminal → New Terminal**.
4. Si l'éditeur reste en anglais : palette de commandes `Ctrl+Shift+P` → **Configure Display Language** → **fr**, puis rechargez.
5. Si votre compte dispose de Copilot, sélectionnez **Tuteur TD1** dans le choix des agents. Son utilisation est facultative.

## Repères
Dans le terminal distant, utilisez `pwd`, `ls`, `ping -c 4 127.0.0.1`, `nslookup example.org`, `traceroute example.org`.
Pour lancer le serveur HTTP, depuis le dossier contenant la frise :
```bash
python3 -m http.server 8000 --bind 0.0.0.0
```
Ouvrez sa prévisualisation depuis **Ports → 8000**, en gardant le port **privé**, puis arrêtez le serveur avec `Ctrl+C`.
Les commandes réseau peuvent échouer à cause de restrictions ICMP : voir `traces/exemples-reseau.txt` et ne pas confondre blocage et panne.

**Important :** un Codespace est distant ; ses fichiers et son réseau ne sont pas ceux de votre ordinateur.
Ne consignez aucun nom, numéro étudiant ou secret dans ces fichiers ou dans Copilot.
Arrêtez le Codespace à la fin du cours pour éviter de consommer inutilement votre quota.
