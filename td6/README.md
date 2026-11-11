# TD6 — Auditer des requêtes SQL avec Adminer

**BUT TC Toulon · 2 h · Suite de BUT-Boutique · Copilot = aide à vérifier, pas oracle**

**Outil commun : Adminer.** Au TD5, vous avez observé la base interne de WordPress via **Playground → Dev Tools → Database → Adminer** (`wp_posts`). Au TD6, vous utiliserez **Adminer dans Codespaces** avec une autre base SQLite, cette fois commerciale. Ce sont deux bases différentes et indépendantes, pas une base WordPress avec des commandes.

## Démarrer en trois étapes

**Dans le dépôt étudiant** `CultureNumTC-Etudiants`, les dossiers `td5` et `td6` sont directement à la racine : **il n'y a pas de dossier `student-kit`**. Si vous êtes déjà dans `td6`, utilisez `python3 generer_base.py` et `bash demarrer_adminer.sh` au lieu des chemins relatifs ci-dessous. Le script de création ne doit être lancé qu'une fois par base.

1. Depuis la racine du Codespace, dans un premier terminal, créer la base depuis le CSV fictif du TD5 :

   ```bash
   python3 td6/generer_base.py
   ```

   Ce script n'écrase jamais `td6/boutique.sqlite` : si le fichier existe déjà, conservez-le.

2. Dans un **second terminal**, démarrer Adminer :

   ```bash
   bash td6/demarrer_adminer.sh
   ```

   Le lancement crée si besoin une copie non destructive `td6/boutique_adminer.sqlite`, télécharge Adminer et génère un **code temporaire à huit chiffres**. Il crée aussi `td6/ACCES_ADMINER.txt`, fichier privé temporaire à ouvrir directement dans VS Code, sur ordinateur comme sur tablette, pour retrouver et copier le code. Si la copie SQLite existe déjà, elle n'est pas écrasée.

3. Dans l'onglet **Ports** de Codespaces, ouvrir le **port 8765**, en vérifiant impérativement que la visibilité reste **Private**. Dans Adminer, le formulaire indique déjà **SQLite 3** et **boutique_adminer.sqlite** : **aucun identifiant ni long chemin à recopier**. Il suffit de saisir le **code à huit chiffres** lu dans le terminal, ou dans `td6/ACCES_ADMINER.txt` ouvert dans l'éditeur VS Code. **Cette méthode est recommandée sur tous les appareils**, et pas seulement sur tablette. En cas d'erreur de code, un message clair apparaît ; SQLite lui-même ne gère pas de mots de passe. Après connexion, vérifiez les tables `Clients`, `Produits`, `Commandes` et `LignesCommande`.

   Si PHP ou son pilote SQLite est absent, effectuer **Codespaces → Rebuild Container** pour installer les dépendances du cours, puis relancer la commande. S'il est impossible de télécharger Adminer, signaler le message d'erreur à l'enseignant, sans publier le port ni désactiver les contrôles de sécurité.

**Important :** n'ouvrez jamais le port en mode Public, ne partagez pas le code et arrêtez le serveur avec `Ctrl+C` en fin de séance. Le fichier `ACCES_ADMINER.txt` sera supprimé à l'arrêt et ignoré par Git. Ne copiez pas le code dans un rapport ni dans le chat. Le répertoire HTTP d'Adminer est temporaire et séparé des fichiers `.sqlite`. La base initiale est préservée pour permettre des comparaisons fiables.

## Exécuter une requête

Dans Adminer, ouvrez la base et son onglet **SQL** (ou *Commande SQL*). Essayez séparément :

```sql
SELECT id_client, nom FROM Clients LIMIT 5;
```

```sql
SELECT id_commande, id_client FROM Commandes LIMIT 5;
```

Vérifiez que la base affichée est `boutique_adminer.sqlite`. L'onglet SQL remplace les commandes `python3 -m sqlite3` du prototype : **le terminal sert uniquement à créer la base et lancer Adminer**.

## Exercices à documenter dans `rapport-td6.md`

1. **Schéma :** repérez clés primaires et étrangères dans Adminer et dans `generer_base.py`. Proposez un `CREATE TABLE` simplifié avec PK ; expliquez pourquoi l'adresse d'Alice est stockée une seule fois.
2. **Observations :** inspectez les quatre tables. Copiez au moins un résultat réel de `SELECT` dans le rapport et expliquez comment `JOIN` relie commandes et clients.
3. **Audit de trois requêtes d'IA :** ouvrez `requetes_a_auditer.sql`. Prédisez chaque résultat **avant** exécution, puis copiez chaque proposition individuellement dans **Adminer → SQL**. Testez la confusion ET/OU, la condition impossible et le `COUNT(*)` non discriminant.
4. **Requête corrigée :** recherchez les clients ayant acheté **Mug BUT ET T-shirt Code**, éventuellement sur deux commandes différentes. Testez le cas d'Hugo Martin, qui a acheté plusieurs mugs et aucun T-shirt. Une requête qui s'exécute sans erreur n'est pas forcément juste.
5. **Retour au contrôle historique :** produisez une requête `SELECT` pour le chiffre d'affaires d'Alice et confrontez-la au calcul du TD5. Analysez le changement d'adresse et l'effet d'un `DELETE` sur un produit référencé.

## Modifications facultatives et précautions

Pour `INSERT INTO`, `UPDATE` et `DELETE`, utilisez **uniquement la copie `boutique_adminer.sqlite` ouverte dans Adminer**, pas `boutique.sqlite`. Avec les clés étrangères actives, la suppression d'un produit référencé peut être refusée. N'exécutez pas d'instructions SQL provenant d'un inconnu. Les données sont fictives ; ne publiez ni base, ni rapport, ni port dans GitHub public.

En fin de TD, conservez `rapport-td6.md`, votre requête corrigée et, si nécessaire, votre copie modifiée. **Aucun correcteur SQL public n'est actif** ; un éventuel correcteur futur utiliserait un environnement isolé et des données fictives.
