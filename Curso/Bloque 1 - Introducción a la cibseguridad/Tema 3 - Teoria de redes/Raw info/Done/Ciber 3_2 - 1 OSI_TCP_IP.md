## **2. Network Models: TCP/IP & OSI**

Conceptual models are used to visualize and standardize how data is organized and transmitted across a network. They help professionals troubleshoot issues and identify the layer at which a security threat has occurred.

### **The TCP/IP Model**

The TCP/IP (Transmission Control Protocol/Internet Protocol) model is the standard framework for network communication.

  * **Transmission Control Protocol (TCP):** A connection-oriented protocol that allows two devices to establish a reliable connection and stream data. It ensures packets are organized, sent, and arrive at their destination correctly.
  * **Internet Protocol (IP):** A set of standards for routing and addressing data packets so they can travel between networks.
  * **Ports:** Software-based locations that organize the sending and receiving of data for specific services. A port number in a packet header tells the receiving computer which application or service should handle the data.
      * **Port 25:** Used for email (SMTP).
      * **Port 443:** Used for secure web communication (HTTPS).
      * **Port 20:** Used for large file transfers (FTP data).

### **The Four Layers of TCP/IP**

1.  **Network Access Layer (or Data Link Layer)**
      * **Function:** Deals with the physical transmission of data packets. It manages the creation of packets and how they are sent over physical hardware.
      * **Protocols & Hardware:** ARP (Address Resolution Protocol), Ethernet, Wi-Fi, Switches, Hubs, Cables.

2.  **Internet Layer**
      * **Function:** Responsible for addressing packets with IP addresses and routing them across different networks to their final destination.
      * **Protocols:** IP (Internet Protocol), ICMP (Internet Control Message Protocol for error reporting).

3.  **Transport Layer**
      * **Function:** Controls the flow of traffic and ensures reliable end-to-end data delivery between systems.
      * **Protocols:**
          * **TCP (Transmission Control Protocol):** Reliable, connection-oriented. Guarantees delivery.
          * **UDP (User Datagram Protocol):** Connectionless, faster, but does not guarantee delivery. Used for real-time applications like video streaming.

4.  **Application Layer**
      * **Function:** Defines protocols for how applications interact with the network. This is the layer users interact with.
      * **Protocols:** HTTP (Web), SMTP (Email), FTP (File Transfer), SSH (Secure Shell), DNS (Domain Name System).

### **The OSI Model & Comparison**

The OSI (Open Systems Interconnection) model is a standardized conceptual framework that describes how seven different layers work together to enable communication and data transfer over a network. It provides a more in-depth understanding of the processes occurring at each stage, from direct user interaction down to the physical connection. It is a more detailed, 7-layer conceptual model. The TCP/IP model is a more practical, condensed version of the OSI model.

### TCP/IP Model vs. OSI Model

Both the TCP/IP and OSI models are conceptual frameworks used to visualize how data is organized and transmitted across a network. They help network engineers and security analysts understand network processes and communicate about disruptions or security threats.

* The **TCP/IP model** is a four-layer model (Network Access, Internet, Transport, and Application) that is a condensed form of the OSI model. It is widely used in practice.
* The **OSI model** is a seven-layer standardized concept that provides a more granular view of network communication processes.

While some organizations prefer one model over the other, it's crucial for security analysts and network professionals to be familiar with both to effectively analyze network events and communicate about issues. Both models are invaluable tools for comprehending the intricacies of network operations.


| **OSI Model Layer** | **Layer \#** | **Description** | **TCP/IP Layer** |
| :------------------ | :---------: | :--------------------------------------------------------------------------------------- | :--------------------- |
| **Application** | 7 | User-facing protocols and services (HTTP, DNS). | **Application Layer** |
| **Presentation** | 6 | Data translation, formatting, encryption (SSL/TLS), and compression. | **Application Layer**
| **Session** | 5 | Establishes, manages, and terminates connections (sessions) between devices. | **Application Layer**
| **Transport** | 4 | End-to-end data transport, segmentation, and flow control (TCP, UDP). | **Transport Layer** |
| **Network** | 3 | Logical addressing (IP addresses), routing, and path determination. | **Internet Layer** |
| **Data Link** | 2 | Physical addressing (MAC addresses), framing, and controlling access to the physical medium. | **Network Access Layer** |
| **Physical** | 1 | The physical hardware: cables, hubs, switches. Transmits raw bit streams (0s and 1s). | **Network Access Layer**

