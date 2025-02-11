
# In this kata, you have an input string and you should check whether it is a valid message.
# To decide that, you need to split the string by the numbers,
# and then compare the numbers with the number of characters in the following substring.
#
# For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2, hi
# and the function should return true, because "hey" is 3 characters, "hello" is 5, and "hi" is 2;
# as the numbers and the character counts match, the result is true.

def is_a_valid_message(message):
    message = message.lower()
    count = message.translate({ord(i): ' ' for i in 'abcdefghijklmnopqrstuvwxyz'})
    words = message.translate({ord(i): ' ' for i in '1234567890'})
    count, words = count.split(), words.split()
    if len(count) != len(words) or (len(message) > 0 and not message[0].isdigit()):
        return False
    for i in range(len(count)):
        if int(count[i]) == len(words[i]):
            continue
        else:
            return False
    return True

is_a_valid_message("3hey5hello2hi")
is_a_valid_message("4code13hellocodewars")