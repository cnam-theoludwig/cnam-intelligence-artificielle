# cnam-intelligence-artificielle

## À propos

Code réalisé dans le cadre de la formation [Ingénieur en Informatique et Systèmes d'Information (SI), CNAM](https://www.itii-alsace.fr/formations/informatique-et-systemes-dinformation-le-cnam/), pour le module Intelligence Artificielle (IA).

### Membres du groupe

[Théo LUDWIG](https://gitlab.com/theoludwig)

## Prérequis

- [Python](https://www.python.org/) v3.14.3
- [uv](https://docs.astral.sh)

## Installation

```sh
# Cloner le dépôt
git clone git@github.com:cnam-theoludwig/cnam-intelligence-artificielle.git

# Se déplacer dans le répertoire
cd cnam-intelligence-artificielle

# Installer les dépendances
uv sync
```
## Utilisation

```sh
# Lancer le projet
uv run main.py

# Format
uvx ruff format .

# Lint
uvx ruff check .

# Type-check
uvx ty check

# Tests (with coverage)
uv run pytest --cov
```
