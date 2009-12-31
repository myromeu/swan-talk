from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout
from PyQt4 import QtCore, QtGui
from talk import *
import qt4reactor
from swan import*

app=QtGui.QApplication(['swan'])
GUI=Swan()
GUI.show()
reactor=qt4reactor.install()
talk_list={}  
GUI.pushButton_3.setEnabled(False)

class Echo(Protocol):						##to build protocol

   def dataReceived(self, data):				##called when data is received
	print "data",data
	packet=data.split(">>:")
	if packet[0]=="populate_list":
		packet.remove('populate_list')			##remove "populate_list" to get user names
		GUI.listWidget.clear()
		j=0
		print packet
		for i in packet:
			username=i
			print i
	      		item = QtGui.QListWidgetItem(GUI.listWidget)
        		GUI.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", username, None, QtGui.QApplication.UnicodeUTF8))
			j=j+1
	elif packet[0]=="chat":
		if packet[2] not in talk_list:			##if user not in user_list
			current_index=packet[2]			##current_index set to user name
			tab = QtGui.QWidget()
        		tab.setObjectName("tab"+packet[2])
        		textBrowser = QtGui.QTextBrowser(tab)
	    		textBrowser.setGeometry(QtCore.QRect(0, 10, 361, 351))
        		textBrowser.setObjectName("textBrowser"+packet[2])
        		lineEdit = QtGui.QLineEdit(tab)
        		lineEdit.setGeometry(QtCore.QRect(0, 400, 361, 41))
        		lineEdit.setObjectName("lineEdit"+packet[2])
        		label = QtGui.QLabel(tab)
        		label.setGeometry(QtCore.QRect(10, 380, 91, 16))
        		label.setObjectName("label"+packet[2])
        		talk_page.tabWidget.addTab(tab, "")
			label.setText(QtGui.QApplication.translate("MainWindow", "Your Message :", None, QtGui.QApplication.UnicodeUTF8))
        		talk_page.tabWidget.setTabText(talk_page.tabWidget.indexOf(tab), QtGui.QApplication.translate("MainWindow", packet[2], None, QtGui.QApplication.UnicodeUTF8))
			QtCore.QObject.connect(lineEdit,QtCore.SIGNAL("returnPressed()"),Send_Chat)
			talk_list[packet[2]]=(textBrowser,lineEdit)
		talk_list[packet[2]][0].append(packet[3]+": "+packet[1])	
  
	
class EchoClientFactory(ClientFactory):

    def startedConnecting(self, connector):
        GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", "Started to connect.", None, QtGui.QApplication.UnicodeUTF8))
    
    def buildProtocol(self, addr):				##to set protocol as Echo
        print 'Connected.'
	GUI.pushButton_3.setEnabled(True)
	GUI.pushButton_2.setEnabled(False)
        return Echo()
    
    def clientConnectionLost(self, connector, reason):		##executed when loseConnection() is called
	global talk_page
	GUI.pushButton_3.setEnabled(False)
	GUI.pushButton_2.setEnabled(True)
	try:
		talk_page.hide()
	except:
		pass     
	GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Lost connection.', None, QtGui.QApplication.UnicodeUTF8))
  
    def clientConnectionFailed(self, connector, reason):
	 global talk_page
	 GUI.pushButton_3.setEnabled(False)
	 GUI.pushButton_2.setEnabled(True)
	 try:
		talk_page.hide()
	 except:
		pass      
	 GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Connection Failed, Retry', None, QtGui.QApplication.UnicodeUTF8))

