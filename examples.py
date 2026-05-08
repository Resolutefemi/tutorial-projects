def check_num(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
#num = int(input("Enter your number"))
#print(check_num(num))
def know_grade(score):
    if score >= 70:
        return "A(Distinction)"
    elif score >= 60:
        return "B(Good)"
    elif score >= 50:
        return "C(Credit)"
    elif score >= 40:
        return "D(Pass)"
    elif score >= 30:
        return "E(fair)"
    else:
        return "F(Fail)"
print("------------- GRADE CHECKER APP --------------")
print("----------------------------------------------")
scores = int(input("Input your score to check your GRADE"))
print(know_grade(scores))
print("----------------------------------------------")
