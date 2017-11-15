import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QFileDialog, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import lineAddingSpace
import numChanger
import subAdvance
import subDelay

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Subtitle editor'
        self.left = 50
        self.top = 50

        self.subFileName=''
        self.path=''

        self.positions()
        self.initUI()

    def positions(self):
        self.width = 340
        self.height = 280
        self.leftSideX=20
        self.boxX1=70
        self.boxX2=180

        self.l1=20
        self.l2=70
        self.l3=140
        self.l4=170
        self.l5=220

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.fileSelect = QPushButton('Select Subtitle file', self)
        self.fileSelect.move(self.leftSideX,self.l1)
        self.fileSelect.resize(300,40)
        self.fileSelect.clicked.connect(self.openSubFile)

        fileLabel = QLabel()
        fileLabel.setText("No File Selected")
        fileLabel.move(self.leftSideX,self.l2)

        # Create textbox
        self.textBox_lineNumber = QLineEdit(self)
        self.textBox_lineNumber.move(self.width/2-40, self.l2)
        self.textBox_lineNumber.resize(80,40)
        self.textBox_lineNumber.setText("LINE NUMBER")

        button1 = QPushButton('Add subtitles', self)
        button1.move(self.boxX1,self.l3)
        button1.clicked.connect(self.addsubs)

        button2 = QPushButton('Fix Numbers', self)
        button2.move(self.boxX2,self.l3)
        button2.clicked.connect(self.fixNums)

        # Create textbox
        self.textBox_time = QLineEdit(self)
        self.textBox_time.move(self.width/2-140,self.l4)
        self.textBox_time.resize(280,40)
        self.textBox_time.setText("Time to adjust(Seconds)")

        button3 = QPushButton('Sub Advance', self)
        button3.move(self.boxX1,self.l5)
        button3.clicked.connect(self.advance)

        button4 = QPushButton('Sub Delay', self)
        button4.move(self.boxX2,self.l5)
        button4.clicked.connect(self.delay)

        self.show()

    #Return 0 for fail 1 for path ok 3 for path and line 7 for all
    def validInput(self,n):
        n=int(n)
        o=0

        if(len(self.path)>1):
            o+=1
        else:
            print("Select File")

        if(n>=1):
            if (self.textBox_lineNumber.text().isnumeric()):
                o+=2
            else:
                print("Choose Line number")

        if(n==2):
            if(self.textBox_time.text().isnumeric()):
                o+=4
            else:
                print("Select time in seconds")

        return o

    @pyqtSlot()
    def openSubFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(type(fileName))
            print(fileName)
            nameStart=fileName.rfind('/')
            self.subFileName=fileName[nameStart+1:]
            self.path=fileName[:nameStart]
            self.fileSelect = QPushButton('self.subFileName',self)
            print("path=",self.path)
            print(self.subFileName)

    @pyqtSlot()
    def addsubs(self):
        line = self.textBox_lineNumber.text()
        print(line)
        if(self.validInput(1)>1):
            print("Adding Space for new lines")
            lineAddingSpace.addLine(line,self.path,self.subFileName)

    @pyqtSlot()
    def fixNums(self):
        if(self.validInput(0)>0):
            numChanger.numFixer(self.path,self.subFileName)

    @pyqtSlot()
    def delay(self):
        line=self.textBox_lineNumber.text()
        time=self.textBox_time.text()
        if(self.validInput(2)==7):
            subDelay.advance(line,time,self.path,self.subFileName)
        print('Sub delay selected')

    @pyqtSlot()
    def advance(self):
        line=self.textBox_lineNumber.text()
        time=self.textBox_time.text()
        if(self.validInput(2)==7):
            subAdvance.advance(line,time,self.path,self.subFileName)
        print('Sub Advance selected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
