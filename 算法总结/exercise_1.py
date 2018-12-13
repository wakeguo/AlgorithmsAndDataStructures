


def maxfun(array, L, R):
    if L == R:
        return array[L]
    else:
        mild = int((L + R)/2)
        a = maxfun(array, L, mild)
        b = maxfun(array, mild + 1, R)
        if a > b:
            return b
        else:
            return a


array = [1, 2, 3, 4, 0, 9, 7, 5, 6, 10]
m = maxfun(array, 0, (len(array) - 1))
print(m)

