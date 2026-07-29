from pydantic import BaseModel
from typing import Literal

class CEODecision(BaseModel):
    next_agent: Literal[
        "planner",
        "cleaner",
        "feature_engineer",
        "evaluator",
        "visualization",
        "report_generator",
        "end",
    ]
    reason: str