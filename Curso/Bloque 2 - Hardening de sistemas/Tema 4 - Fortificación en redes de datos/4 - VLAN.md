# Gestión y Hardening de VLANs: Segmentación de Redes para la Ciberseguridad

Las **VLANs (Virtual Local Area Networks)** son una tecnología fundamental en la gestión y seguridad de redes modernas. Permiten a los administradores de red segmentar una única red física en múltiples redes lógicas, creando un aislamiento que puede dividirse por grupos de usuarios, departamentos o incluso tipos de tráfico. Esto convierte a las VLANs en una técnica extremadamente efectiva para el **hardening** o securización de una red de datos.

Antes de configurar la segmentación, es crucial realizar un estudio previo de las redes existentes y su direccionamiento, lo que garantiza una implementación planificada y segura.

## 1. ¿Qué son las VLANs y cómo Funcionan?

Una VLAN es una tecnología que permite segmentar una red física en diferentes redes lógicas independientes. Esto significa que los dispositivos en diferentes VLANs no pueden comunicarse entre sí por defecto, a menos que exista un enrutador (router) o una configuración específica en los dispositivos de red que lo permita. Este aislamiento mejora enormemente la seguridad al limitar el tráfico a un grupo de dispositivos y puede reducir la congestión al limitar los dominios de broadcast.

### 1.1. Switches Gestionados: El Corazón de las VLANs

Para implementar y gestionar VLANs, es indispensable utilizar **switches gestionados**. A diferencia de los switches domésticos, estos dispositivos de hardware de nivel superior permiten la configuración y administración de VLANs, a menudo a través de una línea de comandos (CLI) o una interfaz web.

* **Identificación y Conexión de Puertos**: El primer paso práctico es identificar físicamente qué puertos del switch se van a utilizar para cada VLAN. Cada cable de usuario se conectará a un puerto concreto del switch, lo que subraya la necesidad de una buena fase de planificación y localización física de los usuarios dentro de la organización.
* **Asignación Visual**: En un esquema, cada color puede corresponder a una VLAN específica (ej. verde para Recursos Humanos, amarillo para IT). Cualquier equipo conectado a uno de estos puertos asignados a una VLAN tendrá acceso a una cantidad determinada de recursos limitada por las políticas de esa VLAN.
* **Capa OSI**: Es importante recordar que los switches trabajan en la **capa 2 del modelo OSI (Data Link)**. Por este motivo, el switch distingue a nivel de trama (frame) y es capaz de leer etiquetas que identifican a qué VLAN corresponde una trama.

### 1.2. Identificación de Trama: El Estándar IEEE 802.1Q

La identificación de las tramas de los paquetes Ethernet, es decir, el **identificador VLAN (VLAN ID)**, está especificada por el estándar **IEEE 802.1Q**. Este protocolo permite que múltiples VLANs compartan la misma infraestructura física al añadir una "etiqueta" a cada trama de Ethernet.

#### Proceso de VLAN Tagging (Etiquetado VLAN)

El etiquetado VLAN funciona de la siguiente manera:

1.  **Dispositivo Emisor**: Un dispositivo (por ejemplo, un PC) envía una trama de datos normal a su switch conectado.
2.  **Switch de Origen (VLAN Aware)**: Cuando el Switch 1 (configurado para VLANs) recibe la trama sin etiquetar de un puerto de acceso (ver más adelante), le **asigna una etiqueta VLAN**. Esta etiqueta contiene el VLAN ID, que identifica a qué VLAN pertenece la trama.
3.  **Trama Etiquetada (`Frame with VLAN Tag`)**: La trama ahora lleva información adicional en su encabezado (el VLAN ID). Esta etiqueta es crucial para que los switches y routers en la red sepan cómo manejar la trama correctamente según las reglas de la VLAN.
4.  **Tránsito a través de Puertos Trunk**: La trama etiquetada se envía a través de un **puerto trunk** a otro switch. Los puertos trunk son enlaces especiales entre switches que están diseñados para transportar tráfico de **múltiples VLANs** de forma simultánea. (Esto se explicará más adelante).
5.  **Switch de Destino (VLAN Aware)**: El Switch 2 (o cualquier otro switch en la ruta) lee la etiqueta VLAN de la trama para determinar a qué VLAN pertenece.
6.  **Reenvío a la VLAN Correcta**: Basándose en el VLAN ID, el Switch 2 reenvía la trama solo a los puertos que pertenecen a esa misma VLAN. Esto asegura que los dispositivos en diferentes VLANs no puedan acceder a los datos destinados a otra VLAN, manteniendo el aislamiento lógico.
7.  **Dispositivo Destino**: Finalmente, la trama llega al dispositivo destino, el cual está en la misma VLAN que el emisor. El dispositivo recibe los datos como si estuviera en una red físicamente separada, a pesar de compartir la misma infraestructura de red. Esto permite que múltiples "redes virtuales" coexistan sobre el mismo cableado y hardware.

