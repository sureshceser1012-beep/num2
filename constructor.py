# 08-07-26
# Constructor and Instance Variable Assignment

class Person:

    # Constructor
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    # Method to display person information
    def display_info(self):
        print("Person Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)


# Main method
def main():

    # Creating two Person objects
    person1 = Person("Suresh", 25, "Hyderabad")
    person2 = Person("Ravi", 30, "Vijayawada")

    # Display information
    print("Person 1:")
    person1.display_info()

    print("\nPerson 2:")
    person2.display_info()


# Calling main method
if __name__ == "__main__":
    main()