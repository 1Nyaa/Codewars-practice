
# Given two positive integers n and p, we want to find a positive integer k, if it exists,
# such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.
# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k

def dig_pow(n, p):
    number_sum = 0
    for i in str(n):
        number_sum += int(i) ** p
        p += 1
    k = number_sum / n
    return k if k.is_integer() else -1