from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    id: int
    user: str
    password: str


class ReadStudents(BaseModel):
    id: int
    user: str
    password: str
    class Config:
        from_attributes = True




class PostStudents(BaseModel):
    id: str
    user: str
    password: str

    class Config:
        from_attributes = True

