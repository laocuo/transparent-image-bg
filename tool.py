# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os
import base64
import convertor_icon
import img_bg_tool

root = Tk()
appicon = open("app.ico", "wb+")
appicon.write(base64.b64decode(convertor_icon.icon_img))
appicon.close()
root.title('一键转换文件夹下全部图片背景')
root.iconbitmap("app.ico")
root.resizable(0,0)
os.remove("app.ico")

class Application(Frame):
    """docstring for Application"""
    def __init__(self,):
        super(Application, self).__init__()
        self.createwidgets()

    def createwidgets(self):
        panel = LabelFrame(root)
        panel.pack(anchor=W, fill=X)
        self.path = StringVar()
        Label(panel, textvariable=self.path, width=50).grid(row=0, column=0, columnspan=5)
        self.path.set('图片文件夹路径')
        Button(panel, text='选择', width=10, command=self.select).grid(row=0, column=5, columnspan=1)
        Button(panel, text='转换(模式1,全部像素)', width=30, command=self.convert1).grid(row=1, column=0, columnspan=3)
        Button(panel, text='转换(模式2,外围像素)', width=30, command=self.convert2).grid(row=1, column=3, columnspan=3)

    def select(self):
        img_dir  = filedialog.askdirectory()
        if len(img_dir) > 0:
            self.path.set(img_dir)

    def convert1(self):
        self.convert(1)

    def convert2(self):
        self.convert(2)

    def convert(self, mode):
        if self.path.get() == '图片文件夹路径':
            messagebox.showerror('Error', '请选择图片文件夹')
            return
        img_bg_tool.convertor(self.path.get(), mode, 220)
        messagebox.showinfo('Info', '图片转换成功')

app = Application()
app.mainloop()
