# Seguridad en Redes: Topología, Direccionamiento IP, Subnetting y Estrategias de Defensa

La seguridad de una red de datos es un pilar fundamental en cualquier organización. Para lograr una infraestructura robusta y resiliente, es imprescindible comprender la importancia de una correcta **topología de red**, una **segmentación eficiente (subnetting)**, una gestión adecuada del **direccionamiento IP**, y la implementación de mecanismos como **NAT**. Además, es crucial conocer las tácticas de los atacantes para realizar **ataques de denegación de servicio (DoS)** y cómo mitigar estas amenazas.

## 1. Topología de Red: La Base de la Seguridad

La **topología de red** es la disposición física o lógica de los elementos de una red. Comprenderla es crucial para la seguridad, ya que permite la identificación de vulnerabilidades potenciales, la colocación óptima de medidas de seguridad y una monitorización efectiva del flujo de tráfico de red. Al diseñar o auditar una arquitectura segura, una visión global de la topología es el punto principal a revisar. Es fundamental que el diseño se base en una topología eficiente para el tipo de negocio o funcionalidad que se ofrece.

Existen varias topologías de red comunes, cada una con sus características, ventajas y desventajas desde el punto de vista de la seguridad y escalabilidad:

### 1.1. Tipos de Topologías de Red

* **Topología en Anillo (Ring Topology)**:
    * **Diseño**: Los dispositivos están conectados en un bucle cerrado, formando un anillo.
    * **Ventajas**: Facilita la escalabilidad y la redirección del tráfico en caso de incidentes.
    * **Desventajas**: El control de la red se complica a medida que crece, lo que puede introducir puntos ciegos para la seguridad. Un fallo en un segmento puede interrumpir toda la comunicación si no hay redundancia.
* **Topología en Bus (Bus Topology)**:
    * **Diseño**: La información se transmite en una sola dirección a lo largo de un cable central al que se conectan todos los dispositivos.
    * **Ventajas**: Muy sencillas de implementar para redes pequeñas.
    * **Desventajas**: Son muy vulnerables, ya que un corte en el cable principal o un fallo en un dispositivo puede afectar a toda la red. No son robustas para entornos empresariales.
* **Topología en Estrella (Star Topology)**:
    * **Diseño**: Cada nodo cliente se conecta a un **dispositivo central**, como un switch. Las redes **LAN (Local Area Network)** son el ejemplo más claro de esta topología.
    * **Ventajas**: Reduce el impacto del fallo de un nodo, ya que solo afecta al nodo específico y no a toda la red. Facilita la resolución de problemas y la adición/eliminación de dispositivos.
    * **Desventajas**: El dispositivo central (switch) se convierte en un **punto único de fallo centralizado** (Single Point of Failure). Si este dispositivo deja de funcionar, toda la red cae. Esto lo convierte en un objetivo crítico para los atacantes.
* **Topología en Árbol (Tree Topology)**:
    * **Diseño**: Funciona como una extensión de la topología en estrella, añadiendo configuraciones en estrella de forma anidada en diferentes capas.
    * **Ventajas**: Permite una red más grande y jerárquica, facilitando la organización de grupos de trabajo.
    * **Desventajas**: Un fallo en un segmento superior puede aislar grandes porciones de la red. Sigue manteniendo un cierto nivel de centralización que puede ser un objetivo.
* **Topología en Malla (Mesh Topology)**:
    * **Diseño**: Es una mezcla de topología estrella con anillo, logrando una **interconexión total** entre los dispositivos. Las redes **Wi-Fi o wireless** suelen implementarse utilizando este tipo de topología.
    * **Ventajas**: Ofrece una infraestructura **más robusta** y tolerante a fallos, ya que si una ruta falla, existen múltiples caminos alternativos para que el tráfico llegue a su destino. Esto la hace muy resistente a los ataques DoS dirigidos a la conectividad.
    * **Desventajas**: Mayor complejidad de instalación y un coste potencialmente más alto debido a la cantidad de cableado y conexiones.

