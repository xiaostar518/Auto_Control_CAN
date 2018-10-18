#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from ..can_control import can_control_interface, can_kinds, can_baud_rate, can_utils


def can_start(event):  # 创建第二个事件，退出程序
    can = can_control_interface.CanDevice(can_kinds.CAN_KIND_USBCAN2)
    print("打开CAN0", can.can_start(can_utils.DEV_INDEX_DEFAULT, can_baud_rate.CAN_BAUD_RATE_125))
