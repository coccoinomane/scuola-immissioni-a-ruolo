"""
Stampa su schermo le scuole divise per disponibilità, con relativi
CAP e indirizzi

Argomenti:

- numero minimo di disponibilità che deve avere la scuola
- numero di pagine da processare; di default è 0 (processa fino alla fine)
- a partire da quale pagina partire; di default è 1 (Roma comincia dalla pagina 83)
"""

from sys import argv
from typing import List
from src.helpers.filter import distribuzione_disponibilita, estrai_scuole
from src.helpers.scuole import get_codice_from_scuola
from src.helpers.sqlite3 import get_by_codice, get_indirizzo
from src.libs.general import secondOrNone, thirdOrNone, fourthOrNone
from src.libs.parse import parseInt

# Config variabili
provincia = "RM"  # starts with
insegnamento = "SOSTEGNO I GRADO"  # substring
min_disponibilita = parseInt(secondOrNone(argv)) or 0
n_pages = parseInt(thirdOrNone(argv)) or 0
from_page = parseInt(fourthOrNone(argv)) or 1

# Feedback
print(f"Provincia: {provincia}")
print(f"Insegnamento: {insegnamento}")
print(f"Disponibilità: da {min_disponibilita} in su")

# Estrai scuole
scuole = estrai_scuole(
    "storage/2022-agosto-avvio-immissioni",
    provincia=provincia,
    insegnamento=insegnamento,
    min_disponibilita=min_disponibilita,
    n_pages=n_pages,
    from_page=from_page,
)

# Feedback
print(f"Numero scuole trovate: {len(scuole)}")
print("")

# Estrai distribuzione diponibilità
distribuzione = distribuzione_disponibilita(scuole)
for n_disp in reversed(list(distribuzione.keys())):
    scuole_con_n_disp = distribuzione[n_disp]
    if len(scuole_con_n_disp) == 0:
        continue
    print(f">>> SCUOLE CON {n_disp} DISPONIBILITÀ ({len(scuole_con_n_disp)})")
    for scuola in scuole_con_n_disp:
        codice = get_codice_from_scuola(scuola)
        scuola_miur = get_by_codice(codice)
        print(get_indirizzo(scuola_miur) + " | " + scuola)
    print("")
