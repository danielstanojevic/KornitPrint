import sys, ctypes, webbrowser, os, shutil, socket
import pyodbc
from PyQt5.QtWidgets import (QMainWindow, QApplication, QGroupBox, QWidget, QLabel, QToolButton, QHBoxLayout, QVBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QMessageBox, QSizePolicy,
                             QInputDialog)
from PyQt5.QtGui import QIcon, QFont, QMovie, QPalette
from PyQt5.QtCore import QSize, Qt, pyqtSignal, QThread


class KornitPrint(QMainWindow):
    gbFont = QFont('Helvetica', 12, QFont.Bold)
    lblFont = QFont('Veranda', 10, QFont.Bold)
    
    def __init__(self):
        super(KornitPrint, self).__init__()
        
        self.setWindowTitle("Kornit Printing Utility")
        self.setWindowIcon(QIcon("icon/scanner.png"))
        
        vbMain = QVBoxLayout()
        vbMain.addWidget(self.loginGroup())
        vbMain.addWidget(self.toolButtons())
                
        mainLayout = QWidget()
        mainLayout.setLayout(vbMain)
        
        self.statusBar()
        
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
        btnLogin.setToolTip('Click here to change printer user')
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
        
    def toolButtons(self):
        
        gbTools = QGroupBox()
        gbTools.setFont(self.gbFont)
        
        grdTools = QGridLayout()
        
        btnNextQueue = QToolButton()
        btnNextQueue.setIcon(QIcon("icon/btn-queue1.png"))
        btnNextQueue.setIconSize(QSize(60, 60))
        btnNextQueue.setStatusTip('View next available queue.')
        btnNextQueue.setToolTip('View next available queue')
        btnNextQueue.setAutoRaise(True)
        btnNextQueue.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnNextQueue.setText("IP View next \n available queue")
        btnNextQueue.clicked.connect(self.btnNextQueue_Clicked)    
        grdTools.addWidget(btnNextQueue, 0, 0)
        
        btnLoadQueue = QToolButton()
        btnLoadQueue.setIcon(QIcon("icon/load.png"))
        btnLoadQueue.setIconSize(QSize(60, 60))
        btnLoadQueue.setStatusTip("Load queue as in progress.")
        btnLoadQueue.setToolTip("Load queue as in progress")
        btnLoadQueue.setAutoRaise(True)
        btnLoadQueue.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnLoadQueue.setText("Load Queue")
        btnLoadQueue.clicked.connect(self.btnLoadQueue_Clicked)
        grdTools.addWidget(btnLoadQueue, 0, 1)
        
        btnSplitQueue = QToolButton()
        btnSplitQueue.setIcon(QIcon("icon/split.png"))
        btnSplitQueue.setIconSize(QSize(60, 60))
        btnSplitQueue.setStatusTip("Split Queue on server.")
        btnSplitQueue.setToolTip("Split Queue on server")
        btnSplitQueue.setAutoRaise(True)
        btnSplitQueue.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnSplitQueue.setText("Split Queue")
        btnSplitQueue.clicked.connect(self.btnSplitQueue_Clicked)
        grdTools.addWidget(btnSplitQueue, 0, 2)
        
        btnPullSplit = QToolButton()
        btnPullSplit.setIcon(QIcon("icon/pull-split.png"))
        btnPullSplit.setIconSize(QSize(60, 60))
        btnPullSplit.setStatusTip("Pull down split breeze queue.")
        btnPullSplit.setToolTip("Pull down split breeze queue")
        btnPullSplit.setAutoRaise(True)
        btnPullSplit.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnPullSplit.setText("Pull Down \n Split Queue")
        btnPullSplit.clicked.connect(self.btnPullSplit_Clicked)
        grdTools.addWidget(btnPullSplit, 0, 3)
        
        btnPullQueue = QToolButton()
        btnPullQueue.setIcon(QIcon("icon/arrow-down.png"))
        btnPullQueue.setIconSize(QSize(60, 60))
        btnPullQueue.setStatusTip("Pull down breeze queue.")
        btnPullQueue.setToolTip("Pull down breeze queue")
        btnPullQueue.setAutoRaise(True)
        btnPullQueue.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnPullQueue.setText("Pull Down \n Queue")
        btnPullQueue.clicked.connect(self.btnPullQueue_Clicked)
        grdTools.addWidget(btnPullQueue, 1, 0)
        
        btnFinishQueue = QToolButton()
        btnFinishQueue.setIcon(QIcon("icon/finish-queue.png"))
        btnFinishQueue.setIconSize(QSize(60, 60))
        btnFinishQueue.setStatusTip("Set queue as being printed.")
        btnFinishQueue.setToolTip("Set queue as being printed")
        btnFinishQueue.setAutoRaise(True)
        btnFinishQueue.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFinishQueue.setText("Add to finished")
        btnFinishQueue.clicked.connect(self.btnFinishQueue_Clicked)
        grdTools.addWidget(btnFinishQueue, 1, 1)
        
        gbTools.setLayout(grdTools)
        
        return gbTools    
        
    def btnNextQueue_Clicked(self):
        
        self.myLongTask = TaskThread()
        self.myLongTask.taskFinished.connect(self.reportFinished)
        self.myLoadingMovie = MoviePlayer()   
                
        self.startReport()

    def btnLoadQueue_Clicked(self):
        
        queueNumber, ok = QInputDialog.getText(self, 'Enter Queue', 'Please scan or enter queue:')

        if ok:
            KornitData.insertQueue(self, queueNumber)
            ie = webbrowser.get(webbrowser.iexplore)
            ie.open('http://sqlrptserver/ReportServer_SQLREPORTS/Pages/ReportViewer.aspx?%' + \
                    '2fInkPixi+Reports%2frptQueueExceptions&queue='+  queueNumber  + '&rs:' + \
                     'Command=Render&rc:Parameters=Collapsed&rc:Toolbar=False')         
            
    def btnSplitQueue_Clicked(self):
        self.startSplit = SplitThread()
        self.startSplit.splitFinished.connect(self.splitQueueFinish)
        self.myLoadingMovie = MoviePlayer()
        
        self.splitQueueStart()
        
    def btnPullSplit_Clicked(self):
        mb = QMessageBox()
        ind = QInputDialog()
        
        mb.information(self, "Breeze Software", "Please make sure that you have your Kornit Software open and running.", mb.Ok)
        
        queueNumber, ok = ind.getText(self, "Queue Number", "Please enter queue number.")
        if ok and queueNumber:
            
            firstOrder, ok = ind.getText(self, "Starting Order", "Optional - please enter the beginning order number.")
            if not firstOrder: firstOrder = 1
            
            machineNumber, ok = ind.getInt(self, "Machine Number", "Please enter machine number", 1, 1, 9, 1)
                
            clearHF = mb.question(self, "Hot Folder", "Do you want to clear all the items in the hot folder?", mb.Yes | mb.No, mb.Yes)
            if clearHF == mb.Yes:
                dirPath = "C:/HotFolder"
                fileList = os.listdir(dirPath)
                for filename in fileList:
                    item = os.path.join(dirPath,filename)
                    if os.path.isfile(item): 
                        os.remove(item)         
            
            front = len(str(machineNumber)) + len(str(queueNumber))+2
            back = len(str(firstOrder)) + front

            for file in os.listdir("//qserver/Breeze Artwork Storage/Test"):
                if file[:len(str(machineNumber)+"_"+queueNumber)] == str(machineNumber)+"_"+queueNumber and file[front:-(len(file) - back)] >= str(firstOrder):
                    type = file.split("_")
                
                    queue = type[1]
                    order = type[2]
                    skuName = type[3]
                    db = type[4]
                    sizeGarment = type[5]
                    skuType = type[6]
                    printType = type[7]
                    qty = type[8]
                    pos1 = type[9]
                    ext = type[10]
                    
                    fileName = skuType+"_"+printType+"_"+queue+"."+order+"."+skuName+"."+db+"."+sizeGarment+"."+qty+"_"+qty+"_"+pos1+"_"+ext                    
                    shutil.copy(os.path.join("//qserver/Breeze Artwork Storage/Test", file), os.path.join("c:\HotFolder", fileName))
                    #shutil.copy(os.path.join("//qserver/Breeze Artwork Storage/Test", file), os.path.join("//qserver/BreezeSplitQueues", file))                                        
            
                                        
        elif ok and not queueNumber:
            mb.critical(self, "No Queue Number", "Must enter queue number to continue.")
            if ok == True:
                self.btnPullSplit_Clicked()
            #self.btnPullSplit_Clicked()

    def btnPullQueue_Clicked(self):
        ind = QInputDialog()
        mb = QMessageBox()
        
        queueNumber, ok = ind.getText(self, "Queue Number", "Please enter queue number.")
        if ok and queueNumber:
            
            firstOrder, ok = ind.getText(self, "Starting Order", "Optional - please enter the  beginning order number.")
            if not firstOrder: firstOrder = 1
            
            clearHF = mb.question(self, "Hot Folder", "Do you want to clear all the items in the hot folder?", mb.Yes | mb.No, mb.Yes)
            if clearHF == mb.Yes:
                dirPath = "C:\HotFolder"
                fileList = os.listdir(dirPath)
                for filename in fileList:
                    item = os.path.join(dirPath,filename)
                    if os.path.isfile(item):
                        os.remove(item)
            
            front = len(str(queueNumber))+1
            back = len(str(firstOrder)) + front
                        
            for file in os.listdir("//qserver/Breeze Artwork Storage"):
                if file[:len(queueNumber)] == queueNumber and file[front:-(len(file)-back)] >= str(firstOrder):
                    type = file.split("_")
                
                    queue = type[0]
                    order = type[1]
                    skuName = type[2]
                    db = type[3]
                    sizeGarment = type[4]
                    skuType = type[5]
                    printType = type[6]
                    qty = type[7]
                    pos1 = type[8]
                    ext = type[9]
                    
                    fileName = skuType+"_"+printType+"_"+queue+"."+order+"."+skuName+"."+db+"."+sizeGarment+"."+qty+"_"+qty+"_"+pos1+"_"+ext
                    shutil.copy(os.path.join("//qserver/Breeze Artwork Storage", file), os.path.join("c:\HotFolder", fileName))
                    
    def btnFinishQueue_Clicked(self):
        queueNumber, ok = QInputDialog.getText(self, "Queue Number", "Please enter queue number.")
        if ok and queueNumber:
            KornitData.insertQueuePrinted(self, queueNumber)
            QMessageBox.information(self, "Added", "Queue number " + queueNumber + " has been marked as printed.", QMessageBox.Ok)
        elif ok and not queueNumber:
            QMessageBox.critical(self, "Enter Queue", "Plese enter a queue number.")
            self.btnFinishQueue_Clicked()
        
    def startReport(self): 
        self.myLongTask.start()
        self.setEnabled(False)
        bgColor = QPalette()
        bgColor.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(bgColor)
        self.myLoadingMovie.show()

    def reportFinished(self):
        self.myLoadingMovie.hide()      
        self.nqt = NextQueueTable.createTable(self, self.data)
        self.nqt.show()
        self.nqt.resize(QSize(815, 400))
        self.setPalette(QPalette())        
        self.setEnabled(True)
        
    def splitQueueStart(self):
        queueNumber, ok = QInputDialog.getText(self, 'Split Queue', "Enter Queue to be split.")
        if ok and queueNumber:
            self.queueNumber = queueNumber
            machineNumber, ok = QInputDialog.getInt(self, 'Number of Machines', 'Please enter number of machines (2-9)', 2, 2, 9, 1, )
            if ok and machineNumber:  
                self.machineNumber = machineNumber      
                self.startSplit.start()
                self.myLoadingMovie.show()
                
                self.setEnabled(False)
                bgColor = QPalette()
                bgColor.setColor(self.backgroundRole(), Qt.lightGray)
                self.setPalette(bgColor)
        
    def splitQueueFinish(self):
        self.myLoadingMovie.hide()
        QMessageBox.information(self, "Complete", "Queue has finished splitting", QMessageBox.Ok)       
        self.setPalette(QPalette())        
        self.setEnabled(True)
                
