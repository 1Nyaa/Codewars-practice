# My friend John and I are members of the "Fat to Fit Club (FFC)".
# John is worried because each month a list with the weights of members is published and each month
# he is the last on the list which means he is the heaviest.
#
# I am the one who establishes the list so I told him:
# "Don't worry any more, I will modify the order of the list".
# It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
#
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
#
# Given a string with the weights of FFC members in normal order can you give this string ordered
# by "weights" of these numbers?


def order_weight(strng):
    strng = sorted(strng.split())
    answ = sorted(strng, key=sortbyweight)
    return ' '.join(map(str, answ))


def sortbyweight(wght):
    n = 0
    for i in str(wght):
        n += int(i)
    return n
