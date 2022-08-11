from typing import Dict, List
from PyPDF2 import PdfReader
from src.helpers.scuole import estrai_disponibilita


def filtra_scuole(
    scuole: List[str],
    provincia: str,
    classi_di_concorso: List[str],
    min_disponibilita: int = 0,
) -> List[str]:
    """
    Filtra le scuole date per i criteri dati
    """
    return list(
        filter(
            lambda s: valida_scuola(
                s, provincia, classi_di_concorso, min_disponibilita
            ),
            scuole,
        )
    )


def valida_scuola(
    scuola: str,
    provincia: str,
    classi_di_concorso: List[str],
    min_disponibilita: int = 0,
) -> bool:
    """
    Ritorna True se la scuola data passa i criteri dati
    """
    return (
        scuola.startswith(provincia)
        and any([c in scuola for c in classi_di_concorso])
        and sum(estrai_disponibilita(scuola)) >= min_disponibilita
    )


def estrai_scuole(
    pdf_file: str,
    provincia: str,
    classi_di_concorso: List[str],
    min_disponibilita: int,
    n_pages: int = 0,
    from_page: int = 1,
    remove_header: bool = False,
) -> List[str]:
    """
    Tira fuori dal PDF una lista di scuole secondo i criteri dati
    """
    # Apri PDF
    reader = PdfReader(pdf_file)

    # Leggi PDF in memoria
    i_page = 0
    rows = []
    for page in reader.pages:
        i_page += 1
        if i_page < from_page:
            continue
        page_text = page.extract_text()
        # Rimuovi header
        if remove_header:
            page_text = page_text.split("\n", 1)[1]
        # Dividi in righe
        page_rows = page_text.split("\n")
        # Filtra le scuole
        page_rows = filtra_scuole(
            page_rows, provincia, classi_di_concorso, min_disponibilita
        )
        # Aggiungi le righe all'accumulatore
        rows += page_rows
        # Stoppa se abbiamo raggiunto il limite di pagine
        if n_pages and i_page - from_page + 1 >= n_pages:
            break

    return rows


def distribuzione_disponibilita(scuole: List[str]) -> Dict[int, List[str]]:
    """
    Data una lista di scuole, dividile per disponibilità totale
    """
    MAX_N_DISP = 100
    output: Dict[int, List[str]] = dict(
        zip(range(1, MAX_N_DISP), [[] for _ in range(MAX_N_DISP)])
    )
    for scuola in scuole:
        n_disp = sum(estrai_disponibilita(scuola))
        if n_disp >= MAX_N_DISP:
            raise Exception(f"Trovata scuola con più di {MAX_N_DISP} disponibilità")
        output[n_disp].append(scuola)
    return output
