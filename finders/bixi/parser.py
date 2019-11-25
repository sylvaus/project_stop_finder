from typing import List
import json
from finders.gps import GPSPosition
from finders.stops import BixiStopInformation, BixiStopStatus
import requests
from requests.exceptions import HTTPError


def get_json_from_http(url):
    # get http response
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        return response.json()


def parse_bixi_station_information(json_str: str) -> List[BixiStopInformation]:

    # extract a dictionary of the stations with the corresponding key
    stations_information_dictionary = json_str['data']

    # extract the list of the stations with the corresponding key
    stations_information_list = stations_information_dictionary['stations']

    # list of stops to return
    stops_station_information = []

    for stop in stations_information_list:

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
        external_id=stop['external_id']
        short_name=stop['short_name']
        electric_bike_surcharge_waiver=['electric_bike_surcharge_waiver']
        eightd_has_key_dispenser=['eightd_has_key_dispenser']
        eightd_station_services=['eightd_station_services']

        # add to the list
        stops_station_information.append(BixiStopInformation(station_name,
                                                  gps_position,
                                                  station_id,
                                                  rental_method,
                                                  station_capacity,
                                                  has_kiosk,
                                                  external_id,
                                                  short_name,
                                                  electric_bike_surcharge_waiver,
                                                  eightd_has_key_dispenser,
                                                  eightd_station_services))

    return stops_station_information


def parse_bixi_station_status(json_str: str):

    # extract a dictionary of the stations with the corresponding key
    stations_status_dictionary = json_str['data']

    # extract the list of the stations with the corresponding key
    stations_status_list = stations_status_dictionary['stations']

    # list of stops to return
    stops_station_status = []

    for stop in stations_status_list:
        # extract the station id
        station_id = stop['station_id']
        # extract num bikes availables
        num_bikes_available = stop['num_bikes_available']
        # extract num ebikes availables
        num_ebikes_available = stop['num_ebikes_available']
        num_bikes_disabled = stop['num_bikes_disabled']
        num_docks_available = stop['num_docks_available']
        num_docks_disabled = stop['num_docks_disabled']
        is_installed=stop['is_installed']
        is_renting=stop['is_renting']
        is_returning=stop['is_returning']
        last_reported=stop['last_reported']

        # add to the list
        stops_station_status.append(BixiStopStatus(station_id,
                                                   num_bikes_available,
                                                   num_ebikes_available,
                                                   num_bikes_disabled,
                                                   num_docks_available,
                                                   num_docks_disabled,
                                                   is_installed,
                                                   is_renting,
                                                   is_returning,
                                                   last_reported))

    return stops_station_status

def build_bixi_station():
    pass
def main():
    url1 = "https://api-core.bixi.com/gbfs/en/station_status.json"
    url2="https://api-core.bixi.com/gbfs/en/station_information.json"
    json_data= get_json_from_http(url1)
    #info=parse_bixi_station_information(json_data)
    status=parse_bixi_station_status(json_data)

    a=1

if __name__ == '__main__':
    main()
