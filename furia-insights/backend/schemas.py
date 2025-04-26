from pydantic import BaseModel
from typing import Dict

class FanBase(BaseModel):
    name: str
    username: str
    location: str
    preferences: Dict[str, int]

class FanCreate(FanBase):
    pass

class FanOut(FanBase):
    id: int

    class Config:
        from_attributes = True
