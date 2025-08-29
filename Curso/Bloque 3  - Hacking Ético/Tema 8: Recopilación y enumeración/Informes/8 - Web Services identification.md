Documentos de Referencia: "RE - Web Services identification.pdf"

# Informe Técnico: Identificación de Tecnologías y Servicios Web

## 1. Resumen Ejecutivo
Este informe se enfoca en la identificación de tecnologías y versiones de servicios web, una etapa crucial en la fase de recopilación de información de una auditoría de seguridad. Se presentan dos herramientas principales: **WhatWeb** y **Wappalyzer**. Se explican sus mecanismos de funcionamiento (activo y pasivo, respectivamente), sus capacidades y sus aplicaciones prácticas en un entorno de laboratorio controlado con una máquina Kali Linux y una Metasploitable 3. El informe detalla cómo estas herramientas pueden detectar sistemas de gestión de contenido, servidores web, lenguajes de programación, librerías y otros componentes, demostrando su valor para identificar posibles vulnerabilidades y planificar estrategias de seguridad.

---

## 2. Conceptos Fundamentales

### 2.1. WhatWeb
* **Definición:** Es una herramienta de código abierto desarrollada en Ruby que se utiliza para reconocer tecnologías web en un sitio o aplicación. Es versátil y popular entre profesionales de la seguridad, desarrolladores y administradores de sistemas. Utiliza más de 1.200 plugins para identificar tecnologías.
* **Funcionamiento:** Opera de manera **activa**, enviando peticiones HTTP al sitio web y analizando la respuesta en busca de patrones en el código HTML, las cabeceras HTTP, las cookies y otros elementos.
* **Características:**
    * Reconoce una amplia gama de tecnologías, incluyendo **CMS (Content Management Systems)**, plataformas de blogs, servidores web, librerías de JavaScript y dispositivos embebidos.
    * Permite ajustar el nivel de **agresividad** del escaneo, desde un modo "sigiloso" (nivel 1) con una petición por objetivo, hasta un modo "agresivo" (nivel 3) con peticiones adicionales para una detección más profunda.
    * Soporta múltiples formatos de salida (texto, HTML, JSON, XML) y se puede utilizar a través de un **proxy Tor** para mayor privacidad.

### 2.2. Wappalyzer
* **Definición:** Es una herramienta de identificación de tecnologías web que, a diferencia de WhatWeb, funciona principalmente como una extensión de navegador. Fue de código abierto, pero su desarrollo ahora es privado.
* **Funcionamiento:** Opera de manera **pasiva**. No envía peticiones adicionales al servidor, sino que analiza la página web que ya ha sido cargada en el navegador. Examina elementos como cabeceras HTTP, el código fuente y la estructura de archivos para identificar las tecnologías.
* **Características:**
    * Detecta una gran variedad de tecnologías, como herramientas de analítica, frameworks de JavaScript, lenguajes de programación, sistemas de gestión de bases de datos, y librerías de JavaScript populares.
    * Su formato más popular es una extensión para navegadores como Chrome, Firefox y Edge, proporcionando un reconocimiento rápido y visual.
    * También cuenta con una versión de línea de comandos (CLI) que se instala a través de Node.js, lo que permite la automatización e integración en scripts.

### 2.3. Comparación entre WhatWeb y Wappalyzer

| Característica | WhatWeb | Wappalyzer |
| :--- | :--- | :--- |
| **Modo de Operación** | Activo (envía peticiones) | Pasivo (analiza el tráfico existente) |
| **Mejor para** | Escaneo de rangos de IP, auditorías automatizadas y análisis detallado desde la terminal. | Reconocimiento rápido y visual, uso diario y escaneo discreto a nivel de navegador. |
| **Detección** | A menudo detecta tecnologías más oscuras o de bajo nivel. | Sobresale en la detección de frameworks y librerías populares. |

Se recomienda utilizar ambas herramientas de forma complementaria en una auditoría de seguridad para obtener una visión completa de las tecnologías del front-end (con Wappalyzer) y un análisis más profundo y activo (con WhatWeb).

---

## 3. Procedimientos Prácticos

El entorno de laboratorio utilizado incluye una máquina Kali Linux (10.0.1.5) y una Metasploitable 3 (10.0.1.9). Se demuestra la identificación de tecnologías en esta última, que expone varios servicios web, y en una instancia de OWASP Juice Shop.

### 3.1. Identificación de Servicios en Metasploitable 3 con WhatWeb
1.  **Análisis del servicio `/chat`:**
    * **Comando:** `whatweb http://10.0.1.9/chat/`.
    * **Resultado:** La herramienta identifica el servidor web como **Apache/2.4.7 (Ubuntu)** y el lenguaje de programación como **PHP 5.4.5**.
