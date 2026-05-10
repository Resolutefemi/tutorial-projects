class Student:
    class_year = 2024
    def __init__(self, name, age):
        self.name = name
        self.age = age


Student1 = Student("Spongebob", 30)
Student2 = Student("Patrick", 35 )

print(Student1.name)
print(Student2.age)
print(Student2.class_year)