from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, time


@dataclass
class SkipDate(Body):
    skip_date_description: str
    skip_every_year: bool
    date_from: Optional[date]
    time_from: Optional[time]
    date_to: Optional[date]
    time_to: Optional[time]

@dataclass
class SkipDateList(Root):
    body_type = SkipDate
    body: List[SkipDate]