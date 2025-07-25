# Redes de Ordenadores: Fundamentos y Conceptos Clave

En el mundo digital actual, las redes de ordenadores son la columna vertebral de la comunicación, permitiendo la interconexión de dispositivos y el intercambio de información a escala global.

## ¿Qué es una Red de Ordenadores?

Una **red de ordenadores** es un conjunto de hardware y dispositivos electrónicos distribuidos y conectados entre sí que permiten la transmisión y comunicación de información entre diferentes elementos, incluso a grandes distancias. Esto incluye la infraestructura necesaria como switches, routers, cables submarinos, etc.

### Puntos Clave y Características de las Redes

  * **Conectividad:** Permite interconectar una amplia gama de dispositivos como equipos, servidores, impresoras, dispositivos NAS y televisores para compartir recursos y datos.
  * **Compartición de Recursos:** Facilita el acceso a recursos compartidos como archivos, impresoras, bases de datos y aplicaciones, lo cual es esencial para la productividad en las organizaciones.
  * **Escalabilidad:** Las redes deben ser capaces de crecer y adaptarse al aumento de dispositivos y usuarios.
  * **Flexibilidad:** Las redes deben ser configurables y adaptarse a los requisitos de usuarios y organizaciones, abarcando tanto redes cableadas como inalámbricas.
  * **Seguridad:** Una característica inherente a las redes. Deben proporcionar mecanismos para proteger la **confidencialidad**, **disponibilidad** e **integridad** de los datos que circulan por ellas, evitando accesos no autorizados o manipulaciones.
  * **Eficiencia:** Optimizan el uso de recursos, mejoran la productividad y facilitan el intercambio de información.
  * **Fiabilidad:** Deben proporcionar un servicio continuo y fiable, minimizando los tiempos de inactividad y garantizando la disponibilidad de recursos.

## Tipos de Redes

Las redes se clasifican según su alcance y propósito:

  * **LAN (Local Area Network):** Redes de área local, típicamente utilizadas en hogares y empresas para gestionar datos sensibles internamente. Pueden estar segmentadas con VLANs o Listas de Control de Acceso (ACLs) para mayor seguridad.
  * **WAN (Wide Area Network):** Redes de área extensa, como Internet. Están fuera del perímetro de nuestro hogar u organización y son configuradas por proveedores de servicios. La seguridad en WAN es más compleja debido a su naturaleza pública.
  * **PAN (Personal Area Network):** Redes de área personal, pequeñas redes formadas por dispositivos cercanos, como los que utilizan **Bluetooth** (ej. móvil, smartwatch).
  * **CAN (Campus Area Network):** Aunque no se menciona en detalle en las notas, típicamente abarca un área geográfica más grande que una LAN pero más pequeña que una WAN, como un campus universitario.
  * **Red de Área de Coche (CAN):** Redes específicas para vehículos, diseñadas para compartir información interna del coche (ej. contactos para manos libres).

## Topología de Red

La topología de red se refiere a la disposición física o lógica de los dispositivos en una red. Es importante para el diseño y la comprensión de los diagramas de red.

### Topología Física

Describe cómo los dispositivos están conectados físicamente. Algunos tipos clásicos incluyen:

  * **Bus:** Un medio compartido al que los dispositivos se añaden.
  * **Estrella:** Todos los dispositivos se conectan a un punto central (ej. un router). Si el punto central falla, toda la red puede quedar aislada.
  * **Anillo**
  * **Árbol**
  * **Malla (Todos los nodos conectados):** Ofrece alta tolerancia a fallos, ya que si un nodo cae, la red sigue funcionando gracias a las múltiples conexiones entre todos los nodos.
  * **Peer-to-Peer (P2P):** Los nodos no están todos conectados entre sí, pero hay una gran lista de nodos a los que conectarse, lo que también proporciona tolerancia a fallos.

### Topología Lógica

Se refiere a cómo los datos fluyen a través de la red, independientemente de la conexión física. Permite la creación de diagramas de red para visualizar el diseño, los dispositivos de interconexión, los equipos y las conexiones.

-----

# Arquitecturas de Red: OSI y TCP/IP

Las arquitecturas de red son fundamentales para estandarizar cómo se organiza y transmite la información en una red. Ayudan a identificar y solucionar problemas, incluyendo amenazas de seguridad.

## ¿Qué es una Arquitectura de Red?

