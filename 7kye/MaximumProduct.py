
# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

def adjacent_element_product(array):
    n = -10000000
    for i in range(len(array[:-1])):
        if array[i] * array[i + 1] > n:
            n = array[i] * array[i + 1]
        else:
            continue
    return n
