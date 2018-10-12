weight=input("体重(KG)")
height=input("身高(M)")
sex=input("性别")
age=eval(input("年龄"))
BMI=eval(weight)/(eval(height)**2)
print("你的BMI是{}".format(round(BMI,6)))
if sex=="男":
    tizhi=float(BMI)*1.2+age*0.23-5.4-10.8
else:
    tizhi=1.2*BMI+0.23*age-5.4
print("你的体脂率为{}".format(tizhi))
