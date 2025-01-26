
# Write a function,
# nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.
# If the 3rd letter is a consonant, return the first 3 letters.
# If the 3rd letter is a vowel, return the first 4 letters.

def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    elif name[2] not in 'aeiou':
        return name[:3]
    elif name[2] in 'aeiou':
        return name[:4]
