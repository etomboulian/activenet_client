from . import ClientTestCase
from client.models import SkipDate
from client.api_client import PaginatedResult


class TestSkipDates(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.skipdates_data = self.client.GetSkipDates(10)

    def test_skipdates_api_success(self):
        self.assertEqual(self.skipdates_data.headers.response_code, '0000')

    def test_skipdates_api_return_type_data(self):
        self.assertIsInstance(self.skipdates_data, PaginatedResult)
    
    def test_skipdates_api_return_type_list(self):
        self.assertIsInstance(self.skipdates_data._data, list)

    def test_skipdates_api_return_type_single(self):
        self.assertIsInstance(self.skipdates_data[0], SkipDate)

    def test_skipdates_api_data_with_filter(self):
        data = self.client.GetSkipDates(10, sort_by=('start_date', 'DESC'))
        
