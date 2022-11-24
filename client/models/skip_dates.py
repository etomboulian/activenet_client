from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, time, datetime

from . import DATE_FORMAT_STR, TIME_FORMAT_STR


@dataclass
class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: Optional[date]
    time_from: Optional[time]
    date_to: Optional[date]
    time_to: Optional[time]

    def __post_init__(self):
        self.date_from = datetime.strptime(self.date_from, DATE_FORMAT_STR) if self.date_from else self.date_from
        self.date_to = datetime.strptime(self.date_to, DATE_FORMAT_STR) if self.date_to else self.date_to
        self.time_from = datetime.strptime(self.time_from, TIME_FORMAT_STR).time() if self.time_from else self.time_from
        self.time_to = datetime.strptime(self.time_to, TIME_FORMAT_STR).time() if self.time_to else self.time_to


@dataclass
class SkipDatesResponse(Root):
    body_type = SkipDate
    body: List[SkipDate]