from twisted.internet.protocol import Factory, Protocol
from sys import stdout
from PyQt4 import QtCore, QtGui
import qt4reactor
from test import*
import sys
import time
app=QtGui.QApplication(['test'])
GUI=Swan_Server()
GUI.show()
reactor=qt4reactor.install()
string=""
class User:

	def __init__(self):
		self.users_list=[]
		self.log=open("log.txt",'a')

	def addUser(self,user_name,stat,avtr,tp):
		self.users_list.append((user_name,tp,stat,avtr))			##username,transport and status message is appended to users_list
		GUI.textBrowser_2.append("new user logined in -> "+user_name)

	def removeUser(self,name):						##called to remove user from users_list
		GUI.textBrowser_2.append(name+" : loged out ")	
		temp=[]
		for i in self.users_list:
			if i[0]!=name:
				temp.append(i)
		self.users_list=temp						##refreshed users_list
	def names(self):
		lis=[]
		for i in self.users_list:
			lis.append(i[0])
		return lis
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
	self.username="un_named"
    def connectionLost(self, reason):						##executed when loseConnection() is called
        self.factory.numProtocols = self.factory.numProtocols-1
	if self.flag!=0:
		try:
			user_base.removeUser(self.username)
			string="remove_my_list"
			string=string+">>:"+self.username              ##appending user name,status msg & avatar pic to string
			#print "ividem ethi"
			try:
				for i in user_base.users_list:
					try:
						i[1].write(string)
					except:
						pass
			except:
		
				pass
			
		except:		
			print "error region"
	GUI.textBrowser_2.append("Connection Lost \n\t user name : "+self.username)
	
	
    def dataReceived(self, data):						##called when data is received from client
	global string
	self.flag=1
	packet=data.split('>>:')						##splitting data at >>:
	
	if packet[0]=="user_details":
		username=packet[1]
		self.username=username
		status_message=packet[2]
		avatar_pic=packet[3]
		GUI.textBrowser_2.append("User name :"+username)
		if username in user_base.names():
			 self.flag=0
			 self.transport.write("Already existing user")
			 GUI.textBrowser_2.append(username+" is an  existing user !!! ")
			 #self.transport.loseConnection()
			 #GUI.textBrowser_2.append(" disconnecting "+username)
		else:
			string="populate_list"
			for i in user_base.users_list:
				string=string+">>:"+i[0]+">>>>("+i[2]+")"+"><:"+"no"+">>>>"+i[3]
			if string!="populate_list":
				self.transport.write(string)	
				for j in user_base.users_list:
					print j[0],string.__len__()
					j[1].write("new_user>>:"+username+">>:("+status_message+")"+">>:"+avatar_pic)			##send string to all users
			if username!="un_named":		
				user_base.addUser(username,status_message,avatar_pic,self.transport)	##goto addUser and append new user to user_list
		
			

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

	elif packet[0]=="change_details":
		status_message=packet[1]
		avatar_pic=packet[2]
		user_base.removeUser(self.username)
		user_base.addUser(self.username,status_message,avatar_pic,self.transport)				
		for i in user_base.users_list:
			if i[0]!=self.username:	
				i[1].write("change_list>>:"+self.username+">>:("+status_message+")>>:"+avatar_pic)
				
		
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
	GUI.pushButton.setEnabled(False)

QtCore.QObject.connect(GUI.lineEdit,QtCore.SIGNAL("returnPressed()"),Start_Service)
QtCore.QObject.connect(GUI.pushButton,QtCore.SIGNAL("clicked()"),Start_Service)


reactor.runReturn()								##reactor will run until Ctrl_C is pressed
sys.exit(app.exec_())
