

class Student:


    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno


    def show(self):
        print(self.name , self.rollno)


s1 = Student('Brilliant',2)
s2 = Student('Amoah',12)

s1.show()