def Send_Details():						##called when chat button is clicked
	global connection,talk_page,talk_list,current_index
	print GUI.lineEdit.text().__str__().__str__()
	print "hello"
	if (GUI.lineEdit.text().__str__().__str__()!=''):
		data="user_details>>:"+GUI.lineEdit.text().__str__().__str__()+">>:"+GUI.lineEdit_4.text().__str__().__str__()
		print data		
		connection.transport.write(data)
		talk_page=Talk_Page(connection.transport,GUI)
		talk_page.show()
		talk_list={}
		talk_list['CommonRoom']=(talk_page.textBrowser,talk_page.lineEdit)
		current_index="CommonRoom"
		QtCore.QObject.connect(talk_page.tabWidget,QtCore.SIGNAL("selected(QString)"),Change_Talk)
		QtCore.QObject.connect(talk_page.tabWidget,QtCore.SIGNAL("tabCloseRequested(int)"),Close)
		QtCore.QObject.connect(talk_page.lineEdit,QtCore.SIGNAL("returnPressed()"),Send_Chat)
		GUI.lineEdit.setEnabled(False)
		GUI.pushButton_2.setEnabled(False)
		GUI.pushButton_3.setEnabled(False)
	else:
		GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Enter your username.', None, QtGui.QApplication.UnicodeUTF8))

def Connect():							##called when connect button is clicked
	global connection
	connection=reactor.connectTCP(GUI.lineEdit_2.text().__str__().__str__(),int(GUI.lineEdit_3.text().__str__().__str__()) , EchoClientFactory()) ##listenTCP and connectTCP,to set defaults for all connections coming from that accept() or connect()
	GUI.lineEdit_3.setEnabled(False)
	GUI.lineEdit_2.setEnabled(False)
	GUI.lineEdit.setEnabled(True)				##to connect again from the same window if the user is already logged in

def Close(index):
	global talk_page,talk_list
	text=talk_page.tabWidget.tabText (index)
	talk_page.tabWidget.removeTab(index)
	talk_list.__delitem__(text.__str__().__str__())                                  

def Change_Talk(item):						##to select particular tab for private chat
	global current_index
	current_index=item.__str__().__str__()

def New_Talk(item):						##to get a new tab when user name is double clicked for private chat
	username=item.text().__str__().__str__()
	if username not in talk_list:	
		tab = QtGui.QWidget()
        	tab.setObjectName("tab"+username)
        	textBrowser = QtGui.QTextBrowser(tab)
        	textBrowser.setGeometry(QtCore.QRect(0, 10, 361, 351))
       		textBrowser.setObjectName("textBrowser"+username)
        	lineEdit = QtGui.QLineEdit(tab)
        	lineEdit.setGeometry(QtCore.QRect(0, 400, 361, 41))
        	lineEdit.setObjectName("lineEdit"+username)
        	label = QtGui.QLabel(tab)
        	label.setGeometry(QtCore.QRect(10, 380, 91, 16))
        	label.setObjectName("label"+username)
        	talk_page.tabWidget.addTab(tab, "")
		label.setText(QtGui.QApplication.translate("MainWindow", "Your Message :", None, QtGui.QApplication.UnicodeUTF8))
        	talk_page.tabWidget.setTabText(talk_page.tabWidget.indexOf(tab), QtGui.QApplication.translate("MainWindow", username, None, 		QtGui.QApplication.UnicodeUTF8))
		QtCore.QObject.connect(lineEdit,QtCore.SIGNAL("returnPressed()"),Send_Chat)
		talk_list[username]=(textBrowser,lineEdit)

def Send_Chat():						##called when returnpressed in lineEdit of talk_Page
	global connection,talk_list
	if current_index != "CommonRoom":
		talk_list[current_index][0].append(GUI.lineEdit.text().__str__().__str__()+": "+talk_list[current_index][1].text().__str__().__str__()) ##textBrowser(current_index[0]) is given username:content in  lineEdit(current_index[1])
	connection.transport.write("chat>>:"+talk_list[current_index][1].text().__str__().__str__()+">>:"+current_index) ##for public chat "chat>>:contents of lineEdit>>:CommonRoom" is transported
	talk_list[current_index][1].clear()

current_index='CommonRoom'
QtCore.QObject.connect(GUI.pushButton_3,QtCore.SIGNAL("clicked()"),Send_Details)
QtCore.QObject.connect(GUI.pushButton_2,QtCore.SIGNAL("clicked()"),Connect)
QtCore.QObject.connect(GUI.listWidget,QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"),New_Talk)
reactor.runReturn()						##reactor will run until Ctrl_C is pressed
sys.exit(app.exec_())
