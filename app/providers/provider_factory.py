from app.config.settings import get_settings
from app.models.enums import LLMProvider
from app.providers.base_provider import BaseLLMProvider
from app.providers.groq_provider import GroqProvider


def get_provider() -> BaseLLMProvider:
    """
    Returns the configured LLM provider.
    """

    settings = get_settings()

    if settings.LLM_PROVIDER == LLMProvider.GROQ:
        return GroqProvider()

    raise ValueError(f"Unsupported LLM provider: {settings.LLM_PROVIDER}")