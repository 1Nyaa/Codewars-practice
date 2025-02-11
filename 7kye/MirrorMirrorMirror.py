
# The list will always consist of integers in range -1000..1000
# and will vary in size between 0 and 10000.
# Your function should not mutate the input array, and this will be tested (where applicable).
# Notice that the returned list will always be of odd size, since there will always be a definitive middle element.

def mirror(data: list):
    n1 = sorted(data)
    n2 = n1[::-1]
    return n1 + n2[1:]