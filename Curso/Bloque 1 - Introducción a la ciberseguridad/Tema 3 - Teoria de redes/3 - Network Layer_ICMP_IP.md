# Fundamentos de la Capa de Internet: IP e ICMP

Para cualquier experto en ciberseguridad, comprender en detalle los protocolos de la Capa de Internet es fundamental. Estos protocolos son la base para el enrutamiento global de datos y, por tanto, el objetivo de muchos tipos de ataques. Un conocimiento profundo de cómo funcionan el Protocolo IP y el Protocolo ICMP permite una mejor detección de anomalías, diagnóstico de problemas de red y una comprensión más clara de las vulnerabilidades.

## 1\. La Capa de Internet (Internet Layer)

La Capa de Internet, también conocida como Capa de Red o Capa IP, es un nivel crucial en las redes de comunicación que se encarga de transportar datos entre diferentes redes, independientemente de la ubicación física o la tecnología subyacente. Sus objetivos principales son el **direccionamiento**, el **enrutamiento** y la **manipulación de paquetes**.

### 1.1. Objetivos Principales de la Capa de Internet

  * **Direccionamiento:** Asignación de direcciones únicas, conocidas como **direcciones IP**, a cada dispositivo conectado a la red. Estas direcciones actúan como identificadores únicos que permiten enviar datos de manera precisa a su destino.
  * **Enrutamiento (Routing):** Una vez que un paquete tiene una dirección IP de destino, la Capa de Internet determina la mejor ruta posible para que el paquete llegue a su destino. Esto implica tomar decisiones sobre el camino más rápido y eficiente, lo que puede involucrar múltiples nodos de red y diferentes tipos de conexiones para optimizar el flujo de datos.
  * **Manipulación de Paquetes:** Los datos a menudo son demasiado grandes para enviarse en una sola unidad. Por lo tanto, esta capa se encarga de dividir los datos en unidades más pequeñas llamadas **paquetes**. Cada paquete contiene una porción de los datos originales, junto con información de control como la dirección IP de origen y destino. Estos paquetes pueden viajar independientemente a través de la red y, una vez que llegan a su destino, son reensamblados para reconstruir los datos originales.

### 1.2. Protocolos de la Capa de Internet

Los protocolos más importantes de esta capa incluyen:

  * **IP (Internet Protocol):** El protocolo principal, encargado de encapsular los datos en datagramas para su envío a través de la red. Existen dos versiones:
      * **IPv4:** Utiliza direcciones de 32 bits.
      * **IPv6:** Utiliza direcciones de 128 bits, lo que permite un número mucho mayor de dispositivos conectados.
  * **ICMP (Internet Control Message Protocol):** Se utiliza para informar de errores en la transmisión de datagramas IP (paquetes perdidos, direcciones incorrectas, etc.) y para realizar diagnósticos de red y controlar el estado de los *hosts* (ej. mediante el comando `ping`).
  * **NDP (Neighbor Discovery Protocol):** Es el equivalente a ARP pero para IPv6. Se utiliza para mapear direcciones IPv6 a direcciones MAC.
  * **ECN (Explicit Congestion Notification):** Permite a los dispositivos de red notificarse entre sí cuando se produce congestión en la red, helping to avoid overload and improve overall network performance.
  * **IGMP (Internet Group Management Protocol):** Se utiliza para que los *hosts* puedan unirse y abandonar grupos de multidifusión (*multicast*), lo que permite la transmisión eficiente de datos a múltiples destinatarios.

Aquí se muestra la ubicación de estos protocolos dentro de la Capa de Internet:

## 2\. Protocolo IP (Internet Protocol)

El Protocolo IP tiene como propósito mover datagramas a lo largo de un conjunto interconectado de redes. A diferencia de **Ethernet**, que se centra en el segmento de red local, IP permite conectar diferentes segmentos de red. En esta sección, nos enfocaremos principalmente en **IPv4**.

### 2.1. Características del Protocolo IP

El Protocolo IP tiene dos características fundamentales:

  * **No orientado a conexión:** Los paquetes se enrutan a su destino como entidades individuales, sin que exista un acuerdo o conexión previa entre el origen y el destino.
  * **No confiable:** IP no asegura ni la entrega del paquete ni el orden de llegada. La red, por diseño, puede perder paquetes, no entregarlos a su destino, o que queden "dando vueltas". Para asegurar la confiabilidad, se recurre a capas superiores, como la Capa de Transporte con el protocolo **TCP**, que añade reglas para garantizar la entrega y el orden.

