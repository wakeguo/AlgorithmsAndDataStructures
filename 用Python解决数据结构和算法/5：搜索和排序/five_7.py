"""
希尔排序
"""


def shellSort(alist):
    gap = len(alist)//6
    while gap > 0:

        for start in range(gap):
            gapInsertSort(alist, start, gap)

        print('After increments of size', gap, 'The list is', alist)
        gap = gap//6  # gap必须得有1才可以，不然是不能排序正确的


def gapInsertSort(alist, start, gap):
    for index in range(start+gap, len(alist), gap):
        currentvalue = alist[index]
        position = index

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue


alist = [4, 7, 9, 2, 3, 5, 6, 34, 23, 35, 98, 26, 45, 56, 66, 33]
shellSort(alist)
print(alist)
print(len(alist))




