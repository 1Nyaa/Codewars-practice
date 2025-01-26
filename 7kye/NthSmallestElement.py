
# Given an array/list of integers, find the Nth smallest element in the array.

def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]
