from pydantic import BaseModel, ConfigDict, Field


class Metrics(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid",
    )

    total_execution_time: float = Field(default=0, ge=0)

    tasks_completed: int = Field(default=0, ge=0)

    tasks_failed: int = Field(default=0, ge=0)

    retries: int = Field(default=0, ge=0)

    llm_calls: int = Field(default=0, ge=0)

    tokens_used: int = Field(default=0, ge=0)