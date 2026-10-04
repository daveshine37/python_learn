import random
secret = random.randint(1,100)
print("我想到了了一个1到100的数字，你来猜！")

while True:
    guess = input("你猜猜是几：")
    guess = int(guess)

    if guess == secret:
        print("恭喜你,猜对了！")
        break
    elif guess > secret:
        print("太大了")
    else:
        print("太小了")