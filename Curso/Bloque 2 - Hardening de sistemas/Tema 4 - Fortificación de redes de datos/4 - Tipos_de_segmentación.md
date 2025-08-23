# Segmentación de Red: Una Estrategia Crucial para la Ciberseguridad

La **segmentación de red** es una práctica de seguridad fundamental que va más allá del simple **subnetting**. Permite dividir una red en secciones más pequeñas y aisladas, lo que facilita un mayor control sobre el tráfico, mejora la visibilidad, optimiza el rendimiento y, lo más importante, fortalece la postura de seguridad de una organización frente a diversas amenazas cibernéticas. La implementación de arquitecturas complejas con algoritmos y protocolos específicos eleva el nivel de seguridad al permitir, por ejemplo, el bloqueo de tráfico en una zona comprometida. La **escalabilidad** también está estrechamente ligada a esta fase de diseño e implementación, recordando que la seguridad de un sistema no solo se refiere a la resiliencia contra ataques, sino a cualquier factor que afecte el rendimiento final de la arquitectura.

Existen tres tipos principales de segmentación de red: **física**, **lógica** e **inalámbrica (Wi-Fi)**.

## 1. Segmentación Física de Red

La segmentación física se basa en el uso de **dispositivos de red** hardware para crear barreras y aislar secciones de la red.

* **Elementos Clave**: Los elementos físicos incluyen routers, gateways, switches y, especialmente, los **firewalls** (cortafuegos).
* **Rol de los Firewalls**: Los firewalls son fundamentales en la seguridad de la segmentación. Si se ubican y configuran correctamente con las políticas adecuadas, son capaces de proteger contra:
    * Ataques externos e internos.
    * Propagación de **Malware** o virus.
    * Ataques de **movimiento lateral**.
* **Beneficios**: Una correcta segmentación de los elementos físicos nos va a permitir:
    * **Monitorizar** el tráfico de red de manera efectiva.
    * Ofrecer la posibilidad de **aislamiento** si fuera necesario.
    * Proporcionar **mayor visibilidad** de la red.
    * Simplificar la **localización de fallos**.

### 1.1. La Zona Desmilitarizada (DMZ)

La **DMZ (Demilitarized Zone)** es un segmento de red que actúa como una **zona de amortiguación** entre la red interna de una empresa y la red pública externa (Internet). Se implementa utilizando elementos físicos, como firewalls, y es clave en la seguridad de la **red perimetral**.

* **Ubicación**: La DMZ se sitúa entre los firewalls que gestionan las conexiones de la red interna a Internet.
* **Propósito**: Se utiliza para alojar servicios accesibles públicamente que necesitan estar expuestos a Internet (como servidores web, de correo electrónico, DNS, FTP, etc.). Al ubicar estos servidores en la DMZ, se mantienen los recursos internos de la empresa seguros, ya que los servidores de la DMZ no tienen acceso directo a la intranet o redes internas.
* **Políticas de Conexión**:
    * Tráfico desde la **red interna** a Internet y a la **DMZ** está permitido.
    * Conexiones desde la **DMZ** solo se permiten a Internet; no pueden acceder a la red interna.
* **Implementación**: Las DMZ pueden configurarse de dos maneras principales:
    * **Un solo firewall**: Un único firewall gestiona todas las conexiones.
    * **Dos firewalls (Diseño más utilizado)**:
        * Un **External Firewall** (Firewall Externo) se dedica a la conexión entre Internet y la DMZ (el "frontend").
        * Un **Internal Firewall** (Firewall Interno) se dedica a la conexión entre la DMZ y la intranet o red interna (el "backend"). Este diseño de doble firewall añade una capa de seguridad significativa.

## 2. Segmentación Lógica de Red

La segmentación lógica permite dividir una red sin necesidad de hardware adicional, utilizando configuraciones de software o protocolos específicos.

