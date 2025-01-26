
# Write a function - triple_double(num1, num2)
# which takes numbers num1 and num2 and returns 1
# if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# If this isn't the case, return 0

def triple_double(num1, num2):
    num1, num2 = str(num1), str(num2)
    answ1, answ2 = 0, 0

    for i in range(len(num1) - 2):
        if num1[i] == num1[i + 1] == num1[i + 2]:
            answ1 = num1[i]
    for j in range(len(num2) - 1):
        if num2[j] == num2[j + 1]:
            answ2 = num2[j]

    if answ2 == answ1 != 0:
        return 1
    else:
        return 0
