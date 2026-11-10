# TD5 — Du CMS au tableur et aux bases de données

**BUT TC Toulon · Document de travail personnel**

N'indiquez ici aucun numéro étudiant, adresse réelle, mot de passe ou autre donnée personnelle. Ce rapport documente votre compréhension : ce n'est pas une liste de réponses à copier depuis une IA.

## Préparation — site et fichiers
- Navigateur utilisé et moyen d'ouverture du Blueprint :
- L'instance Playground a affiché le thème BUT-Boutique : oui / non / erreur observée :
- J'ai retrouvé dans Codespaces `td5/commandes_initiales.csv` :

## Exercice 1 — Site dynamique (WordPress)
- Titre d'une page visible sur le site :
- Différence observée entre affichage public et interface d'administration :
- Où le prix du mug apparaît-il dans l'interface d'édition ?
- Prix initial de la page Mug BUT :
- Prix après ma modification et vérification sur le site :
- Une limite de ce que ma modification permet de conclure :

## Exercice 2 — Modifier la présentation
- Couleur ou variation du thème modifiée :
- Ce qui a changé à l'écran :
- Ce qui n'a **pas** changé dans la description du mug :
- Un indice que le contenu n'est pas stocké directement dans un modèle HTML :

## Exercice 3 — Fichiers, PHP et base interne
- Dans Files, chemin du thème :
- Fichier modèle de page consulté :
- Rôle probable de `wp:post-content` :
- Dans Database → Adminer, table consultée :
- Filtre ou recherche pour retrouver la page Mug BUT :
- Champ `post_title` observé :
- Champ `post_content` : un extrait court (sans recopier toute la page) :
- Pourquoi l'édition du contenu ne nécessite-t-elle pas de modifier le modèle de page ?
- En quoi Adminer ou phpMyAdmin est-il différent du serveur de fichiers TD4 ?
- Je n'ai **pas modifié** les données directement via Adminer : oui / non :

## Exercice 4 — Sauvegarde
- Je suis passé par Playground → Export → Download as .zip :
- Nom du fichier ZIP téléchargé :
- Pourquoi un simple lien vers le Blueprint ne sauvegarde-t-il pas mes modifications ?
- Une précaution de confidentialité concernant l'archive ZIP :

## Exercice 5 — Retour au tableur de commandes
- Fichier de départ ouvert : `td5/commandes_initiales.csv`
- Fichier de travail distinct créé : `commandes_travail.csv` :
- **Ajouter une commande C012 à Bob Dupont** : valeurs recopiées (client, adresse, produit, quantité) :
- Risque si l'adresse ou le nom est mal saisi dans la nouvelle ligne :
- **Adresse fictive A → Adresse fictive Alice nouvelle** : combien de lignes existantes modifiées pour Alice ?
- Une erreur de mise à jour que j'ai volontairement cherchée et corrigée :
- **Supprimer le Sweat Info (P02) uniquement dans une copie de démonstration** : qu'arrive-t-il à la commande C002 ?
- Pourquoi une suppression de ligne peut-elle faire perdre une information sur le client ou sa commande ?
- Chiffre d'affaires d'Alice Martin avant l'ajout de la commande C012 (calcul et unité) :
- Clients ayant acheté **Mug BUT ET T-shirt Code** (avant C012) :
- Pourquoi deux achats de Mug BUT ne signifient-ils pas deux types de produits différents ?

## Exercice 6 — Vers le relationnel et le TD6
| Table proposée | Son identifiant unique (PK) | Ce qui la relie à une autre table (FK) |
| --- | --- | --- |
| Clients | | |
| Produits | | |
| Commandes | | |
| LignesCommande | | |

- Dans quelle table l'adresse du client serait-elle enregistrée une seule fois ?
- Quelle relation permet à une commande de contenir plusieurs produits ?
- En quoi le schéma de cette base commerciale diffère-t-il des tables `wp_posts` de WordPress ?
- Une question que j'aimerais faire vérifier par le tuteur IA, et la façon dont je contrôlerai sa réponse :

## Préparation au dépôt et à l'évaluation
- Fichiers que j'ai conservés : ZIP Playground, CSV de travail et ce rapport :
- Les informations contenues dans les fichiers ZIP peuvent-elles être publiques sans précaution ?
- Je n'ai pas publié mes fichiers de travail sur le dépôt GitHub public :
