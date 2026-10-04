scores=[85,92,77,65,54,37,81]

total=0
pass_count=0

for s in scores:
    total=total+s
    if s >= 60:
        pass_count=pass_count+1

print("全班共",len(scores),"人")
print("班级平均分为",total/len(scores),"分")
print("及格人数为",pass_count,"人")