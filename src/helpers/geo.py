from typing import Dict, Tuple
from geopy.geocoders import GoogleV3
from src.helpers.sqlite3 import get_by_codice
from src.common.config import google_maps_api_key


def get_geolocator() -> GoogleV3:
    """
    Ritorna il geolocalizzatore di geopy, inizializzato con la
    chiave API di Google Maps
    """
    return GoogleV3(api_key=google_maps_api_key)


def calcola_lat_lon(codice: str) -> Tuple[float, float]:
    """
    Ritorna latitudine e longitudine di una scuola, dato il suo codice
    meccanografico.

    Se la geolocalizzazione dovesse fallire, ad es. per un indirizzo errato,
    ritorna (0.0, 0.0).
    """
    geolocator = get_geolocator()
    scuola_miur = get_by_codice(codice)
    indirizzo = get_indirizzo_completo(scuola_miur)
    try:
        point = geolocator.geocode(indirizzo).point
    except:
        print(
            f"WARNING: Non posso localizzare '{scuola_miur['denominazione_scuola']}' [codice={scuola_miur['codice_scuola']}, indirizzo={indirizzo}]"
        )
        return (0.0, 0.0)
    return (point.latitude, point.longitude)


def calcola_lat_lon_spezzettando(codice: str) -> Tuple[float, float]:
    """
    Ritorna latitudine e longitudine di una scuola, dato il suo codice
    meccanografico, passando a Google l'indirizzo "spezzettato"
    """
    geolocator = get_geolocator()
    scuola_miur = get_by_codice(codice)
    params = {
        "postalCode": scuola_miur["cap_scuola"],
        "addressLine": scuola_miur["indirizzo_scuola"],
        "locality": scuola_miur["descrizione_comune"],
        "adminDistrict": scuola_miur["provincia"],
        "country": "IT",
    }
    point = geolocator.geocode(params).point
    return (point.latitude, point.longitude)


def sanitize_indirizzo_scuola(indirizzo_scuola: str) -> str:
    """
    Rendi una via (campo indirizzo_scuola del MIUR) più digeribile per
    le API di Google Maps
    """
    indirizzo_scuola = indirizzo_scuola.replace("SMS ", "")
    indirizzo_scuola = indirizzo_scuola.replace("S.M.S. ", "")
    indirizzo_scuola = indirizzo_scuola.replace("I.C.", "")
    indirizzo_scuola = indirizzo_scuola.replace("P.LE", "PIAZZALE")
    indirizzo_scuola = indirizzo_scuola.replace(", ,", ",")
    return indirizzo_scuola


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
        indirizzo_scuola = denominazione_scuola
    indirizzo_scuola = sanitize_indirizzo_scuola(indirizzo_scuola)
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
