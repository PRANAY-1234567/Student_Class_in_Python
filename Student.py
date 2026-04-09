class Student:
    def __init__(self, name, Roll_number,Department):
        self.name = name
        self.Roll_number = Roll_number
        self.Department = Department

    def display(self):
        print("Name :",self.name)
        print("Roll Number :",self.Roll_number)
        print("Department :",self.Department)

s1 = Student("Pranay", 25,"Entc")

s2 = Student("Raj", 26,"ENTC")

s1.display()
s2.display()
        
