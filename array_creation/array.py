#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''
    
    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.values = alloc(initial_size) 
        self.logical_size = 0
        self.size = initial_size
        self.chunk_size = chunk_size

        
        
    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        return '%i of %i >>> %a' % (self.logical_size, self.size, self.values)
        # print('%i of %i >>> %a' % (self.logical_size, self.size, self.values + [None] * (self.size - self.logical_size)))
        
        
    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if index >= 0 and index <= self.logical_size - 1:
            return True
        else:
            raise Exception('%i is not within the bounds of the current array.' % index)
        
        
        
    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.size - self.logical_size == 0:
            self.size += self.chunk_size
            self.values = memcpy(alloc(self.size), self.values, self.size - self.chunk_size)
            

        
        
    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        if (self.size - self.logical_size) >= self.chunk_size:
            self.size -= self.chunk_size
            self.values = memcpy(alloc(self.size), self.values, self.size)
            
        
    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''

        self._check_increase()
        self.values[self.logical_size] = item
        self.logical_size += 1
        
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''

        if self._check_bounds(index):
            self._check_increase()
            for i in reversed(range(index, self.logical_size + 1)):
                self.values[i] = self.values[i - 1]
            self.values[index] = item
            self.logical_size += 1
                    
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''

        if self._check_bounds(index):
            self.values[index] = item
        
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''

        if self._check_bounds(index):
            return self.values[index]
        
    
    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''

        if self._check_bounds(index):
            for i in range(index, self.logical_size):
                try:
                    self.values[i] = self.values[i + 1]
                except IndexError:
                    self.values[i] = None
            self.logical_size -= 1
            self._check_decrease()
        
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''

        if self._check_bounds(index1) and self._check_bounds(index2):
            val1 = self.values[index1]
            self.values[index1] = self.values[index2]
            self.values[index2] = val1
        
        
        
        
###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''

    return [None] * size

    

def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''

    for i in range(0, size):
        dest[i] = source[i]
    return dest
   