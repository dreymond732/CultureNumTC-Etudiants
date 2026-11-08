# Pilotes expérimentaux — passage au CMS et aux bases de données

Ce répertoire contient **deux démonstrateurs**, destinés d'abord à une relecture enseignante. Il ne remplace pas les TD5 et TD6 actuellement disponibles sur le portail.

## Prototype 1 — WordPress Playground et thème BUT-Boutique

- [Blueprint de démarrage](but-boutique-wp/blueprint.json)
- [Guide du démonstrateur](but-boutique-wp/README.md)
- [Thème à blocs BUT-Boutique](but-boutique-wp/theme-but-boutique/)

Lien de lancement expérimental :

https://playground.wordpress.net/?blueprint-url=https%3A%2F%2Fraw.githubusercontent.com%2Fdreymond732%2FCultureNumTC-Etudiants%2Fprototype%2Ftd5-playground-td6-sqlite%2Fprototypes%2Fbut-boutique-wp%2Fblueprint.json

Le Blueprint importe le thème directement depuis ce dépôt GitHub public, puis crée les pages dans la base interne de WordPress. Le thème contient le **modèle**, mais pas les prix des produits. Après modification d'une page, explorer **Files** et **Database** dans Playground. Les travaux personnels ne sont pas envoyés automatiquement à GitHub.

## Prototype 2 — modèle relationnel BUT-Boutique dans Codespaces

- [Guide SQLite](sqlite-boutique/README.md)
- [Schéma des quatre tables](sqlite-boutique/schema.sql)
- [Données de démonstration](sqlite-boutique/donnees.sql)
- [Trois propositions SQL à auditer](sqlite-boutique/requetes_a_auditer.sql)

Pour les essais dans Codespaces (un clone contenant cette branche) :

```bash
python3 prototypes/sqlite-boutique/preparer.py
python3 prototypes/sqlite-boutique/explorer.py produits
python3 -m sqlite3 prototypes/sqlite-boutique/boutique.sqlite "SELECT code_client FROM clients;"
```

**Cette base métier n'est pas celle de WordPress**. Elle comporte des commandes fictives, des clés primaires/étrangères et des contre-exemples aux erreurs SQL classiques.

## Conditions du prototype

- Aucune modification des TD5 et TD6 publics, aucun correcteur activé, aucune action sur le serveur pédagogique.
- Aucun nom, numéro étudiant ni transaction réelle. Ne pas demander aux étudiants de pousser leurs réponses sur le dépôt GitHub public.
- Vérifications automatiques (CI dépôt enseignant) : JSON, thèmes, syntaxe PHP si disponible, fixture SQLite, clés et cas négatifs.
- **Reste à réaliser** : ouvrir le Blueprint sur un ordinateur et une tablette, vérifier l'activation du thème, la modification de contenu, les variations de style, l'inspection de la base WordPress et l'export ZIP.

Voir l'avis pédagogique enseignant dans le dépôt privé `docs/pedagogy/PROTOTYPE_TD5_WORDPRESS_TD6_SQLITE.md`.
