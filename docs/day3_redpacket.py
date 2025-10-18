# day3_redpacket.py
import random

# def split_redpacket(total, num):
#     """total=总金额(元), num=份数, 返回列表[金额, ...]"""
#     # 1. 先随机生成 num-1 份
#     money = [round(random.uniform(0.01, total / num * 2), 2) for _ in range(num - 1)]
#     # 2. 最后一份 = 剩余金额，保证总和精确
#     money.append(round(total - sum(money), 2))
#     # 3. 打乱顺序
#     random.shuffle(money)
#     return money
#
#
# if __name__ == "__main__":
#     packets = split_redpacket(100, 10)
#     for i, m in enumerate(packets, 1):
#         print(f"第{i}个红包：{m} 元")
#

num=0
c=0
for _ in range(0,11) :
  num=num+1
  Money=random.randint(1,10)
  lst=[Money]
  for i in lst:
     print(f"第{num}个红包，里面有{i}元")
     c=c+i
print(f"红包总计一共是{c}元")



