
# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.


def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = [str(alphabet.find(i.lower()) + 1) for i in text if i.lower() in alphabet]
    return ' '.join(ans)
