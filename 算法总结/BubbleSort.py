"""
冒泡排序
"""


class Bubblesort():
    def fund(self, array):
        if array == None or len(array) < 2:
            return
        i = 0
        j = len(array)
        while j > 0:
            j -= 1
            while i < j:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i +1], array[i]


                i += 1
        return array


array = [3, 2, 4, 0, 7]
a = Bubblesort()
b = a.fund(array)
print(b)



























