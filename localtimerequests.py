import time
i=1
while i!=0:
    print(time.strftime("%Y-%m-%d-%A %H:%M:%S",time.localtime())+"\r",end="")
    time.sleep(0.1)
    