* **Listas de Control de Acceso (ACLs)**: Ya mencionadas en contextos anteriores, las ACLs son reglas configuradas en routers y firewalls para permitir o denegar el tráfico de red basándose en criterios como direcciones IP, puertos o protocolos. Permiten un control de acceso básico pero efectivo.
* **Control de Acceso a la Red (NAC - Network Access Control)**: Las soluciones NAC añaden un nivel de seguridad adicional al garantizar que los dispositivos que intentan acceder a los recursos de la red cumplan con las políticas de seguridad y se autentiquen antes de obtener acceso.
* **Redes Privadas Virtuales (VPN - Virtual Private Network)**: Las VPNs extienden una red privada a través de una red pública (como Internet), permitiendo a los usuarios enviar y recibir datos como si sus dispositivos estuvieran directamente conectados a la red privada. Proporcionan un canal seguro y cifrado para la comunicación, lo cual es fundamental para el acceso remoto seguro.

### 2.1. VLAN (Virtual Local Area Network)

Las **VLANs** son uno de los elementos más utilizados y potentes en la segmentación lógica de red. Su objetivo principal es **separar lógicamente diferentes redes dentro de una misma red física**.

* **Funcionamiento**: Una VLAN permite que dispositivos en diferentes ubicaciones físicas se comporten como si estuvieran en la misma red local, o que dispositivos en la misma ubicación física se comporten como si estuvieran en redes locales diferentes. Los dispositivos en diferentes VLANs **no pueden comunicarse entre sí** a menos que haya un enrutador (router) o una configuración especial que les permita hacerlo.
* **Beneficios**:
    * Mejora drásticamente la seguridad al **limitar el tráfico a un grupo específico de dispositivos**, conteniendo el impacto de posibles brechas.
    * Reduce la **congestión** de la red al limitar los **dominios de broadcast** (cada VLAN es su propio dominio de broadcast).
    * Ofrece **mayor flexibilidad y control** sobre el tráfico de red.
    * Permite una **asignación eficiente de recursos** sin necesidad de hardware adicional significativo.

#### 2.1.1. VLAN Tagging (Etiquetado VLAN)

El **VLAN Tagging** es la técnica utilizada para implementar las VLANs. Implica añadir una etiqueta (tag) a las tramas de datos para identificar a qué VLAN pertenecen.

* **Estándar IEEE 802.1Q**: Este es el protocolo estándar para el etiquetado de VLANs.
* **Proceso de Etiquetado**:
    1.  **Dispositivo Emisor (`Device`)**: Un dispositivo en una red necesita enviar datos a otro dispositivo.
    2.  **Switch 1 (VLAN Aware)**: Cuando un switch configurado para VLANs recibe la trama de datos del dispositivo, le **asigna una etiqueta (VLAN Tag)**. Esta etiqueta identifica a qué VLAN pertenece la trama.
    3.  **Trama con Etiqueta VLAN (`Frame with VLAN Tag`)**: La trama ahora contiene información adicional en su encabezado que incluye el **identificador de la VLAN (VLAN ID)**. Este identificador es crucial para que otros dispositivos de la red manejen la trama correctamente de acuerdo con las reglas de la VLAN.
    4.  **Switch 2 (VLAN Aware)**: La trama etiquetada se envía a través de la red al siguiente switch. Este switch lee la etiqueta VLAN para determinar a qué VLAN pertenece esa trama.
    5.  **Reenvío de la Trama**: Basándose en la etiqueta VLAN, el Switch 2 sabe qué puerto o puertos debe reenviar la trama. **Solamente los puertos que pertenecen a la misma VLAN recibirán esa trama**. Esto nos asegura que los dispositivos en diferentes VLANs no puedan acceder a los datos destinados a otra VLAN.
    6.  **Dispositivo Destino (`Destination Device`)**: Finalmente, la trama llega al dispositivo en esta misma VLAN que el dispositivo emisor. El dispositivo recibe los datos como si estuviera en una red física separada, aunque comparte la misma infraestructura de red con otros dispositivos en otras VLAN. Esto permite que diferentes tramas con diferentes etiquetados circulen por la misma ubicación pero se entreguen en las diferentes VLAN.

#### 2.1.2. Segmentación de Redes VoIP (Voz sobre IP)

Las redes de **VoIP (Voz sobre IP)** deben estar muy bien segmentadas, tanto a nivel físico como lógico.

* **Motivo**: Mezclar el tráfico de voz con el tráfico de datos puros y duros puede llevar a pérdidas significativas de rendimiento global. Además, el tráfico de voz puede suponer un **nuevo vector de ataque** para la arquitectura.
* **Requisito**: Este tipo de redes debe segmentarse utilizando dispositivos de red compatibles, además de la segmentación realizada por VLANs.

