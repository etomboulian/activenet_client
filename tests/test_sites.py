import unittest, os
from dotenv import load_dotenv
from client import ApiClient

from client.models import Site, SiteList

load_dotenv()

class TestSites(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ApiClient(os.environ.get('ORG_NAME'), os.environ.get('API_KEY'), os.environ.get('API_SECRET'))
        self.sites_data = self.client.get('sites')
        return super().setUp()

    def test_sites_api_success(self):
        response_code = self.sites_data.headers.response_code
        self.assertEqual(response_code, '0000')

    def test_sites_api_return_type_data(self):
        data = self.sites_data
        self.assertIsInstance(data, SiteList)

    def test_sites_api_return_type_list(self):
        data = self.sites_data.body
        self.assertIsInstance(data, list)

    def test_sites_api_return_type_single(self):
        data = self.sites_data.body[0]
        self.assertIsInstance(data, Site)
        