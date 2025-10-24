# PokePipeline — Version minimale (Core Requirements uniquement)

Ce projet implémente les **exigences principales** du challenge PokePipeline :
1. **Data Extraction** — récupérer des données de la PokeAPI ;
2. **Data Transformation & Mapping** — transformer les données pour une structure SQL ;
3. **Data Loading** — charger ces données dans une base SQL.

## Installation
1. Assurez-vous d'avoir **Python 3.10+** installé.
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3. Exécutez le pipeline :
```bash
python pipeline.py
```

## Description des choix de conception
- **Extraction** : utilisation de `requests` pour appeler l’API publique `https://pokeapi.co/api/v2/pokemon/{id}`.
- **Transformation** : simplification des réponses JSON (nom, taille, poids, types, abilities, stats).
- **Chargement** : stockage dans une base SQLite via SQLAlchemy.

## Hypothèses
- Aucune clé d'API n'est requise.
- L’exemple télécharge les 20 premiers Pokémon (ID 1–20).

## Améliorations possibles
- Gérer plus de Pokémon ou d’autres endpoints.
- Ajouter des tests et de la validation.
- Passer à PostgreSQL ou un autre SGBD.
