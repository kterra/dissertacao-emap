from  requester import *
from data_filter import get_coordinates

if __name__ == '__main__':
    print("Start...")

    locations = get_coordinates("grid_capital_rj.csv")
    origins = locations
    destinantions = locations

    distance_matrix_request_builder(origins, destinantions)
    #distance_matrix_url_builder(origins, destinantions)

    print("Finished.")