**Impacto de la Topología en la Seguridad (Hardening Mal Hecho)**:
Una topología mal diseñada puede crear **puntos ciegos** para la monitorización, **cuellos de botella** que pueden ser explotados para ataques de denegación de servicio, y **puntos únicos de fallo** que, si son comprometidos, paralizan la operación. Por ejemplo, en una topología en estrella, si el switch central no está endurecido (hardened) adecuadamente (sin acceso físico restringido, sin monitorización de tráfico, o con configuraciones por defecto), un atacante podría comprometerlo y tomar el control de toda la comunicación de la red local.

## 2. Direccionamiento IP y Subnetting

El **direccionamiento IP** es clave para la infraestructura de red y su securización. Asigna identificadores numéricos únicos a los dispositivos para el enrutamiento de datos. Un plan de direccionamiento IP detallado permite identificar y gestionar mejor los dispositivos. Es vital para la seguridad, ya que habilita el control de acceso, las reglas de firewall y la segmentación de red para mitigar riesgos como el acceso no autorizado y las filtraciones de datos (Data Leaks). Una gestión efectiva de IP facilita el registro (logging), la monitorización del tráfico de red y la detección de amenazas de seguridad.

### 2.1. Tipos de Direcciones IP

Existen dos tipos principales de direccionamiento IP:

* **Direcciones IP Públicas**: Son direcciones globales asignadas por la **IANA (Internet Assigned Numbers Authority)**. Son imprescindibles para ofrecer acceso a Internet a las redes empresariales y se utilizan para configurar redes como la **DMZ (Demilitarized Zone)** o routers.
* **Direcciones IP Privadas**: Son direcciones reservadas para uso interno para construir una red de comunicaciones. Cualquier empresa puede usar estas direcciones para configurar su propia red empresarial basada en el protocolo TCP/IP. No son enrutables en Internet.

**Rangos de Direcciones IP Privadas**:

| Rango                     | Máscara de Subred | Uso Común                                    |
| :------------------------ | :---------------- | :------------------------------------------- |
| `10.0.0.0 - 10.255.255.255` | `255.0.0.0`       | Grandes redes corporativas.                  |
| `172.16.0.0 - 172.31.255.255` | `255.240.0.0`     | Redes corporativas medianas.                 |
| `192.168.0.0 - 192.168.255.255` | `255.255.0.0`     | Redes locales, domésticas y pequeñas empresas. |

### 2.2. Subnetting (Segmentación de Red)

El **subnetting** es el proceso de dividir una red IP grande en subredes más pequeñas y manejables. Esto potencia la eficiencia al optimizar la asignación de direcciones y reducir los dominios de difusión (broadcast domains), lo que mejora la seguridad y la escalabilidad de la red.

#### 2.2.1. Notación CIDR

La notación de longitud de prefijo, también llamada **CIDR (Classless Inter-Domain Routing)**, es una forma de representar la dirección IP y su máscara de subred asociada. Utiliza un prefijo seguido por una barra diagonal y un número que indica cuántos bits de la dirección constituyen el prefijo de red. Por ejemplo, `/24` indica que los primeros 24 bits de la dirección son el prefijo de red.

#### 2.2.2. Componentes Clave en Subnetting

Una tabla de subnetting generalmente incluye las siguientes columnas:

* **Prefijo o Slash (Notación CIDR)**: Indica el número de bits del prefijo de red.
* **Máximas Direcciones Totales (Total IPs)**: El número máximo de direcciones IP que se pueden asignar dentro de la red o subred especificada. Se calcula como $2^{(32 - \text{longitud del prefijo})}$.
* **Hosts Disponibles (Usable IPs)**: El número de direcciones IP dentro de la subred que pueden ser asignadas a dispositivos. Generalmente, es el número máximo de direcciones menos 2, ya que una dirección se usa para identificar la subred misma y la otra como dirección de broadcast.
* **Longitud de Subred**: Es el mismo número que aparece después de la barra diagonal en la notación CIDR y representa el número de bits utilizados para la dirección de la subred en la máscara.
* **Máscara de Subred (Subnet Mask)**: Representa la máscara de subred asociada a la notación CIDR. Determina qué porción de la dirección IP representa la red y qué porción representa los hosts dentro de esa red. Es una serie de unos seguidos de ceros en la representación binaria, donde los unos representan los bits de la red y los ceros los bits del host.

