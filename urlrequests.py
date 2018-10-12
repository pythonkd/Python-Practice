import os
import requests
url="http://cn-hbxy-cmcc-v-02.acgvideo.com/upgcxcode/10/99/37619910/37619910-1-64.flv?expires=1531584000&platform=pc&ssig=g2YZi7nf13-wHTN39dgunQ&oi=1880743781&nfa=BpfiWF+i4mNW8KzjZFHzBQ==&dynamic=1&hfa=2037981606&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=56b866b0f2f644408a6abbc0e958acdb&nfc=1"
root='D:/z/'
if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(root+'tt.flv'):
    r=requests.get(url)
    f=open(root+'tt.flv','wb')
    f.write(r.content)
    f.close()
