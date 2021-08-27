"""
My implementation of binary search.

Binary search attempts to find a given value within an SORTED array by analyzing the midpoint value.
If the target value is larger/smaller than the midpoint value, the binary search algorithm 
updates the bounds of it's array search
of the array and updates the indexes of the lower_bound, the upper_bound, and of course the new midpoint of the subarray.

The binary search algorithm performs this task until a value is found OR the lower_bound and upper_bound indexes point 
to the same element (which indicates the entire array has been traversed and the value has not being found)

some variable definitions:

midway point => The index variable that points to the "middle" value in a given array. It is calculated using the floor function.

lower_bound => the index variable that points to the lower bound of the array's search

upper_bound => the index variable that points to the upper bound of the array's search

"""

import math

def binary_search(arr_list,target):


    lower_index = 0

    upper_index = len(arr_list) - 1

    while lower_index <= upper_index:
        midpoint = math.floor( (lower_index+upper_index) / 2 )
        if(arr_list[midpoint] == target):
            return midpoint
        elif( arr_list[midpoint] < target):
            ## Update lower and upper bounds to reflect values below the current midpoint.
            lower_index = midpoint + 1
        else:
            upper_index = midpoint - 1 

    return -1

