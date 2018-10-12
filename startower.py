N=int(eval(input()))
T="*"
for i in range(int((N-1)/2+1)):
    t=T*(2*i+1)
    t=t.center(N)
    print("{}".format(t))
