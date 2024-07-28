from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ProfileType(Enum):
    MYSELF: str = "Myself"
    OTHERS: str = "Others"


class Gender(Enum):
    MALE: str = "Male"
    FEMALE: str = "Female"


class Profile(BaseModel):
    type: ProfileType
    age: int
    gender: Gender
    existing_conditions: Optional[List[str]]
    name: str
