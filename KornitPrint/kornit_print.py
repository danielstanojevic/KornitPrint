import sys, webbrowser, os, shutil 
from collections import Counter
from ui import Ui_mwKornitPrint
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSizePolicy, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog,\
    QProgressDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QMovie, QPalette, QIcon, QFont
import pyodbc

class KornitPrint(QMainWindow, Ui_mwKornitPrint):
    def __init__(self):
        super(KornitPrint, self).__init__()
        self.setupUi(self)
        
        self.btnSwitchUser.clicked.connect(self.switch_printer_user)
        self.btnViewNextQueues.clicked.connect(self.view_next_queues)
        self.btnLoadQueue.clicked.connect(self.load_queue)
        self.btnSplitQueue.clicked.connect(self.split_queue)
        self.btnPullSplit.clicked.connect(self.pull_split_queue)
        self.btnPullQueue.clicked.connect(self.pull_queue)
        self.btnFinishQueue.clicked.connect(self.set_queue_printed)
        
        #self.hbTitle.addStretch(1)
        #self.hbox.addStretch(1)
        #self.hbox1.addStretch(1)
        self.vBox.addStretch(1)
        #self.switch_printer_user()
        
    def switch_printer_user(self):
        killAlerts = "killalerts.vbs"
        prn_name, ok = QInputDialog.getText(self, 'Change User', 'Please enter user name:')

        if ok and prn_name:
            if KornitData.check_printer(self, prn_name) > 0:
                self.lblUser.setText(prn_name)
                KornitData.insert_printer(self, prn_name)
                os.startfile(killAlerts)
            else:
                msg = "Please enter your correct user name, which is your first name and last initial. Example: \"brandonc\""
                QMessageBox.warning(self, 'User not found.', msg, QMessageBox.Ok)
        
    def view_next_queues(self):
        
        self.viewQueues = ViewQueues()
        self.viewQueues.taskFinished.connect(self.report_finished)
        self.myLoadingMovie = MoviePlayer()   
                
        self.start_report()   

    def start_report(self): 
        self.viewQueues.start()
        self.setEnabled(False)
        bgColor = QPalette()
        bgColor.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(bgColor)
        self.myLoadingMovie.show()
        
    def report_finished(self):
        self.myLoadingMovie.hide()      
        self.nqt = NextQueueTable.createTable(self, self.data)
        self.nqt.setWindowTitle('Next Available Queues')
        self.nqt.setWindowIcon(QIcon("icon/scanner.ico"))
        self.nqt.show()
        self.nqt.resize(QSize(900, 400))
        self.setPalette(QPalette())        
        self.setEnabled(True)
        
    def load_queue(self):
        
        queueNumber, ok = QInputDialog.getText(self, 'Enter Queue', 'Please scan or enter queue:')
 
        if ok:
            KornitData.insertQueue(self, queueNumber)
            ie = webbrowser.get(webbrowser.iexplore)
            ie.open('http://sqlrptserver/ReportServer_SQLREPORTS/Pages/ReportViewer.aspx?%' + \
                    '2fInkPixi+Reports%2frptQueueExceptions&queue='+  queueNumber  + '&rs:' + \
                     'Command=Render&rc:Parameters=Collapsed&rc:Toolbar=False')                
          
    def split_queue(self):

        queueNumber, ok = QInputDialog.getText(self, 'Split Queue', "Enter Queue to be split.")
        if ok and queueNumber:
            machineNumber, ok = QInputDialog.getInt(self, 'Number of Machines', 'Please enter number of machines (2-9)', 2, 2, 9, 1, )
            if ok and machineNumber:
                
                lsQueue = []
                lstAll = []
                for file in os.listdir("//qserver/Breeze Artwork Storage"):
                    if file[:len(queueNumber)] == queueNumber:
                        lsQueue.append(file)
                
                for file in os.listdir("//qserver/Breeze Artwork Storage"):
                    if file[2:len(queueNumber) +2] == queueNumber:
                        os.remove("//qserver/Breeze Artwork Storage/" + file)
                
                 
                for ordr in lsQueue:
                    qty = ordr.split("_")[7]
                    
                    for i in range(int(qty)):
                        lstAll.append(ordr)

                self.startSplit = SplitThread(machineNumber, queueNumber, lstAll)   
                self.startSplit.copied.connect(self.split_progress)             
                self.startSplit.splitFinished.connect(self.splitQueueFinish)    
                
                self.progressSplt = QProgressDialog('Splitting Queue...', 'Cancel', 0, len(lstAll))
                self.progressSplt.setWindowModality(Qt.WindowModal)
                self.progressSplt.setWindowTitle('Splitting Queues')
                self.progressSplt.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.progressSplt.setWindowIcon(QIcon('icon/scanner.png'))
                self.progressSplt.canceled.connect(self.split_cancel)
                
                self.startSplit.start()
                self.progressSplt.show()
                
                self.setEnabled(False)
                bgColor = QPalette()
                bgColor.setColor(self.backgroundRole(), Qt.lightGray)
                self.setPalette(bgColor)

    def split_progress(self, val):
        self.progressSplt.setValue(val)

    def split_cancel(self):
        
        self.startSplit.terminate()
        self.setPalette(QPalette())        
        self.setEnabled(True)  

    def splitQueueFinish(self):
        self.progressSplt.hide()
        QMessageBox.information(self, "Complete", "Queue has finished splitting", QMessageBox.Ok)       
        self.setPalette(QPalette())        
        self.setEnabled(True)        
                                
    def pull_split_queue(self):
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
            
            QMessageBox.information(self, 'Pulling Down', 'Your queue should show up in QuickP shortly.')            
            
            front = len(str(machineNumber)) + len(str(queueNumber))+2
            back = len(str(firstOrder)) + front
            
            dir_lst = os.listdir("//qserver/Breeze Artwork Storage")
            counts = Counter(dir_lst)
                        
            for file in dir_lst:
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
                    shutil.copy(os.path.join("//qserver/Breeze Artwork Storage", file), os.path.join("c:\HotFolder", fileName))
                    #shutil.copy(os.path.join("//qserver/Breeze Artwork Storage/Test", file), os.path.join("//qserver/BreezeSplitQueues", file))                                        
        elif ok and not queueNumber:
            mb.critical(self, "No Queue Number", "Must enter queue number to continue.")
            if ok == True:
                self.pull_split_queue()
            #self.btnPullSplit_Clicked()
    
    def pull_queue(self):
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
                    
    def set_queue_printed(self):
        queueNumber, ok = QInputDialog.getText(self, "Queue Number", "Please enter queue number.")
        if ok and queueNumber:
            KornitData.insertQueuePrinted(self, queueNumber)
            QMessageBox.information(self, "Added", "Queue number " + queueNumber + " has been marked as printed.", QMessageBox.Ok)
        elif ok and not queueNumber:
            QMessageBox.critical(self, "Enter Queue", "Please enter a queue number.")
            self.set_queue_printed()                    

