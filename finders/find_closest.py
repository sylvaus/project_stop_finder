from typing import List

from finders.gps import GPSPosition, gps_distance
from finders.stops import Stop


def find_closest_stop(stops: List[Stop], gps: GPSPosition) -> Stop:
    closest_stop = stops[0]
    closest_distance = gps_distance(gps, closest_stop.gps)
    for stop in stops[1:]:
        if gps_distance(gps, stop.gps) < closest_distance:
            closest_distance = gps_distance(gps, stop.gps)
            closest_stop = stop
    return closest_stop
