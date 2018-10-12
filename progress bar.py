import time
print("--------开始--------")
x=10
for i in range(x+1):
    a="*"*i
    b="-"*(x-i)
    c=(i/x)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(1)

print("--------结束--------")
