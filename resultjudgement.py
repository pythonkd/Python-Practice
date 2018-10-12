try:
    0<=grade<=100
    grade=eval(input()) 
except:
    print("输入数据有误！")
else:
    if grade<0:
        print("输入数据有误！")
    elif grade>=90:
        print("输入成绩属于A级别。")
        print("祝贺你通过考试！")
    elif 80<=grade<90:
        print("输入成绩属于B级别。")
        print("祝贺你通过考试！")
    elif 70<=grade<80:
        print("输入成绩属于C级别。")
        print("祝贺你通过考试！")
    elif 60<=grade<70:
        print("输入成绩属于D级别。")
        print("祝贺你通过考试！")
    else :
        print("输入成绩属于E级别。")
finally:
    print("好好学习，天天向上！")
