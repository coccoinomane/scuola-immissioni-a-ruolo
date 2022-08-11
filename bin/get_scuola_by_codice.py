"""
Dato il codice meccanografico di una scuola, ritorna il dict
della scuola dal DB del MIUR
"""

from pprint import pprint
from sys import argv
from src.helpers.sqlite3 import get_by_codice
from src.libs.general import secondOrNone

codice = secondOrNone(argv)

if not codice:
    print("Devi darmi un codice!")
    exit(1)

pprint(get_by_codice(codice))
