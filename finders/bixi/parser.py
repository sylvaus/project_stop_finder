from typing import List
import json
from finders.gps import GPSPosition
from finders.stops import Stop


def parse_bixi_station_information(json_str: str) -> List[Stop]:
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
        # add to the list
        stops_list.append(Stop(station_name, gps_position))

    return stops_list



