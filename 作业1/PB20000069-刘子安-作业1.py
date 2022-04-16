import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

plt.figure(num=1, figsize=(8,8), dpi=120)

# 第一幅图 函数图像
def draw1():
    t = np.arange(-np.pi, np.pi, 0.01)
    s = np.sin(t)
    c = np.cos(t)
    ax1 = plt.subplot(221)
    ax1.plot(t, s, color='red', linestyle='-', linewidth=3, label="$\sin{x}$")
    ax1.plot(t, c, color='blue', linestyle='--', linewidth=3, label="$\cos{x}$")
    ax1.plot(t, t/2, color='green', linestyle=':', linewidth=3, label="x/2")
    ax1.legend(loc="best")
    ax1.set_title('基本初等函数', fontsize=14, loc='center')
    ax1.axhline(y=0, ls='--', c='black')
    ax1.axvline(x=0, ls='--', c='black')
    ax1.scatter(0, 0, marker='o', s=80, c='black')
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-1, 1)
    ax1.set_xlabel("X", size=12)
    ax1.set_ylabel("Y", size=12)


# 第二幅图 堆叠图
def draw2():
    ax2 = plt.subplot(222)
    countries = ['Norway', 'Germany', 'China', 'USA', 'Sweden']
    bronzes = np.array([13, 5, 2, 7, 5])
    slivers = np.array([8, 10, 4, 10, 5])
    golds = np.array([16, 12, 9, 8, 8])

    ind = range(len(countries))

    ax2.bar(ind, golds, width=0.5, label='golds', color='gold', bottom=slivers+bronzes)
    ax2.bar(ind, slivers, width=0.5, label='slivers', color='#C0C0C0', bottom=bronzes)
    ax2.bar(ind, bronzes, width=0.5, label='bronzes', color='#B87333')

    ax2.set_xticks(ind, countries, fontsize=12)
    ax2.set_yticks([5, 10, 15, 20, 25, 30, 35, 40],fontsize=12)
    ax2.set_ylabel('Medals', size=16)
    ax2.set_xlabel('Countries', size=16)
    ax2.legend(loc='upper right')
    ax2.set_title('Medals of 2022 Beijing Winter Olympics', fontsize=14)

# 第三幅图 散点图
def draw3():
    ax3 = plt.subplot(223)
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    t = np.arctan2(y, x) # for color

    ax3.scatter(x, y, s=75, c=t, alpha= 0.5)
    ax3.set_title("随机散点图", fontsize=14)
    ax3.set_xlabel("random X", size=14)
    ax3.set_ylabel("random Y", size=14)
    ax3.set_xlim((-1.5, 1.5))
    ax3.set_ylim((-1.5, 1.5))

# 第四幅图 饼图
def draw4():
    ax4 = plt.subplot(224)
    label = ['计算机', '物理', '数学']
    explode = [0.01, 0.01, 0.01]
    values = [15, 20, 14]
    ax4.pie(values, explode=explode, labels=label, autopct='%.1f%%')
    ax4.set_title('专业人数饼图', y=-0.2, size=14)



if __name__ == "__main__":
    draw1()
    draw2()
    draw3()
    draw4()
    plt.show()