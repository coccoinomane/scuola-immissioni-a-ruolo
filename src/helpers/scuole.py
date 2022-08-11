import re


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
