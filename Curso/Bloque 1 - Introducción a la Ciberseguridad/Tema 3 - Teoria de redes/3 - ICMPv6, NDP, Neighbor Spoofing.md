# Protocolo ICMPv6 y Descubrimiento de Vecinos: Fundamentos y Ataques en Redes IPv6

Este informe explora el **Protocolo de Mensajes de Control de Internet versión 6 (ICMPv6)**, su papel fundamental en las redes IPv6 y su estrecha relación con el **Protocolo de Descubrimiento de Vecinos (NDP)**. Se detallarán los mensajes clave de NDP, **Neighbor Solicitation (NS)** y **Neighbor Advertisement (NA)**, y se analizará el ataque de seguridad conocido como **Neighbor Spoofing** o envenenamiento de vecinos.

## 1\. Protocolo ICMPv6: El Corazón de Control en IPv6

**ICMPv6 (Internet Control Message Protocol Version 6)** es una parte fundamental de las redes IPv6 y es su importancia se refleja especialmente en el correcto funcionamiento del **Protocolo de Descubrimiento de Vecinos (NDP)**.

### 1.1. Funciones Principales de ICMPv6

ICMPv6 ofrece diversas funcionalidades esenciales para la operación y diagnóstico de las redes IPv6:

  * **Errores en la Entrega de Paquetes**: Es el responsable de informar sobre cualquier error en la entrega de paquetes IPv6. Por ejemplo, si un paquete no puede ser entregado a su destino (por una ruta incorrecta o un tiempo de vida expirado), un nodo puede enviar un mensaje ICMPv6 de error (como "destino inalcanzable" o "tiempo de vida excedido") al nodo de origen.
  * **Redirecciones**: Puede utilizarse para redirigir paquetes dentro de una red IPv6. Cuando un *router* determina que un paquete debería ser enviado por un camino diferente al especificado, puede enviar un mensaje ICMPv6 de redirección al nodo de origen para informarle sobre la mejor ruta a seguir.
  * **Mensajes de Solicitud y Respuesta de Eco (Ping)**: Similar a ICMP en IPv4, ICMPv6 se incluyen también los mensajes de **Echo Request** y **Echo Reply**, que son comúnmente conocidos como los paquetes Ping. Estos mensajes se utilizan para verificar la conectividad entre dos nodos y medir la latencia de la red.
  * **Gestión de Mensajes Multicast**: ICMPv6 también se utiliza para la gestión de mensajes **multicast**, como la membresía de grupos de multidifusión y la detección de nodos vecinos.
  * **Mensajes de Información y Diagnóstico**: Puede transportar mensajes de información y diagnóstico sobre el estado y la configuración de la red, como el mensaje de solicitud de información de enlace (**Router Solicitation - RS**) y el mensaje de anuncio de información de enlace (**Router Advertisement - RA**).

## 2\. Protocolo de Descubrimiento de Vecinos (NDP)

El **Protocolo de Descubrimiento de Vecinos (NDP - Neighbor Discovery Protocol)** es una de las funciones más destacadas de ICMPv6. NDP es un protocolo de **capa de enlace** que se encarga de varias funciones esenciales en una red IPv6, para facilitar la comunicación entre nodos en la misma red local.

### 2.1. Funciones Clave de NDP

Las principales funciones de NDP son vitales para la conectividad y eficiencia de las redes IPv6:

  * **Descubrimiento de Vecinos**: Permite a los nodos **descubrir otros nodos** que están activos y disponibles dentro de la misma red local. Este proceso es fundamental para establecer la conectividad entre dispositivos en la red.
  * **Resolución de Direcciones**: Cuando un nodo necesita comunicarse con otro nodo en la misma red local, necesita traducir la **dirección de capa 3 (dirección IPv6) a la dirección de capa 2 (dirección MAC)**. NDP facilita este proceso de resolución de direcciones, asegurando una comunicación eficiente entre sí.
  * **Detección de Direcciones Duplicadas (DAD - Duplicate Address Detection)**: Aunque no se detalla en el texto, NDP también es responsable de asegurar que no haya direcciones IP duplicadas en la misma red, evitando conflictos y garantizando la conectividad.

