from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class GamingChair(Chair, ABC):
    MIN_HEIGHT = 1.2
    MAX_HEIGHT = 1.8

    def __init__(self, max_weight, material, height, has_footrest):
        super().__init__(max_weight, material)
        self.height = height
        self.has_footrest = has_footrest

    def __str__(self):
        return f"GamingChair: {self.max_weight}, {self.material}, {self.height}, {self.has_footrest}"

    def adjust_position(self, delta_height):
        if self.MIN_HEIGHT <= self.height + delta_height <= self.MAX_HEIGHT:
            self.height += delta_height
        elif self.height + delta_height > self.MAX_HEIGHT:
            self.height = self.MAX_HEIGHT
        else:
            self.height = self.MIN_HEIGHT
