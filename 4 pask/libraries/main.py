import random

# from prettytable import prettytable
#
# x = prettytable()
#
# x.field_name = ["City", "Area", "Population"]
# x.add_row(["Adelaide", 1295, 1158259])
# x.add_row(["Brisbane", 5905, 1857594])
# x.add_row(["Darwin", 112, 120900])
# x.add_row(["Hobart", 1357, 205556])
# x.add_row(["Sydney", 2058, 4336374])

#print(x)

german_cars = ["BMW", "Audi", "MB", "Porsche", "VW"]
print(random.randint(0, 100))
print(random.randrange(10, 100, 5))

print(random.choice(german_cars))
random.shuffle(german_cars)
print(german_cars)
german_cars.sort()
print(german_cars)