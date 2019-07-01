# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyReaderMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *

from PyQt5 import QtCore
from ofd_parser import OfdParser

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.filePath = ''
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        fileMenu = QMenu('File', self)

        openAct = QAction('Open...', self)
        openAct.triggered.connect(self.openFile)
        fileMenu.addAction(openAct)

        menubar.addMenu(fileMenu)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 70, 450, 500))
        self.textBrowser.setObjectName("textBrowser")

        # self.textBrowser.setGeometry(QtCore.QRect(150, 70, 401, 341))
        # self.textBrowser

        self.setCentralWidget(self.centralwidget)
        self.setGeometry(300, 50, 600, 650)
        self.setWindowTitle('PyReader')
        self.show()

    def openFile(self):
        self.filePath,fileType = QFileDialog.getOpenFileName(self,'open OFD file','C:/','OFD file(*.ofd)')
        print('filepath: ' + self.filePath)
        ofdParser = OfdParser(self.filePath)
        print(1)











