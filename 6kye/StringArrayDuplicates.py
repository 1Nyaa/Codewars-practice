
# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters
# from each string in the array.
#
# For example:
#
# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
#
# dup(["kelless","keenness"]) = ["keles","kenes"].

def dup(strings):
    result = []
    for s in strings:
        new_s = []
        prev_char = ''
        for char in s:
            if char != prev_char:
                new_s.append(char)
                prev_char = char
        result.append(''.join(new_s))
    return result
