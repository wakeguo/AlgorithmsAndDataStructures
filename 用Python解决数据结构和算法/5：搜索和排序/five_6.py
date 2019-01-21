"""
插入排序
"""


def insertSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue
    return alist


alist = [23, 3, 2, 0, 8, 33, 45]
insertSort(alist)
print(alist)





