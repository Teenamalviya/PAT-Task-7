# Problem: 2

class Circle:
    # class private variable
    __pi = 3.141
    # class variable
    value = 100

    def display_pi(self):
        return self.pi
    def display_value(self):
        return self.value
# Main Method
if __name__ == "__main__":
    circle = Circle()
    print("Circle class having class variable without private: ", circle.display_value())
    print("Circle class having class variable as private variable", circle.display_pi())
