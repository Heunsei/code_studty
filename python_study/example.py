class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} , {self.age}'

class Student(Person):
    def __init__(self,name,age,pap):
        super().__init__(name,age)
        self.pap = pap

p1 = Person('김싸피', 25)
s1 = Student('김기김',13, 1.2)

print(p1)
print(s1)
