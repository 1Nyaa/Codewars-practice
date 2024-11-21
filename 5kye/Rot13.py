
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after
# it in the alphabet. ROT13 is an example of the Caesar cipher.


def rot13(message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_rot = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                    'g', 'h', 'i', 'j', 'k', 'l', 'm']
    # i'm so sorry :(

    answ = []

    for i in message:
        for j in i:
            if j.lower() in alphabet:
                n = alphabet.index(j.lower())
                if j.islower():
                    answ.append(alphabet_rot[n])
                else:
                    answ.append(alphabet_rot[n].upper())
            else:
                answ.append(j)