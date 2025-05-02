#!/usr/bin/env python3
"""Returns a tuple of size two containing a start index and an end index"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Retuns a tuple of size two containing a start index and an end index"""
    index_start = (page - 1) * page_size
    index_end = page * page_size
    return (index_start, index_end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index_start, index_end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[index_start:index_end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get a page of the dataset with hypermedia pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index_start, index_end = index_range(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        return {
            'page_size': len(dataset[index_start:index_end]),
            'page': page,
            'data': dataset[index_start:index_end],
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }