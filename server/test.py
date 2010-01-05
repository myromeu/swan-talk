# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servercaht.ui'
#
# Created: Tue Dec  8 12:03:52 2009
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Swan_Server(QtGui.QMainWindow):
    def __init__(self,parent=None):
	QtGui.QWidget.__init__(self,parent)
	self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646,390)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10,310,201,23))
        self.lineEdit.setStyleSheet("""border-color: rgb(0, 85, 255);
color: rgb(255, 85, 0);""")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10,280,57,17))
        self.label.setStyleSheet("color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
	self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10,330,200,17))
        self.label_3.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_3.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(230,10,401,331))
        self.groupBox.setStyleSheet("color: rgb(0, 85, 255);")
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_2 = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser_2.setGeometry(QtCore.QRect(10,30,381,291))
        self.textBrowser_2.setStyleSheet("color: rgb(255, 85, 0);")
        self.textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_2.setLineWidth(0)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10,10,211,191))
        self.textBrowser.setStyleSheet("color: rgb(255, 85, 0);")
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10,250,201,23))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 85, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10,230,131,17))
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
	self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 340, 50, 27))
	self.pushButton.setStyleSheet("color: rgb(255, 85, 0);")        
	self.pushButton.setObjectName("pushButton")
	MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SWAN Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Port :", None, QtGui.QApplication.UnicodeUTF8))
	#self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Press enter to start server", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/main_window/swan_small.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                  Server Running ....</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", "14", None, QtGui.QApplication.UnicodeUTF8))
	self.lineEdit.setText("2727")
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "No of Connections :", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton.setText(QtGui.QApplication.translate("MainWindow","Start", None, QtGui.QApplication.UnicodeUTF8))

import chat_main_rc
