class ChairManager:
    chairs = []

    def find_chair_by_material(self, material):
        return [chair for chair in self.chairs if chair.material == material]

    def find_chair_with_max_weight_more_than(self, max_weight):
        return [chair for chair in self.chairs if chair.max_weight > max_weight]

    def add_chair(self, chair):
        self.chairs.append(chair)
