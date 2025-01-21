from typing import Union
from core import Array

class UnsortedArray:
    def __init__(self, max_size, typecode = '1'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0
