from . import ClientTestCase
from client.models import Season, SeasonsResponse

class TestSeasons(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.seasons_data = self.client.get('seasons')
        self.mock_seasons_data = self.get_mock_seasons_data()

    def test_seasons_api_success(self):
        response_code = self.seasons_data.headers.response_code
        self.assertEqual(response_code, '0000')

    def test_seasons_api_return_type_data(self):
        self.assertIsInstance(self.seasons_data, SeasonsResponse)

    def test_seasons_api_return_type_list(self):
        self.assertIsInstance(self.seasons_data.body, list)
    
    def test_seasons_api_return_type_single(self):
        self.assertIsInstance(self.seasons_data.body[0], Season)

    def test_seasons_with_test_data(self):
        self.assertIsInstance(self.mock_seasons_data, SeasonsResponse)