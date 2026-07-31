from pydantic import BaseModel
class VisualizationReport(BaseModel):

    charts_created: list[str]

    saved_files: list[str]
    
    total_charts: int

    status: str