sum=0
for i in range(2,100):
    for j in range(2,3):
        if i%j==0:
            break
        else:
            print(i)
            sum=sum+i
