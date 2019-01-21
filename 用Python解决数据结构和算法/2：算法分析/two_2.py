"""
变位词的检测复杂度对比
"""


def anagram_solution1(s1, s2):  # 时间复杂度是O(n**2)
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == s2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 += 1
    return still_ok, a_list


def anagram_solution2(s1, s2):  # 时间复杂度O(n) + 2 * O(n*logn) = O(n*logn)
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()  # O(nlogn)
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos += 1
        else:
            matches = False
    return matches


def anagram_solution3(s1, s2):  # 时间复杂度是O(n)
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok


a = 'abcd'
b = 'dcba'
m, n = anagram_solution1(a, b)
print(m, n)
# print(anagram_solution1(a, b))
