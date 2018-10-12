from functools import reduce
def str2float(s):
    a=reduce(num2int,map(char2num,s.split('.')[0]))
    b=int2float(reduce(num2int,map(char2num,s.split('.')[1])),len(s.split('.')[1]))
    return a+b
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
def num2int(x,y):
    return x*10+y
def int2float(s,n):
    return s*pow(10,-n)
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
