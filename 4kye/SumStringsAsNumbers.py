# Given the string representations of two integers, return the string representation of the sum of those integers.
# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

from gmpy2 import mpz

def sum_strings(x, y):
    if x == '':
        x = '0'
    if y == '':
        y = '0'
    return (mpz(x) + mpz(y)).digits()

# def sum(num1, num2):
#     if len(num1) < len(num2):
#         num1, num2 = num2, num1
#
#     result = []
#     carry = 0
#
#     i, j = len(num1) - 1, len(num2) - 1
#
#     while i >= 0 or j >= 0 or carry > 0:
#         digit1 = int(num1[i]) if i >= 0 else 0
#         digit2 = int(num2[j]) if j >= 0 else 0
#
#         total = digit1 + digit2 + carry
#         result.append(str(total % 10))
#         carry = total // 10
#
#         i -= 1
#         j -= 1
#
#     result.reverse()
#     return ''.join(result)
#
#
# def sum_strings(x, y):
#     result = sum(x, y)
#     if result == '':
#         return '0'
#     elif result[0] == '0' and len(result) > 1:
#         return result[1:]
#     return result