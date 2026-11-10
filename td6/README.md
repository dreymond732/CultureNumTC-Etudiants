# TD6 — Lire et auditer SQL à partir du tableur du TD5

**BUT TC Toulon · Suite de l'étude BUT-Boutique · IA possible comme aide au raisonnement**

Au TD5, les prix et descriptions étaient des contenus WordPress, mais les commandes provenaient d'un CSV. Cette activité construit maintenant une **base relationnelle commerciale indépendante de WordPress** à partir du CSV fictif étudié.

## Préparer la base

Dans le terminal Codespaces, depuis la racine du dépôt :

```bash
python3 td6/generer_base.py
python3 -m sqlite3 td6/boutique.sqlite "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
```

Le fichier `td6/boutique.sqlite` contient les tables `Clients`, `Produits`, `Commandes` et `LignesCommande`. Le script ne remplace jamais une base existante. En cas de deuxième essai, choisissez une autre sortie `--output` et gardez votre première copie.

## Questions à étudier

1. Repérez les clés primaires et étrangères dans `generer_base.py`. Expliquez où se trouve l'adresse d'Alice Martin.
2. Dans le client SQLite de Codespaces, utilisez `SELECT` pour voir les trois premières lignes des tables et contrôler les relations. Les données ne sont pas issues de la base interne `wp_posts` de Playground.
3. Ouvrez `requetes_a_auditer.sql`. Pour chacune des **trois propositions d'IA**, décrivez d'abord le résultat attendu, puis exécutez-la et comparez avec les cas du TD5.
4. Demandez éventuellement à Copilot une quatrième requête qui sélectionne les clients ayant acheté **Mug BUT ET T-shirt Code**, même à des dates différentes. Testez-la sur plusieurs cas, notamment Hugo Martin qui a plusieurs achats de Mug BUT mais aucun T-shirt Code.
5. Imaginez une requête SQL pour calculer le chiffre d'affaires d'Alice Martin. Vérifiez qu'un même article acheté deux fois compte deux fois dans la somme.

## Sauvegarder et partager

Ne publiez pas la base, vos requêtes ni les rapports individuels sur le dépôt GitHub public. Enregistrez `rapport-td6.md` pendant le TD et téléchargez-le à la fin.

**Mode de correction futur :** un correcteur isolé pourra exécuter des requêtes `SELECT` autorisées sur des bases synthétiques de test, et comparer les résultats à un oracle non visible des étudiants. La présence d'une requête syntaxiquement valide ne suffit pas à prouver sa justesse.
