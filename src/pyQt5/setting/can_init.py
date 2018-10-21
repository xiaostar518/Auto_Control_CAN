# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'can_init.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from can_control import can_kinds

devStyles = [can_kinds.CAN_KIND_USBCAN2_NAME,
             can_kinds.CAN_KIND_USBCAN_2E_U_NAME,
             can_kinds.CAN_KIND_USBCAN_4E_U_NAME,
             can_kinds.CAN_KIND_USBCAN_8E_U_NAME]


class Ui_CanInit(object):
    def setupUi(self, CanInit):
        CanInit.setObjectName("CanInit")
        CanInit.resize(343, 230)
        self.DevStyle = QtWidgets.QLabel(CanInit)
        self.DevStyle.setGeometry(QtCore.QRect(50, 20, 54, 12))
        self.DevStyle.setObjectName("DevStyle")

        self.Index = QtWidgets.QLabel(CanInit)
        self.Index.setGeometry(QtCore.QRect(50, 50, 54, 12))
        self.Index.setObjectName("Index")

        self.Num = QtWidgets.QLabel(CanInit)
        self.Num.setGeometry(QtCore.QRect(50, 80, 54, 12))
        self.Num.setObjectName("Num")

        self.Android = QtWidgets.QLabel(CanInit)
        self.Android.setGeometry(QtCore.QRect(20, 110, 101, 16))
        self.Android.setObjectName("Android")

        self.Camera = QtWidgets.QLabel(CanInit)
        self.Camera.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.Camera.setObjectName("Camera")

        self.DevStyleChoice = QtWidgets.QComboBox(CanInit)
        self.DevStyleChoice.setGeometry(QtCore.QRect(150, 20, 141, 22))
        self.DevStyleChoice.setObjectName("DevStyleChoice")
        self.DevStyleChoice.addItems(devStyles)

        self.IndexChoice = QtWidgets.QSpinBox(CanInit)
        self.IndexChoice.setGeometry(QtCore.QRect(150, 50, 141, 22))
        self.IndexChoice.setObjectName("IndexChoice")

        self.NumChoice = QtWidgets.QSpinBox(CanInit)
        self.NumChoice.setGeometry(QtCore.QRect(150, 80, 141, 22))
        self.NumChoice.setObjectName("NumChoice")

        self.AndroidNum = QtWidgets.QLineEdit(CanInit)
        self.AndroidNum.setGeometry(QtCore.QRect(150, 110, 141, 20))
        self.AndroidNum.setObjectName("AndroidNum")

        self.CameraUrl = QtWidgets.QLineEdit(CanInit)
        self.CameraUrl.setGeometry(QtCore.QRect(150, 140, 141, 20))
        self.CameraUrl.setObjectName("CameraUrl")

        self.Confirm = QtWidgets.QPushButton(CanInit)
        self.Confirm.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.Confirm.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Confirm.setObjectName("Confirm")

        self.Cancel = QtWidgets.QPushButton(CanInit)
        self.Cancel.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(CanInit)
        QtCore.QMetaObject.connectSlotsByName(CanInit)

    def retranslateUi(self, CanInit):
        _translate = QtCore.QCoreApplication.translate
        CanInit.setWindowTitle(_translate("CanInit", "can初始化"))
        self.DevStyle.setText(_translate("CanInit", "设备类型："))
        self.Index.setText(_translate("CanInit", "设备号："))
        self.Num.setText(_translate("CanInit", "通道号："))
        self.Android.setText(_translate("CanInit", "Android设备编号"))
        self.Camera.setText(_translate("CanInit", "摄像头地址"))
        self.Confirm.setText(_translate("CanInit", "确定"))
        self.Cancel.setText(_translate("CanInit", "取消"))
