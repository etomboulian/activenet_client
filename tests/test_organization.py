from . import ClientTestCase
from client.models import Organization, OrganizationResponse

class TestOrganization(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.organization_data = self.client.get('organization')

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