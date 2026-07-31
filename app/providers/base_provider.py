from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Abstract interface for all LLM providers.
    """

    @abstractmethod
    def invoke(self, prompt: str) -> str:
        """
        Generate a response from an LLM.
        """
        pass

# from abc import ABC, abstractmethod
# from typing import Type, TypeVar

# T = TypeVar("T")


# class BaseLLMProvider(ABC):

#     @abstractmethod
#     def invoke(self, prompt: str) -> str:
#         pass

#     @abstractmethod
#     def invoke_structured(self, prompt: str, schema: Type[T]) -> T:
#         pass