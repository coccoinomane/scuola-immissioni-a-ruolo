"""
Return latitude and longitude of an address in human
readable form, using Google Maps APIs

Source: https://github.com/vaclavdekanovsky/data-analysis-in-examples/blob/master/Maps/Geocoding/Address%20to%20Location.ipynb
"""

from geopy.geocoders import Nominatim, GoogleV3

AUTH_KEY = "AIzaSyCDyR0O1x5K5qKDenEU5-st62kpIGbyu2w"
geolocator = GoogleV3(api_key=AUTH_KEY)

point = geolocator.geocode("1 Apple Park Way, Cupertino, CA").point
print(f"latitude = {point.latitude}")
print(f"longitude = {point.longitude}")
