#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
from ..can_control import can_control_interface, can_kinds, can_baud_rate, can_utils

canDevices = []


def can_init(event):
    global canDevices
    canDevice = can_control_interface.CanDevice(can_kinds.CAN_KIND_USBCAN2, can_utils.CAN_INDEX_DEFAULT)
    canDevices.append(canDevice)
    for can in canDevices:
        print('canDevice----------')
        if can.devType == can_kinds.CAN_KIND_USBCAN2:
            print('devType: ', can_kinds.CAN_KIND_USBCAN2_NAME)
        elif can.devType == can_kinds.CAN_KIND_USBCAN_2E_U:
            print('devType: ', can_kinds.CAN_KIND_USBCAN_2E_U_NAME)
        elif can.devType == can_kinds.CAN_KIND_USBCAN_4E_U:
            print('devType: ', can_kinds.CAN_KIND_USBCAN_4E_U_NAME)
        elif can.devType == can_kinds.CAN_KIND_USBCAN_8E_U:
            print('devType: ', can_kinds.CAN_KIND_USBCAN_8E_U_NAME)
        print('devIndex: ', can.devIndex)
        print('\n')


def can_start(event):
    can_start_result = canDevices[0].can_start(can_utils.CAN_INDEX_DEFAULT, can_baud_rate.CAN_BAUD_RATE_125)
    if can_start_result == can_utils.CAN_RESULT_CODE_SUCCESS:
        print('打开CAN0', 'success')
    else:
        print("打开CAN0", 'fail')


def can_close(event):
    can_close_result = canDevices[0].can_close()
    if can_close_result == can_utils.CAN_RESULT_CODE_SUCCESS:
        print('关闭CAN0', 'success')
    else:
        print("关闭CAN0", 'fail')
