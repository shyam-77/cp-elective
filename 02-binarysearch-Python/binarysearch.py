"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    #test_list = [1,3,9,11,15,19,29]
    s=0 
    e=len(input_array)
    m=(s+e)//2
    while input_array[m]!=value and s<e:
        if input_array[m]>value:
            e=m-1
        else:
            s=m+1
        m=(s+e)//2    
        
    return m if input_array[m]==value else -1
