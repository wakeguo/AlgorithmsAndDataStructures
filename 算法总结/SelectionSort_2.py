"""
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到
其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

"""


def Selectionsort(array):
    m = len(array)      # 循环 m - 1 次
    for i in range(0, m - 1):
        # min_index = i  # 假设的最小元素下标

        # 从 i + 1 位置循环到末尾找到最小值
        for j in range(i + 1, m):
            if array[j] < array[i]:  # 每次都是选取第一个为基准不动，后面的与其进行比较，选取一个最小的赋值给第一个
                # min_index = j
                array[i], array[j] = array[j], array[i]
    return array


# 实质就是和冒泡排序一样，只是这是反着用的选择最小值，放在最左侧
def Selectionsorts(array):
    m = len(array)
    for i in range(0, m - 1):
        for j in range(i, m - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



def Selectionsortss(array):
    m = len(array)
    for j in range(0, m - 1):
        min_index = j
        for i in range(j + 1, m):
            if array[min_index] > array[i]:
                min_index = i
        if j != min_index:
            array[j], array[min_index] = array[min_index], array[j]
    return array







