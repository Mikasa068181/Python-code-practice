while True:
    s = input("请输入字符串(按q退出):")
    if s == "q":
        break
    op = input("你想转大写还是小写？").strip()
    if op == "大写":
        print(s.upper())
    elif op == "小写":
        print(s.lower())
    else:
        print("请输入大写或小写!")


