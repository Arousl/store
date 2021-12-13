import random
from BDmysql import select


class Tools:

    ##随机数
    def random(self):
        card_id = random.randint(10000000, 99999999)
        return card_id


    # #密码格式验证模块
    def pass_word(self):
        loop = 'loop'
        while loop == 'loop':
            password = input('请输入您的密码')
            if password.isdigit() and len(password) == 6:
                loop = 111
                return password

            else:
                print('密码格式错误请重新输入')


        # #账户格式验证模块
    def card__id(self):
        loop = 'loop'
        while loop == 'loop':
            card_id = input('请输入账号')
            if card_id.isdigit and len(card_id) == 8:
                card_id = int(card_id)
                loop = 111
                return card_id
            else:
                print('账号格式错误请重新输入')


        ##金额格式验证模块
    def ca_sh(self):
        loop = 'loop'
        while loop == 'loop':
            cash = input('金额:')
            if cash.isdigit:
                cash = int(cash)
                loop = 111
                return cash
            else:
                print('金额格式错误请重新输入')

         ##验证菜单输入
    def ckci(self):
        while True:
            ci = input('请输入操作')
            if len(ci)==0:
                print('输入为空')
            elif ci.isdigit():
                if ci== '1':
                    return 1
                elif ci == '2':
                    return 2
                elif ci == '3':
                    return 3
                elif ci == '4':
                    return 4
                elif ci == '5':
                    return 5
                elif ci == '6':
                    return 6
                else:
                    print('输入有误')
            else:
                print('输入非法')


        ##验证账户模块
    def ckid(self,card_id):
        sql = 'select idcard from mes where idcard=%s'
        param = [card_id]
        data = select(sql, param, mode='all')
        sql1 = 'select count(*) from mes'
        param = []
        data1 = select(sql1, param, mode='all')
        if len(data) > 0:  # 判断id是否重复/判断是否存在该账户
            return 2   #存在重复/账户存在

        elif data1[0][0] >= 100:  # 判断是否满库
            return 3
        else:
            return 1    #正常



        ##验证密码模块
    def ckpw(self,card_id, password):
        sql7 = 'select *from mes where idcard=%s and password1=%s '
        param7 = [card_id, password]
        data7 = select(sql7, param7, mode='all')
        sql8 = 'select password1 from mes where idcard=%s  '
        param8 = [card_id]
        data8 = select(sql8, param8, mode='all')
        sql21 = 'select * from mes where idcard=%s'
        param21 = [card_id]
        data21 = select(sql21, param21, mode='all')

        if len(data7) > 0:  #密码账号正确

            return 0
        elif len(data21) == 0:  #账户为空
            return 1
        elif data8[0][0] != password:   #密码错误
            return 2


    def ckmoy(self,card_id,cash):
        sql9 = 'select money from mes where idcard=%s'
        param9 = [card_id]
        data9 = select(sql9, param9, mode='all')
        if cash < data9[0][0]:
            return 1
        else:
            print('余额不足')
            return 0


    def out(self):
        print('恭喜退出')