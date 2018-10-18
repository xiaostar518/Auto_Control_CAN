#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from ctypes import *


class VCI_CAN_OBJ(Structure):
    _fields_ = [("ID", c_uint), ("TimeStamp", c_uint), ("TimeFlag", c_byte), ("SendType", c_byte),
                ("RemoteFlag", c_byte),
                ("ExternFlag", c_byte), ("DataLen", c_byte), ("Data", c_ubyte * 8), ("Reserved", c_byte * 3)]


class VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_long), ("AccMask", c_long), ("Reserved", c_long), ("Filter", c_ubyte),
                ("Timing0", c_ubyte),
                ("Timing1", c_ubyte), ("Mode", c_ubyte)]


class VCI_CAN_STATUS(Structure):
    _fields_ = [("ErrInterrupt", c_ubyte), ("regMode", c_ubyte), ("regStatus", c_ubyte), ("regALCapture", c_ubyte),
                ("regECCapture", c_ubyte),
                ("regEWLimit", c_ubyte), ("regRECounter", c_ubyte), ("regTECounter", c_ubyte), ("Reserved", c_long)]


class VCI_BOARD_INFO(Structure):
    _fields_ = [("hw_Version", c_ushort), ("fw_Version", c_ushort), ("dr_Version", c_ushort), ("in_Version", c_ushort),
                ("irq_Num", c_ushort),
                ("can_Num", c_byte), ("str_Serial_Num", c_char * 20), ("str_hw_Type", c_char * 40),
                ("Reserved", c_ushort * 4)]


class VCI_FILTER_RECORD(Structure):
    _fields_ = [("ExtFrame", c_long), ("Start", c_long), ("End", c_long)]


class ERR_INFO(Structure):
    _fields_ = [("ErrCode", c_uint), ("Passive_ErrData", c_byte * 3), ("ArLost_ErrData", c_byte)]


class VCI_AUTO_SEND_OBJ(Structure):
    _fields_ = [("Enable", c_byte), ("Index", c_byte), ("Interval", c_double), ("Obj", VCI_CAN_OBJ)]
