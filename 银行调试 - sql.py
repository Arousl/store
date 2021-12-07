import random
from BDmysql import update
from BDmysql import select
print("===============")    #界面显示
print("|  中国工商银行 |")
print("===============")
print("|1、开户       |")
print("|2、存钱       |")
print("|3、取钱       |")
print("|4、转账       |")
print("|5、查询       |")
print("|6、退出       |")
print("===============")
#建立库
# bank={11111111:{'password':'123456','name':123,'country':123,'province':13,'street':12,'door':12,'bank_name':'工商银行','money':800}  }       #存储用户信息
# bank_name='工商银行'    #写死的银行名字
def useradd():          #定义添加用户函数
    card_id=random.randint(10000000,99999999)   #随机生成的卡号
    password=pass_word()                        #验证密码格式循环

    name=input('请输入姓名')
    country=input('请输入国家')
    province=input('请输入省')
    street=input('请输入街')
    door=input('门牌号')

    while True:
        gift=bank_add(card_id,password,name,country,province,street,door) #传参

        if gift == 1:
            print('成功,您的账户信息为：')
            info = '''
                                ----------中国工商银行-------------
                                        1、账号：%s
                                        2、密码：%s
                                        3、姓名：%s
                                        4、国家：%s
                                        5、省份：%s
                                        6、街道：%s
                                        7、门牌号：%s
                                        8、卡余额：%s
                                ----------------------------------        
    
                    '''
            print(info % (card_id, password, name, country, province, street, door,0))
            break

        elif gift == 2:
            print('用户已存在请重新开户')
            break




        elif gift == 3:
            print('用户已满')
            break






def bank_add(card_id,password,name,country,province,street,door):       #添加数据
    sql='select idcard from mes where idcard=%s'
    param=[card_id]
    data=select(sql,param,mode='all')
    sql1='select count(*) from mes'
    param=[]
    data1=select(sql1,param,mode='all')

    if len(data)>0:                                             #判断id是否重复
        return 2

    elif data1[0][0]>=100:                                                #判断是否满库
        return 3
    else:                                                               #插入数据
        sql2='insert into mes values(%s,%s,%s,%s,%s,%s,%s,%s)'
        param=[card_id,password,name,country,province,street,door,0]
        update(sql2,param)
        return 1



def putmoney():
    card_id=card__id()
    cash=ca_sh()
    while True:
        gift2= money_add(card_id,cash)
        if gift2==True:
            sql6='select money from mes where idcard=%s'
            param6=[card_id]
            data6=select(sql6,param6,mode='all')
            print('存入成功，您的余额为：',data6[0][0])
            break
        elif gift2==False:
            print('账户不存在')
            card_id = card__id()

def money_add(card_id,cash):
    sql4='select count(*) from mes where idcard=%s'
    param4=[card_id]
    data4=select(sql4,param4,mode='all')
    if data4[0][0]>0:
        sql5='update mes  set money = money + %s  where idcard=%s'
        param5=[cash,card_id]
        update(sql5,param5)
        return True
    else:
        return False

def takemoney():
    card_id = card__id()
    password=pass_word()

    gift3=take_money(card_id,password)
    if gift3==1:
        print('账户不存在')
    elif gift3==2:
        print('密码错误')
    elif gift3==0:
        print('请输入要取的金额')
        cash=ca_sh()
        gift4=_money(card_id,cash)
        if gift4==0:
            print('取款成功')
        elif gift4==3:
            print('余额不足取款失败')


def take_money(card_id,password):
    sql7='select *from mes where idcard=%s and password1=%s '
    param7=[card_id,password]
    data7=select (sql7,param7,mode='all')
    sql8 = 'select password1 from mes where idcard=%s  '
    param8 = [card_id]
    data8 = select(sql8, param8, mode='all')
    sql21='select * from mes where idcard=%s'
    param21=[card_id]
    data21=select(sql21,param21,mode='all')
    # print(len(data21))
    if len(data7)>0:


        return 0
    elif len(data21)==0:
        return 1
    elif data8[0][0]!=password:
        return 2

def _money(card_id,cash):
    sql9='select money from mes where idcard=%s'
    param9=[card_id]
    data9=select (sql9,param9,mode='all')
    if cash<data9[0][0]:
        sql10='update mes set money = money-%s where idcard=%s'
        param10=[cash,card_id]
        update(sql10,param10)
        sql11 = 'select money from mes  where idcard=%s'
        param11 = [card_id]
        data11=select(sql11, param11)
        print('您的卡余额为：',data11[0][0])

        return 0
    else:
        return 3

