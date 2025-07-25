# La Capa de Transporte: Fundamentos de Conexión y Fiabilidad en Redes

La **Capa de Transporte** es un nivel fundamental en los modelos de red TCP/IP y OSI, encargada de facilitar la comunicación entre aplicaciones o procesos en diferentes dispositivos. Su rol principal es asegurar una transferencia de datos fiable y eficiente a través de la red, gestionando tareas como la detección de errores, el control de flujo y la segmentación de datos.

Esta capa es conocida por ser responsable de la **entrega proceso a proceso**. Los procesos se comunican utilizando el paradigma **cliente-servidor**. En esta capa, las unidades de datos se denominan **segmentos** (para TCP) o **datagramas** (para UDP).

## 1\. Puertos de la Capa de Transporte

Mientras que en la capa de enlace se utilizan direcciones MAC y en la capa de red se usan direcciones IP, en la capa de transporte hablamos de **puertos**. Los puertos son ubicaciones basadas en *software* que organizan el envío y la recepción de datos para servicios específicos, identificando el proceso concreto en el *host*.

Para identificar un puerto, se utilizan 16 bits (2 bytes), lo que permite un rango de números del **0 al 65535**. La IANA (Internet Assigned Numbers Authority) clasifica los puertos en tres rangos principales:

  * **Puertos Bien Conocidos (Well-known ports):** Del **0 al 1023**. Estos puertos están asignados y controlados por la IANA para servicios y aplicaciones comunes (ej., HTTP en el puerto 80, SSH en el 22, FTP en el 21).
  * **Puertos Registrados (Registered ports):** Del **1024 al 49151**. No son asignados ni controlados directamente por la IANA, pero pueden ser registrados por ella para evitar duplicaciones por parte de aplicaciones o servicios específicos.
  * **Puertos Dinámicos, Privados o Efímeros (Dynamic, private or ephemeral ports):** Del **49152 al 65535**. No están controlados ni registrados por la IANA y son utilizados por cualquier proceso. Estos son los puertos que un cliente elige al azar para escuchar las respuestas temporalmente, y que dejan de estar activos una vez que se recibe la respuesta.

## 2\. Protocolos de la Capa de Transporte: TCP vs. UDP

En la capa de transporte, los protocolos más importantes y fundamentales para el correcto funcionamiento de las comunicaciones son **TCP** y **UDP**.

| Característica       | TCP (Transmission Control Protocol)           | UDP (User Datagram Protocol)                     |
| :------------------- | :-------------------------------------------- | :----------------------------------------------- |
| **Tipo de Conexión** | Orientado a conexión (requiere *handshake*)       | Sin conexión (no requiere *handshake*)         |
| **Fiabilidad** | Fiable (gestiona confirmación y retransmisión) | No fiable (no gestiona nada de esto)   |
| **Orden de Mensajes**| Garantiza el orden de llegada          | No garantiza el orden de llegada   |
| **Peso del Protocolo**| Pesado (requiere configuración previa, control de flujo/congestión) | Ligero (no requiere configuración previa)       |
| **Transmisión de Datos**| Basada en flujo de *bytes* (sin límites de mensaje definidos) | Basada en datagramas (paquetes individuales con límites definidos) |
| **Control de Congestión y Flujo**| Sí (utiliza ventana deslizante)         | No tiene mecanismos de control          |
| **Soporte Broadcast**| No soporta *broadcasting* | Sí soporta *broadcasting* |
| **Soporte Multicast**| No soporta *multicast* | Sí soporta *multicast* |

## 3\. TCP (Transmission Control Protocol)

El **Protocolo de Control de Transmisiones (TCP)** es un estándar diseñado para garantizar una transmisión segura y eficiente de información a través de redes.

