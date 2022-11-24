import requests, time, json
from hashlib import sha256
from .routes import routes
from .models.base import Root

class BaseClient:
    def __init__(self, org_name, api_key, shared_secret):
        self.org_name = org_name
        self.api_key = api_key
        self.shared_secret = shared_secret
        self.api_base = f"https://api.amp.active.com/anet-systemapi-sec/{org_name}/api/v1/"
        self.routes = routes
        self.session = requests.Session()
        
    def __del__(self):
        self.session.close()

    # Generates the value for the sig parameter from the api_key and shared_secret
    def generate_signature(self) -> str: 
        seconds = int(time.time())
        message = self.api_key + self.shared_secret + str(seconds)
        message_bytes = message.encode()
        signature = sha256(message_bytes).hexdigest()
        return signature

    def find_route_info(self, api_name):
        try:
            url = self.api_base + self.routes[api_name]['endpoint']
            return_cls = self.routes[api_name]['return_class']
            return url, return_cls
        except Exception as e:
            raise e

    def check_connection(self):
        return self.get('organization')

    def validate_route_params(self, route: str, actual_params: dict) -> bool:
        optional_params = {
            field:details['type'] for field, details 
            in self.routes[route]['optional_parameters'].items()
        }
        is_valid_params = set(optional_params.keys()).issubset(set(actual_params.keys()))
        return is_valid_params

    def validate_sort_params(self, route: str, sort_params: dict) -> bool:
        pass

    def set_sort_header_params(headers: dict, sort_params: dict):
        headers.update(sort_params)

    @staticmethod
    def set_page_info_header(page_info: dict) -> str:
        page_info_header = {}
        for header, value in page_info.items():
            page_info_header[header] = str(value)
        return json.dumps(page_info_header)

    @staticmethod
    def set_url_params(existing_params: dict, new_params: dict):
        existing_params.update(new_params)

    @staticmethod
    def check_response(result, return_cls):
        # Throw exception if we get anything other than the expected success http status code (200)
        if result.status_code == 200:
            result = return_cls.from_dict(result.json())
            # 0000 = Success, 0001 = No Results Found
            if result.headers.response_code == '0000':     
                return result
            elif result.headers.response_code == '0001':
                return None
            else:
                raise Exception(result.headers.__dict__) 
        else:
            raise Exception(result.json())

    def get(self, api_name, filters=None, sort=None, page_info=None) -> 'Root':
        url, return_cls = self.find_route_info(api_name)
        http_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
        params = dict()
    
        if filters:
            try:
                if self.validate_route_params(api_name, filters):
                    self.set_url_params(params, filters)                
            except Exception as e:
                raise e

        if sort:
            try:
                if self.validate_sort_params(api_name, sort):
                    self.set_sort_header_params(http_headers, sort)
            except Exception as e:
                raise e

        if page_info:
            http_headers['page_info'] = self.set_page_info_header(page_info)

        params['api_key'] = self.api_key
        params['sig'] = self.generate_signature()
        
        resp = self.session.get(url, headers=http_headers, params=params)
        try:
            result = self.check_response(resp, return_cls)
        except Exception as e:
            raise e

        return result