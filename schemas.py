from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str