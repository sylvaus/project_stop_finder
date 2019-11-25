from typing import List
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
        response.encoding="uft-8"
        return response.json()


def parse_bixi_station_information(json_str: str) -> List[BixiStopInformation]:

    # extract a dictionary of the stations with the corresponding key
    stations_information_dictionary = json_str['data']

    # extract the list of the stations with the corresponding key
    stations_information_list = stations_information_dictionary['stations']

    # list of stops to return
    stops_station_information = [BixiStopInformation(stop['name'],
                                                     GPSPosition(stop['lat'], stop['lon']),
                                                     stop['station_id'],
                                                     stop['rental_methods'],
                                                     stop['capacity'],
                                                     stop['has_kiosk'],
                                                     stop['external_id'],
                                                     stop['short_name'],
                                                     stop['electric_bike_surcharge_waiver'],
                                                     stop['eightd_has_key_dispenser'])
                                 for stop in stations_information_list]

    return stops_station_information


def parse_bixi_station_status(json_str: str):

    # extract a dictionary of the stations with the corresponding key
    stations_status_dictionary = json_str['data']

    # extract the list of the stations with the corresponding key
    stations_status_list = stations_status_dictionary['stations']

    # list of stops to return
    stops_station_status = [BixiStopStatus(stop['station_id'],
                                           stop['num_bikes_available'],
                                           stop['num_ebikes_available'],
                                           stop['num_bikes_disabled'],
                                           stop['num_docks_available'],
                                           stop['num_docks_disabled'],
                                           stop['is_installed'],
                                           stop['is_renting'],
                                           stop['is_returning'],
                                           stop['last_reported'])
                            for stop in stations_status_list]

    return stops_station_status

