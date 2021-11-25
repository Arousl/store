#输入10个数，自动求出和
'''
num = [1,2,3,4,5,6,7,8,9,10]
ac =[0,]
for i in num:
    print('请输入第',i,'个数')
    x =int( input())
    ac.insert(0,x)
print('和为：',sum(ac))
'''

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
'''
num = [1,2,3,4,5,6,7,8,9,10]
ac =[0,]
for i in num:
    print('请输入第',i,'个数')
    x =int( input())
    ac.insert(0,x)
print('和为：',sum(ac))
print('最大为：',max(ac))
print('平均为：',sum(ac)/10)
'''

#使用random模块，如何产生 50~150之间的数
'''
import random
ran = random.randint(50,150)
print(ran)
'''

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a=float(input('请输入三角形第一个边'))
b=float(input('请输入三角形第二个边'))
c=float(input('请输入三角形第三个边'))
if a>0 and b>0 and c>0:
    if a+b>c and b+c>a and c+a>b:
        if a==b and b==c and c==a:
            print('三角形为等边三角形')
        elif a==b or b==c or c==a:
            print('三角形为等腰三角形')
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            print('三角行为直角三角形')

    else:
        print('三角形为一般三角形')
else:
    print('无法构成三角形')
'''

#有以下两个数，使用+，-号实现两个数的调换。
'''
a=10
b=5
a=a+b
b=a-b
a=a-b
print(a,b)
'''

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
i=0
while i<3:
    uid = input('请输入用户名')
    pad = input('请输入密码')
    if uid == 'root' and pad == 'admin':
        print('登录成功')
        break
    else:
        print('用户名密码错误，您还有',2-i,'次机会')
        i += 1
        if i == 3:
            print("锁定")
'''

#编程实现99乘法表
# for x in range(1,10):
#     for y in range(1,11-x):
#         print(y,'X',10-x,'=',y*(10-x),end=" ")
#     print(" ")

#打印三角形
# for y in range(7,0,-1):
#     for x in range (1,y):
#         print(" ",end=' ')
#     for z in range (1,9-y):
#         print("*",end=' ')
#     for u in range (1,8-y):
#         print("*",end=' ')
#     print(' ')

#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# tall = 20
# day = 0
# i=0
# while i<20:
#     day +=1
#     i +=3
#     if i>20 or i==20:
#         print(day,'天')
#         break
#     else:
#         i -=2

#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
cu =[]
for i in range (1,21):
    x = 1
    u=i
    while u>1:
        x=x*u
        u -=1
    cu.insert(0,x)
print(sum(cu))
