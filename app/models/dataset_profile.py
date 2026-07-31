"""
Dataset profile model.

Contains metadata and statistics about the dataset.
"""

from pydantic import BaseModel, ConfigDict, Field


class DatasetProfile(BaseModel):
    """Summary information about the dataset."""

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    rows: int = Field(..., ge=0)
    columns: int = Field(..., ge=0)

    column_names: list[str] = Field(default_factory=list)

    numerical_columns: list[str] = Field(default_factory=list)
    categorical_columns: list[str] = Field(default_factory=list)

    missing_values: dict[str, int] = Field(default_factory=dict)

    duplicate_rows: int = Field(default=0, ge=0)

    target_column: str | None = None