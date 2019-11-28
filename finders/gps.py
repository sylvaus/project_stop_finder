from dataclasses import dataclass
from math import sin, cos, acos, radians


@dataclass
class GPSPosition:
    latitude: float
    longitude: float


def gps_distance(start: GPSPosition, end: GPSPosition):
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    rt = 6378137

    distance = acos(
        sin(radians(start.latitude)) * sin(radians(end.latitude))
        + cos(radians(start.latitude)) * cos(radians(end.latitude))
        * cos(abs(radians(end.longitude) - radians(start.longitude)))
        )
    distance = distance * rt

    return distance
