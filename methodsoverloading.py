#06-07-26
# Method Overloading Assignment


# --------------------------------------------------
# 1. Calculator Class
# --------------------------------------------------

class Calculator:

    def calculate(self, *args):
        # Addition
        if len(args) == 2 and all(isinstance(x, int) for x in args):
            return args[0] + args[1]

        # Subtraction
        elif len(args) == 2 and all(isinstance(x, float) for x in args):
            return args[0] - args[1]

        # Multiplication
        elif len(args) == 3 and all(isinstance(x, int) for x in args):
            return args[0] * args[1] * args[2]

        # Division
        elif len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            if args[1] != 0:
                return args[0] / args[1]
            else:
                return "Cannot divide by zero."

        else:
            return "Invalid parameters."


calculator = Calculator()

print("Calculator Results:")
print("Addition:", calculator.calculate(10, 20))
print("Subtraction:", calculator.calculate(30.0, 10.0))
print("Multiplication:", calculator.calculate(2, 3, 4))
print("Division:", calculator.calculate(20, 5))


# --------------------------------------------------
# 2. Printer Class
# --------------------------------------------------

class Printer:

    def print_data(self, data):
        if isinstance(data, str):
            print("String:", data)

        elif isinstance(data, int):
            print("Integer:", data)

        elif isinstance(data, list):
            print("List:", data)

        else:
            print("Unknown data type.")


printer = Printer()

print("\nPrinter Results:")
printer.print_data("Hello Python")
printer.print_data(100)
printer.print_data([10, 20, 30])


# --------------------------------------------------
# 3. Converter Class
# --------------------------------------------------

class Converter:

    def convert(self, value, unit):
        # Kilometers to meters
        if unit == "km":
            return value * 1000

        # Meters to kilometers
        elif unit == "m":
            return value / 1000

        # Kilograms to grams
        elif unit == "kg":
            return value * 1000

        # Grams to kilograms
        elif unit == "g":
            return value / 1000

        # Celsius to Fahrenheit
        elif unit == "c":
            return (value * 9 / 5) + 32

        # Fahrenheit to Celsius
        elif unit == "f":
            return (value - 32) * 5 / 9

        else:
            return "Invalid unit."


converter = Converter()

print("\nConverter Results:")
print("5 km in meters:", converter.convert(5, "km"))
print("2000 meters in km:", converter.convert(2000, "m"))
print("2 kg in grams:", converter.convert(2, "kg"))
print("100 Celsius in Fahrenheit:", converter.convert(100, "c"))