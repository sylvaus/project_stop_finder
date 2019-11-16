from pytest import mark

from finders.gps import gps_distance, GPSPosition

ACCEPTABLE_TOLERANCE = 0.5


def diff_percentage(expected: float, result: float) -> float:
    return abs(expected - result) / abs(expected) * 100


TEST_VALUES = [
    (GPSPosition(74.2, 25.0), GPSPosition(74.2, 25.0250), 756.90)
    , (GPSPosition(74.2, 25.0), GPSPosition(74.2, 28.0), 90818.94)
    , (GPSPosition(74.2, 25.0), GPSPosition(74.2, 54.5), 884023.73)
    , (GPSPosition(-36.0, -24.0), GPSPosition(-36.0157, -24.0), 1745.76)
    , (GPSPosition(-36.0, -24.0), GPSPosition(-38.0, -24.0), 222389.85)
    , (GPSPosition(-36.0, -24.0), GPSPosition(-79.4578, -24.0), 4832286.88)
    , (GPSPosition(-36.0, -24.0), GPSPosition(-38.0, 5.0), 2574480.89)
    , (GPSPosition(-5.7, -1.2), GPSPosition(9.1, 8.9), 1990329.71)
    , (GPSPosition(5.4459787, 1.219874), GPSPosition(5.45145, 1.2224), 669.56)
]

TEST_NAMES = [
    "Same latitude GPS calculation: short distance"
    , "Same latitude GPS calculation: medium distance"
    , "Same latitude GPS calculation: long distance"
    , "Same longitude GPS calculation: short distance"
    , "Same longitude GPS calculation: medium distance"
    , "Same longitude GPS calculation: long distance"
    , "All angles negative except longitude end"
    , "Start angles negative, end angles positive"
    , "Really short distance"
]


@mark.parametrize("start, end, expected_distance", TEST_VALUES, ids=TEST_NAMES)
def test_gps_distance(start, end, expected_distance):
    distance = gps_distance(start, end)
    assert ACCEPTABLE_TOLERANCE > diff_percentage(distance, expected_distance), \
        f"GPS distance calculated {distance} does not respect tolerance {ACCEPTABLE_TOLERANCE}%" \
        f" from expected distance {expected_distance}"
