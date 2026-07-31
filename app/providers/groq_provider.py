from langchain_groq import ChatGroq

from app.config.settings import get_settings
from app.providers.base_provider import BaseLLMProvider


class GroqProvider(BaseLLMProvider):

    def __init__(self):

        settings = get_settings()

        self.llm = ChatGroq(
            model_name=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            api_key=settings.GROQ_API_KEY.get_secret_value(),
        )

    def invoke(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        return response.content