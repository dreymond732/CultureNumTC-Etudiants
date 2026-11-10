# TD5 — Du site WordPress au tableur puis à la BDD

**BUT TC Toulon · 2 h · Activité guidée, IA autorisée pour expliquer, pas pour remplacer les observations**

La progression reprend les missions du document historique « Gestion des commandes de BUT-Boutique », en y ajoutant la comparaison entre un site statique et un CMS réellement opérationnel.

## Documents
- `rapport-td5.md` : réponses, observations et justifications.
- `commandes_initiales.csv` : jeu de commandes fictif, préparé pour les cinq missions historiques ; il ne contient ni coordonnées ni identités réelles.
- `commandes_travail.csv` : copie **à créer par vous** ; ne modifiez pas le fichier initial.
- `suppression-demo.csv` : seconde copie facultative pour observer ce que provoque la suppression d'une ligne portant le produit P02, sans détruire le jeu de travail.
- **Site WordPress** : <a href="https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Fdreymond732%2FCultureNumTC-Etudiants%2Fmain%2Fprototypes%2Fbut-boutique-wp%2Fblueprint.json">Ouvrir BUT-Boutique dans Playground</a>. Ce lien réinitialise le site initial et **ne contient pas vos modifications personnelles**.

## Parcours naturel dans Playground
1. Lancer le site, attendre son chargement. Ouvrir la page Mug BUT sur le site puis **Pages → Toutes les pages → Mug BUT → Modifier** dans `/wp-admin/`.
2. Remplacer dans la page les **deux occurrences** du prix fictif 12,50 € par 14,50 €, enregistrer (Mettre à jour), revenir au site et actualiser. Observer ce qui a changé.
3. Ouvrir **Apparence → Éditeur → Styles**, changer une couleur ou choisir « Nuit contrastée » et enregistrer. Observer que le contenu du Mug BUT demeure inchangé.
4. Dans la barre inférieure Playground, **Dev Tools → Files** (ou simplement Files selon l'interface). Repérer `wp-content/themes/theme-but-boutique/templates/page.html`, puis la mention `wp:post-content`. Ne modifiez pas ce fichier.
5. **Dev Tools → Database → Adminer**, table `wp_posts`. Chercher la ligne de la page Mug BUT, comparer `post_title` et `post_content`. **Consultation uniquement : aucune suppression ou modification directe de `wp_posts`.** phpMyAdmin est facultatif, pour comparer les interfaces : il ouvre la même base SQLite.
6. **Export → Download as .zip**. Télécharger l'archive complète du Playground **sur votre appareil**. Le ZIP inclut les fichiers et la base ; la modification du prix ne se trouve pas dans le lien de Blueprint original.

## Importer le CSV dans un tableur francophone

Le fichier utilise des **virgules entre les champs**, les guillemets sont rares et les prix sont au **format décimal avec un point** (ex. `12.50`). Lors de l'importation dans Excel, LibreOffice ou Google Sheets, précisez le séparateur `,` et vérifiez que `Prix_Unitaire` et `Quantite` sont bien des **nombres**. Si `12.50` apparaît comme du texte avec les paramètres français, convertissez explicitement la colonne numérique avant vos calculs. Gardez toujours le CSV initial intact.

## Les cinq missions historiques du tableur
1. **Ajout :** la commande `C004` est déjà utilisée dans les données initiales, comme dans le jeu de commandes complet historique. Utilisez donc **`C012`**, une nouvelle commande de **Bob Dupont**, pour **2 T-shirts Code** à **25,00 €** l'unité ; réécrivez les autres champs du client déjà présent.
2. **Mise à jour :** pour toutes les lignes d'Alice Martin, remplacez `Adresse fictive A` par `Adresse fictive Alice nouvelle`. Recomptez les cellules et vérifiez l'absence de valeurs contradictoires.
3. **Suppression :** sur une **copie distincte**, supprimez les lignes `P02` (Sweat Info). Qu'arrive-t-il à la commande `C002` ? Comparez avec la copie non supprimée.
4. **Calcul :** évaluez le chiffre d'affaires d'Alice Martin avec la règle `Prix_Unitaire × Quantite` pour chaque ligne, puis somme. Justifiez le résultat par une formule ou un détail de calcul.
5. **Intersection :** trouvez les clients ayant acheté **Mug BUT ET T-shirt Code**, y compris s'il s'agit de commandes séparées. Attention au piège du client qui a acheté deux fois le même produit.

Pour les personnes sur tablette, les fichiers CSV peuvent être consultés comme texte dans Codespaces ; un tableur accessible depuis le navigateur ou le poste d'un voisin facilite les filtres et calculs. Ne téléversez pas les réponses sur un GitHub public.

## Vers le TD6
Proposez `Clients`, `Produits`, `Commandes`, `LignesCommande` et leurs clés PK/FK. La base commerciale SQLite sera distincte de la base interne `wp_posts` de WordPress ; les anomalies du tableur seront reprises en SQL.

## Sauvegarde et tutorat
Copilot peut aider à comprendre un terme ou suggérer une méthode de vérification. Vérifiez toujours ses indications sur **votre propre Playground**, le ZIP ou les lignes du CSV. Ne lui fournissez aucun secret. Conservez le ZIP exporté, `commandes_travail.csv` et `rapport-td5.md` ; l'enseignant indiquera si et comment remettre ces trois fichiers. **Un outil de correction automatique expérimental est à valider avant une ouverture des dépôts.**
