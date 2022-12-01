import requests, time, json
from requests.adapters import HTTPAdapter, Retry
from hashlib import sha256
from .routes import routes
from .models.base import Root
from typing import Tuple
from .data import PageInfo, SortInfo

USA_API_BASE = "https://api.amp.active.com/anet-systemapi-sec/"
CAN_API_BASE = "https://api.amp.active.com/anet-systemapi-sec/"

class BaseClient:
    def __init__(self, org_name, country, api_key, shared_secret):
        if country == 'USA':
            API_BASE = USA_API_BASE
        elif country == 'CAN':
            API_BASE = CAN_API_BASE
        else:
            raise Exception(f'Unable to determine the url for the country: {country}')

        self.org_name = org_name
        self.api_key = api_key
        self.shared_secret = shared_secret
        self.api_base =  f"{API_BASE}/{org_name}/api/v1/"
        self.routes = routes
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.25, status_forcelist=(403, 500, 502, 503, 504))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def __del__(self):
        self.session.close()

    # Generates the signature from the api_key and shared_secret
    def generate_signature(self) -> str: 
        seconds = int(time.time())
        message = self.api_key + self.shared_secret + str(seconds)
        message_bytes = message.encode()
        signature = sha256(message_bytes).hexdigest()
        return signature

    # Gets the url for the selected api endpoint and its return class
    def find_route_info(self, api_name) -> Tuple[str, Root]:
        try:
            url = self.api_base + self.routes[api_name]['endpoint']
            return_cls = self.routes[api_name]['return_class']
            return url, return_cls
        except Exception as e:
            raise e

    # Checks the connection status with the server
    def check_connection(self) -> bool:
        return self.get('organization').headers.response_code == '0000'

    # Checks to see if the given filter params are valid optional params for the api endpoint
    def validate_route_params(self, route: str, actual_params: dict) -> bool:
        optional_params = {
            field:details['type'] for field, details 
            in self.routes[route]['optional_parameters'].items()
        }
        is_valid_params = set(optional_params.keys()).issubset(set(actual_params.keys()))
        return is_valid_params

    # Check to see if the given sort option is valid for the api endpoint
    def validate_sort_params(self, route: str, sort_params: dict) -> bool:
        return True

    # Generates the page info header for pagination and sorting
    @staticmethod
    def set_page_info_header(page_info: PageInfo, sort_by: SortInfo) -> str:
        page_info_header = {}

        if page_info:
            page_info_header.setdefault('page_number', str(page_info.page_number))
            page_info_header.setdefault('total_records_per_page', str(page_info.total_records_per_page))
            
        if sort_by:
            page_info_header.setdefault('order_by', str(sort_by.order_by))
            page_info_header.setdefault('order_option', str(sort_by.order_option))

        return json.dumps(page_info_header)

    # Check the response to ensure that we are getting a success response
    @classmethod
    def check_response(cls, return_cls: Root, result: str):
        # Throw exception if we get anything other than the expected success http status code (200)
        if result.status_code == 200:
            result = cls.deserialize_response(return_cls, result)
            # 0000 = Success 
            if result.headers.response_code == '0000':     
                return result
            # 0001 = No Results Found
            elif result.headers.response_code == '0001':
                return None
            else:
                raise Exception(result.headers.__dict__) 
        else:
            raise Exception(result.__dict__)

    @classmethod
    def deserialize_response(cls, return_cls, data):
        return return_cls.from_dict(data.json())

    # Gets data from the endpoint and returns a constructed model class for the response
    def get(self, api_name, filters: dict=None, sort_by: SortInfo=None, page_info=None, **kwargs) -> 'Root':
        url, return_cls = self.find_route_info(api_name)
        
        http_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }

        params = {
            'api_key': self.api_key,
            'sig': self.generate_signature()
        }
    
        if filters:
            if self.validate_route_params(api_name, filters):
                params.update(filters)                
            else:
                raise Exception("Filter Validation Failed")

        if sort_by:
            if self.validate_sort_params(api_name, sort_by):
                http_headers['page_info'] = json.dumps({
                    'order_option': sort_by.order_option,
                    'order_by': sort_by.order_by
                    })
            else:
                raise Exception("Sort Option Validation Failed")

        if page_info or sort_by:
            http_headers['page_info'] = self.set_page_info_header(page_info, sort_by)
        
        resp = self.session.get(url, headers=http_headers, params=params)

        if kwargs.get('print_url', None):
            print(resp.request.url)

        try:
            result = self.check_response(return_cls, resp)
        except Exception as e:
            raise e

        return result
        