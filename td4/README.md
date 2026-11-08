# TD4 — Évaluation intermédiaire : HTML, CSS et client–serveur

**BUT TC Toulon, semestre 5 · Durée : 2 heures · Travail individuel · /20**

Le TD4 est une **évaluation intermédiaire** des compétences travaillées aux TD1, TD2 et TD3. Contrairement aux exercices guidés précédents, les transformations demandées doivent être réalisées **sans assistance IA/Copilot**.

## Fichiers de départ
- `td4/site-a/histoire-web.html` : **votre production à modifier**. Contient une frise historique, des blocs CSS à compléter et un panneau « Aide-sélecteur CSS » déjà prêt.
- `td4/site-a/images/mosaic.svg` : illustration locale disponible pour une image HTML.
- `td4/site-b/index.html` : seconde page de démonstration, à **laisser intacte**. Elle ne doit pas contenir la frise.
- `td4/rapport-td4.md` : relevé de vos observations. Remplissez-le au fil du contrôle.

Ne saisissez pas de nom, prénom, numéro étudiant ou groupe dans ces fichiers. L'identification sera effectuée lors de la remise, si elle est activée par l'enseignant. Le dépôt GitHub de départ est public et ne vous appartient pas : **n'utilisez pas les outils Git** pour publier vos réponses.

## Deux serveurs, chacun dans son dossier

Ouvrez **deux terminaux Codespaces distincts**. Depuis la racine du projet :

**Terminal A (dossier A, port 8000) :**
```bash
cd td4/site-a
pwd
ls
python3 -m http.server 8000 --bind 0.0.0.0
```

**Terminal B (dossier B, port 8001) :**
```bash
cd td4/site-b
pwd
ls
python3 -m http.server 8001 --bind 0.0.0.0
```

Dans l'onglet **Ports** de Codespaces, ouvrez les ports 8000 et 8001 dans le navigateur. **Les deux ports doivent rester Private.** Lisez attentivement le début et la fin de chaque adresse Web pour ne pas confondre les deux serveurs.

Sur le port **8000**, demandez `histoire-web.html` ; sur le port **8001**, demandez `index.html`, puis `histoire-web.html`. Comparez les réponses et les lignes nouvelles qui s'affichent dans le terminal de chacun des serveurs. Ne fermez pas les terminaux : ils affichent les **journaux HTTP** des requêtes.

## GET puis POST (sans écrire de serveur en Python)

Ouvrez un **troisième terminal** depuis le dossier du projet. Il servira à demander des pages, sans interrompre les deux serveurs.

Pour une vraie requête `GET` :
```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8000/histoire-web.html
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8001/histoire-web.html
```

Pour découvrir ce que répond un simple serveur de fichiers lorsqu'on lui envoie une requête `POST` :
```bash
curl -i -X POST -d 'essai=TC' http://127.0.0.1:8000/histoire-web.html
```

Il n'y a **aucune donnée personnelle** dans `essai=TC`. Le serveur Python utilisé ne possède pas de programme de réception et de traitement des formulaires : ne vous attendez pas à ce que votre saisie soit enregistrée. Notez **le code HTTP effectivement observé** et la nouvelle ligne du journal.

## Fin du contrôle
Arrêtez les deux serveurs avec `Ctrl+C` dans leurs terminaux. Téléchargez sur votre appareil une copie de `td4/site-a/histoire-web.html` et `td4/rapport-td4.md`. Ne publiez pas vos réponses sur GitHub ; l'enseignant indiquera le canal de remise.

Les consignes détaillées et le barème sont sur le portail CultureNumTC, dans **TD4 — Évaluation intermédiaire**.
