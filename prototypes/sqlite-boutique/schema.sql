-- BUT-Boutique : jeu entièrement fictif, indépendant de la base interne WordPress.
PRAGMA foreign_keys = ON;
CREATE TABLE clients (
  id_client INTEGER PRIMARY KEY,
  code_client TEXT NOT NULL UNIQUE,
  ville TEXT NOT NULL
);
CREATE TABLE produits (
  id_produit INTEGER PRIMARY KEY,
  libelle TEXT NOT NULL UNIQUE,
  prix_centimes INTEGER NOT NULL CHECK (prix_centimes > 0)
);
CREATE TABLE commandes (
  id_commande INTEGER PRIMARY KEY,
  id_client INTEGER NOT NULL REFERENCES clients(id_client),
  date_commande TEXT NOT NULL
);
CREATE TABLE lignes_commande (
  id_commande INTEGER NOT NULL REFERENCES commandes(id_commande),
  id_produit INTEGER NOT NULL REFERENCES produits(id_produit),
  quantite INTEGER NOT NULL CHECK (quantite > 0),
  prix_unitaire_centimes INTEGER NOT NULL CHECK (prix_unitaire_centimes > 0),
  PRIMARY KEY (id_commande, id_produit)
);
CREATE INDEX idx_commandes_client ON commandes(id_client);
CREATE INDEX idx_lignes_produit ON lignes_commande(id_produit);
