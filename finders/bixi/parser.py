from typing import List
import json
from finders.gps import GPSPosition
from finders.stops import Stop, BixiStop


def parse_bixi_station_information(json_str: str) -> List[BixiStop]:
    # list of stops to return
    stops_list = []

    # parse the data in a dictionary
    all_bixi_data = json.loads(json_str)
    # TODO: find a way to ensure that the structure didn't change

    # extract a dictionary of the stations with the corresponding key
    stations_dictionary = all_bixi_data['data']

    # extract the list of the stations with the corresponding key
    stations_list = stations_dictionary['stations']

    for stop in stations_list:
        # extract gps position
        gps_position = GPSPosition(stop['lat'], stop['lon'])
        # extract station name
        station_name = stop['name']
        # extract the station id
        station_id = stop['station_id']
        # extract rental method
        rental_method = stop['rental_methods']
        # extract capacity
        station_capacity = stop['capacity']
        # extract kiosk flag
        has_kiosk = stop['has_kiosk']
        # add to the list
        stops_list.append(BixiStop(station_name, gps_position, station_id, rental_method, station_capacity, has_kiosk))

    return stops_list



