from sklearn.preprocessing import LabelEncoder
from langchain_core.messages import AIMessage
from state.state import CEOState
from state.todo import TodoItem
from typing import Any
from state.feature_engineering_report import FeatureEngineeringReport
import logging

def feature_engineer_node(state: CEOState)-> dict[str, Any]:
    logger = logging.getLogger(__name__)

    df = state["dataframe"].copy()

    encoded_columns = []

    dropped_columns = []

    created_features = []

    # Encode categorical columns
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in categorical_columns:

        encoder = LabelEncoder()

        df[column] = encoder.fit_transform(df[column].astype(str))

        encoded_columns.append(column)

    # Drop unnecessary columns
    for column in ["PassengerId"]:

        if column in df.columns:

            df.drop(columns=column, inplace=True)

            dropped_columns.append(column)

    report = FeatureEngineeringReport(
        encoded_columns=encoded_columns,
        dropped_columns=dropped_columns,
        created_features=created_features,
        status="Completed",
    )

    updated_tasks = []

    for task in state["todo_list"]:
        owner = task.owner.lower().replace("_", " ")

        if task.owner == "Feature_Engineer":

            updated_tasks.append(
                TodoItem(
                    task=task.task,
                    owner=task.owner,
                    status="Completed",
                )
            )

        else:

            updated_tasks.append(task)
    logger.info("Feature engineering completed.")

    return {
        "engineered_dataframe": df,
        "feature_engineering_report": report,
        "todo_list": updated_tasks,
        "messages": [
            AIMessage(
                content="Feature engineering completed successfully."
            )
        ],
    }