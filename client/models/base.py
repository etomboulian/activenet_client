from dataclasses import dataclass
from typing import Dict, List, Any, Optional

@dataclass
class PageInfo:
    order_by: str
    page_number: int
    total_page: int
    order_option: str
    total_records: int
    total_records_per_page: int

@dataclass
class Headers:
    response_code: str
    response_message: str
    page_info: Optional[PageInfo] = None

    @classmethod
    def from_dict(cls, d: dict) -> 'Headers':
        if type(d).__name__ == 'dict':
            _response_code = d.get('response_code')
            _response_message = d.get('response_message')
            _page_info = d.get('page_info')
            return cls(
                response_code=_response_code, 
                response_message=_response_message,
                page_info = _page_info
                )
        elif type(d).__name__ == 'list':
            raise Exception("method from_dict expects a dict but got a list instead")
        else:
            return d
            
@dataclass
class Body:
    @classmethod
    def from_dict(cls, d: dict):
        if type(d).__name__ == 'dict':
            return cls(**d)
        elif type(d).__name__ == 'list':
            raise Exception("method from_dict expects a dict but got a list instead")
        else:
            return d

@dataclass
class Root:
    body_type = Body
    headers: Headers
    body: List[body_type]

    @classmethod
    def from_dict(cls, d : dict) -> Any :
        _headers = Headers.from_dict(d.get('headers'))
        _body = [cls.body_type.from_dict(item) for item in d.get('body')]
        return cls(headers=_headers, body=_body)