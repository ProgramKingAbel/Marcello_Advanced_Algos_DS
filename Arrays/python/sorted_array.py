from core import Array

class SortedArray():
    def __init__(self, max_size, typecode='l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError(f'The array is already full, maximum size {self._max_size}')
        
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
            else:
                self._array[i] = self._array[i-1]
        
        self._array[0] = value
        self._size += 1

    def delete_by_index(self, target_index):
        if target_index < 0 or target_index >= self._size:
            raise ValueError(f'Index {target_index} is out of bounds')
        
        for i in range(target_index, self._size - 1):
            self._array[i] = self._array[i + 1]
        
        self._size -= 1

    def delete(self, target):
        index = self.linear_search(target)

        if index is None:
            raise ValueError(f'Unable to delete alement {target}: the element is not in the array')
        
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size - 1
    
    def linear_search(self, target):
        for i in range(0, self._size):
            if self._array[i] == target:
                return i
            
            elif self._array[i] > target:
                return None
        return None
    
    def binary_search(self, target):
        left = 0
        right = self._size - 1

        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]

            if mid_val == target:
                return mid_index
            
            elif mid_val > target:
                right = mid_index - 1

            else:
                left = mid_index + 1
        return None
    
    def traverse(self, callback):
        for i in range(0, self._size):
            callback(self._array[i])