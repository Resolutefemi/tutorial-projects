balance = 0
def showBalance():
    print(f"Your balalance is {balance:.2f}")
def banking_engine(choice):
    """choice_list = [showBalance(), deposit(), withdraw(), quit()]
    if 1 <= choice <= 4:
        return choice_list[choice - 1]"""
    choice_list = [showBalance, deposit, withdraw, quit]
    if 1 <= choice <= 4:
        return choice_list[choice - 1]()

def withdraw():
    global balance
    amount = float(input("How much do you want withdraw:  "))
    if  amount > balance:
        print ("insufficient amount")
        return

    elif amount < 0:
        print("That's not a valid amount")
    balance -= amount
    return showBalance()
def deposit():
    global balance
    amount = float(input("How much do you want deposit:  "))
    if amount< 0:
        print("That's invalid")
    balance += amount
    return showBalance()
def quit():
    print("Thanks for visting!")
def option(options = None):
        if options is None:
            options= {1 : "Show Balance",
                    2 : "Deposit Money",
                    3 : "Withdraw Money",
                    4 : "Quit"}
        return options
def ATM():
    options = option()

    while True:
        print("*"*8, "BANKING SYSYTEM", "*"*8, "\n")
        for opt, task in options.items():
            print(f"{opt}. {task} ")
        print("*"*34, "\n")
        choice = int(input("What do you wanna do? :  "))
        banking_engine(choice)

        if choice == 4:
            quit()
            break
ATM()
