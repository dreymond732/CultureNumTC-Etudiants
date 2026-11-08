# BUT TC Toulon — Culture numérique S5

Bienvenue dans l’espace de travail des **étudiants du BUT Techniques de commercialisation de Toulon**. GitHub a copié automatiquement dans votre Codespace les documents de départ du cours ; vous pouvez les modifier dans votre propre espace de travail.

## Retrouvez vos exercices

- **TD1 :** ouvrez [le mode d’emploi du TD1](td1/README.md), puis **`td1/rapport-td1.md`** pour rédiger vos réponses au fil de la séance. Les fichiers HTML, les données et le terminal réseau simulé sont rangés sous `td1/`.
- **TD2 :** ouvrez [le mode d’emploi du TD2](td2/README.md), puis **`td2/rapport-td2.md`**. Les pages HTML de BUT-Boutique et les images sont dans `td2/`.

Les consignes détaillées et les quiz sont disponibles sur le **portail pédagogique CultureNumTC**.

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
