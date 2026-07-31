from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from enum import Enum

class LLMProvider(str, Enum):
    GROQ = "groq"
    OPENAI = "openai"
    GEMINI = "gemini"
    OLLAMA = "ollama"


class Settings(BaseSettings):
    """
    Application configuration.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    # =========================
    # LLM
    # =========================

    GROQ_API_KEY: SecretStr

    LLM_PROVIDER: LLMProvider = LLMProvider.GROQ

    MODEL_NAME: str = "llama-3.3-70b-versatile"

    TEMPERATURE: float = 0.0

    MAX_TOKENS: int = 2048

    # =========================
    # Workflow
    # =========================

    MAX_RETRIES: int = 2

    ENABLE_REFLECTION: bool = True

    # =========================
    # Paths
    # =========================

    OUTPUT_DIR: str = "outputs"

    DATASET_DIR: str = "datasets"

    # =========================
    # Logging
    # =========================

    LOG_LEVEL: str = "INFO"
    
    LOG_DIR: str = "logs"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached settings instance.
    """
    return Settings()