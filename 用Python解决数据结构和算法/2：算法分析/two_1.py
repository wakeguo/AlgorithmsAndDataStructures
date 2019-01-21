import time


def sum_1(n):  # 时间复杂度为O(n)
    start = time.perf_counter()  # time.time()
    the_sum = 0
    for i in range(n + 1):
        the_sum += i
    end = time.perf_counter()  # time.time()
    m = end - start
    return the_sum, m


def sum_2(n):  # 时间复杂度为O(1)
    start = time.perf_counter()
    a = n*(n + 1)/2
    end = time.perf_counter()
    b = start - end
    return a, b


for j in range(5):
    a, b = sum_1(100000)
    print('数字:{}, 时间:{}'.format(a, b))
    print('sum is %d, time is %f' % sum_2(100000))
