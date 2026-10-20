from pydantic import BaseModel
from typing import Optional

# Base schema for shared attributes
class MealBase(BaseModel):
    meal_name: str
    category: str

# Schema for creating a new meal (Request payload)
class MealCreate(MealBase):
    pass

# Schema for returning meal details (Response payload)
class MealResponse(MealBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True
