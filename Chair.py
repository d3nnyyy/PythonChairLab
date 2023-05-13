class Chair:

    _instance = None

    def __init__(self, max_weight, material, owner, id=1):
        self.max_weight = max_weight
        self.material = material
        self.owner = owner
        self.id = id

    def __str__(self):
        return "Chair: " \
            + str(self.id) + ", " \
            + str(self.max_weight) + ", " \
            + str(self.material) + ", " \
            + str(self.owner)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def getInstance(max_weight, material, owner, id):
        if Chair._instance is None:
            Chair._instance = Chair(max_weight, material, owner, id)
        return Chair._instance

    @property
    def max_weight(self):
        return self.__max_weight

    @property
    def material(self):
        return self.__material

    @property
    def owner(self):
        return self.__owner

    @property
    def id(self):
        return self.__id

    @max_weight.setter
    def max_weight(self, max_weight):
        self.__max_weight = max_weight

    @material.setter
    def material(self, material):
        self.__material = material

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @id.setter
    def id(self, id):
        self.__id = id

    def occupy(self, owner):
        self.owner = owner
        return f"Chair " + str(self.id) + " is occupied by " + str(self.owner)

    def release(self):
        self.owner = None
        f"Chair " + str(self.id) + " is released"

    def isOccupied(self):
        return self.owner is not None


chairs = []

chair1 = Chair.getInstance(100, "wood", "Vasya", 1)
chair2 = Chair.getInstance(150, "plastic", "Yurko", 2)

chairs.append(chair1)
chairs.append(chair2)

print(chairs)
print(chair1.occupy("Zenyk"))