def transmoney():
    print('请输入转出账户')
    card_id = card__id()
    id=card_id
    print('请输入转入账户')
    card_id = card__id()

    password = pass_word()

    # print(id,card_id)

    print('请输入要取的金额')
    cash = ca_sh()
    gift5=trans_money(id,card_id,password,cash)
    if gift5==1:
        print('账号错误')
    elif gift5==2:
        print('密码错误')
    elif gift5==3:
        print('余额不足')
    elif gift5==0:
        sql16='update mes set money = money-%s where idcard=%s'
        param16=[cash,id]
        update(sql16,param16)

        sql17 = 'update mes set money = money+%s where idcard=%s'
        param17 = [cash,card_id ]
        update(sql17, param17)

        sql18='select money from mes where idcard=%s'
        param18=[id]
        data18=select(sql18,param18,mode='all')


        print('转账成功,您的余额为：',data18[0][0])

def trans_money (id,card_id,password,cash):
    sql12='select * from mes where idcard=%s '              #转出
    param12=[id]
    data12=select (sql12,param12)

    sql13 = 'select * from mes where idcard=%s '            #转入
    param13 = [card_id ]
    data13 = select(sql13, param13)

    sql14 = 'select password1 from mes where idcard=%s '    #转出密码
    param14 = [id]
    data14 = select(sql14, param14)

    if len(data12)==0 or len(data13)==0:
        return 1
    if  data12[0][0]>0 and data13[0][0]>0 and data14[0][0]==password:
        sql15='select money from mes where idcard=%s'
        param15=[id]
        data15=select(sql15,param15,mode='all')
        if cash<data15[0][0]:
            return 0
        else:
            return 3
    elif data12[0][0]>0 and data13[0][0]>0 and data14[0][0]!=password:
        return 2

def check():
    card_id = card__id()
    password = pass_word()
    gift6=_check(card_id,password)
    if gift6==0:
        print('账号不存在')
    elif gift6==1:
        print('密码错误')
    elif gift6==2:
        sql20='select *from mes where idcard=%s'
        param20=[card_id]
        data20=select(sql20,param20,mode='all')

        print('您的账户信息为：')

        info = '''
                           ----------中国工商银行-------------
                                   1、账号：%s
                                   2、密码：%s
                                   3、姓名：%s
                                   4、国家：%s
                                   5、省份：%s
                                   6、街道：%s
                                   7、门牌号：%s
                                   8、卡余额：%s
                           ----------------------------------

               '''
        print(info % (data20[0][0],data20[0][1],data20[0][2],data20[0][3],data20[0][4],data20[0][5],data20[0][6],data20[0][7]))

def _check(card_id,password):
    sql19='select password1 from mes where idcard=%s'
    param19=[card_id]
    data19=select(sql19,param19,mode='all')

    if len(data19[0][0])>0 :
        if  data19[0][0]==password:
            return 2
        else:
            return 1
    else:
        return 0




# #密码格式验证模块
def pass_word():
    loop='loop'
    while loop=='loop':
        password = input('请输入您的密码')
        if password.isdigit() and len(password) == 6:
            loop=111
            return password

        else:
            print('密码格式错误请重新输入')


# #账户格式验证模块
def card__id():
    loop = 'loop'
    while loop == 'loop':
        card_id = input('请输入账号')
        if card_id.isdigit and len(card_id) == 8:
            card_id = int(card_id)
            loop=111
            return card_id
        else:
            print('账号格式错误请重新输入')

##金额格式验证模块
def ca_sh():
    loop = 'loop'
    while loop == 'loop':
        cash = input('金额:')
        if cash.isdigit:
            cash=int(cash)
            loop=111
            return cash
        else:
            print('金额格式错误请重新输入')






while True:

    cc=input('请选择服务项目')
    if cc=='1':
        print('1.开户')
        useradd()

    if cc=='2':
        print('2.存钱')
        putmoney()

    if cc=='3':
        print('3.取钱')
        takemoney()

    if cc=='4':
        print('4.转账')
        transmoney()

    if cc=='5':
        print('5.查询')
        check()

    if cc=='6':
        print('退出')
        break

