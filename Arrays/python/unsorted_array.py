from typing import Union
from .core import Array

class UnsortedArray:
    def __init__(self, max_size, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        # actual number of elements stored in the array 
        self._size = 0

    def __len__(self) -> int:
        '''
        Returns the number of elements in the array.

        Parameters:
            None

        Returns:
            int: number of elements in the array
        '''

        return self._size
    
    def __getitem__(self, index) -> Union[int, float]:
        '''
        Get the value at a given index

        Parameters:
            index (int): the index to get the value from

        Returns:
            Union[int, float]: The value at the given index
        '''

        if index < 0 or index > self._size:
            raise ValueError(f'index {index} is out of bound')
        return self._array[index]

    def __repr__(self) -> str:
        '''
        Return the String representation of the array.

        Parameters:
            None

        Returns:
            str: The string representation of the array.
        '''

        return f'UnsortedArray({repr(self._array._array[:self._size])})'
    

    def max_size(self):
        '''
        Return the number of elements that the array can hold

        Parameters:
            None

        Returns:
            int: the max size of the array
        '''
        return self._max_size

    def insert(self, new_entry) -> None:
        '''
        Insert and entry into an unsorted array.

        Parameters:
            new_entry (Any): The entry to insert
        '''

        if self._size >= len(self._array):
            raise ValueError('The Array is already full')
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index) -> None:
        '''
        Delete an entry at a given index from an unsorted array.

        Parameters:
            index (int): the index of the entry to delete
        '''

        if self._size == 0:
            raise ValueError('Delete from an Empty Array')
        elif index < 0 or index >= self._size:
            raise ValueError(f'Index {index} out of range.')
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1
    
    def find(self, target) -> int:
        '''
        Find the index of the target entry in the unsorted array.

        Parameters:
            target (Any): The entry to search for.

            Returns:
                int: the index of the first occurrence of the target entry, else None
        '''

        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        # target not found 
        return None
    
    def traverse(self, callback):
        '''
        Traverse an unsorted array and vall a callback function on each element.

        Parameters: 
            callback (function): function to call on each element
        '''
        for index in range(self._size):
            callback(self._array[index])
    # array.traverse(print)


    def min_in_array(self) -> tuple[Union[int, float], int]:
        
        '''
        Get the minimum value in an array

        Parameters:
            None

        Returns:
            tuple: (min, index):
                min(int or float): The minimum value in the array
                index(int): index of minimum value
        '''
        min_value_index = 0
        for index in range(1, len(self._array)):
            if self._array[index] < self._array[min_value_index]:
                min_value_index = index
        return self._array[min_value_index] , min_value_index
    
    def max_in_array(self) -> tuple[Union[int, float], int]:
        
        '''
        Get the maximum value in an array

        Parameters:
            None

        Returns:
            tuple: (max, index):
                max(int or float): The minimum value in the array
                index(int): index of minimum value
        '''
        max_value_index = 0
        for index in range(1, len(self._array)):
            if self._array[index] > self._array[max_value_index]:
                max_value_index = index
        return self._array[max_value_index] , max_value_index

    def max_min_in_arr(self) -> tuple[Union[int, float], Union[int, float]]:

        '''
        Get the maximum and minimum values in an array

        Parameters:
            None

        Returns:
            tuple[Union[int, float], Union[int, float]]:
                min(int of float): The minimum value in the array
                max(int or float): The maximum value in the array
        '''
        min_value_index = 0
        max_value_index = 0

        for index in range(1, len(self._array)):
            if self._array[index] < self._array[min_value_index]:
                min_value_index = index
            if self._array[index] > self._array[max_value_index]:
                max_value_index = index

        return self._array[max_value_index], self._array[min_value_index]