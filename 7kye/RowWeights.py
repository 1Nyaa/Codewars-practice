
# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

def row_weights(array):
    n1, n2 = 0, 0
    for i in range(len(array)):
        if i % 2 == 0:
            n1 += array[i]
        else:
            n2 += array[i]
    return [n1, n2]
