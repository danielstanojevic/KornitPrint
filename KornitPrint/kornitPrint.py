import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class KornitPrint(QMainWindow):
    def __init__(self):
        super(KornitPrint, self).__init__()
        
        
        
if "name" == "__main__":
    app = QApplication(sys.argv)
    kp = KornitPrint()
    kp.show()
    sys.exit(app.exec_())