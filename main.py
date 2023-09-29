import requests #sending a GET request to the Google Geocoding API
import random
import pandas as pd
from config.creds import api_key
from random import choice # for the bus ids
from bus_ids import generate_bus_ids
from sigtuna_stations import sigtuna_stations
from norrtalje_stations import norrtalje_busstations
from upplands_stations import upplands_vasby_stations
from vallentuna_stations import vallentuna_stations
from danderyd_stations import danderyd_stations
"""
Retrieves the latitude and longitude coordinates for a given location.
Args:location (str): The location to geocode.
Returns:tuple: The latitude and longitude coordinates.
    """

def get_latitude_longitude(location):
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}, Stockholm, Sweden&key={creds.api_key}')
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            result = data['results'][0]
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            return lat, lng  # Return coordinates if data['results'] exists
        else:
            return None, None  # Return None, None if data['results'] is empty
    else:
        return None, None  # Return None, None if status code is not 200

# Using sets to remove duplicate locations and # Combining all lists of stations into one
def remove_duplicates(locations):
    flat_locations= [item for sublist in locations for item in sublist]
    return list(set(flat_locations))


all_stations = norrtalje_busstations + sigtuna_stations + upplands_vasby_stations + vallentuna_stations + danderyd_stations
unique_stations = remove_duplicates(all_stations)

# Get list of bus IDs
bus_ids_df = generate_bus_ids(len(unique_stations))
bus_ids = bus_ids_df['BUS ID'].tolist()

#Creating an empty list to store the locations
coordinates = []


for station in unique_stations:
    latitude, longitude = get_latitude_longitude(station)
    if latitude is not None and longitude is not None:
        # Select a random bus ID for each station
        bus_id = random.choice(bus_ids)
        coordinates.append((station,latitude,longitude, bus_id))


for station, latitude, longitude, bus_id in coordinates:
    print(f'Location: {station}')
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
    print(f'Bus ID: {bus_id}')
    print("------")

    # Collecting the data into data frame
df = pd.DataFrame(coordinates, columns=['Station', 'Latitude', 'Longitude', 'Bus ID'])

# Write the DataFrame to a CSV file
#df.to_csv('bus_locations.csv', index=False)
df.to_excel('bus_locations.xlsx', index=False)


"""
#testing printint to csv
#Collecting the data into data frame
df = pd.DataFrame(coordinates, columns=['Station', 'Latitude', 'Longitude', 'Bus ID'])

# Write the DataFrame to a CSV file
df.to_csv('bus_locations.csv', index=False)
"""