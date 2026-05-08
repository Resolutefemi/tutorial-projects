"""def main(*args):
    total = 0
    for arg in args:
         total +=arg
    return total

print(main(1, 2, 5))"""

def address(**addr):
    for key, value in addr.items():
        print(f"{key:.10} | {value}")

address(town = "Ikare Akoko",
        city = "Lago state",
        state = "Ondo State",
        zip = "34233",
        country = "Nigeria")