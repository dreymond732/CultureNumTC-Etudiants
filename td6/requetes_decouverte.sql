-- TD6 · Requêtes de découverte : à exécuter UNE À UNE dans Adminer.
-- Chaque phrase « En français » décrit l'action de la requête.
-- Travail en lecture seule sur boutique_adminer.sqlite.
-- Ces huit exemples ne constituent PAS le corrigé des propositions d'IA A/B/C.

-- D1 — Lire une table.
-- En français : montre l'identifiant et le nom de cinq clients au maximum.
SELECT id_client, nom
FROM Clients
LIMIT 5;

-- D2 — Lire les références.
-- En français : montre cinq commandes et l'identifiant de leur client.
SELECT id_commande, id_client
FROM Commandes
LIMIT 5;

-- D3 — Relier une commande à un client.
-- En français : affiche le numéro, le nom du client et la date de C001.
SELECT
    Commandes.id_commande,
    Clients.nom,
    Commandes.date_commande
FROM Commandes
JOIN Clients
    ON Commandes.id_client = Clients.id_client
WHERE Commandes.id_commande = 'C001';

-- D4 — Retrouver toutes les commandes avec leurs clients.
-- En français : affiche chaque commande avec son client et sa date, triée par numéro.
SELECT
    Commandes.id_commande,
    Clients.nom,
    Commandes.date_commande
FROM Commandes
JOIN Clients
    ON Commandes.id_client = Clients.id_client
ORDER BY Commandes.id_commande;

-- D5 — Examiner les lignes d'une commande.
-- En français : liste les produits, quantités et prix de chaque ligne de C001.
SELECT
    id_commande,
    id_produit,
    quantite,
    prix_vente_centimes
FROM LignesCommande
WHERE id_commande = 'C001';

-- D6 — Remplacer un identifiant produit par un nom lisible.
-- En français : affiche les produits de C001 avec leur nom, quantité et prix en euros.
SELECT
    l.id_commande,
    p.nom AS produit,
    l.quantite,
    l.prix_vente_centimes / 100.0 AS prix_euros
FROM LignesCommande AS l
JOIN Produits AS p
    ON l.id_produit = p.id_produit
WHERE l.id_commande = 'C001';

-- D7 — Calculer le total d'une commande.
-- En français : additionne quantité × prix de chaque ligne de C001 (euros).
SELECT
    l.id_commande,
    SUM(l.quantite * l.prix_vente_centimes) / 100.0
        AS montant_total_euros
FROM LignesCommande AS l
WHERE l.id_commande = 'C001'
GROUP BY l.id_commande;

-- D8 — Calculer le chiffre d'affaires d'une cliente.
-- En français : additionne toutes les lignes de toutes les commandes d'Alice (euros).
SELECT
    c.nom,
    SUM(l.quantite * l.prix_vente_centimes) / 100.0
        AS chiffre_affaires_euros
FROM Clients AS c
JOIN Commandes AS co
    ON c.id_client = co.id_client
JOIN LignesCommande AS l
    ON co.id_commande = l.id_commande
WHERE c.nom = 'Alice Martin'
GROUP BY c.id_client, c.nom;
