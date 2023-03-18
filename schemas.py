from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str

class User(UserCreate):
    id: int
    class Config:
        orm_mode = True