class NextQueueTable(QTableWidget):
    def __init__(self, *args):
        super(NextQueueTable, self).__init__()
        
        self.setWindowTitle("Next Available Queue")
        self.setWindowIcon(QIcon("icon/scanner.png"))
                
        self.createTable()

    def createTable(self, data):
        tblNextQue = QTableWidget()
        #tblNextQue.setMinimumWidth(410)
        #tblNextQue.setMinimumHeight(240)

        tblNextQue.setColumnCount(7)
        tblNextQue.setAlternatingRowColors(True)
        lstHeader = ["Queue Letter", "Description", "Orders", "Queue Date", "Oldest Order Date", "Queue Pulled Date", "Kornit ID"]     
        tblNextQue.setHorizontalHeaderLabels(lstHeader)
        #tblNextQue.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        tblNextQue.setWordWrap(False)
        # Check to make sure the list is there and has data, then we go through it and add data to the table.
        if data:
            tblNextQue.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    #item.setFlags(Qt.ItemIsEditable)
                    if item.text() == "None":
                        item.setText("")
                    tblNextQue.setItem(i, j, item)      
        else:
            tblNextQue.setRowCount(1)
            item = QTableWidgetItem()
            item.setText("Nothing Found")
            tblNextQue.setItem(0, 0, item)
            
        tblNextQue.resizeColumnsToContents()
         
        return tblNextQue
        
