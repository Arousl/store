from BDmysql import update
from BDmysql import select


class Bank:
    def add_mes(self,id,pwd,na,co,pro,str,dor):
        sql2 = 'insert into mes values(%s,%s,%s,%s,%s,%s,%s,%s)'
        param = [id,pwd,na,co,pro,str,dor, 0]
        update(sql2, param)


    def add_money(self,cash,card_id):
        sql5 = 'update mes  set money = money + %s  where idcard=%s'
        param5 = [cash, card_id]
        update(sql5, param5)


    def chk_money(self,card_id):
        sql6 = 'select money from mes where idcard=%s'
        param6 = [card_id]
        data6 = select(sql6, param6, mode='all')
        print('存入成功，您的余额为：', data6[0][0])


    def tak_moy(self,card_id,cash):
        sql10 = 'update mes set money = money-%s where idcard=%s'
        param10 = [cash, card_id]
        update(sql10, param10)
        sql11 = 'select money from mes  where idcard=%s'
        param11 = [card_id]
        data11 = select(sql11, param11)
        print('您的卡余额为：', data11[0][0])

    def tak_mes(self,card_id):
        sql20 = 'select idcard from mes where idcard=%s'
        param20 = [card_id]
        id = select(sql20, param20, mode='all')

        sql21 = 'select password1 from mes where idcard=%s'
        param21 = [card_id]
        pwd = select(sql21, param21, mode='all')

        sql22 = 'select name1 from mes where idcard=%s'
        param22 = [card_id]
        nam = select(sql22, param22, mode='all')

        sql23 = 'select country from mes where idcard=%s'
        param23 = [card_id]
        coy = select(sql23, param23, mode='all')

        sql24 = 'select province from mes where idcard=%s'
        param24 = [card_id]
        pro = select(sql24, param24, mode='all')

        sql25 = 'select street from mes where idcard=%s'
        param25 = [card_id]
        str = select(sql25, param25, mode='all')

        sql26 = 'select door from mes where idcard=%s'
        param26 = [card_id]
        dor = select(sql26, param26, mode='all')

        sql27 = 'select money from mes where idcard=%s'
        param27 = [card_id]
        mony = select(sql27, param27, mode='all')
        print('查询成功,您的账户信息为：')
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
        print(info % (id[0][0],pwd[0][0],nam[0][0],coy[0][0],pro[0][0],str[0][0],dor[0][0],mony[0][0]))