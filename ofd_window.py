# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyReaderMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor

from PyQt5 import QtCore
from ofd_parser import OfdParser


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.filePaths = []
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
        #self.scroll = QScrollArea()
        #self.scroll.verticalScrollBar()
        #self.scroll.setWidget(self.centralwidget)
        #self.vbox = QVBoxLayout()
        
        
        

        self.textBrowser = QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 70, 450, 500))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.verticalScrollBar()
        self.textBrowser.setVerticalScrollBarPolicy(2)
        
            
        # self.textBrowser.setGeometry(QtCore.QRect(150, 70, 401, 341))
        # self.textBrowser

        self.setCentralWidget(self.centralwidget)
        self.setGeometry(300, 50, 600, 650)
        self.setWindowTitle('OFD Parser')
        self.show()

    def openFile(self):
        self.filePaths, _ = QFileDialog.getOpenFileNames(self,'open OFD file','C:/','OFD file(*.ofd)')
        for file_path in self.filePaths:
            self.sendText('filepath: ' + file_path)
            Ofd_Parser = OfdParser(file_path)
            self.Analysis_Of_OFD(Ofd_Parser)
            self.sendText('\n\n')

    def Analysis_Of_OFD(self, Ofd_Parser):
        #OFD
        self.sendText('-' * 46)
        self.sendText(' '*10 + '---Parsing OFD.xml---')
        self.sendText('Versions: {}\nDocType: {}'.format(Ofd_Parser.OFD.get_Version(), Ofd_Parser.OFD.get_DocType()))
        self.sendText('\n')
        
        #Document
        self.sendText('-' * 46)
        self.sendText(' '*10 + '---Parsing Document.xml---')
        self.sendText(('MaxUnitID: {}').format(Ofd_Parser.Document.get_CommonData().get_MaxUnitId()))
        self.sendText('Length of Pages: {}'.format(Ofd_Parser.Document.get_Pages().__len__()))
        self.sendText('\n')
        
        #Pages
        self.sendText('-' * 46)
        self.sendText(' '*10 + '---Parsing Pages---')
        for i in range(len(Ofd_Parser.Pages)):
            self.sendText(('Pages{}' + ' '*4 + 'PageID: {}' + ' '*4 + 'PageRes: {}').format\
                (i+1, Ofd_Parser.Pages[i].get_PageID(), 'None' if Ofd_Parser.Pages[i].get_PageN().\
                    get_select_PageRes() == '' else Ofd_Parser.Pages[i].get_PageN().get_select_PageRes()))
        
        #Res
        self.sendText('-' * 46)
        self.sendText(' '*10 + '---Parsing Res---')
        try:
            for i in range(len(Ofd_Parser.PublicRes.get_Fonts())):
                self.sendText(('ID: {}' + ' '*4 + 'FontName: {}' + ' '*4 +'FamilyName: {}' + ' '*4 + 'FontFile: {}').format(\
                    Ofd_Parser.PublicRes.get_Fonts()[i].get_ID(), Ofd_Parser.PublicRes.get_Fonts()[i].get_FontName(),\
                        Ofd_Parser.PublicRes.get_Fonts()[i].get_select_FamilyName(), Ofd_Parser.PublicRes.get_Fonts()[i].get_select_FontFile()))
        except:
            self.sendText('No PublicRes')
        self.sendText('\n')
        try:
            for i in range(len(Ofd_Parser.DocumentRes.get_MultiMedias())):
                self.sendText(('ID: {}' + ' '*4 + 'Type: {}' +' '*4 + 'MediaFile: {}' + ' '*4 + 'Format: {}').format(\
                    Ofd_Parser.DocumentRes.get_MultiMedias()[i].get_ID(), Ofd_Parser.DocumentRes.get_MultiMedias()[i].get_Type(),\
                        Ofd_Parser.DocumentRes.get_MultiMedias()[i].get_MediaFile(), Ofd_Parser.DocumentRes.get_MultiMedias()[i].get_select_Format()))
        except:
            self.sendText('No DocumentRes')


    def sendText(self, text):
        self.textBrowser.append(text)
        









