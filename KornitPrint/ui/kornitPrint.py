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
        mwKornitPrint.resize(458, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon/scanner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mwKornitPrint.setWindowIcon(icon)
        mwKornitPrint.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 25;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #d7801a;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(image/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QGroupBox {\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;        \n"
"    \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(image/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QProgressDialog\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressDialog::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(image/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}            \n"
"\n"
"QToolButton\n"
"{\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-weight: bold;    \n"
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
        icon2.addPixmap(QtGui.QPixmap(":/images/icon/btn-queue2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.btnKillArtwork = QtWidgets.QToolButton(self.centralwidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icon/kill-art.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnKillArtwork.setIcon(icon8)
        self.btnKillArtwork.setIconSize(QtCore.QSize(60, 60))
        self.btnKillArtwork.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnKillArtwork.setAutoRaise(True)
        self.btnKillArtwork.setObjectName("btnKillArtwork")
        self.hbox1.addWidget(self.btnKillArtwork)
        self.btnPullSource = QtWidgets.QToolButton(self.centralwidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icon/print-source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPullSource.setIcon(icon9)
        self.btnPullSource.setIconSize(QtCore.QSize(60, 60))
        self.btnPullSource.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnPullSource.setAutoRaise(True)
        self.btnPullSource.setObjectName("btnPullSource")
        self.hbox1.addWidget(self.btnPullSource)
        self.hbox1.setStretch(0, 1)
        self.hbox1.setStretch(1, 1)
        self.vBox.addLayout(self.hbox1)
        self.vBox.setStretch(0, 1)
        self.vBox.setStretch(1, 1)
        self.vBox.setStretch(2, 1)
        self.verticalLayout.addLayout(self.vBox)
        mwKornitPrint.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mwKornitPrint)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
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
        self.btnKillArtwork.setToolTip(_translate("mwKornitPrint", "Add artwork to kill list to be rerun on server."))
        self.btnKillArtwork.setText(_translate("mwKornitPrint", "Kill Artwork"))
        self.btnPullSource.setToolTip(_translate("mwKornitPrint", "Pull artwork from source on art server."))
        self.btnPullSource.setText(_translate("mwKornitPrint", "Pull From\n"
"Source"))

import images_rc
