"""
快速排序
"""
import random


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        temp = first + int(random.random() * (last - first + 1))  # 这两行是保证是随机快排的
        alist[first], alist[temp] = alist[temp], alist[first]

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):

    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            alist[rightmark], alist[leftmark] = alist[leftmark], alist[rightmark]

    alist[rightmark], alist[first] = alist[first], alist[rightmark]

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)















