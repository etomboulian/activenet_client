from . import ClientTestCase
from client.models import Organization, OrganizationResponse
from client.routes import routes
import json

class TestOrganization(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.organization_data = self.client.get('organization')
        self.mock_organization_data = self.get_mock_organization_data()

    def test_organization_api_success(self):
        data = self.organization_data.headers
        self.assertEqual(data.response_code, '0000')

    def test_organization_api_return_type_data(self):
        data = self.organization_data
        self.assertIsInstance(data, OrganizationResponse)

    def test_organization_api_return_type_list(self):
        data = self.organization_data.body
        self.assertIsInstance(data, list)

    def test_organization_api_return_type_single(self):
        data = self.organization_data.body[0]
        self.assertIsInstance(data, Organization)

    def test_organization_with_test_data(self):
        self.assertIsInstance(self.mock_organization_data, OrganizationResponse)
        