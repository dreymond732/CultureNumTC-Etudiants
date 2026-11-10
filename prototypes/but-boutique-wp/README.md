# Prototype BUT-Boutique sous WordPress Playground

**État : prototype de validation, pas un TD5 officiellement publié.** Le projet est une boutique *fictive* du BUT TC Toulon ; aucun compte client, paiement ou commande réelle.

## Ouvrir le site

Vous pouvez ouvrir ce Blueprint avec :
[WordPress Playground — BUT-Boutique](https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Fdreymond732%2FCultureNumTC-Etudiants%2Fprototype%2Ftd5-playground-td6-sqlite%2Fprototypes%2Fbut-boutique-wp%2Fblueprint.json).

Ou ouvrez https://playground.wordpress.net/ puis **Open New → Blueprint URL**, et indiquez ce chemin public :
`https://raw.githubusercontent.com/dreymond732/CultureNumTC-Etudiants/main/prototypes/but-boutique-wp/blueprint.json`.

Le Blueprint installe automatiquement le thème BUT-Boutique depuis la **branche publique de prototype sur GitHub**, puis crée quatre pages de contenu dans la base WordPress.

## Quatre observations à réaliser

1. **Contenu** : Pages → Toutes les pages → Mug BUT → Modifier. Changer le montant fictif de 12,50 € en 14,50 €, enregistrer, puis voir le site. Aucun fichier du thème n'a été modifié.
2. **Modèle de présentation** : Apparence → Éditeur → Styles. Modifier des couleurs ou choisir la variation « Nuit contrastée ». Vérifier que le titre et le nouveau prix restent identiques, tandis que l'apparence change.
3. **Fichiers** : dans le panneau Playground, ouvrir **Files**, repérer `wp-content/themes/theme-but-boutique/templates/page.html` et `theme.json`. Le modèle HTML contient `wp:post-content`, et non le prix du mug.
4. **Base** : ouvrir **Database** dans le panneau Playground ; chercher `wp_posts` et l'article/page « Mug BUT » ; voir le contenu révisé dans `post_content`. Attention : `wp_posts` contient aussi les pages, pas uniquement les articles.

## Limites

Playground exécute WordPress et PHP **dans le navigateur**, avec une base SQLite intégrée. Ce n'est ni le serveur Codespaces des TD1–TD4, ni un site commercial public hébergé sur Internet. Le lien de Blueprint **recrée les données initiales**, pas les modifications d'un étudiant. Pour conserver un travail : **Export → Download as .zip**. Les versions de WordPress/Playground et certaines interfaces peuvent changer.

Un thème WordPress ne s'obtient pas en renommant simplement une page HTML ; les fichiers `style.css`, `templates/index.html` et `theme.json` sont distincts. Le dépôt GitHub public héberge le **point de départ**, pas la sauvegarde privée des étudiants. Ne pas utiliser Git durant ce prototype.

## Pour l'enseignant

Tester sur ordinateur et tablette : création du site, activation du thème, présence des quatre pages, modification et persistance, variation du thème, inspection Database et export ZIP. **Aucune exécution navigateur complète n'est attestée à ce stade** ; les vérifications automatisées portent sur la syntaxe et la structure du Blueprint et du thème.

Références : https://developer.wordpress.org/playground/blueprints/steps/ et https://developer.wordpress.org/themes/core-concepts/theme-structure/
