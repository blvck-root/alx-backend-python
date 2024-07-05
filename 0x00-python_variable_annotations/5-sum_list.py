#!/usr/bin/env python3
"""Type-annotated function sum_list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated sum_list function.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: Sum of a list of float numbers.
    """
    return sum(input_list)
