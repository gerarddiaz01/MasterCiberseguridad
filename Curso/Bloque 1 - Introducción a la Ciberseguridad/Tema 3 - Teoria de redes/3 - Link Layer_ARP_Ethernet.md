# Fundamentos de la Capa de Enlace: Ethernet y Protocolo ARP

La Capa de Enlace de Datos es un componente crucial en la arquitectura de redes, actuando como el puente entre el mundo lógico de las direcciones IP y el mundo físico de la transmisión de datos a través de cables o señales inalámbricas. Comprender sus funciones, estándares y protocolos es esencial para cualquier experto en ciberseguridad.

## 1\. La Capa de Enlace (Link Layer)

La Capa de Enlace es la capa más baja del modelo TCP/IP (conocida como Capa 1, aunque algunos modelos la asocian con las Capas 1 y 2 del modelo OSI) y es la responsable de transferir datos a través de un **segmento de red físico**. Su objetivo principal es asegurar que los datos se entreguen al dispositivo deseado dentro del *mismo segmento de red*, sin encargarse de enrutar datos a través de diferentes redes.

### 1.1. Capa de Enlace en los Modelos TCP/IP y OSI

La relación entre la Capa de Enlace del modelo TCP/IP y las capas del modelo OSI puede variar según la interpretación.

En un esquema general:

  * **Modelo TCP/IP:** La Capa de Enlace abarca las funcionalidades de la capa física y la capa de enlace de datos del modelo OSI.
  * **Modelo OSI:** Se divide en dos capas separadas:
      * **Capa de Enlace de Datos (Data Link Layer):** Responsable de la transferencia fiable de datos entre nodos directamente conectados.
      * **Capa Física (Physical Layer):** Se encarga de la transmisión de bits puros a través del medio físico.

Aquí se muestra una comparación visual de cómo se relacionan las capas de ambos modelos:

Es importante notar que existen diversas representaciones de los modelos, con algunas variaciones en el número y la correspondencia de las capas.

### 1.2. Flujo de Datos a Través de las Capas

Cuando la información se comparte entre dos *hosts*, atraviesa cada una de las capas:

1.  Los datos se originan en la **Capa de Aplicación**.
2.  En la **Capa de Transporte**, se añaden cabeceras con información de puertos (origen y destino) y se forman los **segmentos**.
3.  Estos segmentos llegan a la **Capa de Internet (o de Red)**, donde se encapsulan con direcciones IP (origen y destino) y otras cabeceras, pasando a denominarse **paquetes**.
4.  Finalmente, en la **Capa de Enlace**, los paquetes se manejan como **tramas** (frames) para ser enviados por medios como **Ethernet** o **Wi-Fi**. A la trama se le añade información como la **dirección MAC**.
5.  En el **nivel físico**, la trama se reduce a **bits** para su transmisión.

### 1.3. Protocolos de la Capa de Enlace

Los protocolos clave que operan en esta capa incluyen:

  * **ARP (Address Resolution Protocol):** Su función principal es traducir las direcciones IP en direcciones MAC dentro de una red local. Se profundiza en la Sección 3.
  * **PPP (Point-to-Point Protocol):** Permite establecer conexiones directas entre dos dispositivos en una red. Fue ampliamente utilizado en conexiones de red por línea telefónica.
  * **Ethernet (IEEE 802.3):** La tecnología principal para conectar dispositivos en una red local de forma alámbrica. Si la conexión es inalámbrica, se utiliza la tecnología **Wi-Fi**.

Aquí se muestra visualmente la ubicación de algunos de estos protocolos en la Capa de Enlace:

## 2\. Ethernet: El Estándar de Red Cableada

**Ethernet** se define como el conjunto de tecnologías utilizado para conectar diferentes dispositivos electrónicos dentro de una **red local** mediante **cable**. Es la tecnología dominante en redes de área local y se utiliza también en redes de área metropolitana (**MAN**) y redes de área extensa (**WAN**).

Comercialmente, Ethernet apareció por primera vez en 1980. En 1983, el **IEEE 802.3** se estableció como el estándar oficial. Desde entonces, ha evolucionado continuamente para soportar mayores velocidades (desde 2.94 Mbps en 1973 hasta 10 Gbps a nivel doméstico actualmente) y mayores distancias, manteniendo siempre la compatibilidad hacia atrás. Otras tecnologías de la época, como **FDDI** o **Token Ring**, fueron finalmente reemplazadas por Ethernet.

