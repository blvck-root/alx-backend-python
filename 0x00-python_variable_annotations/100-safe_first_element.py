#!/usr/bin/env python3
"""Duck typing - first element of a sequence."""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type-annotated safe_first_element function.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Any: first element in a sequence or None if lst is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
