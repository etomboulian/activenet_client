from .base import Body, Root
from dataclasses import dataclass
from typing import List, Optional
from datetime import date, datetime


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
class SeasonList(Root):
    body_type = Season