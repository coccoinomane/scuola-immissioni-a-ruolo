from typing import Tuple
from geopy.geocoders import GoogleV3
from src.helpers.sqlite3 import (
    get_by_codice,
    get_cap_scuola,
    get_indirizzo_completo,
    get_via_scuola,
)
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
    meccanografico
    """
    geolocator = get_geolocator()
    scuola_miur = get_by_codice(codice)
    point = geolocator.geocode(get_indirizzo_completo(scuola_miur)).point
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
