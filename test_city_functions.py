import unittest

from  city_functions import get_formatted_name_city

class CityNameTest(unittest.TestCase):
    def test_city_country(self):
        full_name_city = get_formatted_name_city("moscow", "russia")
        self.assertEqual(full_name_city, "Moscow, Russia")
    def test_city_country_population(self):
        full_name_city = get_formatted_name_city("moscow", "russia", 15000000)
        self.assertEqual(full_name_city, "Moscow, Russia Population - 15000000" )
