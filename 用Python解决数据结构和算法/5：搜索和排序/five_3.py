"""
Hash查找
"""


class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:  # 还没有赋值时，直接进行赋值
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:  # 重新一个赋值
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:  # 保证搜索没有再次回到原槽，保证搜索操作不会陷入死循环；
                    stop = True  # 如果发生这种情况，我们已用尽所有可能的槽，并且项不存在。
        return data

    def __getitem__(self, key):  # 重载 __getitem__ 和__setitem__ 方法以允许使用 [] 访问
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = 'cat'
H[26] = 'dog'
H[93] = 'lion'
H[17] = 'tiger'
H[77] = 'bird'
H[31] = 'cow'
H[44] = 'goat'
H[55] = 'pig'
H[20] = 'chicken'

print(H.slots)
print(H.data)

print(H[20])

H[20] = 'duck'
print(H.data)