**Ejemplo de una entrada en la tabla de Subnetting (conceptualizando la diapositiva):**

| Prefijo | Máximas Direcciones Totales (Total IPs) | Hosts Disponibles (Usable IPs) | Longitud de Subred | Máscara de Subred |
| :------ | :------------------------------------ | :----------------------------- | :----------------- | :---------------- |
| /24     | 256                                   | 254                            | 24                 | 255.255.255.0     |
| /28     | 16                                    | 14                             | 28                 | 255.255.255.240   |
| /30     | 4                                     | 2                              | 30                 | 255.255.255.252   |

#### 2.2.3. Direcciones IP Especiales

Existen direcciones IP especiales con propósitos específicos:

* **Local Host / Loopback**:
    * **Rango**: `127.0.0.0` a `127.255.255.255`.
    * **Uso**: Utilizada para pruebas en bucles internos (loopback), como `127.0.0.1` o `localhost`.
* **APIPA (Automatic Private IP Addressing)**:
    * **Rango**: `169.254.0.0` a `169.254.255.255`.
    * **Uso**: Asignadas automáticamente a máquinas cliente cuando no hay servidores DHCP presentes.
* **IP Bogon**:
    * **Significado**: Proviene de "BOGUS" (falso). Una IP Bogon es un paquete con una dirección IP que nunca debería aparecer en una Internet pública.
    * **Características**: Comúnmente son direcciones no asignadas o reservadas para redes privadas. No son legítimas cuando se ven en Internet público y son indicativas de redes mal configuradas o **actividad maliciosa**.
    * **Uso Malicioso y Contramedidas**: Dada su ilegitimidad, a menudo se utilizan en **filtrado para evitar tráfico no deseado** o para **suplantación (spoofing)** o **ataques de denegación de servicio (DoS)**. Filtrar las IP Bogon en los firewalls perimetrales es una medida de seguridad importante.

#### 2.2.4. Clases de Direcciones IP (Concepto Histórico)

Aunque CIDR ha reemplazado el sistema de clases para la asignación de direcciones, es útil conocer las clases históricas de IP:

| Clase | Rango                               | Máscara de Subred Estándar | Uso Típico                 |
| :---- | :---------------------------------- | :------------------------- | :------------------------- |
| A     | `0.0.0.0` a `127.255.255.255`       | `255.0.0.0`                | Redes muy grandes.         |
| B     | `128.0.0.0` a `191.255.255.255`     | `255.255.0.0`              | Redes medianas.            |
| C     | `192.0.0.0` a `223.255.255.255`     | `255.255.255.0`            | Redes pequeñas (domésticas, PYMES). |
| D     | `224.0.0.0` a `239.255.255.255`     | No aplicable               | Multidifusión (Multicast). |
| E     | `240.0.0.0` a `255.255.255.255`     | No aplicable               | Experimental.              |

**Consejos para Fortificar Sistemas (Hardening)**:

* **Plan de Direccionamiento Detallado**: Crear un plan de direccionamiento IP que permita identificar y gestionar fácilmente los dispositivos.
    * **Asignación por Rango**: Asignar rangos de IP específicos para diferentes tipos de dispositivos o departamentos (ej. `x.x.x.1` para gateways, `x.x.x.10` para servidores, `x.x.x.100` para PCs, `x.x.x.50` para impresoras). Esto ayuda a identificar dispositivos críticos.
    * **Reserva de Direcciones IP Críticas**: La reserva de direcciones IP para dispositivos de red y, sobre todo, para aquellos críticos, debe ser una de las tareas principales en el diseño de una arquitectura de red.
* **Segmentación de Red (Subnetting)**: Dividir la red en subredes más pequeñas. Esto no solo mejora la eficiencia, sino que también crea límites de seguridad, aislando segmentos de red. Si un segmento se ve comprometido, el daño puede contenerse.

## 3. DHCP: Gestión de Direcciones IP Dinámicas

El **DHCP (Dynamic Host Configuration Protocol)** es un servicio vital para el direccionamiento IP dinámico en una red privada.

