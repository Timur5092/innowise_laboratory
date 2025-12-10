from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class Book(BookCreate):
    id: int

    class Config:
        from_attributes = True
