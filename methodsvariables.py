#02-07-26
# Methods and Variables Practice


class Calculator:

    # Static variable
    calculator_name = "Basic Calculator"

    # Constructor
    def __init__(self):
        # Instance variable
        self.result = 0

    # Instance method
    def addNumbers(self, num1, num2):
        # Local variable
        total = num1 + num2

        # Updating instance variable
        self.result = total

        return self.result

    # Static method
    @staticmethod
    def isPositive(number):
        return number > 0


# Create Calculator object
calculator = Calculator()

# Using instance method
result = calculator.addNumbers(20, 30)

print("Addition Result:", result)

# Using static method
print("Is 10 positive?", Calculator.isPositive(10))
print("Is -5 positive?", Calculator.isPositive(-5))


# Method demonstrating local variable
def greetUser(name):

    # Local variable
    user_name = name

    print("Hello,", user_name + "!")
    print("Welcome to Python programming.")


# Calling the method
greetUser("Suresh")