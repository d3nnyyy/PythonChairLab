from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class ReclinerChair(Chair, ABC):
    MIN_ANGLE = 90
    MAX_ANGLE = 150

    def __init__(self, maxWeight, material, angle, has_remote_control):
        super().__init__(maxWeight, material)
        self.angle = angle
        self.has_remote_control = has_remote_control

    def __str__(self):
        return f"ReclinerChair: {self.max_weight}, {self.material}, {self.angle}, {self.has_remote_control}"

    def adjust_position(self, deltaAngle):
        if self.MIN_ANGLE <= self.angle + deltaAngle <= self.MAX_ANGLE:
            self.angle += deltaAngle
        elif self.angle + deltaAngle > self.MAX_ANGLE:
            self.angle = self.MAX_ANGLE
        else:
            self.angle = self.MIN_ANGLE
