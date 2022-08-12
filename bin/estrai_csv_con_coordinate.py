"""
Salva sul file 'storage/scuole-con-coordinate.csv' un CSV delle scuole con
disponibilità, indirizzo e coordinate geografiche (latitudine e longitudine).

ATTENZIONE: per ogni scuola verrà chiamata l'API di Google Maps! Assicurati
di aver impostato una chiave valida in .env.

Argomenti:

- numero minimo di disponibilità che deve avere la scuola
- numero di pagine da processare; di default è 0 (processa fino alla fine)
"""

import csv
from sys import argv
from typing import Any, List
from src.helpers.filter import estrai_scuole
from src.helpers.scuole import estrai_disponibilita
from src.helpers.geo import calcola_lat_lon
from src.helpers.scuole import get_codice_from_scuola
from src.helpers.sqlite3 import get_by_codice, get_indirizzo_completo
from src.libs.general import secondOrNone, thirdOrNone
from src.libs.parse import parseInt

# Config variabili
output_csv_file = "storage/scuole-con-coordinate.csv"
provincia = "RM"  # starts with
classi_di_concorso = ["MMCH", "MMDH", "MMEH"]  # substring
min_disponibilita = parseInt(secondOrNone(argv)) or 0
n_pages = parseInt(thirdOrNone(argv)) or 0

# Feedback
print(f"Provincia: {provincia}")
print(f"Classi di concorso: {classi_di_concorso}")
print(f"Disponibilità: da {min_disponibilita} in su")

# Estrai scuole
scuole = estrai_scuole(
    "storage/2022-agosto-avvio-immissioni.pdf",
    provincia=provincia + "  " + provincia,  # match "RM  RM"
    classi_di_concorso=classi_di_concorso,
    min_disponibilita=min_disponibilita,
    n_pages=n_pages,
    from_page=2,  # la tabella comincia dalla seconda pagina
    remove_header=False,  # l'header è su più righe
)

# Feedback
print(f"Numero scuole trovate: {len(scuole)}")
print(f"Disponibilità totali: {sum([sum(estrai_disponibilita(s)) for s in scuole])}")
print("")

# Estrai array con coordinate
csv_array: List[List[Any]] = [
    ["codice", "nome scuola", "indirizzo", "disp", "lat", "lon", "riga pdf"]
]

for scuola in scuole:
    codice = get_codice_from_scuola(scuola, provincia + "  ")  # better match
    lat, lon = calcola_lat_lon(codice)
    scuola_miur = get_by_codice(codice)
    disp = sum(estrai_disponibilita(scuola))
    csv_array.append(
        [
            codice,
            scuola_miur["denominazione_scuola"],
            get_indirizzo_completo(scuola_miur),
            disp,
            lat,
            lon,
            scuola,
        ]
    )

# Salva array nel CSV
with open(output_csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerows(csv_array)
