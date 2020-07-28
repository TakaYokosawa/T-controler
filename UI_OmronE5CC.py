# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_OmronE5CC.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OmronMainWindow(object):
    def setupUi(self, OmronMainWindow):
        OmronMainWindow.setObjectName("OmronMainWindow")
        OmronMainWindow.resize(475, 440)
        font = QtGui.QFont()
        font.setPointSize(16)
        OmronMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(OmronMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 60, 341, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Timer_control = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.Timer_control.setEnabled(True)
        self.Timer_control.setWrapping(False)
        self.Timer_control.setFrame(False)
        self.Timer_control.setReadOnly(False)
        self.Timer_control.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.Timer_control.setTime(QtCore.QTime(3, 0, 0))
        self.Timer_control.setObjectName("Timer_control")
        self.verticalLayout_4.addWidget(self.Timer_control)
        self.Timer_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Timer_button.setFont(font)
        self.Timer_button.setCheckable(True)
        self.Timer_button.setObjectName("Timer_button")
        self.verticalLayout_4.addWidget(self.Timer_button)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 1, 1, 1)
        self.Power_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Power_button.setFont(font)
        self.Power_button.setCheckable(True)
        self.Power_button.setObjectName("Power_button")
        self.gridLayout.addWidget(self.Power_button, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.PV_indicator = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.PV_indicator.setFont(font)
        self.PV_indicator.setStyleSheet("QLCDNumber{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.PV_indicator.setFrameShape(QtWidgets.QFrame.Box)
        self.PV_indicator.setSmallDecimalPoint(True)
        self.PV_indicator.setDigitCount(4)
        self.PV_indicator.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.PV_indicator.setObjectName("PV_indicator")
        self.gridLayout.addWidget(self.PV_indicator, 0, 1, 1, 1)
        self.SetPoint_control = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SetPoint_control.setFont(font)
        self.SetPoint_control.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SetPoint_control.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SetPoint_control.setDecimals(1)
        self.SetPoint_control.setMaximum(200.0)
        self.SetPoint_control.setSingleStep(0.1)
        self.SetPoint_control.setObjectName("SetPoint_control")
        self.gridLayout.addWidget(self.SetPoint_control, 2, 1, 1, 1)
        self.SetPoint_indicator = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.SetPoint_indicator.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SetPoint_indicator.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 255, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.SetPoint_indicator.setSmallDecimalPoint(True)
        self.SetPoint_indicator.setDigitCount(4)
        self.SetPoint_indicator.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.SetPoint_indicator.setProperty("value", 0.0)
        self.SetPoint_indicator.setObjectName("SetPoint_indicator")
        self.gridLayout.addWidget(self.SetPoint_indicator, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.RampRate_control = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.RampRate_control.setFont(font)
        self.RampRate_control.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RampRate_control.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RampRate_control.setDecimals(1)
        self.RampRate_control.setMaximum(200.0)
        self.RampRate_control.setSingleStep(0.1)
        self.RampRate_control.setProperty("value", 5.0)
        self.RampRate_control.setObjectName("RampRate_control")
        self.gridLayout.addWidget(self.RampRate_control, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(1, 4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        OmronMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OmronMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 43))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        OmronMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OmronMainWindow)
        self.statusbar.setObjectName("statusbar")
        OmronMainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Hardware = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Hardware.setObjectName("actionAbout_Hardware")
        self.actionAbout_Heater = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Heater.setObjectName("actionAbout_Heater")
        self.actionAbout_Thermo_Couple = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Thermo_Couple.setObjectName("actionAbout_Thermo_Couple")
        self.actionAbout_Solid_State_Relay = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Solid_State_Relay.setObjectName("actionAbout_Solid_State_Relay")
        self.actionAbout_Communication = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Communication.setObjectName("actionAbout_Communication")
        self.actionAbout_Fuse = QtWidgets.QAction(OmronMainWindow)
        self.actionAbout_Fuse.setObjectName("actionAbout_Fuse")
        self.menuHelp.addAction(self.actionAbout_Hardware)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(OmronMainWindow)
        QtCore.QMetaObject.connectSlotsByName(OmronMainWindow)

    def retranslateUi(self, OmronMainWindow):
        _translate = QtCore.QCoreApplication.translate
        OmronMainWindow.setWindowTitle(_translate("OmronMainWindow", "Omron Temperature Controller"))
        self.label.setText(_translate("OmronMainWindow", "PV"))
        self.Timer_control.setDisplayFormat(_translate("OmronMainWindow", "H:mm:ss"))
        self.Timer_button.setText(_translate("OmronMainWindow", "Start / Stop"))
        self.Power_button.setText(_translate("OmronMainWindow", "ON / OFF"))
        self.label_2.setText(_translate("OmronMainWindow", "SetPoint"))
        self.label_3.setText(_translate("OmronMainWindow", "SP Control"))
        self.label_5.setText(_translate("OmronMainWindow", "Ramp Rate"))
        self.label_4.setText(_translate("OmronMainWindow", "Omron Temerature Controller"))
        self.menuHelp.setTitle(_translate("OmronMainWindow", "Help"))
        self.actionAbout_Hardware.setText(_translate("OmronMainWindow", "About Hardware"))
        self.actionAbout_Heater.setText(_translate("OmronMainWindow", "About Heater"))
        self.actionAbout_Thermo_Couple.setText(_translate("OmronMainWindow", "About Thermo Couple"))
        self.actionAbout_Solid_State_Relay.setText(_translate("OmronMainWindow", "About Solid State Relay"))
        self.actionAbout_Communication.setText(_translate("OmronMainWindow", "About Communication"))
        self.actionAbout_Fuse.setText(_translate("OmronMainWindow", "About Fuse"))
