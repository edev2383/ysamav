from abc import ABC, abstractmethod
from .model_base import ModelBase


class DataProvider(ABC):
    @abstractmethod
    def __init__(self):
        pass
