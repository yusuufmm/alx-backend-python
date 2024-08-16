#!/usr/bin/env python3
"""6-sum_mixed_list.py: A function to sum a list of mixed integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
