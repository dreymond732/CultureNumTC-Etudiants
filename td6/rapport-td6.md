# TD6 — Vérifier des requêtes SQL proposées par une IA

## Exercice 1 — Le schéma
- Tables retrouvées :
- Clé primaire de Clients :
- Clé étrangère de Commandes :
- Rôle de LignesCommande :
- Ma proposition de commande `CREATE TABLE` simplifiée pour une table, avec clé primaire :
- Avantage pour le changement d'adresse d'Alice Martin :

## Exercice 2 — Observer des données
- Exemple d'une ligne de Clients :
- Exemple d'une ligne de Commandes :
- Exemple d'une ligne de LignesCommande :
- Quelle jointure relie le nom d'un client à sa commande ?

## Exercice 3 — Auditer trois propositions
| Requête proposée | Ma prédiction avant exécution | Résultat observé | Est-ce la bonne réponse métier ? Justification |
| --- | --- | --- | --- |
| A | | | |
| B | | | |
| C | | | |

## Exercice 4 — Une requête corrigée et un contre-exemple
- Code SQL proposé (vous pouvez l'écrire dans un fichier à part) :
- Résultat observé :
- Cas Hugo Martin (deux achats de Mug, aucun T-shirt) :
- Pourquoi le résultat est-il discriminant ?
- Une suggestion de Copilot que j'ai vérifiée plutôt que de recopier :

## Exercice 5 — Chiffre d'affaires
- Montant calculé pour Alice Martin :
- Colonnes et jointures utilisées :
- Pourquoi ne pas simplement compter les lignes de commandes ?

## Pour aller plus loin — modifications SQL sur une copie
- Mon `INSERT INTO` de commande C012 et de ligne associée :
- Mon `UPDATE` de l'adresse client et sa vérification SELECT :
- Ce qui se passe pour un `DELETE` du produit P02 encore référencé :
- Pourquoi la contrainte FK est-elle utile :

## Bilan
- La différence entre le SQL syntaxiquement correct et la réponse correcte pour la question métier :
- Différence entre la base SQLite commerciale et wp_posts de WordPress :
