from typing import List

from finders.gps import GPSPosition, gps_distance
from finders.stops import Stop


def find_stops_in_range(
        stops: List[Stop], gps: GPSPosition, range_: float) -> List[Stop]:
    return [stop for stop in stop if gps_distance(gps, stop.gps) <= range_]
