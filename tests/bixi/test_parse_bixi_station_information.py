import json

from pytest import mark

from finders.bixi.parser import parse_bixi_station_information
from finders.gps import GPSPosition
from finders.stops import BixiStop


def make_stop_json_text(name, latitude, longitude, station_id, rental_methods, capacity, has_kiosk) -> str:
    return json.dumps({
        "lat": latitude, "lon": longitude, "name": name, "station_id": station_id
        , "capacity": capacity, "rental_methods": rental_methods, "has_kiosk": has_kiosk
    })


NOMINAL_JSON_TEXT_STATIONS = [
    make_stop_json_text("Station Nominal 1", 12.5, 74.2, 458, ["cash", "visa"], 12, True)
    , make_stop_json_text("Station Nominal 2", -2.5, 36.2, 75, ["cash"], 5, False)
    , make_stop_json_text("Station Nominal 3", -16.5, -54.2, 1247, ["visa"], 0, True)
    , make_stop_json_text("Station Nominal 4", -2.5, 61.2, 1247, ["visa"], 0, True)
]

NOMINAL_STATIONS = [
    BixiStop("Station Nominal 1", GPSPosition(12.5, 74.2), 458, ["cash", "visa"], 12, True)
    , BixiStop("Station Nominal 2", GPSPosition(-2.5, 36.2), 75, ["cash"], 5, False)
    , BixiStop("Station Nominal 3", GPSPosition(-16.5, -54.2), 1247, ["visa"], 0, True)
    , BixiStop("Station Nominal 4", GPSPosition(-2.5, 61.2), 1247, ["visa"], 0, True)
]


TEST_VALUES = [
    (f'{{"data": {{"stations": []}}}}', [])
    , (f'{{"data": {{"stations": [{", ".join(NOMINAL_JSON_TEXT_STATIONS)}]}}}}', NOMINAL_STATIONS)
]


TEST_NAMES = [
    "No station"
    , "Nominal case"
]


@mark.parametrize("json_text, expected_stops", TEST_VALUES, ids=TEST_NAMES)
def test_parse_bixi_station_information(json_text, expected_stops):
    stops = parse_bixi_station_information(json_text)
    assert stops == expected_stops


