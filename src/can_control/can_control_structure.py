#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from . import can_baud_rate, can_structure


class CanControlStructure:
    def __init__(self):
        pass

    def VCI_INIT_CONFIG(self, baud_rate):
        if baud_rate == can_baud_rate.CAN_BAUD_RATE_125:
            init_config = can_structure.VCI_INIT_CONFIG(AccCode=0, AccMask=0xFFFFFFFF, Reserved=0, Filter=0,
                                                        Timing0=3,
                                                        Timing1=0x1c, Mode=0)
        elif baud_rate == can_baud_rate.CAN_BAUD_RATE_250:
            init_config = can_structure.VCI_INIT_CONFIG(AccCode=0, AccMask=0xFFFFFFFF, Reserved=0, Filter=1,
                                                        Timing0=1,
                                                        Timing1=0x1c, Mode=0)
        elif baud_rate == can_baud_rate.CAN_BAUD_RATE_500:
            init_config = can_structure.VCI_INIT_CONFIG(AccCode=0, AccMask=0xFFFFFFFF, Reserved=0, Filter=1,
                                                        Timing0=0,
                                                        Timing1=0x1c, Mode=0)
        else:
            init_config = can_structure.VCI_INIT_CONFIG(AccCode=0, AccMask=0xFFFFFFFF, Reserved=0, Filter=0,
                                                        Timing0=3,
                                                        Timing1=0x1c, Mode=0)
        return init_config
