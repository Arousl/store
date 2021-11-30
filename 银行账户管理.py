import random

#建立信息库
l1=['0','1','2','3','4','5','6','7','8','9']

message={'91507824':{'密码':123456,'姓名':'小明','余额':666,'银行':'工商银行昌平支行','地址':{'中国':{'河北省':{'小鸟街':{'门牌号':'610'}},'黑龙江省':{'凑数的':'无'}},'美国':{'没有':'无'} }},
        '92507824':{'密码':123456,'姓名':'小红','余额':666,'银行':'工商银行昌平支行','地址':{'中国':{'河北省':{'小鸟街':{'门牌号':'610'}},'黑龙江省':{'凑数的':'无'}},'美国':{'没有':'无'} }},
        '81507824':{'密码':123456,'姓名':'小刚','余额':666,'银行':'工商银行昌平支行','地址':{'中国':{'河北省':{'小鸟街':{'门牌号':'610'}},'黑龙江省':{'凑数的':'无'}},'美国':{'没有':'无'} }}



        }
dd={'中国':{'北京':{'昌平街':{'门牌号':'110'},'海淀街':'无'},'河北省':'无','黑龙江省':'无','山东省':'无'},'美国':'无','日本':'无','加拿大':'无'}
# 余额位置 messge['账号']['余额']

while True:       #整体循环
      # 打印菜单
      print('*******************************\n'
            '*       中国工商银行            *\n'
            '*       账户管理系统            *\n'
            '*          V1.0               *\n'
            '*******************************\n'
            '*                              *\n'
            '*                              *\n'
            '*1.开户                        *\n'
            '*2.存钱                        *\n'
            '*3.取钱                        *\n'
            '*4.转账                        *\n'
            '*5.查询                        *\n'
            '*6.退出                        *\n'
            '******************************\n')
      loop = 1                      #外循环开关
      cc=input()
      if cc == '1':
            #开户模块
            while True:      #循环注册账号
                  ip = random.sample(l1, 8)           #随机生成账号
                  ip = "".join(ip)
                  print('您生成的账号为',ip)
                  print('正在检查您的账号是否可用...')
                  if ip in message:
                        print('该用户已存在请重新生成')
                        continue
                  else:
                        if len(message)>99:
                              print('用户已满')
                              break
                        else:
                              print('创建成功，请填写信息')
                              while True:             #密码循环体
                                    pw=input('请输入密码：6位')
                                    if pw.isdigit():
                                          if len(pw)>6 or len(pw)<6:
                                                print('长度错误重新输入')
                                                continue
                                          else:
                                                print('恭喜密码设置成功')
                                                break
                                    else:
                                          print('格式错误重新输入')
                              name = input('请输入名字')
                              while True:
                                    address = input('请输入地址——国家')
                                    if address in dd:
                                          d1 = input('请输入地址——省份')
                                          if d1 in dd[address]:
                                                d2 = input('请输入地址——街道')
                                                if d2 in dd[address][d1]:
                                                      d3 = input('请输入地址——门牌号')
                                                      break
                                                else:
                                                      print('输入错误')
                                          else:
                                                print('输入错误')
                                    else:
                                          print('输入错误')
                        pw = int(pw)

                        message.update({ip: {'密码': pw, '姓名': name, '余额': 0, '银行': '工商银行昌平支行',
                                                         '地址': {address: {d1: {d2: {'门牌号': d3}}}}}})
                        print('您的注册信息为：账号',ip,message[ip])
                  break






      elif cc =='2':
            #存钱模块

            while loop==1:
                  ip2=input('请输入您的卡号')
                  if ip2 in message:
                        cash=message[ip2]['余额']
                        print('卡余额为：',cash)
                        while True:
                              m2=input('请输入存入额度')
                              if m2.isdigit():
                                    m2=int(m2)
                                    c=cash+m2
                                    message[ip2]['余额']=c
                                    print('您卡余额为：', c)
                                    loop=2
                                    break

                              else:
                                    print('输入金额错误')

                  else:
                        print('卡号错误请重新输入')




      elif cc=='3':
            #取钱模块
            while loop==1:
                ip2=input('请输入卡号')
                print('正在检查卡号')
                if ip2 in message:
                      pw=input('请输入密码')
                      print('正在检查密码')
                      if pw.isdigit():
                         pw=int(pw)
                         if pw== message[ip2]['密码']:
                              cash = message[ip2]['余额']
                              print('您的余额为：', cash)
                              while True:
                                  u=input('请输入要取的金额')
                                  if u.isdigit():
                                        u=int(u)
                                        if cash+1>u:
                                          message[ip2]['余额'] = (cash-u)
                                          print('取钱成功,您的余额为：',cash-u)
                                          loop=2
                                          break
                                        else:
                                              print('余额不足')

                                  else:
                                       print('金额输入错误，请重新输入')
                         else:
                            print('密码错误')
                      else:
                            print('输入格式错误')
                else:
                      print('卡号错误')




      elif cc =='4':
            #转账模块
            while loop==1:
                  ip2=input('请输入转出卡号')
                  ip3=input('请输入转入卡号')
                  if ip2 in message and ip3 in message:
                        while loop==1:
                              pw=input('请输入转出账号密码')
                              if pw.isdigit():
                                    pw=int(pw)
                                    if pw==message[ip2]['密码']:
                                          cash = message[ip2]['余额']
                                          print('您的余额为：', cash)
                                          while True:
                                                u=input('请输入您要转出的金额')
                                                if u.isdigit():
                                                      u=int(u)
                                                      if cash+1>u:
                                                            cash2=message[ip3]['余额']
                                                            message[ip3]['余额']=cash2+u
                                                            message[ip2]['余额'] = (cash - u)
                                                            print('转账成功,您的余额为：', cash - u)
                                                            loop=2
                                                            break


                                                      else:
                                                            print('余额不足')
                                                else:
                                                      print('金额输入格式错误')
                                    else:
                                          print('密码错误请重新输入')
                              else:
                                    print('密码格式错误')
                  else:
                        print('转入或转出账号输入错误')

      elif cc=='5':
            #查询模块
            while loop==1:
                  ip2=input('请输入要查询的卡号')
                  if ip2 in message:
                        while True:
                              pw=input('请输入密码')
                              if pw.isdigit():
                                    pw=int(pw)
                                    if pw==message[ip2]['密码']:
                                          print('正在打印您的信息')
                                          print('您的信息为：卡号：',ip2,message[ip2])
                                          loop=2
                                          break
                                    else:
                                          print('密码错误')
                              else:
                                    print('密码格式错误')
                  else:
                        print('卡号不存在请重新输入')

      elif cc=='6':
            #退出程序
            print('成功退出程序')
            break

      else:
            print('输入错误')


