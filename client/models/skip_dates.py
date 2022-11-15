from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, time


# {
# "response_code":"0000",
# "response_message":"Successful",
# "page_info":{
# "order_by":
# "start_date",
# "page_number":1,
# "total_page":1,
# "order_option":"ASC",
# "total_records":3,
# "total_records_per_page":50}},
# "body":[
# {"skip_date_description":"New Year's Day",
# "skip_every_year":true,
# "date_from":"2010-01-01",
# "time_from":null,
# "date_to":"2010-01-02",
# "time_to":null
# }
@dataclass
class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: Optional[date]
    time_from: Optional[time]
    date_to: Optional[date]
    time_to: Optional[time]

@dataclass
class SkipDates(Root):
    body_type = SkipDate
    body: List[SkipDate]