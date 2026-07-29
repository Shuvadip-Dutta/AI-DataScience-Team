from pydantic import BaseModel
class EvaluationReport(BaseModel):

    rows: int

    columns: int

    numerical_columns: list[str]

    categorical_columns: list[str]

    missing_values: int

    duplicate_rows: int

    status: str