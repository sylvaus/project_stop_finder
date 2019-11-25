from dataclasses import dataclass

from finders.gps import GPSPosition


@dataclass
class Stop:
    name: str
    gps: GPSPosition
    station_id: int


@dataclass
class BixiStopInformation(Stop):
    rental_method: list
    capacity: int
    is_kiosk: bool
    external_id: str
    short_name: str
    electric_bike_surcharge_waiver: bool
    eightd_has_key_dispenser: bool
    eightd_station_services: list

@dataclass
class BixiStopStatus():
    station_id: int
    num_bikes_available: int
    num_ebikes_available: int
    num_bikes_disabled: int
    num_docks_available: int
    num_docks_disabled: int
    is_installed: int
    is_renting: int
    is_returning: int
    last_reported: str