### 1.3. Puertos Trunk: Interconectando VLANs entre Switches

Para extender una VLAN a otros switches dentro de la misma red, se utilizan los **puertos trunk**.

* **Función**: La misión principal de los puertos trunk es **transmitir la información de múltiples VLANs** entre switches. Son como "puentes" que interconectan diferentes switches de forma física a través de un cable.
* **Escalabilidad**: Permiten crear lo que se denomina **pilas o stacks de diferentes servidores interconectados**, facilitando que una VLAN se extienda a través de varios dispositivos de conmutación en la organización.
* **Protocolo VTP (VLAN Trunk Protocol)**: Este protocolo es el encargado de transmitir la información de las diferentes VLANs a través de los puertos tipo trunk.

### 1.4. Direccionamiento IP y DHCP en VLANs

Cada VLAN debe tener asignado su propio **rango de direcciones IP**.

* **Enrutamiento entre VLANs**: El router es el encargado de identificar las diferentes VLANs que conforman el switch o los switches para enrutar la información entre ellas. Este proceso se conoce como **inter-VLAN routing**.
* **Asignación Automática de IPs**: El **servidor DHCP (Dynamic Host Configuration Protocol)** debe ser el encargado de asignar las direcciones IP para cada VLAN de forma automatizada. Esto divide aún más la infraestructura y puede hacerse más seguro utilizando técnicas de protección ya vistas.

## 2. Tipos de VLANs

Existen varios tipos de VLANs, cada una con un propósito específico en el diseño de red:

* **VLAN por Defecto (Default VLAN)**:
    * **Identificador**: Suele ser la **VLAN 1** (o VLAN 0 en algunos casos).
    * **Función**: Es la configuración base donde se agrupan todos los puertos del switch por defecto. Se encarga del control de todo el tráfico. Todo switch viene preconfigurado con una VLAN por defecto.
* **VLAN Nativa (Native VLAN)**:
    * **Función**: Permite el tráfico de cualquier tipo de paquetes o tramas **no etiquetadas**. Es decir, todo el tráfico que llega a un puerto trunk sin una etiqueta 802.1Q se asocia a la VLAN nativa.
    * **Uso/Riesgo**: Se suele utilizar para solucionar problemas de compatibilidad con otro tipo de redes, pero es una configuración que **no se puede securizar ni gestionar fácilmente**. Por ello, se recomienda usarla solo para testeo o pruebas, o mejor aún, **no usarla para tráfico de usuario** y cambiarla de la VLAN por defecto (VLAN 1) para evitar ataques de **VLAN Hopping**.
* **VLAN de Gestión (Management VLAN)**:
    * **Función**: Proporciona acceso directo a la gestión de los switches y otros dispositivos de red.
    * **Buenas Prácticas de Seguridad**: Por defecto, a menudo está en la misma VLAN que la VLAN 1, lo cual es una **mala práctica de seguridad** porque expone los puertos de gestión al resto de usuarios de la red. Es una buena práctica **definir esta VLAN fuera de la VLAN por defecto** para aislar el tráfico de gestión.
* **VLAN de Voz (Voice VLAN)**:
    * **Función**: Soportan el tráfico de **VoIP (Voz sobre IP)**. Los dispositivos VoIP tienen mayor prioridad de tráfico y no necesitan mucho ancho de banda, pero son sensibles a la latencia.
    * **Requisito**: Es necesario configurar estas VLANs para que funcionen exclusivamente para la función de Voz IP. Si se monta VoIP, se debe dedicar una VLAN exclusivamente para ello. Un dispositivo VoIP es un aparato de red con su propia IP y MAC, por lo que se le pueden aplicar todas las técnicas de protección estándar.
* **VLAN de Datos (Data VLAN)**:
    * **Función**: Aquí se genera el mayor tráfico de la red, ya que circula la mayoría de los paquetes de usuarios y dispositivos.
    * **Seguridad**: Estos puertos se pueden securizar de forma individual o colectiva (toda la VLAN).

## 3. Hardening de VLANs: Mitigación de Ataques

La gestión de VLANs no es solo para la organización, sino que es una técnica **crítica** para securizar cualquier arquitectura de red que aspire a un alto nivel de seguridad. Una configuración adecuada de las VLANs es esencial para el **hardening** y para mitigar ataques de agentes maliciosos.

### 3.1. Buenas Prácticas de Seguridad para VLANs

Aquí se presenta un listado de buenas prácticas que ayudan a mitigar problemas e incidentes de seguridad asociados con las VLANs:

