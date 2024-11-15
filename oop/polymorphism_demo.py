import math  # Required for circle calculations

# Base class Shape for polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Polymorphism demonstration function
def print_shape_details(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing polymorphism
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    print_shape_details(circle)

    print("\nRectangle:")
    print_shape_details(rectangle)
