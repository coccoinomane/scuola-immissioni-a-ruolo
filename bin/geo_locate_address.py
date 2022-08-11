"""
Return latitude and longitude of an address in human
readable form, using Google Maps APIs

Source: https://github.com/vaclavdekanovsky/data-analysis-in-examples/blob/master/Maps/Geocoding/Address%20to%20Location.ipynb
"""

from geopy.geocoders import GoogleV3
from src.common.dotenv import getenv

AUTH_KEY = getenv("GOOGLE_MAPS_API_KEY")
geolocator = GoogleV3(api_key=AUTH_KEY)

point = geolocator.geocode("1 Apple Park Way, Cupertino, CA").point
print(f"latitude = {point.latitude}")
print(f"longitude = {point.longitude}")
