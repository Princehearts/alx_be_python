# polymorphism_demo.py

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Demonstration of polymorphism
def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

# Test cases
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    square = Square(7)

    print_area(rect)  # Expected output: The area of the shape is: 50
    print_area(square)  # Expected output: The area of the shape is: 49
