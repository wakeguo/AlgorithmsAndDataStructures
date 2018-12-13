"""
大家都打过牌吧，理牌的时候，每人手里一把牌，一般都会按由大到小顺序排好，每抓一个新牌（比如 5），
都会找到4和6，把6往后挪一下，然后把5插到4和6之间。

插入排序算法的原理与理牌是一样的，在一组未排序或部分排序的物体中，将物体从左到右挨个比较，
每比较一次，将物体从小到大排好，每次比较后，前面几个物体都是排好序了的，后面的物体插入到前面已排好的序列，
以此类推直到全部排序完毕。

"""


def Insertsort(array):
    m = len(array)
    for i in range(1, m):  # 从第二个数开始比较
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


if __name__ == '__main__':
    array = [2, 1, 4, 0, 3, 8, 6]
    arrayed = Insertsort(array)
    print(arrayed)
















