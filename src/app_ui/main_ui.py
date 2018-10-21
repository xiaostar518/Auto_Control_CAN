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

        # 设置窗口图标
        root.iconbitmap(setting.iconbitmap_path)

        # 全屏
        # root.wm_state('zoomed')

        # frmLT = tkinter.Frame(width=500, height=320, bg='white')
        # frmLC = tkinter.Frame(width=500, height=150, bg='red')
        # frmLB = tkinter.Frame(width=500, height=30, bg='blue')
        # frmRT = tkinter.Frame(width=200, height=500, bg='yellow')
        #
        # frmLT.grid(row=0, column=0, padx=10, pady=3)
        # frmLC.grid(row=1, column=0, padx=15, pady=3)
        # frmLB.grid(row=2, column=0)
        # frmRT.grid(row=0, column=1, rowspan=3, padx=2, pady=3)
        #
        # frmLT.grid_propagate(0)
        # frmLC.grid_propagate(0)
        # frmLB.grid_propagate(0)
        # frmRT.grid_propagate(0)

        button_left = tkinter.Button(root, text='Left')
        button_left.pack(side=tkinter.LEFT)
        button_left.bind("<Button-1>", button_interface.button_left_control())

        button_center = tkinter.Button(root, text='TOP')
        button_center.pack(side=tkinter.TOP)
        button_center.bind("<Button-1>", button_interface.button_top_control())

        button_right = tkinter.Button(root, text='Right')
        button_right.pack(side=tkinter.RIGHT)
        button_right.bind("<Button-1>", button_interface.button_right_control())

        root.mainloop()
