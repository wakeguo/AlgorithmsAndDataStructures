#!/usr/bin/env python
# _*_ coding:utf-8 _*_




def merge(left, right):
    help = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            help.append(left[i])
            i += 1
        else:
            help.append(right[j])
            j += 1
    while i < len(left):
        help.append(left[i])
        i += 1
    while j < len(right):
        help.append(right[j])
        j += 1
    # help.extend(left[i:])  # help += letf[i:]
    # help.extend(right[j:])
    return help



def merges(left, right):
    help = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        help.append(min_val)
    help += left if left else right
    return help



def Mergesort(array):
    if len(array) <= 1:
        return array
    else:
        mild = int(len(array)/2)
        left = Mergesort(array[:mild])
        right = Mergesort(array[mild:])
        return merges(left, right)



array = [1, 9, 3, 8, 4, 7]
a = Mergesort(array)
print(a)










