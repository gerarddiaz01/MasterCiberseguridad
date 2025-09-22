Documentos de Referencia: "AWEB - Recolección de información.pdf"

# Informe Técnico: Recolección de Información en Auditorías Web (Pasiva y Activa)

## 1. Resumen Ejecutivo
Este informe detalla las técnicas de recolección de información, tanto pasiva como activa, para auditorías de aplicaciones web. Se definen las metodologías de **escaneo pasivo** (sin conexión directa) a través de buscadores avanzados (**dorks**) y fuentes públicas de datos filtrados (**leaks**), así como el **escaneo activo** (**fingerprinting**), que implica interactuar directamente con el objetivo. Se introducen herramientas y conceptos clave como **Shodan**, **Censys** y **Dirsearch**, y se explican las diferencias entre **Spidering** y **Crawling**. El informe concluye con una demostración práctica usando un entorno de laboratorio para ilustrar cómo estas técnicas se aplican para mapear la infraestructura y los recursos de una aplicación.

---

## 2. Conceptos Fundamentales

### Escaneo Pasivo (Passive Scanning)
El escaneo pasivo es la fase de recolección de información en la que un auditor no establece una conexión directa con el objetivo. En su lugar, se apoya en datos que el propio sistema ha expuesto públicamente. Los principales métodos son:
* **Dorks**: Son palabras clave y operadores de búsqueda avanzados que aprovechan los algoritmos de motores de búsqueda como **Google**, **Bing** y **Shodan** para encontrar información específica. Por ejemplo, `site:`, `inurl:`, `filetype:` y `cache:`.
* **Leaks**: Consisten en el uso de credenciales y datos sensibles expuestos en Internet a través de brechas de seguridad de otras organizaciones. Estos datos pueden incluir correos electrónicos, nombres de usuario y contraseñas. Herramientas como **HaveIBeenPwned**, **Dehashed** o **Leak-lookup** permiten a un auditor verificar si las credenciales de un usuario han sido comprometidas.
* **Buscadores de seguridad**: Herramientas como **Shodan**, **Censys**, **Fofa**, **SecurityTrails**, **RiskIQ** y **ZoomEye** permiten buscar dispositivos y servicios expuestos en Internet, analizando sus configuraciones, certificados y tecnologías subyacentes sin necesidad de interactuar directamente con ellos.

### Escaneo Activo (Active Scanning) o Fingerprinting
El escaneo activo implica realizar peticiones directas al objetivo para obtener información. A diferencia del pasivo, este método requiere autorización previa del cliente o del propietario del activo. Su objetivo es identificar:
* **Servicios y protocolos disponibles**: Puertos abiertos y servicios que se están ejecutando.
* **Sistemas operativos y tecnologías**: El *software* del servidor, librerías, versiones, etc..
* **Configuraciones por defecto**: Archivos y directorios de instalación por defecto.
* **Recursos internos**: Directorios y archivos ocultos que pueden no estar enlazados.

### Spidering y Crawling
Estas dos técnicas son fundamentales en el escaneo activo:
* **Spidering**: Consiste en la extracción de enlaces de una aplicación web utilizando *scripts* automatizados, conocidos como *spiders*. Permite mapear la arquitectura y las interconexiones de la aplicación.
* **Crawling**: Es la búsqueda de archivos y directorios en una aplicación web mediante ataques de fuerza bruta con diccionarios. Esta técnica, también llamada **fuzzing**, permite descubrir recursos ocultos. Herramientas como **Dirsearch** y diccionarios como **Rockyou** o **SecLists** son esenciales para esta tarea.

---

## 3. Procedimientos Prácticos

### 1. Preparación del Entorno de Laboratorio
Antes de realizar un escaneo activo, se recomienda configurar un entorno de laboratorio controlado.
* **Instalación de Metasploitable2**: Se descarga e importa la máquina virtual **Metasploitable2** en un *software* de virtualización. Esta máquina está diseñada intencionalmente con servicios y configuraciones vulnerables para practicar ataques de forma segura.
* **Configuración de red**: Se configura la red de **Metasploitable2** en modo **NAT** para que sea accesible desde la máquina atacante, y se obtiene la dirección IP local de la víctima con `ifconfig`.

### 2. Escaneo de una Máquina Víctima con Dirsearch
El documento presenta un ejemplo de escaneo activo en **Metasploitable2** usando la herramienta `Dirsearch`.
* **Comando de ejecución**: `dirsearch -u http://192.168.106.132`.
    * `dirsearch`: Es la herramienta que realiza el escaneo.
    * `-u`: Especifica la URL del objetivo.
