from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class FeedingTable(Chair, ABC):
    MIN_HEIGHT = 0.5
    MAX_HEIGHT = 1

    def __init__(self, max_weight, material, height, child_age):
        super().__init__(max_weight, material)
        self.height = height
        self.child_age = child_age

    def __str__(self):
        return f"FeedingTable: {self.max_weight}, {self.material}, {self.height}, {self.child_age}"

    def adjust_position(self, delta_height):
        if self.MIN_HEIGHT <= self.height + delta_height <= self.MAX_HEIGHT:
            self.height += delta_height
        elif self.height + delta_height > self.MAX_HEIGHT:
            self.height = self.MAX_HEIGHT
        else:
            self.height = self.MIN_HEIGHT
