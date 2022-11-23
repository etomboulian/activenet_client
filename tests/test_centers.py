from . import ClientTestCase
from client.models import Center, CentersResponse


class TestCenters(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.centers_data = self.client.get('centers')

    def test_centers_api_success(self):
        response_code = self.centers_data.headers.response_code
        self.assertEqual(response_code, '0000')
        
    def test_centers_api_return_type_data(self):
        self.assertIsInstance(self.centers_data, CentersResponse)

    def test_centers_api_return_type_list(self):
        list_data = self.centers_data.body
        self.assertIsInstance(list_data, list)

    def test_centers_api_return_type_single(self):
        center = self.centers_data.body[0]
        self.assertIsInstance(center, Center)