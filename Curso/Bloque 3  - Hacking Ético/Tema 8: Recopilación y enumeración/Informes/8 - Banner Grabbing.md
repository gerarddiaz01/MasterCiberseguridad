Documentos de Referencia: "RE - Banner Grabbing.pdf"

# Informe Técnico: Banner Grabbing y Detección de Servicios

## 1. Resumen Ejecutivo
Este informe explora en detalle la técnica de **Banner Grabbing**, un método esencial en la ciberseguridad para recopilar información sobre servicios y sistemas remotos. Se diferencian y explican las dos modalidades: **Banner Grabbing Pasivo**, que utiliza fuentes de datos intermedias como Shodan, y **Banner Grabbing Activo**, que implica una interacción directa con el sistema objetivo. El documento profundiza en la aplicación práctica de herramientas como **Netcat**, **Telnet**, **cURL**, **Wget** y, en particular, **Nmap** con sus opciones de detección de versiones y su modo "todo en uno" (`-A`). La finalidad es demostrar cómo obtener información crítica sobre las versiones de los servicios, lo cual es vital para identificar vulnerabilidades y planificar auditorías de seguridad.

---

## 2. Conceptos Fundamentales

### 2.1. Banner Grabbing
Es una técnica que consiste en obtener información sobre un servicio o sistema remoto al interceptar y analizar los **banners** o encabezados que este devuelve al establecer una conexión. Estos banners pueden contener datos valiosos como la versión del software, el sistema operativo, y otros detalles que son cruciales para evaluar la seguridad de un sistema. El objetivo principal es identificar las versiones de los servicios para poder encontrar posibles vulnerabilidades, especialmente si están desactualizados.

### 2.2. Técnicas de Banner Grabbing
* **Pasivo:** Este enfoque se basa en la recopilación discreta de información sin interactuar directamente con el host. Esto se puede lograr observando el tráfico de red con herramientas como **Wireshark** o **Pof**. Otra forma es usar servicios de terceros, como **Shodan**, que es un motor de búsqueda especializado en dispositivos conectados a Internet que indexa detalles técnicos y banners de forma pasiva.
* **Activo:** Esta técnica implica la interacción directa con el servicio o servidor objetivo para obtener detalles sobre su versión y atributos. Aunque genera cierto "ruido" en la red, es una forma efectiva de obtener información precisa. Herramientas comunes para esta técnica son **Netcat**, **Telnet**, **cURL** y **Wget**.

### 2.3. Detección de Servicios y Versiones con Nmap
**Nmap** es una herramienta poderosa que, además de escanear puertos, puede detectar servicios y sus versiones con gran precisión.
* **Detección de versiones (`-sV`):** La opción `-sV` habilita la detección de versiones, enviando peticiones y analizando las respuestas para identificar el software y su versión. Se pueden usar opciones adicionales para controlar el escaneo, como `--version-intensity <0-9>` para ajustar el nivel de agresividad y `--allports` para escanear todos los puertos.
* **Modo "All-in-one" (`-A`):** El parámetro `-A` es una opción integral que combina la detección de versiones, la detección del sistema operativo, el escaneo de scripts (NSE) y el uso de `traceroute` en un solo comando. Se puede ajustar su velocidad con el parámetro `-T<0-5>`.

---

## 3. Procedimientos Prácticos

El laboratorio se realiza con una máquina **Kali Linux** (IP 10.0.1.5) y una máquina **Metasploitable** (IP 10.0.1.9) en la misma red.

### 3.1. Escaneo de Puertos Básico con Nmap
1.  **Comando:** `nmap 10.0.1.9`.
2.  **Propósito:** Realizar un escaneo de puertos inicial para identificar los servicios activos en la máquina objetivo.
3.  **Resultado:** El escaneo revela puertos abiertos como el 21 (ftp), 22 (ssh), 80 (http), 445 (microsoft-ds), 631 (ipp), 3306 (mysql) y 8080 (http-proxy).

### 3.2. Banner Grabbing Activo con Herramientas Específicas
1.  **FTP (Puerto 21) con Netcat:**
    * **Comando:** `nc -v 10.0.1.9 21`.
    * **Propósito:** Conectar al puerto 21 y capturar el banner del servicio FTP.
    * **Resultado:** El banner revela que el servicio es **ProFTPD 1.3.5 Server**.
