import sqlite3
from src.helpers.scuole import get_codice_from_scuola

from src.helpers.sqlite3 import get_by_codice


def aggiungi_geo(scuola: str) -> str:
    """
    Aggiungi alla scuola data il suo indirizzo, prendendolo
    dal DB sqlite3
    """
    codice = get_codice_from_scuola(scuola)
    scuola_miur = get_by_codice(codice)
    return scuola + "| " + scuola_miur["cap_scuola"]
