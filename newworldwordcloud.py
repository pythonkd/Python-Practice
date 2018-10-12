import wordcloud
import jieba
fo= open("D:\z\新时代报告.txt","r",encoding="utf-8")
t=fo.read()
fo.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud( font_path="msyh.ttc",\
    width=1000,height=700,background_color="white",max_words=15)
w.generate(txt)
w.to_file("grwordcloud.png")
