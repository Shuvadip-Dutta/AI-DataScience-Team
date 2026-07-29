from langchain_core.messages import AIMessage
from state.ceo import CEODecision
from typing import Any
from state.state import CEOState
import logging

logger = logging.getLogger(__name__)

OWNER_TO_AGENT = {
    "cleaner": "cleaner",
    "feature engineer": "feature_engineer",
    "evaluator": "evaluator",
    "visualization": "visualization",
    "report generator": "report_generator",
}

def ceo_node(state: CEOState) -> dict[str, Any]:

    todo_list = state.get("todo_list")

    if not todo_list:
        decision = CEODecision(
            next_agent="planner",
            reason="No execution plan exists."
        )

    else:

        # Find the first pending task
        pending_task = next(
            (task for task in todo_list if task.status == "Pending"),
            None
        )

        # All tasks completed
        if pending_task is None:
            decision = CEODecision(
                next_agent="end",
                reason="All tasks have been completed."
            )

        else:
            owner = pending_task.owner.strip().lower()

            agent = OWNER_TO_AGENT.get(owner)

            if agent is None:
                raise ValueError(
                    f"Unknown task owner: {pending_task.owner}"
                )

            decision = CEODecision(
                next_agent=agent,
                reason=f"Routing '{pending_task.task}' to {pending_task.owner}."
            )
    logger.info("\n=== CEO STATE ===")
    logger.info("Todo exists:", "todo_list" in state)

    todo_list = state.get("todo_list")

    logger.info("Todo type:", type(todo_list))
    logger.info("Todo value:", todo_list)

    if todo_list:
        logger.info("Length:", len(todo_list))
        for i, task in enumerate(todo_list, start=1):
            logger.info("Task %d: %s", i, task)

    return {
        "ceo_decision": decision,
        "messages": [
            AIMessage(content=decision.reason)
        ]
    }