class ViewQueues(QThread):
    taskFinished = pyqtSignal()
    def run(self):
        self.getData()
        self.taskFinished.emit()

    def getData(self):
        kp.data = KornitData.getNextQueue(self)
        
class SplitThread(QThread):
    splitFinished = pyqtSignal()
    copied = pyqtSignal(int)
    
    def __init__(self, machineNumber, queueNumber, lstQueue):
        super(SplitThread, self).__init__()
        self.machineNumber, self.queueNumber, self.lstQueue = machineNumber, queueNumber, lstQueue
    
    def run(self):
        cnt = 0
        for i in range(self.machineNumber):
            lstMach = self.lstQueue[i::self.machineNumber]
            counts = Counter(lstMach)
            for c in self.lstQueue[i::self.machineNumber]:
                new_qty = counts[c]
                type = c.split("_")
            
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
                us = "_"
                
                file = queue+us+order+us+skuName+us+db+us+sizeGarment+us+skuType+us+printType+us+str(new_qty)+us+pos1+us+ext
                shutil.copy(os.path.join("//qserver/Breeze Artwork Storage", c), os.path.join("//qserver/Breeze Artwork Storage", str(i + 1) + "_" + file))
                cnt += 1
                self.copied.emit(cnt)
                
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
        
class NextQueueTable(QTableWidget):
    def __init__(self, *args):
        super(NextQueueTable, self).__init__()
                
        self.createTable()

    def createTable(self, data):
        tblNextQue = QTableWidget()
        
        h_font = QFont('Seqoe UI', 10, QFont.Bold)
        i_font = QFont('Seqoe UI', 10, QFont.Bold)
        
        tblNextQue.setColumnCount(7)
        tblNextQue.setAlternatingRowColors(True)
        head = tblNextQue.horizontalHeader()
        head.setStretchLastSection(True)
        head.setFont(h_font)
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
                    item.setFont(i_font)
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
        tblNextQue.setWindowIcon(QIcon('icon/scanner.png'))
         
        return tblNextQue    

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
        
    def check_printer(self, printer):
        try:
            db = ConnectDB.sqlConnect(self, 'ImportExport')
            db.execute("SELECT COUNT([User]) AS printer " + \
                       "FROM dbo.PrinterOperators " + \
                       "WHERE [User] = '" + printer + "'")
            ds = db.fetchone()
            prnCount = ds[0]
            
        except BaseException as e:
            prnCount = 0
            QMessageBox.warning(self, 'Database Error', "Problem connecting to database: \n" + str(e), QMessageBox.Ok)
        return prnCount      
    
    def insert_printer(self, printer):
        try:
            db = ConnectDB.sqlConnect(self, 'ImportExport')
            db.execute("INSERT INTO dbo.PrinterOperatorLogins " + \
                       "([User], Machine, LoginTime) " + \
                       "SELECT '" + printer + "',HOST_NAME(), GETDATE()")
            db.commit()
        except BaseException as e:
            QMessageBox.warning(self, 'Database Error', str(e), QMessageBox.Ok)           
        
        
if __name__ == "__main__":
    myappid = 'Kornit Printing Utility'
    #ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
    
    app = QApplication(sys.argv)
    app.setStyle("plastique")
    kp = KornitPrint()
    kp.show()
    
    sys.exit(app.exec_())    