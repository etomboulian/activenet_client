from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, time, datetime


@dataclass
class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: Optional[date]
    time_from: Optional[time]
    date_to: Optional[date]
    time_to: Optional[time]

    def __post_init__(self):
        self.date_from = datetime.strptime(self.date_from, '%Y-%m-%d')
        self.date_to = datetime.strptime(self.date_to, '%Y-%m-%d')
        self.time_from = datetime.strptime(self.time_from, '%H:%M:%S').time() if self.time_from else self.time_from
        self.time_to = datetime.strptime(self.time_to, '%H:%M:%S').time() if self.time_to else self.time_to

@dataclass
class SkipDateList(Root):
    body_type = SkipDate
    body: List[SkipDate]