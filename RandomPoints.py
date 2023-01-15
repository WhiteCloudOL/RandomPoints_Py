"""
Edit By WhiteCloudCN
随机抽取给予点券，源码仅供参考与公示，请勿滥用与盗窃
"""

# 导入模块
from random import randint


# 定义块
n = int(input('请输入抽取人数:'))  # 玩家人数
ply = input('请输入最近在线玩家：').split(',')    # 待抽取玩家
plim = [400, 2400]  # 定义最小,最大值（单位：点券）
jz = 100    # 定义进制（最小单位换算制），最佳为10的n次方


# 函数块
def cy(x):
    return x // jz     # 进制为100，可选择其他


# 选取玩家，代码较繁杂但此项目没必要化简
plim = list(map(cy, plim))
print(plim)
pln = len(ply)
if pln > 1:
    i = 0
    pl = []
    while i < n:
        a = len(ply)
        rand = randint(0, a - 1)
        plc = ply[rand]
        ply.remove(plc)
        pl.append(plc)
        i += 1
else:
    pl = ply    # 特殊值
# 随机抽取一定数量点券给予已抽取的玩家
for i in pl:
    rr = str(randint(plim[0], plim[1]) * jz)
    print('玩家[' + i + ']:' + rr)
    print('points give ' + str(i) + ' ' + str(rr))
