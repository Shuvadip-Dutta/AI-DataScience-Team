from typing import Optional, List
import pandas as pd
from langgraph.graph import MessagesState

from state.todo import TodoItem
from state.ceo import CEODecision
from state.cleaning_report import CleaningReport
from state.feature_engineering_report import FeatureEngineeringReport
from state.evaluation_report import EvaluationReport
from state.visualization_report import VisualizationReport
from state.report_generator_report import ReportGeneratorReport

class CEOState(MessagesState):
    """Shared state used by all AI Data Science Team agents."""

    # User Input
    user_request: str

    # Dataset
    dataset_path: Optional[str]
    dataframe: pd.DataFrame | None

    # Planner
    todo_list: List[TodoItem]
    ceo_decision: CEODecision

    # Processed Data
    engineered_dataframe: pd.DataFrame | None

    # Reports
    cleaning_report: CleaningReport | None
    feature_engineering_report: FeatureEngineeringReport | None
    evaluation_report: EvaluationReport | None
    visualization_report: VisualizationReport | None
    report_generator_report: ReportGeneratorReport | None
