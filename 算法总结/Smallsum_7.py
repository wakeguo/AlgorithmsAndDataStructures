#!/usr/bin/env python
# _*_ coding:utf-8 _*_




def Smallsum(array):
    if len(array) <= 1:
        return sum(array)
    else:
        mild = int(len(array)/2)
        left = Smallsum(array[:mild])
        right = Smallsum(array[mild:])
        return merge(left, right)


def merge(left, right):
















