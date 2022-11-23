from dataclasses import dataclass
from typing import List, Optional
from .base import Body, Root


@dataclass
class Organization(Body):
    organization_id: int
    name: str
    time_zone: str
    logo_on_member_app: Optional[str]
    country: str
    retired: str
    cui_url: str


@dataclass
class OrganizationResponse(Root):
    body_type = Organization
    body: List[Organization]