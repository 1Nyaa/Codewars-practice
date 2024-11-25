
# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.

def reverse_words(s):
    words = s.split(' ')
    reversed_words = [word[::-1] for word in words]
    result = ' '.join(reversed_words)

    return result
