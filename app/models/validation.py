from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import ValidationStatus


class ValidationResult(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    name: str

    status: ValidationStatus

    message: str

    details: dict = Field(default_factory=dict)