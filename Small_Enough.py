def small_enough(array, limit):
    check = True
    for i in range(len(array)):
        num = array[i]
        if num <= limit:
            continue
        else:
            check = False
            return check
    return check


print(small_enough([1, 8, 58, 9, 12], 12))