### 3.1. Características Esenciales de TCP

  * **Orientación a Conexión:** Antes de transferir datos, TCP establece una comunicación de tres pasos llamada **Three-way Handshake** (apretón de manos de tres vías) entre el emisor y el receptor.
  * **Fiabilidad:** Garantiza que los datos enviados se reciban correctamente. Utiliza técnicas como la **confirmación de recepción** mediante **ACKs** y la **retransmisión de datos** para asegurar que no se pierda información.
  * **Control de Flujo y Congestión:** TCP ajusta la velocidad de transmisión de datos para evitar la saturación de la red, utilizando algoritmos como el **control de congestión de ventana deslizante**. Esto controla la cantidad de datos que un emisor puede enviar antes de recibir una confirmación del receptor.
  * **Full-Duplex:** Permite la comunicación bidireccional simultánea. Ambos extremos pueden enviar y recibir datos al mismo tiempo.
  * **Comprobación de Errores y Recuperación:** TCP verifica constantemente si los datos han llegado correctamente al destino. Si detecta errores o *timeouts*, retransmite los datos perdidos para garantizar una entrega precisa y completa.
  * **Segmentación y Reensamblaje:** Divide los datos en segmentos más pequeños antes de enviarlos a través de la red, facilitando la transmisión y permitiendo que los datos se reensamblen correctamente en el destino.

### 3.2. Formato del Segmento TCP

Un segmento TCP contiene los siguientes campos:

  * **Puerto Origen (Source Port):** El puerto que el servidor utilizará en las respuestas para saber dónde enviar la información de vuelta al cliente.
  * **Puerto Destino (Destination Port):** El puerto del servicio al que se conecta el cliente (ej., 80 para HTTP, 443 para HTTPS, 21 para FTP).
  * **Número de Secuencia (Sequence Number - SEQ):**
      * Si el *flag* **SYN** está activo (`1`), este campo toma el número de secuencia inicial de la transmisión (aleatorio).
      * Si el *flag* **SYN** está desactivado (`0`), representa el número de *bytes* de datos enviados y se suma el número de *bytes* en cada nueva secuencia.
  * **Número de Acknowledge (Acknowledgment Number - ACK):** Presente cuando el *flag* **ACK** está activo. Indica el número del próximo *byte* que el emisor espera recibir del receptor.
  * **Data Offset:** Indica el tamaño de la cabecera TCP en palabras de 32 *bytes*.
  * **Reservado (Reserved):** Campo de 3 *bits*, normalmente a cero, para uso futuro.
  * **Flags (Banderas):** Ocho *flags* de 1 *bit* cada uno, que indican el estado de la conexión o acciones específicas:
      * **ACK:** Para confirmar recepciones.
      * **SYN:** Para iniciar una conexión.
      * **RST (Reset):** Para cerrar una conexión abruptamente.
      * **FIN (Finish):** Para terminar una conexión de forma exitosa.
      * **PSH (Push):** Para enviar datos.
      * **URG (Urgent):** Indica que el puntero de urgencia es significativo.
      * **ECE (ECN-Echo):** Relacionado con ECN (Explicit Congestion Notification).
      * **CWR (Congestion Window Reduced):** Relacionado con ECN.
  * **Window Size (Tamaño de Ventana):** Especifica el número de unidades de datos que el receptor está dispuesto a recibir antes de enviar una confirmación, utilizado para el control de flujo.
  * **Urgent Pointer (Puntero de Urgencia):** Se utiliza junto al *flag* **URG** e indica la posición del último *byte* de datos urgentes en el segmento.
  * **Opciones (Options):** Campo variable que proporciona información adicional o parámetros de configuración específicos para una conexión TCP.

### 3.3. Usos Comunes de TCP

TCP se utiliza en aplicaciones donde la **fiabilidad** y la **integridad de los datos** son críticas:

  * **Transferencia de Archivos:** Ampliamente utilizado por protocolos como **FTP**, **SFTP**, **Samba**, y conexiones seguras **HTTPS**.
  * **Correo Electrónico:** Servidores de correo utilizan TCP (para protocolos como SMTP, POP3, IMAP) para enviar y recibir correos de manera confiable y en el orden correcto.
  * **Navegación Web:** Cada vez que se visita un sitio web, el navegador utiliza TCP para establecer una conexión con el servidor web y descargar los datos de la página.
  * **Acceso Remoto y VPNs:** Para conexiones seguras y confiables a máquinas remotas o a través de redes privadas virtuales (**VPN**).
  * **Transacciones Financieras y Bases de Datos:** En general, para transferir datos sensibles donde no hay tolerancia a la pérdida de paquetes (ej., escritura y lectura en bases de datos).

