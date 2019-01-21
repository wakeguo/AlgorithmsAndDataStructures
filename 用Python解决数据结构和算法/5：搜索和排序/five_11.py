def small_sum(alist):
    if not alist or len(alist) < 2:
        return 0
    return mergeSort(alist, 0, len(alist)-1)


def mergeSort(alist, l, r):
    if l == r:
        return 0
    mid = (l + r)//2
    # mid = l + ((r - l) >> 1)
    return mergeSort(alist, l, mid) + mergeSort(alist, mid+1, r) + merge(alist, l, mid, r)


def merge(alist, l, m, r):
    i = l
    j = m + 1
    help = []
    res = 0
    while i <= m and j <= r:
        res += alist[i] * (r-j+1) if alist[i] < alist[j] else 0
        if alist[i] < alist[j]:
            help.append(alist[i])
            i += 1
        else:
            help.append(alist[j])
            j += 1
    while i <= m:
        help.append(alist[i])
        i += 1
    while j <= r:
        help.append(alist[j])
        j += 1
    for n in range(len(help)):
        alist[l+n] = help[n]
    return res


alist = [1, 3, 4, 2, 5]
a = small_sum(alist)
print(a)


























