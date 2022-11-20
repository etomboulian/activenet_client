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

    def validate_required_params(self, route: str, actual_params: dict):
        required_params = {field:field_type for (field, field_type) in self.routes[route]['parameters']['required']}
        return set(required_params.keys()).issubset(set(actual_params.keys()))

    @staticmethod
    def set_page_info_header(page_info: dict) -> str:
        page_info_header = {}
        for header, value in page_info.items():
            page_info_header[header] = str(value)

        return json.dumps(page_info_header)

    @staticmethod
    def set_url_params(existing_params: dict, new_params: dict):
        existing_params.update(new_params)
    
    def get(self, api_name, url_params=None, sort=None, page_info=None) -> 'Root':
        url, return_cls = self.find_route_info(api_name)
        http_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
        params = dict()
        
        if url_params:
            self.set_url_params(params, url_params)

        if sort:
            # TODO implement sort options
            pass

        if page_info:
            http_headers['page_info'] = self.set_page_info_header(page_info)

        params['api_key'] = self.api_key
        params['sig'] = self.generate_signature()
        
        resp = self.session.get(url, headers=http_headers, params=params)
        
        if resp.status_code == 200:
            return return_cls.from_dict(resp.json())
        else:
            raise Exception(f'{resp.status_code}, {resp.text}')