'''
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个辣条优惠券（0.3），20个威猛先生优惠券（0.9），免单一张优惠券，先整体打折8后在单独打折，
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
import random
'''

shop =[

    ['酱油',20],
    ['盐',15],
    ['电饭锅',299],
    ['辣条',20],
    ['威猛先生',80],
    ['电脑',500],
    ['苹果',30]

]
#优惠卷抽取
while True :
    x=input('请按1抽取你的优惠卷')
    if x =='1':
        j= random.randint(1,31)
        if j<11:
            j=0.3
            print('辣条优惠券3折')
            break
        elif j>10 and j<21:
            j=0.9
            print('威猛先生优惠券9折')
            break
        else:
            j=0
            print('恭喜抽中免单机会')
            break
    else:
        print('输入错误请重新抽取')
#准备阶段
mycar =[]
money=1000
#商城界面
while True:
    for i in enumerate(shop):
        print(i)
    o=input('请输入购买产品编号')
    if o =='q' or o=='Q':
        print('已退出,余额为',money)
        print(mycar)
        break

    else:
        if o.isdigit():
            o=int(o)
            if o<len(shop):
                if money>shop[o][1]:
                   mycar.append(shop[o])
                   if o== 3 and j==0.3:
                       money=money-shop[o][1]*j*0.8

                   elif o==4 and j==0.9:
                       money=money-shop[o][1]*j*0.8

                   elif j==0:
                       money=money

                   else:
                       money=money-shop[o][1]*0.8

                else:
                    print('余额不足')

                print('已购买的商品为',mycar)
                print('您的余额为：', money)
            else:
                print('输入非法')
        else:
            print('输入非法')

'''

#有一个列表，[“北京”,”上海”,”广东”]
# 1)	将中国所有省会城市添加到上述列表中
# 2)	广东成为第二大发达城市，将广东排在上海前面
# 3)	[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。

# city =['北京','上海','广东']
# ci=input('请输入城市')    #1、插入城市
# city.append(ci)

# u=city.pop(2)         #2、变换位置
# city.insert(1,u)
# print(city)

# gdp=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# print('总和为：%.2f'%sum(gdp),'平均值为：%.2f'%(sum(gdp)/8))                             #3、平均gdp


# 有以下一个列表，求其中是5的倍数的和
'''
a = [1,5,21,30,15,9,30,24]
sum=0
for i in a:
    if i%5 == 0:
        sum=sum+i
    else:
        sum=sum
print('和为：',sum)
'''

# List = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]
'''
List = [1,2,3,4,5,6,7,8,9]
i=0
while i<9:
    u=List.pop()
    List.insert(i,u)
    i +=1
    print(List)
    
    #print(list[::-1])
'''

# 请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
# from  collections import  Counter
# list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# print(Counter(list))

# 生成一个指定长度的验证码，验证码由英文字大小写和数字组成。


# li = []
# for i in range(65, 91):
#     li.append(chr(i))
# for a in range(97, 123):
#     li.append(chr(a))
# for b in range(48, 58):
#     li.append(chr(b))
# while True:
#     lg=int(input('请输入要生成验证码的长度'))
#     mm=random.sample(li,lg)
#     mm=''.join(mm)
#     print(li)
#     print('验证码为：',mm)


# 双色球选号：
# 1、双色球由7个两位数组成 前六个范围是1-33，第七个是1-15
# 2、后一个比前一个数大，第7个数字随机
# 3、键盘输入一个数字就打印几组数
#
# l1=[]
# for a in range(1,34):   #准备数组
#     l1.append(a)
# x=0
# c=int(input('请输入要获取的组数'))
# while x<c :
#     su= random.sample(l1,6)
#     su.sort()
#     l3=[]
#     for i in su:
#         if i<10:
#             i='0'+str(i)
#             l3.append(i)
#         else:
#             l3.append(i)
#     ss=random.randint(1,15)
#     if ss<10:
#         ss='0'+str(ss)
#     print(l3,'|',ss)
#     x +=1

# 打印杨辉三角形
# 10
# 110
# 1210
# 13310
# 146410
#________________________________________________________________

# num=input('请输入行数：')
# num =int(num)
# list1 =[] #list 用来保存杨辉三角
# for n in range(0,num):
#   row =[1] #保存行
#   list1.append(row)
#
#   if n ==0:
#     print(row)
#     continue
#   for m in range(1,n):
#     row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#   row.append(1)
#
#   print(row)
#///////////////////////////////////////////////////////
L=[1]
n=int(input('请输入层数'))
for i in range(n):
    print(L)
    L.append(0)
    L=[L[k]+L[k-1] for k in range (0,i+2)]

#/////////////////////////////////////////////////////

