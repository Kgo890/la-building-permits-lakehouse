INTERNAL_CONFIG = [
    {
        "API_URL": "https://data.lacity.org/api/v3/views/qyra-qm2s/query.csv",
        "DELTA_TABLE_NAME": "bronze.la_parcels",
        "limit" : 5000,
        "offset" : 0,
        "order" : "id"
    },
    {
        "API_URL": "https://data.lacity.org/api/v3/views/pi9x-tg5x/query.csv",
        "DELTA_TABLE_NAME": "bronze.la_building_permits",
        "limit" : 5000,
        "offset" : 0,
        "order" : "permit_nbr"
    }
]