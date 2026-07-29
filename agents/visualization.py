import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from langchain_core.messages import AIMessage
from state.todo import TodoItem
from typing import Any
from state.state import CEOState
from state.visualization_report import VisualizationReport
output_dir = Path("outputs")

output_dir.mkdir(exist_ok=True)

def visualization_node(state: CEOState) -> dict[str, Any]:

    df = state["engineered_dataframe"].copy()

    charts = []

    # Histogram

    df.hist(figsize=(12,10))
    plt.tight_layout()

    hist_path = output_dir/"histograms.png"

    plt.savefig(hist_path)
    plt.close()

    charts.append(str(hist_path.resolve()))


    # Correlation Heatmap

    plt.figure(figsize=(8,6))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="Blues"
    )

    heatmap_path = output_dir/"correlation_heatmap.png"

    plt.savefig(heatmap_path)

    plt.close()

    charts.append(str(heatmap_path.resolve()))
    
    # Target Distribution

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Survived",
        data=df
    )

    plt.title("Target Distribution")

    target_path = output_dir/"target_distribution.png"

    plt.savefig(target_path)

    plt.close()

    charts.append(str(target_path.resolve()))
    
    # Feature Relationships

    plt.figure(figsize=(7,6))

    sns.scatterplot(
        data=df,
        x="Age",
        y="Fare",
        hue="Survived"
    )

    relationship_path = output_dir/"feature_relationships.png"

    plt.savefig(relationship_path)

    plt.close()

    charts.append(str(relationship_path.resolve()))


    report = VisualizationReport(
        charts_created=[
            "Histograms",
            "Correlation Heatmap",
            "Target Distribution",
            "Feature Relationships"
        ],
        saved_files=charts,
        total_charts=len(charts),
        status="Completed"
    )
    updated_tasks = []
    for task in state["todo_list"]:
        if task.owner == "Visualization":
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
        "visualization_report": report,
        "todo_list": updated_tasks,
        "messages": [
            AIMessage(
                content=f"Visualization completed successfully. Generated {len(charts)} charts."
            )
        ]
    }