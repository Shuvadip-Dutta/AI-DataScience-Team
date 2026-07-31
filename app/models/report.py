from enum import Enum

from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import ReportType

class Report(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    title: str

    report_type: ReportType

    content: str

    generated_by: str

    metadata: dict = Field(default_factory=dict)