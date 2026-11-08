# BUT TC Toulon — Culture numérique S5

Bienvenue dans l’espace de travail des **étudiants du BUT Techniques de commercialisation de Toulon**. GitHub a copié automatiquement dans votre Codespace les documents de départ du cours ; vous pouvez les modifier dans votre propre espace de travail.

## Retrouvez vos exercices

- **TD1 :** ouvrez [le mode d’emploi du TD1](td1/README.md), puis **`td1/rapport-td1.md`** pour rédiger vos réponses au fil de la séance. Les fichiers HTML, les données et le terminal réseau simulé sont rangés sous `td1/`.
- **TD2 :** ouvrez [le mode d’emploi du TD2](td2/README.md), puis **`td2/rapport-td2.md`**. Les pages HTML de BUT-Boutique et les images sont dans `td2/`.

1. Créez un compte personnel sur https://github.com/signup si nécessaire ; choisissez **Continuer avec Google** si cette possibilité vous est proposée, ou utilisez votre adresse courriel. Vous pouvez aussi simplement vous connecter à un compte existant.
2. Ouvrez le **dépôt étudiant public** https://github.com/dreymond732/CultureNumTC-Etudiants.
3. Cliquez **Code → Codespaces → Create codespace on main**, ou suivez https://codespaces.new/dreymond732/CultureNumTC-Etudiants. **Les fichiers du dépôt de départ sont automatiquement copiés** dans votre Codespace : inutile de les télécharger et de les transférer un par un. La première mise en place peut prendre **plusieurs minutes**. Si GitHub ou VS Code demande de **faire confiance au contenu**, vérifiez qu’il s’agit du dépôt officiel **dreymond732/CultureNumTC-Etudiants** (BUT TC Toulon), puis choisissez **Oui / Trust**.
4. Si l’écran affiche **Recovery Mode**, il s’agit d’un problème de préparation technique de l’environnement. Prévenez l’enseignant, sans essayer de commandes système aléatoires. Identifiez ensuite l’**Explorateur** de fichiers à gauche, l’**éditeur** au centre et le menu **Terminal → New Terminal**. Pour mettre l’interface en français : `Ctrl+Shift+P` puis **Configure Display Language → fr**.
5. **Ouvrez d’abord `rapport-td1.md`**. Écrivez une phrase dans la rubrique « Avant de commencer », puis sauvegardez si nécessaire (`Ctrl+S` ou `Cmd+S`). Vous rédigerez **toutes vos réponses** dans ce même fichier au fil du TD1.
6. Ouvrez `frise-histoire-web.html`, puis un terminal ; tapez `pwd` pour obtenir le dossier courant.
7. **N’utilisez pas `/create-agent`** : le tuteur du cours est déjà dans `.github/agents/tuteur-td1.agent.md`. Le volet « Créer avec des assistants » est un conseil générique de VS Code. Si vous souhaitez le masquer : **Affichage → Apparence → Barre latérale secondaire** (Windows/Linux : `Ctrl+Alt+B`). Pour accéder au tuteur plus tard, ouvrez **Copilot Chat**, puis choisissez **Tuteur TD1** dans le sélecteur d’agents en bas de la conversation, si Copilot est accessible avec votre compte.
8. **Langue et clavier :** `Configure Display Language → fr` change l’interface de l’éditeur ; les messages du terminal Linux peuvent rester en anglais. Le clavier dépend de votre appareil et de votre navigateur, pas d’un réglage clavier à imposer sur la machine distante. Si AZERTY est interprété comme QWERTY, contrôlez d’abord la disposition de saisie locale, puis essayez les caractères dans l’éditeur et le terminal.

## Une page Web privée dans votre navigateur

Au TD1, vous afficherez le terminal réseau simulé à l’aide d’un petit serveur Web. Depuis le terminal Codespaces, à la **racine du projet** (`pwd` et `ls` permettent de vérifier), saisissez :

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

Dans l’onglet **Ports**, vérifiez que `8000` est **Private**, puis ouvrez-le dans le navigateur. Parcourez le dossier `td1` jusqu’au fichier `terminal-reseau.html`. **Cette page simule des commandes : elle ne mesure pas le réseau.** Pour arrêter le serveur, revenez au terminal et utilisez `Ctrl+C`.

## Sauvegarder sans publier vos réponses

**Nous n’utilisons pas les outils Git pour ces premiers TD.** Le dépôt de départ GitHub est public et appartient à l’enseignant. Ne faites pas de `push` ou de `fork` public avec vos réponses. La modification d’un fichier dans votre Codespace n’est pas automatiquement publiée.

Pour retrouver les fichiers enregistrés, reprenez le **même Codespace** depuis https://github.com/codespaces. Il peut toutefois être supprimé après une période d’inactivité : **téléchargez une copie locale** de vos travaux importants. Pour arrêter votre Codespace : `… → Stop codespace` dans cette page.

Copilot est facultatif. Les profils **Tuteur TD1** et **Tuteur TD2** sont déjà disponibles dans `.github/agents/` si votre compte autorise leur utilisation : inutile de lancer `/create-agent`.

**Vie privée :** n’inscrivez pas vos nom, prénom, numéro étudiant, groupe, téléphone, mot de passe ou jeton dans ces fichiers ou dans Copilot.
