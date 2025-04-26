from pydantic import BaseModel
from typing import Optional

class FanBase(BaseModel):
    name: str
    username: str
    location: str
    preferences: dict

class FanCreate(FanBase):
    pass

class Fan(FanBase):
    id: int

    class Config:
        from_attributes = True  