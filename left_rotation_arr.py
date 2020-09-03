def rotLeft(a, d):
    while d > 0:
        b = a[0]
        for i in range(len(a)):
            # b = a[0]
            if i == len(a) - 1:
                a[i] = b
                break
            else:
                a[i] = a[i + 1]
        d -= 1
    return a


def rotLeft(a, d):
    n = len(a)
    rotarr = [0] * n

    for i in range(len(a)):
        new_i = (i + n - d) % n
        rotarr[new_i] = a[i]

    return rotarr


print(rotLeft([1,2,3,4,5],2))
