from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout
from PyQt4 import QtCore, QtGui
from talk import *
import qt4reactor
import Image
from swan import*
import smileys_rc
import eastereggs_rc
app=QtGui.QApplication(['swan'])
GUI=Swan()
GUI.show()
reactor=qt4reactor.install()
talk_list={}  
GUI.pushButton_3.setEnabled(False)
chat=0
suser=[]

def smilies(browser,packet):
	convers=packet[1].split(":)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/sm1.jpg\" />"+convers[i]
	else :
		string=packet[1]
	convers=string.split(":D")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/sm2.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split("sharingan")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/eastereggs/Desktop/sharingan.jpeg\" />"+convers[i]
	else :
		pass
	
	convers=string.split(":-D")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/sm3.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":P")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/sm6.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":(")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/sm8.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(";)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(">-)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley10.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(";D")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley11.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":O")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley12.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":|")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley13.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":-S")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley14.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":-|")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley15.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split("|-)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley5.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(">D")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley7.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split("B-)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/smiley9.jpg\" />"+convers[i]
	else :
		pass
	convers=string.split(":03")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/108.png\" />"+convers[i]
	else :
		pass
	convers=string.split(":bz")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/115.png\" />"+convers[i]
	else :
		pass
	convers=string.split(">)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/16.png\" />"+convers[i]
	else :
		pass
		
	convers=string.split(":o)")
	if convers.__len__()>1:
		string=convers[0]
		for i in range(1,convers.__len__()):
			string=string+"<img src=\":/newPrefix/29.png\" />"+convers[i]
	else :
		pass
	
	browser.append(packet[3]+": "+string)




class Echo(Protocol):							##to build protocol
  
   
   def dataReceived(self, data):					##called when data is received
	global packet,talk_list
	packet=data.split(">>:")
	
	

	if packet[0]=="change_list":
		for i in xrange(GUI.listWidget.count()):
			token=""
			try:
				token=GUI.listWidget.item(i).text().__str__().__str__()
			except:
				pass
			if token==packet[1]:
				GUI.listWidget.item(i).setToolTip(QtGui.QApplication.translate("MainWindow", packet[2], None,QtGui.QApplication.UnicodeUTF8))
				h = open(".temp/"+packet[1]+"av.png", "wb")
				h.write(packet[3])
				h.close()
				icon = QtGui.QIcon()
        			icon.addPixmap(QtGui.QPixmap(".temp/"+packet[1]+"av.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				GUI.listWidget.item(i).setIcon(icon)
	elif packet[0]=="new_user":
		j1=GUI.listWidget.count()
		item = QtGui.QListWidgetItem(GUI.listWidget)
        	GUI.listWidget.item(j1).setText(QtGui.QApplication.translate("MainWindow", packet[1], None, QtGui.QApplication.UnicodeUTF8))
		GUI.listWidget.item(j1).setToolTip(QtGui.QApplication.translate("MainWindow", packet[2], None, QtGui.QApplication.UnicodeUTF8))
		h = open(".temp/"+packet[1]+"av.png", "wb")
		h.write(packet[3])
		h.close()
		icon = QtGui.QIcon()
        	icon.addPixmap(QtGui.QPixmap(".temp/"+packet[1]+"av.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		GUI.listWidget.item(j1).setIcon(icon)
		
	elif packet[0]=="remove_my_list":
		for i in xrange(GUI.listWidget.count()):
			token=""
			try:
				token=GUI.listWidget.item(i).text().__str__().__str__()
			except:
				pass
			if token==packet[1]:
				GUI.listWidget.takeItem(i)
		expireduname=packet[1]
		talk_list['CommonRoom'][0].append(expireduname+" has logged out")
		#displaying logout message in corresponding tab
		for k in talk_list:
			if k==expireduname:
				print k,"logout"
				talk_list[k][0].append(k+" has logged out")
					
		
	elif packet[0]=="populate_list":

		packet.remove('populate_list')				##remove "populate_list" to get user names
		GUI.listWidget.clear()
		global j		
		j=0
		#smsg=[]
		global suser
		suser=[]
		#spic=[]
		print "packet length",packet.__len__()
		for i in packet:
			tr=i.split(">>>>")
			username=tr[0]
			pic=tr[2]
			print tr[0],tr[1]
			suser.append(username)
			trr=tr[1].split("><:")
	      		item = QtGui.QListWidgetItem(GUI.listWidget)
        		GUI.listWidget.item(j).setText(QtGui.QApplication.translate("MainWindow", username, None, QtGui.QApplication.UnicodeUTF8))
			GUI.listWidget.item(j).setToolTip(QtGui.QApplication.translate("MainWindow", trr[0], None, QtGui.QApplication.UnicodeUTF8))
			h = open(".temp/"+username+"av.png", "wb")
			h.write(pic)
			h.close()
			icon = QtGui.QIcon()
        		icon.addPixmap(QtGui.QPixmap(".temp/"+username+"av.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			GUI.listWidget.item(j).setIcon(icon)

                        j=j+1
		
		GUI.tabWidget.setCurrentIndex(0)
		#displaying logout message in commonroom
		
				
		#making status message as tooltip for sorted chatlist
				
		'''for m in smsg:	
			l=0
			for i in suser:
				
				if GUI.listWidget.item(k).text()==suser[l]:
					GUI.listWidget.item(k).setToolTip(QtGui.QApplication.translate("MainWindow", smsg[l], None, QtGui.QApplication.UnicodeUTF8))
					#h = open(username+"av.png", "w")
					#h.write(spic[l])
					#h.close()
					#icon = QtGui.QIcon()
        				#icon.addPixmap(QtGui.QPixmap(username+"av.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
					#GUI.listWidget.item(k).setIcon(icon)
				l=l+1
			k=k+1'''		
	elif packet[0]=="chat":
		   
		
		
		if packet[2] not in talk_list:				##if user not in user_list
			current_index=packet[2]				##current_index set to user name
			tab = QtGui.QWidget()
        		tab.setObjectName("tab"+packet[2])
        		textBrowser = QtGui.QTextBrowser(tab)
	    		textBrowser.setGeometry(QtCore.QRect(0, 10, 361, 351))
        		textBrowser.setObjectName("textBrowser"+packet[2])
        		lineEdit = QtGui.QLineEdit(tab)
        		lineEdit.setGeometry(QtCore.QRect(0, 400, 361, 41))
        		lineEdit.setObjectName("lineEdit"+packet[2])
        		label = QtGui.QLabel(tab)
        		label.setGeometry(QtCore.QRect(10, 380, 100, 16))
        		label.setObjectName("label"+packet[2])
        		talk_page.tabWidget.addTab(tab, "")
			label.setText(QtGui.QApplication.translate("MainWindow", "Your Message :", None, QtGui.QApplication.UnicodeUTF8))
        		talk_page.tabWidget.setTabText(talk_page.tabWidget.indexOf(tab), QtGui.QApplication.translate("MainWindow", packet[2], None, QtGui.QApplication.UnicodeUTF8))
			QtCore.QObject.connect(lineEdit,QtCore.SIGNAL("returnPressed()"),Send_Chat)
			talk_list[packet[2]]=(textBrowser,lineEdit)
			
		global smilies	
		smilies(talk_list[packet[2]][0],packet) 		##to display user name:data in CommonRoom textBrowser
		
        elif packet[0]=="Already existing user":
		global talk_page
		GUI.pushButton_3.setEnabled(True)
		GUI.lineEdit.setEnabled(True)
		#GUI.pushButton_2.setEnabled(True)
		try:
			talk_page.destroy()
		except:
			pass     
		GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", "Change your username.", None, QtGui.QApplication.UnicodeUTF8))
	else:
		pass	
	
class EchoClientFactory(ClientFactory):

    def startedConnecting(self, connector):
        GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", "Started to connect.", None, QtGui.QApplication.UnicodeUTF8))
    
    def buildProtocol(self, addr):					##to set protocol as Echo
       
	GUI.pushButton_3.setEnabled(True)
	GUI.pushButton_2.setEnabled(False)
        return Echo()
    
    def clientConnectionLost(self, connector, reason):			##executed when loseConnection() is called
	global talk_page
	GUI.pushButton_3.setEnabled(False)
	GUI.pushButton_2.setEnabled(True)
	try:
		talk_page.destroy()
	except:
		pass     
	GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Lost connection.', None, QtGui.QApplication.UnicodeUTF8))
  
    def clientConnectionFailed(self, connector, reason):
	 global talk_page
	 GUI.pushButton_3.setEnabled(False)
	 GUI.pushButton_2.setEnabled(True)
	 try:
		talk_page.destroy()
	 except:
		pass      
	 GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Connection Failed, Retry', None, QtGui.QApplication.UnicodeUTF8))

def Send_Details():							##called when chat button is clicked
	global connection,talk_page,talk_list,current_index,chat
	f = Image.open(".temp/avatar.png")
	size=f.resize((30,30))
	size.save(".temp/avat.png","png")
	h=open(".temp/avat.png","rb")
	contents=h.read()
	h.close()
	
	if (GUI.lineEdit.text().__str__().__str__()!=''):
		stat=GUI.lineEdit_4.text().__str__().__str__()
		if stat=="Set your status message here":
			stat="Available"
		data="user_details>>:"+GUI.lineEdit.text().__str__().__str__()+">>:"+stat+">>:"+contents
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
		chat=1
	else:
		GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", 'Enter your username.', None, QtGui.QApplication.UnicodeUTF8))

def Connect():								##called when connect button is clicked
	global connection
	GUI.listWidget.clear()
	connection=reactor.connectTCP(GUI.lineEdit_2.text().__str__().__str__(),int(GUI.lineEdit_3.text().__str__().__str__()) , EchoClientFactory()) ##listenTCP and connectTCP,to set defaults for all connections coming from that accept() or connect()
	GUI.lineEdit_3.setEnabled(False)
	GUI.lineEdit_2.setEnabled(False)
	GUI.lineEdit.setEnabled(True)					##to connect again from the same window if the user is already logged in
	GUI.tabWidget.setCurrentIndex(1)
	GUI.setStatusTip(QtGui.QApplication.translate("MainWindow", "Connected", None, QtGui.QApplication.UnicodeUTF8))
def Close(index):
	global talk_page,talk_list
	text=talk_page.tabWidget.tabText (index)
	talk_page.tabWidget.removeTab(index)
	talk_list.__delitem__(text.__str__().__str__())                                  

def Change_Talk(item):							##to select particular tab for private chat
	global current_index
	current_index=item.__str__().__str__()

def New_Talk(item):							##to get a new tab when user name is double clicked for private chat
	
	username=item.text().__str__().__str__().split("(")[0]
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
        	label.setGeometry(QtCore.QRect(10, 380, 100, 16))
        	label.setObjectName("label"+username)
        	talk_page.tabWidget.addTab(tab, "")
		label.setText(QtGui.QApplication.translate("MainWindow", "Your Message :", None, QtGui.QApplication.UnicodeUTF8))
        	talk_page.tabWidget.setTabText(talk_page.tabWidget.indexOf(tab), QtGui.QApplication.translate("MainWindow", username, None, 		QtGui.QApplication.UnicodeUTF8))
		
		QtCore.QObject.connect(lineEdit,QtCore.SIGNAL("returnPressed()"),Send_Chat)
		talk_list[username]=(textBrowser,lineEdit)

def help():
	talk_list[current_index][0].append("/clear	-to clear the talk page")
	talk_list[current_index][0].append("/status	-to change status message (/status:message)")
	talk_list[current_index][0].append("/log	-to save the chat ")
	talk_list[current_index][0].append("/users	-to display logged in users")
	talk_list[current_index][1].clear()


def Send_Chat():							##called when returnpressed in lineEdit of talk_Page
	global connection,talk_list,packet
	status=talk_list[current_index][1].text().__str__().__str__().split(":")
	if talk_list[current_index][1].text().__str__().__str__()=="/clear":
		talk_list[current_index][0].clear()
			
	elif talk_list[current_index][1].text().__str__().__str__()=="/help":
		global help			
		help()
	elif talk_list[current_index][1].text().__str__().__str__()=="/users":
		talk_list[current_index][0].append(suser.__str__())
		c=GUI.listWidget.count()
		for index in xrange(c): 
			talk_list[current_index][0].append(GUI.listWidget.item(index).text().__str__().__str__()) 
		talk_list[current_index][1].clear()
	
	elif status[0]=="/status":
					
		GUI.lineEdit_4.setText(status[1])
		Send_Dynamic()
		talk_list[current_index][1].clear()
	elif talk_list[current_index][1].text().__str__().__str__()=="/log":
		save=open("save.txt",'w')
		save.write(talk_list[packet[2]][0].toPlainText())
		save.close()
	else:
		if current_index != "CommonRoom":
			smilies(talk_list[current_index][0],("",talk_list[current_index][1].text().__str__().__str__(),"",GUI.lineEdit.text().__str__().__str__()))
	        connection.transport.write("chat>>:"+talk_list[current_index][1].text().__str__().__str__()+">>:"+current_index)##for public chat "chat>>:contents of lineEdit>>:CommonRoom" is transported
	talk_list[current_index][1].clear()

def Send_Dynamic():
	global chat,connection
	if chat== 1:
                f = Image.open(".temp/avatar.png")
		size=f.resize((30,30))
		size.save(".temp/avat.png","png")
		h=open(".temp/avat.png","rb")
		contents=h.read()
		h.close()
		stat=GUI.lineEdit_4.text().__str__().__str__()
		if stat=="Set your status message here":
			stat="available"
		data="change_details>>:"+stat+">>:"+contents 
		connection.transport.write(data)
	else:
		pass

current_index='CommonRoom' #setting up initial chat flag

QtCore.QObject.connect(GUI.pushButton_3,QtCore.SIGNAL("clicked()"),Send_Details)
QtCore.QObject.connect(GUI.pushButton_2,QtCore.SIGNAL("clicked()"),Connect)
QtCore.QObject.connect(GUI.listWidget,QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"),New_Talk)
QtCore.QObject.connect(GUI.pushButton,QtCore.SIGNAL("clicked()"),Send_Dynamic)
QtCore.QObject.connect(GUI.lineEdit_4,QtCore.SIGNAL("returnPressed()"),Send_Dynamic)
reactor.runReturn()							##reactor will run until Ctrl_C is pressed
sys.exit(app.exec_())
