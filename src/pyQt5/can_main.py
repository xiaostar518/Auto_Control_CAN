# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from pyQt5.setting import can_init
from pyQt5.help import ui_help


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.MainInpute = QtWidgets.QTabWidget(self.centralwidget)
        self.MainInpute.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.MainInpute.setObjectName("MainInpute")
        self.Inpute = QtWidgets.QWidget()
        self.Inpute.setObjectName("Inpute")
        self.MainInpute.addTab(self.Inpute, "")
        self.Running = QtWidgets.QWidget()
        self.Running.setObjectName("Running")
        self.MainInpute.addTab(self.Running, "")
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.MainInpute.addTab(self.Report, "")
        self.Tool = QtWidgets.QWidget()
        self.Tool.setObjectName("Tool")
        self.MainInpute.addTab(self.Tool, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        MainWindow.setMenuBar(self.menubar)

        self.menubar.setObjectName("menubar")
        self.Setting = QtWidgets.QMenu(self.menubar)
        self.Setting.setObjectName("Setting")

        self.action_can = QtWidgets.QAction(MainWindow)
        self.action_can.setObjectName("action_can")
        self.action_can.triggered.connect(self.on_click_can)

        self.action_usb = QtWidgets.QAction(MainWindow)
        self.action_usb.setObjectName("action_usb")

        self.action_data = QtWidgets.QAction(MainWindow)
        self.action_data.setObjectName("action_data")

        self.action_serial_port = QtWidgets.QAction(MainWindow)
        self.action_serial_port.setObjectName("action_serial_port")

        self.action_camera = QtWidgets.QAction(MainWindow)
        self.action_camera.setObjectName("action_camera")

        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(self.on_click_exit)

        self.Setting.addAction(self.action_can)
        self.Setting.addAction(self.action_usb)
        self.Setting.addAction(self.action_data)
        self.Setting.addAction(self.action_serial_port)
        self.Setting.addAction(self.action_camera)
        self.Setting.addSeparator()
        self.Setting.addAction(self.action_exit)

        self.Loading = QtWidgets.QMenu(self.menubar)
        self.Loading.setObjectName("Loading")

        self.Saving = QtWidgets.QMenu(self.menubar)
        self.Saving.setObjectName("Saving")

        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_about.triggered.connect(self.on_click_about)
        self.Help.addAction(self.action_about)

        self.menubar.addAction(self.Setting.menuAction())
        self.menubar.addAction(self.Loading.menuAction())
        self.menubar.addAction(self.Saving.menuAction())
        self.menubar.addAction(self.Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.MainInpute.setTabText(self.MainInpute.indexOf(self.Inpute), _translate("MainWindow", "输入"))
        self.MainInpute.setTabText(self.MainInpute.indexOf(self.Running), _translate("MainWindow", "运行"))
        self.MainInpute.setTabText(self.MainInpute.indexOf(self.Report), _translate("MainWindow", "报告"))
        self.MainInpute.setTabText(self.MainInpute.indexOf(self.Tool), _translate("MainWindow", "工具"))

        self.Setting.setTitle(_translate("MainWindow", "设置"))
        self.Loading.setTitle(_translate("MainWindow", "载入"))
        self.Saving.setTitle(_translate("MainWindow", "保存"))
        self.Help.setTitle(_translate("MainWindow", "帮助"))

        self.action_can.setText(_translate("MainWindow", "can初始化"))
        self.action_usb.setText(_translate("MainWindow", "usb初始化"))
        self.action_data.setText(_translate("MainWindow", "数据采集卡初始化"))
        self.action_serial_port.setText(_translate("MainWindow", "串口初始化"))
        self.action_camera.setText(_translate("MainWindow", "摄像头初始化"))
        self.action_exit.setText(_translate("MainWindow", "退出"))
        self.action_about.setText(_translate("MainWindow", "关于"))

    def on_click_about(self):
        about_Dialog = QtWidgets.QDialog()
        uiHelp = ui_help.Ui_Help()
        uiHelp.setupUi(about_Dialog)
        about_Dialog.show()
        about_Dialog.exec_()

    def on_click_can(self):
        canInit_Dialog = QtWidgets.QDialog()
        uiCanInit = can_init.Ui_CanInit()
        uiCanInit.setupUi(canInit_Dialog)
        canInit_Dialog.show()
        canInit_Dialog.exec_()

    def on_click_exit(self):
        sys.exit(app.exec_())


import sys

app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
myWin = Ui_MainWindow()
myWin.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())
