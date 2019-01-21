"""
汉诺塔问题
"""


def move(n, a, b, c):
    if n >= 1:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


def moves(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        moves(n-1, a, c, b)
        moves(1, a, b, c)
        moves(n-1, b, a, c)


moves(3, 'A', 'B', 'C')





