# Documentation des classes

- **SimpleEnergySensor**: Simule un capteur d’énergie domestique. Génère à chaque lecture des mesures synthétiques de `power_w`, `current_a`, `energy_kwh`, `temperature_c`, `gas_ppm` avec horodatage, et gère l’historique de facturation trimestriel (réinitialisation et sauvegarde des périodes).

- **AnomalyDetector**: Détecte des anomalies simples sur les mesures en comparant `power_w`, `temperature_c`, `gas_ppm` à des seuils (min/max) dérivés des moyennes et écarts-types. Retourne un dictionnaire des valeurs anormales avec `timestamp`, sinon `None`.

- **saveToMongoDB**: Persiste les lectures et anomalies dans MongoDB. Offre `save(data, anomalies)` pour insérer un enregistrement, `save_history(history)` pour stocker l’historique de facturation (avec `_id` = `date_start`), et `get_records(filter)` pour récupérer les documents.

## Génération des données et définition des anomalies

- Les mesures simulées suivent une loi normale (gaussienne) avec les paramètres définis dans `src/const.py` (`MEAN_*` et `STD_*`).
- Une anomalie est définie comme une valeur qui s’écarte de plus de 2 écarts-types du moyen: au-dessus de `mean + 2*std` ou en dessous de `mean - 2*std`.
