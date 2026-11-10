-- Requêtes fictives proposées par une IA.
-- À examiner, SANS considérer qu'elles sont toutes correctes.
-- Question métier : quels clients ont acheté à la fois un Mug BUT ET un T-shirt Code ?

-- A. Sélectionne les clients ayant acheté AU MOINS UN des deux produits.
SELECT DISTINCT c.code_client
FROM clients c JOIN commandes co ON co.id_client=c.id_client
JOIN lignes_commande l ON l.id_commande=co.id_commande
JOIN produits p ON p.id_produit=l.id_produit
WHERE p.libelle IN ('Mug BUT', 'T-shirt Code')
ORDER BY c.code_client;

-- B. Demande aux deux libellés d'être vrais SUR LA MÊME ligne de produit.
SELECT DISTINCT c.code_client
FROM clients c JOIN commandes co ON co.id_client=c.id_client
JOIN lignes_commande l ON l.id_commande=co.id_commande
JOIN produits p ON p.id_produit=l.id_produit
WHERE p.libelle='Mug BUT' AND p.libelle='T-shirt Code'
ORDER BY c.code_client;

-- C. Confond le nombre de lignes de commandes avec le nombre de produits distincts.
SELECT c.code_client
FROM clients c JOIN commandes co ON co.id_client=c.id_client
JOIN lignes_commande l ON l.id_commande=co.id_commande
GROUP BY c.id_client
HAVING COUNT(*) >= 2
ORDER BY c.code_client;

-- Travail attendu dans la future séquence TD6 :
-- 1. Prévoir les résultats de chaque requête avant exécution.
-- 2. Exécuter sur la base synthétique, comparer avec les attentes.
-- 3. Produire un contre-exemple qui met en évidence une fausse réponse.
-- La requête de référence (solution) reste dans le dépôt enseignant privé.
