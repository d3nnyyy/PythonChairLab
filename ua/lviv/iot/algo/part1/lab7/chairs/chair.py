from abc import ABC, abstractmethod


@abstractmethod
class Chair(ABC):

    def __init__(self, max_weight=None, material=None):
        self.max_weight = max_weight
        self.material = material

    def __str__(self):
        return f"Chair: {self.max_weight}, {self.material}"

    @abstractmethod
    def adjust_position(self):
        pass