2.  **Análisis del servicio `/drupal`:**
    * **Comando:** `whatweb http://10.0.1.9/drupal/`.
    * **Resultado:** Además de Apache y PHP, WhatWeb detecta que la página está usando **JavaScript**, **jQuery**, y se trata de una aplicación **Drupal 7**.
3.  **Análisis del servicio `/phpmyadmin`:**
    * **Comando:** `whatweb http://10.0.1.9/phpmyadmin/`.
    * **Resultado:** La herramienta identifica el servidor **Apache 2.4.7**, la versión de **PHP 5.4.5**, y librerías como **jQuery 1.6.2**, confirmando que se trata de una instalación de **phpMyAdmin**.

### 3.2. Identificación de Servicios en Metasploitable 3 con Wappalyzer
1.  **Instalación:** Se instala la extensión Wappalyzer en el navegador Firefox de la máquina Kali.
2.  **Análisis visual:** Al navegar a `10.0.1.9`, la extensión se activa y al hacer clic en su icono, se abre una ventana que muestra un resumen consolidado de todas las tecnologías detectadas en los diferentes subdominios.
3.  **Resultado:** Wappalyzer detecta:
    * **CMS:** Drupal 7
    * **Lenguajes de programación:** PHP 5.4.5
    * **Servidor web:** Apache HTTP Server 2.4.7
    * **Gestor de base de datos:** phpMyAdmin
    * **Bases de datos:** MySQL
    * **Sistema operativo:** Ubuntu
    * **Librerías de JavaScript:** jQuery 1.6.2 y jQuery UI 1.8.16.

### 3.3. Identificación de Servicios en OWASP Juice Shop con ambas herramientas
1.  **Configuración del laboratorio:** Se utiliza Docker para montar la aplicación vulnerable **OWASP Juice Shop**.
    * **Comando:** `docker run -rm -p 3000:3000 bkimminich/juice-shop`.
    * **Resultado:** El servidor queda disponible en `http://localhost:3000`.
2.  **Análisis con WhatWeb:**
    * **Comando:** `whatweb http://localhost:3000`.
    * **Resultado:** WhatWeb detecta que la página utiliza **HTML5** y **jQuery 2.2.4**, pero no proporciona mucha más información.
3.  **Análisis con Wappalyzer:**
    * Se navega a `http://localhost:3000` en el navegador con la extensión instalada.
    * **Resultado:** Wappalyzer identifica una gama más amplia de tecnologías que WhatWeb, incluyendo: **Angular 15.2.10**, **TypeScript**, **Font Awesome**, y librerías como **jQuery 2.2.4** y **core-js 3.35.0**.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
La identificación de tecnologías web es un paso indispensable en la auditoría de seguridad. Revelar los componentes de un sitio web, como el servidor, el CMS y las librerías, permite a los auditores identificar rápidamente las vulnerabilidades conocidas asociadas a esas versiones. Esto reduce significativamente el tiempo de reconocimiento y permite enfocar los esfuerzos en la explotación de debilidades específicas, mejorando la eficiencia y efectividad de la auditoría.

### 4.2. Puntos de Aprendizaje Clave
* **WhatWeb y Wappalyzer:** Se ha aprendido a utilizar ambas herramientas, entendiendo sus diferencias en el modo de operación (activo vs. pasivo) y sus respectivos casos de uso.
* **Ventajas de cada herramienta:** WhatWeb es ideal para escaneos automatizados y profundos desde la terminal, mientras que Wappalyzer destaca en el reconocimiento rápido y discreto a nivel de navegador.
* **Identificación de tecnologías:** La práctica demuestra cómo estas herramientas pueden extraer información valiosa, como las versiones de Apache, PHP, Drupal, jQuery y Angular, que son datos fundamentales para cualquier evaluación de seguridad.

### 4.3. Relevancia Técnica
La habilidad para utilizar estas herramientas de forma complementaria es de gran relevancia profesional. Permite a los profesionales de la seguridad obtener una comprensión detallada del stack tecnológico de un objetivo. Esto no solo es útil para las auditorías, sino también para los administradores de sistemas que necesitan mantener sus plataformas actualizadas y seguras. Dominar estas técnicas de identificación de servicios es una habilidad fundamental para cualquier persona en el campo de la ciberseguridad, ya que facilita la transición de la fase de recopilación de información a la de análisis de vulnerabilidades y explotación.