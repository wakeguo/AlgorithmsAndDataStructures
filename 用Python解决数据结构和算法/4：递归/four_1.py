"""
递归介绍1
"""

# 计算整数数列和


def listsum1(numlist):
    theSum = 0
    for i in numlist:
        theSum = theSum + i
    return theSum


print(listsum1([1, 3, 5, 7, 9]))


def listsum2(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum2(numlist[1:])


print(listsum2([1, 3, 5, 7, 9]))












