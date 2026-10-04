import random

def make_secret():
    return random.randint(1,100)

def check_guess(guess,secret):
    if guess==secret:
        return "correct"
    elif guess>secret:
        return "太大了"
    else:
        return "太小了"

def play():
    secret=make_secret()
    print("我想到了一个1到100的数字，你来猜猜看,你有7次机会")
    times=0
    while times<7:
        guess=int(input("你猜猜是几？还有"+str(7-times)+"次机会"))
        times=times+1
        result=check_guess(guess,secret)
        if result =="correct":
            print("恭喜你猜对了！，用了",times,"次机会")
            return
        else:print(result)
    print("7次机会用完啦，答案是",secret)

while True:
    play()
    again=input("还要再来一局吗？输入y继续，其他退出")
    if again !="y":
        print("再见")
        break
