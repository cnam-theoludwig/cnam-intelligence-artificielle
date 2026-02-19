def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("number must be a non-negative integer")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result
