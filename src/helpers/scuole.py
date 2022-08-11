import re
from typing import List


def get_codice_from_scuola(scuola: str, provincia: str) -> str:
    """
    Data una stringa che rappresenta una scuola, ritornane il
    codice meccanografico

    Per il PDF di agosto, necessita di specificare la provincia
    perché il codice non è all'inizio della riga
    """
    result = re.search(f"^{provincia}([0-9A-Z]+).*$", scuola)
    try:
        return result.group(1)
    except:
        raise Exception(
            f"La scuola non ha un codice meccanografico valido! SCUOLA = {scuola}"
        )


def estrai_disponibilita(scuola: str) -> List[int]:
    """
    Estrai le disponibilità (colonne CIN e COE) da una scuola.

    Se per qualche motivo non ci riesco, ritorno None
    """

    result = re.search("^.*\s+(\d+)\s+(\d+)\s*$", scuola)
    try:
        return [(int)(result.group(1)), (int)(result.group(2))]
    except:
        pass
    try:
        return [(int)(result.group(1))]
    except:
        return None
