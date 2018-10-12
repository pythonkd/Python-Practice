import requests
import re
def gettext(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def parserpage(infolist,html):
    try:
        raw_title=re.findall(r'\"raw_title\"\:\".*?\"',html)
        view_price=re.findall(r'\"view_price\"\:\"[\d.]*\"',html)
        view_fee=re.findall(r'\"view_fee\"\:\"[\d.]*\"',html)
        item_loc=re.findall(r'\"item_loc\"\:\".*?\"',html)
        for i in range(len(raw_title)):
            title=(raw_title[i]).split(":")[1]
            price=(view_price[i]).split(":")[1]
            postage=(view_fee[i]).split(":")[1]
            local=(item_loc[i]).split(":")[1]
            infolist.append([title,price,postage,local])
    except:
        return ""
def printgooslist(infolist):
    tplt="{:*^4}\t{:*^25}\t{:*^25}\t{:*^4}\t{:*>16}"
    print(tplt.format("序号","标题","价格","邮费","产地"))
    count=0
    for i in infolist:
        count+=1
        print(tplt.format(count,i[0],i[1],i[2],i[3]))
def main():
    url="https://s.taobao.com/search?q=%E6%B0%B4%E6%9D%AF&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
    infolist=[]
    try:
        html=gettext(url)
        parserpage(infolist,html)
        printgooslist(infolist)
    except:
        print("程序有误")
main()
    
