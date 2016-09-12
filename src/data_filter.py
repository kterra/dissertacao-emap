import os

def get_coordinates(coordinates_filename):

    coordinates_file = open(os.path.join("raw", coordinates_filename), 'r', encoding='ISO-8859-1')
    coordinates = []

    line = coordinates_file.readline()
    while(line != ''):
    #for i in range(4):
        coordinates.append(line.split(','))
        line = coordinates_file.readline()

    return coordinates
