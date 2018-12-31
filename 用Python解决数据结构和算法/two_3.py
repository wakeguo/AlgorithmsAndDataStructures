"""
关于列表和字典的复杂度的对比
"""

from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer('test1()', 'from __main__ import test1')
print('concat', t1.timeit(number=1000), 'millisecond')

t2 = Timer('test2()', 'from __main__ import test2')
print('append', t2.timeit(number=1000), 'millisecond')

t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension', t3.timeit(number=1000), 'millisecond')

t4 = Timer('test4()', 'from __main__ import test4')
print('list range', t4.timeit(number=1000), 'millisecond')

# concat 2.042292299195132 millisecond
# append 0.12109842330018372 millisecond
# comprehension 0.04601161468199466 millisecond
# list range 0.017865928876270143 millisecond


pop_zero = Timer('x.pop(0)', 'from __main__ import x')
pop_end = Timer('x.pop()', 'from __main__ import x')


x = list(range(2000000))
a = pop_zero.timeit(number=1000)
b = pop_end.timeit(number=1000)

print(a)
print(b)

# 1.852117116741474
# 0.00013342835827234723
