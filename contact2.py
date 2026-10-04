import os

FILE="C:\\Users\\xdw20\\python_learn\\contacts_data.txt"

def load_contacts():
    contacts={}
    if os.path.exists(FILE):
        try:
            with open(FILE,"r") as f:
                for line in f:
                    line=line.strip()
                    if line:
                        name,phone=line.split(",")
                        contacts[name]=phone
        except Exception:
            print("文件存在问题")
    return contacts

def save_contacts(contacts):
    with open(FILE,"w") as f:
        for name,phone in contacts.items():
            f.write(name+","+phone+"\n")

def add_Contacts(contacts):
    name=input("请输入联系人的名称:")
    phone=input("请输入联系人的电话号码:")
    contacts[name]=phone
    save_contacts(contacts)
    print("已经添加",name,"啦！")

def show_contacts(contacts):
    if not contacts:
        print("主人，通讯录是空的哦")
        return
    for name,phone in contacts.items():
        print(name,"的电话是",phone)

def delete_contact(contacts):
    name=input("主人要删除谁？")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("已经删除",name)
    else:
        print("通讯录里没有",name)

def update_contact(contacts):
    name=input("要改谁的电话？")
    if name in contacts:
        new_phone=input(name+"的新电话是？")
        contacts[name]=new_phone
        save_contacts(contacts)
        print(name,"的电话号码已经更新为",new_phone)
    else:
        print("主人的通讯录里面没有",name,"哦")

def main():
    contacts=load_contacts()
    while True:
        print("\n1.查看通讯录 2.添加联系人 3.删除联系人 4.修改联系人 5.退出")
        choice=input("请主人选择(输入数字)")
        if choice=="1":
            show_contacts(contacts)
        elif choice=="2":
            add_Contacts(contacts)
        elif choice=="3":
            delete_contact(contacts)
        elif choice=="4":
            update_contact(contacts)
        elif choice=="5":
            print("主人拜拜")
            break
        else:
            print("主人我听不懂你在说什么,输入数字吧")

main()



