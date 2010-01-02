from twisted.internet.protocol import Factory, Protocol
from sys import stdout
from PyQt4 import QtCore, QtGui
import qt4reactor
from test import*
import sys

app=QtGui.QApplication(['test'])
GUI=Swan_Server()
GUI.show()
reactor=qt4reactor.install()
string=""
#user class
class User:

	def __init__(self):
		self.users_list=[]

	def addUser(self,user_name,stat,tp):
		self.users_list.append((user_name,tp,stat))				##username and transport is appended to users_list
		GUI.textBrowser_2.append("new user logined in -> "+user_name)

	def removeUser(self,name):						##called to remove user from users_list
		#print "removing!!!"
		GUI.textBrowser_2.append(name+" : loged out ")	
		temp=[]
		for i in self.users_list:
			if i[0]!=name:
				temp.append(i)
		self.users_list=temp						##refreshed users_list
user_base=User()

class Echo(Protocol):								##Protocols for new connection,connection lost,data received are defined here.This 											  class inherits Protocol class
    def connectionMade(self):
	
	GUI.textBrowser_2.append("connection")
        self.factory.numProtocols = self.factory.numProtocols+1 
	if self.factory.numProtocols > int(GUI.lineEdit_2.text().__str__().__str__()):
            self.transport.write("Too many connections, try later")
	    GUI.textBrowser_2.append("Too many connections, try later")
            self.transport.loseConnection()					##go to connectionLost() to lose connection
	self.flag=1
	
    def connectionLost(self, reason):						##executed when loseConnection() is called
        self.factory.numProtocols = self.factory.numProtocols-1
	if self.flag!=0:
		user_base.removeUser(self.username)
	print "removed"+self.username
	GUI.textBrowser_2.append("Connection Lost \n\t user name : "+self.username)
	#print "to genrate populate list"
	string="populate_list"
	for i in user_base.users_list:
			string=string+">>:"+i[0]+">>>>("+i[2]+")"				##appending name to string to display all users.
	#print "populated list generated",string
	print "users list",user_base.users_list
	try:
		for i in user_base.users_list:
			print"keri"+i[0]
			i[1].write(string)
		#print "kazhinju"
	except:
		#print "oooooooooo"
		pass
	
    def dataReceived(self, data):						##called when data is received from client
	global string
	self.flag=1
	
	packet=data.split('>>:')						##splitting data at >>:
	
	if packet[0]=="user_details":
		username=packet[1]
		status_message=packet[2]
		
		GUI.textBrowser_2.append("User name :"+username)
		self.username=username
		string="populate_list"
		users_poplast=[]
		for i in user_base.users_list:
			users_poplast.append(i)			
		for i in users_poplast:
			if i[0]!=username:
			    string=string+">>:"+i[0]+">>>>("+i[2]+")"				##refresh string 
			else:
			    self.flag=0
			    self.transport.write("Already existing user")
			    GUI.textBrowser_2.append(username+" is an  existing user !!! ")
			    self.transport.loseConnection()			##connection rejected if user name already exists
			    GUI.textBrowser_2.append(" disconnecting "+username)
			    return
		user_base.addUser(username,status_message,self.transport)			##goto addUser and append new user to user_list
		string=string+">>:"+username+">>>>("+status_message+")"
		
			
		if string!="populate_list":
			
			for j in user_base.users_list:
				j[1].write(string)				##send string to all users
	elif packet[0]=="chat":							##packet[0] is chat when chatting
		if packet[2]=="CommonRoom":					##packet[2] indicate "CommonRoom" i.e. public or else name of recepient
			for i in user_base.users_list:
				i[1].write("chat>>:"+packet[1]+">>:CommonRoom>>:"+self.username) ##send to all user  packet[1] indicate data
			GUI.textBrowser_2.append("CommonRoom"+">>>"+packet[1])
		else:
			try:
				tpr=None
				for i in user_base.users_list:
					if i[0]==packet[2]:			##if name=name of recepient
						tpr=i[1]			##tpr=transport of recepient
						break
				tpr.write("chat>>:"+packet[1]+">>:"+self.username+">>:"+self.username)
			        GUI.textBrowser_2.append(self.username+">>>"+packet[1])
			except:
				pass
	elif packet[0]=="lost":
		self.flag=1
		self.transport.loseConnection()

class EchoFactory(Factory):							##inherits Factory class
	protocol = Echo								##define protocol as Echo
	def __init__(self):
		self.numProtocols=0
		
def Start_Service():								##start server after port is specified
	GUI.textBrowser_2.append("Listening")
	reactor.listenTCP(int(GUI.lineEdit.text().__str__().__str__()), EchoFactory())
	GUI.lineEdit.setEnabled(False)
	GUI.lineEdit_2.setEnabled(False)
QtCore.QObject.connect(GUI.lineEdit,QtCore.SIGNAL("returnPressed()"),Start_Service)
reactor.runReturn()								##reactor will run until Ctrl_C is pressed
sys.exit(app.exec_())
