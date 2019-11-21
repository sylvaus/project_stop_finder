from typing import List

from finders.gps import GPSPosition, gps_distance
from finders.stops import Stop


def find_stops_in_range(
        stops: List[Stop], gps: GPSPosition, range_: float) -> List[Stop]:
    return filter(lambda stop: gps_distance(gps, stop.gps) <= range_, stops)
