
from user import User
from tools import Tools
from window import Window
from bank import Bank
user1 = User()
window =Window()


class Operate:

    def cin(self):

        cc=Tools().ckci()
        # print(cc)
        if cc==1:
            self.add()
        elif cc==2:
            self.put()
        elif cc==3:
            self.take()
        elif cc==4:
            self.trans()
        elif cc==5:
            self.chk()
        elif cc==6:
            print('成功退出')
            return 6



    def add(self):

        loop=0
        while loop ==0:
            card_id=Tools().random()
            password=Tools().pass_word()
            name = input('请输入姓名')
            country = input('请输入国家')
            province = input('请输入省')
            street = input('请输入街')
            door = input('门牌号')
            user1.set_mes(card_id,password,name,country,province,street,door)
            con=Tools().ckid(card_id)

            if con == 2:
                print('卡号已存在')
                return 0
            elif con == 3:
                print('账户已满')
                return 0
            elif con == 1:
                Bank().add_mes(card_id,password,name,country,province,street,door)
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
                print(info % (user1.get_card(), user1.get_password(), user1.get_name(), user1.get_country(),
                              user1.get_province(), user1.get_street(), user1.get_door(), 0))
                break










    def put(self):
        while True:
            id_card=Tools().card__id()
            cash=Tools().ca_sh()
            con=Tools().ckid(id_card)
            if con ==2:
                Bank().add_money(cash,id_card)
                Bank().chk_money(id_card)
                break
            else:
                print('用户不存在')




    def take(self):
        while True:
            id_card = Tools().card__id()
            password= Tools().pass_word()
            con=Tools().ckpw(id_card, password)
            if con==1:
                print('账户为空')
                continue
            elif con==2:
                print('密码错误')
                continue
            elif con==0:
                cash=Tools().ca_sh()
                son=Tools().ckmoy(id_card,cash)
                if son ==0:
                    continue
                elif son ==1:
                    Bank().tak_moy(id_card,cash)
                    break







    def trans(self):
        while True:
            print('请输入转出账户')
            id_card_out = Tools().card__id()
            print('请输入转入账户')
            id_card_in =  Tools().card__id()
            con=Tools().ckid(id_card_out)
            son=Tools().ckid( id_card_in)
            if con ==2 and son ==2:
                password = Tools().pass_word()
                pon=Tools().ckpw(id_card_out,password)
                if pon==0:
                    cash=Tools().ca_sh()
                    ccc=Tools().ckmoy(id_card_out,cash)
                    if ccc==1:
                        Bank().add_money(cash,id_card_in)
                        Bank().tak_moy(id_card_out,cash)
                        break
                    else:
                        print('余额不足')

                else:
                    print('密码错误')

            else:
                print('账户不存在')


    def chk(self):
        while True:
            id_card = Tools().card__id()
            password = Tools().pass_word()
            con = Tools().ckpw(id_card, password)
            if con == 1:
                print('账户为空')
                continue
            elif con == 2:
                print('密码错误')
                continue
            elif con == 0:
                Bank().tak_mes(id_card)
                break















