def factorial(n):
    """
    This function calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
    """

    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 4
result = factorial(number)
print(f"The factorial of {number} is {result}")
