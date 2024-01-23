# Problem: 1

class Circle:
    # constructor
    def __init__(self, radius):
        self.radius = radius
    # instance method
    def displaylist(self):
        return self.radius

# Main Method
if __name__ == "__main__":
    # Given list of values
    list = [10,501,22,37,100,999,87,351]
    # Creating object of class
    circle = Circle(list)
    # Printing list of values from instance method
    print("List of values from class method:", circle.displaylist())

