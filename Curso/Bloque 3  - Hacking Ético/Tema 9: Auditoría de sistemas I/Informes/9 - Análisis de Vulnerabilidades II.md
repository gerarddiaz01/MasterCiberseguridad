Documentos de Referencia: "AS-I - Análisis de Vulnerabilidades: NSE, Scripting, Nessus, OpenVAS.pdf"
Documentos de Referencia: "AS-I - Análisis de Vulnerabilidades_ OSB-Rastreator.pdf"

# Informe Técnico: Análisis de Vulnerabilidades con Nmap NSE, Nessus y OpenVAS

## 1. Resumen Ejecutivo
Este informe se centra en el **análisis de vulnerabilidades** desde una perspectiva práctica, utilizando herramientas clave en ciberseguridad. Se explora el **Nmap Scripting Engine (NSE)**, una de las funcionalidades más potentes de **Nmap**, que permite automatizar tareas de detección de vulnerabilidades con scripts de la comunidad o personalizados. Se detallan los diferentes tipos de scripts de NSE, incluyendo las categorías `default`, `vuln` y `vulners`. Además, el documento introduce los escáneres de vulnerabilidades **Nessus** y **OpenVAS**, explicando su instalación y uso para identificar, evaluar y reportar fallos de seguridad en una red. El objetivo es proporcionar una guía exhaustiva sobre cómo emplear estas herramientas para fortalecer la postura de seguridad de una infraestructura.

---

## 2. Conceptos Fundamentales

### 2.1. Nmap Scripting Engine (NSE)
El Nmap Scripting Engine es una funcionalidad de Nmap que permite a los usuarios ejecutar scripts para automatizar una amplia variedad de tareas de red. Los scripts están escritos en el lenguaje **Lua (v 5.3)**. En la actualidad, existen más de 600 scripts disponibles, categorizados por su propósito.

* **Objetivos del NSE:**
    * **Descubrimiento de red:** Buscar datos `whois` o identificar la propiedad de una IP.
    * **Detección de versiones más sofisticada:** Recopilar información detallada sobre las versiones de los servicios en ejecución.
    * **Detección de vulnerabilidades:** Realizar verificaciones de vulnerabilidades para descubrir si un host es susceptible a `CVEs` específicos. Un ejemplo destacado es el script que se creó en solo dos días para detectar la vulnerabilidad Heartbleed en OpenSSL.
    * **Detección de `backdoors`:** Identificar puertas traseras o `malware` en un sistema objetivo.
    * **Explotación de vulnerabilidades:** Aunque Nmap no es un `framework` de explotación, el NSE puede usarse para explotar vulnerabilidades específicas.

* **Tipos de Scripts (Categorías):**
    * **`auth`:** Interactúa con sistemas para obtener o eludir credenciales de acceso.
    * **`brute`:** Lanza ataques de fuerza bruta para adivinar credenciales de servicios.
    * **`default`:** Contiene scripts preseleccionados que se ejecutan por defecto con la opción `-sC` o `-A`. Están diseñados para ser rápidos, confiables y poco intrusivos.
    * **`vuln`:** Busca vulnerabilidades específicas y solo informa de resultados positivos, ofreciendo referencias a `CVEs` y `exploits`.
    * **`vulners`:** Un script moderno y externo que se conecta a una base de datos en línea para verificar si existen vulnerabilidades asociadas a un `CPE` detectado por Nmap. Esta base de datos ocupa más de 250 GB y no se puede usar de forma local.
    * **`vulscan`:** Un script externo que transforma Nmap en un escáner de vulnerabilidades al integrar bases de datos locales como `CVE` de MITRE y ExploitDB. Aunque se considera obsoleto, sentó un precedente para la detección de vulnerabilidades con Nmap.
    * **`safe`:** Diseñado para no causar daños ni interrupciones en el servicio, lo opuesto a la categoría `intrusive`.
    * **`intrusive`:** Contiene scripts que consumen recursos significativos o que pueden ser percibidos como ataques.

### 2.2. Escáneres de Vulnerabilidades
Un escáner de vulnerabilidades es un programa que evalúa computadoras, redes o aplicaciones en busca de debilidades de seguridad conocidas. El proceso general consta de tres pasos:
1.  **Identificación de activos:** Crea un inventario de todos los dispositivos conectados a una red.
2.  **Análisis de vulnerabilidades:** Compara las características de los activos con una base de datos de vulnerabilidades conocidas como `CVE` y `CWE`.
3.  **Generación de informes:** Emite un informe detallado con las vulnerabilidades encontradas, su severidad, ubicación y recomendaciones para su corrección.

