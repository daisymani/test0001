def add_and_subtract(num1, num2, num3):
    """Returns the result of adding the first two numbers and subtracting the third."""
    return num1 + num2 - num3

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = add_and_subtract(num1, num2, num3)
print(f"The result of adding {num1} and {num2}, then subtracting {num3}, is: {result}")