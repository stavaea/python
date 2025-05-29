# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/28 13:54
# @Author : waxberry
# @File : countdown_tool.py
# @Software : PyCharm


import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import calendar


class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("自动倒计时工具")
        self.root.geometry("500x400")

        # 状态变量
        self.running = False
        self.paused = False
        self.target_time = None # 存储最初设定的目标时间
        self.pause_remaining = None # 暂停时的剩余时间
        # self.total_paused_duration = None # 累计暂停时间
        # self.last_update_time = None # 上次更新时间
        self.update_job = None  # 用于存储定时任务

        # 初始化UI
        self.setup_ui()

        # 启动时钟更新
        self.update_clock()

    def setup_ui(self):
        """初始化用户界面"""
        # 当前时间显示
        self.current_time_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.current_time_label.pack(pady=10)

        # 目标时间设置区域
        setting_frame = tk.LabelFrame(self.root, text="设置目标时间", padx=10, pady=10)
        setting_frame.pack(fill="x", padx=20, pady=10)

        # 日期设置
        date_frame = tk.Frame(setting_frame)
        date_frame.pack(fill="x", pady=5)
        tk.Label(date_frame, text="日期:").pack(side="left")

        now = datetime.now()
        self.year_var = tk.StringVar(value=str(now.year))
        self.month_var = tk.StringVar(value=str(now.month))
        self.day_var = tk.StringVar(value=str(now.day))
        # 年份输入框
        self.year_spin = tk.Spinbox(date_frame, from_=2000, to=2100, width=5,
                                    textvariable=self.year_var, command=self.validate_date)
        self.year_spin.pack(side="left", padx=5)
        tk.Label(date_frame, text="年").pack(side="left")
        # 月份输入框
        self.month_spin = tk.Spinbox(date_frame, from_=1, to=12, width=4,
                                     textvariable=self.month_var, command=self.validate_date)
        self.month_spin.pack(side="left", padx=5)
        tk.Label(date_frame, text="月").pack(side="left")
        # 日期输入框（初始范围1-31）
        self.day_spin = tk.Spinbox(date_frame, from_=1, to=31, width=4,
                                   textvariable=self.day_var, command=self.validate_date)
        self.day_spin.pack(side="left", padx=5)
        tk.Label(date_frame, text="日").pack(side="left")

        # 时间设置
        time_frame = tk.Frame(setting_frame)
        time_frame.pack(fill="x", pady=5)
        tk.Label(time_frame, text="时间:").pack(side="left")

        self.hour_var = tk.StringVar(value=str(now.hour))
        self.minute_var = tk.StringVar(value=str(now.minute))
        self.second_var = tk.StringVar(value="0")

        self.hour_spin = tk.Spinbox(time_frame, from_=0, to=23, width=5, textvariable=self.hour_var)
        self.hour_spin.pack(side="left", padx=5)
        tk.Label(time_frame, text="时").pack(side="left")

        self.minute_spin = tk.Spinbox(time_frame, from_=0, to=59, width=4, textvariable=self.minute_var)
        self.minute_spin.pack(side="left", padx=5)
        tk.Label(time_frame, text="分").pack(side="left")

        self.second_spin = tk.Spinbox(time_frame, from_=0, to=59, width=4, textvariable=self.second_var)
        self.second_spin.pack(side="left", padx=5)
        tk.Label(time_frame, text="秒").pack(side="left")

        # 倒计时显示
        display_frame = tk.Frame(self.root)
        display_frame.pack(pady=20)

        self.days_label = tk.Label(display_frame, text="00", font=("Arial", 24), fg="blue")
        self.days_label.grid(row=0, column=0, padx=5)
        tk.Label(display_frame, text="天", font=("Arial", 12)).grid(row=1, column=0)

        self.hours_label = tk.Label(display_frame, text="00", font=("Arial", 24), fg="green")
        self.hours_label.grid(row=0, column=1, padx=5)
        tk.Label(display_frame, text="小时", font=("Arial", 12)).grid(row=1, column=1)

        self.minutes_label = tk.Label(display_frame, text="00", font=("Arial", 24), fg="orange")
        self.minutes_label.grid(row=0, column=2, padx=5)
        tk.Label(display_frame, text="分钟", font=("Arial", 12)).grid(row=1, column=2)

        self.seconds_label = tk.Label(display_frame, text="00", font=("Arial", 24), fg="red")
        self.seconds_label.grid(row=0, column=3, padx=5)
        tk.Label(display_frame, text="秒", font=("Arial", 12)).grid(row=1, column=3)

        # 目标时间显示
        self.target_display = tk.Label(self.root, text="目标时间: 未设置", font=("Arial", 12))
        self.target_display.pack(pady=10)

        # 控制按钮
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="开始", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.pause_button = tk.Button(button_frame, text="暂停", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(button_frame, text="重置", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

    def validate_date(self):
        """验证日期有效性（特别是2月份）"""
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())

            # 获取当月最大天数
            _, max_days = calendar.monthrange(year, month)

            # 调整日期输入框的最大值
            self.day_spin.config(to=max_days)

            # 如果当前日大于最大天数，自动调整为最大天数
            if day > max_days:
                self.day_var.set(str(max_days))
        except:
            pass # 避免在输入不完整时报错

    def toggle_inputs(self, state):
        '''切换输入控件的可用状态'''
        state = tk.NORMAL if state else tk.DISABLED
        self.year_spin.config(state=state)
        self.month_spin.config(state=state)
        self.day_spin.config(state=state)
        self.hour_spin.config(state=state)
        self.minute_spin.config(state=state)
        self.second_spin.config(state=state)

    def update_clock(self):
        """更新当前时间和倒计时显示"""
        try:
            # 更新当前时间显示
            now = datetime.now()
            self.current_time_label.config(text=f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

            # 更新倒计时显示
            if self.running and self.target_time:
                if self.paused:
                    # 暂停状态下显示固定的的剩余时间
                    if self.pause_remaining:
                        days = self.pause_remaining.days
                        hours, remainder = divmod(self.pause_remaining.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        self.update_display(days, hours, minutes, seconds)
                else:
                    # 运行状态下计算真实剩余时间
                    remaining = self.target_time - now
                    if remaining.total_seconds() <= 0:
                        self.timer_complete()
                    else:
                        days = remaining.days
                        hours, remainder = divmod(remaining.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        self.update_display(days, hours, minutes, seconds)

            # 安排下一次更新
            self.update_job = self.root.after(1000, self.update_clock)
        except Exception as e:
            messagebox.showerror("错误", f"更新时钟时出错: {str(e)}")
            self.reset_timer()

    def start_timer(self):
        """开始倒计时"""
        if self.running and not self.paused:
            return

        try:
            # 获取用户输入的时间
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            second = int(self.second_var.get())

            # 验证日期有效性
            _, max_days = calendar.monthrange(year, month)
            if day > max_days:
                raise ValueError(f'{year}年{month}月只有{day}天')


            # 创建目标时间
            target_time = datetime(year, month, day, hour, minute, second)
            if target_time <= datetime.now():
                raise ValueError("目标时间必须是将来的时间")

            # 更新目标时间（关键修复：确保每次开始都重新设置original_target_time）
            self.target_time = target_time

            # 如果是暂停后继续
            if self.paused:
                self.paused = False
                self.pause_button.config(text='暂停')
            else:
                # 全新开始
                # self.target_time = target_time
                # 锁定输入控件
                self.toggle_inputs(False)
            # 更新状态
            self.running = True
            self.paused = False
            self.pause_remaining = False
            self.target_display.config(text=f"目标时间: {self.target_time.strftime('%Y-%m-%d %H:%M:%S')}")
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)

            # 强制立即更新显示
            self.update_clock()

        except ValueError as e:
            messagebox.showerror("错误", f"无效的时间设置: {str(e)}")
            self.target_time = None

    def pause_timer(self):
        '''暂停/继续倒计时'''
        if not self.running:
            return

        if not self.paused:
            # 暂停倒计时
            self.paused = True
            self.pause_remaining = self.target_time - datetime.now()
            self.pause_button.config(text='继续')
        else:
            # 继续倒计时
            self.paused = False
            self.pause_remaining = False
            self.pause_button.config(text='暂停')

    def reset_timer(self):
        """重置倒计时"""
        self.running = False
        self.paused = False
        if self.update_job:
            self.root.after_cancel(self.update_job)
            self.update_job = None
        self.target_time = None
        self.pause_remaining = None
        self.update_display(0, 0, 0, 0)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text='暂停')
        self.target_display.config(text="目标时间: 未设置")

        # 解锁输入控件
        self.toggle_inputs(True)
        # 强制立即更新显示
        self.update_clock()

    def update_display(self, days, hours, minutes, seconds):
        """更新倒计时显示"""
        self.days_label.config(text=f"{days:02d}")
        self.hours_label.config(text=f"{hours:02d}")
        self.minutes_label.config(text=f"{minutes:02d}")
        self.seconds_label.config(text=f"{seconds:02d}")

    def timer_complete(self):
        """倒计时完成处理"""
        self.running = False
        self.update_display(0, 0, 0, 0)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.target_display.config(text='倒计时已完成！')

        # 解锁输入控件
        self.toggle_inputs(True)
        messagebox.showinfo("倒计时完成", f"目标时间 {self.target_time.strftime('%Y-%m-%d %H:%M:%S')} 已到达！")


if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()