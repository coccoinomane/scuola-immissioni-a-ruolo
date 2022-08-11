"""
Stampa su schermo le scuole divise per disponibilità, con relativi
CAP e indirizzi

Argomenti:

- numero minimo di disponibilità che deve avere la scuola
- numero di pagine da processare; di default è 0 (processa fino alla fine)
"""

from sys import argv
from typing import List
from src.helpers.filter import distribuzione_disponibilita, estrai_scuole
from src.helpers.scuole import estrai_disponibilita, get_codice_from_scuola
from src.helpers.sqlite3 import get_by_codice, get_indirizzo
from src.libs.general import secondOrNone, thirdOrNone
from src.libs.parse import parseInt

# Config variabili
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

# Estrai distribuzione diponibilità
distribuzione = distribuzione_disponibilita(scuole)
for n_disp in reversed(list(distribuzione.keys())):
    scuole_con_n_disp = distribuzione[n_disp]
    if len(scuole_con_n_disp) == 0:
        continue
    print(f">>> SCUOLE CON {n_disp} DISPONIBILITÀ ({len(scuole_con_n_disp)})")
    for scuola in scuole_con_n_disp:
        codice = get_codice_from_scuola(scuola, provincia + "  ")  # better match
        scuola_miur = get_by_codice(codice)
        print(get_indirizzo(scuola_miur) + " | " + scuola)
    print("")