Una arquitectura de red representa todos los elementos y protocolos necesarios para interconectar redes y permitir el envío de mensajes de un extremo a otro del mundo.

### Características Deseables de una Arquitectura de Red

  * **Elementos de Interconexión:** Imprescindibles para crear la red (ej. *switches*, *routers*).
  * **Escalabilidad:** Debe poder crecer según las necesidades, soportando la adición de nuevos nodos.
  * **Seguridad:** Debe proporcionar mecanismos para proteger la **integridad** de la información que viaja por la red.
  * **Fiabilidad:** Debe garantizar que los mensajes lleguen a su destino y, en caso de pérdida, tener mecanismos de reenvío.

## El Modelo OSI (Open Systems Interconnection)

El Modelo OSI es un **modelo de referencia** conceptual que surgió en 1983. No es una arquitectura de red, sino un marco estandarizado que describe cómo siete capas diferentes trabajan juntas para permitir la comunicación y la transferencia de datos en una red. Proporciona una comprensión profunda de los procesos en cada etapa, desde la interacción con el usuario hasta la conexión física.

Este modelo es más detallado que TCP/IP, ofreciendo una visión granular de la comunicación de red.

### Las 7 Capas del Modelo OSI

Las capas se leen desde la más baja (física) hasta la más alta (aplicación).

| Capa OSI | Descripción | Funciones Clave | Ejemplos/Protocolos |
| :------- | :---------- | :-------------- | :------------------ |
| **Capa 7: Aplicación** | La más cercana al usuario final. Proporciona servicios de red a las aplicaciones de usuario. | Interacción directa con el usuario a través de aplicaciones; solicitudes de red. | **HTTP**, **HTTPS**, **SMTP**, **DNS**, **FTP**, **SSH**. |
| **Capa 6: Presentación** | Se encarga de la representación de los datos, incluyendo cifrado y compresión. | Formato de datos, cifrado, compresión, confirmación de conjunto de caracteres. | **SSL/TLS** (cifrado). |
| **Capa 5: Sesión** | Gestiona el establecimiento, mantenimiento y terminación de sesiones de comunicación entre aplicaciones. | Mantenimiento y terminación de sesiones, autenticación, reconexión, puntos de control en transferencias. | |
| **Capa 4: Transporte** | Responsable de la entrega fiable de datos entre dispositivos, gestionando el flujo y la segmentación. | Entrega de datos entre dispositivos, control de flujo, **segmentación** de datos. | **TCP**, **UDP**. |
| **Capa 3: Red** | Encargada del **direccionamiento lógico** (IP) y el enrutamiento de paquetes entre diferentes redes. | Enrutamiento de paquetes entre redes, identificación del destino por **IP**, optimización de rutas. | **IP**, **ICMP**. |
| **Capa 2: Enlace de Datos** | Maneja el **direccionamiento físico** (MAC) y la gestión lógica de las tramas dentro de una *misma red*. | Gestión de flujo en red local, detección y corrección de errores en tramas, acceso al medio físico. | **Ethernet**, **Wi-Fi**, **ARP**, **NCP**, **HDLC**, **SDLC**. |
| **Capa 1: Física** | Corresponde al hardware físico involucrado en la transmisión de red. | Transmisión y recepción de datos a nivel físico (señales, impulsos eléctricos, bits). | Cables (Ethernet, coaxial), hubs, módems, Wi-Fi. |

**Características del Modelo OSI:**

  * **Abstracción:** Cada capa tiene funciones específicas y está aislada, simplificando el proceso y permitiendo modularidad en el diseño.
  * **Estandarización:** Define estándares para la comunicación entre sistemas.
  * **Independencia de Hardware y Software:** Las capas superiores operan independientemente del hardware y software subyacente (excepto la capa física).
  * **Interoperabilidad:** Permite que sistemas de diferentes fabricantes o sistemas operativos (Windows, Linux, Mac) se comuniquen y se entiendan.
  * **Seguridad:** Facilita la aplicación de seguridad en diferentes niveles, fortificando la seguridad general (ej. defensa en profundidad).
  * **Modularidad:** Cada capa puede ser modificada, actualizada o sustituida sin afectar al resto de capas.
  * **Comprensión:** Al estar dividido en funciones, facilita la comprensión de lo que hace cada capa.

## La Arquitectura TCP/IP

La arquitectura **TCP/IP (Transmission Control Protocol/Internet Protocol)** es la arquitectura de red más utilizada en el mundo y es la base de Internet. Es una versión más práctica y condensada del modelo OSI.

