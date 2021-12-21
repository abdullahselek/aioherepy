import unittest

from aioherepy.routing_api import RoutingApi


class RoutingApiTests(unittest.TestCase):
    def setUp(self):
        self._api = RoutingApi("api_key")

    def test_init(self):
        self.assertIsInstance(self._api, RoutingApi)
        self.assertEqual(self._api.api_key, "api_key")
        self.assertEqual(self._api.api_url, "https://router.hereapi.com/v8/routes")
