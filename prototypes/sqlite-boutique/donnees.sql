-- Données synthétiques : huit codes, aucun nom ni adresse personnelle réelle.
INSERT INTO clients VALUES
 (1,'Client A','Toulon'),(2,'Client B','La Garde'),
 (3,'Client C','Hyères'),(4,'Client D','La Seyne'),
 (5,'Client E','Toulon'),(6,'Client F','Hyères'),
 (7,'Client G','La Garde'),(8,'Client H','Toulon');
INSERT INTO produits VALUES
 (1,'Mug BUT',1250),(2,'T-shirt Code',2500),(3,'Sac tissu',850);
INSERT INTO commandes VALUES
 (101,1,'2026-10-01'),(102,1,'2026-10-08'),
 (103,2,'2026-10-02'),(104,3,'2026-10-03'),
 (105,4,'2026-10-04'),(106,5,'2026-10-05'),
 (107,6,'2026-10-06'),(108,6,'2026-10-07'),
 (109,7,'2026-10-09'),(110,7,'2026-10-10'),
 (111,5,'2026-10-11');
INSERT INTO lignes_commande VALUES
 (101,1,1,1250),(102,2,1,2500),
 (103,1,1,1250),(104,2,1,2500),
 (105,3,1,850),(106,1,1,1250),(106,2,1,2500),
 (107,1,3,1250),(108,1,2,1250),
 (109,1,1,1250),(110,3,1,850),
 (111,3,1,850);
