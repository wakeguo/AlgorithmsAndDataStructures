

# 整数转换成任意进制的字符串, 栈帧来实现递归

from stack import Stack


rStack = Stack()


def toStr(n, base):
    convertString = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base

    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


print(toStr(10, 2))


def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]


print(toStr(10, 2))











