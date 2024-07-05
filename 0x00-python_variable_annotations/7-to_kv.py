#!/usr/bin/env python3
"""Type-annotated function to_kv."""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function to_kv.

    Args:
        k (str): A string.
        v (int | float): A number.

    Returns:
        Tuple[str, float]: Tuple containing key and a number.
    """
    return (k, v ** 2)
