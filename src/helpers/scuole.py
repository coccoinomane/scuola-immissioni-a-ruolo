import re


def get_codice_from_scuola(scuola: str) -> str:
    """
    Data una stringa che rappresenta una scuola, ritornane il
    codice meccanografico
    """
    result = re.search("^([0-9A-Z]+).*$", scuola)
    try:
        return result.group(1)
    except:
        raise Exception(
            f"La scuola non ha un codice meccanografico valido! SCUOLA = {scuola}"
        )
