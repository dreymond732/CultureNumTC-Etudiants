# BUT TC Toulon — Culture numérique S5

Bienvenue dans le Codespace du cours de **BUT Techniques de commercialisation, Toulon**. GitHub a copié automatiquement ici les fichiers de départ des TD. Vous pouvez les modifier dans votre espace personnel ; ils ne sont pas automatiquement publiés.

## Où trouver les activités ?

- **TD1** — [Mode d'emploi](td1/README.md), rapport `td1/rapport-td1.md`, fichiers d'exemples et terminal réseau simulé.
- **TD2** — [Mode d'emploi](td2/README.md), rapport `td2/rapport-td2.md`, pages HTML de BUT-Boutique.
- **TD4** — **Évaluation intermédiaire sur 20 points** : [Consignes pratiques](td4/README.md), rapport `td4/rapport-td4.md`, frise `td4/site-a/histoire-web.html` à modifier et page `td4/site-b/index.html` à laisser intacte.

Les énoncés complets, le barème et les informations de remise figurent sur le **portail pédagogique CultureNumTC**.

## Première ouverture de Codespaces

Vous pouvez vous connecter à GitHub avec votre compte existant (ou vous inscrire, notamment avec Google si proposé). Ouvrez le dépôt public `dreymond732/CultureNumTC-Etudiants`, choisissez **Code → Codespaces → Create codespace on main** ou utilisez https://codespaces.new/dreymond732/CultureNumTC-Etudiants. La première préparation peut prendre plusieurs minutes. Si la plateforme demande de faire confiance au dépôt, vérifiez son nom et validez **Oui / Trust**.

Dans Codespaces, ouvrez les dossiers à gauche (Explorateur), les fichiers au centre (éditeur) et le terminal avec **Terminal → New Terminal**. Le volet « Créer avec des assistants » est facultatif : les profils **Tuteur TD1 et TD2** existent déjà, donc **ne lancez pas `/create-agent`**. Vous pourrez mettre l'éditeur en français avec `Ctrl+Shift+P` → **Configure Display Language** → `fr`. Le clavier de votre appareil et les messages en anglais du terminal Linux sont deux sujets distincts.

## Quel dossier est servi par le navigateur ?

Au TD1, vous avez affiché le terminal réseau simulé avec un serveur privé :

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

Au **TD4**, vous exécuterez deux instances simultanées depuis **deux terminaux et deux dossiers différents** :

```bash
cd td4/site-a
python3 -m http.server 8000 --bind 0.0.0.0
```

Dans le second terminal Codespaces, depuis la racine du projet :

```bash
cd td4/site-b
python3 -m http.server 8001 --bind 0.0.0.0
```

Dans l'onglet **Ports**, les deux ports 8000 et 8001 doivent rester **Private**. Pour arrêter chaque serveur, revenez à son terminal et tapez `Ctrl+C`. Les étapes détaillées et les commandes GET/POST figurent dans le **TD4** du portail.

## Conserver vos réponses sans Git

**Nous n'utilisons pas les outils Git pour ces premiers TD.** Le dépôt de départ est public et appartient à l'enseignant. Ne faites pas de *push* ou de *fork* public avec vos réponses. Les fichiers modifiés dans votre Codespace ne sont pas automatiquement publiés sur GitHub.

Pour retrouver votre travail, reprenez le **même Codespace** depuis https://github.com/codespaces. Celui-ci peut être supprimé après une période d'inactivité : téléchargez une copie locale de vos rapports et pages importantes. Pour arrêter votre Codespace : **… → Stop codespace** sur cette page.

**Vie privée :** ne mettez aucun nom, prénom, numéro étudiant, groupe, mot de passe ou jeton dans les fichiers de travail ni dans Copilot. Pendant l'évaluation intermédiaire du TD4, aucune assistance IA n'est autorisée.
