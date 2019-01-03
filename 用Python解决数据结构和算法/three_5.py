"""
队列介绍2
"""


import random


# 定义队列
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 模拟打印机
class Printer():
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印机单位时间打印张数
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


# 模拟一个打印任务
class Task():
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):  # 记录任务被创建和被放入打印队列的时间
        return self.timestamp

    def getPages(self):  # 需要打印的页数
        return self.pages

    def waitTime(self, currenttime):  # 打印开始前在队列中的等待时长
        return currenttime - self.timestamp


# 新的打印任务
def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:  # 打印任务每180秒到达一次
        return True
    else:
        return False


# 进行模拟打印
def simulation(numSeconds, pagesPerMinute):  # 打印机的总时长和单位时间打印张数

    labprinter = Printer(pagesPerMinute)  # 定义打印机
    printQueue = Queue()  # 定义队列
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():  # 判断是否为新的打印任务
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print('Average Wait %6.2f secs % 3d tasks remaining.' % (averageWait, printQueue.size()))


for i in range(10):
    simulation(3600, 10)



































