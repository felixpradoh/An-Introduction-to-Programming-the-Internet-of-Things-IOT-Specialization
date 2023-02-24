# In your own words, write a short paragraph describing the differences between the TCP and IP protocols. Then, in your own words, describe the different roles between the TCP and IP protocols in Internet communication.

The OSI model is composed of different layers that contain different protocols. 

-The TCP protocol (Transmission Control Protocol) is a protocol employed in the transport layer. It arranges packets in order so IP can deliver them. Specifically, TCP numbers individual packets because IP can send packets to their destinations through different routes and get them out of order, so TCP amends this before IP delivers the packets.

TCP also detects errors in the sending process -- including if any packets are missing based on TCP's numbered system -- and requires IP to retransmit those packets before IP delivers the data to its destination. 

-The IP protocol (Internet Protocol) is a protocol that is used in the network layer, the final layer of the OSI model.  It is assigned to each device that is connected to a computer network which uses the IP for communication. Its routing function allows internetworking and essentially establishes the Internet. Combination of IP with a TCP allows developing a virtual connection between a destination and a source.
