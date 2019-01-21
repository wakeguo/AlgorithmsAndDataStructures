"""
选择排序
"""


def selectionSort1(alist):
    for index in range(len(alist)-1, 0, -1):
        maxpoint = 0
        for i in range(1, index+1):
            if alist[maxpoint] < alist[i]:
                maxpoint = i
        alist[index], alist[maxpoint] = alist[maxpoint], alist[index]
    return alist



def selectionSort2(alist):
    index = len(alist) - 1
    while index > 0:
        maxpoint = 0
        for i in range(1, index + 1):
            if alist[maxpoint] < alist[i]:
                maxpoint = i
        alist[index], alist[maxpoint] = alist[maxpoint], alist[index]
        index -= 1
    return alist


alist = [1, 3, 0, 9, 4, 7]
a = selectionSort2(alist)
print(a)


