import random
rnum=random.randint(1,100)
i=0
while True:
    num=input('请输入你猜的数:')
    try:
        num=int(num)
    except:
        print('请输入数字！')
        continue
    i+=1
    if num==rnum:
        print(f'猜对了，一共猜了{i}次')
        break
    elif num<rnum:
        print('猜小了再来')
        continue
    elif num>rnum:
        print('猜大了再来')
        continue