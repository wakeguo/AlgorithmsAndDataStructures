


def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    else:

        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)

        i = 0
        j = 0
        help = []
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                help.append(lefthalf[i])
                i += 1
            else:
                help.append(righthalf[j])
                j += 1
        while i < len(lefthalf):
            help.append(lefthalf[i])
            i += 1
        while j < len(righthalf):
            help.append(righthalf[j])
            j += 1
        return help


def mergeSorts(alist):
    if len(alist) <= 1:
        return alist

    else:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        lefthalf = mergeSort(lefthalf)
        righthalf = mergeSort(righthalf)

        help = []
        while lefthalf and righthalf:
            min_val = lefthalf.pop(0) if lefthalf[0] < righthalf[0] else righthalf.pop(0)
            help.append(min_val)
        help += lefthalf if lefthalf else righthalf
        return help




alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = mergeSort(alist)
print(a)

















