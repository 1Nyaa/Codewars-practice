
def cyclic_index(arr, n):
    length = len(arr)
    return (n - 1) % length


def last_digit(n1, n2):
    if str(n1 ** n2)[-1] == '6' or str(n1 ** n2)[-1] == '6' or str(n1 ** n2)[-1] == '5':
        return int(str(n1 ** n2)[-1])
    elif str(n1 ** n2)[-1] == '2':
        arr = [2, 4, 8, 6]
        return(cycl_shft(arr,))
        pass
    elif str(n1 ** n2)[-1] == '3':
        arr = [3, 9, 7, 1]
        pass
    elif str(n1 ** n2)[-1] == '4':
        arr = [4, 6]
        pass
    elif str(n1 ** n2)[-1] == '7':
        arr = [7, 9, 3, 1]
        pass
    elif str(n1 ** n2)[-1] == '8':
        arr = [8, 4, 2, 6]
        pass
    elif str(n1 ** n2)[-1] == '9':
        arr = [9, 1]
        pass

print(last_digit(2 ** 200, 2 ** 300))