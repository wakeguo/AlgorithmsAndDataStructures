# 实质就是二分法进行分解


def maxfun(array, L, R):
    if L == R:
        return array[L]
    else:
        mild = int((L + R)/2)
        a = maxfun(array, L, mild)
        print('a: ', a)
        b = maxfun(array, mild + 1, R)
        print('b: ', b)
        if a < b:
            return b
        else:
            return a


array = [9, 1, 8, 2, 7, 3, 4]
if __name__ == '__main__':
    m = maxfun(array, 0, (len(array) - 1))
    print('m: ', m)


