# BUT TC Toulon — TD1 : mon appareil, Internet et le Web

Bienvenue dans votre **Codespace personnel**, un ordinateur Linux distant ouvert dans le navigateur. Il contient un éditeur de texte, des fichiers, un terminal et une aide IA facultative (Copilot).

## Formation Codespaces — à faire avant les exercices

Sur la page d’accueil **CultureNumTC**, ouvrez la rubrique « **Formation Codespaces** ». Elle explique avec un dessin votre appareil, Internet, votre compte GitHub et votre machine Codespaces.

1. Créez un compte personnel sur https://github.com/signup si nécessaire ; choisissez **Continuer avec Google** si cette possibilité vous est proposée, ou utilisez votre adresse courriel. Vous pouvez aussi simplement vous connecter à un compte existant.
2. Ouvrez le **dépôt étudiant public** https://github.com/dreymond732/CultureNumTC-Etudiants.
3. Cliquez **Code → Codespaces → Create codespace on main**, ou suivez https://codespaces.new/dreymond732/CultureNumTC-Etudiants. **Les fichiers du dépôt de départ sont automatiquement copiés** dans votre Codespace : inutile de les télécharger et de les transférer un par un. La première mise en place peut prendre **plusieurs minutes**. Si GitHub ou VS Code demande de **faire confiance au contenu**, vérifiez qu’il s’agit du dépôt officiel **dreymond732/CultureNumTC-Etudiants** (BUT TC Toulon), puis choisissez **Oui / Trust**.
4. Si l’écran affiche **Recovery Mode**, il s’agit d’un problème de préparation technique de l’environnement. Prévenez l’enseignant, sans essayer de commandes système aléatoires. Identifiez ensuite l’**Explorateur** de fichiers à gauche, l’**éditeur** au centre et le menu **Terminal → New Terminal**. Pour mettre l’interface en français : `Ctrl+Shift+P` puis **Configure Display Language → fr**.
5. **Ouvrez d’abord `rapport-td1.md`**. Écrivez une phrase dans la rubrique « Avant de commencer », puis sauvegardez si nécessaire (`Ctrl+S` ou `Cmd+S`). Vous rédigerez **toutes vos réponses** dans ce même fichier au fil du TD1.
6. Ouvrez `frise-histoire-web.html`, puis un terminal ; tapez `pwd` pour obtenir le dossier courant.
7. **N’utilisez pas `/create-agent`** : le tuteur du cours est déjà dans `.github/agents/tuteur-td1.agent.md`. Le volet « Créer avec des assistants » est un conseil générique de VS Code. Si vous souhaitez le masquer : **Affichage → Apparence → Barre latérale secondaire** (Windows/Linux : `Ctrl+Alt+B`). Pour accéder au tuteur plus tard, ouvrez **Copilot Chat**, puis choisissez **Tuteur TD1** dans le sélecteur d’agents en bas de la conversation, si Copilot est accessible avec votre compte.
8. **Langue et clavier :** `Configure Display Language → fr` change l’interface de l’éditeur ; les messages du terminal Linux peuvent rester en anglais. Le clavier dépend de votre appareil et de votre navigateur, pas d’un réglage clavier à imposer sur la machine distante. Si AZERTY est interprété comme QWERTY, contrôlez d’abord la disposition de saisie locale, puis essayez les caractères dans l’éditeur et le terminal.

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

**Non public par défaut :** vos modifications dans votre Codespace personnel, dont votre `rapport-td1.md`, tant que vous ne les publiez pas sur GitHub. Le formulaire de dépôt des travaux est différent des ressources publiques. **Ne publiez pas votre rapport dans un dépôt public.**

Ne renseignez ni nom, prénom, numéro étudiant, groupe, téléphone, mot de passe, ni jeton dans les fichiers d’exercice ou les demandes à Copilot. Si Codespaces demande un paiement, ne payez pas : prévenez l’enseignant.

## Où sont mes fichiers et comment conserver mon travail ?

Au départ, le contenu du dépôt GitHub public est copié dans votre espace personnel, généralement dans `/workspaces/CultureNumTC-Etudiants/`. Les fichiers que vous modifiez dans ce dossier ne sont **pas publiés automatiquement** sur GitHub.

**En arrêtant le Codespace, vous ne perdez pas les fichiers enregistrés dans ce dossier.** Pour la séance suivante, reprenez le **même Codespace**, depuis https://github.com/codespaces. Les modifications du dépôt public réalisées après votre création n'arrivent toutefois pas automatiquement dans un Codespace déjà existant : préservez vos productions avant toute mise à jour.

Un Codespace arrêté depuis longtemps peut être supprimé automatiquement (par défaut après 30 jours d'inactivité, selon les réglages GitHub). **Téléchargez des copies** de vos documents de travail pour ne pas les perdre.

## En fin de TD

Dans l’Explorateur Codespaces, clic droit sur `rapport-td1.md` → **Download / Télécharger** pour conserver une copie sur votre appareil.

**Pour arrêter votre Codespace :** ouvrez https://github.com/codespaces, puis **… → Stop codespace / Arrêter le codespace** à droite de votre machine. **Fermer seulement l'onglet ne l'arrête pas.**

## Que faire si la création affiche « Recovery Mode » ?
La configuration de départ a déjà rencontré un problème de signature du dépôt Yarn lors d’une installation supplémentaire inutile. Si cela se reproduit, conservez le journal d’erreur et informez l’enseignant. La réparation documentée consiste à corriger `.devcontainer/Dockerfile`, puis à utiliser la palette de commandes **Codespaces: Rebuild Container**. Pour une première création sans travail personnel, vous pouvez aussi supprimer le Codespace défaillant et le recréer **après publication du correctif**. Ne supprimez jamais un Codespace contenant vos réponses sans les sauvegarder.
