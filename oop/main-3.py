class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Static method for addition
    @staticmethod
    def add(x, y):
        return x + y

    # Static method for subtraction
    @staticmethod
    def subtract(x, y):
        return x - y

    # Static method for multiplication
    @staticmethod
    def multiply(x, y):
        return x * y

    # Static method for division
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed"

# Example usage
if __name__ == "__main__":
    # Access class attribute
    print(f"Calculation Type: {Calculator.calculation_type}")

    # Using static methods
    print(f"Addition: {Calculator.add(5, 3)}")
    print(f"Subtraction: {Calculator.subtract(10, 7)}")
    print(f"Multiplication: {Calculator.multiply(4, 6)}")
    print(f"Division: {Calculator.divide(8, 2)}")
