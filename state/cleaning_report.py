from pydantic import BaseModel

class CleaningReport(BaseModel):
    rows_before: int
    rows_after: int

    columns: int

    missing_values_removed: int

    duplicates_removed: int

    status: str