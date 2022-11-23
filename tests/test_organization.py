import unittest, os
from dotenv import load_dotenv
from client import ApiClient
from typing import List

from client.models import Organization, OrganizationList

org_name = 'ljsupport12'
load_dotenv()

class TestOrganization(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ApiClient(org_name, os.environ.get('API_KEY'), os.environ.get('API_SECRET') )
        self.organization_data = self.client.get('organization')
        return super().setUp()

    def test_organization_api_success(self):
        data = self.organization_data.headers
        self.assertEqual(data.response_code, '0000')

    def test_organization_api_return_type_data(self):
        data = self.organization_data
        self.assertIsInstance(data, OrganizationList)

    def test_organization_api_return_type_list(self):
        data = self.organization_data.body
        self.assertIsInstance(data, list)

    def test_organization_api_return_type_single(self):
        data = self.organization_data.body[0]
        self.assertIsInstance(data, Organization)