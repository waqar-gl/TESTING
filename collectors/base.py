from abc import ABC, abstractmethod
from typing import List

from core.models import Advisory

class BaseCollector(ABC):
    name = "Base"
    @abstractmethod
    def collect(self) -> List[Advisory]:
        """
        Return list of advisories.
        """
        raise NotImplementedError
