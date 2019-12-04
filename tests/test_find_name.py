import pytest

from finders.find_name import find_stops_matching_name
from finders.stops import BixiStop
from finders.gps import GPSPosition

SAMPLE_STOPS = [
    (BixiStop(name='de la Commune / Place Jacques-Cartier',
             gps=GPSPosition(latitude=45.50761009451047, longitude=-73.55183601379395), station_id='25', rental_method=['CREDITCARD', 'KEY'],capacity=89, is_kiosk=True)),
    (BixiStop(name='Métro Champ-de-Mars (Viger / Sanguinet)',
             gps=GPSPosition(latitude=45.51035067563653, longitude=-73.55650842189789), station_id='1',rental_method=['CREDITCARD', 'KEY'], capacity=33, is_kiosk=True)),
    (BixiStop(name='Ste-Catherine / Dezery',
             gps=GPSPosition(latitude=45.539385081961676, longitude=-73.54099988937377),station_id='2', rental_method=['CREDITCARD', 'KEY'], capacity=19, is_kiosk=True)),
    (BixiStop(name='Clark / Evans',
              gps=GPSPosition(latitude=45.51100666600306, longitude=-73.56760203838348),station_id='3', rental_method=['CREDITCARD', 'KEY'], capacity=19, is_kiosk=True)),
    (BixiStop(name='du Champ-de-Mars / Gosford',
             gps=GPSPosition(latitude=45.50965520472071, longitude=-73.55400860309601), station_id='4',rental_method=['CREDITCARD', 'KEY'], capacity=23, is_kiosk=True)),
    (BixiStop(name='Metcalfe / du Square-Dorchester',
             gps=GPSPosition(latitude=45.500208064155046, longitude=-73.57113786041737), station_id='5',rental_method=['CREDITCARD', 'KEY'], capacity=31, is_kiosk=True)),
    (BixiStop(name='18e avenue / Rosemont',
              gps=GPSPosition(latitude=45.55789545752947, longitude=-73.5765291005373),station_id='6', rental_method=['CREDITCARD', 'KEY'], capacity=31, is_kiosk=True)),
    (BixiStop(name="de l'Hôtel-de-Ville / Ste-Catherine",
             gps=GPSPosition(latitude=45.51166045593874, longitude=-73.56213569641113), station_id='7',rental_method=['CREDITCARD', 'KEY'], capacity=23, is_kiosk=True)),
    (BixiStop(name='Sanguinet / Ste-Catherine',
             gps=GPSPosition(latitude=45.51279685582333, longitude=-73.56146247242577), station_id='8',rental_method=['CREDITCARD', 'KEY'], capacity=27, is_kiosk=True)),
    (BixiStop(name='Crescent / de Maisonneuve',
             gps=GPSPosition(latitude=45.49811161443597, longitude=-73.57761539518833), station_id='9',rental_method=['CREDITCARD', 'KEY'], capacity=19, is_kiosk=True)),
    (BixiStop(name="Gare d'autocars de Montréal (Berri / Ontario)",
             gps=GPSPosition(latitude=45.51689676614314, longitude=-73.5639488697052), station_id='10',rental_method=['CREDITCARD', 'KEY'], capacity=15, is_kiosk=True))
]

TEST_DATA = [
    ("Ber", False, []),
    ("Ber", True, [SAMPLE_STOPS[10]]),
    ("Ste-Catherine", False, []),
    ("Ste-Catherine", True, [SAMPLE_STOPS[2], SAMPLE_STOPS[7], SAMPLE_STOPS[8]]),
    ("Ste-", False, []),
    ("Ste-", True, [SAMPLE_STOPS[2], SAMPLE_STOPS[7], SAMPLE_STOPS[8]]),
]


@pytest.mark.parametrize("name_to_find, regex, list_expected_stop", TEST_DATA)
def test_find_stops_matching_name(name_to_find, regex, list_expected_stop):
    list_found_stop = find_stops_matching_name(SAMPLE_STOPS, name_to_find, regex)
    assert list_found_stop == list_expected_stop
