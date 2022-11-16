import requests, time
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
        # self.org = 1 # Create an organization object here to hold org info

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
    
    def get(self, api_name, options=None) -> 'Root':
        url, return_cls = self.find_route_info(api_name)

        http_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }

        params = dict()
        
        if options:
            for k, v in options.items():
                params[k] = v

        params['api_key'] = self.api_key
        params['sig'] = self.generate_signature()
        
        resp = self.session.get(url, headers=http_headers, params=params)
        print(resp.url)
        if resp.status_code == 200:
            json_str = resp.json()
            return return_cls.from_dict(json_str)
        else:
            raise Exception(f'{resp.status_code}, {resp.text}')