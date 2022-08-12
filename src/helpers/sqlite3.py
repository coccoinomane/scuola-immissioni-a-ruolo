import sqlite3
from typing import Dict
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
