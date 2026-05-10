class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Mustang", 2024, "red", False)
car1 = Car("Corvette", 2025, "blue", False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)