2.  **SSH (Puerto 22) con Telnet:**
    * **Comando:** `telnet 10.0.1.9 22`.
    * **Propósito:** Conectar al puerto 22 y obtener el banner del servicio SSH.
    * **Resultado:** El banner indica que el servicio es **SSH-2.0-OpenSSH_6.6.1p1** y que se ejecuta en una máquina **Ubuntu**.
3.  **HTTP (Puerto 80) con Wget:**
    * **Comando:** `wget http://10.0.1.9/phpmyadmin/ -q -S`.
    * **Propósito:** Solicitar la página de `phpmyadmin` con los flags `-q` (modo silencioso) y `-S` (imprimir cabeceras) para obtener el banner del servidor web.
    * **Resultado:** El banner muestra que el servidor es **Apache/2.4.7 (Ubuntu)** y que la versión de PHP es **PHP/5.4.5**.
    * **Comando Adicional:** Al investigar el directorio `/drupal`, se ejecuta `wget http://10.0.1.9/drupal/ -q -S`. El resultado, además de la versión de Apache y PHP, revela que la versión de la aplicación es **Drupal 7**.

### 3.3. Banner Grabbing con Nmap
1.  **Detección de versiones (`-sV`):**
    * **Comando:** `nmap -sV 10.0.1.9`.
    * **Propósito:** Detectar versiones de todos los servicios abiertos en los puertos comunes.
    * **Resultado:** El escaneo muestra una lista de servicios y sus versiones detectadas, como **ProFTPD 1.3.5** para FTP y **OpenSSH 6.6.1p1** para SSH.
2.  **Escaneo "All-in-one" (`-A`):**
    * **Comando:** `nmap -A -T4 10.0.1.9`.
    * **Propósito:** Realizar un escaneo completo y agresivo que combina varias técnicas para obtener la máxima cantidad de información posible.
    * **Resultado:** La salida es mucho más extensa y detallada. Incluye la versión de los servicios (`Apache httpd 2.4.7`, `Samba smbd 4.3.11`, `CUPS 1.7`, `MySQL`, `Jetty 8.1.7`), los hostkeys del servidor SSH, los directorios del servidor web, y scripts de seguridad que revelan el nombre del sistema (`Ubuntu`) y su hora actual.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
El Banner Grabbing es una técnica crucial para la fase de reconocimiento en una auditoría de seguridad. Permite a los profesionales perfilar la superficie de ataque e identificar posibles puntos de entrada. Al conocer las versiones exactas de los servicios en ejecución, se puede determinar si existen vulnerabilidades conocidas que puedan ser explotadas, lo que facilita la planificación de las siguientes etapas de un pentesting.

### 4.2. Puntos de Aprendizaje Clave
* **Técnicas activas vs. pasivas:** Se ha aprendido a diferenciar entre el Banner Grabbing activo (con interacción directa) y el pasivo (sin interacción).
* **Herramientas para Banner Grabbing:** Herramientas como Netcat, Telnet, Wget y Nmap son indispensables en el arsenal de un profesional de la ciberseguridad para obtener información detallada de los servicios.
* **Nmap como herramienta integral:** Nmap es una herramienta muy versátil que, con opciones como `-sV` y `-A`, permite no solo la detección de servicios y versiones, sino también la ejecución de scripts para una recopilación de información más exhaustiva.
* **Correlación de datos:** La información recopilada con diferentes herramientas debe ser sintetizada para obtener una visión completa del entorno, como se mostró en la recopilación de los banners de los servicios FTP, SSH y HTTP.

### 4.3. Relevancia Técnica
La habilidad para realizar Banner Grabbing de manera efectiva es de gran relevancia profesional. Permite a los auditores y administradores de red obtener una instantánea de los servicios expuestos y sus versiones. Esto es vital para priorizar la mitigación de vulnerabilidades y mantener una postura de seguridad proactiva. La práctica con estas herramientas y la comprensión de sus resultados son habilidades fundamentales para la evaluación de la seguridad de cualquier infraestructura.