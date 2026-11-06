while True:
    num1 = input("请输入第一个数（按q退出）:")
    if num1 == "q":
        break
    try:
        num1 = float(num1)
    except:
        print('不是有效数字，请重新输入！')
        continue
    num2 = input("请输入第二个数:")
    try:
        num2 = float(num2)
    except:
        print('不是有效数字，请重新输入！')
        continue
    char = input("请输入运算符:")
    if char=='+':
        print(num1 + num2)
    elif char=='*':
        print(num1 * num2)
    elif char=='/':
        if num2==0:
            print('除数不能为0')
            continue
        print(num1 / num2)
    elif char=='-':
        print(num1 - num2)
    else:
        print('请输入运算符！')


