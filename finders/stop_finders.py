from finders.bixi.parser import parse_bixi_station_information
from finders.find_closest import find_closest_stop
from finders.find_in_range import find_stops_in_range
from finders.find_name import find_stops_matching_name
from finders.gps import GPSPosition


class BixiStopFinder:
    def __init__(self, bixi_station_information_path: str):
        self._stops = parse_bixi_station_information(bixi_station_information_path)

    def find_closest(self, gps: GPSPosition):
        return find_closest_stop(self._stops, gps)

    def find_in_range(self, gps: GPSPosition, range_: float):
        return find_stops_in_range(self._stops, gps, range_)

    def find_name(self, name: str, regex: bool = True):
        return find_stops_matching_name(self._stops, name, regex)