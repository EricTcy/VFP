import requests
import re
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox
import webbrowser

url = 'http://www.qmaile.com/'
req = requests.get(url)
#req.encoding='utf-8'
req.encoding = req.apparent_encoding
reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg,req.text)

#print(req.text)
#print(res)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]


root = tk.Tk()
#root.geometry('620x320')
root.title('屯村播放器3.0版  by屯村Eric')
root.resizable(0, 0)

frame_bofang =tk.LabelFrame(root)

frame_bofang.grid(column=0, row=0, sticky=tk.W)

var = tk.StringVar()
var.set(1)
#var = tk.IntVar()
r1 = tk.Radiobutton(frame_bofang, text='屯村影院',  variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(frame_bofang, text='巴厘岛影院',  variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(frame_bofang, text='香港影院',  variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(frame_bofang, text='好来舞影院',  variable=var, value=four)
r4.grid(row=3, column=1)

frame_bofang2 =tk.LabelFrame(root,text="网址链接",fg='blue')
frame_bofang2.grid(column=1, row=0)

e1 = tk.Entry(frame_bofang2,text='', width=50)
e1.grid(row=1, column=1, sticky=tk.W)

def bf():
    webbrowser.open(var.get()+ e1.get())

b1 = tk.Button(frame_bofang2,fg='green', text='播放',font=12,width=8,command=bf)
b1.grid(row=2, column=1)

def qc():
    e1.delete(0, 'end')

b2=tk.Button(frame_bofang2,text='清除',font=12,width=8,command=qc)
b2.grid(row=3, column=1)

def _quit():
    root.quit()
    root.destroy()
    exit()


# Creating a Menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)



def _msgBox4():
    mBox.showinfo("致敬逆行者，武汉挺住，中国必胜",
                           "先选定左边其中的一个影院，如果播放不了，再选另一个影院\n"
                           "再把电影电视剧的网址粘贴到网址链接的空白输入框里\n"
                           "最后点播放\n"
                           "必须要把谷歌chrome设为默认浏览器\n"
                           "\n"
                           "疫情期间，尽量不出门,出门一定要戴口罩"
                          )



msgMenu = Menu(menuBar, tearoff=0)

msgMenu.add_command(label="使用说明", command=_msgBox4)
menuBar.add_cascade(label="帮助", menu=msgMenu)

root.iconbitmap(r'h:\py\vip28\t.ico')

root.mainloop()