### The 7 Layers of the OSI Model

We'll explore the layers from 7 (closest to the user) down to 1 (the physical connection).

#### Layer 7: Application Layer

The **Application Layer** is the closest to the end-user. It encompasses processes that directly involve user interaction with the network. This layer includes all networking protocols that software applications use to connect a user to the internet.

* **Key Function:** User connection to the internet via applications and requests.
* **Examples:**
    * Web browsers using **HTTP** (Hypertext Transfer Protocol) or **HTTPS** (Hypertext Transfer Protocol Secure) to send and receive information from website servers.
    * Email applications using **SMTP** (Simple Mail Transfer Protocol) to send and receive email.
    * Web browsers using **DNS** (Domain Name System) to translate website domain names into IP addresses, identifying the web server hosting the website's information.

#### Layer 6: Presentation Layer

The **Presentation Layer** is responsible for data translation and encryption, ensuring data can be understood by applications (Layer 7) on both sending and receiving systems. Formats at the user end may differ from those of the receiving system, requiring standardization at this layer.

* **Key Functions:** Data formatting, encryption, compression, and character code set confirmation.
* **Examples:**
    * **SSL** (Secure Sockets Layer) encryption, which encrypts data between web servers and browsers for websites using HTTPS.
    * Converting data into a standardized format for seamless exchange between different systems.

#### Layer 5: Session Layer

The **Session Layer** manages the establishment, maintenance, and termination of connections (sessions) between two devices. An open session allows devices to communicate.

* **Key Functions:**
    * Maintaining an open session while data is being transferred.
    * Terminating the session upon completion of data transmission.
    * Authentication.
    * Reconnection.
    * Setting checkpoints during data transfers to enable resumption from the last checkpoint if a session is interrupted.
* **Interaction:** Responds to service requests from the Presentation Layer (Layer 6) and sends requests for services to the Transport Layer (Layer 4).

#### Layer 4: Transport Layer

The **Transport Layer** is responsible for reliable data delivery between devices. It manages the speed and flow of data transfer and breaks down large data into smaller segments for easier transport.

* **Key Functions:**
    * Delivering data between devices.
    * Handling data transfer speed and flow control.
    * **Segmentation:** Dividing large data transmissions into smaller pieces that can be processed by the receiving system. These segments must be reassembled at the destination.
    * Matching the transmission speed and rate to the connection speed of the destination system.
* **Protocols:** **TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol).

#### Layer 3: Network Layer

The **Network Layer** oversees receiving frames from the Data Link Layer (Layer 2) and delivering them to their intended destination. This destination is determined by the address within the data packet's frame.

* **Key Functions:**
    * Routing data packets between different networks.
    * Identifying the intended destination based on IP addresses within data packets.
* **Components:** Data packets include IP addresses that instruct routers where to send them, enabling communication between two networks.

#### Layer 2: Data Link Layer

The **Data Link Layer** organizes the sending and receiving of data packets within a *single network*.

* **Key Functions:**
    * Managing data flow within a local network.
    * Error detection and correction for data frames.
* **Components:** This layer is home to network switches on the local network and network interface cards (NICs) on local devices.
* **Protocols:** **NCP** (Network Control Protocol), **HDLC** (High-Level Data Link Control), and **SDLC** (Synchronous Data Link Control Protocol).

#### Layer 1: Physical Layer

As its name suggests, the **Physical Layer** corresponds to the physical hardware involved in network transmission.

* **Key Functions:**
    * Translating data packets into a stream of 0s and 1s for transmission over physical media.
    * Sending and receiving these streams of 0s and 1s across physical wiring and cables.
    * Passing received data to higher levels of the OSI model.
* **Components:** Hubs, modems, cables, and wiring (e.g., Ethernet or coaxial cables) are all part of the Physical Layer.
