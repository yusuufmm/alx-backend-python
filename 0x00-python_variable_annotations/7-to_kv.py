#!/usr/bin/env python3
"""7-to_kv.py: A function to return a tuple with a string and the square of an int or float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))
