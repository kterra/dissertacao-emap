import constants
import httplib2
import json


def format_locations(coordinates_list):
    first_loc = coordinates_list[0]
    locations = str(first_loc[0]) + "," + str(first_loc[1]) + "|"

    for location in coordinates_list[1:]:
        locations += "|" + str(location[0]) + "," + str(location[1])

    return locations

def distance_matrix_request_builder(origins, destinantions, mode = MODE_TRANSIT, transit_mode = BUS, traffic_model = BEST_GUESS, departure_time = "now" ):

    url  = "https://maps.googleapis.com/maps/api/distancematrix/json?language=pt-BR&key=AIzaSyAuzg_eIeh9ejbUCx-DyIywkbmOUvaFWLg"
    url += "&oringins=" + format_locations(origins)
    url += "&destinations=" + format_locations(destinations)
    url += "&mode=" + mode
    url += "&transit_mode=" + transit_mode

    return url


def distance_matrix_request(url):
    resp, content = httplib2.Http().request(url)
    json.load(content)
    print(json)
