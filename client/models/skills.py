from dataclasses import dataclass
from typing import List
from .base import Body, Root
#
# {
# "skill_id":4,
# "skill_title":"CPR Certification",
# "skill_description":"CPR and First Aid",
# "available_for":"Activities,Customers"
# }

@dataclass
class Skill(Body):
    skill_id: int
    skill_title: str
    skill_description: str
    available_for: str

@dataclass
class Skills(Root):
    body_type = Skill
    body: List[Skill]