### Las Cuatro Capas del Modelo TCP/IP

El modelo TCP/IP agrupa las funcionalidades del modelo OSI en cuatro capas:

| Capa TCP/IP | Equivalencia OSI | Funciones Clave | Protocolos |
| :---------- | :--------------- | :-------------- | :--------- |
| **Capa de Aplicación** | Aplicación, Presentación, Sesión | Define protocolos para la interacción de aplicaciones con la red. La capa más cercana al usuario. | **HTTP**, **SMTP**, **FTP**, **SSH**, **DNS**. |
| **Capa de Transporte** | Transporte | Controla el flujo de tráfico y asegura la entrega de datos de extremo a extremo, gestionando el acceso de los procesos a la red mediante puertos. | **TCP** (fiable, orientado a conexión, garantiza entrega), **UDP** (no fiable, sin conexión, más rápido, para tiempo real como vídeo). |
| **Capa de Internet** | Red | Responsable del direccionamiento lógico (IP) y el enrutamiento de paquetes a través de diferentes redes para alcanzar su destino final. | **IP**, **ICMP**. |
| **Capa de Acceso a la Red (o Enlace de Datos)** | Física, Enlace de Datos | Se encarga de la transmisión física de paquetes, la gestión del acceso al medio (cable o aire) y la composición/descomposición de cabeceras. | **ARP**, **Ethernet**, **Wi-Fi**. |

**Comparación TCP/IP vs. OSI:**

Ambos modelos son marcos conceptuales para visualizar la organización y transmisión de datos en una red. Ayudan a ingenieros de red y analistas de seguridad a comprender los procesos de red y comunicar problemas.

  * El modelo **TCP/IP** es un modelo de cuatro capas, una forma condensada del modelo OSI, ampliamente utilizada en la práctica.
  * El modelo **OSI** es un concepto estandarizado de siete capas que proporciona una vista más granular de los procesos de comunicación de red.

Aunque algunas organizaciones prefieren un modelo sobre otro, es crucial que los analistas de seguridad y profesionales de red estén familiarizados con ambos para analizar eventos de red y comunicar problemas eficazmente. Ambos son herramientas invaluable para comprender las complejidades de las operaciones de red.

-----

# Encapsulación y Desencapsulación en TCP/IP

La **encapsulación** es un concepto fundamental en la comunicación de redes, especialmente en la arquitectura TCP/IP. Es el proceso mediante el cual los datos se van "embebido" en capas inferiores dentro de una arquitectura de red, añadiendo información de cabecera en cada nivel, hasta que se conforma una **trama de red** completa que puede salir de nuestro equipo en busca de la máquina de destino.

## El Proceso de Encapsulación

Para entenderlo, consideremos el envío de datos desde una aplicación en la máquina A (ej. un navegador) a una aplicación en la máquina B (ej. un servidor web).

1.  **Capa de Aplicación:**

      * La aplicación (ej. navegador) genera datos (ej. una petición **HTTP** GET).
      * Estos datos se entregan al protocolo de aplicación (ej. HTTP), que añade sus propias cabeceras y los pasa a la capa inferior.

2.  **Capa de Transporte:**

      * La capa de transporte recibe los datos de la capa de aplicación.
      * Le añade sus propias cabeceras (ej. puerto origen, puerto destino, *flags* **TCP** si es TCP, o nada si es **UDP**). La parte de "datos" para la capa de transporte incluye las cabeceras y datos de la capa de aplicación.
      * Esta unidad de datos con las cabeceras de transporte se pasa a la capa inferior, la capa de red.

3.  **Capa de Red (Internet):**

      * La capa de red recibe la información de la capa de transporte.
      * Su función principal es el **direccionamiento lógico** (direcciones IP) para enviar paquetes fuera de la red local.
      * Añade sus propias cabeceras, que incluyen la **IP origen** y la **IP destino**. La parte de "datos" para la capa de red incluye todo lo encapsulado por la capa de transporte.
      * Este "datagrama" se pasa a la capa de enlace.

4.  **Capa de Enlace de Datos (Acceso a la Red):**

      * La capa de enlace recibe el datagrama de la capa de red.
      * Su función es la comunicación dentro de la red local, añadiendo cabeceras con **direcciones MAC** (físicas) de origen y destino (que puede ser otra máquina en la red local o el **router** si el destino está fuera de la red).
      * La unidad de datos resultante se conoce como **trama de red** (ej. trama **Ethernet**) y es la que más ocupa, ya que contiene todos los protocolos encapsulados de las capas superiores.
      * Esta trama se envía al router o al destino local.

