# 1 
class Person:
    def __init__(self, name, age):
        self.nm = name
        self.ag = age

    def details(self):
        return self.nm, self.ag

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student = student_id

    def details(self):
        return super().details(), self.student
    
person = Person("Mahmoud Saied", 26)
print(person.details())

student = Student("Ahmed Ali", 24, "1id")
print(student.details())

#============================================================================================#
# 2
class Sports:
    def __init__(self, Spname, achievements):
        self.nm = Spname
        self.ach = achievements
        
class Academics:
    def __init__(self, subject, aca_achievements):
        self.sub = subject
        self.acach = aca_achievements

class Student(Sports, Academics):
    def __init__(self, name, Spname, achievements, subject, aca_achievements):
        Sports.__init__(self, Spname, achievements)
        Academics.__init__(self, subject, aca_achievements)
        self.name = name

    def display_total_achievements(self):
        print(self.name)
        print(self.nm , self.ach)
        print(self.sub , self.acach)

student = Student()
student.displayFullachievements()

#============================================================================================#
# 3 
class Animal:
    def __init__(self, name, age):
        self.nm = name
        self.ag = age

    def eat(self):
        print(self.nm)
    def sleep(self):
        print(self.nm)

class Mammal(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name, age)
        self.col = color

    def nurse(self):
        print(self.nm)

    def walk(self):
        print(self.nm)

class Dog(Mammal):
    def __init__(self, name, age, color, breed):
        Mammal.__init__(self, name, age, color)
        self.breed = breed

    def bark(self):
        print(self.nm)

    def fetch(self):
        print(self.nm)

dog = Dog()
dog.eat()
dog.walk()
dog.bark()

print(dog.nm)
print(dog.col)
print(dog.breed)

#============================================================================================#
# 4
class Shape:
    def draw(self):
        print("shape")
class Circle(Shape):
    def draw(self):
        print("Circle")
class Rectangle(Shape):
    def draw(self):
        print("Rectangle")

circle = Circle()
rectangle = Rectangle()

circle.draw()
rectangle.draw()

#============================================================================================#
# 5
class BankAccount:
    def __init__(self, initial_balance=1000):
        self._bl = initial_balance

    def deposit(self, amount):
        self._bl += amount
        print(amount,self._bl)

    def withdraw(self, amount):
        if amount > self._bl:
            print("Insufficient balance.")
        else:
            self._bl -= amount
            print(amount,self._bl)

account = BankAccount()
account.deposit()
account.withdraw()
account.withdraw()

#============================================================================================#
"""
Python doesn't support method overloading directly.
Overloading in Python is not supported in the traditional sense where multiple methods can have the same name but different parameters. 
However, Python supports operator overloading and allows methods to handle arguments of different types,
effectively overloading by type checking inside methods
"""

"""
Key differences between protected and public access modifiers in Python:
1. Intent: Public members are intended to be used by anyone, while protected members are intended to be used internally within the class or its subclasses.
2. Conventions: Public members follow the standard naming conventions, while protected members are prefixed with a single underscore (_).
3. Access: Public members can be accessed directly from anywhere, while protected members are discouraged from being accessed directly from outside the class or its subclasses.
4. Enforcement: Python does not enforce access restrictions for public or protected members. The access restrictions are based on conventions and are intended to promote good coding practices.
"""


#============================================================================================#
#============================================================================================#
#============================================================================================#