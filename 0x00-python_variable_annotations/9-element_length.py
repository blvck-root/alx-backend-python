#!/usr/bin/env python3
"""Let's duck type an iterable object."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function element_length.

    Args:
    lst (Iterable): An iterable sequence.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples containing
    sequence-length pairs.
    """
    return [(i, len(i)) for i in lst]
