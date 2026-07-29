from langchain_core.messages import AIMessage
from state.state import CEOState
from state.todo import TodoItem
from typing import Any
from pathlib import Path
from state.report_generator_report import ReportGeneratorReport
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def report_generator_node(state: CEOState) -> dict[str, Any]:

    report_path = OUTPUT_DIR / "EDA_Report.md"

    cleaning = state["cleaning_report"]
    feature = state["feature_engineering_report"]
    evaluation = state["evaluation_report"]
    visualization = state["visualization_report"]

    report = f"""
# AI Data Science Team Report

---

## Dataset Cleaning

Rows Before: {cleaning.rows_before}

Rows After: {cleaning.rows_after}

Columns: {cleaning.columns}

Missing Values Removed: {cleaning.missing_values_removed}

Duplicate Rows Removed: {cleaning.duplicates_removed}

Status: {cleaning.status}

---

## Feature Engineering

Encoded Columns:

{", ".join(feature.encoded_columns)}

Dropped Columns:

{", ".join(feature.dropped_columns)}

Created Features:

{", ".join(feature.created_features) if feature.created_features else "None"}

Status: {feature.status}

---

## Dataset Evaluation

Rows: {evaluation.rows}

Columns: {evaluation.columns}

Missing Values: {evaluation.missing_values}

Duplicate Rows: {evaluation.duplicate_rows}

Numerical Columns:

{", ".join(evaluation.numerical_columns)}

Categorical Columns:

{", ".join(evaluation.categorical_columns) if evaluation.categorical_columns else "None"}

Status: {evaluation.status}

---

## Visualizations

Charts Generated:

{chr(10).join("- " + chart for chart in visualization.charts_created)}

Files:

{chr(10).join("- " + file for file in visualization.saved_files)}

Status: {visualization.status}

---

## Conclusion

✔ Dataset cleaned successfully.

✔ Features engineered successfully.

✔ Dataset evaluated successfully.

✔ Visualizations generated successfully.

AI Data Science Team completed the workflow successfully.
"""

    report_path.write_text(report, encoding="utf-8")

    report_info = ReportGeneratorReport(
        report_path=str(report_path.resolve()),
        sections=[
            "Cleaning",
            "Feature Engineering",
            "Evaluation",
            "Visualization",
            "Conclusion"
        ],
        status="Completed"
    )

    updated_tasks = []

    for task in state["todo_list"]:

        if task.owner == "Report Generator":

            updated_tasks.append(
                TodoItem(
                    task=task.task,
                    owner=task.owner,
                    status="Completed"
                )
            )

        else:

            updated_tasks.append(task)

    return {

        "report_generator_report": report_info,

        "todo_list": updated_tasks,

        "messages":[
            AIMessage(
                content="Final report generated successfully."
            )
        ]
    }