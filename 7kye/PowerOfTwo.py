
# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language)
# that determines if a given non-negative integer is a power of two.

def power_of_two(x):
    if bin(x).count('1') > 1 or x == 0:
        return False
    else:
        return True
