# TD2 — Lire le HTML produit par une IA, puis le modifier

Le dossier `td2/` du dépôt étudiant accompagne le **TD2 de Culture numérique TC S5**. Les consignes complètes et les questions se trouvent sur le portail pédagogique, page TD2.

## Objectifs
- Demander à Copilot une page **pédagogique** expliquant quelques balises HTML, avec commentaires dans le code.
- Observer les balises et la coloration syntaxique dans l’éditeur, puis le rendu de cette page depuis le serveur HTTP de Codespaces.
- Modifier **personnellement** `td2/but-boutique.html` : titre, contenus de produits, image `images/mug.svg`, tableau et lien relatif.
- Tester `curl -I`, le résultat HTTP et un chemin d’image cassé volontairement.

## Avant de commencer
1. **Conservez une copie de votre rapport TD1** si vous l’avez déjà réalisé. N’effacez pas un Codespace contenant votre travail.
2. À sa création, Codespaces a copié automatiquement les fichiers du dépôt GitHub étudiant. Assurez-vous que le dossier `td2/` et `td2/rapport-td2.md` sont visibles dans votre Codespace. Si vous aviez créé le Codespace avant leur publication, ils ne s’ajoutent pas automatiquement : demandez au professeur comment actualiser l’espace **sans effacer vos réponses**.
3. Ouvrez `td2/rapport-td2.md` dans l’éditeur et complétez-le au fur et à mesure.

## Avec Copilot (si disponible)
Sélectionnez le profil `Tuteur TD2` dans la discussion Copilot, puis suivez la consigne du premier exercice sur le portail. Vous recevrez du code HTML dans la conversation : **créez vous-même le fichier `td2/guide-html.html` et collez uniquement le code**. Une balise HTML et un commentaire ne sont pas la même chose.

**Sans Copilot :** ouvrez `td2/guide-html-sans-copilot.html`, créez une copie sous le nom `td2/guide-html.html` et complétez vous-même les commentaires demandés dans le TD.

## Voir votre page dans le navigateur
La manipulation du serveur privé pour le simulateur TD1 vous a préparés à ce geste. Ici, vous utilisez le même serveur pour afficher **une page HTML que vous avez écrite ou modifiée**.
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
- `td2/rapport-td2.md` : vos observations et explications, à conserver ;
- `td2/but-boutique.html` : **seul document HTML destiné au correcteur formatif TD2**, si celui-ci est ouvert par l’enseignant.

Le correcteur vérifie la présence de structures HTML, pas toute leur pertinence. N’ajoutez aucun nom, numéro étudiant, groupe ou secret dans les fichiers pédagogiques ou dans Copilot. Ne publiez jamais votre rapport dans le dépôt GitHub public.

## Reprendre ou arrêter son Codespace
Les fichiers enregistrés dans le dossier de travail `/workspaces` sont conservés à l'arrêt, mais le Codespace peut être supprimé après une période d'inactivité (30 jours par défaut, selon les réglages). Téléchargez vos pages et votre rapport.

Pour reprendre ou arrêter la machine : https://github.com/codespaces → **… → Stop codespace**. La fermeture d'un onglet ne l'arrête pas. Dans le panneau **Ports**, le serveur TD2 doit rester en visibilité **Private** ; la visibilité **Public** partagerait la page avec quiconque dispose de l'URL.
