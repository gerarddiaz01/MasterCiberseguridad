Documentos de Referencia: "AS-I - Ejercicios.pdf"

# Informe Técnico: Análisis de Vulnerabilidades, Integración de Herramientas y Pivoting con Docker

---

### 1. Resumen Ejecutivo

El presente informe detalla los procedimientos y conceptos abordados en una serie de ejercicios prácticos centrados en la ciberseguridad ofensiva. Se cubren tres áreas principales: el análisis de vulnerabilidades utilizando la herramienta **Nuclei**, la integración del escáner **Nessus** con **Metasploit** para la gestión de reportes, y la configuración de un entorno de laboratorio de **pivoting** usando **Docker**. Los ejercicios demuestran la importancia de la automatización en el escaneo, la centralización de datos de seguridad y la creación de redes de laboratorio controladas para simular y practicar técnicas de ataque como el **pivoting** y la explotación de vulnerabilidades.

---

### 2. Conceptos Fundamentales

* **Nuclei:** Es una herramienta de código abierto utilizada para detectar y explotar vulnerabilidades en un amplio rango de servicios, tanto en aplicaciones web como en otros servicios. Funciona a través de **plantillas** (templates) que contienen patrones específicos para identificar fallos de seguridad comunes como **SQL Injection** y **Cross Site Scripting**.
* **Vulnerabilidad:** Se refiere a una debilidad en un sistema o software que puede ser explotada por un atacante para comprometer su seguridad. En el contexto de los ejercicios, se clasifican por su **criticidad** (alta, baja, crítica).
* **Metasploit:** Un framework de pruebas de penetración ampliamente utilizado. Permite a los profesionales de la seguridad desarrollar, probar y ejecutar exploits contra sistemas remotos. Su funcionalidad puede extenderse mediante **plugins**, como el de **Nessus**, para centralizar la gestión de datos de escaneo.
* **Pivoting:** Es una técnica en la que un atacante utiliza un sistema comprometido (la máquina "pivote") para moverse y atacar otros sistemas en una red interna a la que no tiene acceso directo. En el laboratorio, se simula esta técnica utilizando múltiples máquinas interconectadas por diferentes redes.
* **Docker y Docker Compose:**
    * **Docker:** Una plataforma que utiliza la tecnología de **contenedores** para empaquetar una aplicación y sus dependencias en una unidad que puede ejecutarse de forma aislada.
    * **Docker Compose:** Una herramienta para definir y ejecutar aplicaciones multi-contenedor. Utiliza un archivo **`docker-compose.yml`** para configurar todos los servicios, redes y volúmenes de la aplicación de forma centralizada.

---

### 3. Procedimientos Prácticos

#### 3.1. Análisis de Vulnerabilidades con Nuclei

1.  **Instalación y Configuración:** El primer paso es instalar Nuclei en una máquina Kali Linux. La herramienta requiere **Go (Golang)**. Se instala Go con los comandos `sudo apt update` y `sudo apt install golang -y`. Una vez instalado Go, se procede a instalar Nuclei utilizando el comando `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest`. Para facilitar su uso, se mueve el binario de Nuclei a la ruta `/usr/bin` con `sudo mv nuclei /usr/bin`.
2.  **Identificación del Objetivo:** Se utiliza un escáner ARP para identificar la dirección IP de la máquina vulnerable en la red. El comando `sudo arp-scan <rango de red>` (por ejemplo, `sudo arp-scan 10.0.1.0/24`) lista los hosts activos.
3.  **Escaneo Básico:** Se lanza un escaneo contra el objetivo con el comando `nuclei -target <IP del objetivo>`. El comando analiza el host, detecta los servicios, y ejecuta las plantillas por defecto de Nuclei, mostrando las vulnerabilidades encontradas y su criticidad (alta, baja, crítica). El resultado muestra, por ejemplo, servicios como Apache, phpMyAdmin y Samba, junto con sus vulnerabilidades.
4.  **Escaneo con Filtrado:** Se puede filtrar el escaneo para mostrar solo las vulnerabilidades más críticas. El comando `nuclei -target <IP del objetivo> -severity critical` permite enfocarse únicamente en los hallazgos de alta severidad.
5.  **Explotación de Vulnerabilidades:**
    * **Método con Exploit:** Se utiliza un script de terceros de un repositorio público. El script, escrito en Python, aprovecha la vulnerabilidad del servicio FTP (ProFTPD 1.3.3c) para obtener una **reverse shell**. El comando `python3 exploit.py <IP del atacante> <IP del objetivo>` se usa para ejecutar el exploit, que abre un **listener** en un puerto específico y envía el **payload** a la máquina objetivo.
    * **Método Manual (Netcat):** Se demuestra que la vulnerabilidad puede ser explotada manualmente. Al conectarse al servicio FTP con `nc <IP del objetivo> 21`, el atacante puede enviar un comando específico (`HELP ACIDBITCHEZ`) que activa la **backdoor** en el servidor, permitiendo la ejecución de comandos como `whoami`, tal como se muestra en la captura de pantalla.

#### 3.2. Integración de Nessus y Metasploit

