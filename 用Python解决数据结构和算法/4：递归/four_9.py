"""
动态规划：找零钱问题
"""


# # 通过循环,但是没有跟踪
# def dpMakeChange(coinValueList, change, minCoins):
#     for cents in range(change+1):
#         coinCount = cents  # 这是按每个都是1美分时的最大情况
#         for j in [c for c in coinValueList if c <= cents]:
#             if minCoins[cents-j] + 1 < coinCount:
#                 coinCount = minCoins[cents-j] + 1
#         minCoins[cents] = coinCount
#     return minCoins[change]
#
#
#
# a = [5, 1, 10, 25]
# b = 10
# c = [0] * 11
# d = dpMakeChange(a, b, c)
# print(c)
# print(d)


# 通过循环,有跟踪
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents  # 这是按每个都是1美分时的最大情况
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j

        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


# a = [1, 5, 10, 25]
# b = 11
# c = [0] * 12
# d = [0] * 12
# m, n = dpMakeChange(a, b, c, d)
# print(m)
# print(n)


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    amnt = 45
    clist = [1, 5, 10, 21, 25]
    coinCount = [0] * (amnt+1)
    coinsUsed = [0] * (amnt + 1)
    print('Making change for', amnt, 'requires')
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed))
    print('They are:')
    printCoins(coinsUsed, amnt)
    print('coinCount: ', coinCount)
    print('coinsUsed: ', coinsUsed)


main()