
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.

def high(x):
    alph, answ, n = 'abcdefghijklmnopqrstuvwxyz', ['', 0], 0
    for i in x.split():
        for j in i:
            n += alph.find(j) + 1
        if n > answ[1]: answ[1], answ[0], n = n, i, 0
        else: n = 0
    return answ[0]