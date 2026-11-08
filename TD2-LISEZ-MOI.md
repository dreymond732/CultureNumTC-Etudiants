# TD2 — Lire le HTML produit par une IA, puis le modifier

Ce dossier du dépôt étudiant accompagne le **TD2 de Culture numérique TC S5**. Les consignes complètes et les questions se trouvent sur le portail pédagogique, page TD2.

## Objectifs
- Demander à Copilot une page **pédagogique** expliquant quelques balises HTML, avec commentaires dans le code.
- Observer les balises et la coloration syntaxique dans l’éditeur, puis le rendu de cette page depuis le serveur HTTP de Codespaces.
- Modifier **personnellement** `td2/but-boutique.html` : titre, contenus de produits, image `images/mug.svg`, tableau et lien relatif.
- Tester `curl -I`, le résultat HTTP et un chemin d’image cassé volontairement.

## Avant de commencer
1. **Conservez une copie de votre rapport TD1** si vous l’avez déjà réalisé. N’effacez pas un Codespace contenant votre travail.
2. Assurez-vous que le dossier `td2/` et `rapport-td2.md` sont visibles dans votre Codespace. Si ce n’est pas le cas, demandez au professeur comment actualiser l’espace. Une nouvelle création de Codespace depuis le dépôt GitHub étudiant à jour est possible, après sauvegarde du TD1.
3. Ouvrez `rapport-td2.md` dans l’éditeur et complétez-le au fur et à mesure.

## Avec Copilot (si disponible)
Sélectionnez le profil `Tuteur TD2` dans la discussion Copilot, puis suivez la consigne du premier exercice sur le portail. Vous recevrez du code HTML dans la conversation : **créez vous-même le fichier `td2/guide-html.html` et collez uniquement le code**. Une balise HTML et un commentaire ne sont pas la même chose.

**Sans Copilot :** ouvrez `td2/guide-html-sans-copilot.html`, créez une copie sous le nom `td2/guide-html.html` et complétez vous-même les commentaires demandés dans le TD.

## Voir votre page dans le navigateur
Depuis le terminal à la racine du projet :
```bash
cd td2
pwd
ls
python3 -m http.server 8000 --bind 0.0.0.0
```
Si `pwd` indique déjà le dossier `td2`, ne répétez pas `cd td2`.
Dans l’onglet **Ports**, ouvrez le port `8000` en gardant sa visibilité **privée**, puis consultez `guide-html.html` ou `but-boutique.html`.

Dans un autre terminal (serveur toujours actif) :
```bash
curl -I http://127.0.0.1:8000/guide-html.html
curl -I http://127.0.0.1:8000/introuvable.html
```
Une fois les tests terminés, revenez au premier terminal et arrêtez le serveur avec `Ctrl+C`.

## À conserver / déposer
- `td2/guide-html.html` : page d’apprentissage, pas destinée au correcteur ;
- `rapport-td2.md` : vos observations et explications, à conserver ;
- `td2/but-boutique.html` : **seul document HTML destiné au correcteur formatif TD2**, si celui-ci est ouvert par l’enseignant.

Le correcteur vérifie la présence de structures HTML, pas toute leur pertinence. N’ajoutez aucun nom, numéro étudiant, groupe ou secret dans les fichiers pédagogiques ou dans Copilot. Ne publiez jamais votre rapport dans le dépôt GitHub public.
