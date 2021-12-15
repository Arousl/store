
from threading import Thread
import time


take_money=0
bag = 0
clock=3
out = 0





class time_out(Thread):
    def run(self) -> None:
        global clock
        for i in range(3):
            clock -= 1
            print('时间还剩%s分钟'%clock)
            time.sleep(2)







class cooker(Thread):
    name=''
    pay=0
    count=0

    def run(self) -> None:
        global clock
        global bag
        global take_money
        global out
        while True:
            if clock==0:
                take_money -= self.count * 1.5
                print(self.name,'做了',self.count,'个','挣了',self.count*1.5)
                break
            elif bag == 500:
                time.sleep(3)

            elif bag<500 :
                self.count =self.count + 1
                bag = bag + 1
                # print(self.name,'做个1个蛋挞')









class buyer(Thread):
    name=''
    money=30000
    count=0



    def run(self) -> None:
        global bag
        global take_money
        global clock
        global out
        while True:
            if bag>0 and self.money>0 and clock!=0:
                self.count += 1
                bag -= 1
                out += 1
                self.money -= 3
                take_money += 3
                # print(self.name,'买了一个蛋挞')

            elif clock==0:
                print(self.name,'买到：',self.count,'个,钱包余额为：',self.money)
                break











c1=cooker()
c2=cooker()
c3=cooker()

b1=buyer()
b2=buyer()
b3=buyer()
b4=buyer()
b5=buyer()

t1=time_out()
t1.start()

c1.name='c11'
c2.name='c22'
c3.name='c33'

b1.name='GU11'
b2.name='GU22'
b3.name='GU33'
b4.name='GU44'
b5.name='GU55'

c1.start()
c2.start()
c3.start()



b1.start()
b2.start()
b3.start()
b4.start()
b5.start()

# cc1=c1.count
# cc2=c2.count
# cc3=c3.count
# all=cc1+cc2+cc3
#
# class pay_ment(Thread):
#     pay=0
#     all=0
#     count=0
#     name=''
#     def run(self) -> None:
#         global out
#         while True:
#             if clock==0:
#                 self.pay=self.count/self.all*out*1.5
#                 print(self.name,'工资为',self.pay)
#                 break
#             else:
#                 pass
#
#
#
#
#
#
#
#
# p1=pay_ment()
# p2=pay_ment()
# p3=pay_ment()
#
# p1.name='c11'
# p2.name='c22'
# p3.name='c33'
#
# p1.all=all
# p2.all=all
# p3.all=all
#
# p1.count=cc1
# p2.count=cc2
# p3.count=cc3
#
# p1.start()
# p2.start()
# p3.start()