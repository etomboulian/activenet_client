from unittest import TestCase
from dotenv import load_dotenv
from client import ApiClient
import os

load_dotenv()

org_name = os.environ.get('ORG_NAME')
country = os.environ.get('COUNTRY')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

class ClientTestCase(TestCase):
    def setUp(self) -> None:
        self.client = ApiClient(org_name, country, api_key, api_secret)
        return super().setUp()