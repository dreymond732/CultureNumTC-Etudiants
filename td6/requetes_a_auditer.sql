-- BUT-Boutique · TD6 · Requêtes proposées par une IA pour analyse critique.
-- Ne les prenez pas comme des solutions. Consultez aussi votre résultat du tableur TD5.
-- QUESTION : quels clients ont acheté à la fois Mug BUT ET T-shirt Code ?

-- Proposition A : analyser la logique et le résultat avant de conclure.
SELECT DISTINCT c.nom
FROM Clients c JOIN Commandes co ON co.id_client=c.id_client
JOIN LignesCommande lc ON lc.id_commande=co.id_commande
JOIN Produits p ON p.id_produit=lc.id_produit
WHERE p.nom IN ('Mug BUT','T-shirt Code')
ORDER BY c.nom;

-- Proposition B : analyser la logique et le résultat avant de conclure.
SELECT DISTINCT c.nom
FROM Clients c JOIN Commandes co ON co.id_client=c.id_client
JOIN LignesCommande lc ON lc.id_commande=co.id_commande
JOIN Produits p ON p.id_produit=lc.id_produit
WHERE p.nom='Mug BUT' AND p.nom='T-shirt Code'
ORDER BY c.nom;

-- Proposition C : analyser la logique et le résultat avant de conclure.
SELECT c.nom
FROM Clients c JOIN Commandes co ON co.id_client=c.id_client
JOIN LignesCommande lc ON lc.id_commande=co.id_commande
GROUP BY c.id_client
HAVING COUNT(*)>=2
ORDER BY c.nom;
