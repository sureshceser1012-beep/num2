
# Inheritance Methods Assignment


# --------------------------------------------------
# Base Class: Vehicle
# --------------------------------------------------

class Vehicle:

    def __init__(self, color, speed, wheel_count):
        self.color = color
        self.speed = speed
        self.wheel_count = wheel_count

    def accelerate(self):
        self.speed += 10
        print("Vehicle accelerated.")
        print("Current speed:", self.speed, "km/h")

    def brake(self):
        self.speed -= 10

        if self.speed < 0:
            self.speed = 0

        print("Vehicle braking.")
        print("Current speed:", self.speed, "km/h")


# --------------------------------------------------
# Derived Class: Car
# --------------------------------------------------

class Car(Vehicle):

    def __init__(self, color, speed, wheel_count, number_of_doors):
        super().__init__(color, speed, wheel_count)
        self.number_of_doors = number_of_doors

    # Overriding accelerate()
    def accelerate(self):
        self.speed += 20
        print("Car accelerated quickly.")
        print("Current speed:", self.speed, "km/h")


# --------------------------------------------------
# Derived Class: Truck
# --------------------------------------------------

class Truck(Vehicle):

    def __init__(self, color, speed, wheel_count, cargo_capacity):
        super().__init__(color, speed, wheel_count)
        self.cargo_capacity = cargo_capacity

    # Overriding accelerate()
    def accelerate(self):
        self.speed += 5
        print("Truck accelerated slowly because of heavy load.")
        print("Current speed:", self.speed, "km/h")


# --------------------------------------------------
# Derived Class: Motorcycle
# --------------------------------------------------

class Motorcycle(Vehicle):

    def __init__(self, color, speed, wheel_count):
        super().__init__(color, speed, wheel_count)

    # Unique method
    def do_wheelie(self):
        print("Motorcycle is doing a wheelie!")

    # Overriding brake()
    def brake(self):
        self.speed -= 15

        if self.speed < 0:
            self.speed = 0

        print("Motorcycle uses a special braking mechanism.")
        print("Current speed:", self.speed, "km/h")


# --------------------------------------------------
# Creating Objects
# --------------------------------------------------

car = Car("Red", 50, 4, 4)
truck = Truck("Blue", 40, 6, 10000)
motorcycle = Motorcycle("Black", 60, 2)


# Car operations
print("CAR")
print("Color:", car.color)
print("Wheels:", car.wheel_count)
print("Doors:", car.number_of_doors)
car.accelerate()
car.brake()


# Truck operations
print("\nTRUCK")
print("Color:", truck.color)
print("Wheels:", truck.wheel_count)
print("Cargo Capacity:", truck.cargo_capacity, "kg")
truck.accelerate()
truck.brake()


# Motorcycle operations
print("\nMOTORCYCLE")
print("Color:", motorcycle.color)
print("Wheels:", motorcycle.wheel_count)
motorcycle.accelerate()
motorcycle.do_wheelie()
motorcycle.brake()