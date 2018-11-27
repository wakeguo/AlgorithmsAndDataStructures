"""
冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

冒泡排序算法的运作如下：
1、比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3、针对所有的元素重复以上的步骤，除了最后一个。
4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

"""


"""
方法一：使用for循环
"""


class Bubblesort():
    def fund(self, array):
        m = len(array)
        count = 0
        for n in range(m - 1, 0, -1):  # 注意不包含末端的，所以没有0的
            for i in range(n):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    count += 1
        return array, count


"""
方法二：使用while语句
"""


class Bubblesort():
    def fund(self, array):
        if array == None or len(array) < 2:
            return
        j = len(array) - 1
        count = 0  # 记录排序的次数
        while j > 0:
            i = 0
            while i < j:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    count += 1
                i += 1
            j -= 1
        return array, count

















