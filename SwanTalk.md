> # CONTENTS #



  1. Introduction

> 2. NetWork

> 3. [used](Protocals.md)
> > 3.1 TCP


> 3.2 IP

> 4.  [Client-Server Application]

> 5. Framework

> 5.1 Twisted 8.2.0-3

> 6. Language used

> 6.1 Python

> 7. PyQt4

> 8. Future Enhancements

> 9. Issues

  1. .Conclusion



> # Introduction #

> SWAN LAN Chat is a tiny and easy to use instant messaging software. Users can initiate their respective chat -”PUBLIC & PRIVATE” in corresponding chat rooms. Written in Python Language. Swan chat is a LAN based chat messenger.Our project is an example of a chat server. It is made up of 2 applications the client application, which runs on the user’s Pc and server application, which runs on any Pc on the network. To start chatting client should get connected to server where they can practice two kinds of chatting, public one (message is broadcasted to all connected users) and private one (between any 2 users only) and during the last one security measures were taken.






> # LAN Networks #

> A LAN network will allow computers in a home or office to talk to one another, pass files, use a common database, and share a printer or fax machine, to name a few advantages. A high-speed Internet account can also be shared on a LAN to provide online access to all computers connected to the network.

> Most local area networks are built with relatively inexpensive hardware such as Ethernet cables, network adapters, and hubs. Wireless LAN and other more advanced LAN hardware options also exist.

> # Protocols used #
> > TCP


> TCP (the “Transmission Control Protocol “) has the responsibility for breaking up t he message       into datagrams, reassembling them at the other end, resending anything that gets lost, and putting things back in the right order. It may seem that TCP is doing all the work. And in small network it is true. With TCP, there is no maximum message length. When a message is passed to the TCP protocol, if it is too large to be sent in one peace, the message is broken up into chunks or packets and sent one at a time to the destination address. The TCP packet contains the addressing information. The TCP message also contains a packet number and total number of packets.

> IP

> As the number of computers networked become larger, a system becomes necessary to give remote computers the capability to recognize other remote computers; thus the IP addressing method was born. Therefore, simply an IP address uniquely identifies any computer connected to a network. This address is made up of 32 bits divided into 4 four bytes. But since the number of connected computers is too large and since it is difficult to remember all their IP addresses, the Domain Name Service (DNS) was designed .



> # Client-Server Application #

> Client-server software architecture is versatile and flexible in today’s fast changing IT landscape. It is modular in structure and relies on messaging services for communication between components. They were designed to improve flexibility, usability, scalability, and interoperability. Software flexibility implies the ability for a program to change easily according to different users and different system requirements.
> When the program wishes to use TCP to exchange data, one of the programs should take the role of a client while the other must take the role of a server. The client application initiates what is called active open.An environment in which the application processing is divided between client workstations and servers. It implies the use of desktop computers interacting with servers in a network in contrast to processing everything in a large centralized mainframe.


> The server side would follow these steps:

  1. Listen for incoming connections from clients

> 2. Accept the client connection

> 3.Send and receive information

> In case of the client, these steps are followed:

  1. Specify the address and service port of the server program

> 2. Establish the connection with the server

> 3.Send and receive information


> # FrameWork #

> Twisted 8.2.0-3

> Twisted is an open source networking framework designed to be very flexible and let you write powerful servers. The cost of this flexibility is a few layers in the way to writing your server.Twisted is an event driven Networking engine,written in Python and licensed under the MIT license.Twisted is supporting numerous protocols.It contains a web server ,numerous chat clients,chat servers,mail servers and more.It is designed to support both clients and servers and run on multiple operating systems and platforms.

> Twisted is divided into several packages ,each providing different services ,some  packages are:

  1. twisted.internet
> > At twisted's core,the twisted.internet package provides a networking event loop.Theevent loop networking model was chossen over threads as it tends to be most scable ,integrates well with GUI applications.


> 2.twisted.protocols
> > Some applications use Twisted exclusively to develope custom protocols, many applications use common,internet standard protocol.Supported protocols includes  HTTP,FTP,DNS,SMTP,NNTP etc


> In our project we use

  1. twisted.internet.protocol.protocol

> Our protocol handling class usually sub classtwisted.internet.protocol.protocol. Most protocol handlers inherit either from this class or from one of its convienence children An instance of this protocol class might be instantiated per connection,on demand,and might go away when the connection is finished.This means that persistent configeration is not saved in the protocol.

> 2.twisted.internet.protocol.Factory

> The persistent configuration is kept in a Factory class,which usually inherits from twisted.internet.protocol.protocol.The default factory class just instantiates each protocols,and then sets on it an attribute called factory which points to itself.This lets every  protocol access,and possibily modify,the persistent configuration.

> 3. twisted.internet.reactor
> > The reactor is Twisted's event loop. You use the reactor to register sources of events and handlers for these events, and then the reactor calls those handlers.The reactor provides basic interfaces to a number of services,including network communication ,threading a nd event dispatching.


> .
> # Language Used: #

> The Swan chat server is written in python 2.5.2 ,Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapidapplication development in many areas on most platforms.

> Features:

> Python is a simple and minimalistic language

> Python has an extraordinarily simple syntax

> Python is an example of a FLOSS (Free/Libré and Open Source Software

> Python is a high level language

> Python is indeed an exciting and powerful language. It has the right combination of performance and features that make writing programs in Python both fun and easy.



> # PyQt4 #

> In swan lan chat we use PyQt4 4.4.2-4  is a toolkit for creating GUI
> applications. It is a blending of python programming language and the successfull Qt
> library. Qt library is one of the most powerful libraries on this planet. If not the
> most powerful.

> Creating an application in PyQT4 may be done in a few ways. The most common
> one is to use QTDesigner, which we get with QT. QTDesigner let us draw the GUI which
> is very handy for complicated interfaces. We can place widgets on the window, add
> names etc.

> To create an application in PyQT4 we have to:

  1. Create the GUI in QTDesigner

> 2. Set names in the Property Editor to ease coding of the application (QTDesigner)

> 3. Using pyuic4 create the python GUI class

> 4. Call the application using that GUI class

> 5. Extend it with our own slots

> 6. When you use a widget you go to pyqt4's classess and check methods of each used

> 7. widgets. The method names as "setText" are very easy to understand.


> # ISSUES: #

  1. The server crashes into a segmentation fault whenever one or more clients
> close their talk page.

> 2. closing the talk page does not disconnect the user

> 3. once the talk page is closed the user cannot revive it for a new chat




> # Conclusion #

> The primary goal of this  project is to give an idea about LAN Chat. This project has given us an in depth information about LAN and its applications in day today life. If Local Area Network lives up to its potential, it will revolutionize the way people interact with information technology. This project offers several benefits due to the use of simple and easy to understand tools like qt4 designer. This project is developed in Python ,which is easy to read, learn, scales well, performs well for being interpreted, and is incredibly well-documented.


