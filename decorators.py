# Decorators Fundamentals

import time


# --------------------------------------------------
# 1. Hello Decorator
# --------------------------------------------------

def hello_decorator(func):

    def wrapper():
        print("Hello, world!")
        func()
        print("Hello, world!")

    return wrapper


@hello_decorator
def say_message():
    print("This is the original function.")


print("Task 1: Hello Decorator")
say_message()


# --------------------------------------------------
# 2. Timer Decorator
# --------------------------------------------------

def timer_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print("Execution time:", execution_time, "seconds")

        return result

    return wrapper


@timer_decorator
def calculate_sum():
    total = 0

    for number in range(1, 100000):
        total += number

    return total


print("\nTask 2: Timer Decorator")
result = calculate_sum()
print("Sum:", result)


# --------------------------------------------------
# 3. Debug Decorator
# --------------------------------------------------

def debug_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function arguments:", args)

        result = func(*args, **kwargs)

        print("Return value:", result)

        return result

    return wrapper


@debug_decorator
def add_numbers(a, b):
    return a + b


print("\nTask 3: Debug Decorator")
answer = add_numbers(10, 20)