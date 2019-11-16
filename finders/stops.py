from dataclasses import dataclass

from finders.gps import GPSPosition


@dataclass
class Stop:
    name: str
    gps: GPSPosition
    station_id: int


@dataclass
class BixiStop(Stop):
    rental_method: list
    capacity: int
    is_kiosk: bool
