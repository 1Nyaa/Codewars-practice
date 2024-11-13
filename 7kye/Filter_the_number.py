
# Oh, no! The number has been mixed up with the text.
# Your goal is to retrieve the number from the text,

# can you return the number back to its original state?

def filter_string(st):
    answ = []
    for i in st:
        answ.append(i) if i in '1234567890' else ''
    return int(''.join(answ))
