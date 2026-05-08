menu = {"apple": 2.5456, "banana": 1.0456, "orange": 1.5567, "cashew": 2.6455}
cart = []
total = 0
print("-----------------------------------MENU-------------------------------------")
for key, value in menu.items():
    print(f"{key:8} : ${value:.2f}")
print("----------------------------------------------------------------------------")

while True:
    fruit = input("Select an item  (q to quit):  ").lower()
    if fruit == "q":
        print("Thanks for patronzing us!")
        break
    elif menu.get(fruit) is not None:
        cart.append(fruit)

for fruit in cart:
    total += float(menu.get(fruit))
    print(fruit, end=" ")
print("\n-------------YOUR ORDER----------------")
print(f"Total is: {total} ")