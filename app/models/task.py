"""
Task model for the AI Data Science Team workflow.

A Task represents the smallest executable unit in the system.
Tasks are created by the Planner and executed by the Execution Manager.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import TaskStatus, TaskPriority, ToolType



class Task(BaseModel):
    """
    Represents a single executable task in the workflow.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    id: str = Field(
        ...,
        description="Unique identifier for the task.",
    )

    name: str = Field(
        ...,
        description="Human-readable task name.",
    )

    description: str = Field(
        default="",
        description="Detailed description of the task.",
    )

    status: TaskStatus = Field(
        default=TaskStatus.PENDING,
        description="Current execution status.",
    )

    priority: TaskPriority = Field(
        default=TaskPriority.MEDIUM,
        description="Scheduling priority.",
    )

    dependencies: list[str] = Field(
        default_factory=list,
        description="IDs of tasks that must complete first.",
    )

    assigned_tool: ToolType | None = Field(
        default=None,
        description="Tool responsible for executing this task.",
    )

    input_data: dict[str, Any] = Field(
        default_factory=dict,
        description="Input required for execution.",
    )

    output_data: dict[str, Any] = Field(
        default_factory=dict,
        description="Output generated after execution.",
    )

    retry_count: int = Field(
        default=0,
        ge=0,
        description="Number of retries attempted.",
    )

    max_retries: int = Field(
        default=2,
        ge=0,
        description="Maximum retries allowed.",
    )

    error_message: str | None = Field(
        default=None,
        description="Failure reason, if any.",
    )

    execution_time: float | None = Field(
        default=None,
        ge=0,
        description="Execution time in seconds.",
    )