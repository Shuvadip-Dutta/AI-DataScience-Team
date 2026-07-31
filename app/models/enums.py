from enum import Enum

class TaskStatus(str, Enum):
    """Represents the execution status of a task."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    RETRYING = "retrying"
    
class TaskPriority(str, Enum):
    """Represents the scheduling priority of a task."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    


class ToolType(str, Enum):
    DATASET_PROFILER = "dataset_profiler"
    DATA_CLEANER = "data_cleaner"
    FEATURE_ENGINEER = "feature_engineer"
    MODEL_BUILDER = "model_builder"
    EVALUATOR = "evaluator"
    VISUALIZER = "visualizer"
    REPORT_GENERATOR = "report_generator"


class WorkflowStatus(str, Enum):
    NOT_STARTED = "not_started"
    PLANNING = "planning"
    EXECUTING = "executing"
    VALIDATING = "validating"
    REPORTING = "reporting"
    REFLECTING = "reflecting"
    COMPLETED = "completed"
    FAILED = "failed"

class ValidationStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    WARNING = "warning"


class ReportType(str, Enum):
    DATA_PROFILE = "data_profile"
    MODEL_EVALUATION = "model_evaluation"
    VISUALIZATION = "visualization"
    EXECUTIVE = "executive"
