from ua.lviv.iot.algo.part1.lab7.chairs.feedingTable import FeedingTable
from ua.lviv.iot.algo.part1.lab7.chairs.gamingChair import GamingChair
from ua.lviv.iot.algo.part1.lab7.chairs.officeChair import OfficeChair
from ua.lviv.iot.algo.part1.lab7.chairs.reclinerChair import ReclinerChair
from ua.lviv.iot.algo.part1.lab7.manager.manager import ChairManager

manager = ChairManager()
feeding_table1 = FeedingTable(40, "Wood", 0.8, 2)
feeding_table2 = FeedingTable(20, "Plastic", 0.6, 3)

office_chair1 = OfficeChair(150, "Steel", 90, True)
office_chair2 = OfficeChair(130, "Leather", 100, False)

gaming_chair1 = GamingChair(120, "Plastic", 1.5, True)
gaming_chair2 = GamingChair(140, "Metal", 1.6, True)

recliner_chair1 = ReclinerChair(200, "Leather", 120, True)
recliner_chair2 = ReclinerChair(180, "Fabric", 100, False)

manager.add_chair(feeding_table1)
manager.add_chair(feeding_table2)
manager.add_chair(office_chair1)
manager.add_chair(office_chair2)
manager.add_chair(gaming_chair1)
manager.add_chair(gaming_chair2)
manager.add_chair(recliner_chair1)
manager.add_chair(recliner_chair2)

for chair in manager.chairs:
    print(chair)

chairs_with_max_weight_more_than = manager.find_chair_with_max_weight_more_than(150)
chairs_with_certain_material = manager.find_chair_by_material("Leather")

print("\nChairs with max weight more than:")
for chair in chairs_with_max_weight_more_than:
    print(chair)

print("\nChairs with certain material:")
for chair in chairs_with_certain_material:
    print(chair)