Actualmente, existen más de 100 versiones de este conjunto de estándares, lo que subraya su rol como pasado, presente y futuro de Internet.

El **IEEE 802.3** es una colección de estándares que establecen los protocolos de comunicación para las capas inferiores del modelo OSI: la **Capa Física (Capa 1)** y la **Capa de Enlace (Capa 2)**. Las conexiones físicas, que en el pasado se realizaban con cable coaxial o de cobre, ahora utilizan cables de par trenzado y fibra óptica.

### 2.1. CSMA/CD: Control de Acceso al Medio y Detección de Colisiones

**CSMA/CD** (Carrier Sense Multiple Access with Collision Detection), o Acceso Múltiple con Escucha de Portadora y Detección de Colisiones, es un algoritmo de acceso al medio compartido utilizado en redes **Ethernet cableadas**.

Este algoritmo se fragmenta en tres partes:

  * **Carrier Sense (Escucha de Portadora):** Antes de transmitir, un dispositivo escucha el medio (el cable) para detectar si otras tramas se están transmitiendo. Esto asegura que el medio esté libre antes de iniciar la transmisión propia.
  * **Multiple Access (Acceso Múltiple):** Indica que el medio de transmisión es compartido por múltiples *hosts* que envían sus tramas a través de él.
  * **Collision Detection (Detección de Colisiones):** Mientras un dispositivo está transmitiendo, continúa escuchando el medio. Si detecta una señal que no coincide con su propia transmisión, se produce una **colisión**. Esto significa que dos o más dispositivos intentaron transmitir al mismo tiempo. Cuando una colisión ocurre, todos los dispositivos implicados detienen inmediatamente la transmisión y esperan un tiempo aleatorio antes de intentar retransmitir sus datos, para evitar que la colisión se repita.

**Analogía de la Carretera:**
Imagina una carretera de un solo carril en ambas direcciones. Los coches son los dispositivos y la carretera es el medio de red. Solo un coche puede estar en la carretera a la vez.

1.  **Escucha de Portadora:** Antes de entrar, un coche "escucha" si hay otros coches viniendo en ambas direcciones. Si la carretera está libre, puede entrar y conducir.
2.  **Detección de Colisiones:** Mientras el coche avanza, sigue "escuchando". Si detecta otro coche en dirección opuesta que también ha entrado a la carretera, se produce una **colisión**.
3.  **Resolución de Colisiones:** Ambos coches deben retroceder inmediatamente y salir de la carretera. Cada coche espera un tiempo aleatorio antes de intentar reingresar.

Para **redes inalámbricas (Wi-Fi)**, se utiliza un protocolo homólogo llamado **CSMA/CA** (Collision Avoidance), que intenta evitar colisiones en lugar de solo detectarlas.

### 2.2. Subcapas de la Capa de Enlace: LLC y MAC

La Capa de Enlace de Datos se divide en dos subcapas principales:

  * **LLC (Logical Link Control - Capa de Control de Enlace Lógico):**

      * **Función:** Proporciona un mecanismo para el control de errores, control de flujo y control de secuencia.
      * Permite que múltiples protocolos de nivel de red (como **IP** o **IPX**) compartan una misma interfaz de red física y establezcan comunicación sin preocuparse por los detalles específicos del medio físico. Es como un adaptador para estos protocolos.

  * **MAC (Media Access Control - Capa de Acceso al Medio):**

      * **Función:** Responsable de la asignación de **direcciones únicas** a los dispositivos de red (direcciones MAC) y del acceso al medio físico compartido.
      * Define cómo los dispositivos acceden y comparten este medio, evitando colisiones en redes de acceso múltiple como Ethernet.

Las capas **LLC** y **MAC** añaden sus respectivas cabeceras y sufijos al paquete que proviene de las capas superiores, formando así la trama que finalmente se enviará a la capa física en forma de bits.

### 2.3. Direcciones MAC (Media Access Control)

Cada *host* en una red tiene una **tarjeta de interfaz de red (NIC)**, y cada tarjeta tiene una dirección única grabada en su memoria **ROM**. Esta es la **dirección Ethernet**, también conocida como **dirección física** o **dirección MAC**.

