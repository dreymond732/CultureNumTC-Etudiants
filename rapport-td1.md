# TD1 — Mon appareil, Internet et le Web
Ce fichier sert à noter **mes réponses au fur et à mesure**. Ne pas y renseigner de nom, prénom, numéro étudiant, groupe, mot de passe ou jeton. Le rapport reste dans mon Codespace personnel tant que je ne le publie pas sur GitHub.

## Avant de commencer — formation Codespaces
- J'ai ouvert mon Codespace depuis GitHub :
- J'ai repéré l'Explorateur, l'éditeur et le terminal :
- J'ai ouvert ce rapport et rédigé une phrase :
- Je distingue le dépôt public de mon Codespace personnel :
- Pour les commandes locales, j'utilise mon ordinateur ou celui du voisin si tablette :

## Exercice 1 — Les outils que j'utilise déjà
Compléter avec mes propres mots la colonne de droite ; le premier exemple est fourni.

| Exemple | Ce que c'est | À quoi cela sert-il ? |
| --- | --- | --- |
| Windows / macOS | Système d'exploitation | Faire fonctionner l'appareil et lancer les applications. |
| Firefox / Chrome | Navigateur | |
| Google Search | Moteur de recherche | |
| GitHub Codespaces | Service donnant accès à une machine distante | Permet de créer, modifier et tester des fichiers de code. Leur publication sur GitHub ou via un port Web est une action distincte. |
| frise-histoire-web.html | Fichier | |
| Internet | Réseau de réseaux | |
| Serveur Web | Logiciel qui répond aux demandes de pages | |

**Attention — public ou privé ?** Votre Codespace est personnel. Le dépôt de départ de BUT TC Toulon est public. Une page rendue accessible par un **port Web public** ou un fichier publié sur un **dépôt GitHub public** peut être consulté par d’autres. Ne publiez pas vos rapports ni de données personnelles.

### Mon usage de Wix
1. Je vois directement les fichiers HTML de mon CV (oui/non) :
2. J'écris des commandes dans un terminal pour publier mon CV (oui/non) :
3. Je démarre un serveur Web moi-même (oui/non) :
4. Wix permet la publication sans transférer soi-même le HTML (oui/non) :
5. Une différence concrète entre Wix et Codespaces :

## Exercice 2 — Retrouver et ouvrir un fichier
- Poste local (ordinateur ou celui du voisin) : dossier où le fichier a été téléchargé :
- Dans le navigateur, je vois :
- Dans un éditeur de texte brut, je vois :
- Dans Codespaces, je repère ces balises :
- Le fichier a-t-il changé ? Ce qui explique la différence d'affichage :

## Exercice 3 — Le terminal donne des instructions à l'OS
- POSTE LOCAL : commande `pwd`, ce que j'obtiens :
- POSTE LOCAL : commande `dir` ou `ls`, ce que je vois :
- CODESPACES : commande `pwd`, ce que j'obtiens :
- CODESPACES : commande `ls`, ce que je vois :
- CODESPACES : effet de `cd donnees`, puis de `cd ..` :

## Exercice 4 — Diagnostics réseau sur le POSTE LOCAL
- Commande `ping 127.0.0.1` : observation (ou erreur) :
- Commande `ping example.org` : observation (ou erreur) :
- Commande `nslookup example.org` : observation (ou erreur) :
- Commande `tracert` ou `traceroute example.org` : observation (ou erreur) :
- Pourquoi `ping 127.0.0.1` ne prouve-t-il pas que l'accès Internet fonctionne ?
- À quoi sert `nslookup` ?
- Que peuvent montrer les étapes du trajet réseau ?
- Pourquoi un `ping` sans réponse ne prouve-t-il pas que le Web est coupé ?

## Exercice 5 — Transfert entre le poste local et Codespaces
- Fichier créé sur le poste local :
- Comment je l'ai envoyé vers Codespaces :
- Ce que j'ai vérifié dans l'éditeur Codespaces :
- Fichiers déjà présents dans le dossier `donnees` :
- Comment j'ai téléchargé mon fichier depuis Codespaces vers le poste local :
- Pourquoi un fichier présent dans Codespaces n'est-il pas automatiquement dans mes Téléchargements ?

## Exercice 6 — Distinguer un fichier local et une page Web
- Début de l'adresse de la frise téléchargée : `file:` ou autre :
- Début de l'adresse de la frise sur le portail : `https:` ou autre :
- Ce que les deux présentations ont en commun :
- Quelle est la différence entre les deux origines du document ?
- Quel logiciel est le client pour la page du portail ?
- Que se passe-t-il pour une adresse de document inexistant ?
- Au TD2, que permettront le serveur Codespaces et `curl` ?

## Exercice 7 — Deux mini-diagnostics
Choisir deux situations du TD, ne remplir que les deux lignes ci-dessous.

| Situation choisie | Mon hypothèse | Le test que je ferais | Ce que j'en déduirais et les limites |
| --- | --- | --- | --- |
| Première situation : | | | |
| Seconde situation : | | | |

## Bilan personnel
- Une chose que je comprends mieux maintenant :
- Une chose que je voudrais revoir :
