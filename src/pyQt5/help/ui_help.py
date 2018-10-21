#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, UiHelp):
        UiHelp.setObjectName("UiHelp")
        UiHelp.resize(197, 83)
        self.label = QtWidgets.QLabel(UiHelp)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(UiHelp)
        QtCore.QMetaObject.connectSlotsByName(UiHelp)

    def retranslateUi(self, UiHelp):
        _translate = QtCore.QCoreApplication.translate
        UiHelp.setWindowTitle(_translate("Frame", "关于"))
        self.label.setText(_translate("Frame", "Author：Wang.Chong\nDate: 2018/6/22\nVersion：v1.0"))
