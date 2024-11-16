import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import pickle
import pygame
import random
# 实例化窗口
window = tk.Tk()
window.title('登录界面')
window.geometry('800x600')
window.configure(bg='#F0F8FF')  # 设置背景颜色

# 画布
canvas = tk.Canvas(window, width=800, height=600, bg='#F0F8FF', highlightthickness=0)

# 创建动态图案
circles = []
for _ in range(20):  
    x1 = random.randint(0, 800)
    y1 = random.randint(0, 600)
    r = random.randint(20, 50)
    x2, y2 = x1 + r, y1 + r
    color = random.choice(["#FFB6C1", "#ADD8E6", "#90EE90", "#FFD700", "#FFA07A"])
    circle = canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")
    circles.append((circle, random.randint(-1, 1), random.randint(-1, 1)))  # 添加速度

def move_circles():
    for i, (circle, dx, dy) in enumerate(circles):
        # 移动圆形
        canvas.move(circle, dx, dy)
        coords = canvas.coords(circle)
        if coords[0] <= 0 or coords[2] >= 800:  
            dx = -dx  
        if coords[1] <= 0 or coords[3] >= 600:  
            dy = -dy  
        circles[i] = (circle, dx, dy)
    # 递归调用更新
    window.after(50, move_circles)


# 启动动态效果
move_circles()
# 图片
image_file = tk.PhotoImage(file='1.png')  # 替换为你的图片路径
canvas.create_image(64, 0, anchor='n', image=image_file)
canvas.create_text(400, 60, text="欢迎来到游戏登录注册界面", fill="#4B0082", font=("Helvetica", 24, "bold"))
canvas.pack()

# 用户信息标签
tk.Label(window, text='用户名:', font=('Arial', 13), bg='#F0F8FF').place(x=200, y=200)
tk.Label(window, text='密码:', font=('Arial', 13), bg='#F0F8FF').place(x=200, y=240)

# 用户输入框
var_usr_name = tk.StringVar()
var_usr_name.set('username@email.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 13), width=25)
entry_usr_name.place(x=320, y=200)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 13), show='*', width=25)
entry_usr_pwd.place(x=320, y=240)

# 登录功能
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info and usr_pwd == usrs_info[usr_name]:
        tkinter.messagebox.showinfo('欢迎', f'您好！欢迎 {usr_name}')
    elif usr_name in usrs_info:
        tkinter.messagebox.showerror('错误', '密码错误，请重试！')
    else:
        if tkinter.messagebox.askyesno('提示', '用户不存在，是否注册？'):
            usr_sign_up()

# 注册功能
def usr_sign_up():
    def sign_to_website():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        if np != npf:
            tkinter.messagebox.showerror('错误', '密码和确认密码不一致！')
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('错误', '用户名已被注册！')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('成功', '注册成功！')
            window_sign_up.destroy()
    
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x300')
    window_sign_up.title('注册')
    window_sign_up.configure(bg='#F0F8FF')
    tk.Label(window_sign_up, text='用户名:', font=('Arial', 12), bg='#F0F8FF').place(x=40, y=30)
    new_name = tk.StringVar()
    tk.Entry(window_sign_up, textvariable=new_name, font=('Arial', 12)).place(x=150, y=30)
    tk.Label(window_sign_up, text='密码:', font=('Arial', 12), bg='#F0F8FF').place(x=40, y=80)
    new_pwd = tk.StringVar()
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*', font=('Arial', 12)).place(x=150, y=80)
    tk.Label(window_sign_up, text='确认密码:', font=('Arial', 12), bg='#F0F8FF').place(x=40, y=130)
    new_pwd_confirm = tk.StringVar()
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*', font=('Arial', 12)).place(x=150, y=130)
    btn_confirm = tk.Button(window_sign_up, text='注册用户', font=('Arial', 12), command=sign_to_website, bg='#F0F8FF')
    btn_confirm.place(x=200, y=180)
 
# 按钮样式
btn_style = {'font': ('Arial', 14), 'width': 10, 'bg': '#F0F8FF', 'relief': 'raised'}
btn_login = tk.Button(window, text='登录', command=usr_login, **btn_style)
btn_login.place(x=220, y=330)
btn_sign_up = tk.Button(window, text='注册', command=usr_sign_up,**btn_style)
btn_sign_up.place(x=420, y=330)
btn_game = tk.Button(window, text='开始游戏', **btn_style)
btn_game.place(x=220, y=400)
btn_quit = tk.Button(window, text='退出游戏', command=window.quit, **btn_style)
btn_quit.place(x=420, y=400)
#音乐
def play_music():
    pygame.mixer.init()  
    pygame.mixer.music.load("vo3.mp3")  
    pygame.mixer.music.set_volume(0.1)  
    pygame.mixer.music.play(-1)  

# 播放音乐
play_music()

# 主窗口循环
window.mainloop()