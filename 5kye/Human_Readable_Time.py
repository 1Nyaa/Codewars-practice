
# Write a function, which takes a non-negative integer (seconds) as input and returns the
# time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59

def make_readable(ss):
    answ = list()
    hh = ss // 3600
    ss -= hh * 3600
    mm = ss // 60
    ss -= mm * 60
    for i in [hh,mm,ss]:
        if len(str(i)) > 1:
            answ.append(str(i))
        else:
            answ.append('0' + str(i))
    return f"{answ[0]}:{answ[1]}:{answ[2]}"