class TaskThread(QThread):
    taskFinished = pyqtSignal()
    def run(self):
        self.getData()
        self.taskFinished.emit()

    def getData(self):
        kp.data = KornitData.getNextQueue(self)
        
class SplitThread(QThread):
    splitFinished = pyqtSignal()
    def run(self):
        lsQueue = []
        for file in os.listdir("//qserver/Breeze Artwork Storage"):
            if file[:len(kp.queueNumber)] == kp.queueNumber:
                lsQueue.append(file)
        for i in range(kp.machineNumber):
            for c in lsQueue[i::kp.machineNumber]:
                shutil.copy(os.path.join("//qserver/Breeze Artwork Storage", c), os.path.join("//qserver/Breeze Artwork Storage/Test", str(i + 1)+"_" + c))
        self.splitFinished.emit()
        
class MoviePlayer(QWidget):
    def __init__(self):
        super(MoviePlayer, self).__init__()
        
        self.setAttribute(Qt.WA_TranslucentBackground)        
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.movie = QMovie(self)

        self.movieLabel = QLabel("No movie loaded")
        self.movieLabel.setAlignment(Qt.AlignAbsolute)
        self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.movieLabel)
        self.setLayout(self.mainLayout)
        
        #self.resize(400, 500)

        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName('icon/LoadingCircleTrans.gif')

        pos = kp.pos()

        x = pos.x() - ((self.width()/2) - (kp.width()/2)) +140
        y = pos.y() - ((self.height()/2) - (kp.height()/2)) +180
        
        self.setGeometry(x,y, 400, 500)

        self.movie.start()        

