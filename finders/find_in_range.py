from typing import List

from finders.gps import GPSPosition
from finders.stops import Stop


def find_stops_in_range(
        stops: List[Stop], gps: GPSPosition, range_: float, regex: bool = False
) -> List[Stop]:
    pass
