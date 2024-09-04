#!/usr/bin/env python3
"""
Simple function to calculate start and end indexes
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    @page refers: the specific page required
    @page_size: how much a specific page is
    ex: for the following dataset [x for x in range(21)]
        if a single page is 7 elements, the start and end indexes
        of the first page would be 0, 7
    """
    return ((page_size * page) - page_size, (page_size * page))
