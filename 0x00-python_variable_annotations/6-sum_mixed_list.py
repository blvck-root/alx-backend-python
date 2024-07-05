#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list."""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated sum_mixed_list function.

    Args:
        mxd_lst (List[Union(int, float)]): A list of ints and floats.

    Returns:
        float: A sum of a list with ints and floats.
    """
    return sum(mxd_lst)
