from pydantic import BaseModel
from typing import List
from state.todo import TodoItem

class PlannerOutput(BaseModel):
    todo_list: List[TodoItem]