Una dirección MAC está formada por **seis octetos** en formato **hexadecimal**, separados por dos puntos (ej. `24:B4:25:23:E1:32`). En total, son **6 bytes** o **48 bits**.

La dirección MAC se divide en dos partes:

  * **OUI (Organizationally Unique Identifier - Identificador Único Organizacional):**

      * Son los primeros tres octetos (24 bits) de la dirección MAC.
      * Es un prefijo asignado por el **Comité de la Autoridad de Registro IEEE** a los proveedores registrados.
      * Permite identificar el fabricante de la tarjeta de red (ej. Intel, Realtek).

  * **NIC (Network Interface Controller - Número de Identificación de Componente de Red):**

      * Son los últimos tres octetos (24 bits) de la dirección MAC.
      * Identifica de manera única al dispositivo dentro de la red, siendo asignado por el fabricante de la tarjeta.

Al igual que con las direcciones IP, existen direcciones MAC especiales:

  * **Dirección Broadcast:** Se utiliza para enviar una trama a **todos los dispositivos** en el segmento Ethernet local. Está formada por 12 `F`s en hexadecimal (`FF:FF:FF:FF:FF:FF`).

### 2.4. Estructura de la Trama (Frame) Ethernet

Una trama Ethernet está compuesta por varias cabeceras y un sufijo que encapsulan el paquete de datos de las capas superiores.

| Campo | Tamaño | Descripción |
| :---- | :----- | :---------- |
| **Preámbulo + SFD** | 7 + 1 bytes | \* **Preámbulo (7 bytes):** Patrón alternado de `0`s y `1`s que indica el inicio de la trama y permite la sincronización de bits entre el remitente y el receptor. \<br\> \* **SFD (Start Frame Delimiter - Delimitador de Inicio de Trama) (1 byte):** Siempre tiene el valor `10101011` e indica que los próximos bits corresponden a la trama de datos real. |
| **MAC de Destino** | 6 bytes | Dirección MAC del dispositivo al que se destina la trama. |
| **MAC de Origen** | 6 bytes | Dirección MAC del dispositivo que envía la trama. |
| **Longitud / Tipo** | 2 bytes | Indica la longitud del paquete de datos de las capas superiores o el tipo de protocolo de capa superior encapsulado (ej. IP). |
| **Paquete de Datos** | 46 - 1500 bytes | El paquete de datos real proveniente de la capa de red (Capa 3, ej. un paquete IP). |
| **CRC (Cyclic Redundancy Check) / FCS (Frame Check Sequence)** | 4 bytes | Un *checksum* o valor de comprobación de redundancia cíclica. Se utiliza para detectar errores y verificar que la información recibida no ha sido modificada o corrompida durante la transmisión. |

**Nota sobre la subcapa LLC:** Las cabeceras de la subcapa **LLC** son opcionales y rara vez se usan en redes modernas, ya que la mayoría de las redes utilizan el protocolo **IP** en la capa de red y se da por hecho que el tipo de protocolo se indica en el campo "Longitud / Tipo" de la trama Ethernet.

## 3\. Protocolo ARP (Address Resolution Protocol)

El protocolo **ARP** es un protocolo de la **capa de enlace de datos** cuya función principal es encontrar la **dirección hardware (dirección MAC)** que corresponde a una dirección IP determinada. Es decir, traduce direcciones lógicas (IP) a direcciones físicas (MAC).

### 3.1. Funcionamiento de ARP

El funcionamiento de ARP se basa en un mecanismo de solicitud y respuesta:

1.  Un dispositivo (host) que conoce la dirección IP de otro dispositivo en la misma red, pero no su dirección MAC, envía una **trama ARP Request** a toda la red.
2.  Esta solicitud se envía utilizando la **dirección MAC de broadcast** (`FF:FF:FF:FF:FF:FF`).
3.  La trama ARP Request contiene la dirección IP de la cual se desea conocer la MAC.
4.  El dispositivo que posee la dirección IP por la que se pregunta responde con una **trama ARP Reply**, que contiene su propia dirección MAC.
5.  Una vez que un host ha realizado esta traducción, almacena la dirección MAC obtenida en una **caché** local, conocida como la **tabla ARP**. Esto reduce el retardo y la carga de la red, evitando enviar una solicitud ARP cada vez que se necesita comunicarse con un dispositivo conocido.
6.  Las entradas de la tabla ARP tienen un tiempo de vida y se borran periódicamente, ya que las direcciones físicas pueden cambiar (ej. cambio de tarjeta de red o de dirección IP de un host).

