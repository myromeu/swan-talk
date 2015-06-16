> Twisted 8.2.0-3

> Twisted is an open source networking framework designed to be very flexible and let you write powerful servers. The cost of this flexibility is a few layers in the way to writing your server.Twisted is an event driven Networking engine,written in Python and licensed under the MIT license.Twisted is supporting numerous protocols.It contains a web server ,numerous chat clients,chat servers,mail servers and more.It is designed to support both clients and servers and run on multiple operating systems and platforms.

> Twisted is divided into several packages ,each providing different services ,some packages are:

  1. twisted.internet

> At twisted's core,the twisted.internet package provides a networking event loop.Theevent loop networking model was chossen over threads as it tends to be most scable ,integrates well with GUI applications.

> 2.twisted.protocols

> Some applications use Twisted exclusively to develope custom protocols, many applications use common,internet standard protocol.Supported protocols includes HTTP,FTP,DNS,SMTP,NNTP etc

> In our project we use

  1. twisted.internet.protocol.protocol

> Our protocol handling class usually sub classtwisted.internet.protocol.protocol. Most protocol handlers inherit either from this class or from one of its convienence children An instance of this protocol class might be instantiated per connection,on demand,and might go away when the connection is finished.This means that persistent configeration is not saved in the protocol.

> 2.twisted.internet.protocol.Factory

> The persistent configuration is kept in a Factory class,which usually inherits from twisted.internet.protocol.protocol.The default factory class just instantiates each protocols,and then sets on it an attribute called factory which points to itself.This lets every protocol access,and possibily modify,the persistent configuration.

> 3. twisted.internet.reactor

> The reactor is Twisted's event loop. You use the reactor to register sources of events and handlers for these events, and then the reactor calls those handlers.The reactor provides basic interfaces to a number of services,including network communication ,threading a nd event dispatching.