## 3. Segmentación y Seguridad de Redes Wi-Fi (Inalámbricas)

Las redes inalámbricas presentan retos adicionales para la segmentación y seguridad debido a las nuevas tecnologías y dispositivos, y una configuración insegura puede generar problemas graves. La seguridad en redes Wi-Fi tiene un impacto directo y significativo en infraestructuras relacionadas con el **IoT (Internet of Things)**, ya que estos dispositivos suelen usar tecnologías inalámbricas como Wi-Fi y Bluetooth.

* **SSID (Service Set Identifier)**: Es el nombre de la red Wi-Fi que permite a los usuarios identificarla y conectarse.
    * **Consejos de Seguridad**: Es crucial elegir un **SSID** que no ofrezca información útil a un posible atacante.
    * **Evitar Nombres por Defecto**: No se deben dejar los nombres por defecto que se suelen asignar por los dispositivos que la gestionan, ya que esta información es pública y se podría sacar información, por ejemplo, el tipo de cifrado utilizado o el modelo del dispositivo de red y de esta forma buscar contraseñas por defecto o algún tipo de vulnerabilidad asociada a ese dispositivo.
    * **Ocultar SSID**: Aunque no es muy efectivo, algunas redes se configuran para ocultar su SSID.
* **Segmentación Wi-Fi con AP (Access Points)**: La segmentación de Wi-Fi con puntos de acceso implica dividir una red inalámbrica en múltiples secciones para mejorar la seguridad y la gestión del tráfico. Los APs también sirven para ampliar el rango de utilización de dichas redes Wi-Fi.
* **Estándar IEEE 802.11**: Es un conjunto de estándares para implementar comunicaciones de red de área local inalámbrica (WLAN) en varias frecuencias (2.4, 5 y 60 GHz). Es importante ir viendo las diferentes versiones que van apareciendo sobre este estándar o normativa.
* **RADIUS (Remote Authentication Dial-In User Service)**: RADIUS es un protocolo de red que proporciona una gestión centralizada de **Autenticación, Autorización y Contabilidad (AAA)** para los usuarios que se conectan y utilizan un servicio de red.
    * **Funcionamiento**: Los servidores RADIUS se conectan con el directorio de servicios de la empresa (por ejemplo, con un LDAP o un Directorio Activo) para autenticar los accesos de los usuarios.
    * **Cifrados**: Para comprobar la autenticación se utilizan cifrados como **PAP, CHAP o EAP**.
    * **Implementación**: Es posible configurar este tipo de servicios RADIUS directamente contra un servidor, por ejemplo en Windows o Linux, es decir, no hace falta un dispositivo específico, aunque la mayoría de los routers empresariales lo llevan ya por defecto.
    * **Seguridad Vital**: En las redes empresariales, tenemos que evitar a toda costa conectar dispositivos sin autenticación, es decir, no solo aquellos que tienen usuarios que se validan, sino también los dispositivos con cuentas que están asociadas al directorio de la infraestructura (que tienen un nombre de usuario y una contraseña).

## Relación entre Segmentación y Hardening de Sistemas

La **segmentación es un componente fundamental del hardening** de sistemas y redes. Mientras que el **hardening** se enfoca en asegurar cada componente individual (servidores, dispositivos de red, aplicaciones) mediante la reducción de su superficie de ataque y la aplicación de configuraciones de seguridad robustas, la **segmentación** aplica estos principios a nivel de red, creando barreras y límites que contienen y aíslan.

* **Defensa en Profundidad (Defense-in-Depth)**: La segmentación es una capa clave en una estrategia de **defensa en profundidad**. Incluso si un atacante logra superar una primera línea de defensa (ej. un firewall perimetral o un sistema con hardening deficiente en un dispositivo), la segmentación asegura que se enfrente a barreras adicionales antes de poder acceder a recursos críticos.
* **Principio de Mínimo Privilegio (Principle of Least Privilege)**: La segmentación facilita la aplicación de este principio a nivel de red, al permitir que el tráfico solo fluya entre subredes si es estrictamente necesario y autorizado por políticas de seguridad explícitas.
* **Reducción de la Superficie de Ataque**: Al crear subredes más pequeñas y aisladas, se reduce la superficie de ataque que un compromiso inicial puede explotar. Los servicios que no necesitan comunicarse con otros segmentos pueden ser estrictamente limitados.
* **Mayor Visibilidad y Monitorización**: Al dividir la red, es más fácil monitorizar el tráfico relevante dentro de cada segmento, lo que facilita la detección temprana de anomalías, intrusiones o movimientos laterales maliciosos.

