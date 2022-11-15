from dataclasses import dataclass
from typing import List, Optional
from .base import Body, Root


@dataclass
class OrganizationDetails(Body):
    organization_id: int
    name: str
    time_zone: str
    logo_on_member_app: Optional[str]
    country: str
    retired: str
    cui_url: str


@dataclass
class Organization(Root):
    body_type = OrganizationDetails
    body: List[OrganizationDetails]