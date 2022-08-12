from typing import Optional

from pydantic import BaseModel, validator


class NameForm(BaseModel):
    name: str
    age: int
    filepath: Optional[str]

    @validator("name")
    @classmethod
    def name_lenght(cls, value):
        if not value:
            raise ValueError("Name is required")
        return value