* **Función Principal**: Un servidor DHCP se encarga de suministrar automáticamente direcciones IP a los dispositivos clientes. Debe estar perfectamente sincronizado con el plan de direccionamiento inicial.
* **Información Adicional**: Además de la dirección IP, DHCP también envía la dirección IP del **gateway** y las direcciones de los **DNS primario y secundario**.
* **Tiempo de Préstamo (Lease Time)**: Es posible configurar el tiempo durante el cual un dispositivo "presta" una dirección IP.
* **Identificación por MAC**: DHCP identifica a los clientes por su dirección MAC, lo que permite asignar una IP específica a un dispositivo o rango de dispositivos.
* **Reserva de Direcciones IP**: Una **dirección IP reservada** es suministrada por el servidor DHCP a un dispositivo específico basado en su MAC. Esto difiere de una **dirección IP estática**, que se configura manualmente en el dispositivo y su tarjeta de red. Las direcciones estáticas se usan para servicios y servidores críticos (routers, switches, servidores VPN) donde un cambio de IP o un fallo de DHCP podría tener consecuencias en la infraestructura.

### 3.1. Comparativa: IP Estática vs. IP Dinámica (DHCP)

| Aspecto           | IP Estática                                | IP Dinámica (DHCP)                           |
| :---------------- | :----------------------------------------- | :------------------------------------------- |
| **Estabilidad** | Red más estable, las IPs no cambian.      | Potencial de conflictos de IP, agotamiento del pool. |
| **Acceso Remoto** | Más fácil para acceso remoto y servicios de hosting. | Más difícil, a menos que se use un servicio Dynamic DNS. |
| **Control de Acceso** | Más fácil de implementar listas de control de acceso. | Más difícil de gestionar debido a IPs cambiantes. |
| **Monitoreo** | Más sencillo de rastrear y monitorear la actividad. | Más desafiante, requiere mapear IPs a dispositivos constantemente. |
| **Configuración** | Requiere configuración manual, propenso a errores. | Asignación automática simplifica la configuración en redes grandes. |
| **Vulnerabilidad** | Potencialmente más vulnerable si no se gestiona bien (IP constante). | Menos predecible, puede ofrecer una capa de oscuridad contra ataques. |
| **Escalabilidad** | Menos escalable debido a la asignación manual. | Más escalable, especialmente en redes grandes. |
| **Identificación** | IP permanente facilita la identificación de dispositivos. | Asignación dinámica requiere mecanismos adicionales. |

### 3.2. Ejemplo de Ataque: DHCP Starvation Attack (DoS)

Un **ataque de agotamiento de direcciones DHCP (DHCP Starvation Attack)** es un ataque común dirigido a servidores DHCP, que puede llevar a una **denegación de servicio (DoS)**.

**Fases del Ataque (siguiendo el diagrama de la diapositiva)**:

1.  **Inicio del Ataque**: El atacante, desde una máquina bajo su control, comienza a enviar **peticiones DHCP DISCOVER con direcciones MAC falsas**.
2.  **Envío Masivo de Solicitudes**: El atacante genera y envía una **gran cantidad de peticiones DHCP DISCOVER**, cada una con una dirección MAC diferente, simulando múltiples dispositivos que intentan unirse a la red.
3.  **Respuestas del Servidor DHCP**: El servidor DHCP legítimo empieza a responder a cada solicitud falsa con un mensaje **DHCP OFFER**, ofreciendo una dirección IP de su pool de direcciones disponibles.
4.  **Agotamiento del Pool de Direcciones**: El servidor agota su pool de direcciones IP disponibles debido a las respuestas a las peticiones falsas.
5.  **Denegación de Servicio (DoS)**: Como resultado, los **clientes legítimos** que intentan unirse a la red y obtener una IP a través de DHCP no pueden hacerlo porque no hay direcciones IP disponibles. Esto provoca una denegación de servicio.
6.  **Ataque Man-in-the-Middle (Opcional)**: Con la red agotada de direcciones IP, el atacante puede establecer su propio **servidor DHCP malicioso** para ofrecer direcciones IP y parámetros de configuración. Esto le permite potencialmente **interceptar o redirigir todo el tráfico de red**, convirtiéndose en un **Man-in-the-Middle (Hombre en el Medio)**.

