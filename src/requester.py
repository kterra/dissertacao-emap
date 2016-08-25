from constants import *
import googlemaps
import json


def format_locations(coordinates_list):
    first_loc = coordinates_list[1]
    locations = str(first_loc[1]) + "," + str(first_loc[2])

    for location in coordinates_list[2:]:
        locations += "|" + str(location[1]) + "," + str(location[2])
    #print(locations)
    return locations

def distance_matrix_request_builder(origins, destinations, mode = MODE_TRANSIT, transit_mode = BUS, traffic_model = BEST_GUESS, departure_time = "now" ):

    gmaps = googlemaps.Client(key='AIzaSyAuzg_eIeh9ejbUCx-DyIywkbmOUvaFWLg')
    matrix =  gmaps.distance_matrix(format_locations(origins), format_locations(destinations), mode, transit_mode)

    print(matrix)

def distance_matrix_url_builder(origins, destinations, mode = MODE_TRANSIT, transit_mode = BUS, traffic_model = BEST_GUESS, departure_time = "now" ):

    url  = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    url += "&origins=" + format_locations(origins)
    url += "&destinations=" + format_locations(destinations)
    url += "&mode=" + mode
    url += "&transit_mode=" + transit_mode
    url += "&language=pt-BR&key=AIzaSyAuzg_eIeh9ejbUCx-DyIywkbmOUvaFWLg"

    print(url)
