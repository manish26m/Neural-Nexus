# 1. Introduction to OOP
# Object-Oriented Programming (OOP) is a programming paradigm that revolves around objects.
# Objects are instances of classes, which can have attributes (data) and methods (functions).
# OOP aims to model real-world entities as objects and solve problems by creating interactions between them.

# 2. Classes and Objects
# A class is a blueprint for creating objects. It defines the properties and behaviors that objects of that class will have.
# An object is an instance of a class, representing a specific entity with its own unique set of attribute values.

class Person:
    pass  # This is an empty class definition

person1 = Person()  # Creating an instance (object) of the Person class

# 3. Attributes

# A. Instance Attributes
# Instance attributes are specific to each instance (object) of a class. They hold data related to that particular instance.

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

# B. Class Attributes
# Class attributes are shared among all instances of a class. They are defined within the class but outside any methods.

class Circle:
    pi = 3.14159  # Class attribute

circle1 = Circle()
circle2 = Circle()

print(circle1.pi)  # Output: 3.14159
print(circle2.pi)  # Output: 3.14159

# 4. Methods

# A. Instance Methods
# Instance methods are functions that can access and modify instance attributes of an object.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())  # Output: 15

# B. Class Methods
# Class methods are bound to the class itself and take the class as the first argument (cls).

class Circle:
    pi = 3.14159

    @classmethod
    def get_pi(cls):
        return cls.pi

print(Circle.get_pi())  # Output: 3.14159

# C. Static Methods
# Static methods are functions defined within a class but are not bound to any instance or the class itself.

class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

print(MathUtils.is_even(4))  # Output: True
print(MathUtils.is_prime(7))  # Output: True

# 5. Inheritance

# A. Single Inheritance
# Single inheritance allows a class to inherit from a single parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal speaks")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

dog = Dog("Buddy")
dog.speak()  # Output: The animal speaks
dog.bark()   # Output: The dog barks

# B. Multiple Inheritance
# Multiple inheritance allows a class to inherit from multiple parent classes.

class Flyable:
    def fly(self):
        print("I can fly")

class Swimmable:
    def swim(self):
        print("I can swim")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # Output: I can fly
duck.swim()  # Output: I can swim

# 6. Polymorphism

# A. Method Overriding
# Method overriding allows a subclass to provide a specific implementation of a method already defined in its base class.

class Animal:
    def speak(self):
        print("The animal speaks")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

animal = Animal()
dog = Dog()

animal.speak()  # Output: The animal speaks
dog.speak()     # Output: The dog barks

# B. Operator Overloading
# Operator overloading allows customizing the behavior of operators for user-defined classes.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Output: (6, 8)

# 7. Encapsulation and Abstraction

# A. Encapsulation
# Encapsulation is the bundling of data and methods within a single unit, hiding internal details from the outside world.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# B. Abstraction
# Abstraction exposes only the essential features of an object while hiding unnecessary details.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        pass  # Abstract method to be implemented by subclasses

class Car(Vehicle):
    def start(self):
        print(f"Starting the {self.make} {self.model}")

car = Car("Toyota", "Camry")
car.start()  # Output: Starting the Toyota Camry

# 8. Example Class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into {self.owner}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account. Remaining balance: {self.balance}")
        else:
            print(f"Insufficient funds in {self.owner}'s account.")

    def get_balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()
