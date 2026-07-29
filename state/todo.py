from pydantic import BaseModel
from typing import Literal
class TodoItem(BaseModel):
    task: str
    owner: Literal[
        "Cleaner",
        "Feature_Engineer",
        "Model_Builder",
        "Evaluator",
        "Visualization",
        "Report_Generator",
    ]
    status: Literal["Pending", "In_Progress", "Completed"]