class Calculator:
    # Class attribute to indicate the type of calculations
    calculation_type = "Arithmetic Operations"

    def __init__(self):
        pass  # No instance attributes needed for this example

    @staticmethod
    def add(a, b):
        """Performs addition of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Performs subtraction of two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Performs multiplication of two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Performs division of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Demo of class and static methods
if __name__ == "__main__":
    print(f"Calculation Type: {Calculator.calculation_type}")

    # Using static methods directly from the class
    print(f"Addition: {Calculator.add(10, 5)}")
    print(f"Subtraction: {Calculator.subtract(10, 5)}")
    print(f"Multiplication: {Calculator.multiply(10, 5)}")
    print(f"Division: {Calculator.divide(10, 5)}")
