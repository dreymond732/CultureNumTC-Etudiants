# TD3 — CSS : diagnostiquer BUT-Boutique et une frise de l'histoire du Web

**BUT TC Toulon · 2 heures · Travail guidé, IA possible pour expliquer mais pas pour remplacer les observations.**

Vous avez construit une page HTML de BUT-Boutique au TD2. Avant l'évaluation individuelle du TD4, vous allez **diagnostiquer et corriger des comportements CSS réels** sur deux pages de départ, sans réécrire leurs contenus : une boutique et une frise historique inspirée de l'exercice de l'enseignant. Ce ne sont **pas** les fichiers du contrôle TD4 : les tâches et les sélecteurs sont différents.

## Les fichiers à utiliser

- `but-boutique.html` et `css/boutique.css` : catalogue fictif, avec trois fiches et plusieurs défauts de présentation **intentionnels** ; l'image `images/mug.svg` vient du TD2.
- `frise-web.html` et `css/frise.css` : sept étapes historiques (World Wide Web, Mosaic, JavaScript, CSS, Wikipédia, WordPress, AJAX) et une présentation à analyser.
- `js/aide-selecteur.js` : aide interactive pour **tester des sélecteurs** dans la frise. Le nombre d'éléments ciblés est affiché, mais l'outil ne corrige aucun style.
- `rapport-td3.md` : observations avant/après et justifications à remplir **au fur et à mesure**.

**Ne modifiez pas les fichiers `td2/` ou `td4/`.** Travaillez dans `td3/`. Gardez le HTML, les sept événements, les trois produits, les liens, la navigation et l'aide aux sélecteurs intacts. Les corrections doivent être apportées **dans les deux fichiers CSS**. Évitez `!important` et les styles directement sur les balises HTML : le but est de comprendre la cascade, pas de masquer les symptômes.

## Ouvrir les deux pages (10 min)

Depuis la racine du Codespace étudiant :

```bash
cd td3
python3 -m http.server 8000 --bind 0.0.0.0
```

Dans l'onglet **Ports** de Codespaces, ouvrez le port **8000 en visibilité Private**. Consultez `but-boutique.html`, puis `frise-web.html`. Si le port 8000 est déjà utilisé, arrêtez le serveur du TD2 avec `Ctrl+C` avant de recommencer. N'ouvrez pas la boutique à travers WordPress : ici, nous diagnostiquons le CSS de **fichiers statiques**.

## Enquête 1 — Ce que ciblent réellement les sélecteurs (15 min)

1. Comparez le HTML et la feuille CSS de la boutique : quels rôles jouent `h1`, `.produit`, `#promo` et `a:hover` ? Une classe peut-elle concerner plusieurs fiches ?
2. Dans `frise-web.html`, utilisez l'**Aide-Sélecteur CSS** pour tester au moins quatre sélecteurs différents : un nom de balise, une classe, un identifiant et un sélecteur combiné. Notez pour chacun le nombre d'éléments trouvés. En cas de sélecteur invalide, observez le message de l'outil.
3. Avant de corriger, décrivez **deux symptômes** visibles dans chaque page (boutique et frise). Distinguez la règle CSS suspectée de l'élément HTML qui devrait être ciblé.

## Enquête 2 — Réparer le catalogue sans dommages collatéraux (30 min)

Les fiches de la boutique doivent être distinctes, l'offre mise en valeur **uniquement sur le Mug**, et les liens d'action utilisables au repos, au survol et au clavier.

1. Diagnostiquez pourquoi les styles de fiche ne produisent pas l'effet attendu. Corrigez le **sélecteur réellement en cause**, pas toutes les fiches HTML.
2. Faites ressortir l'offre du Mug, **sans modifier l'apparence des deux autres fiches**. Vérifiez le résultat sur les trois produits, et notez votre contre-exemple (« ce qui ne doit pas changer »).
3. Rendez les liens d'action lisibles dans **trois états** : normal, survol et focus clavier (`Tab`). Justifiez les couleurs et l'indication de focus choisies. Une simple suppression du lien n'est pas une correction.
4. Dans la boutique, choisissez un **sélecteur d'élément** ciblant un titre pertinent (par exemple `h2`) et ajustez **deux propriétés CSS** de manière lisible. Expliquez en quoi sa portée est différente de `.produit` et `#promo` : le résultat ne doit pas dégrader les titres des fiches.

Pour chaque réparation, renseignez dans le rapport : **symptôme → hypothèse → règle trouvée → modification ciblée → preuve avant/après**. Une modification globale qui casse un autre produit n'est pas une réponse valide.

## Enquête 3 — Réparer la frise sans toucher aux événements (30 min)

1. Comparez le rendu de deux événements portant la classe `evenement--jalon` avec les autres. En consultant `css/frise.css` et les règles réellement appliquées, expliquez pourquoi une déclaration peut être présente sans produire l'effet visuel prévu. Corrigez ce conflit de **cascade/spécificité** sans utiliser `!important`.
2. Donnez une présentation identifiable, mais lisible, aux **deux événements** marqués `evenement--publication`, sans affecter les cinq autres.
3. Vérifiez l'apparence des liens **au clavier** (touche `Tab`) et au survol. Le focus doit être clairement visible, même sans souris. Conservez l'aide aux sélecteurs, ses messages et les sept événements.
4. Expliquez l'effet de `:nth-child(even)` sur l'alternance des cartes ; le résultat doit rester compréhensible lorsque la mise en page se réorganise.

## Enquête 4 — Test sur deux largeurs d'écran (25 min)

Comparez les deux pages sur une fenêtre **large (environ 1100 px)** et **étroite (environ 375–400 px)**. Utilisez les outils de développement du navigateur lorsqu'ils sont disponibles, ou le redimensionnement de l'aperçu. Vous n'avez pas besoin d'un téléphone physique.

1. Relevez **ce qui déborde horizontalement** dans chaque page au départ : une mise en page peut paraître acceptable sur ordinateur et rester inutilisable sur écran étroit.
2. Corrigez les règles pertinentes dans les deux fichiers CSS. Le catalogue doit rester lisible, et la frise ne doit ni exiger un défilement horizontal de la page ni cacher les dates. Les sept événements doivent conserver leur **ordre chronologique**.
3. Vérifiez également que les liens, les fiches et le panneau d'aide restent accessibles au clavier et sur écran étroit. Enregistrez une comparaison grand/petit écran pour **chaque** page dans le rapport.

## Bilan — Réutiliser sans reproduire un corrigé (10 min)

Dans `rapport-td3.md`, rassemblez **au moins six diagnostics distincts** répartis sur les deux pages : nom du sélecteur, symptôme, correction CSS, preuve et effet secondaire éventuellement évité. Expliquez en trois à cinq phrases comment le TD2 (HTML), le TD3 (CSS) et le TD4 (évaluation) s'enchaînent. Les réponses vagues (« j'ai changé les couleurs ») ne sont pas des preuves.

**À conserver :** `but-boutique.html`, `frise-web.html`, `css/boutique.css`, `css/frise.css` et `rapport-td3.md`. Aucun dépôt public de vos réponses. Il n'y a pas encore de notation automatique de ce TD : les exercices et leurs critères sont d'abord validés pédagogiquement.

**À ne pas faire :** modifier le HTML pour contourner une erreur de sélecteur, supprimer une fiche ou un événement, copier le fichier du contrôle TD4, désactiver le focus, injecter `!important` pour résoudre toutes les difficultés, rendre le port 8000 public ou laisser croire qu'une réponse de Copilot équivaut à un test réel.
