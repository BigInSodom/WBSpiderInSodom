import os
import time

class Markdown():
    def __init__(self):
        print(time.strftime("%Y-%m-%d", time.localtime()))
        self.md = open(time.strftime("%Y-%m-%d", time.localtime())+"eee.md","w+",encoding="utf-8")

    def md_name(self,name):
        self.md.write(name)

    # def md_id(self,id):

    # def md_space(self):

    # def md_time(self,time):

    # def md_text(self,text):

    # def md_pic(self,pic):
    #     self.md.write("![1]("+pic+")")

    # def md_vid(self,vid):
    #     self.md.write("<video src=\""+vid+" width=\"100%\" height=\"100%\" controls=\"controls\"></video>")

md = open("zzz.txt","a",encoding="utf-8")
md.write("zzz")
#md=Markdown()
#md.md_name("nnzzzzzzzzzzzzz")

# x = time.strftime("%Y-%m-%d", time.localtime())
# #print(x.type)
# f = open(x+".md","a",encoding="utf-8")
# f.write("demo\n")
# f.write("test")
# f.close()