from typing import Tuple
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
    meccanografico
    """
    geolocator = get_geolocator()
    scuola_miur = get_by_codice(codice)
    point = geolocator.geocode(
        {
            "addressLine": scuola_miur["indirizzo_scuola"],
            "postalCode": scuola_miur["cap_scuola"],
            "locality": scuola_miur["descrizione_comune"],
            "adminDistrict": scuola_miur["provincia"],
            "country": "IT",
        }
    ).point
    return (point.latitude, point.longitude)
