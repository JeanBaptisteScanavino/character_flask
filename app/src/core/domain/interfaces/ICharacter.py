from enum import Enum

from pydantic import BaseModel


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

class ICharacter(BaseModel):
    id: int | None
    name: str
    origin: OriginEnum.NO_SELECTION
    gender: GenderEnum.NO_SELECTION
    work: WorkEnum.NO_SELECTION