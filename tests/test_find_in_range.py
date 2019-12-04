import pytest

from finders.find_in_range import find_stops_in_range
from finders.gps import GPSPosition
from finders.stops import Stop

SAMPLE_STOPS = [
    Stop("Bibliothèque du Boisé", GPSPosition(45.506314, -73.711494))
    , Stop("Cavendish / Poirier", GPSPosition(45.504783, -73.704418))
    , Stop("Thimens / Alexis-Nihon", GPSPosition(45.508977, -73.698584))
    , Stop("Marcel-Laurin / Beaudet", GPSPosition(45.506968, -73.681766))
]


TEST_DATA = [
    (GPSPosition(45.498265, -73.707559), 950, [Stop("Bibliothèque du Boisé", GPSPosition(45.506314, -73.711494))
                                                , Stop("Cavendish / Poirier", GPSPosition(45.504783, -73.704418))])
    , (GPSPosition(45.498265, -73.707559), 750, [Stop("Bibliothèque du Boisé", GPSPosition(45.506314, -73.711494))])
    , (GPSPosition(45.498265, -73.707559), 1400, [Stop("Bibliothèque du Boisé", GPSPosition(45.506314, -73.711494))
                                                    , Stop("Cavendish / Poirier", GPSPosition(45.504783, -73.704418))
                                                    , Stop("Thimens / Alexis-Nihon", GPSPosition(45.508977, -73.698584))])
    , (GPSPosition(45.498265, -73.707559), 2250, SAMPLE_STOPS)
]


@pytest.mark.parametrize("current_gps_location, range_value,expected_stops", TEST_DATA)
def test_find_in_range(current_gps_location, range_value, expected_stops):
    stops_in_range = find_stops_in_range(SAMPLE_STOPS, current_gps_location, range_value)
    assert stops_in_range == expected_stops
