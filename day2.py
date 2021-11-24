import random
i=0
scr = 5000
print('初始金额5000')
while i < 15:
    gust = random.randint(1,20)
    unm = int(input('猜猜看'))
    if unm > gust:
         i += 1
         scr -= 100
         print('大了，您还有',15-i,'次机会','剩余分数',scr)
    elif unm < gust:
         i += 1
         scr -= 100
         print('小了,您还有',15-i,'次机会','剩余分数',scr)
    else :
         scr += 300
         print('恭喜答对','您还有',15-i,'次机会','剩余分数',scr)