**Impacto de un Hardening Insuficiente**: Un servidor DHCP sin un hardening adecuado (ej. sin limitar las tasas de solicitudes, sin inspección de paquetes DHCP, o sin una lista de MACs permitidas en redes críticas) es extremadamente vulnerable a este tipo de ataque. Un ataque de DHCP Starvation puede paralizar la conectividad de una red, impidiendo que nuevos dispositivos se unan o que los existentes renueven sus leases, lo que es una forma efectiva de DoS a nivel de red.

## 4. NAT: Network Address Translation

**NAT (Network Address Translation)** es un procedimiento comúnmente utilizado en routers y firewalls para **cambiar la dirección IP de origen y destino, así como los puertos**.

* **Función Principal**: Permite que múltiples dispositivos en una red privada (con IPs privadas) compartan una o pocas direcciones IP públicas para acceder a Internet.
* **Ventajas de Seguridad**: Además de reducir el número de IP públicas necesarias, NAT ofrece un sistema de protección al **ocultar las direcciones privadas reales** de la red interna, añadiendo una capa de seguridad y dificultando que atacantes externos mapeen directamente la red interna.

### 4.1. Tipos de NAT

Existen diferentes tipos de NAT con propósitos específicos:

* **SNAT (Source Network Address Translation)**:
    * **Función**: Transforma la **dirección IP de origen** del tráfico saliente de una red privada para que parezca que se origina desde una dirección IP pública diferente (normalmente, la del router/firewall).
    * **Uso**: Es el tipo de NAT más común para permitir que los dispositivos de una red interna accedan a Internet. Un tipo específico de SNAT es el **Static NAT**, que permite asignar la misma dirección IP pública a un host específico, de modo que cada vez que este host se conecta a Internet, siempre tendrá la misma IP pública. Esto es útil para servidores internos que necesitan ser accesibles desde el exterior con una IP fija.
* **DNAT (Destination Network Address Translation)**:
    * **Función**: Cambia la **dirección IP de destino y el número de puerto** del tráfico entrante para redirigirlo al host apropiado dentro de una red privada.
    * **Uso**: Permite que un elemento fuera de la red corporativa acceda a un equipo concreto de la red privada. Por ejemplo, si tienes un servidor web en tu red interna con una IP privada, DNAT puede redirigir el tráfico del puerto 80 de tu IP pública al puerto 80 de la IP privada de tu servidor web, haciéndolo accesible desde Internet. Se puede configurar también para activar en caso de fallo de la red principal, redirigiendo todo el tráfico entrante a otra red interna.

**Ejemplo Integrado de NAT**:
Una red corporativa puede tener configurado un **SNAT** en su router para que todos los elementos de la red privada tengan acceso a Internet. Adicionalmente, puede haber un **DNAT** configurado en el mismo router para que, por ejemplo, los usuarios externos puedan acceder a una página web alojada en un servidor interno. Si la red principal falla, el DNAT podría redirigir el tráfico entrante a un servidor de respaldo en otra subred interna para mantener el servicio.

**Importancia del Hardening en NAT**: Si las reglas de NAT (especialmente DNAT) no se configuran con precisión y con el principio de "mínimo privilegio", pueden abrir puertos o redirigir tráfico a servicios internos que no deberían estar expuestos. Un DNAT mal configurado podría, por ejemplo, exponer un servicio de administración interno a Internet, lo que permitiría a los atacantes explotar vulnerabilidades en ese servicio.

## Conclusión

La selección de una topología de red adecuada es fundamental para la eficiencia en la transmisión de datos y la utilización de recursos. La subdivisión correcta de redes o **subnetting** potencia esta eficiencia al optimizar la asignación de direcciones y reducir los dominios de difusión, lo que resulta en una mejora significativa de la seguridad y la escalabilidad de la red.

En resumen, una topología bien diseñada, junto con un subnetting efectivo y una configuración segura de servicios como DHCP y NAT, asegura que una infraestructura de red sea confiable, adaptable y capaz de satisfacer las demandas empresariales en constante evolución, al tiempo que se protege contra una amplia gama de ataques cibernéticos.