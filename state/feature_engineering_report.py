from pydantic import BaseModel
class FeatureEngineeringReport(BaseModel):
    encoded_columns: list[str]
    dropped_columns: list[str]
    created_features: list[str]
    status: str