### 3.4. Funcionamiento de TCP: Three-way Handshake y Transferencia de Datos

El funcionamiento técnico de TCP se divide en tres pasos principales: establecimiento de la conexión, transferencia de datos y cierre de la conexión.

#### 3.4.1. Establecimiento de Conexión (Three-way Handshake)

Este proceso de tres vías establece una comunicación entre cliente y servidor.

1.  **Cliente envía SYN:** El cliente inicia el *handshake* enviando un segmento TCP con el *flag* **SYN** activado. El número de secuencia (`seq`) es un valor aleatorio (ej., 8000).
2.  **Servidor responde SYN + ACK:** El servidor responde con un segmento TCP que tiene los *flags* **SYN** y **ACK** activados.
      * El *flag* **SYN** indica que también desea sincronizarse.
      * El *flag* **ACK** confirma la recepción del SYN del cliente.
      * El número de secuencia del servidor (`seq`) es aleatorio (ej., 15000).
      * El número de *acknowledgement* (`ack`) es el número de secuencia del cliente **incrementado en 1** (ej., 8001), indicando que el servidor ha recibido *bytes* hasta el 8000 y espera a partir del 8001.
3.  **Cliente envía ACK:** Finalmente, el cliente responde con un segmento TCP con el *flag* **ACK** activado.
      * El número de secuencia del cliente (`seq`) es el número de ACK que recibió del servidor (ej., 8001).
      * El número de *acknowledgement* (`ack`) es el número de secuencia del servidor **incrementado en 1** (ej., 15001).
      * Este último ACK no consume un número de secuencia, lo que significa que si el servidor comenzara a enviar datos, podría usar el 15001 como siguiente número de secuencia.

#### 3.4.2. Transferencia de Datos

Una vez establecida la conexión, los datos se envían en segmentos TCP, a menudo con el *flag* **PSH** (Push) activado.

1.  **Cliente envía PSH (datos):** El cliente envía el primer segmento de datos. El número de secuencia es el 8001 (el mismo que el último ACK enviado por el cliente, ya que los ACKs no consumen número de secuencia). Si el cliente envía, por ejemplo, 1000 *bytes* de datos (del 8001 al 9000), el siguiente número de secuencia para el cliente será 9001. El número ACK permanece igual, ya que no se han recibido datos del servidor.
2.  **Cliente envía PSH (más datos):** El cliente puede continuar enviando más datos. El número de secuencia se incrementa según la cantidad de *bytes* enviados (ej., del 9001 al 10000).
3.  **Servidor responde ACK (y datos):** El servidor confirma la recepción de los datos del cliente. Envía un ACK con el número 10001 (confirmando la recepción hasta el *byte* 10000 y esperando a partir del 10001). El servidor también puede enviar sus propios datos en este mismo segmento (ej., del 15001 al 17000, desde su perspectiva).
4.  **Cliente responde ACK:** El cliente responde al servidor confirmando la recepción de sus datos. Su número de secuencia será 10001 (el último número de secuencia usado por el cliente más los *bytes* enviados), y su ACK será 17001 (confirmando la recepción hasta el *byte* 17000 del servidor y esperando a partir del 17001).

#### 3.4.3. Cierre de Conexión

El cierre de una conexión TCP es un proceso de cuatro vías, aunque a veces se puede reducir a tres.

