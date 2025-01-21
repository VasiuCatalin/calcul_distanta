import math


# Function to calculate the nth Fibonacci number using memoization
def fibonacci(n, memo=None):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    # Use default mutable argument only for the first call
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


# Function to calculate the area of a circle with input validation
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


# Function to find the maximum value in a list using recursion
def find_max(numbers):
    if not numbers:  # Check for an empty list
        raise ValueError("Cannot find the maximum of an empty list.")
    # Iterative approach to avoid recursion depth issues for large lists
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max


# Function to compute the geometric mean of a list of numbers
def geometric_mean(numbers):
    if not numbers:  # Check for an empty list
        raise ValueError("Cannot calculate geometric mean of an empty list.")
    if any(num <= 0 for num in numbers):
        raise ValueError("All numbers must be positive for geometric mean.")

    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))


# Main function to demonstrate the operations
def main():
    print("=== Fibonacci ===")
    n = 30
    try:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    except ValueError as e:
        print(e)

    print("\n=== Circle Area ===")
    radius = 5
    try:
        print(f"The area of a circle with radius {radius} is: {circle_area(radius)}")
    except ValueError as e:
        print(e)

    print("\n=== Find Max ===")
    numbers = [1, 3, 2, 8, 5]
    try:
        print(f"The maximum value in the list {numbers} is: {find_max(numbers)}")
    except ValueError as e:
        print(e)

    print("\n=== Geometric Mean ===")
    numbers = [1, 2, 3, 4]
    try:
        print(f"The geometric mean of {numbers} is: {geometric_mean(numbers)}")
    except ValueError as e:
        print(e)


main()
