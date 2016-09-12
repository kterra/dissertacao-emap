import pandas as pd
import os
from geopy.geocoders import GoogleV3

ceps = pd.read_csv(os.path.join("raw", "ceps_rio_de_janeiro_estado_filtered_columns.csv"))
ceps_five = [str(x)[:5] for x in ceps["CEP"]]

ceps_five = sorted(list(set(ceps_five)))
print(len(ceps_five))

geolocator = GoogleV3()
locations = []
for cep in ceps_five:
    print(cep)
    location = geolocator.geocode(cep + ", Rio de Janeiro, RJ")
    if location:
        with open(os.path.join("raw", 'grid_rj.csv'), 'a') as grid_file:
            grid_file.write("{}, {}\n".format(location.latitude, location.longitude))
    else:
        print("error:")
        print((location.latitude, location.longitude))
