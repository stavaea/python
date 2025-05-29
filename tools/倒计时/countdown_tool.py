# -*- coding:utf-8 -*-
# ！/usr/bin/env python
# @Time : 2025/5/28 13:54
# @Author : waxberry
# @File : countdown_tool.py
# @Software : PyCharm


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import calendar
import json
import os
from PIL import Image, ImageTk


class CountdownTimer:
    CONFIG_FILE = 'countdown_config.json'
    THEMES = {
        '默认': {
            'bg': '#f0f0f0',
            'fg': '#000000',
            'button_bg': '#e0e0e0',
            'display_fg': ['blue', 'green', 'orange', 'red'],
            'entry_bg': 'white',
            'entry_fg': 'black',
            'frame_bg': '#f0f0f0',
            'label_frame_bg': '#f0f0f0',
        },
        '深色': {
            'bg': '#2d2d2d',
            'fg': '#ffffff',
            'button_bg': '#3d3d3d',
            'display_fg': ['#5b9bd5', '#70ad47', '#ffc000', '#ff0000'],
            'entry_bg': '#4d4d4d',
            'entry_fg': '#ffffff',
            'frame_bg': '#2d2d2d',
            'label_frame_bg': '#3d3d3d',
        },
        '蓝色': {
            'bg': '#e6f2ff',
            'fg': '#003366',
            'button_bg': '#cce0ff',
            'display_fg': ['#0033cc', '#0066cc', '#0099cc', '#00cccc'],
            'entry_bg': 'white',
            'entry_fg': 'black',
            'frame_bg': '#e6f2ff',
            'label_frame_bg': '#d6e9ff',
        }
    }
    def __init__(self, root):
        self.root = root
        self.root.title("自动倒计时工具")
        self.root.geometry("500x500")

        # 状态变量
        self.running = False
        self.paused = False
        self.target_time = None # 存储最初设定的目标时间
        self.pause_remaining = None # 暂停时的剩余时间
        self.update_job = None  # 用于存储定时任务
        self.auto_start_var = tk.BooleanVar(value=False) #初始化自动开始变量
        self.event_name_var = tk.StringVar(value='目标事件')
        self.current_theme = '默认'
        self.custom_bg_image = None
        self.bg_image_label = None

        # 存储所有需要换肤的控件
        self.themeable_widgets = []

        # 初始化UI
        self.setup_ui()

        # 加载上次保存的设置
        self.load_settings()

        # 启动时钟更新
        self.update_clock()

        # 窗口关闭时保存设置
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

    def load_settings(self):
        '''加载上次保存的设置'''
        if os.path.exists(self.CONFIG_FILE):
            try:
                with open(self.CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                    # 设置时间控件值
                    if 'year' in config:
                        self.year_var.set(config['year'])
                    if 'month' in config:
                        self.month_var.set(config['month'])
                    if 'day' in config:
                        self.day_var.set(config['day'])
                    if 'hour' in config:
                        self.hour_var.set(config['hour'])
                    if 'minute' in config:
                        self.minute_var.set(config['minute'])
                    if 'second' in config:
                        self.second_var.set(config['second'])
                    if 'auto_start' in config:
                        self.auto_start_var.set(config['auto_start'])
                    if 'event_name' in config:
                        self.event_name_var.set(config['event_name'])
                    if 'theme' in config:
                        self.current_theme = config['theme']
                        self.apply_theme()
                    if 'bg_image' in config and os.path.exists(config['bg_image']):
                        self.load_bg_image(config['bg_image'])

                    # 验证日期有效性
                    self.validate_date()

                    # 如果有设置且启用了自动开始
                    if self.auto_start_var.get() and self.has_valid_time_set():
                        # 使用after延迟启动，确保UI完全加载
                        self.root.after(100, self.auto_start_timer)

            except Exception as e:
                print(f'加载设置失败:{e}')

    def auto_start_timer(self):
        '''自动开始倒计时'''
        if not self.running and self.has_valid_time_set():
            self.start_timer()

    def has_valid_time_set(self):
        '''检查是否有有效时间设置'''
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            second = int(self.second_var.get())

            # 验证日期有效性
            _, max_days = calendar.monthrange(year, month)
            if day > max_days:
                return False

            # 创建目标时间
            target_time = datetime(year, month, day, hour, minute, second)
            if target_time <= datetime.now():
                return False

            return True
        except:
            return False

    def save_settings(self):
        '''保存到当前设置文件'''
        try:
            config = {'year': self.year_var.get(),
                      'month': self.month_var.get(),
                      'day': self.day_var.get(),
                      'hour': self.hour_var.get(),
                      'minute': self.minute_var.get(),
                      'second': self.second_var.get(),
                      'auto_start': self.auto_start_var.get(),
                      'event_name': self.event_name_var.get(),
                      'theme': self.current_theme,
                      'bg_image': self.custom_bg_image if self.custom_bg_image else ''
                      }
            with open(self.CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f)
        except Exception as e:
            print(f'保存设置失败：{e}')

    def on_close(self):
        '''窗口关闭事件处理'''
        self.save_settings()
        if self.update_job:
            self.root.after_cancel(self.update_job)
        self.root.destroy()

    def setup_ui(self):
        """初始化用户界面"""
        # 主容器
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True)
        self.themeable_widgets.append(self.main_frame)

        # 当前时间显示
        self.current_time_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.current_time_label.pack(pady=10)

        # 背景图片标签（先创建但不显示）
        self.bg_image_label = tk.Label(self.main_frame)
        self.bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_image_label.lower()

        # 配置选项区域
        config_frame = tk.LabelFrame(self.root, text='配置选项', padx=10, pady=10)
        config_frame.pack(fill='x', padx=20, pady=5)
        self.themeable_widgets.append(config_frame)

        # 事件名称设置
        event_frame = tk.Frame(config_frame)
        event_frame.pack(fill='x', pady=5)
        self.themeable_widgets.append(event_frame)

        tk.Label(event_frame, text='距离：').pack(side='left')
        self.event_entry = tk.Entry(event_frame, textvariable=self.event_name_var)
        self.event_entry.pack(side='left', fill='x', expand=True, padx=5)
        self.themeable_widgets.append(self.event_entry)

        # 自动开始复选框
        auto_start_frame = tk.Frame(config_frame)
        auto_start_frame.pack(fill='x', pady=5)
        self.themeable_widgets.append(auto_start_frame)

        self.auto_start_check = tk.Checkbutton(
            config_frame,
            text='自动开始倒计时',
            variable=self.auto_start_var,
            command=self.save_settings()
        )
        self.auto_start_check.pack(side='left')
        self.themeable_widgets.append(self.auto_start_check)

        # 主题选择
        theme_frame = tk.Frame(config_frame)
        theme_frame.pack(fill='x', pady=5)
        self.themeable_widgets.append(theme_frame)

        tk.Label(theme_frame, text='主题：').pack(side='left')

        self.theme_var = tk.StringVar(value=self.current_theme)
        self.theme_menu = ttk.Combobox(
            theme_frame,
            textvariable=self.theme_var,
            values=list(self.THEMES.keys()) + ['自定义背景'],
            state='readonly'
        )
        self.theme_menu.pack(side='left', padx=5)
        self.theme_menu.bind('<<ComboboxSelected>>', self.change_theme)

        # 目标时间设置区域
        setting_frame = tk.LabelFrame(self.root, text="设置目标时间", padx=10, pady=10)
        setting_frame.pack(fill="x", padx=20, pady=10)
        self.themeable_widgets.append(setting_frame)

        # 日期设置
        date_frame = tk.Frame(setting_frame)
        date_frame.pack(fill="x", pady=5)
        self.themeable_widgets.append(date_frame)

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
        self.themeable_widgets.append(time_frame)

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
        self.themeable_widgets.append(display_frame)

        self.event_label = tk.Label(display_frame, text='剩余', font=('Arial', 18))
        self.event_label.pack()
        self.themeable_widgets.append(self.event_label)

        time_display_frame = tk.Frame(display_frame)
        time_display_frame.pack()
        self.themeable_widgets.append(time_display_frame)

        self.days_label = tk.Label(time_display_frame, text="00", font=("Arial", 24), fg="blue")
        self.days_label.grid(row=0, column=0, padx=5)
        tk.Label(time_display_frame, text="天", font=("Arial", 12)).grid(row=1, column=0)

        self.hours_label = tk.Label(time_display_frame, text="00", font=("Arial", 24), fg="green")
        self.hours_label.grid(row=0, column=1, padx=5)
        tk.Label(time_display_frame, text="小时", font=("Arial", 12)).grid(row=1, column=1)

        self.minutes_label = tk.Label(time_display_frame, text="00", font=("Arial", 24), fg="orange")
        self.minutes_label.grid(row=0, column=2, padx=5)
        tk.Label(time_display_frame, text="分钟", font=("Arial", 12)).grid(row=1, column=2)

        self.seconds_label = tk.Label(time_display_frame, text="00", font=("Arial", 24), fg="red")
        self.seconds_label.grid(row=0, column=3, padx=5)
        tk.Label(time_display_frame, text="秒", font=("Arial", 12)).grid(row=1, column=3)

        # 目标时间显示
        self.target_display = tk.Label(self.root, text="目标时间: 未设置", font=("Arial", 12))
        self.target_display.pack(pady=10)
        self.themeable_widgets.append(self.target_display)

        # 控制按钮
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        self.themeable_widgets.append(button_frame)

        self.start_button = tk.Button(button_frame, text="开始", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)
        self.themeable_widgets.append(self.start_button)

        self.pause_button = tk.Button(button_frame, text="暂停", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=0, column=1, padx=10)
        self.themeable_widgets.append(self.pause_button)

        self.reset_button = tk.Button(button_frame, text="重置", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)
        self.themeable_widgets.append(self.reset_button)

        # 将所有标签添加到可换肤控件列表
        for child in self.main_frame.winfo_children():
            self.collect_labels(child)

        # 应用初始主题
        self.apply_theme()

    def collect_labels(self, parent):
        '''递归收集所有标签'''
        for child in parent.winfo_children():
            if isinstance(child, tk.Label):
                self.themeable_widgets.append(child)
            if isinstance(child, (tk.Frame, ttk.Frame, tk.LabelFrame)):
                self.collect_labels(child)

    def change_theme(self, event=None):
        '''更换主题'''
        selected = self.theme_var.get()
        if selected == "自定义背景":
            self.choose_custom_bg()
        else:
            self.current_theme = selected
            self.custom_bg_image = None
            self.apply_theme()
            self.save_settings()

    def choose_custom_bg(self):
        '''选择自定义背景图片'''
        file_path = filedialog.askopenfilename(
            title='选择背景图片',
            filetypes=[('图片文件', '*.jpg *.jpeg *.png *.bmp *.gif')],
        )
        if file_path:
            self.load_bg_image(file_path)
            self.current_theme = '自定义背景'
            self.theme_var.set('自定义背景')
            self.save_settings()

    def load_bg_image(self, image_path):
        '''加载背景图片'''
        try:
            self.custom_bg_image = image_path
            img = Image.open(image_path)
            img = img.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img)
            self.bg_image_label.config(image=self.bg_photo)
            self.bg_image_label.lift()
        except Exception as e:
            messagebox.showerror('错误', f'加载背景图片失败{str(e)}')
            self.custom_bg_image = None
            self.bg_image_label.config(image='')
            self.current_theme = '默认'
            self.theme_var.set('默认')
            self.apply_theme()

    def apply_theme(self):
        '''应用当前主题'''
        theme = self.THEMES.get(self.current_theme, self.THEMES['默认'])

        # 设置主窗口背景
        self.root.config(bg=theme['bg'])
        self.main_frame.config(bg=theme['bg'])

        # 隐藏或显示背景图片
        if self.current_theme == '自定义背景' and self.custom_bg_image:
            self.bg_image_label.lift()
        else:
            self.bg_image_label.lower()

        # 应用颜色主题
        for widget in self.themeable_widgets:
            if isinstance(widget, tk.Label):
                widget.config(bg=theme['bg'], fg=theme['fg'])
            elif isinstance(widget, tk.Button):
                widget.config(bg=theme['button_bg'], fg=theme['fg'], activebackground=theme['button_bg'])
            elif isinstance(widget, tk.Entry):
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'])
            elif isinstance(widget, tk.Frame):
                widget.config(bg=theme['frame_bg'])
            elif isinstance(widget, tk.LabelFrame):
                widget.config(bg=theme['label_frame_bg'], fg=theme['fg'])
            elif isinstance(widget, tk.Spinbox):
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], buttonbackground=theme['button_bg'])

        # 更新倒计时显示颜色
        self.days_label.config(fg=theme['display_fg'][0])
        self.hours_label.config(fg=theme['display_fg'][1])
        self.minutes_label.config(fg=theme['display_fg'][2])
        self.seconds_label.config(fg=theme['display_fg'][3])

        # 更新组合框样式
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox',
                        fieldbackground=theme['entry_bg'],
                        background=theme['button_bg'],
                        foreground=theme['fg'],
                        selectbackground=theme['entry_bg'],
                        selecforeground=['fg']
                        )

        # 更新复选框样式
        self.auto_start_check.config(bg=theme['bg'], fg=theme['fg'], selectcolor=theme['button_bg'])

        # 更新事件名称显示
        self.event_label.config(bg=theme['bg'], fg=theme['fg'])
        self.target_display.config(bg=theme['bg'], fg=theme['fg'])

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