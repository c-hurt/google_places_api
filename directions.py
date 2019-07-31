import googlemaps

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
        result_times[mode] = directions_result[0]['legs'][0]['distance']['text']

    return result_times