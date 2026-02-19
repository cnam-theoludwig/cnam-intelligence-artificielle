import pytest

from src.factorial import factorial


def test_factorial_zero():
    # Arrange - Given
    input_value = 0
    expected = 1

    # Act - When
    output = factorial(input_value)

    # Assert - Then
    assert output == expected


def test_factorial_one():
    # Arrange - Given
    input_value = 1
    expected = 1

    # Act - When
    output = factorial(input_value)

    # Assert - Then
    assert output == expected


def test_factorial_five():
    # Arrange - Given
    input_value = 5
    expected = 120

    # Act - When
    output = factorial(input_value)

    # Assert - Then
    assert output == expected


def test_factorial_three():
    # Arrange - Given
    input_value = 3
    expected = 6

    # Act - When
    output = factorial(input_value)

    # Assert - Then
    assert output == expected


def test_factorial_negative_raises():
    # Arrange - Given
    input_value = -1

    # Act & Assert - When & Then
    with pytest.raises(ValueError):
        factorial(input_value)
