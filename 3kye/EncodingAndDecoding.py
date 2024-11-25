
# Create two functions to encode and then decode a string using the Rail Fence Cipher.
# This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails".
# First start off moving diagonally and down. When you reach the bottom,
# reverse direction and move diagonally and up until you reach the top rail.
# Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

# For example, the string "WEAREDISCOVEREDFLEEATONCE" would ben "WECRLTEERDSOEEFEAOCAIVDEN"

def encode_rail_fence_cipher(string, n):
    if not string:
        return ""

    n_lvls = ['' for i in range(n)]
    direction_down = True
    row = 0

    for char in string:
        n_lvls[row] += char

        if row == 0:
            direction_down = True
        elif row == n - 1:
            direction_down = False

        row += 1 if direction_down else -1

    return ''.join(n_lvls)


def decode_rail_fence_cipher(string, n):
    if not string:
        return ""

    n_lvls = []
    for i in range(n):
        n_lvls.append(['\n'] * len(string))
    direction_down = True
    row, col = 0, 0

    for char in string:
        if row == 0:
            direction_down = True
        if row == n - 1:
            direction_down = False

        n_lvls[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for r in range(n):
        for c in range(len(string)):
            if n_lvls[r][c] == '*':
                n_lvls[r][c] = string[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(string)):
        result.append(n_lvls[row][col])
        if row == 0:
            direction_down = True
        if row == n - 1:
            direction_down = False

        col += 1
        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)