# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conf.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wnd_configure(object):
    def setupUi(self, wnd_configure):
        wnd_configure.setObjectName("wnd_configure")
        wnd_configure.resize(802, 514)
        self.centralwidget = QtWidgets.QWidget(wnd_configure)
        self.centralwidget.setObjectName("centralwidget")
        self.grp_cells = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_cells.setGeometry(QtCore.QRect(10, 180, 481, 71))
        self.grp_cells.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.grp_cells.setObjectName("grp_cells")
        self.comboBox = QtWidgets.QComboBox(self.grp_cells)
        self.comboBox.setGeometry(QtCore.QRect(400, 0, 79, 27))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.grp_cells)
        self.label.setGeometry(QtCore.QRect(150, 40, 67, 19))
        self.label.setObjectName("label")
        self.grp_cellsView = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_cellsView.setGeometry(QtCore.QRect(0, 0, 551, 141))
        self.grp_cellsView.setObjectName("grp_cellsView")
        self.chk_cellSolorSelect = QtWidgets.QCheckBox(self.grp_cellsView)
        self.chk_cellSolorSelect.setGeometry(QtCore.QRect(50, 30, 121, 25))
        self.chk_cellSolorSelect.setObjectName("chk_cellSolorSelect")
        self.label_2 = QtWidgets.QLabel(self.grp_cellsView)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 67, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.grp_cellsView)
        self.label_3.setGeometry(QtCore.QRect(200, 60, 67, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.grp_cellsView)
        self.label_4.setGeometry(QtCore.QRect(200, 90, 67, 19))
        self.label_4.setObjectName("label_4")
        self.edt_crytical = QtWidgets.QLineEdit(self.grp_cellsView)
        self.edt_crytical.setGeometry(QtCore.QRect(270, 30, 113, 21))
        self.edt_crytical.setObjectName("edt_crytical")
        self.edt_warning = QtWidgets.QLineEdit(self.grp_cellsView)
        self.edt_warning.setGeometry(QtCore.QRect(270, 60, 113, 21))
        self.edt_warning.setObjectName("edt_warning")
        self.edt_ok = QtWidgets.QLineEdit(self.grp_cellsView)
        self.edt_ok.setGeometry(QtCore.QRect(270, 90, 113, 21))
        self.edt_ok.setObjectName("edt_ok")
        self.btn_crytical = QtWidgets.QPushButton(self.grp_cellsView)
        self.btn_crytical.setGeometry(QtCore.QRect(400, 30, 31, 27))
        self.btn_crytical.setText("")
        self.btn_crytical.setObjectName("btn_crytical")
        self.buttonGroup = QtWidgets.QButtonGroup(wnd_configure)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_crytical)
        self.btn_warning = QtWidgets.QPushButton(self.grp_cellsView)
        self.btn_warning.setGeometry(QtCore.QRect(400, 60, 31, 27))
        self.btn_warning.setText("")
        self.btn_warning.setObjectName("btn_warning")
        self.buttonGroup.addButton(self.btn_warning)
        self.btn_ok = QtWidgets.QPushButton(self.grp_cellsView)
        self.btn_ok.setGeometry(QtCore.QRect(400, 90, 31, 27))
        self.btn_ok.setText("")
        self.btn_ok.setObjectName("btn_ok")
        self.buttonGroup.addButton(self.btn_ok)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 210, 88, 27))
        self.pushButton.setObjectName("pushButton")
        wnd_configure.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(wnd_configure)
        self.statusbar.setObjectName("statusbar")
        wnd_configure.setStatusBar(self.statusbar)

        self.retranslateUi(wnd_configure)
        QtCore.QMetaObject.connectSlotsByName(wnd_configure)

    def retranslateUi(self, wnd_configure):
        _translate = QtCore.QCoreApplication.translate
        wnd_configure.setWindowTitle(_translate("wnd_configure", "Configure"))
        self.grp_cells.setTitle(_translate("wnd_configure", "Cells view settings"))
        self.label.setText(_translate("wnd_configure", "TextLabel"))
        self.grp_cellsView.setTitle(_translate("wnd_configure", "Cells view settings"))
        self.chk_cellSolorSelect.setText(_translate("wnd_configure", "Color scheme"))
        self.label_2.setText(_translate("wnd_configure", "Crytical"))
        self.label_3.setText(_translate("wnd_configure", "Warning"))
        self.label_4.setText(_translate("wnd_configure", "OK"))
        self.pushButton.setText(_translate("wnd_configure", "PushButton"))

