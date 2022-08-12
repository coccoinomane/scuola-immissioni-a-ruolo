"""
Data una provincia, salva sul file 'storage/estrazione-scuole-miur.csv'
un CSV delle scuole di quella provincia, con indirizzo e coordinate
geografiche (latitudine e longitudine).

ATTENZIONE: per ogni scuola verrà chiamata l'API di Google Maps! Assicurati
di aver impostato una chiave valida in .env.

Argomenti:

- nome completo della provincia, tutto maiuscolo, default "ROMA"
- nome completo della tipologia, default "SCUOLA PRIMO GRADO"
  (le virgolette intorno sono importanti!)
"""

import csv
from sys import argv
from typing import Any, List
from src.helpers.geo import calcola_lat_lon, get_indirizzo_completo
from src.helpers.sqlite3 import get_cursor
from src.libs.general import secondOrNone, thirdOrNone

# Config variabili
output_csv_file = "storage/estrazione-scuole-miur.csv"
provincia = secondOrNone(argv) or "ROMA"
tipologia = thirdOrNone(argv) or "SCUOLA PRIMO GRADO"

# Feedback
print(f"Provincia: {provincia}")

# Estrai scuole dal CSV del MIUR
cur = get_cursor()
cur.execute(
    "SELECT * FROM scuole WHERE provincia=:provincia AND descrizione_tipologia_grado_istruzione_scuola=:tipologia",
    {"provincia": provincia, "tipologia": tipologia},
)
fetched = cur.fetchall()
if fetched:
    scuole_miur = [dict(s) for s in fetched]
else:
    print("NESSUNA SCUOLA TROVATA")
    exit(1)

# Feedback
print(f"Numero scuole trovate: {len(scuole_miur)}")
print("")

# Inizializza CSV
csv_array: List[List[Any]] = [
    ["codice", "nome scuola", "indirizzo", "disp", "lat", "lon", "riga pdf"]
]

for scuola_miur in scuole_miur:
    codice = scuola_miur["codice_scuola"]
    lat, lon = calcola_lat_lon(codice)
    csv_array.append(
        [
            codice,
            scuola_miur["denominazione_scuola"],
            get_indirizzo_completo(scuola_miur),
            lat,
            lon,
        ]
    )

# Salva array nel CSV
with open(output_csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerows(csv_array)
