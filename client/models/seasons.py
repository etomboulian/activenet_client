from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, datetime

from . import DATETIME_FORMAT_STR


@dataclass
class BaseSeason:
    start_date: date
    end_date: date
    prevent_further_use: bool
    first_date_in_person: Optional[datetime]
    first_date_in_person_non_residents: Optional[datetime]
    first_date_in_person_members: Optional[datetime]
    last_date_in_person: Optional[datetime]
    first_date_on_internet: Optional[datetime]
    first_date_on_internet_non_residents: Optional[datetime]
    first_date_on_internet_members: Optional[datetime]
    last_date_on_internet: Optional[datetime]

    def __post_init__(self):
        self.first_date_in_person = datetime.strptime(self.first_date_in_person, DATETIME_FORMAT_STR) if self.first_date_in_person else self.first_date_in_person
        self.first_date_in_person_non_residents = datetime.strptime(self.first_date_in_person_non_residents, DATETIME_FORMAT_STR) if self.first_date_in_person_non_residents else self.first_date_in_person_non_residents
        self.first_date_in_person_members = datetime.strptime(self.first_date_in_person_members, DATETIME_FORMAT_STR) if self.first_date_in_person_members else self.first_date_in_person_members
        self.last_date_in_person = datetime.strptime(self.last_date_in_person, DATETIME_FORMAT_STR) if self.last_date_in_person else self.last_date_in_person
        self.first_date_on_internet = datetime.strptime(self.first_date_on_internet, DATETIME_FORMAT_STR) if self.first_date_on_internet else self.first_date_on_internet
        self.first_date_on_internet_non_residents = datetime.strptime(self.first_date_on_internet_non_residents, DATETIME_FORMAT_STR) if self.first_date_on_internet_non_residents else self.first_date_on_internet_non_residents
        self.first_date_on_internet_members = datetime.strptime(self.first_date_on_internet_members, DATETIME_FORMAT_STR) if self.first_date_on_internet_members else self.first_date_on_internet_members
        self.last_date_on_internet = datetime.strptime(self.last_date_on_internet, DATETIME_FORMAT_STR) if self.last_date_on_internet else self.last_date_on_internet


@dataclass
class ChildSeason(BaseSeason):
    child_season_id: int
    child_season: str


@dataclass
class Season(Body, BaseSeason):
    season_id: int
    season_name: str
    child_season: List[ChildSeason]
    site_id: int
    

    def __post_init__(self):
        child_seasons = []
        for item in self.child_season:
            child_seasons.append(ChildSeason(**item))
        self.child_season = child_seasons


@dataclass
class SeasonsResponse(Root):
    body_type = Season
    body: List[Season]