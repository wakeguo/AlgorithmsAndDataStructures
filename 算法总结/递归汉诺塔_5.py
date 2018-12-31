# 汉诺塔问题，要保证大的在下面，小的在上面
# 实质先把上面的(n-1)个看成整体，先从a-->b，然后a-->c, 最后b-->c


def move(n, a, b, c):  # 理解中间的是不动的
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')



count = 0  # 总共多少步
def moves(n, a, b, c):
    global count
    if n == 1:
        print('{}: {} --> {}'.format(1, a, c))
        count += 1
    else:
        moves(n-1, a, c, b)
        print('{}: {} --> {}'.format(n, a, c))
        count += 1
        moves(n-1, b, a, c)


moves(3, 'A', 'B', 'C')
print(count)