### 2.2. Formato del Datagrama IP

Un datagrama IP es la unidad de datos que IP mueve a través de las redes. Su formato incluye varios campos esenciales:

| Campo | Bits | Descripción |
| :---- | :--- | :---------- |
| **Versión** | 4 | Indica la versión del protocolo IP utilizada (ej. 4 para IPv4, 6 para IPv6). |
| **IHL (Internet Header Length)** | 4 | Longitud de la cabecera IP, en palabras de 32 bits. |
| **TOS (Type of Service)** | 8 | Permite priorizar el tráfico o diferenciar servicios (también conocido como **Calidad de Servicio - QoS**). |
| **Total Length** | 16 | Longitud total del paquete IP, incluyendo la cabecera y los datos. El tamaño máximo es 65.535 bytes. |
| **Identification** | 16 | Número de identificación del datagrama. Si un paquete se fragmenta, todos los fragmentos del mismo datagrama original tendrán el mismo valor en este campo. |
| **Flags** | 3 | Contiene bits de control para la fragmentación:\<br\> \* **DF (Don't Fragment):** Indica a los *routers* que no deben fragmentar este paquete.\<br\> \* **MF (More Fragments):** Indica que este fragmento no es el último. Si es el último, el bit es `0`; si no, es `1`. En paquetes no fragmentados, este bit es siempre `0`. |
| **Fragment Offset** | 13 | Indica la posición del fragmento en el datagrama original. Para el primer fragmento o un datagrama no fragmentado, el valor es `0`. |
| **TTL (Time To Live)** | 8 | Tiempo máximo (en segundos o saltos de *router*) que el paquete puede estar vivo en la red. En cada salto (entre un *router* y otro), este contador se resta en `1`. Cuando llega a `0`, el paquete se descarta y no se reenvía. |
| **Protocol** | 8 | Describe la carga útil del paquete, es decir, el protocolo de la capa superior encapsulado. Ejemplos de códigos (definidos por IANA): `1` para ICMP, `6` para TCP, `17` para UDP. |
| **Header Checksum** | 16 | Suma de verificación calculada a partir de los datos de la cabecera para detectar errores. Se recalcula cada vez que cambia el TTL para asegurar la consistencia en el destino. |
| **Source Address** | 32 | Dirección IP de origen del paquete. |
| **Destination Address** | 32 | Dirección IP de destino del paquete. |
| **Options** | Variable (0-40 bytes) | Campo opcional que no se suele utilizar. Algunos *routers* pueden bloquear paquetes con ciertas opciones por seguridad. |
| **Data** | Variable (hasta 65515 bytes) | Los datos que provienen de la capa anterior (transporte) o que se desean enviar. |

### 2.3. Direccionamiento IP

Una dirección IP es un número de **32 bits** (para IPv4) que identifica de forma única a un *host* dentro de una red. Un *host* puede tener varias direcciones IP, una por cada interfaz de red.

Una dirección IP se divide en dos partes:

  * **NetID (Network ID):** Identifica la red a la que pertenece el *host* (ej. `192.168.3.0/24`).
  * **HostID (Host ID):** Identifica al *host* dentro de esa red.

La **máscara de red** (ej. `/24`) indica qué parte de la dirección IP corresponde al NetID y cuál al HostID.

**Ejemplo de una red `/24`:**
Para la red `192.168.3.0/24` con máscara `255.255.255.0`:

  * **Dirección de Red:** `192.168.3.0` (identifica la red, no se asigna a un *host*).
  * **Rango de Hosts Utilizables:** `192.168.3.1` a `192.168.3.254`.
  * **Dirección de Broadcast:** `192.168.3.255` (se utiliza para enviar datos a todos los *hosts* de la red, no se asigna a un *host*).
  * **Total de Hosts Posibles:** 256.
  * **Número de Hosts Utilizables:** 254 (256 - 2, por las direcciones de red y *broadcast*).

### 2.4. Direcciones IP Especiales y Privadas

Existen direcciones IP con funciones especiales y rangos reservados para uso privado:

**Direcciones Especiales:**

  * **`0.0.0.0`:** Indica que se escucha en cualquier interfaz. Se usa al levantar un servidor para que escuche en todas las interfaces de red.
  * **`255.255.255.255`:** Dirección de *broadcast* global. Se usa para dirigirse a todos los *hosts* en la red local.
  * **`192.168.3.0`:** Ejemplo de dirección de red (el `HostID` es todo ceros).
  * **`192.168.3.255`:** Ejemplo de dirección de *broadcast* para una subred.
  * **`127.0.0.1`:** Dirección de *loopback* o *localhost*. Permite que una máquina se dirija a sí misma a través de una interfaz virtual interna, sin necesidad de conocer su dirección IP real en la red.

**Direcciones Privadas:**

El RFC 1918 define bloques de direcciones IP reservados para direccionamiento privado. Los paquetes con una dirección de destino privada nunca deben salir de la red local hacia Internet. Estos rangos son:

  * **`10.0.0.0/8`**
  * **`172.16.0.0/12`**
  * **`192.168.0.0/16`**

Estas son las direcciones que comúnmente encontramos en redes domésticas, escolares u organizacionales.

### 2.5. Enrutamiento IP (IP Routing)

Todos los *hosts* poseen una **tabla de enrutamiento** que asocia parejas de dirección IP y máscara de red con un método de entrega. Existen dos métodos principales de entrega:

  * **Entrega Directa:** Ocurre cuando el destino es un *host* vecino en la misma red (comunicación entre dos ordenadores en la misma LAN) o cuando es el último salto de un *router* al destino final.
  * **Entrega Indirecta:** La tabla de enrutamiento contiene la dirección del "próximo salto" (*next hop*), es decir, la dirección del *gateway* o *router* al que se debe enviar el paquete para que este lo reenvíe a su destino final (ej. para ir a Internet).

Un *host* determina si la entrega es directa o indirecta mediante los siguientes pasos:

1.  Calcula la dirección de red del destino usando la máscara de red y la dirección IP de destino del paquete.
2.  Comprueba si esta dirección de red es su propia dirección de red.
3.  Si es afirmativo, la entrega es directa (el emisor está en la misma red que el destino).
4.  En cualquier otro caso, la entrega es indirecta.

Si la entrega es indirecta, se realiza un **reenvío** del paquete. La tabla de enrutamiento se consulta para encontrar el camino hacia el destino final.

Para visualizar la tabla de enrutamiento en Windows, se puede usar `route PRINT` en Powershell.

En el ejemplo de la tabla:

  * La primera columna (`Network Destination`) indica la red o *host* de destino.
  * La columna `Interface` muestra la interfaz por donde debe salir el tráfico.
  * La primera fila (`0.0.0.0` con `Netmask 0.0.0.0`) representa la **ruta por defecto**, indicando que para cualquier dirección IP, el próximo salto (`Gateway`) es el *router* `192.168.3.1`.
  * La **métrica** (última columna) indica el coste asociado a esa ruta. Un valor menor de métrica significa una ruta más preferida. Windows calcula esta métrica basándose en la velocidad de conexión, distancia, fiabilidad, etc.

### 2.6. Tipos de Enrutamiento

Existen dos tipos principales de enrutamiento:

  * **Enrutamiento Estático:**

      * Los administradores de red configuran manualmente las rutas en los *routers* y *hosts*.
      * **Ventajas:** Simple de configurar y entender.
      * **Desventajas:** Cualquier cambio en la red requiere una actualización manual de la configuración de enrutamiento en todos los dispositivos afectados, lo que puede ser laborioso.

  * **Enrutamiento Dinámico:**

      * Los *routers* utilizan **protocolos de enrutamiento** (ej. **OSPF - Open Shortest Path First**, **EIGRP - Enhanced Interior Gateway Routing Protocol**, **RIP**) para intercambiar información sobre las redes disponibles y seleccionar automáticamente las mejores rutas para enviar datos.
      * **Ventajas:** Las rutas se adaptan automáticamente a los cambios en la topología de red, reduciendo la carga administrativa.
      * **Desventajas:** Puede generar mayor tráfico en la red y requiere una configuración más compleja. La configuración automática no siempre es la más eficiente.

## 3\. Protocolo ICMP (Internet Control Message Protocol)

El Protocolo ICMP sirve como **complemento al Protocolo IP**. Dado que IP es un protocolo no orientado a conexión y no confiable (no asegura la entrega ni el orden de los paquetes), ICMP es fundamental para suministrar información sobre el estado de la red y los errores que se producen. Los mensajes ICMP se encapsulan dentro de paquetes IP.

### 3.1. Casos de Uso de ICMP

ICMP tiene varios casos de uso populares:

  * **Ping:** El uso más conocido. Se envía un mensaje **ICMP Echo Request** y se espera un **ICMP Echo Reply** para comprobar si un *host* es alcanzable y está activo.
  * **Traceroute:** Utiliza mensajes ICMP de tipo "Tiempo Excedido" (`Time Exceeded`) y valores de **TTL** (Time To Live) gradualmente crecientes para descubrir los *routers* e IPs por los que pasa un paquete en su camino hacia un destino.
  * **Diagnóstico de Problemas de Conectividad:** Varios mensajes ICMP proporcionan información sobre problemas de red encontrados durante la transmisión de paquetes, ayudando a diagnosticar fallos.
  * **Descubrimiento de MTU de Ruta (Path MTU Discovery):** Los mensajes ICMP de tipo "Paquete Demasiado Grande" (`Packet Too Big`) se utilizan para descubrir la **MTU** (Maximum Transmission Unit) de una ruta, es decir, el tamaño máximo del paquete que se puede transmitir sin fragmentar a lo largo de un camino.
  * **Reporte de Errores (Error Reporting):** *Routers* y *hosts* utilizan ICMP para reportar errores encontrados durante el procesamiento de paquetes IP. Estos errores incluyen:
      * **Destino Inalcanzable (Destination Unreachable):** La red, *host*, protocolo o puerto de destino no es accesible.
      * **Tiempo Excedido (Time Exceeded):** El TTL de un paquete ha llegado a `0`.
      * **Problema de Parámetro (Parameter Problem):** Indica un problema con el encabezado IP.
  * **Redireccionamiento (Redirect):** Los mensajes ICMP de redirección informan a los *hosts* de una red sobre un mejor *router* o "siguiente salto" para llegar a un destino particular, lo que ayuda a optimizar los caminos de los paquetes.

### 3.2. Formato del Datagrama ICMP

La cabecera ICMP **no reemplaza** la cabecera IP, sino que la **complementa** y se apoya en ella. Un paquete ICMP viaja *dentro* de la sección de datos de un paquete IP.

| Campo | Bits | Descripción |
| :---- | :--- | :---------- |
| **Type (Tipo)** | 8 | Identifica el tipo de mensaje ICMP (ej. `0` para Echo Reply, `3` para Destination Unreachable, `8` para Echo Request). |
| **Code (Código)** | 8 | Subtipo del mensaje ICMP, que proporciona información más específica sobre el mensaje. El código varía en función del tipo (ej. para Tipo `3` (Destination Unreachable): `0` para Red Inalcanzable, `1` para Host Inalcanzable, `2` para Protocolo Inalcanzable, `3` para Puerto Inalcanzable). |
| **Checksum** | 16 | Suma de verificación calculada a partir de la cabecera y los datos ICMP para detectar errores. |
| **Content (Contenido)** | Variable (4 bytes) | Campo que varía dependiendo del tipo y código del mensaje ICMP. |

### 3.3. Mensajes de Control ICMP (Tipos y Códigos)

La IANA (Internet Assigned Numbers Authority) mantiene una tabla con todos los tipos y códigos de mensajes ICMP. Algunos ejemplos importantes son:

  * **Tipo 0: Echo Reply:**
      * Código 0: Respuesta a un Echo Request (Ping).
  * **Tipo 3: Destination Unreachable (Destino Inalcanzable):**
      * Código 0: Red Inalcanzable.
      * Código 1: Host Inalcanzable.
      * Código 2: Protocolo Inalcanzable.
      * Código 3: Puerto Inalcanzable.
      * ... (y otros códigos que informan sobre problemas en la conexión).
  * **Tipo 5: Redirect (Redirección):**
      * Varios códigos para informar sobre redireccionamientos.
  * **Tipo 8: Echo Request:**
      * Código 0: Solicitud de eco (Ping).
  * **Tipo 11: Time Exceeded (Tiempo Excedido):**
      * Utilizado en `traceroute` para indicar que el TTL de un paquete ha expirado.

Comprender la relación entre los tipos y códigos de ICMP es esencial para interpretar los mensajes de error de la red y para la detección de anomalías o actividades maliciosas. Los RFCs de cada tipo de mensaje ofrecen información más profunda.