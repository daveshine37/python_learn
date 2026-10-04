with open("C:\\Users\\xdw20\\python_learn\\test.txt","r") as f:
    content=f.read()

print("文件内容是:")
print(content)

with open("C:\\Users\\xdw20\\python_learn\\test.txt", "r") as f:
    for line in f:
        print("读到一行：",line)
