from langchain_core.messages import AIMessage
from state.state import CEOState
from state.cleaning_report import CleaningReport
from state.todo import TodoItem
from typing import Any
import pandas as pd

def cleaner_node(state: CEOState) -> dict[str, Any]:

    df = pd.read_csv(state["dataset_path"])

    rows_before = len(df)

    duplicates = df.duplicated().sum()

    missing = df.isnull().sum().sum()

    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    categorical_columns = df.select_dtypes(exclude=["number"]).columns

    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    rows_after = len(df)

    report = CleaningReport(
        rows_before=rows_before,
        rows_after=rows_after,
        columns=len(df.columns),
        missing_values_removed=int(missing),
        duplicates_removed=int(duplicates),
        status="Completed",
    )
    updated_tasks = []

    for task in state["todo_list"]:
        if task.owner == "Cleaner":
            updated_tasks.append(
                TodoItem(
                    task=task.task,
                    owner=task.owner,
                    status="Completed",
                )
            )
        else:
            updated_tasks.append(task)

    return {
        "todo_list": updated_tasks,
        "dataframe": df,
        "cleaning_report": report,
        "current_agent": "Cleaner",
        "messages": [
            AIMessage(
                content="Dataset cleaned successfully."
            )
        ]
    }