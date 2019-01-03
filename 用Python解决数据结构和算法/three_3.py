"""
栈的介绍3
"""


# 定义栈
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 把输入的数据转换成后缀表达式
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()  # 很重要的不然没法循环了，结束时会把栈中的"("删除

        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)


print(infixToPostfix('( A + B ) * ( C + D )'))
print(infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))


# 采用后缀表达式进行求值
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(token)
        else:
            operand2 = int(operandStack.pop())
            operand1 = int(operandStack.pop())
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


a = infixToPostfix('( 7 + 8 ) / ( 3 + 2 ) + 2 * ( 7 + 3 )')
print(a)
b = postfixEval(a)
print(b)

























