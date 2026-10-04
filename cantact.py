cantacts={
    "小明":"18155655432",
    "小黄":"14327654908",
    "豆包":"88888888",
}
name=input("想查谁的电话，主人？")
if name in cantacts:
    print(name,"的电话是",cantacts[name])
else:
    print("好像没有记录这个人的电话")