# Encapsulation Assignment


# 1. BankAccount Class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


# 2. Vehicle Class
class Vehicle:
    def __init__(self, speed, color):
        self.__speed = speed     # Private attribute
        self.__color = color     # Private attribute

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            print(f"Vehicle accelerated to {self.__speed} km/h")

    def brake(self, amount):
        if amount > 0:
            self.__speed -= amount

            if self.__speed < 0:
                self.__speed = 0

            print(f"Vehicle speed reduced to {self.__speed} km/h")

    def get_speed(self):
        return self.__speed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


# 3. Person Class
class Person:
    def __init__(self, name, age, address):
        self.__name = name       # Private attributes
        self.__age = age
        self.__address = address

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def update_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age.")

    def update_address(self, address):
        self.__address = address


# Main Program

# Bank Account
print("===== BANK ACCOUNT =====")

account = BankAccount("BA001", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Current Balance:", account.get_balance())


# Vehicle
print("\n===== VEHICLE =====")

vehicle = Vehicle(50, "Red")

print("Speed:", vehicle.get_speed())
print("Color:", vehicle.get_color())

vehicle.accelerate(30)
vehicle.brake(20)

vehicle.set_color("Blue")
print("Updated Color:", vehicle.get_color())


# Person
print("\n===== PERSON =====")

person = Person("John", 25, "Hyderabad")

print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

person.update_age(26)
person.update_address("Vijayawada")

print("Updated Age:", person.get_age())
print("Updated Address:", person.get_address())