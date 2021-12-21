from  collections import  Counter
import time

while True:
    ip=[]
    f1= open(file='baidu_x_system.log',mode='r+',encoding='utf8')
    for i in f1.readlines():
        u=i.split(' ',-1)
        ip.append(u[0])
    print(Counter(ip))
    time.sleep(30)
