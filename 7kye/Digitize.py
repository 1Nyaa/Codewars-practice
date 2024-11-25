
# Given a non-negative integer, return an array
# a list of the individual digits in order.
# 123 => [1, 2, 3]

def digitize(n):
    answ = [i for i in str(n)]
    return list(map(int, answ))
