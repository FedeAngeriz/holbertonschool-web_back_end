#!/usr/bin/env python3
"""Returns a tuple of size two containing a start index and an end index"""


def index_range(page: int, page_size: int) -> tuple:
    """Retuns a tuple of size two containing a start index and an end index"""
    index_start = (page - 1) * page_size
    index_end = page * page_size
    return (index_start, index_end)
