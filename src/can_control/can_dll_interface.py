#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from . import can_utils, can_baud_rate, can_kinds, can_structure
from ctypes import *


class VCIControl:
    def __init__(self, can):
        self.can = can

    # 此函数用以打开设备。注意一个设备只能打开一次
    # 返回值：1表示操作成功，0表示操作失败
    def VCI_OpenDevice(self, DevType, DevIndex, Reserved=can_utils.VCI_OPENDEVICE_RESERVED_DEFAULT):
        return self.can.VCI_OpenDevice(DevType, DevIndex, Reserved)

    # 此函数用以初始化指定的CAN通道。有多个CAN通道时，需要多次调用。
    # （当设备类型为PCI-5010-U、PCI-5020-U、USBCAN-E-U、USBCAN-2E-U、USBCAN-4E-U时，
    # 必须在调用此函数之前调用VCI_SetReference对波特率进行设置）。
    # 返回值：1表示操作成功，0表示操作失败
    def VCI_InitCAN(self, DevType, DevIndex, CANIndex, pInitConfig):
        return self.can.VCI_InitCAN(DevType, DevIndex, CANIndex, pointer(pInitConfig))

    # 此函数用以设置CANET与PCI-5010-U/PCI-5020-U/USBCAN-E-U/USBCAN-2E-U/USBCAN-4E-U/CANDTU等设备的相应参数，
    # 主要处理不同设备的特定操作。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_SetReference(self, DevType, DevIndex, CANIndex=can_utils.CAN_INDEX_DEFAULT,
                         RefType=can_utils.VCI_SETREFERENCE_REFTYPE_DEFAULT,
                         baud_rate=can_baud_rate.CAN_BAUD_RATE_125):

        if DevType == can_kinds.CAN_KIND_USBCAN_2E_U:
            if baud_rate == can_baud_rate.CAN_BAUD_RATE_125:
                pData = c_char_p(0x1C0011)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_250:
                pData = c_char_p(0x1C0008)
            elif baud_rate == can_baud_rate.CAN_BAUD_RATE_500:
                pData = c_char_p(0x060007)
            else:
                pData = c_char_p(0x1C0011)

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
        else:
            return
        return self.can.VCI_SetReference(DevType, DevIndex, CANIndex, RefType, pointer(pData))

    # 此函数用以获取设备的相应参数（主要是CANET的相关参数）。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_GetReference(self, DevType, DevIndex, CANIndex=can_utils.CAN_INDEX_DEFAULT,
                         RefType=can_utils.VCI_SETREFERENCE_REFTYPE_DEFAULT,
                         pData=c_char_p):
        return self.can.VCI_GetReference(DevType, DevIndex, CANIndex, RefType, pointer(pData))

    # 此函数用以启动CAN卡的某一个CAN通道。有多个CAN通道时，需要多次调用。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_StartCAN(self, DevType, DevIndex, CANIndex):
        return self.can.VCI_StartCAN(DevType, DevIndex, CANIndex)

    # 此函数用以关闭设备。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_CloseDevice(self, DevType, DevInde):
        return self.can.VCI_CloseDevice(DevType, DevInde)

    # 此函数用以获取设备信息。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_ReadBoardInfo(self, DevType, DevIndex, pInfo=can_structure.VCI_BOARD_INFO()):
        return self.can.VCI_ReadBoardInfo(DevType, DevIndex, pInfo)

    # 此函数用以获取CAN卡发生的最近一次错误信息。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_ReadErrInfo(self, DevType, DevIndex, CANIndex, pErrInfo=can_structure.ERR_INFO()):
        return self.can.VCI_ReadErrInfo(DevType, DevIndex, CANIndex, pointer(pErrInfo))

    # 此函数用以获取CAN状态。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_ReadCANStatus(self, DevType, DevIndex, CANIndex, pCANStatus=can_structure.VCI_CAN_STATUS()):
        return self.can.VCI_ReadCANStatus(DevType, DevIndex, CANIndex, pointer(pCANStatus))

    # 此函数用以复位CAN。主要用与VCI_StartCAN配合使用，无需再初始化，即可恢复CAN卡的正常状态。
    # 比如当CAN卡进入总线关闭状态时，可以调用这个函数。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_ResetCAN(self, DevType, DevIndex, CANIndex):
        return self.can.VCI_ResetCAN(DevType, DevIndex, CANIndex)

    # 此函数用以获取指定CAN通道的接收缓冲区中，接收到但尚未被读取的帧数量。
    # 主要用途是配合VCI_Receive使用，即缓冲区有数据，再接收。
    # 用户无需一直调用VCI_Receive，可以节约PC系统资源，提高程序效率。
    # 返回值：返回尚未被读取的帧数。
    def VCI_GetReceiveNum(self, DevType, DevIndex, CANIndex):
        return self.can.VCI_GetReceiveNum(DevType, DevIndex, CANIndex)

    # 此函数用以清空指定CAN通道的缓冲区。
    # 主要用于需要清除接收缓冲区数据的情况。
    # 返回值: 为1表示操作成功，0表示操作失败。
    def VCI_ClearBuffer(self, DevType, DevIndex, CANIndex):
        return self.can.VCI_ClearBuffer(DevType, DevIndex, CANIndex)

    # 发送函数。
    # 返回值：为实际发送成功的帧数。
    def VCI_Transmit(self, DevType, DevIndex, CANIndex,
                     pSend=can_structure.VCI_CAN_OBJ(ID=1, TimeStamp=0, TimeFlag=0, SendType=0, RemoteFlag=0,
                                                     ExternFlag=0, DataLen=8), Len=1):
        return self.can.VCI_Transmit(DevType, DevIndex, CANIndex, pointer(pSend), Len)

    # 接收函数。
    # 此函数从指定的设备CAN通道的接收缓冲区中读取数据。
    # 建议在调用之前，先调用VCI_GetReceiveNum。
    # 函数获知缓冲区中有多少帧，然后对应地去接收。
    # 返回值：返回实际读取到的帧数。
    # 如果返回值为0xFFFFFFFF，则表示读取数据失败，有错误发生，请调用VCI_ReadErrInfo函数来获取错误码。
    def VCI_Receive(self, DevType, DevIndex, CANIndex, pReceive=can_structure.VCI_CAN_OBJ(), Len=1, WaitTime=-1):
        return self.can.VCI_Receive(DevType, DevIndex, CANIndex, pointer(pReceive), Len, WaitTime)