### 2.3. Herramientas de Escaneo de Vulnerabilidades
* **Nessus:** Es un escáner de vulnerabilidades comercial desarrollado por Tenable, Inc.. Nació como un proyecto `opensource` en 1998, pero a partir de la versión 3 pasó a ser privativo. Nessus ofrece una versión gratuita (`Nessus Essential`) para estudiantes y educadores, y tiene una interfaz web que permite gestionar escaneos, políticas y la administración de la herramienta.
* **OpenVAS:** Es un escáner de vulnerabilidades `opensource` de Greenbone Community Edition. A diferencia de Nessus, OpenVAS sigue siendo de código abierto y ejecuta más de 6.000 pruebas de vulnerabilidad. Al igual que Nessus, tiene una interfaz web y permite a los usuarios lanzar escaneos y generar informes detallados.

---

## 3. Procedimientos Prácticos

El laboratorio se realiza con una máquina Kali Linux (10.0.1.5) y una Metasploitable 3 (10.0.1.9).

### 3.1. Práctica de Scripts de Nmap
1.  **Escaneo con la categoría `vuln`:** Se ejecuta el comando `sudo nmap -sV --script vuln 10.0.1.9`.
    * **Resultado:** El escaneo revela múltiples vulnerabilidades asociadas a servicios como FTP (`ProFTPD 1.3.5`), con `CVSS scores` que van desde 10.0 a 2.1. Nmap proporciona URLs de referencia a bases de datos como Vulners, Packetstorm y ExploitDB para cada vulnerabilidad encontrada.
2.  **Escaneo con el script `vulners`:** Se ejecuta `sudo nmap -sV --script vulners 10.0.1.9`.
    * **Resultado:** Este script consulta una base de datos externa para cada `CPE` identificado. Se obtiene información similar a la categoría `vuln`, pero el escaneo es más rápido ya que no ejecuta tantos scripts locales, y es más moderno.
3.  **Escaneo con el script `vulscan` (Externo):** Se clona el repositorio de `vulscan` de GitHub y se crea un enlace simbólico a la carpeta de scripts de Nmap. Se ejecuta el comando `sudo nmap -sV --script=vulscan/vulscan.nse 10.0.1.9`.
    * **Resultado:** El script utiliza bases de datos locales (`cve.csv`, `exploitdb.csv`) para detectar vulnerabilidades en servicios como FTP y Apache.
4.  **Creación de un script NSE:** Se explican las tres partes de un script NSE:
    * **`Head` (Cabecera):** Contiene metadatos como la descripción, el autor, la licencia y la categoría (`default`, `vuln`, etc.).
    * **`Rule` (Regla):** Define cuándo se ejecuta la acción. Puede ser `prerule()`, `hostrule(host)`, `portrule(host, port)` o `postrule()`.
    * **`Action` (Acción):** La función principal del script que realiza la tarea deseada.

### 3.2. Práctica de Escáneres de Vulnerabilidades
1.  **Instalación y configuración de Nessus:**
    * Se descarga la versión `Nessus-10.7.1` en formato `.deb`.
    * Se instala con `sudo dpkg -i <paquete>`.
    * Se inicia el servicio con `sudo systemctl start nessusd.service` y se accede a la interfaz web en `https://kali:8834`.
    * Se registra la versión `Nessus Essential` y se espera a que se descarguen y compilen los plugins.
2.  **Escaneo con Nessus:**
    * **`Host Discovery`:** Se crea un escaneo de tipo `Host Discovery` para la red `10.0.1.0/24`. El escaneo se completa en un minuto y detecta los hosts activos en la red.
    * **`Advanced Scan`:** Se crea un `Advanced Scan` para el host `10.0.1.9`. El escaneo dura 19 minutos y detecta 39 vulnerabilidades en total.
    * **Análisis de resultados:** El informe de Nessus categoriza las vulnerabilidades por severidad (críticas, altas, medias, etc.). Se puede ver una vulnerabilidad crítica de **Remote Code Execution** en el módulo Coder de Drupal. El informe también proporciona una solución, como actualizar el módulo o eliminarlo.
3.  **Instalación de OpenVAS:**
    * Se instala la versión de Greenbone Community Edition con `sudo apt install gvm`.
    * Se ejecuta `sudo gvm-setup` y se guarda la contraseña de administrador.
    * Se verifica que la instalación está correcta con `sudo gvm-check-setup`.
    * Se accede a la interfaz web en `https://127.0.0.1:9392`. OpenVAS no permite escanear hasta que todas las bases de datos de vulnerabilidades se hayan descargado y actualizado.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
