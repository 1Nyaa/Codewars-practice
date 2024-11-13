
# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.

# It should remove all values from list (a), which are present in list b keeping their order.

def array_diff(a, b):
    n = []
    for i in a:
        n.append(i) if i not in b else ""
    return n
