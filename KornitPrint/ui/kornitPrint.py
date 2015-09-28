# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kornitPrint.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mwKornitPrint(object):
    def setupUi(self, mwKornitPrint):
        mwKornitPrint.setObjectName("mwKornitPrint")
        mwKornitPrint.resize(468, 353)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon/scanner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mwKornitPrint.setWindowIcon(icon)
        mwKornitPrint.setStyleSheet("QGroupBox:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QGroupBox \n"
"{\n"
"   /* background-color: #323232;*/\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 5px; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title \n"
"{\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px ;\n"
"     /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FF0ECE, stop: 1 #FFFFFF);*/\n"
"    \n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-weight:  bold;\n"
"}\n"
"\n"
"\n"
"QToolButton\n"
"{\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mwKornitPrint)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.setObjectName("vBox")
        self.hbTitle = QtWidgets.QHBoxLayout()
        self.hbTitle.setObjectName("hbTitle")
        self.gbLogin = QtWidgets.QGroupBox(self.centralwidget)
        self.gbLogin.setMinimumSize(QtCore.QSize(0, 65))
        self.gbLogin.setMaximumSize(QtCore.QSize(16777215, 65))
        self.gbLogin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gbLogin.setCheckable(False)
        self.gbLogin.setObjectName("gbLogin")
        self.btnSwitchUser = QtWidgets.QToolButton(self.gbLogin)
        self.btnSwitchUser.setGeometry(QtCore.QRect(10, 18, 41, 41))
        self.btnSwitchUser.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icon/switch-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSwitchUser.setIcon(icon1)
        self.btnSwitchUser.setIconSize(QtCore.QSize(30, 30))
        self.btnSwitchUser.setAutoRaise(False)
        self.btnSwitchUser.setObjectName("btnSwitchUser")
        self.lblCurentUser = QtWidgets.QLabel(self.gbLogin)
        self.lblCurentUser.setGeometry(QtCore.QRect(80, 20, 91, 20))
        self.lblCurentUser.setObjectName("lblCurentUser")
        self.lblUser = QtWidgets.QLabel(self.gbLogin)
        self.lblUser.setGeometry(QtCore.QRect(90, 40, 121, 16))
        self.lblUser.setObjectName("lblUser")
        self.hbTitle.addWidget(self.gbLogin)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/icon/pixi_logo_new.png"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label.setObjectName("label")
        self.hbTitle.addWidget(self.label)
        self.hbTitle.setStretch(0, 1)
        self.hbTitle.setStretch(1, 1)
        self.vBox.addLayout(self.hbTitle)
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.setObjectName("hbox")
        self.btnViewNextQueues = QtWidgets.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icon/btn-queue1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnViewNextQueues.setIcon(icon2)
        self.btnViewNextQueues.setIconSize(QtCore.QSize(60, 60))
        self.btnViewNextQueues.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnViewNextQueues.setAutoRaise(True)
        self.btnViewNextQueues.setObjectName("btnViewNextQueues")
        self.hbox.addWidget(self.btnViewNextQueues)
        self.btnLoadQueue = QtWidgets.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icon/load.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLoadQueue.setIcon(icon3)
        self.btnLoadQueue.setIconSize(QtCore.QSize(60, 60))
        self.btnLoadQueue.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnLoadQueue.setAutoRaise(True)
        self.btnLoadQueue.setObjectName("btnLoadQueue")
        self.hbox.addWidget(self.btnLoadQueue)
        self.btnSplitQueue = QtWidgets.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icon/split.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSplitQueue.setIcon(icon4)
        self.btnSplitQueue.setIconSize(QtCore.QSize(60, 60))
        self.btnSplitQueue.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnSplitQueue.setAutoRaise(True)
        self.btnSplitQueue.setObjectName("btnSplitQueue")
        self.hbox.addWidget(self.btnSplitQueue)
        self.btnPullSplit = QtWidgets.QToolButton(self.centralwidget)
        self.btnPullSplit.setToolTipDuration(-1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icon/pull-split.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPullSplit.setIcon(icon5)
        self.btnPullSplit.setIconSize(QtCore.QSize(60, 60))
        self.btnPullSplit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnPullSplit.setAutoRaise(True)
        self.btnPullSplit.setObjectName("btnPullSplit")
        self.hbox.addWidget(self.btnPullSplit)
        self.hbox.setStretch(0, 1)
        self.hbox.setStretch(1, 1)
        self.hbox.setStretch(2, 1)
        self.hbox.setStretch(3, 1)
        self.vBox.addLayout(self.hbox)
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.setObjectName("hbox1")
        self.btnPullQueue = QtWidgets.QToolButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icon/arrow-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPullQueue.setIcon(icon6)
        self.btnPullQueue.setIconSize(QtCore.QSize(60, 60))
        self.btnPullQueue.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnPullQueue.setAutoRaise(True)
        self.btnPullQueue.setObjectName("btnPullQueue")
        self.hbox1.addWidget(self.btnPullQueue)
        self.btnFinishQueue = QtWidgets.QToolButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icon/finish-queue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFinishQueue.setIcon(icon7)
        self.btnFinishQueue.setIconSize(QtCore.QSize(60, 60))
        self.btnFinishQueue.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnFinishQueue.setAutoRaise(True)
        self.btnFinishQueue.setObjectName("btnFinishQueue")
        self.hbox1.addWidget(self.btnFinishQueue)
        self.hbox1.setStretch(0, 1)
        self.hbox1.setStretch(1, 1)
        self.vBox.addLayout(self.hbox1)
        self.vBox.setStretch(0, 1)
        self.vBox.setStretch(1, 1)
        self.vBox.setStretch(2, 1)
        self.verticalLayout.addLayout(self.vBox)
        mwKornitPrint.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mwKornitPrint)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        mwKornitPrint.setMenuBar(self.menubar)

        self.retranslateUi(mwKornitPrint)
        QtCore.QMetaObject.connectSlotsByName(mwKornitPrint)

    def retranslateUi(self, mwKornitPrint):
        _translate = QtCore.QCoreApplication.translate
        mwKornitPrint.setWindowTitle(_translate("mwKornitPrint", "Kornit Printing Utility"))
        self.gbLogin.setTitle(_translate("mwKornitPrint", "Switch Printer User"))
        self.btnSwitchUser.setToolTip(_translate("mwKornitPrint", "Switch Printer User"))
        self.btnSwitchUser.setText(_translate("mwKornitPrint", "..."))
        self.lblCurentUser.setText(_translate("mwKornitPrint", "Current User:"))
        self.lblUser.setText(_translate("mwKornitPrint", "Please log in."))
        self.btnViewNextQueues.setToolTip(_translate("mwKornitPrint", "View next available queue."))
        self.btnViewNextQueues.setText(_translate("mwKornitPrint", "IP View Next \n"
" Available Queue"))
        self.btnLoadQueue.setToolTip(_translate("mwKornitPrint", "Load queue as in progress."))
        self.btnLoadQueue.setText(_translate("mwKornitPrint", "Load Queue"))
        self.btnSplitQueue.setToolTip(_translate("mwKornitPrint", "Split Queue on server."))
        self.btnSplitQueue.setText(_translate("mwKornitPrint", "Split Queue"))
        self.btnPullSplit.setToolTip(_translate("mwKornitPrint", "Pull down split breeze queue."))
        self.btnPullSplit.setText(_translate("mwKornitPrint", "Pull Down \n"
" Split Queue"))
        self.btnPullQueue.setToolTip(_translate("mwKornitPrint", "Pull down entire breeze queue."))
        self.btnPullQueue.setText(_translate("mwKornitPrint", "Pull Down \n"
" Queue"))
        self.btnFinishQueue.setToolTip(_translate("mwKornitPrint", "Set Queue as being printed."))
        self.btnFinishQueue.setText(_translate("mwKornitPrint", "Add To Finished"))

import images_rc