El análisis de vulnerabilidades es una fase crítica de cualquier auditoría de seguridad. Herramientas como Nmap NSE, Nessus y OpenVAS permiten a los profesionales identificar debilidades en los sistemas de forma automatizada. Al detectar vulnerabilidades como las que se encuentran en el módulo Coder de Drupal, se pueden aplicar soluciones preventivas, como la actualización de software, para fortalecer la postura de seguridad. La `Heartbleed bug` es un claro ejemplo de cómo una vulnerabilidad puede tener un impacto masivo si no es corregida a tiempo.

### 4.2. Puntos de Aprendizaje Clave
* **Nmap como escáner de vulnerabilidades:** El `NSE` transforma a Nmap en una herramienta multifuncional, con la capacidad de detectar vulnerabilidades con scripts como `vuln` y `vulners`.
* **Escáneres de vulnerabilidades comerciales y `opensource`:** Se han comparado Nessus (comercial) y OpenVAS (`opensource`), entendiendo sus diferencias y similitudes en su funcionamiento y potencial.
* **Proceso de escaneo:** Se ha aprendido el flujo de trabajo de un escaneo de vulnerabilidades: identificar activos, escanear en busca de vulnerabilidades conocidas y generar informes detallados con recomendaciones.
* **Creación de scripts:** Se han explorado los fundamentos para crear un script de Nmap, incluyendo el `head` (metadatos), la `rule` (condiciones de ejecución) y la `action` (funcionalidad).

### 4.3. Relevancia Técnica
El uso de Nmap NSE, Nessus y OpenVAS es una habilidad técnica indispensable para los profesionales de la ciberseguridad. Estas herramientas no solo facilitan la detección de vulnerabilidades, sino que también permiten comprender la lógica de los ataques y cómo se manifiestan en diferentes servicios. La capacidad de generar y analizar informes detallados es crucial para comunicar los riesgos de seguridad y recomendar soluciones efectivas a los administradores de sistemas, lo que convierte esta práctica en una parte fundamental de cualquier evaluación de seguridad.

---

# Informe Técnico: Análisis de Vulnerabilidades con OSB-Rastreator

## 1. Resumen Ejecutivo
Este informe técnico detalla el proceso de análisis de vulnerabilidades en código de software de código abierto utilizando la herramienta OSB-Rastreator. El análisis se centra en la detección de funciones de programación en C consideradas inseguras, las cuales pueden conducir a problemas de gestión de memoria, como el **desbordamiento de búfer** (*buffer overflow*), y que persisten en los repositorios de Linux. El documento describe el desarrollo de la herramienta, su flujo de trabajo y los resultados obtenidos de una prueba de concepto, que incluyen el descubrimiento de una vulnerabilidad real.

## 2. Conceptos Fundamentales
* **OSB-Rastreator:** Es una herramienta diseñada para analizar automáticamente el código fuente de software de código abierto y buscar posibles vulnerabilidades. Fue desarrollada en 2015 por Pablo González para auditar la gran cantidad de software vulnerable en los repositorios de código abierto de Linux.
* **Funciones Inseguras (*Insecure Functions*):** En el lenguaje de programación C, una función se considera insegura si su uso incorrecto puede causar vulnerabilidades, a menudo relacionadas con problemas de gestión de memoria. Una premisa fundamental del análisis con OSB-Rastreator es que la mayoría del código en los repositorios de paquetes de Linux está escrito en C, un lenguaje que contiene este tipo de funciones.
* **Ejemplos de Funciones Inseguras y sus Alternativas Seguras:**
    * **`strcpy`**: Copia una cadena de caracteres sin verificar si el espacio de destino es suficiente, lo que puede causar un **desbordamiento de búfer**. Su alternativa segura es **`strncpy`**, que requiere un parámetro adicional para especificar el tamaño máximo del destino y así prevenir el desbordamiento.
    * **`sprintf`**: Similar a la anterior, puede provocar un **desbordamiento de búfer** si no se controla adecuadamente. Su alternativa es **`snprintf`**, la cual toma un argumento adicional para indicar el tamaño máximo del búfer.
    * **`gets`**: Lee una línea de entrada del usuario y la almacena en un búfer, lo que también puede causar un **desbordamiento de búfer**. La alternativa segura es **`fgets`**, que permite limitar el tamaño máximo del búfer.
    * **`scanf`**: Permite leer datos formateados y almacenarlos en variables. Si la entrada no es validada, puede provocar un **desbordamiento de búfer**. **`fscanf`** es la alternativa para evitar este riesgo.

## 3. Procedimientos Prácticos
El análisis de vulnerabilidades con OSB-Rastreator sigue un flujo de trabajo cíclico, como se ilustra en el diagrama de flujo (*Workflow*) del documento. El proceso se repite para cada paquete listado en un archivo de texto.

