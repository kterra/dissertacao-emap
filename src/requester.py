from constants import *
import googlemaps
import json
import csv
import os
from random import randint
from time import sleep

def format_locations(coordinates_list):

    first_loc = coordinates_list[0]
    locations = str(first_loc[0]) + "," + str(first_loc[1])
    #print(locations)

    if len(coordinates_list) > 1:
        for location in coordinates_list[1:]:
            locations += "|" + str(location[0]) + "," + str(location[1])
        #print(locations)
    return locations


def distance_matrix_request_builder(origins, destinations, mode = MODE_TRANSIT, transit_mode = BUS, traffic_model = BEST_GUESS, departure_time = "now" ):

    gmaps = googlemaps.Client(key='AIzaSyAuzg_eIeh9ejbUCx-DyIywkbmOUvaFWLg')

    n = len(destinations[1:])

    loop = 10
    for origin in origins[1:]:
        first = 1
        last = loop
        n_loops = int(n/loop) + 1

        rows = []
        destination_addresses = []
        while n_loops > 0:
            if last > n:
                last = n
            if first < last:
                print("Requesting Google...")
                matrix =  gmaps.distance_matrix(format_locations([origin]), format_locations(destinations[first:last]), mode, transit_mode)
                rows = rows + matrix['rows']
                destination_addresses= destination_addresses + matrix['destination_addresses']
                origin_address = matrix['origin_addresses'][0]
                print("Sleeping...")
                sleep(randint(1,5))

            n_loops = n_loops - 1
            first = last + 1
            last = first + loop
            break

        with open(os.path.join("output", 'distance_matrix_distance_result.csv'), 'a') as result_file:
            result_file.write("{},".format("origins"))

        f = open('output/distance_matrix_distance_result.csv', 'a')
        writer = csv.writer(f)
        writer.writerow(destination_addresses)
        f.close()

        with open(os.path.join("output", 'distance_matrix_duration_result.csv'), 'a') as result_file:
            result_file.write("{},".format("origins"))

        f = open('output/distance_matrix_duration_result.csv', 'a')
        writer = csv.writer(f)
        writer.writerow(destination_addresses)
        f.close()
        print(rows)

        for row in rows:
            elements = row["elements"]
            # print("\n\nElements...")
            distances = []
            durations = []
            for element in elements:
                status = element["status"]
                if status == "OK":
                    distances.append(element["distance"]["value"])
                    durations.append(element["duration"]["value"])
                    # print("Distance:" + str(element["distance"]["value"]) + " metros")
                    # print(element["distance"] )
                    # print("Duration:" + str(element["duration"]["value"]) + " segundos")
                    # print(element["duration"])
                else:
                    distances.append(0)
                    durations.append(0)
                print("Status:")
                print(status)

            with open(os.path.join("output", 'distance_matrix_distance_result.csv'), 'a') as result_file:
                result_file.write("{},".format(origin_address))
            with open(os.path.join("output", 'distance_matrix_duration_result.csv'), 'a') as result_file:
                result_file.write("{},".format(origin_address))

            f = open('output/distance_matrix_distance_result.csv', 'a')
            writer = csv.writer(f)
            writer.writerow(distances)
            f.close()

            f = open('output/distance_matrix_duration_result.csv', 'a')
            writer = csv.writer(f)
            writer.writerow(durations)
            f.close()

            break





def distance_matrix_url_builder(origins, destinations, mode = MODE_TRANSIT, transit_mode = BUS, traffic_model = BEST_GUESS, departure_time = "now" ):

    url  = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    url += "&origins=" + format_locations(origins)
    url += "&destinations=" + format_locations(destinations)
    url += "&mode=" + mode
    url += "&transit_mode=" + transit_mode
    url += "&language=pt-BR&key=AIzaSyAuzg_eIeh9ejbUCx-DyIywkbmOUvaFWLg"

    print(url)
