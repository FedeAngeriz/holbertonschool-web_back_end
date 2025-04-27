#!/usr/bin/env python3
from typing import List, Tuple
# Function to return a list of tuples with each element and its length

def element_length(lst):
    return [(i, len(i)) for i in lst]
