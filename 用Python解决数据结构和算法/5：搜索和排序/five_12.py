def small_sum(arr):
    if not arr or len(arr)<1:
        return 0
    return merge_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, l, r):
    if l == r:
        return 0
    mid = l + ((r - l) >> 1)
    return merge_sort(arr, l, mid) + merge_sort(arr, mid + 1, r) + merge(arr, l, mid, r)

def merge(arr, l, m, r):
    help = []
    p1 = l
    p2 = m + 1
    res = 0
    while p1 <= m and p2 <= r:
        res += (r - p2 + 1) * arr[p1] if arr[p1] < arr[p2] else 0
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    while p1 <= m:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[l + i] = help[i]
    return res


arr = [1, 3, 4, 2, 5]
a = small_sum(arr)
print(a)