#!/usr/bin/env python3

FILENAMES = [
    [ 'list1.txt', 'int'   ],  # Interstates in USA
    [ 'list2.txt', 'int'   ],  # 2^N
    [ 'list3.txt', 'int'   ],  # World population since 1900
    [ 'list4.txt', 'int'   ],  # Fibanocci
    [ 'list5.txt', 'float' ],  # DJIA year end since 1896
    [ 'list6.txt', 'int'   ],  # average distance of planets from sun
]

        
class Result:
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None
        
        
def main():
    pass        
        
        
### Main runner ###
if __name__ == '__main__':
    main()