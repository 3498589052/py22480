# a=1
# b=2
# print("变量&运算符的应用,要求10分钟内掌握")
# print("python运算，a=1,b=2")
# print('*'*90)
# print("a+b=",a+b)  #加法
# print('*'*90)
# print("a-b=",a-b)  #减法
# print('*'*90)
# print("a X b =",a*b)  #乘法
# print('*'*90)
# print("a➗b=",a/b)   #除法
# print('*'*90)
# print("\'a➗b\'取余数",a%b)  #取余
# print('*'*90)
# print('\'a的b次方\'',a**b)   #次方
# print('*'*90)
# print('\'a➗b\'整除，不要余数',a//b)  #整除
# print('*'*90)

# print("字符串常用方法,要求十分钟内掌握")
# s="Py22480"
# print(s.upper()) #字符串里的字母全大写
# print('*'*90)
# print(s.lower()) #字符串里的字母全小写
# print('*'*90)
# print(s.replace("y",'i'))  #替换字符串里的内容
# print('*'*90)
# print(s[0:2])  # [开始:结束:步长]
# print(s[::2],s[::-2])  # 步长为负数就会倒着来
# print(len(s))  #字符串的长度

import random   #if和while嵌套，掌握，15分钟
Number_User=random.randint(1,100)
chengji=0
while True :
    User_Number=int(input('请输入你猜的数字，按0退出：\n'))
    if User_Number ==0:
        print(f"当前得分为{chengji}")
        print("已退出")
        break


    elif User_Number > Number_User :
            print("猜大了")
    elif User_Number < Number_User :
            print("猜小了")
    elif Number_User == Number_User :
            chengji=chengji+1
            print("恭喜你，猜中了，当前+1分")



# 算法：两数之和，目标值为9，并打印出这个数的下标
# num =[2,7,11,15]
# for i,j in enumerate(num):
#     for x,c in enumerate(num):
#         if j+c==9 :
#             print(f"{j},{c}这两个数相加起来能够满足目标值")
#             print(f'{j}的下标值为{i}')
#             print(f'{c}的下标值为{x}')


