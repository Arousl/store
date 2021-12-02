import xlrd
import xlwt
import re
import numpy as np
# 1.	统计和分析以下问题数据：
# a)	统计所有表格中有多少人
# b)	统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
# c)	总公司男女人数
# d)	年龄超过45岁的老员工人数
# e)	薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
# f)	统计去传媒公司的工作的人员数量
# g)	统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）


xl=xlrd.open_workbook(filename=r"百度合作单位-人员管理-二期.xls",encoding_override=True)
st=xl.sheet_by_index(0)
row=st.nrows
col=st.ncols
# a)	统计所有表格中有多少人
# print('表中一共有：',row-1,'人')

# b)	统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
phon=st.col_values(5,1)
dx = 0
yd = 0
lt = 0
for nn in phon:
    cc=nn[:2]

    if cc=='14' or cc=='17':
        dx+=1
    elif cc=='13':
        yd+=1
    elif cc=='15':
        lt+=1

print('电信用户为%d,移动%d, 联通%d'%(dx,yd,lt))

# c)	总公司男女人数
sex=st.col_values(8,1)
man=0
woman=0
for xb in sex:
    if xb=='男':
        man+=1
    elif xb=='女':
        woman+=1
print('男有%d人,女有%d人'%(man,woman))

# d)	年龄超过45岁的老员工人数
age=st.col_values(7,1)
a_ge=0
for ag_e in age:
    if ag_e>45:
        a_ge+=1
print('超过45岁的有%d人'%a_ge)

# e)	薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
money=st.col_values(11,1)
high=0
low=0
for mon_ey in money:
    if mon_ey>8000:
        high+=1
    elif mon_ey<3000:
        low+=1
print('高工资为%d人,低工资为%d人'%(high,low))

# f)	统计去传媒公司的工作的人员数量
person=st.col_values(13,1)
pop=0
for per_son in person:
    if '传媒' in per_son:
        pop+=1
print('传媒公司有%d人'%pop)

# g)	统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）
adress=st.col_values(9,1)
pp=0
for ad_ress in adress:
    if '黑龙江' in ad_ress or '北京' in ad_ress or '福建' in ad_ress or '四川' in ad_ress:
        pp+=1
print('高位地区为%d人'%pp)
