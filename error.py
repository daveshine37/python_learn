try:
    num=int(input("请输入一个数字"))
    print("你输入的数字是：",num)
except ValueError:
    print("你刚刚输入的不是数字")