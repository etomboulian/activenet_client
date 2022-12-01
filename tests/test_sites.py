from . import ClientTestCase
from client.models import Site, SitesResponse

class TestSites(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.sites_data = self.client.get('sites')
        self.mock_sites_data = self.get_mock_sites_data()

    def test_sites_api_success(self):
        response_code = self.sites_data.headers.response_code
        self.assertEqual(response_code, '0000')

    def test_sites_api_return_type_data(self):
        data = self.sites_data
        self.assertIsInstance(data, SitesResponse)

    def test_sites_api_return_type_list(self):
        data = self.sites_data.body
        self.assertIsInstance(data, list)

    def test_sites_api_return_type_single(self):
        data = self.sites_data.body[0]
        self.assertIsInstance(data, Site)

    def test_sites_with_test_data(self):
        self.assertIsInstance(self.mock_sites_data, SitesResponse)