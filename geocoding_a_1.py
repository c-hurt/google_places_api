import googlemaps
import json
import datetime
from collections import namedtuple

Geo_Coord = namedtuple('Geo_Coord', 'long lat')

def get_geo_coord(map_api, place):
    geocode_result = map_api.geocode(place)

    if geocode_result:
        return Geo_Coord(long=geocode_result[0]['geometry']['location']['lng'], lat=geocode_result[0]['geometry']['location']['lat'])
    return None


def geo_get_reverse(map_api, coord):
    geocode_reverse_result = map_api.reverse_geocode((coord.lat, coord.long))

    if geocode_reverse_result:
        return geocode_reverse_result[0]['formatted_address']
    return None


def get_direcitons_time(map_api, source, dest, dep_time):
    modes = ['driving', 'walking', 'transit', 'bicycling']
    result_times = {}

    for mode in modes:
        directions_result = map_api.directions(
            source,
            dest,
            mode=mode,
            departure_time= dep_time
        )
        result_times[mode] = directions_result[0]['legs'][0]['duration']['text']

    return result_times