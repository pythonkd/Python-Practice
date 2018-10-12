def allnum():
    n=1
    while True:
        yield n
        n=n+1
        if n>1200:
            break
def revert(n):
    l=str(n)
    return l[::-1]== l

def is_palindrome():
    it=allnum()
    it=filter(revert,it)
    while True:
        n=next(it)
        yield n
t=[]
for i in is_palindrome():
    if i<1200:
        t.append(i)
    else:
        break
print(t)
