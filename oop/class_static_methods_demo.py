class DemoClass:
    # Class variable
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def show_class_variable(cls):
        """A class method to access class-level data."""
        return f"Class Variable: {cls.class_variable}"

    @staticmethod
    def calculate_sum(a, b):
        """A static method to perform a utility task."""
        return f"Sum of {a} and {b}: {a + b}"

# Testing the implementation
if __name__ == "__main__":
    # Using the class method
    print(DemoClass.show_class_variable())  # Output: Class Variable: I am a class variable

    # Using the static method
    print(DemoClass.calculate_sum(5, 7))  # Output: Sum of 5 and 7: 12
