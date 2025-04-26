import unittest
from mbta_helper import get_lat_long, get_weather, get_events

class TestMbtaHelper(unittest.TestCase):

    def test_get_lat_long(self):
        lat, lon = get_lat_long("Fenway Park")
        self.assertTrue(lat and lon)

    def test_get_weather(self):
        weather = get_weather(42.3467, -71.0972)
        self.assertIn("description", weather)
        self.assertIn("temperature", weather)

    def test_get_events(self):
        events = get_events(42.3467, -71.0972)
        self.assertIsInstance(events, list)

if __name__ == '__main__':
    unittest.main()
