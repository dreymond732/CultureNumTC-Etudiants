# TD1–TD6 : environnement Codespaces réduit, sans image "universal".
# Le pilote du 10/11/2026 a échoué avec universal:2 : disque plein
# lors de l'extraction de torch/lib/libtorch_cpu.so.
# Debian 13 (Trixie) apporte Python 3 et PHP + SQLite sans piles IA.
FROM mcr.microsoft.com/devcontainers/base:trixie

# Installation ciblée depuis les dépôts Debian (pas de dépôt Yarn ajouté).
# Tout est installé en une couche, avec purge du cache APT.
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 php-cli php-sqlite3 curl; \
    python3 -c 'import csv, decimal, sqlite3'; \
    php -r 'exit(extension_loaded("pdo_sqlite") ? 0 : 1);'; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*
