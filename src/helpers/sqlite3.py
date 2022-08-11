import sqlite3
from typing import Dict
from xmlrpc.client import boolean
from src.libs.sqlite import create_db_from_csv_file
from src.common.config import (
    scuole_miur_csv_file,
    scuole_miur_sqlite_file,
    scuole_miur_schema,
)


def get_cursor() -> sqlite3.Cursor:
    """
    Ritorna un cursore connesso al database
    """
    con = sqlite3.connect(scuole_miur_sqlite_file)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return cur


def crea_database_scuole_miur() -> None:
    """
    Popola il database sqlite3 con gli indirizzi delle scuole
    presi da OpenData
    """
    create_db_from_csv_file(
        csv_file=scuole_miur_csv_file,
        sqlite_file=scuole_miur_sqlite_file,
        schema=scuole_miur_schema,
        skip_first_line=True,
    )


def get_by_codice(codice: str) -> Dict[str, str]:
    """
    Dato il codice meccanografico di una scuola, ritorna il dict
    della scuola dal DB del MIUR
    """
    cur = get_cursor()
    cur.execute("SELECT * FROM scuole WHERE codice_scuola=:codice", {"codice": codice})
    fetched = cur.fetchone()
    if fetched:
        output = dict(fetched)
    else:
        output = None
    return output


def get_via_scuola(scuola_miur: Dict[str, str]) -> str:
    """
    Data una scuola presa dal database del MIUR, ritornane la via.

    Se la scuola non ha una via valida (campo indirizzo_scuola), usa
    al suo posto la denominazione della scuola, purgata da eventuali
    denominazioni (SMS, IC...)
    """
    indirizzo_scuola = scuola_miur["indirizzo_scuola"]
    if not indirizzo_scuola or "non disponibile" in indirizzo_scuola.lower():
        denominazione_scuola = scuola_miur["denominazione_scuola"]
        print(
            f"WARNING: Indirizzo non definito per '{scuola_miur['codice_scuola']}' [{denominazione_scuola}]"
        )
        indirizzo_scuola = denominazione_scuola.replace("SMS ", "").replace("IC ", "")
    return indirizzo_scuola


def get_cap_scuola(scuola_miur: Dict[str, str], fallback: str = None) -> str:
    """
    Data una scuola presa dal database del MIUR, ritornane il CAP,
    o il valore di fallback se il CAP non è definito
    """
    cap_scuola = scuola_miur["cap_scuola"]
    if not cap_scuola or "non disponibile" in cap_scuola.lower():
        print(
            f"WARNING: CAP non definito per '{scuola_miur['codice_scuola']}' [{scuola_miur['denominazione_scuola']}]"
        )
        cap_scuola = fallback
    return cap_scuola


def get_indirizzo_completo(
    scuola_miur: Dict[str, str], fallback_cap: str = None
) -> str:
    """
    Data una scuola presa dal database del MIUR, ritornane l'indirizzo
    formattato, con il CAP per primo.

    Se la scuola non ha una via valida (campo indirizzo_scuola), usa
    al suo posto la denominazione della scuola.
    """
    return ", ".join(
        [
            get_via_scuola(scuola_miur),
            get_cap_scuola(scuola_miur, fallback_cap or ""),
            scuola_miur["descrizione_comune"],
            scuola_miur["provincia"],
        ]
    )
