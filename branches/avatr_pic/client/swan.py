# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Fri Dec  4 00:20:29 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os,sys

class Swan(QtGui.QMainWindow):
    def __init__(self,parent=None):
	QtGui.QWidget.__init__(self,parent)
	self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 501)
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("avatar1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(0, 85, 255);")
	MainWindow.setMaximumSize(QtCore.QSize(377, 495))        
	self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_page = QtGui.QFrame(self.centralwidget)
        self.Main_page.setGeometry(QtCore.QRect(0, 0, 377, 481))
        
        self.Main_page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Main_page.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Main_page.setFrameShadow(QtGui.QFrame.Raised)
        self.Main_page.setObjectName("Main_page")
        self.textBrowser = QtGui.QTextBrowser(self.Main_page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 161, 181))
        self.textBrowser.setStyleSheet("color: rgb(0, 85, 255);")
        self.textBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtGui.QTextBrowser(self.Main_page)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 20, 191, 151))
        self.textBrowser_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.textBrowser_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget = QtGui.QTabWidget(self.Main_page)
        self.tabWidget.setGeometry(QtCore.QRect(20, 220, 341, 251))
        self.tabWidget.setStyleSheet("""selection-background-color: rgb(0, 0, 0);
color: rgb(0, 85, 255);
alternate-background-color: rgb(0, 0, 0);""")
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget = QtGui.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 311, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("""alternate-background-color: rgb(85, 255, 255);
selection-background-color: rgb(0, 85, 255);""")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setBatchSize(200)
        self.listWidget.setObjectName("listWidget")
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(":/main_window/face-smile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #item = QtGui.QListWidgetItem(self.listWidget)
        #item.setIcon(icon)
        #item = QtGui.QListWidgetItem(self.listWidget)
        #item.setIcon(icon)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 96, 101))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(110, 110))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 171, 25))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.lineEdit.setObjectName("lineEdit")
	self.lineEdit.setText(os.getenv("USERNAME"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 60, 53, 15))
        self.label.setObjectName("label")
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 271, 31))
        self.textEdit.setObjectName("textEdit")
	self.textEdit.setText("Set your status message here")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
	self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(210,200,83,27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 53, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 261, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
	
	QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.choose_avatar)	
	
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def choose_avatar(self):
	image_file=open(QtGui.QFileDialog.getOpenFileName(self,"*.jpg","ChooseAvatar").__str__().__str__(),'r')
	avatar=open("avatar.jpg",'w')
	avatar.write(image_file.read())
	avatar.close()
	print "avatar is:",avatar
	image_file.close()
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("avatar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(110, 110))
	
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SWAN Chat", None, QtGui.QApplication.UnicodeUTF8))
	MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Connecting", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/main_window/swan_small.png\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to SWAN Chat!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SWAN is a LAN Chat Client written completely in Python</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The project was inspired by and modeled along the PLC project by Bart Spaans</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        #self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        #self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Chat List", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Change your picture", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Status Message :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Avatar", None,QtGui.QApplication.UnicodeUTF8))
	self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Chat", None, QtGui.QApplication.UnicodeUTF8))
	self.lineEdit_3.setText("2727")        
	self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", "localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Server :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Port : ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

import chat_main_rc
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	cli=Ui_MainWindow()
	cli.show()
	sys.exit(app.exec_())
