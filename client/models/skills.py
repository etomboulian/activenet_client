from dataclasses import dataclass
from typing import List
from .base import Body, Root


@dataclass
class Skill(Body):
    skill_id: int
    skill_title: str
    skill_description: str
    available_for: str


@dataclass
class SkillsResponse(Root):
    body_type = Skill
    body: List[Skill]