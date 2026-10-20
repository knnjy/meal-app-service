from app.db.supabase import supabase_client
from app.schemas.meal import MealCreate
from typing import List, Dict, Any, Optional

class MealRepository:
    def __init__(self):
        self.table_name = "meal"

    def get_all(self) -> List[Dict[str, Any]]:
        response = supabase_client.table(self.table_name).select("*").order("id", desc=False).execute()
        return response.data

    def get_by_id(self, meal_id: int) -> Optional[Dict[str, Any]]:
        response = supabase_client.table(self.table_name).select("*").eq("id", meal_id).execute()
        if response.data:
            return response.data[0]
        return None

    def create(self, meal: MealCreate) -> Dict[str, Any]:
        response = supabase_client.table(self.table_name).insert({
            "meal_name": meal.meal_name,
            "category": meal.category
        }).execute()
        return response.data[0]
