import pytest

from finders.find_in_range import find_stops_in_range
from finders.gps import GPSPosition
from finders.stops import Stop

SAMPLE_STOPS = [
    Stop("location_sw", GPSPosition(-10, -10))
    , Stop("location_se", GPSPosition(10, -10))
    , Stop("location_ne", GPSPosition(10, 10))
    , Stop("location_nw", GPSPosition(-10, 10))
]


TEST_DATA = [
    (GPSPosition(1, 1), Stop("location_ne", GPSPosition(10, 10)))
    , (GPSPosition(1, -1), Stop("location_se", GPSPosition(10, -10)))
    , (GPSPosition(-1, -1), Stop("location_sw", GPSPosition(-10, -10)))
    , (GPSPosition(-1, 1), Stop("location_nw", GPSPosition(-10, 10)))
]


@pytest.mark.parametrize("current_gps_location, range_value,expected_stops", TEST_DATA)
def test_find_in_range(current_gps_location, range_value, expected_stops):
    stop_in_range = find_stops_in_range(SAMPLE_STOPS, current_gps_location, range_value)
    assert stop_in_range == expected_stops
