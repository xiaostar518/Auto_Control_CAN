#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from ..ui_control_can import control_can


def button_left_control():
    return control_can.can_init


def button_top_control():
    return control_can.can_close


def button_right_control():
    return control_can.can_start