El proceso de encapsulación se puede visualizar como la adición progresiva de "sobres" o "cabeceras" alrededor de los datos originales a medida que descienden por las capas, haciendo que cada unidad de datos sea más grande que la anterior.

### Ilustración del Proceso de Encapsulación

A continuación, se muestra un diagrama que representa cómo los datos se encapsulan a través de las diferentes capas del modelo TCP/IP:

## El Rol del Router en la Encapsulación

Cuando una trama de red llega a un **router** (ej. el router de nuestra red), este opera a **nivel de red**.

1.  El router recibe la trama de la capa de enlace.
2.  Desencapsula las cabeceras de la capa de enlace para acceder al datagrama IP.
3.  Analiza la **IP destino** del paquete para determinar la mejor ruta de enrutamiento.
4.  No desencapsula más allá de la capa de red.
5.  Vuelve a encapsular el datagrama IP con una nueva cabecera de enlace de datos (para el siguiente salto o router) y lo reenvía hacia el destino.

### Ilustración del Proceso en un Router

El siguiente diagrama muestra cómo un router procesa la información:

## El Proceso de Desencapsulación

Una vez que los datos encapsulados llegan a la máquina de destino (Máquina B), ocurre el proceso contrario: la **desencapsulación**.

1.  **Capa de Enlace de Datos:**

      * La máquina de destino recibe la trama de red a través de su nivel de enlace.
      * Desencapsula las cabeceras de enlace de datos (las quita) y pasa el campo de "datos" restante a la capa superior, la capa de red.

2.  **Capa de Red (Internet):**

      * La capa de red recibe el datagrama.
      * Analiza sus propias cabeceras (IP de origen, IP de destino) y quita estas cabeceras.
      * Pasa el campo de "datos" a la capa superior, la capa de transporte.

3.  **Capa de Transporte:**

      * La capa de transporte recibe los datos de la capa de red.
      * Analiza sus cabeceras (puertos) y las quita.
      * El campo de "datos" ahora contiene el protocolo de aplicación (ej. **HTTP**).
      * Pasa estos datos a la capa de aplicación.

4.  **Capa de Aplicación:**

      * La capa de aplicación recibe los datos finales.
      * El proceso de la aplicación (ej. el servidor web) procesa la información solicitada.

### Ilustración del Proceso de Desencapsulación

El siguiente diagrama muestra cómo los datos se desencapsulan a medida que ascienden por las capas del modelo TCP/IP:

## La Importancia de la Encapsulación en Ciberseguridad

Comprender la encapsulación es crucial para la ciberseguridad por varias razones:

  * **Análisis de la Red:** Herramientas como **Wireshark** permiten visualizar las capas de los paquetes de red, sus protocolos y los diferentes niveles de encapsulación. Esto es fundamental para analizar el tráfico, identificar anomalías y diagnosticar problemas.
  * **Escaneos de Red y Enumeración:** El conocimiento de los protocolos y capas de TCP/IP es vital para realizar escaneos de red (**Network Scans**) y enumerar servicios. Esto permite identificar puertos abiertos, servicios en ejecución, versiones de aplicaciones, y máquinas activas en la red.
  * **Vulnerabilidades y Ataques:** Muchos ataques de red explotan vulnerabilidades en protocolos específicos en diferentes capas. Entender cómo los datos se encapsulan y desencapsulan ayuda a identificar dónde y cómo se pueden introducir o manipular datos maliciosos (ej. inyecciones, desbordamientos de búfer) o cómo se pueden ocultar ataques (ej. **Data Leaks**, **Ransomware**, **Phishing**).
  * **Fortificación de Redes:** El diseño por capas de las arquitecturas de red simplifica la complejidad y permite aplicar medidas de seguridad específicas en cada nivel, lo que fortalece la postura de seguridad general (similar al concepto de defensa en profundidad).
  * **Forensia Digital:** En caso de un incidente de seguridad, el análisis de paquetes capturados y su desencapsulación es clave para entender la secuencia de eventos del ataque y recolectar evidencia.

En resumen, la arquitectura de red y el proceso de encapsulación/desencapsulación son pilares fundamentales para cualquier profesional de la ciberseguridad, proporcionando la base para comprender, analizar y proteger los sistemas y datos en el entorno digital.