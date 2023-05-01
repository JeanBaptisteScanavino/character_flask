from enum import Enum
from typing import List

from pydantic import UUID4, BaseModel


class OriginEnum(str, Enum):
    DWARF = "DWARF"
    NO_SELECTION = "NO_SELECTION"


class GenderEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NO_SELECTION = "NO_SELECTION"


class WorkEnum(str, Enum):
    WARRIOR = "WARRIOR"
    NO_SELECTION = "NO_SELECTION"


class PyMoney(BaseModel):
    gold: int
    silver: int
    thritil: int
    berylium: int


class PyCaract(BaseModel):
    force: int
    intel: int
    charisma: int
    agility: int
    brave: int


class PyObjectInInventory(BaseModel):
    id: UUID4
    name: str


class PySkillsOnSheet(BaseModel):
    id: UUID4
    name: str


class PyCharacter(BaseModel):
    id: str | None
    name: str
    origin: OriginEnum = OriginEnum.NO_SELECTION
    gender: GenderEnum = GenderEnum.NO_SELECTION
    work: WorkEnum = WorkEnum.NO_SELECTION
    caract: PyCaract
    money: PyMoney
    XP: int
    level: int
    destiny_points: int
    inventory: List[UUID4] | List[PyObjectInInventory]
    skills: List[UUID4] | List[PySkillsOnSheet]
