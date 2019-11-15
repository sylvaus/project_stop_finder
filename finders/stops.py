from dataclasses import dataclass

from finders.gps import GPSPosition


@dataclass
class Stop:
    name: str
    gps: GPSPosition
