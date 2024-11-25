
# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
# your task is to find the sum of the minimum values in each row.

def sum_of_minimums(numbers):
    k = 0
    for i in range(len(numbers)):
        k += min(numbers[i])
    return k