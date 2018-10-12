import  requests
wd={'ip':'202.204.80.112'}
url='https://ip.cn/index.php'
def getip(url,wd):
    try:
        r=requests.get(url,params=wd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text[300:-300]
    except:
        return '获取失败'
IP=print(getip(url,wd))
