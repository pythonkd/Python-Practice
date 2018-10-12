account="Kate"
password="666666"
j=0
for i in range (3):
    x=input("请输出帐户名")
    y=input("请输入密码")
    if x==account and y==password:
        print("登录成功！")
        break
    else:
        j=j+1
        if j==3:
            print("3次用户名或者密码均有误！退出程序。")
        else:
            
        print("用户名或者密码错误！")
