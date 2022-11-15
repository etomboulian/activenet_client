from dataclasses import dataclass
from .base import Body, Root
from typing import List, Optional


@dataclass
class Site(Body):
    site_id: int
    site_name: str
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    country: Optional[str]
    geographic_area: Optional[str]
    email_address: Optional[str]


@dataclass
class Sites(Root):
    body_type = Site
    body: List[Site]
