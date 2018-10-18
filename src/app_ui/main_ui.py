#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from . import button_interface, setting

import tkinter


def buttonListener3(event):  # 创建第二个事件，退出程序
    print('HelloWorld')


class AppUI():
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        root = tkinter.Tk()
        # self.our_control = OurControl()
        self.case_list = []

        # 全屏和取消全屏时的大小
        root.title(setting.window_title)
        root.geometry(setting.window_size)
        # self.master['background'] = 'LightSkyBlue'

        # 设置窗口图标
        root.iconbitmap(setting.iconbitmap_path)

        # 全屏
        root.wm_state('zoomed')

        button_left = tkinter.Button(root, text='Left')
        button_left.pack(side=tkinter.LEFT)
        button_left.bind("<Button-1>", button_interface.button_left_control())

        button_right = tkinter.Button(root, text='Right')
        button_right.bind("<Button-1>", buttonListener3)
        button_right.pack(side=tkinter.RIGHT)

        root.mainloop()
