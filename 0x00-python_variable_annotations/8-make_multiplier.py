#!/usr/bin/env python3
"""Type-annotated function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier.

    Args:
        multiplier (float): The float value to be used for multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns its product with the multiplier (float).
    """

    def inner(number: float) -> float:
        """
        Inner function multiplies number with the pre-defined multiplier.

        Args:
            number (float): The float to be multiplied by
            the outer function's multiplier.

        Returns:
            float: The product of the number and the
            outer function's multiplier (float).
        """
        return number * multiplier

    return inner
