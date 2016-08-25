import requester
from data_filter import get_coordinates

if __name__ == '__main__':
    print("Start...")

    locations = get_coordinates("olympics_locations.csv")
    origins = locations
    destinantions = locations

    url = distance_matrix_request_builder(origins, destinantions)
    distance_matrix_request(url)

    print("Finished.")
