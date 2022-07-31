from src.common.dotenv import getenv

# CSV con gli indirizzi delle scuole e i rispettivi codici meccanografici,
# preso dall'OpenData del MIUR
scuole_miur_csv_file = "storage/scuole-miur.csv"

# Database sqlite da creare a partire dal CSV delle scuole del MIUR
scuole_miur_sqlite_file = "storage/scuole-miur.sqlite"

# Schema del database delle scuole del MIUR
scuole_miur_schema = {
    "anno_scolastico": "varchar(255)",
    "area_geografica": "varchar(255)",
    "regione": "varchar(255)",
    "provincia": "varchar(255)",
    "codice_istituto riferimento": "varchar(255)",
    "denominazione_istituto_riferimento": "varchar(255)",
    "codice_scuola": "varchar(255)",
    "denominazione_scuola": "varchar(255)",
    "indirizzo_scuola": "varchar(255)",
    "cap_scuola": "varchar(255)",
    "codice_comune_scuola": "varchar(255)",
    "descrizione_comune": "varchar(255)",
    "descrizione_caratteristica_scuola": "varchar(255)",
    "descrizione_tipologia_grado_istruzione_scuola": "varchar(255)",
    "indicazione_sede_direttivo": "varchar(255)",
    "indicazione_sede_omnicomprensivo": "varchar(255)",
    "indirizzo_email_scuola": "varchar(255)",
    "indirizzo_pec_scuola": "varchar(255)",
    "sito_web_scuola": "varchar(255)",
    "sede_scolastica": "varchar(255)",
}

# Chiave delle API Google Maps da usare per estrarre
# latitudine e longitudine delle scuole
google_maps_api_key = getenv("GOOGLE_MAPS_API_KEY")
print(google_maps_api_key)