1.  **Requisitos y Carga del Plugin:** Se inicia Nessus y se ejecuta Metasploit con `sudo msfconsole`. Dentro de la consola, se carga el plugin de Nessus con el comando `load nessus`. Este comando integra la funcionalidad de Nessus en Metasploit, lo que permite realizar escaneos desde la misma consola.
2.  **Conexión con el Servidor Nessus:** Se establece la conexión con el servidor Nessus local usando el comando `nessus_connect <usuario>:<contraseña>@<hostname>:<puerto>`. Se puede verificar el estado de la conexión con el comando `nessus_admin`, que confirma los privilegios de administrador.
3.  **Creación y Lanzamiento de Escaneos:** Se crea una política de escaneo en la interfaz web de Nessus. Luego, se lista la política en Metasploit con `nessus_policy_list`. Para crear un nuevo escaneo, se utiliza el comando `nessus_scan_new <UUID de la política> <nombre del escaneo> <descripción> <targets>`. Un error común relacionado con un **bug** en el plugin puede ser solucionado reemplazando un archivo de **Ruby** en el sistema con un comando `curl`. Una vez creado, el escaneo se lanza con `nessus_scan_launch <ID del escaneo>`.
4.  **Importación de Reportes y Análisis de Datos:** Una vez completado el escaneo en Nessus, el reporte se exporta en formato Nessus. Se inicia la base de datos de PostgreSQL con `sudo service postgresql start` y se conecta a Metasploit. Con el comando `db_import <ruta del reporte>`, se importan los resultados del escaneo a la base de datos de Metasploit, centralizando la información. Ahora es posible usar comandos de Metasploit como `hosts` para ver los hosts escaneados, `services <IP del host>` para listar los servicios, y `vulns` para ver las vulnerabilidades detalladas, incluyendo su **CVE** o **NSS**.

#### 3.3. Laboratorio de Pivoting con Docker

1.  **Configuración del Entorno:** Se utiliza un archivo **`docker-compose.yml`** para definir un entorno de laboratorio con tres máquinas (**Kali**, **M1**, y **M2**) en dos redes aisladas (**net1** y **net2**). Cada máquina tiene un servidor SSH y un servidor web. Las máquinas se definen con **Dockerfiles** personalizados para instalar los servicios y crear usuarios con credenciales predefinidas. La configuración de red, como la dirección IP y el `gateway`, se especifica directamente en el archivo `docker-compose.yml`.
2.  **Lanzamiento del Laboratorio:** El entorno completo se inicia con un único comando: `docker compose up -d --build`. Este comando construye las imágenes de los Dockerfiles, las arranca en segundo plano y las configura según el archivo `docker-compose.yml`, como se ilustra en las capturas de pantalla de la terminal.
3.  **Verificación de Conectividad:** Se comprueba la conectividad entre las máquinas. Se demuestra que es posible hacer `ping` desde la máquina Kali (en **net1**) a la máquina M1 (en **net1** y **net2**), pero no directamente a la máquina M2 (solo en **net2**).
4.  **Demostración de Pivoting:** Se utiliza SSH para realizar **pivoting** desde la máquina Kali hasta la M2, pasando por la M1. El comando `ssh -J <usuario1>@<IP de M1> <usuario2>@<IP de M2>` establece un túnel a través de M1 para acceder a M2, demostrando que es posible sortear la segmentación de red.

---

### 4. Conclusiones y Puntos Clave

* **Importancia y Beneficios de Seguridad:**
    * La automatización del escaneo de vulnerabilidades con herramientas como **Nuclei** permite a los profesionales de seguridad identificar fallos de manera rápida y eficiente en múltiples sistemas, reduciendo el tiempo y el esfuerzo de los procesos manuales.
    * La centralización de los datos de escaneo en una base de datos conectada a un framework como **Metasploit** facilita la gestión, el análisis y la correlación de vulnerabilidades, permitiendo una respuesta más ágil ante amenazas.
    * La práctica de técnicas de **pivoting** en entornos controlados de laboratorio es fundamental para comprender cómo los atacantes se mueven lateralmente dentro de una red y para que los defensores puedan fortalecer sus perímetros y segmentación de red.

* **Puntos de Aprendizaje Clave:**
    * Se aprendió a instalar, configurar y utilizar **Nuclei** para realizar escaneos de vulnerabilidades.
    * Se demostró cómo integrar herramientas de escaneo como **Nessus** con un framework de explotación como **Metasploit** para centralizar la información.
    * Se validó la capacidad de **Docker** y **Docker Compose** para crear entornos de laboratorio personalizados y aislados, ideales para la práctica de técnicas de ciberseguridad sin riesgo.
    * Se confirmó que la comprensión de una vulnerabilidad es más importante que la herramienta utilizada, ya que muchas fallas pueden explotarse tanto con **exploits** predefinidos como manualmente, como se vio con el servicio FTP.

* **Relevancia Técnica:**
    * El uso de **Docker Compose** para la creación de entornos complejos de múltiples máquinas es una habilidad técnica invaluable, ya que permite la replicabilidad y la portabilidad de laboratorios de prueba de forma programática.
    * El dominio de la línea de comandos y los parámetros de herramientas como **Nuclei** y **Metasploit** es crucial para personalizar los ataques y los escaneos según los requerimientos específicos de un objetivo.
    * La habilidad de realizar **pivoting** y de gestionar la conectividad a través de redes segmentadas es una competencia avanzada que diferencia a un experto en pentesting. La práctica de esta técnica en el entorno de laboratorio desarrollado es directamente aplicable a escenarios de la vida real.