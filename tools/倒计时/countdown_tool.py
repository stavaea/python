# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/28 13:54
# @Author : waxberry
# @File : countdown_tool.py
# @Software : PyCharm


import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import time
from tkinter import messagebox

class AdvancedControldownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title('倒计时工具')
        self.root.geometry('500x500')
        self.root.resizable(False, False)

        #变量初始化
        self.running = False
        self.target_time = None

        # 界面元素
        self.create_widgets()

    def create_widgets(self):
        # 标题
        tk.Label(self.root, text='倒计时工具', font=('Arial', 14)).pack(pady=10)

        # 目标时间设置
        setting_frame = tk.LabelFrame(self.root, text='设置目标时间', padx=10, pady=10)
        setting_frame.pack(pady=10, padx=20, fill='x')

        # 日期选择
        date_frame = tk.Frame(setting_frame)
        date_frame.pack(fill='x', pady=5)

        tk.Label(date_frame, text='日期:').pack(side='left')
        self.year_var = tk.StringVar(value=str(datetime.now().year))
        self.month_var = tk.StringVar(value=str(datetime.now().month))
        self.day_var = tk.StringVar(value=str(datetime.now().day))

        tk.Spinbox(date_frame, from_=2000, to=2100, width=5, textvariable=self.year_var,).pack(side='left', padx=5)
        tk.Label(date_frame, text='年').pack(side='left')
        tk.Spinbox(date_frame, from_=1, to=12, width=3, textvariable=self.month_var,).pack(side='left', padx=5)
        tk.Label(date_frame, text='月').pack(side='left')
        tk.Spinbox(date_frame, from_=1, to=31, width=3, textvariable=self.day_var,).pack(side='left', padx=5)
        tk.Label(date_frame, text='日').pack(side='left')

        # 时间选择
        time_frame = tk.Frame(setting_frame)
        time_frame.pack(fill='x', pady=5)

        tk.Label(time_frame, text='时间').pack(side='left')
        self.hour_var = tk.StringVar(value='0')
        self.minute_var = tk.StringVar(value='0')
        self.second_var = tk.StringVar(value='0')

        tk.Spinbox(time_frame, from_=0, to=23, width=3, textvariable=self.hour_var,).pack(side='left', padx=5)
        tk.Label(time_frame, text='时').pack(side='left')
        tk.Spinbox(time_frame, from_=0, to=59, width=3, textvariable=self.minute_var,).pack(side='left', padx=5)
        tk.Label(time_frame, text='分').pack(side='left')
        tk.Spinbox(time_frame, from_=0, to=59, width=3, textvariable=self.second_var, ).pack(side='left', padx=5)
        tk.Label(time_frame, text='秒').pack(side='left')

        # 显示剩余时间
        display_frame = tk.Frame(self.root)
        display_frame.pack(pady=20)

        self.days_labal = tk.Label(display_frame, text='00', font=('Arial', 24), fg='blue')
        self.days_labal.grid(row=0, column=0, padx=5)
        tk.Label(display_frame, text='天', font=('Arial', 12)).grid(row=1, column=0)

        self.hours_labal = tk.Label(display_frame, text='00', font=('Arial', 24), fg='green')
        self.hours_labal.grid(row=0, column=1, padx=5)
        tk.Label(display_frame, text='小时', font=('Arial', 12)).grid(row=1, column=1)

        self.minutes_labal = tk.Label(display_frame, text='00', font=('Arial', 24), fg='orange')
        self.minutes_labal.grid(row=0, column=2, padx=5)
        tk.Label(display_frame, text='分钟', font=('Arial', 12)).grid(row=1, column=2)

        self.seconds_labal = tk.Label(display_frame, text='00', font=('Arial', 24), fg='red')
        self.seconds_labal.grid(row=0, column=3, padx=5)
        tk.Label(display_frame, text='秒', font=('Arial', 12)).grid(row=1, column=3)

        # 目标时间显示
        self.target_display = tk.Label(self.root, text='目标时间：未设置', font=('Arial', 12))
        self.target_display.pack(pady=10)

        # 控制按钮
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text='开始倒计时', command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.pause_button = tk.Button(button_frame, text='暂停', command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(button_frame, text='重置', command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

        # 初始化显示
        self.update_display(0, 0, 0, 0)

    def start_timer(self):
        if self.running:
            return
        try:
            year = int(self.year_var.get())
            mouth = int(self.month_var.get())
            day = int(self.day_var.get())
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            second = int(self.second_var.get())

            self.target_time = datetime(year, mouth, day, hour, minute, second)
            now = datetime.now()

            if self.target_time <= now:
                raise ValueError('目标时间必须是将来的时间')

            self.running = True
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.target_display.config(text=f'目标时间: {self.target_time.strftime('%Y-%m-%d %H:%M:%S')}')

        except ValueError as e:
            messagebox.showerror('错误', f'请输入有效的时间\n{str(e)}')

    def pause_timer(self):
        self.running = not self.running

        if self.running:
            self.pause_button.config(text='暂停')
            self.update_timer()
        else:
            self.pause_button.config(text='继续')

    def reset_timer(self):
        self.running = False
        self.target_time = None
        self.update_display(0, 0, 0, 0)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text='暂停')
        self.target_display.config(text='目标时间：未设置')

    def update_timer(self):
        if self.running and self.target_time:
            now = datetime.now()
            if now >= self.target_time:
                return

            remaining = self.target_time - now
            days = remaining.days
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.update_display(days, hours, minutes, seconds)
            self.root.after = (1000, self.update_timer)

    def update_display(self, days, hours, minutes, seconds):
        self.days_labal.config(text=f'{days:02d}')
        self.hours_labal.config(text=f"{hours:02d}")
        self.minutes_labal.config(text=f"{minutes:02d}")
        self.seconds_labal.config(text=f"{seconds:02d}")

    def timer_complete(self):
        self.running = False
        self.update_display(0, 0, 0, 0)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text='暂停')
        messagebox.showinfo('倒计时完成', f'目标时间{self.target_time.strftime('%Y-%m-%d %H:%M:%S')}已到达！')

if __name__ == '__main__':
    root = tk.Tk()
    app = AdvancedControldownTimer(root)
    root.mainloop()