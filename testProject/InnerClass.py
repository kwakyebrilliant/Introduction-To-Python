

class Student:


    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    class Laptop:

        def __init__(self):
            self.brand = 'Mackbook'
            self.cpu = 'M1'
            self.ram = 8


    def show(self):
        print(self.name , self.rollno)


s1 = Student('Brilliant',2)
s2 = Student('Amoah',12)

s1.show()