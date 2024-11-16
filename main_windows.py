import tkinter
import tkinter.messagebox
from tkinter import  font
import os
import sys
import pygame
from pygame.locals import *
from random import randint
import pingtu
import Tetris
import yjwj

def setting():
    root = tkinter.Tk()#创建一个窗口
    root.title("请选择你要玩的游戏")

    root.iconbitmap('D:\ccode\python_code\lab_class\images\over.ico')#设置窗口图标

# 设置窗口的宽度和高度
    window_width = 1000
    window_height = 750

# 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

# 计算窗口放置在屏幕中央的坐标
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

# 设置窗口的大小和位置
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
#创建菜单栏，这里我们创建的是顶级菜单
    menubar = tkinter.Menu(root)
    root.config(menu=menubar)

#创建下拉菜单Game
    gamemenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='游戏',menu=gamemenu)
#创建下拉菜单Edit
    editmenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='退出',menu=editmenu)
#创建下拉菜单Help
    helpmenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='帮助',menu=helpmenu)

#创建下拉菜单About
    aboutmenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='关于',menu=aboutmenu)

#创建下拉菜单Setting
    settingmenu = tkinter.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='设置',menu=settingmenu)

#给菜单栏添加菜单
    gamemenu.add_command(label='开始游戏')
#给菜单栏添加菜单
    editmenu.add_command(label='退出',command=root.quit)
#给菜单栏添加菜单
    helpmenu.add_command(label='帮助')
    helpmenu.add_command(label='关于')
#给菜单栏添加菜单
    aboutmenu.add_command(label='关于我们')
#设置窗口背景图

    photo = tkinter.PhotoImage(file=r"D:\ccode\python_code\lab_class\images\e.png")
#
    theLabel = tkinter.Label(root,
                         justify=tkinter.LEFT,  # 左对齐
                         image=photo,  # 加入图片
                         compound=tkinter.CENTER,  # 关键:设置为背景图片
                         font=("Cooper 黑体", 40,"bold"),  # 修改字体为行楷
                         fg='white')  # 前景色
    theLabel.pack()

#在窗口中放三个按钮，分别为开始游戏，游戏设置，退出游戏
    button1 = tkinter.Button(root,text='我爱拼图',font=('华文彩云',40,"bold"),fg='black')
    button1.pack()
    button2 = tkinter.Button(root,text='猫和老鼠',font=('华文彩云',40,"bold"),fg='black')
    button2.pack()
    button3 = tkinter.Button(root,text='永劫无间',font=('华文彩云',40,"bold"),fg='black')
    button3.pack()
#把按钮放到 window 窗口上
    button1.place(x=410,y=180)
    button2.place(x=380,y=360)
    button3.place(x=410,y=540)
#在窗口上放一个标签
    label = tkinter.Label(root,text='请选择你要玩的游戏',font=('Cooper',50),fg='red')
    label.pack()
    label.place(x=250,y=50)
#修改标签背景色为透明色
    label['bg'] = 'white'
#给button1按钮添加事件
    button1['command'] = menu_event1
    button2['command'] = menu_event2
    button3['command'] = menu_event3
    
    root.mainloop()#显示窗口
#给菜单中的菜单项添加事件
def menu_event1():
    tkinter.messagebox.showinfo('提示','游戏开始')
    pingtu.main()
def menu_event2():
    tkinter.messagebox.showinfo('提示','游戏开始')
    Tetris.main()
def menu_event3():
    tkinter.messagebox.showinfo('提示','游戏开始')
    yjwj.main()