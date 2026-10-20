from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.meal import MealCreate, MealResponse
from app.services.meal_service import MealService

router = APIRouter(prefix="/meals", tags=["Meals"])
meal_service = MealService()

@router.get("/", response_model=List[MealResponse])
def get_meals():
    return meal_service.get_all_meals()

@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: int):
    meal = meal_service.get_meal_by_id(meal_id)
    if not meal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meal not found")
    return meal

@router.post("/", response_model=MealResponse, status_code=status.HTTP_201_CREATED)
def create_meal(meal: MealCreate):
    return meal_service.create_meal(meal)
