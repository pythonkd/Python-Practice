L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    print(t)
    return t
def by_score(t):
    s=(t[1],t[0])
    return s
L2 = sorted(L, key=by_score)
print(L2)