class ConnectDB():        
    def sqlConnect(self, database): 
        try:
            conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=SQLSERVER; DATABASE=' + database + '; Trusted_Connection=yes')
            db = conn.cursor()
        except BaseException as e:
            QMessageBox.critical(kp, 'Database Error', "Can not connect to database: \n" + str(e), QMessageBox.Ok)
        return db  

class KornitData():
    
    def getNextQueue(self):
        db = ConnectDB.sqlConnect(self, "InkPixi")
        db.execute("""EXEC InkPixi.dbo.uspGetIPOldestOpenQueues""")
        ds = db.fetchall()

        return ds
    
    def insertQueue(self, queueNumber):
        try:
            db = ConnectDB.sqlConnect(self, "ImportExport")
            db.execute("INSERT INTO dbo.QueuesBeingProduced (QueueID, [Database], Kornit, [Date Entered]) " + \
                       "SELECT    j.ID, 'I', HOST_NAME(), GETDATE() " + \
                       "FROM    dbo.JobStamps j " + \
                       "WHERE    j.ID = " + queueNumber + \
                       " AND    " + queueNumber + " NOT IN (select QueueID from dbo.QueuesBeingProduced)")
            db.commit()
        except BaseException as e:
            QMessageBox.warning(self, 'Database Error', str(e), QMessageBox.Ok)
            
    def insertQueuePrinted(self, queueNumber):
        db = ConnectDB.sqlConnect(self, "ImportExport")
        db.execute("""INSERT INTO dbo.QueuesPrinted 
                    (QueueID, [Database], Kornit, PrintType, [Date Entered]) 
                    SELECT    js.ID, 'I', HOST_NAME(), 'Breeze', GETDATE() 
                    FROM    dbo.JobStamps js 
                    LEFT JOIN   dbo.QueuesPrinted qp ON js.ID = qp.QueueID 
                    WHERE    js.ID = ?
                       AND    qp.QueueID IS NULL""", (queueNumber))
        db.commit()
        
        
if __name__ == "__main__":
    #For windows 7
    myappid = 'Approval Tool' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
        
    app = QApplication(sys.argv)
    kp = KornitPrint()
    kp.show()
    sys.exit(app.exec_())