> TCP

> TCP (the “Transmission Control Protocol “) has the responsibility for breaking up t he message into datagrams, reassembling them at the other end, resending anything that gets lost, and putting things back in the right order. It may seem that TCP is doing all the work. And in small network it is true. With TCP, there is no maximum message length. When a message is passed to the TCP protocol, if it is too large to be sent in one peace, the message is broken up into chunks or packets and sent one at a time to the destination address. The TCP packet contains the addressing information. The TCP message also contains a packet number and total number of packets.

> IP

> As the number of computers networked become larger, a system becomes necessary to give remote computers the capability to recognize other remote computers; thus the IP addressing method was born. Therefore, simply an IP address uniquely identifies any computer connected to a network. This address is made up of 32 bits divided into 4 four bytes. But since the number of connected computers is too large and since it is difficult to remember all their IP addresses, the Domain Name Service (DNS) was designed .