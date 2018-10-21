#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from tkinter import *
from src.test.LoginPage import *

if __name__ == '__main__':
    root = Tk()
    root.title('小程序')
    LoginPage(root)
    root.mainloop()
