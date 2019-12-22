import requests
import re
import tkinter as tk
import webbrowser

url = 'http://www.qmaile.com/'
responed = requests.get(url)
# responed.encoding = 'utf-8' 下一个也可以
responed.encoding = responed.apparent_encoding
# print(responed.text)

reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg,responed.text)
#print(res)

one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
#six = res[5]

root = tk.Tk() #启动窗口
root.title('andy的软件')
root.geometry('500x300') #界面大小
# root.geometry('500x250+100+100')  # 固定界面大小
l1 = tk.Label(root,text='播放接口：',font=12) #标签
l1.grid(row = 0,column = 0) #位置

var = tk.StringVar()
r1 = tk.Radiobutton(root,text='播放接口1',variable = var,value = one)
r1.grid(row = 0,column = 1)
r2 = tk.Radiobutton(root,text='播放接口2',variable = var,value = two)
r2.grid(row = 1,column = 1)
r3 = tk.Radiobutton(root,text='播放接口3',variable = var,value = three)
r3.grid(row = 2,column = 1)
r4 = tk.Radiobutton(root,text='播放接口4',variable = var,value = four)
r4.grid(row = 3,column = 1)
r5 = tk.Radiobutton(root,text='播放接口5',variable = var,value = five)
r5.grid(row = 4,column = 1)
#r6 = tk.Radiobutton(root,text='播放接口6',variable = var,value = six)
#r6.grid(row = 5,column = 1)

l2 = tk.Label(root,text='播放链接：',font=12) #标签
l2.grid(row=6,column=0)

e1 = tk.Entry(root,text='',width=45) #文本框
e1.grid(row=6,column=1)

def bf():
    print(var.get()+e1.get())
    webbrowser.open(var.get()+e1.get())

def qc():
    e1.delete(0,'end')

b1 = tk.Button(root,text='播放',font=12,width=8,command = bf)
b1.grid(row=7,column=1)
b2 = tk.Button(root,text='清除',font=12,width=8,command = qc)
b2.grid(row=8,column=1)

root .mainloop()