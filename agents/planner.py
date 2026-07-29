from config.llm import llm
from state import state
from state.planner import PlannerOutput
from prompts.planner_prompt import planner_prompt
from state.state import CEOState
from langchain_core.messages import AIMessage
from typing import Any
import logging

logger = logging.getLogger(__name__)

structured_planner_llm = llm.with_structured_output(PlannerOutput)

def create_planner_chain():
    return planner_prompt | structured_planner_llm

def planner_node(state: CEOState) -> dict[str, Any]:
    planner_chain= create_planner_chain()
    response = planner_chain.invoke(
        {
            "user_request": state["user_request"],
            "dataset_path": state["dataset_path"]
        }
    )
    todo_list = response.todo_list
    logger.info("\n=== Planner Output ===")
    for task in todo_list:
        logger.info(f"{task.owner} | {task.task} | {task.status}")
    return {
    "todo_list": todo_list,
    "current_agent": "Planner",
    "workflow_log": [
        f"Planner created {len(todo_list)} tasks."
    ],
    "messages": [
        AIMessage(
            content=f"Planner created {len(todo_list)} tasks."
        )
    ],
}
    
    