* **Análisis del *output***: El resultado del comando muestra una lista de archivos y directorios encontrados, junto con el código de estado **HTTP** (`200`, `403`, `404`, etc.) y el tamaño del recurso. El escaneo revela la existencia de recursos importantes, como:
    * `robots.txt`: Un archivo que puede contener pistas sobre directorios ocultos.
    * `phpMyAdmin/`: Un panel de administración de bases de datos que es un objetivo común.
    * `/admin/`: Un directorio de administración, lo que indica un posible punto de escalada de privilegios.
    * `/doc/`: Un directorio público que, al ser visitado, muestra una lista de archivos, lo que expone la estructura de directorios del servidor.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La recolección de información es la primera y más crucial fase en cualquier auditoría de seguridad. Al utilizar una combinación de técnicas de escaneo pasivo y activo, un auditor puede construir un mapa detallado de la superficie de ataque de una organización. Esto permite identificar vulnerabilidades de manera más eficiente y planificar ataques de forma más estratégica.

### Puntos de Aprendizaje Clave
* **Escaneo pasivo vs. activo**: La diferencia fundamental radica en la interacción. El pasivo utiliza información pública para obtener pistas sin contactar al objetivo, mientras que el activo realiza peticiones directas y requiere autorización.
* **Uso de diccionarios y buscadores**: Herramientas como **Dirsearch**, junto con diccionarios de palabras, son esenciales para descubrir recursos ocultos, mientras que los motores de búsqueda avanzados permiten encontrar información expuesta públicamente.
* **El contexto es fundamental**: Los resultados de la recolección de información no son un fin en sí mismos, sino un medio para entender la arquitectura y las tecnologías de una aplicación, lo que permite al auditor formular hipótesis sobre posibles vulnerabilidades.

### Relevancia Técnica
El dominio de las técnicas de recolección de información es una habilidad fundamental para cualquier profesional de la ciberseguridad. En un entorno profesional, estas habilidades se utilizan para realizar evaluaciones de vulnerabilidad, pruebas de penetración y para construir una inteligencia de amenazas sólida que proteja a la organización de ataques externos.

---

Documentos de Referencia: "AWEB - Recolección de información.pdf"

# Informe Técnico: Enumeración y Exposición de Información en Auditorías Web

## 1. Resumen Ejecutivo
Este informe detalla las técnicas de recolección de información, tanto pasiva como activa, para auditorías de aplicaciones web. Se definen las metodologías de **escaneo pasivo** (sin conexión directa) a través de buscadores avanzados (**dorks**) y fuentes públicas de datos filtrados (**leaks**), así como el **escaneo activo** (**fingerprinting**), que implica interactuar directamente con el objetivo. Se introducen herramientas y conceptos clave como **Shodan**, **Censys** y **Dirsearch**, y se explican las diferencias entre **Spidering** y **Crawling**. El informe concluye con una demostración práctica usando un entorno de laboratorio para ilustrar cómo estas técnicas se aplican para mapear la infraestructura y los recursos de una aplicación.

---

## 2. Conceptos Fundamentales

### Escaneo Pasivo (Passive Scanning)
El escaneo pasivo es la fase de recolección de información en la que un auditor no establece una conexión directa con el objetivo. En su lugar, se apoya en datos que el propio sistema ha expuesto públicamente. Los principales métodos son:
* **Dorks**: Son palabras clave y operadores de búsqueda avanzados que aprovechan los algoritmos de motores de búsqueda como **Google**, **Bing** y **Shodan** para encontrar información específica. Por ejemplo, `site:`, `inurl:`, `filetype:` y `cache:`.
* **Leaks**: Consisten en el uso de credenciales y datos sensibles expuestos en Internet a través de brechas de seguridad de otras organizaciones. Estos datos pueden incluir correos electrónicos, nombres de usuario y contraseñas. Herramientas como **Have I Been Pwned**, **Dehashed** o **Leak-lookup** permiten a un auditor verificar si las credenciales de un usuario han sido comprometidas.
* **Buscadores de seguridad**: Herramientas como **Shodan**, **Censys**, **Fofa**, **SecurityTrails**, **RiskIQ** y **ZoomEye** permiten buscar dispositivos y servicios expuestos en Internet, analizando sus configuraciones, certificados y tecnologías subyacentes sin necesidad de interactuar directamente con ellos.

