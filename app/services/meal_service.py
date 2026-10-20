from app.repositories.meal_repository import MealRepository
from app.schemas.meal import MealCreate, MealResponse
from typing import List, Optional

class MealService:
    def __init__(self):
        self.repository = MealRepository()

    def get_all_meals(self) -> List[MealResponse]:
        raw_meals = self.repository.get_all()
        return [MealResponse(**meal) for meal in raw_meals]

    def get_meal_by_id(self, meal_id: int) -> Optional[MealResponse]:
        raw_meal = self.repository.get_by_id(meal_id)
        if raw_meal:
            return MealResponse(**raw_meal)
        return None

    def create_meal(self, meal: MealCreate) -> MealResponse:
        created_meal = self.repository.create(meal)
        return MealResponse(**created_meal)
