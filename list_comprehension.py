"""double = []
for x in range(1, 11):
    double.append(x*2)
print(double)"""

"""double = [x*2 for x in range(1, 11)]
print(double)"""

fruits = ["Orange", "Apple", "Cashew", "Banana"]
fruits = [fruit.upper() for fruit in fruits if len(fruit) < 6]
print(fruits)