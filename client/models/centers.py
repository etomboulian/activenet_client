from dataclasses import dataclass
from typing import List, Optional
from datetime import time, datetime
from .base import Root, Body

@dataclass
class DefaultHoursOfOperation:
    default_opens: Optional[time]
    default_closes: Optional[time]

    def __post_init__(self):
        self.default_opens = datetime.strptime(self.default_opens, '%H:%M:%S').time()
        self.default_closes = datetime.strptime(self.default_closes, '%H:%M:%S').time()

@dataclass
class HoursOfOperation:
    closed_all_day: bool
    opens: Optional[time]
    closes: Optional[time]

    def __post_init__(self):
        self.opens = datetime.strptime(self.opens, '%H:%M:%S').time() if self.opens else None
        self.closes = datetime.strptime(self.closes, '%H:%M:%S').time() if self.closes else None

@dataclass
class Center(Body):
    center_id: int
    center_name: str
    prevent_further_use: bool
    site_id: int
    site_name: str
    show_on_member_app: str
    member_app_image: Optional[str]
    latitude: float
    longitude: float
    description: Optional[str]
    customer_webpage_url: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip_code: Optional[str]
    country: Optional[str]
    phone1: Optional[str]
    phone2: Optional[str]
    fax: Optional[str]
    default_hours_of_operation: DefaultHoursOfOperation
    Sunday_hours_of_operation: HoursOfOperation
    Monday_hours_of_operation: HoursOfOperation
    Tuesday_hours_of_operation: HoursOfOperation
    Wednesday_hours_of_operation: HoursOfOperation
    Thursday_hours_of_operation: HoursOfOperation
    Friday_hours_of_operation: HoursOfOperation
    Saturday_hours_of_operation: HoursOfOperation

    def __post_init__(self):
        self.Sunday_hours_of_operation = HoursOfOperation(**self.Sunday_hours_of_operation)
        self.Monday_hours_of_operation = HoursOfOperation(**self.Monday_hours_of_operation)
        self.Tuesday_hours_of_operation = HoursOfOperation(**self.Tuesday_hours_of_operation)
        self.Wednesday_hours_of_operation = HoursOfOperation(**self.Wednesday_hours_of_operation)
        self.Thursday_hours_of_operation = HoursOfOperation(**self.Thursday_hours_of_operation)
        self.Friday_hours_of_operation = HoursOfOperation(**self.Friday_hours_of_operation)
        self.Saturday_hours_of_operation = HoursOfOperation(**self.Saturday_hours_of_operation)

@dataclass
class Centers(Root):
    body_type = Center


