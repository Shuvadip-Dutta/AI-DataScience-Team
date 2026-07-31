"""
Cleaning report model.

Contains information about the data cleaning process.
"""

from pydantic import BaseModel, ConfigDict, Field


class CleaningReport(BaseModel):
    """
    Summary of data cleaning operations.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    rows_before: int = Field(..., ge=0)
    rows_after: int = Field(..., ge=0)

    duplicate_rows_removed: int = Field(default=0, ge=0)

    missing_values_before: int = Field(default=0, ge=0)
    missing_values_after: int = Field(default=0, ge=0)

    columns: int = Field(..., ge=0)