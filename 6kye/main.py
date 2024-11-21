
# Write a function that accepts a string,
# and returns the same string with all even indexed characters in each word upper cased,
# and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
# so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

def to_weird_case(words):
    c, answ, word = 0, [], ''
    word_checker = words.lower().split()

    for i in word_checker:
        for j in i:
            if c % 2 == 0:
                word += j.upper()
                c += 1
            else:
                word += j
                c += 1
        answ.append(word)

        if word.lower() != word_checker[-1]:
            answ.append(' ')
        c, word = 0, ''

    return ''.join(answ)