1.  **Cliente envía FIN:** El cliente inicia el cierre enviando un segmento TCP con el *flag* **FIN** activo. El número de secuencia es el último usado por el cliente (ej., 10001, si el último mensaje fue un ACK que no consumió secuencia). El ACK es el último recibido del servidor (ej., 17001). Este FIN consume un número de secuencia, aunque no lleve datos.
2.  **Servidor responde FIN + ACK:** El servidor confirma la recepción del FIN del cliente con un **ACK**, y también indica que desea finalizar la comunicación enviando su propio **FIN**.
      * El número de secuencia del servidor es el último que utilizó (ej., 17001).
      * El número de ACK es el número de secuencia del cliente **incrementado en 1** (ej., 10002, por el FIN recibido). Este FIN también consume un número de secuencia.
3.  **Cliente envía ACK Final:** Finalmente, el cliente recibe el FIN+ACK del servidor y le confirma la recepción con un último **ACK**.
      * El número de secuencia del cliente es el número de ACK que recibió del servidor (ej., 10002).
      * El número de ACK es el número de secuencia del servidor **incrementado en 1** (ej., 17002, por el FIN del servidor).
      * Este último paquete ACK no lleva datos y no consume número de secuencia.

## 4\. UDP (User Datagram Protocol)

El **Protocolo de Datagramas de Usuario (UDP)** es un protocolo de la capa de transporte que ofrece una entrega de datos más rápida, aunque es menos fiable y no orientado a conexión que TCP.

### 4.1. Características de UDP

A diferencia de TCP, UDP es:

  * **Sin conexión:** No requiere un *handshake* ni establece una conexión antes de transmitir datos.
  * **No fiable:** No gestiona la confirmación de mensajes, la retransmisión o los tiempos de espera.
  * **No garantiza el orden:** Los mensajes pueden llegar desordenados.
  * **Ligero:** No requiere configuración previa, control de flujo o congestión, lo que lo hace más eficiente para ciertas aplicaciones.
  * **Basado en Datagramas:** Transmite datos en paquetes individuales con límites de mensaje definidos.
  * **Sin control de congestión o flujo:** No tiene mecanismos para controlar la congestión o el flujo de mensajes.
  * **Soporta Broadcast y Multicast:** A diferencia de TCP.

### 4.2. Formato del Datagrama UDP

La cabecera del datagrama UDP es bastante sencilla:

| Campo        | Bits | Descripción                                                       |
| :----------- | :--- | :---------------------------------------------------------------- |
| **Source Port** | 16   | Puerto de origen de la aplicación que envía el datagrama.      |
| **Destination Port** | 16   | Puerto de destino de la aplicación que recibe el datagrama.    |
| **Length** | 16   | Longitud total del datagrama UDP (cabecera + datos) en *bytes*. |
| **Checksum** | 16   | Suma de verificación opcional para detectar errores en la cabecera y los datos UDP. |

### 4.3. Usos Principales de UDP

UDP se utiliza en aplicaciones donde la **velocidad** y la **simplicidad** son más importantes que la fiabilidad y el control de flujo, o donde la sobrecarga de TCP no es rentable.

  * **Transmisión de Audio y Video en Tiempo Real:** En *streaming* multimedia, videollamadas o voz sobre IP (VoIP), la pérdida ocasional de paquetes es preferible a la retransmisión y el retardo.
  * **Videojuegos Online:** Similar al *streaming*, la velocidad es crucial y la retransmisión podría causar latencia inaceptable.
  * **DHCP (Dynamic Host Configuration Protocol):** Utilizado para la asignación automática de direcciones IP.
  * **DNS (Domain Name System):** Para la resolución de nombres de dominio a direcciones IP, donde la rapidez en la consulta es clave.
  * **Servicios de Transmisión de Datos con Tolerancia a Pérdidas:** Aplicaciones donde la pérdida ocasional de paquetes no es crítica para la funcionalidad.

### 4.4. Funcionamiento de UDP

Los programas pueden enviar mensajes datagramas a través de la red sin necesidad de establecer una conexión previa (no hay *handshake*). Los datagramas UDP se envían con direcciones IP de origen y destino, así como números de puerto para identificar tanto la aplicación que envía como la que recibe. La simplicidad de UDP lo hace más eficiente en términos de sobrecarga de procesamiento y latencia, a costa de la fiabilidad.