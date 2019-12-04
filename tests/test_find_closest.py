import pytest

from finders.find_closest import find_closest_stop
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


@pytest.mark.parametrize("current_gps_location,expected_stop", TEST_DATA)
def test_find_closest_stop(current_gps_location, expected_stop):
    current_stop = find_closest_stop(SAMPLE_STOPS, current_gps_location)
    assert current_stop == expected_stop
