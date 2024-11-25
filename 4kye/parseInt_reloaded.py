
# In this kata we want to convert a string into an integer.
# The strings simply represent the numbers in words.

def parse_int(s):
    num_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }

    multi_map = {"hundred": 100, "thousand": 1000, "million": 1000000}

    result, current = 0, 0

    for word in s.replace('-', ' ').split():
        if word in num_map:
            current += num_map[word]
        elif word in multi_map:
            if word == "hundred":
                current *= multi_map[word]
            else:
                result += current * multi_map[word]
                current = 0

    return result + current
