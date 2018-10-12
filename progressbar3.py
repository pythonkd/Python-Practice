import time
scale=50
print("执行开始".center(50//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a=(i/scale)*100
    b="*"*i
    c="."*(scale-i)
    d=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}秒".format(a,b,c,d),end="")
    time.sleep(0.1)
    
print("执行结束".center(50//2,"-"))