### Escaneo Activo (Active Scanning) o Fingerprinting
El escaneo activo implica realizar peticiones directas al objetivo para obtener información. A diferencia del pasivo, este método requiere autorización previa del cliente o del propietario del activo. Su objetivo es identificar:
* **Servicios y protocolos disponibles**: Puertos abiertos y servicios que se están ejecutando.
* **Sistemas operativos y tecnologías**: El *software* del servidor, librerías, versiones, etc..
* **Configuraciones por defecto**: Archivos y directorios de instalación por defecto.
* **Recursos internos**: Directorios y archivos ocultos que pueden no estar enlazados.

### Spidering y Crawling
Estas dos técnicas son fundamentales en el escaneo activo:
* **Spidering**: Consiste en la extracción de enlaces de una aplicación web utilizando *scripts* automatizados, conocidos como *spiders*. Permite mapear la arquitectura y las interconexiones de la aplicación.
* **Crawling**: Es la búsqueda de archivos y directorios en una aplicación web mediante ataques de fuerza bruta con diccionarios. Esta técnica, también llamada **fuzzing**, permite descubrir recursos ocultos. Herramientas como **Dirsearch** y diccionarios como **Rockyou** o **SecLists** son esenciales para esta tarea.

---

## 3. Procedimientos Prácticos

### 1. Preparación del Entorno de Laboratorio
Antes de realizar un escaneo activo, se recomienda configurar un entorno de laboratorio controlado.
* **Instalación de Metasploitable2**: Se descarga e importa la máquina virtual **Metasploitable2** en un *software* de virtualización. Esta máquina está diseñada intencionalmente con servicios y configuraciones vulnerables para practicar ataques de forma segura.
* **Configuración de red**: Se configura la red de **Metasploitable2** en modo **NAT** para que sea accesible desde la máquina atacante, y se obtiene la dirección IP local de la víctima con `ifconfig`.

### 2. Escaneo de una Máquina Víctima con Dirsearch
El documento presenta un ejemplo de escaneo activo en **Metasploitable2** usando la herramienta `Dirsearch`.
* **Comando de ejecución**: `dirsearch -u http://192.168.106.132`.
    * `dirsearch`: Es la herramienta que realiza el escaneo.
    * `-u`: Especifica la URL del objetivo.
* **Análisis del *output***: El resultado del comando muestra una lista de archivos y directorios encontrados, junto con el código de estado **HTTP** (`200`, `403`, `404`, etc.) y el tamaño del recurso. El escaneo revela la existencia de recursos importantes, como:
    * `robots.txt`: Un archivo que puede contener pistas sobre directorios ocultos.
    * `phpMyAdmin/`: Un panel de administración de bases de datos que es un objetivo común.
    * `/admin/`: Un directorio de administración, lo que indica un posible punto de escalada de privilegios.
    * `/doc/`: Un directorio público que, al ser visitado, muestra una lista de archivos, lo que expone la estructura de directorios del servidor.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La recolección de información es la primera y más crucial fase en cualquier auditoría de seguridad. Al utilizar una combinación de técnicas de escaneo pasivo y activo, un auditor puede construir un mapa detallado de la superficie de ataque de una organización. Esto permite identificar vulnerabilidades de manera más eficiente y planificar ataques de forma más estratégica.

### Puntos de Aprendizaje Clave
* **Escaneo pasivo vs. activo**: La diferencia fundamental radica en la interacción. El pasivo utiliza información pública para obtener pistas sin contactar al objetivo, mientras que el activo realiza peticiones directas y requiere autorización.
* **Uso de diccionarios y buscadores**: Herramientas como **Dirsearch**, junto con diccionarios de palabras, son esenciales para descubrir recursos ocultos, mientras que los motores de búsqueda avanzados permiten encontrar información expuesta públicamente.
* **El contexto es fundamental**: Los resultados de la recolección de información no son un fin en sí mismos, sino un medio para entender la arquitectura y las tecnologías de una aplicación, lo que permite al auditor formular hipótesis sobre posibles vulnerabilidades.

### Relevancia Técnica
El dominio de las técnicas de recolección de información es una habilidad fundamental para cualquier profesional de la ciberseguridad. En un entorno profesional, estas habilidades se utilizan para realizar evaluaciones de vulnerabilidad, pruebas de penetración y para construir una inteligencia de amenazas sólida que proteja a la organización de ataques externos.

---

