# Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
# and return as shown below. Index 0 will be considered even.

def capitalize(s):
    answ, c = '', 0

    if len(s) == 0:
        return ['', '']

    for i in s:
        if c % 2 == 0:
            answ += i.upper()
            c += 1
        else:
            answ += i
            c += 1

    answ += ' '
    c = 0

    for j in s:
        if c % 2 != 0:
            answ += j.upper()
            c += 1
        else:
            answ += j
            c += 1

    return answ.split()




capitalize("indexinglessons")