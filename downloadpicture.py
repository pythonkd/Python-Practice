import requests
def getpicture(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.content
    except:
        return ""
def downpicture(content,url):
    try:
        name=(url).split("/")[-1]
        with open("D:/z/"+name,"xb") as f:
            f.write(content)
            f.close()
            print("保存成功")
    except:
        print("保存失败")
def main():
    url="http://pic1.win4000.com/wallpaper/7/57a96e741e006.jpg"
    content=getpicture(url)
    downpicture(content,url)
main()
