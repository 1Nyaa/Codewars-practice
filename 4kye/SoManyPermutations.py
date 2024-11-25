# In this kata,
# your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!

import itertools


def permutations(s):
    answ = set()
    for i in itertools.permutations(s, len(s)):
        answ.add(''.join(i))
    return(sorted(answ))
