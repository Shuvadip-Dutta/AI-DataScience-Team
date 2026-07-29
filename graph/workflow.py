from agents.ceo import ceo_node
from langgraph.graph import StateGraph, END, START
from agents.planner import planner_node
from agents.cleaner import cleaner_node
from agents.feature_engineer import feature_engineer_node
from agents.evaluator import evaluator_node
from agents.visualization import visualization_node
from agents.report_generator import report_generator_node
from typing import Literal

from state.state import CEOState

builder = StateGraph(CEOState)
# Register nodes
builder.add_node("CEO", ceo_node)
builder.add_node("Planner", planner_node)
builder.add_node("Cleaner", cleaner_node)
builder.add_node("Feature Engineer", feature_engineer_node)
builder.add_node("Evaluator", evaluator_node)
builder.add_node("Visualization", visualization_node)
builder.add_node("Report Generator", report_generator_node)

def ceo_router(state: CEOState) ->Literal[
        "planner",
        "cleaner",
        "feature_engineer",
        "model_builder",
        "evaluator",
        "visualization",
        "report_generator",
        "end",
    ]:
    return state["ceo_decision"].next_agent

builder.add_edge(START, "CEO")

builder.add_conditional_edges(
    "CEO",
    ceo_router,
    {
        "planner": "Planner",
        "cleaner": "Cleaner",
        "feature_engineer": "Feature Engineer",
        "evaluator": "Evaluator",
        "visualization": "Visualization",
        "report_generator": "Report Generator",
        "end": END,
    }
)

builder.add_edge("Planner", "CEO")
builder.add_edge("Cleaner", "CEO")
builder.add_edge("Feature Engineer", "CEO")
builder.add_edge("Evaluator", "CEO")
builder.add_edge("Visualization", "CEO")
builder.add_edge("Report Generator", "CEO")

graph = builder.compile()