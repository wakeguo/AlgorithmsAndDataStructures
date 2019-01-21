"""
冒泡排序和短路冒泡排序
"""


# 冒泡的两种基本方法
def bubbleSort1(alist):
    for index in range(len(alist)-1, 0, -1):
        for i in range(index):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


alist = [2]
bubbleSort1(alist)
print(alist)


def bubbleSort2(alist):
    index = len(alist) - 1
    while index > 0:
        for i in range(index):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        index -= 1
    return alist


alist = [2, 3, 5, 0, 8, 1]
m = bubbleSort2(alist)
print(m)



# 短路冒泡排序
def shortbubbleSort(alist):
    index = len(alist) - 1
    exchange = True
    while index > 0 and exchange:  # 只有采用while才能进行判断，这样才能减少循环比较次数
        exchange = False
        for i in range(index):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        index -= 1
    return


alist = [2, 3, 5, 7, 8, 9]
shortbubbleSort(alist)
print(alist)





