def formula(SI = None, p= None, r= None, t= None):
    if SI is None:       
        return float((p*r*t)/100)
    elif p is None:
        return float((100*SI)/(r*t))
    elif r is None:
        return float((100*SI)/(p*t))
    elif t is None:
        return float((100*SI)/(r*p))

def calc_SI():
    p= float(input("PRINCIPAL: "))
    r= float(input("RATE: "))
    t= float(input("TIME: "))
    SI = formula( p= p, r = r, t= t)
    print(f"The simple Interest is ${SI}")
def calc_time():
    p= float(input("PRINCIPAL: "))
    r= float(input("RATE: "))
    SI= float(input("INTEREST: "))
    t=formula( SI = SI, p= p, r = r)
    print(f"The time is ${t}")
def calc_rate():
    p= float(input("PRINCIPAL: "))
    SI= float(input("INTEREST: "))
    t= float(input("TIME: "))
    r=formula( SI = SI, p= p, t= t)
    print(f"The RATE is ${r}")
def calc_p():
    SI= float(input("INTEREST: "))
    r= float(input("RATE: "))
    t= float(input("TIME: "))
    p=formula( SI = SI, r = r, t= t)
    print(f"The PRINCIPAL is ${p}")
def calc( ):
    comm = {
        "I": ("Interest", calc_SI),
        "T": ("Time", calc_time),
        "R": ("Rate", calc_rate),
        "P": ("Principal", calc_p),
        "Q": ("Quit", None)
    }
    while True:
        print("--------------------------------------------SIMPLE INTEREST CALCULATOR-----------------------------------------")
        for key, (value, _) in comm.items():
            print(f"{key:8} for {value}")
        print("-"*40)
        calc = input("What do you wnat to calculate(I, P, R, T): ").strip().upper()
        if calc == "Q":
            print("\n GOODBYE \n")
            break
        elif calc in comm:
            print()
            comm[calc][1]()
        else:
            print("Enter sth Valid")
calc()