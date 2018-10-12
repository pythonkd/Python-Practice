P=input()
for i in range (len(P)):
    c=ord(P[i])
    if c==120:
        c=97
        x=chr(c)
        P=P[:i]+x+P[i+1:]
    elif c==121:
        c=98
        x=chr(c)
        P=P[:i]+x+P[i+1:]
    elif c==122:
        c=99
        x=chr(c)
        P=P[:i]+x+P[i+1:]
    elif c==32:
        x=chr(c)
        P=P[:i]+x+P[i+1:]
    else:
        c=c+3
        x=chr(c)
        P=P[:i]+x+P[i+1:]
print(P)
