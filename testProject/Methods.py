

class Student:

    school = 'Brilliant'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3


s1 = Student(24,56,84)
s2 = Student(12,28,52)

print(s1.avg)