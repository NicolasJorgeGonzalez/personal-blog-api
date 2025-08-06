from pydantic import BaseModel
from datetime import date

class Publication(BaseModel):
    id:str
    title:str
    content:str
    category:str
    tags:list(str)
    createdAt: date
    updatedAt: date
