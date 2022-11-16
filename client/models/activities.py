from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, date
from .base import Body, Root

@dataclass
class Activity(Body):
    activity_name: str
    activity_number: str
    activity_id: int
    modified_date_time: datetime
    activity_type_id: int
    activity_type: str
    parent_season_id: Optional[int]
    parent_season: Optional[str]
    child_season_id: Optional[int]
    child_season: Optional[str]
    activity_status_id: int
    activity_status: str
    activity_department_id: Optional[int] 
    activity_department: Optional[str]
    category_id: Optional[int]
    category: Optional[str]
    other_category_id: Optional[int]
    other_category: Optional[str]
    site_id: Optional[int]
    site_name: Optional[str]
    default_facilities: Optional[str]
    default_beginning_date: Optional[date]
    default_ending_date: Optional[date]
    default_pattern_dates: Optional[str]
    gender_id: int
    gender: str
    enroll_min: Optional[int]
    enroll_max: Optional[int]
    show_on_member_app: str
    image_on_member_app: str
    age_min_year: int
    age_min_month: int
    age_min_week: int
    age_max_year: int
    age_max_month: int
    age_max_week: int
    

@dataclass
class ActivityList(Root):
    body_type = Activity
