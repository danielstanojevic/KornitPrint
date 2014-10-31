import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGroupBox, QWidget, QLabel, QToolButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt

class KornitPrint(QMainWindow):
    gbFont = QFont('Helvetica', 12, QFont.Bold)
    lblFont = QFont('Veranda', 10, QFont.Bold)
    
    def __init__(self):
        super(KornitPrint, self).__init__()
        
        self.setWindowTitle("Kornit Printing Utility")
        self.setWindowIcon(QIcon("icon/scanner.png"))
        
        vbMain = QVBoxLayout()
        vbMain.addWidget(self.loginGroup())
                
        mainLayout = QWidget()
        mainLayout.setLayout(vbMain)

        self.setCentralWidget(mainLayout)
        
    def loginGroup(self):

        groupBox = QGroupBox("Switch Printer User")
        groupBox.setFont(self.gbFont)

        lblCurrentUser = QLabel('Current User:', self)
        lblCurrentUser.setFont(self.lblFont)
        lblCurrentUser.setAlignment(Qt.AlignBottom)

        self.lblUser = QLabel()
        self.lblUser.setFont(QFont(self.lblFont))
        self.lblUser.setAlignment(Qt.AlignBottom)

        #Another button, this one switches printer login in.
        btnLogin = QToolButton(self)
        btnLogin.setIcon(QIcon("icon/switch-user.png"))
        btnLogin.setIconSize(QSize(30, 30))
        btnLogin.setStatusTip('Click here to change printer user.')
        btnLogin.setToolTip('Click here to change printer user.')
        btnLogin.clicked.connect(self.btnLogin_Clicked)

        hbox = QHBoxLayout()
        hbox.addWidget(btnLogin)
        hbox.addWidget(lblCurrentUser)
        hbox.addWidget(self.lblUser)
        hbox.addStretch(1)
        hbox.setAlignment(self, Qt.AlignCenter)
        
        groupBox.setLayout(hbox)
        groupBox.setMaximumWidth(250)
        groupBox.setMinimumWidth(250)
        groupBox.setMaximumHeight(125)

        return groupBox
    
    def btnLogin_Clicked(self):
        print("Clicked")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    kp = KornitPrint()
    kp.show()
    sys.exit(app.exec_())