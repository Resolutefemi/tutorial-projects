def login():
    tries = 4
    correct_pin = 636685
    while tries > 0:
        pin_input =input("Enter your pin:  ")
        pin = int(pin_input)
        if pin == correct_pin:
            return "Successful login attempt"
        tries -= 1
        print("WRONG PIN, ATTEMPTS LEFT: ",tries)
    return "ACCESS DENIED"
print(login())