### Flujo de Trabajo (Workflow)
1.  **Leer el paquete:** La herramienta comienza leyendo, línea por línea, el nombre de un paquete de un archivo de texto. Este archivo se genera previamente listando todos los paquetes disponibles en la distribución de Linux (por ejemplo, Ubuntu).
2.  **Descargar el paquete:** A continuación, la herramienta descarga el código fuente del paquete. Esto se logra mediante el comando **`apt-get source`**, que descarga el código en un archivo comprimido `tar.gz`.
3.  **Descomprimir el archivo `tar.gz`:** Una vez descargado, el paquete se descomprime para acceder a los archivos de código fuente. El comando utilizado para esto es `tar -xvzf`.
4.  **Buscar archivos de código en C:** La herramienta busca archivos con la extensión `.c` entre los archivos descomprimidos, ya que estos son los que contienen código del lenguaje C.
5.  **Buscar funciones inseguras:** Utilizando expresiones regulares, la herramienta escanea los archivos de código en C para encontrar las funciones potencialmente inseguras mencionadas previamente, como `strcpy` o `gets`. Los resultados se guardan en archivos de texto para su posterior análisis.
6.  **Eliminar el paquete:** Para evitar que el disco duro se llene, el archivo comprimido descargado y los archivos descomprimidos se eliminan después de cada análisis.

### Explicación de Comandos de Terminal
* **`apt list`:** Muestra todos los paquetes disponibles en una distribución, como Ubuntu. Un ejemplo en el documento muestra que en 2015 había más de 45,000 paquetes disponibles, y en 2024 este número se duplicó, superando los 84,000.
* **`wc -l openHack.txt`:** El comando `wc` (*word counter*) con el parámetro `-l` cuenta el número de líneas en el archivo especificado. En este caso, se usa para determinar la cantidad de paquetes listados en el archivo `openHack.txt`.
* **`apt list | cut -d'/' -f1 >> /home/pablo/perro/open2.txt`:** Este comando utiliza una **tubería (`|`)** para encadenar dos comandos.
    * **`apt list`:** Lista todos los paquetes.
    * **`cut -d'/' -f1`:** Divide la salida de `apt list` usando el delimitador (`-d`) `/` y extrae el primer campo (`-f1`), que es el nombre del paquete.
    * **`>> /home/pablo/perro/open2.txt`:** Redirige la salida resultante y la añade (`>>`) al archivo `open2.txt`.

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
El análisis con OSB-Rastreator subraya la importancia de auditar el vasto ecosistema de software de código abierto. La herramienta reveló que un alto número de funciones potencialmente inseguras, como **`strcpy`** y **`scanf`**, se utilizan en miles de ocasiones en los repositorios de paquetes de Linux. Este hallazgo demuestra que, aunque el código sea abierto y revisado, sigue habiendo riesgos de **desbordamiento de búfer** que pueden ser explotados. El hecho de que la herramienta ayudara a descubrir una vulnerabilidad real en un programa llamado Chemtool confirma su utilidad práctica.

### Puntos de Aprendizaje Clave
* A pesar de la popularidad del código abierto, el riesgo de vulnerabilidades, especialmente las relacionadas con la gestión de memoria en el lenguaje C, es significativo.
* El uso de funciones seguras y sus alternativas, como **`strncpy`** en lugar de **`strcpy`**, es fundamental para prevenir **desbordamientos de búfer** y otras fallas. Las alternativas seguras suelen incluir un parámetro adicional para limitar el tamaño de la entrada, lo que mejora la sanitización de los datos.
* Las herramientas automatizadas como OSB-Rastreator son esenciales para la detección inicial de vulnerabilidades a gran escala, pero sus resultados pueden contener **falsos positivos**.
* Una vez detectadas las posibles vulnerabilidades, es necesaria una revisión manual para validar la existencia del riesgo y evaluar si hay otras protecciones que lo mitiguen.
* El análisis de metadatos, como los comentarios en el código, puede proporcionar pistas adicionales para la detección de vulnerabilidades.

### Relevancia Técnica
El flujo de trabajo automatizado de OSB-Rastreator es un ejemplo práctico de cómo se puede auditar de forma eficiente un gran volumen de código. Los procedimientos descritos son altamente relevantes en un entorno de ciberseguridad profesional, ya que combinan el uso de comandos de terminal de Linux (`apt list`, `cut`, `wc`), la automatización de tareas con *scripts*, la búsqueda de patrones con expresiones regulares y la gestión de archivos. La documentación de los hallazgos en archivos de texto para su posterior análisis también es una práctica estándar en los procesos de auditoría y análisis forense.