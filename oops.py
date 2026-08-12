#29-06-26
# Introduction to OOPS in Python

# --------------------------------------------------
# 1. Vehicle Class
# --------------------------------------------------

class Vehicle:
    def __init__(self, color, speed, vehicle_type):
        self.color = color
        self.speed = speed
        self.vehicle_type = vehicle_type

    def display_info(self):
        print("Vehicle Information")
        print("Color:", self.color)
        print("Speed:", self.speed, "km/h")
        print("Type:", self.vehicle_type)

    def calculate_travel_time(self, distance):
        time = distance / self.speed
        print("Distance:", distance, "km")
        print("Travel Time:", time, "hours")


vehicle = Vehicle("Red", 80, "Car")

vehicle.display_info()
vehicle.calculate_travel_time(160)


# --------------------------------------------------
# 2. Employee Class
# --------------------------------------------------

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print("Bonus:", bonus)


employee = Employee("Suresh", 25, 50000)

employee.display_details()
employee.calculate_bonus()


# --------------------------------------------------
# 3. BankAccount Class
# --------------------------------------------------

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("\nDeposited:", amount)
        print("Updated Balance:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("\nWithdrawn:", amount)
            print("Updated Balance:", self.__balance)
        else:
            print("\nInsufficient balance.")

    def display_balance(self):
        print("\nBank Account Details")
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.__balance)


account = BankAccount("123456789", "Suresh", 10000)

account.display_balance()
account.deposit(5000)
account.withdraw(3000)
account.display_balance()