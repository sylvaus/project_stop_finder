import pytest

from finders.find_name import find_stops_matching_name
from finders.stops import Stop
from finders.gps import GPSPosition

SAMPLE_STOPS = [
    (Stop(name='de la Commune / Place Jacques-Cartier',
             gps=GPSPosition(latitude=45.50761009451047, longitude=-73.55183601379395))),
    (Stop(name='Métro Champ-de-Mars (Viger / Sanguinet)',
             gps=GPSPosition(latitude=45.51035067563653, longitude=-73.55650842189789))),
    (Stop(name='Ste-Catherine / Dezery',
             gps=GPSPosition(latitude=45.539385081961676, longitude=-73.54099988937377))),
    (Stop(name='Clark / Evans',
              gps=GPSPosition(latitude=45.51100666600306, longitude=-73.56760203838348))),
    (Stop(name='du Champ-de-Mars / Gosford',
             gps=GPSPosition(latitude=45.50965520472071, longitude=-73.55400860309601))),
    (Stop(name='Metcalfe / du Square-Dorchester',
             gps=GPSPosition(latitude=45.500208064155046, longitude=-73.57113786041737))),
    (Stop(name='18e avenue / Rosemont',
              gps=GPSPosition(latitude=45.55789545752947, longitude=-73.5765291005373))),
    (Stop(name="de l'Hôtel-de-Ville / Ste-Catherine",
             gps=GPSPosition(latitude=45.51166045593874, longitude=-73.56213569641113))),
    (Stop(name='Sanguinet / Ste-Catherine',
             gps=GPSPosition(latitude=45.51279685582333, longitude=-73.56146247242577))),
    (Stop(name='Crescent / de Maisonneuve',
             gps=GPSPosition(latitude=45.49811161443597, longitude=-73.57761539518833))),
    (Stop(name="Gare d'autocars de Montréal (Berri / Ontario)",
             gps=GPSPosition(latitude=45.51689676614314, longitude=-73.5639488697052)))
]

TEST_DATA = [
    ("Ber", False, []),
    ("Ber", True, [SAMPLE_STOPS[10]]),
    ("Ste-Catherine / Dezery", False, [SAMPLE_STOPS[2]]),
    ("Ste-Catherine", True, [SAMPLE_STOPS[2], SAMPLE_STOPS[7], SAMPLE_STOPS[8]])
]

TEST_NAMES = [
    "Incomplete name, without regex: no stop found"
    , "Incomplete name, with regex: one stop found"
    , "Exact name, without regex: one stop found"
    , "Incomplete name, with regex: multiple stops found"
]


@pytest.mark.parametrize("name_to_find, regex, list_expected_stop", TEST_DATA, ids=TEST_NAMES)
def test_find_stops_matching_name(name_to_find, regex, list_expected_stop):
    list_found_stop = find_stops_matching_name(SAMPLE_STOPS, name_to_find, regex)
    assert list_found_stop == list_expected_stop
