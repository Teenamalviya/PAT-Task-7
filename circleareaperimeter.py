# Problem: 3

class Circle:
    # class variable
    __pi = 3.141
    arealist = []
    perimeterlist = []
    # constructor
    def __init__(self, radius):
        self.radius = radius

    # instance method
    def area_of_circle(self):
        for r in self.radius:
            area = self.__pi * r * r
            self.arealist.append(area)
        return self.arealist

    # instance method
    def perimeter_of_circle(self):
        for r in self.radius:
            perimeter = 2 * self.__pi * r
            self.perimeterlist.append(perimeter)
        return self.perimeterlist
# Main Method
if __name__ == "__main__":
    list = [10, 501, 22, 37, 100, 999, 87, 351]
    print("List of given values of radius:", list)
    circle = Circle(list)
    print("List of areas of circle for given values of radius: ", circle.area_of_circle())
    print("List of perimeters of circle for given values of radius: ", circle.perimeter_of_circle())

