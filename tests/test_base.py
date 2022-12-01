from unittest import TestCase
from dotenv import load_dotenv
from client import ApiClient
import os, json
from client.models import *

load_dotenv()

org_name = os.environ.get('ORG_NAME')
country = os.environ.get('COUNTRY')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

mock_data_path_base = 'tests\\test_data'

class ClientTestCase(TestCase):
    def setUp(self) -> None:
        self.client = ApiClient(org_name, country, api_key, api_secret)
        return super().setUp()

    def get_mock_data_filename(self, api_name) -> str:
        return os.path.join(mock_data_path_base, f"{api_name}.json")

    def get_mock_organization_data(self) -> 'OrganizationResponse':
        with open(self.get_mock_data_filename('organization'), 'r') as f:
            return OrganizationResponse.from_dict(json.load(f))

    def get_mock_centers_data(self) -> 'CentersResponse':
        with open(self.get_mock_data_filename('centers'), 'r') as f:
            return CentersResponse.from_dict(json.load(f))

    def get_mock_sites_data(self) -> 'SitesResponse':
        with open(self.get_mock_data_filename('sites'), 'r') as f:
            return SitesResponse.from_dict(json.load(f))

    def get_mock_seasons_data(self) -> 'SeasonsResponse':
        with open(self.get_mock_data_filename('seasons'), 'r') as f:
            return SeasonsResponse.from_dict(json.load(f))

    def get_mock_skills_data(self) -> 'SkillsResponse':
        with open(self.get_mock_data_filename('skills'), 'r') as f:
            return SkillsResponse.from_dict(json.load(f)) 

    def get_mock_skip_dates_data(self) -> 'SkipDatesResponse':
        with open(self.get_mock_data_filename('skip_dates'), 'r') as f:
            return SkipDatesResponse.from_dict(json.load(f))
    