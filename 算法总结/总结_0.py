# 冒泡
def Bobblesort(array):
    m = len(array)
    for i in range(m-1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# 选择排序
def Selectionsort(array):
    m = len(array)
    for i in range(0, m - 1):
        for j in range(i, m - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array




def Selectionsorts(array):
    m = len(array)
    for i in range(0, m - 1):
        for j in range(i + 1, m):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# 插入排序
def Insertsort(array):
    m = len(array)
    for i in range(1, m):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


# 递归选择最大值或最小值
def maxfun(array, L, R):
    if L == R:
        return array[L]
    else:
        Mild = int((L + R)/2)
        maxleft = maxfun(array, L, Mild)
        maxright = maxfun(array, Mild + 1, R)
        if maxleft > maxright:
            return maxleft
        else:
            return maxright



# 递归汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

