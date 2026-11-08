# TD4 — Évaluation intermédiaire : HTML, CSS et deux serveurs

**BUT TC Toulon — S5 · Travail individuel · 2 heures · Barème /20**

**Ce fichier est votre relevé d'observations.** Vous devez produire personnellement les modifications HTML et CSS dans `td4/site-a/histoire-web.html`. N'utilisez pas Copilot, les agents IA ou Git pendant l'épreuve. Ne saisissez pas votre identité dans ce rapport ou dans les fichiers HTML : si la remise en ligne est activée, l'identification aura lieu dans le formulaire prévu.

## 0. Préparer la séance (10 min)
- Je retrouve les dossiers `td4/site-a/` et `td4/site-b/` :
- Le fichier HTML que je dois modifier :
- Le fichier HTML que je dois laisser intact :

## 1. Modifier la frise — HTML et CSS (50 min)
- La frise conserve-t-elle ses cinq événements d'origine ?
- Balise `meta name="description"` ajoutée (contenu sans donnée personnelle) :
- Image insérée avec `src` et `alt` :
- Tableau : nombre de lignes et de colonnes :
- Lien extérieur ajouté et URL utilisée :
- Sélecteur `h1` : deux propriétés CSS choisies et effet constaté :
- Sélecteur `.frise-item` : deux propriétés CSS choisies et effet constaté :
- Sélecteur `#creation-web` : deux propriétés CSS choisies et effet constaté :
- Sélecteur `a:hover` : deux propriétés CSS choisies et effet constaté :
- Aide-sélecteur : ce qui est surligné quand j'entre `.frise-item` :
- Une vérification de l'affichage sur écran étroit :

## 2. Deux serveurs : dossiers et ports (25 min)
| Serveur | Dossier réellement servi | Port | Page demandée dans le navigateur | Code HTTP | Ce que voit le navigateur |
| --- | --- | --- | --- | --- | --- |
| A | | 8000 | `histoire-web.html` | | |
| B | | 8001 | `index.html` | | |
| B | | 8001 | `histoire-web.html` | | |

- Terminal du serveur A : une ligne de journal observée pour `GET` :
- Terminal du serveur B : une ligne de journal observée pour `GET` :
- Pourquoi le serveur B ne trouve-t-il pas `histoire-web.html` alors que le serveur A la trouve ?
- Si je modifie le fichier sous `site-a/`, quelle page change à l'actualisation ? Pourquoi ?

## 3. HTTP : GET et POST (20 min)
- La méthode utilisée par le navigateur pour demander `histoire-web.html` :
- Code de la requête GET pour un fichier présent :
- Code de la requête GET pour un fichier absent :
- Commande `curl` utilisée pour observer GET :
- Code HTTP obtenu lors de l'envoi d'un POST de démonstration :
- Une ligne `POST` observée dans le journal du serveur :
- Pourquoi ce serveur de fichiers ne traite-t-il pas notre POST comme une saisie de formulaire ?
- Quel logiciel joue le rôle de client et quel logiciel celui de serveur ?

## 4. Bilan et copie (15 min)
- Pourquoi deux serveurs sur la même machine peuvent-ils répondre différemment à un même chemin relatif ?
- Un élément du HTML ou du CSS que j'ai contrôlé par une observation :
- J'ai arrêté les deux serveurs avec `Ctrl+C` :
- J'ai téléchargé une copie locale de `td4/site-a/histoire-web.html` et de ce rapport :

**La remise de ces deux fichiers sera précisée par l'enseignant.** Ne publiez pas ces documents sur le dépôt GitHub public.
