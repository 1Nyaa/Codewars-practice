
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and,
# you must return that string in an array where an uppercase letter is a person standing up.

def wave(people):
    answ = []
    for j in range(len(people)):
        preansw = [i for i in people]
        preansw[j] = preansw[j].upper()
        if preansw[j] != ' ':
            answ.append(''.join(preansw))
    return answ
