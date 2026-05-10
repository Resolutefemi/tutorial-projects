from car import Car

car2 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car2.drive()