# 1️⃣ Class and Object (Most Important)

# class is blueprint
# object is instance of class
class Student:
    def __init__ (self,name, marks):
        self.name = name
        self.marks = marks
        
    def show(self):
        print(self.name, self.marks)

s1 = Student("om",31)
s1.show()

# Student - class
# __init__ - constructor - call when we create class object (here s1)
# self - reference to current object


# Encapsulation means:
# Keeping the important / secret / internal data of an object hidden from the outside world — and allowing access only through carefully controlled methods that you yourself created.

class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def show_balance(self):
        print(self.__balance)

b = Bank(5000)
b.show_balance()


# __balance is hidden cannot accessed directly

# Inheritance (Very Important)

# A class can inherit properties from another class.(only child access parents properties)
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


# Method Overriding

# Child class changes parent method behavior.

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()


# Abstraction
# In simple words: Abstraction hides the complex "how" details and shows only the simple "what" interface. Use abstract base classes (ABC) to force subclasses to implement key methods.


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):  # Abstract base class
    @abstractmethod
    def process(self, amount: float) -> str:
        pass  # Must be implemented by subclasses

class CreditCard(PaymentProcessor):
    def process(self, amount: float) -> str:  # Implements the abstract method
        return f"Processed ₹{amount} via Credit Card (details hidden)"

class PayPal(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Processed ₹{amount} via PayPal (API calls hidden)"

# Abstraction: Use the simple interface, ignore internals
def checkout(payment: PaymentProcessor, amount: float):
    print(checkout(payment.process(amount)))

# Usage
card = CreditCard()
paypal = PayPal()
checkout(card, 1000)   # → Processed ₹1000 via Credit Card (details hidden)
checkout(paypal, 500)  # → Processed ₹500 via PayPal (API calls hidden)


# Polymorphism
# In simple words: Polymorphism lets you call the same method on different objects, but each object responds in its own way (via overriding).
class Bird:
    def fly(self):
        return "Flapping wings"

class Airplane:
    def fly(self):  # Same method name, different behavior
        return "Using engines"

# Polymorphism: Same call, different results
def make_it_fly(thing):
    print(thing.fly())

# Usage
bird = Bird()
plane = Airplane()
make_it_fly(bird)   # → Flapping wings
make_it_fly(plane)  # → Using engines


# Class Methods
# Used when the method needs to work with the class itself, not with a specific object.
# It can modify class variables or create alternative constructors.
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")
print(Student.school)


# Static Methods
# Used when the method doesn't need to access class variables or objects.
# It is just a utility/helper function inside the class. not required self,cls.

class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))