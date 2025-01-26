
# Write a program that outputs the top n elements from a list.

def largest(n, xs):
    return sorted(xs)[len(xs) - n:]
