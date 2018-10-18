#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from . import can_utils, can_baud_rate, can_kinds
from ctypes import *


class VCIControl:
    def __init__(self, can):
        self.can = can

    def VCI_OpenDevice(self, DevType, DevIndex, Reserved=can_utils.VCI_OPENDEVICE_RESERVED_DEFAULT):
        return self.can.VCI_OpenDevice(DevType, DevIndex, Reserved)

    def VCI_SetReference(self, DevType, DevIndex, CANIndex=can_utils.CANINDEX_DEFAULT,
                         RefType=can_utils.VCI_SETREFERENCE_REFTYPE_DEFAULT,
                         baud_rate=can_baud_rate.CAN_BAUD_RATE_125):
        pData = c_char_p(0x1C0011)

        if DevType == can_kinds.CAN_KIND_USBCAN_2E_U:
            if baud_rate == can_baud_rate.CAN_BAUD_RATE_125:
                pData = c_char_p(0x1C0011)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_250:
                pData = c_char_p(0x1C0008)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_500:
                pData = c_char_p(0x060007)
            else:
                pData = c_char_p(0x1C0011)
                return self.can.VCI_SetReference(DevType, DevIndex, CANIndex, RefType, pointer(pData))

        elif (DevType == can_kinds.CAN_KIND_USBCAN_8E_U) or (
                DevType == can_kinds.CAN_KIND_USBCAN_4E_U):
            if baud_rate == can_baud_rate.CAN_BAUD_RATE_125:
                pData = c_char_p(125000)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_250:
                pData = c_char_p(250000)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_500:
                pData = c_char_p(500000)
            else:
                pData = c_char_p(125000)
            return self.can.VCI_SetReference(DevType, DevIndex, CANIndex, RefType, pointer(pData))

    def VCI_InitCAN(self, DevType, DevIndex, CANIndex, pInitConfig):
        return self.can.VCI_InitCAN(DevType, DevIndex, CANIndex, pointer(pInitConfig))

    def VCI_StartCAN(self, DevType, DevIndex, CANIndex):
        return self.can.VCI_StartCAN(DevType, DevIndex, CANIndex)
