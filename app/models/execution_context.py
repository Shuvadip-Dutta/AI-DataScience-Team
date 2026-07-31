"""
Execution context shared across the entire workflow.
ExecutionContext
│
├── Dataset
├── Dataset Profile
├── Execution Plan
├── Current Task
├── Completed Tasks
├── Failed Tasks
├── Validation Results
├── Reports
├── Metrics
├── Reflection History
├── Shared Memory
└── Workflow Status
"""

from typing import Any

from enum import Enum
import pandas as pd
from pydantic import BaseModel, ConfigDict, Field


from app.models.dataset_profile import DatasetProfile
from app.models.execution_plan import ExecutionPlan
from app.models.metrics import Metrics
from app.models.report import Report
from app.models.task import Task
from app.models.validation import ValidationResult
from app.models.enums import WorkflowStatus

class ExecutionContext(BaseModel):
    """
    Central state shared by every component in the workflow.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="forbid",
    )

    # -----------------------
    # Dataset
    # -----------------------

    dataset_name: str

    dataset: pd.DataFrame | None = None

    dataset_profile: DatasetProfile | None = None

    # -----------------------
    # Planning
    # -----------------------

    execution_plan: ExecutionPlan | None = None

    # -----------------------
    # Execution
    # -----------------------

    current_task: Task | None = None

    completed_tasks: list[Task] = Field(default_factory=list)

    failed_tasks: list[Task] = Field(default_factory=list)

    workflow_status: WorkflowStatus = WorkflowStatus.NOT_STARTED

    # -----------------------
    # Validation
    # -----------------------

    validation_results: list[ValidationResult] = Field(default_factory=list)

    # -----------------------
    # Reports
    # -----------------------

    reports: list[Report] = Field(default_factory=list)

    # -----------------------
    # Metrics
    # -----------------------

    metrics: Metrics = Field(default_factory=Metrics)

    # -----------------------
    # Reflection
    # -----------------------

    reflection_notes: list[str] = Field(default_factory=list)

    # -----------------------
    # Shared Runtime Storage
    # -----------------------

    shared_memory: dict[str, Any] = Field(default_factory=dict)