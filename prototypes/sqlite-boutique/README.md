# Prototype SQLite métier BUT-Boutique

**Prototype enseignant, non affecté aux TD5/TD6 officiels pour le moment.**

Cette base est **distincte de la base SQLite interne de WordPress Playground** : elle sert à apprendre les notions de clé primaire, clé étrangère, table de lignes de commande, jointure et vérification sémantique du SQL.

Données 100 % synthétiques : huit clients « Client A » à « Client H », trois produits (« Mug BUT », « T-shirt Code », « Sac tissu »), onze commandes et douze lignes de commande. Aucun client réel, pas d'information personnelle.

## Dans le terminal Codespaces

Depuis la racine du dépôt :
```bash
python3 prototypes/sqlite-boutique/preparer.py
python3 prototypes/sqlite-boutique/explorer.py clients
python3 prototypes/sqlite-boutique/explorer.py produits
python3 prototypes/sqlite-boutique/explorer.py commandes
python3 prototypes/sqlite-boutique/explorer.py lignes
```

Pour lire une vraie requête SQL depuis le shell Python 3.12 :
```bash
python3 -m sqlite3 prototypes/sqlite-boutique/boutique.sqlite "SELECT code_client, ville FROM clients;"
```

Le script ne remplace jamais silencieusement une base préexistante. Si `boutique.sqlite` existe déjà, l'étudiant doit la conserver ou choisir un autre fichier `--output`.

## Expérience métier

La question est : « Quels clients ont acheté **les deux produits** Mug BUT **et** T-shirt Code ? »

Ouvrez `requetes_a_auditer.sql` : trois propositions d'IA sont volontairement imparfaites. Décrivez leurs erreurs et les contre-exemples nécessaires. Ne prenez pas le fait qu'une requête **s'exécute sans erreur** comme preuve qu'elle répond à la question.

Pour un travail approfondi, discuter pourquoi « acheter deux mugs » n'équivaudra jamais à « avoir acheté un mug et un T-shirt ».

## Différence avec WordPress

WordPress conserve ses contenus éditoriaux dans ses propres tables (par exemple `wp_posts`) ; ce prototype modélise des **transactions commerciales** dans `clients`, `produits`, `commandes` et `lignes_commande`. Nous n'ajoutons donc pas une extension WooCommerce au CMS pendant l'apprentissage de la modélisation relationnelle.

## Sécurité

Cette base doit être exécutée dans le Codespace individuel, pas sur le serveur de correction public. `explorer.py` ne lance que des requêtes fixées à l'avance, en lecture seule. N'ajoutez pas de noms ou de numéros étudiants et ne publiez pas vos résultats personnels sur GitHub.
