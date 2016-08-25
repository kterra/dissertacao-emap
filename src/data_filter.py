import os

def get_coordinates(coordinates_filename):

    coordinates_file = open(os.path.join("raw", coordinates_filename), 'r')
    coordinates = []

    line = coordinates_file.readline()
    while(line != ''):
        coordinates.append(map(tuple,line.split(',')))
        line = coordinates_file.readline()

    return coordinates
