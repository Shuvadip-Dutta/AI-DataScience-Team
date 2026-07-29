from langchain_core.messages import AIMessage
from state.state import CEOState
from state.todo import TodoItem
from typing import Any
from state.evaluation_report import EvaluationReport
import logging

def evaluator_node(state: CEOState) -> dict[str, Any]:
    logger = logging.getLogger(__name__)

    df = state.get("engineered_dataframe")

    if df is None:
        raise ValueError(
            f"engineered_dataframe missing.\nAvailable keys: {list(state.keys())}"
        )

    numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

    report = EvaluationReport(

        rows=len(df),

        columns=df.shape[1],

        numerical_columns=numerical_columns,

        categorical_columns=categorical_columns,

        missing_values=int(df.isnull().sum().sum()),

        duplicate_rows=int(df.duplicated().sum()),

        status="Completed",
    )

    updated_tasks = []

    for task in state["todo_list"]:

        if task.owner == "Evaluator":

            updated_tasks.append(
                TodoItem(
                    task=task.task,
                    owner=task.owner,
                    status="Completed",
                )
            )

        else:

            updated_tasks.append(task)
    logger.info("Dataset evaluation completed.")

    return {

        "evaluation_report": report,

        "todo_list": updated_tasks,

        "messages":[
            AIMessage(
                content="Dataset evaluation completed successfully."
            )
        ]
    }