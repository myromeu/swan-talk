# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talk.ui'
#
# Created: Fri Dec  4 00:31:12 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
from twisted.internet.protocol import Protocol, ClientFactory
import qt4reactor

class Talk_Page(QtGui.QMainWindow):
    def __init__(self,trns,parent=None):
	QtGui.QWidget.__init__(self,parent)
	self.setupUi(self,trns)
	
    def setupUi(self,MainWindow,trans):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 501)
	self.trns=trans
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 381, 481))
        self.tabWidget.setStyleSheet("color: rgb(0, 85, 255);")
        self.tabWidget.setObjectName("tabWidget")
	self.tabWidget.setTabsClosable(True)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 361, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(0, 400, 361, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 380, 100, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
	#QtCore.QObject.connect(self.lineEdit,QtCore.SIGNAL("returnPressed()"),self.entr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self,e):
	self.trns.write("lost")	   


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Talk Page", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Your Message :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "CommonRoom", None, QtGui.QApplication.UnicodeUTF8))

import chat_main_rc
