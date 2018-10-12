import time
x=101
for i in range(x):
    print("\r{:^3}%".format(i),end="")
    time.sleep(0.1)
