from pydantic import BaseModel
class ReportGeneratorReport(BaseModel):

    report_path: str

    sections: list[str]

    status: str