from finders.bixi.parser import parse_bixi_station_information
from finders.bixi.parser import parse_bixi_station_status
from finders.bixi.parser import get_json_from_http
from finders.find_closest import find_closest_stop
from finders.find_in_range import find_stops_in_range
from finders.find_name import find_stops_matching_name
from finders.gps import GPSPosition


class BixiStopFinder:
    def __init__(self, json_info: str, json_status:str):

        self.stop_information_ = parse_bixi_station_information(json_info)
        self.stop_status_ = parse_bixi_station_status(json_status)

    def find_closest(self, gps: GPSPosition):
        return find_closest_stop(self._stops, gps)

    def find_in_range(self, gps: GPSPosition, range_: float):
        return find_stops_in_range(self._stops, gps, range_)

    def find_name(self, name: str, regex: bool = True):
        return find_stops_matching_name(self._stops, name, regex)

    def update_bikes_nuumbers(self, url:str):
        pass




