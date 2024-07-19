# API pour Accéder aux Données de PostgreSQL

## Installation des Dépendances

```bash
pip install -r requirements.txt
```

## Lancement de l'API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Utilisation

### Endpoint pour Récupérer des Données

- **GET** `/data`

### Paramètres de Requête

- `table_name`: Le nom de la table à interroger.
- `start_date`: La date de départ des données à récupérer (format: `YYYY-MM-DD`).
- `end_date`: La date de fin des données à récupérer (format: `YYYY-MM-DD`).
# API_PMU