Como analista de ciberseguridad, la tabla ARP es crucial para detectar ataques de **ARP Spoofing/Poisoning**, donde un atacante manipula esta tabla para redirigir el tráfico.

### 3.2. Casos de Uso de ARP

ARP se utiliza en varios escenarios de comunicación en red:

  * **Comunicación entre dos hosts en la misma red:** Cuando un host necesita enviar un paquete IP a otro host en la misma red, utiliza ARP para obtener la dirección MAC del destino.
  * **Comunicación entre hosts en redes diferentes (a través de un router):** Cuando dos hosts están en redes diferentes y necesitan comunicarse a través de un *gateway* (router), el host de origen usa ARP para obtener la dirección MAC del *gateway*. El router, a su vez, utilizará ARP en la red de destino para encontrar el host final.
  * **Router a host a través de otro router:** Cuando un router necesita enviar un paquete a un host en otra red a través de otro router.
  * **Router a host en la misma red:** Cuando un router necesita enviar un paquete a un host que se encuentra directamente en su misma red.

### 3.3. Estructura del Paquete ARP

Un paquete ARP tiene un tamaño total de **28 bytes** y contiene varios campos:

| Campo | Tamaño | Descripción |
| :---- | :----- | :---------- |
| **Tipo de Hardware (HTYPE)** | 2 bytes | Indica el protocolo de enlace de red que se está utilizando. Para **Ethernet**, el valor es `1`. |
| **Tipo de Protocolo (PTYPE)** | 2 bytes | Especifica el protocolo de red para el cual se destina la solicitud ARP. Para **IPv4**, el valor es `0x0800`. |
| **Longitud de Dir. Hardware (HLEN)** | 1 byte | Longitud en octetos de las direcciones de hardware. Para direcciones **MAC**, es `6` octetos. |
| **Longitud de Dir. Protocolo (PLEN)** | 1 byte | Longitud en octetos de las direcciones de protocolo. Para **IPv4**, es `4` octetos. |
| **Código de Operación (OPER)** | 2 bytes | Indica el tipo de operación ARP:\<br\> \* `1`: **ARP Request** (solicitud de una MAC para una IP específica).\<br\> \* `2`: **ARP Reply** (respuesta con la dirección MAC correspondiente). |
| **Dirección Hardware del Remitente (SHA)** | 6 bytes | Dirección MAC del host que envía el paquete. |
| **Dirección de Protocolo del Remitente (SPA)** | 4 bytes | Dirección IP del host que envía el paquete. |
| **Dirección Hardware del Destinatario (THA)** | 6 bytes | Dirección MAC del host receptor. En una solicitud ARP Request, este campo se ignora (suele ser `00:00:00:00:00:00`), ya que es lo que se desea conocer. |
| **Dirección de Protocolo del Destinatario (TPA)** | 4 bytes | Dirección IP del host receptor. |

Aquí se muestra la estructura visual de un paquete ARP:

### 3.4. Protocolos Derivados de ARP: RARP e InARP

Existen protocolos derivados de ARP que realizan funciones inversas o específicas:

  * **RARP (Reverse ARP - ARP Inverso):**

      * Este protocolo es el caso **contrario a ARP**.
      * Se utiliza para obtener una **dirección IP** a partir de una **dirección MAC**. Era comúnmente usado por *hosts* sin disco para obtener su dirección IP de un servidor RARP.

  * **InARP (Inverse ARP - ARP Inverso):**

      * Se utiliza en redes específicas, como **Frame Relay**, para obtener **direcciones de la capa de red (direcciones IP)** a partir de **direcciones de la capa de enlace de datos** (ej. identificadores de conexión de Frame Relay). Es una variante de ARP adaptada a ciertas tecnologías de red.

Comprender la Capa de Enlace, el funcionamiento de Ethernet y el protocolo ARP es fundamental para un analista de ciberseguridad, ya que son la base para entender cómo se comunican los dispositivos en una red local y cómo pueden ser explotadas estas comunicaciones en ataques de bajo nivel.