Este proceso de descubrimiento y resolución se realiza mediante el envío y recepción de mensajes ICMPv6 específicos: los mensajes **Neighbor Solicitation (NS)** y **Neighbor Advertisement (NA)**.

### 2.2. Mensajes NS (Neighbor Solicitation)

Los mensajes **Neighbor Solicitation (NS)** son enviados por un nodo IPv6 cuando necesita comunicarse con otro nodo en la misma red local, pero **no tiene su dirección de capa 2 (dirección MAC)**.

  * **Propósito**: Son la "pregunta" en una red IPv6 para solicitar la dirección MAC de un vecino.
  * **Contenido**: Este mensaje incluye la dirección IPv6 del nodo destino cuya MAC se busca y la dirección IPv6 del nodo que envía la solicitud.

### 2.3. Mensajes NA (Neighbor Advertisement)

Los mensajes **Neighbor Advertisement (NA)** son la "respuesta" a las solicitudes NS o una forma proactiva de anunciar la presencia de un nodo.

  * **Propósito**: Cuando un nodo recibe un mensaje NS dirigido a él, responde con un mensaje NA que contiene su propia **dirección de capa 2**. Esto permite al nodo que envió la solicitud actualizar su caché de vecinos y continuar con la comunicación.
  * **Uso Proactivo**: Los mensajes NA también pueden enviarse de forma proactiva para simplemente anunciar la presencia de un nodo en la red. Esto es útil para asegurar que otros nodos tienen la información de capa 2 necesaria para comunicarse, incluso si no la han solicitado explícitamente.

## 3\. Neighbor Spoofing (Envenenamiento o Suplantación de Vecinos)

El **Neighbor Spoofing** es una técnica de ataque peligrosa que compromete la seguridad en redes IPv6. Ocurre cuando un atacante **falsifica los mensajes NS o NA** para suplantar la identidad de un nodo legítimo en la red.

  * **Mecanismo**: El atacante engaña a otros nodos de la red haciéndoles creer que es él el nodo legítimo al que se están intentando comunicar.
  * **Analogía**: Esto sería algo parecido a un **envenenamiento de la tabla ARP** en redes IPv4.

### 3.1. Actividades Maliciosas Asociadas

Cuando un atacante logra suplantar la identidad de un nodo legítimo, puede llevar a cabo una serie de actividades maliciosas, tales como:

  * **Interceptar y manipular el tráfico de red**: El atacante se posiciona como un intermediario entre dos hosts, lo que le permite ver o modificar el tráfico.
  * **Robar información confidencial**: Si la información viaja sin cifrar, el atacante puede capturarla.
  * **Lanzar ataques de Denegación de Servicio (DDoS - Denial of Service)**: Interrumpiendo el funcionamiento normal de la red.

### 3.2. Medidas de Mitigación

Existen medidas para mitigar este tipo de ataques:

  * **Autenticación de Mensajes NDP**: Implementar mecanismos como **Secure Network Discovery (SEND)** para autenticar los mensajes NDP.
  * **Configuración de Listas Blancas de Direcciones MAC**: Limitar qué nodos se pueden comunicar entre sí basándose en sus direcciones MAC permitidas.

## 4\. Conclusión

ICMPv6 es un protocolo fundamental para la administración y el mantenimiento de las redes IPv6, siendo esencial para el correcto funcionamiento del NDP. El Protocolo de Descubrimiento de Vecinos (NDP) es una parte integral de IPv6 que facilita funciones clave como el descubrimiento de vecinos y la resolución de direcciones. Los mensajes Neighbor Solicitation (NS) y Neighbor Advertisement (NA) son componentes esenciales de NDP, utilizados para solicitar y anunciar direcciones de capa 2 respectivamente. Finalmente, el Neighbor Spoofing es una técnica de ataque que permite suplantar estos nodos legítimos simplemente enviando por ellos mismos esta serie de mensajes NS y NA.

-----