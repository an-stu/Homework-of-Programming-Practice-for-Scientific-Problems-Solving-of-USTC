import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib
matplotlib.use('TkAgg')  # 为了在wsl2中显示图像,需要将matplotlib.use('TkAgg')放在最前面


class Location():
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distForm(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self) -> str:
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Field():
    def __init__(self) -> None:
        self.drunks = {}

    def addDrunk(self, drunk, loc: Location):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # 使用Location的move方法获得一个新位置
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk) -> Location:
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk():
    def __init__(self, name: str = None) -> None:
        self.name = name

    def __str__(self) -> str:
        if self.name != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    """有偏随机游走,向下走的步长变长"""

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


class TendencyDrunk(Drunk):
    """有倾向的随机游走, 向右走的概率变大"""

    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0),
                       (-1.0, 0.0), (0.0, 1.0)]
        return random.choice(stepChoices)


def walk(f: Field, d: Drunk, numSteps: int):
    """假设f是一个Field对象,d是f中的一个Drunk对象,numSteps是正整数。
       将d移动numStep次,返回这次游走最终位置与开始位置之间的距离"""
    start = Location(0, 0)
    for _ in range(numSteps):
        f.moveDrunk(d)
    return start.distForm(f.getLoc(d))


def simWalks(walkLengths, numTrials: int, dClass: Drunk):
    """假设walkLengths是非负整数有序数列,numTrials是正整数,
        dClass是Drunk的一个子类。
        模拟numTrials次游走,每次游走walkLengths中的某一步数。
        返回一个列表,表示每次模拟的最终距离"""
    Homer = dClass()
    origin = Location(0, 0)
    r = []
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        t = 0
        distances = []
        for numSteps in walkLengths:
            distances.append(round(walk(f, Homer, numSteps - t), 1))
            t = numSteps
        r.append(distances)
    return r


def drunkTest(walkLengths, numTrials, dClass: Drunk):
    """假设walkLengths是非负整数序列
        numTrials是正整数,dClass是Drunk的一个子类
        对于walkLengths的每个步数,运行numTrials次simWalk函数,并输出结果"""
    result = np.array(simWalks(walkLengths, numTrials, dClass))
    R = []
    for i in range(len(walkLengths)):
        # numSteps = walkLengths[i]
        distances = result[:, i]
        ave_dis = round(sum(distances) / len(distances), 4)
        # print(dClass.__name__, 'random walk of', numSteps, 'steps')
        # print(' Mean =', ave_dis)
        # print(' Max =', max(distances), 'Min =', min(distances))
        R.append(ave_dis)
    return R


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(num=1, figsize=(8, 8), dpi=120)
    plt.title('Random Walk', fontsize=20)
    walkLengths = range(1, 10000)

    sqrtwalkLengths = [round(i**0.5, 1) for i in walkLengths]
    plt.plot(walkLengths, sqrtwalkLengths, linestyle="--", label="步数的平方根")

    # 正常随机游走
    result1 = drunkTest(walkLengths, 1000, UsualDrunk)
    plt.plot(walkLengths, result1, label="正常随机游走")

    # 有偏随机游走
    result2 = drunkTest(walkLengths, 1000, ColdDrunk)
    plt.plot(walkLengths, result2, label="有偏随机游走", linestyle=":")

    # 有倾向随机游走
    result3 = drunkTest(walkLengths, 1000, TendencyDrunk)
    plt.plot(walkLengths, result3, label="有倾向随机游走", linestyle="-.")

    plt.xscale("log")  # 使用对数坐标
    plt.yscale("log")
    plt.xlabel("步数", fontsize=12)
    plt.ylabel("距远点的距离", fontsize=12)
    plt.legend()
    plt.savefig("RandomWalk.png")
    plt.show()
