"""
Object-Oriented Programming (OOP) in Python - Comprehensive Guide
================================================================

Educational guide to OOP concepts: classes, inheritance, polymorphism, encapsulation, and design patterns.
Includes practical examples, best practices, and real-world applications.

Author: Python Learning Notes
Date: September 2025
Topic: OOP, Classes, Inheritance, Polymorphism, Design Patterns
"""

# =============================================================================
# BASIC CLASS AND OBJECTS
# =============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# =============================================================================
# INHERITANCE
# =============================================================================

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def greet(self):
        return f"Hi, I'm {self.name}, student ID {self.student_id}."

# =============================================================================
# POLYMORPHISM
# =============================================================================

def greet_all(people):
    for person in people:
        print(person.greet())

# =============================================================================
# ENCAPSULATION
# =============================================================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    def get_balance(self):
        return self.__balance

# =============================================================================
# SIMPLE DESIGN PATTERN: SINGLETON
# =============================================================================

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    # Basic class usage
    alice = Person('Alice', 30)
    bob = Student('Bob', 20, 'S123')
    greet_all([alice, bob])
    # Encapsulation
    acct = BankAccount('Carol', 100)
    acct.deposit(50)
    acct.withdraw(30)
    print(f"Carol's balance: {acct.get_balance()}")
    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton instances are the same: {s1 is s2}")

if __name__ == "__main__":
    main()