* **No Usar la Configuración por Defecto**: Nunca dejar las configuraciones de VLANs (especialmente la VLAN de gestión y la nativa) en sus valores predeterminados (ej. VLAN 1).
* **IDs de VLAN por Departamento/Tipo de Tráfico**: Crear VLANs específicas para cada departamento, tipo de tráfico (voz, datos, invitados) o nivel de criticidad.
* **Desconectar Puertos no Usados**: Deshabilitar físicamente (y lógicamente) todos los puertos del switch que no estén en uso. Esto previene que alguien pueda conectar un cable y obtener acceso no autorizado a una VLAN. Este es un problema asociado a la **seguridad física**.
* **Desactivar Puertos Trunk no Usados**: Los puertos trunk son críticos; si no se utilizan, deben estar deshabilitados.
* **Crear una VLAN de Gestión Separada**: Definir y utilizar una VLAN de gestión (Management VLAN) separada de la VLAN por defecto (VLAN 1/0). Esto asegura que los puertos de gestión del switch no estén expuestos al resto de usuarios de la red.
* **Permitir Solo Acceso SSH a la VLAN de Gestión**: Configurar los puertos de la VLAN de gestión para que solo permitan acceso a través de protocolos seguros como **SSH** (Secure Shell), y no otros menos seguros como Telnet.
* **Crear una VLAN para Invitados (`Guest VLAN`)**: No mezclar equipos no controlados por la organización (ej. dispositivos de visitantes) en la red corporativa. La VLAN de invitados debe tener un acceso a Internet muy limitado y ningún acceso a la red interna.
* **Segmentación para VoIP**: Mantener el tráfico de Voz IP en una VLAN diferente a la de datos para asegurar rendimiento y reducir vectores de ataque.
* **Filtrado de Puertos Estricto**: Utilizar solo los puertos que se necesitan en cada VLAN, ni uno más ni uno menos. Implementar listas de control de acceso (ACLs) para filtrar el tráfico en los puertos.
* **Evitar Reglas "VLAN a VLAN" Generales**: Se debe evitar crear reglas de enrutamiento o filtrado que permitan tráfico indiscriminado entre VLANs completas, a menos que sea estrictamente necesario. Es preferible utilizar reglas más específicas del tipo **VLAN a Host** o **Host a VLAN**, lo que proporciona un control de acceso mucho más granular y reduce la superficie de ataque.
* **Listas de Control de Acceso (ACLs)**: Utilizar ACLs en los routers o switches de capa 3 que realizan el enrutamiento entre VLANs. Las ACLs permiten o deniegan explícitamente el tráfico entre las diferentes VLANs, reforzando las políticas de aislamiento.

### 3.2. Cómo la Segmentación por VLANs Mitiga Ataques

Las VLANs son una capa crucial en una estrategia de **defensa en profundidad** y contribuyen significativamente a mitigar diversos tipos de ataques:

* **Contención de Movimiento Lateral (Lateral Movement)**: Si un atacante (un **Insider** o alguien que ha logrado un acceso inicial a través de **Phishing** o un **Exploit**) compromete un dispositivo en una VLAN, la segmentación restringe su capacidad para moverse libremente a otras subredes y sistemas críticos (como bases de datos con **Data Leaks** potenciales o servidores de administración). Cada VLAN actúa como una barrera, obligando al atacante a encontrar nuevas vulnerabilidades o técnicas para "saltar" entre VLANs (**VLAN Hopping**), lo que incrementa el tiempo de ataque y la probabilidad de detección.
* **Aislamiento de Brotes de Malware y Ransomware**: En caso de un brote de **Malware** o **Ransomware**, si una VLAN (por ejemplo, la de usuarios) se ve afectada, la infección puede ser contenida dentro de ese segmento. Esto evita que el **Malware** se propague rápidamente a servidores de producción, sistemas financieros u otras áreas críticas de la red, minimizando el impacto y facilitando la recuperación.
* **Reducción de la Superficie de Ataque**: Al separar lógicamente los dispositivos y servicios en VLANs, se reduce la cantidad de dispositivos que están "visibles" o accesibles entre sí por defecto. Esto minimiza la superficie de ataque disponible para los escaneos de reconocimiento y los **exploits** dirigidos.
* **Protección contra Ataques de Denegación de Servicio (DoS)**: La reducción de los dominios de broadcast que ofrecen las VLANs disminuye el impacto de ataques que abusan del tráfico de difusión (ej. **broadcast storms** o ciertos tipos de **DDoS**). Si un ataque de inundación ocurre en una VLAN, su efecto se contiene principalmente a ese segmento, sin afectar al resto de la red.
* **Aplicación de Políticas de Seguridad Más Granulares**: Las VLANs permiten aplicar políticas de seguridad mucho más estrictas y específicas a grupos de dispositivos o tipos de tráfico. Por ejemplo, se pueden implementar **IDS/IPS (Intrusion Detection/Prevention Systems)** con reglas más agresivas en la VLAN de servidores, o restringir el acceso a Internet en la VLAN de invitados.

En conclusión, el uso de VLANs es fundamental como un elemento básico en la protección de la arquitectura de red de datos. Los switches gestionados son de vital importancia para poder segmentar redes físicas en redes lógicas. Esta técnica se convierte en un requisito crítico para cualquier arquitectura que busque un alto nivel de seguridad, contribuyendo a una defensa robusta y a la integridad y confidencialidad de los datos.