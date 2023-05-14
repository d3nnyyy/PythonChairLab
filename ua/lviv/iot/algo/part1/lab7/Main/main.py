from ua.lviv.iot.algo.part1.lab7.Chair.Chair import Chair
get_instance = Chair.get_instance

chairs = []

chair0 = Chair.get_instance()

chair1 = Chair.get_instance(100, "wood", "Vasya", 1)
chair2 = Chair.get_instance(150, "plastic", "Yurko", 2)

chairs.append(chair0)
chairs.append(chair1)
chairs.append(chair2)

for chair in chairs:
    print(chair)
