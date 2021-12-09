# 1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
# 3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
# 4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
# 5、使用空调对象获取空调的品牌和价格并打印到控制台上；
# 6、使用空调对象调用开机方法；
# 7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
# 其中语句中的“xxx”是调用方法时传递的具体数据值；
'''
class kong :
    __pin=''
    __price=''

    def set_pin(self,setpin):
        self.__pin =setpin

    def get_pin(self):
        return self.__pin

    def set_prince(self,setprice):
        self.__price =setprice

    def get_price(self):
        return self.__price

    def open(self):
        print('空调开了')

    def close(self,time):
        print('空调将在%s分钟后自动关闭'%time)

p = kong()
p.set_pin('格力')
p.set_prince('1000')
print('品牌为%s,价格为%s'%(p.get_pin(),p.get_price()))
p.open()
p.close(5)

'''

# 定义一个学生类和对应的测试类
# 要求：
# 1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
# 2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
# “大家好，我叫xxx，今年xxx岁了！”
# 3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
# 4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
# 5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
# 6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；

'''
class student:
    __age=''
    __name=''

    def set_age(self,age):
        self.__age =age

    def get_age(self):
        return self.__age

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def showme(self):
        print('大家好，我叫%s，今年%s岁了！'%( self.__name,self.__age))
    def chkage(self,chkage):
        if chkage > self.__age:
            print('我比同桌大%s岁！'%(chkage-self.__age))
        elif chkage < self.__age:
            print('我比同桌小%s岁！'%(self.__age-chkage))
        elif chkage == self.__age:
            print('我和同桌一样大！')

s = student()
s.set_age(18)
s.set_name('王明')
a = student()
a.set_age(10)
a.set_name('我')
a.showme()
s.chkage(a.get_age())

'''


# 题目三：打电话业务逻辑
# 人类：
# 属性:
# 姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
# 功能：
# 发短信（要求参数传入短信内容）。
# 打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否小于1元，若为空或者小于1元则报相对应的错误信息，
# 否则的话拨通。结束后，按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））

'''
class person :
    name=''
    sex=''
    age=''
    phc=0           #余额
    ppp=''          #品牌
    peg=''          #电池容量
    pwin=''         #分辨率
    ptim=''         #待机时长
    pscr=0          #积分

    def putmes(self,mes):
        print('短信内容为：',mes)

    def putphon(self,count,time):
        if len(count)==0:
            print('输入号码为空')
        else:
            if self.phc < 1 :
                print('余额不足1元')
            else:
                print('正在为您拨通...')
                if time<10 and time>0:
                    self.phc-=time
                    self.pscr=time*15
                    print('余额剩余%s,积分为%s' % (self.phc, self.pscr))
                elif time>10 and time<20:
                    self.phc-=0.8*time
                    self.pscr=time*39
                    print('余额剩余%s,积分为%s' % (self.phc, self.pscr))
                else:
                    self.phc -= 0.65 * time
                    self.pscr = time * 48
                    print('余额剩余%s,积分为%s'%( self.phc,self.pscr))


a=person()
a.phc=1000
a.putmes('你好')
a.putphon('13313025208',5)

'''


# 题目四：需求编程
# i.	定义了一个学生类：属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。行为：学习（要求参数传入学习的时间），
# 玩游戏（要求参数传入游戏名），编程（要求参数传入写代码的行数），数的求和（要求参数用变长参数来做，返回求和结果）


class student:
    count=''
    name=''
    age=''
    sex=''
    high=''
    weigh=''
    score=''
    address=''
    callnumber=''

    def learn(self,time):
        print('学习了%s个小时'%time)

    def play(self,game_name):
        print('玩了%s' % game_name)

    def python(self,line):
        print('写了%s行代码' % line)

    def sum(self,*number):
        print('和为',sum (number))
        print(number)

a=student()
a.learn(10)
a.play('DNF')
a.python(10)
a.sum(1,2,3,4)


# ii.	车类：属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。功能：跑（要求参数传入车的具体功能，比如越野，赛车）
# 创建：法拉利，宝马，铃木，五菱，拖拉机对象
class car:
    type=''
    count=0
    colour=''
    weight=''
    oil=''

    def run(self,type):
        print('%s跑'%type)

b=car()
b.type='法拉利'
b.run ('跑车')
c=car()
c.type='宝马'
c.run='轿车'
d=car()
d.type='铃木'
d.run('拖拉机')


# iii.	笔记本：属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  行为：打游戏（传入游戏的名称）,办公。
class computer:
    type=''
    time=''
    colour=''
    weight=''
    cpu=''
    rad=''
    pan=''
    def game(self,name):
        print('打',name)
    def work(self):
        print('工作')

e=computer()
e.game('CF')





# iv.	猴子类：属性：类别，性别，身体颜色，体重。行为：造火（要求传入造火的材料：比如木棍还是石头），学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）

class monkey:
    type=''
    sex=''
    colour=''
    weight=''

    def fire(self,material):
        print('用%s生火'%material)
    def learn(self,*thing):
        print('学习',thing)

f=monkey()
f.learn('看电视','玩游戏','打乒乓球')