"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

"""
方法一：使用replace
"""


class Solution():
    # s 字符串
    def replaceSpace(self, s):
        s = s.replace(' ', '%20')
        return s


s = 'we are happy.'
a = Solution()
b = a.replaceSpace(s)
print(b)






