## Cómo la Segmentación Ayuda a Mitigar Ataques de Agentes Maliciosos

La segmentación de red es una de las estrategias más efectivas para mitigar una amplia gama de ataques cibernéticos, limitando su alcance y conteniendo su impacto.

* **Mitigación de Movimiento Lateral (Lateral Movement)**:
    * **Ataque**: Una vez que un atacante (o **APT - Advanced Persistent Threat**) compromete un punto de entrada inicial (ej. un ordenador de usuario a través de **Phishing** o un **0-day Exploit**), intenta moverse lateralmente a otros sistemas para buscar información valiosa, escalar privilegios o desplegar más **Malware**.
    * **Mitigación por Segmentación**: Las VLANs y otras formas de segmentación crean barreras que impiden que el atacante acceda directamente a otras subredes críticas (ej. servidores de bases de datos, sistemas de administración) sin pasar por un firewall o un router con reglas estrictas. Esto obliga al atacante a gastar más tiempo y recursos, aumentando la probabilidad de ser detectado por sistemas de monitorización de red o **IDS/IPS (Intrusion Detection/Prevention Systems)**.
* **Contención de Brotes de Malware y Ransomware**:
    * **Ataque**: El **Ransomware** y otros tipos de **Malware** a menudo intentan propagarse rápidamente a través de la red una vez que infectan un dispositivo.
    * **Mitigación por Segmentación**: Si la red está segmentada, un brote de malware en una subred (ej. la subred de usuarios) quedará contenido dentro de ese segmento, impidiendo que infecte servidores críticos o subredes de administración. Esto es especialmente importante en redes planas donde una infección podría propagarse a todos los dispositivos conectados.
* **Protección contra Ataques de Denegación de Servicio (DoS/DDoS)**:
    * **Ataque**: Los ataques **DDoS (Distributed Denial of Service)** buscan sobrecargar recursos de red o servicios para hacerlos inaccesibles. Si la red no está segmentada, un ataque contra un servidor web puede impactar a toda la red, incluyendo sistemas internos críticos.
    * **Mitigación por Segmentación**: Una DMZ protege los servidores internos de los ataques DDoS dirigidos a los servicios públicos. Si un servidor web en la DMZ es atacado, la red interna permanece aislada y operativa. Además, la segmentación interna puede aislar servicios de un **DDoS interno** (ej. causado por un dispositivo comprometido), evitando que afecte a toda la red.
* **Prevención de Escaneo y Reconocimiento de Red**:
    * **Ataque**: Los atacantes realizan fases de reconocimiento de red (escaneo de puertos, descubrimiento de servicios) para mapear la infraestructura y encontrar vulnerabilidades.
    * **Mitigación por Segmentación**: Al segmentar, los atacantes solo podrán ver y escanear la subred a la que tienen acceso inicial. Las subredes críticas estarán ocultas y protegidas por firewalls que filtran el tráfico no deseado. Esto reduce la cantidad de información que un atacante puede recopilar sobre la red interna.
* **Aplicación de Políticas de Seguridad Más Estrictas**:
    * **Ataque**: Los atacantes se aprovechan de configuraciones laxas que permiten demasiado tráfico o accesos innecesarios.
    * **Mitigación por Segmentación**: Permite aplicar políticas de seguridad más rigurosas a segmentos de red que contienen datos o sistemas de alta criticidad (ej. segmentar bases de datos, servidores de contabilidad, o sistemas de **DevSecOps**). Se puede implementar una inspección de paquetes más profunda o sistemas **IDS/IPS** específicos para estas subredes, detectando comportamientos anómalos o **Exploits** contra vulnerabilidades conocidas (como **0-day** si se utilizan mecanismos avanzados de detección).

En resumen, la segmentación de red es una estrategia esencial para securizar redes de datos y garantizar su eficiencia y confiabilidad en el mundo real. Es una capa proactiva de defensa que refuerza la postura de seguridad global de una organización.