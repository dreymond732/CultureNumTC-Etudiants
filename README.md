# TD1 — Mon appareil, Internet et le Web

Bienvenue dans votre **Codespace personnel**, un ordinateur Linux distant ouvert dans le navigateur. Il contient un éditeur de texte, des fichiers, un terminal et une aide IA facultative (Copilot).

## Formation Codespaces — à faire avant les exercices

Sur la page d’accueil **CultureNumTC**, ouvrez la rubrique « **Formation Codespaces** ». Elle explique avec un dessin votre appareil, Internet, votre compte GitHub et votre machine Codespaces.

1. Créez un compte personnel sur https://github.com/signup si nécessaire, puis connectez-vous.
2. Ouvrez le **dépôt étudiant public** https://github.com/dreymond732/CultureNumTC-Etudiants.
3. Cliquez **Code → Codespaces → Create codespace on main**, ou suivez https://codespaces.new/dreymond732/CultureNumTC-Etudiants.
4. Identifiez l’**Explorateur** de fichiers à gauche, l’**éditeur** au centre et le menu **Terminal → New Terminal**. Pour mettre l’interface en français : `Ctrl+Shift+P` puis **Configure Display Language → fr**.
5. **Ouvrez d’abord `rapport-td1.md`**. Écrivez une phrase dans la rubrique « Avant de commencer », puis sauvegardez si nécessaire (`Ctrl+S` ou `Cmd+S`). Vous rédigerez **toutes vos réponses** dans ce même fichier au fil du TD1.
6. Ouvrez `frise-histoire-web.html`, puis un terminal ; tapez `pwd` pour obtenir le dossier courant.
7. Si vous avez accès à Copilot, repérez le profil **Tuteur TD1**.

**Le profil *Tuteur TD1* peut vous aider à interpréter un résultat. Il vous questionne mais n'est pas censé faire le TD à votre place : les compétences visées sont humaines et au programme TC.**

## Deux environnements obligatoires au TD1

- **Poste local :** votre ordinateur Windows/macOS/Linux, ou celui d’un voisin si vous avez une tablette. Les commandes de diagnostic réseau (`ping`, `nslookup`, `tracert`/`traceroute`) se font sur cet ordinateur.
- **Codespaces :** votre machine distante, pour l’éditeur, le rapport Markdown, les commandes de fichiers et les transferts. Le **serveur Web et `curl`** sont introduits au **TD2**, pas au TD1.

## Les fichiers déjà présents

- `rapport-td1.md` : **votre document de réponses**, rédigé en Markdown (`##` pour un titre, `-` pour une liste).
- `frise-histoire-web.html` : page HTML pour comparer texte source et affichage.
- `donnees/a-lire.txt` et `donnees/produits.csv` : autres types de fichiers.
- `traces/exemples-reseau.txt` : sorties **fictives** pour comprendre les commandes réseau sur le poste local.
- `.github/agents/tuteur-td1.agent.md` : instructions du tuteur IA, s’il est disponible.

## Ce qui est public et ce qui ne l’est pas

**Public :** les ressources du portail CultureNumTC ; ce dépôt étudiant (README, frise, données d’exemple, modèles vierges) ; les informations de votre profil GitHub visibles selon vos réglages ; les fichiers que vous publiez dans un dépôt GitHub public.

**Non public par défaut :** vos modifications dans votre Codespace personnel, dont votre `rapport-td1.md`, tant que vous ne les publiez pas sur GitHub. Le formulaire de remise sur le NAS est distinct. **Ne publiez pas votre rapport dans un dépôt public.**

Ne renseignez ni nom, prénom, numéro étudiant, groupe, téléphone, mot de passe, ni jeton dans les fichiers d’exercice ou les demandes à Copilot. Si Codespaces demande un paiement, ne payez pas : prévenez l’enseignant.

## En fin de TD

Dans l’Explorateur Codespaces, clic droit sur `rapport-td1.md` → **Download / Télécharger** pour conserver une copie sur votre appareil. Puis arrêtez votre Codespace depuis GitHub pour préserver votre quota.
