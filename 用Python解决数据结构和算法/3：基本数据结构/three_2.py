"""
栈的介绍2
"""


# 定义栈
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def divideBy2(decNumber):  # 十进制转换成二进制
    remstack = Stack()

    while decNumber > 0:  # 进栈
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():  # 出栈
        binString = binString + str(remstack.pop())

    return binString


print(divideBy2(200))


def baseConverter(decNumber, base):  # 十进制转换成任意进制
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


print(baseConverter(233, 5))









