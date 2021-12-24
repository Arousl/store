from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.action_chains import ActionChains #滑块包
#-----------------------------弹框----------------------------------------------
# web=webdriver.Chrome()
# web.get(r"D:\PYthon\pythonproject\day15 网页自动化\弹框的验证\dialogs.html")
# web.maximize_window()
# try:
#     web.find_element_by_id('alert').click()
#     web.switch_to.alert.accept()
# except:
#     print('定位失败')
#
# time.sleep(3)
# web.quit()
#-----------------------------跳转页面------------------------------------------
# web1=webdriver.Chrome()
# web1.get(r'D:\PYthon\pythonproject\day15 网页自动化\跳转页面\pop.html')
# try:
#     web1.find_element_by_id('goo').click()
#     count=web1.window_handles
#     web1.switch_to.window(count[-1])
#     web1.find_element_by_id('kw').send_keys('python')
#     web1.find_element_by_id('su').click()
# except:
#     print('跳转失败')
# time.sleep(3)
# web1.quit()

#-----------------------------滑块-----------------------------------------------
# web2=webdriver.Chrome()
# web2.get(r'D:\PYthon\pythonproject\day15 网页自动化\滑动验证\mousedrag.html')
# try:
#     lp = web2.find_element(By.XPATH,'/html/body/div/div[3]')     # lp=web2.find_element_by_xpath('/html/body/div/div[3]')
#     ac=ActionChains(web2)               #把driver交给事件链执行
#     # ac.click_and_hold(lp).move_by_offset(300,0).perform()
#     ac.drag_and_drop_by_offset(lp, 248, 0).perform()
# except:
#     print('滑块定位失败')
#     web2.save_screenshot("erro.png")
# time.sleep(3)
# web2.quit()

#-----------------------------上传-----------------------------------------------
# web3=webdriver.Chrome()
# web3.get(r'D:\PYthon\pythonproject\day15 网页自动化\上传文件和下拉列表\autotest.html')
# try:
#     web3.find_element(By.ID,'accountID').send_keys('123456')        #id
#     web3.find_element(By.ID,'passwordID').send_keys('123')          #pwd
#     web3.find_element(By.ID,'areaID').send_keys('天')                #下拉列表
#     web3.find_element(By.XPATH, '/html/body/form/table/tbody/tr[5]/td/input[2]').click()   #多选
#     web3.find_element(By.XPATH, '/html/body/form/table/tbody/tr[5]/td/input[3]').click()   #多选
#     web3.find_element(By.NAME, 'file').send_keys('D:\\PYthon\\pythonproject\\day15 网页自动化\\上传文件和下拉列表\\autotest.html')   #上传
#     web3.find_element(By.ID, 'buttonID').click()
#
#
# except:
#     print('定位错误')
# time.sleep(3)
# web3.quit()


#-----------------------------苏宁作业-----------------------------------------------
# web4=webdriver.Chrome()
# web4.get('https://www.suning.com/')
#
# web4.find_element(By.ID,'searchKeywords').send_keys('PS4')
# web4.find_element(By.ID,'searchSubmit').click()
# web4.find_element(By.CLASS_NAME,'brand-name').click()

                                    # 右侧快捷购物
# try:
#     web4.find_element(By.XPATH,'/html/body/div[10]/div/ul/li[3]/div/div/div[3]/a[3]').click()
#     web4.find_element(By.CLASS_NAME, 'tab-cart-tip').click()
#     web4.find_element(By.NAME, 'public0_none_cblnew_gouwuche_gotogwc').click()
# except:
#     print('错误')

#                                     # 常规流程购物
# try:
#     web4.find_element(By.NAME,'ssdsn_search_pro_name03-1_0_0_12119524903_0071051333').click()                      #进入店面
#     web4.switch_to.window(web4.window_handles[-1])                                                                  #跳转页面选择
#     web4.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div[12]/dl[1]/dd/ul/li[9]/a/span').click()          #选择购买的品类
#     web4.find_element(By.ID,'addCart').click()                                                                       #加入购物车
#     web4.find_element(By.NAME,'cart1_go').click()                                                                   #弹框确定进入结算
#     web4.find_element(By.NAME,'icart1_ope_buy01').click()                                                           #结算金额
# except:
#     print('错误')
#
#
# time.sleep(3)
# web4.quit()

#-----------------------------国美作业-----------------------------------------------
web5=webdriver.Chrome()
web5.get('https://www.gome.com.cn/')
ac=ActionChains(web5)
ms=web5.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div/ul/li[4]/h3/a[1]')
ac.move_to_element(ms).perform()
web5.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/div/div[2]/div/div[4]/div[1]/div[2]/div[1]/ul/div[2]/a[14]').click()
time.sleep(3)
web5.quit()






