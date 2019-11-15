from dataclasses import dataclass
from math import sin, cos, acos, pi, radians

@dataclass
class GPSPosition:
    latitude: float
    longitude: float

def gps_distance(Start : GPSPosition,End : GPSPosition):
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137

    distance = acos(
        sin(radians(Start.latitude)) * sin(radians(End.latitude))
        + cos(radians(Start.latitude)) * cos(radians(End.latitude))
        * cos(abs(radians(End.longitude) - radians(Start.longitude)))
    )
    distance = distance * RT

    return distance
