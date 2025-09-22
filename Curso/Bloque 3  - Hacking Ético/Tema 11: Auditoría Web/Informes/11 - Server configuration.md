Documentos de Referencia: "AWEB - Configuración de servidores.pdf"

# Informe Técnico: Configuración de Servicios y Enumeración de Recursos

## 1. Resumen Ejecutivo
Este informe técnico profundiza en la configuración de seguridad de los servidores web y en las técnicas de enumeración de servicios y recursos. Se presenta a `nmap` como la herramienta fundamental para el descubrimiento de hosts, puertos y versiones de *software*. Además, se identifican archivos y directorios clave (como `robots.txt`, `sitemap.xml` y copias de seguridad) que pueden contener información sensible para un atacante. El documento concluye con la importancia de una configuración de servidor estricta y de una gestión de permisos rigurosa para mitigar los riesgos de seguridad.

---

## 2. Conceptos Fundamentales

### Servicios Web y Puertos
Las aplicaciones web se asocian típicamente a los puertos `80` para el protocolo **HTTP** y `443` para el protocolo **HTTPS**. Sin embargo, también pueden ejecutarse en puertos alternativos, como `8080`, `8081` o `8443`, a menudo para servicios de gestión o interfaces que no están destinadas al público general.

### Nmap (Network Mapper)
`Nmap` es una herramienta de código abierto versátil y popular para el descubrimiento de servicios y el mapeo de redes. Envía paquetes a un host y analiza las respuestas para determinar qué puertos están abiertos, qué servicios se están ejecutando, sus versiones específicas, el sistema operativo subyacente e incluso posibles vulnerabilidades asociadas.

### Recursos Sensibles
Durante una auditoría de seguridad, el análisis de los archivos y directorios expuestos es crucial. Algunos de los recursos más sensibles que un atacante buscaría son:
* **Archivos de infraestructura**: `robots.txt` y `sitemap.xml`. Mientras que `robots.txt` le indica a los motores de búsqueda qué rutas no deben indexar, un atacante puede usarlo para descubrir directorios ocultos. El archivo `sitemap.xml` contiene un mapa de todos los enlaces del sitio, revelando su arquitectura.
* **Copias de seguridad**: Archivos como `backup.db`, `files.old` o `database.bak`. Si están expuestos, pueden contener información valiosa como credenciales antiguas, datos de desarrollo o rutas de archivos que ya no existen, lo que le da al atacante una ventaja en el reconocimiento.
* **Interfaces de administración**: Son directorios o archivos comunes para la gestión de la aplicación, como `/admin`, `/wp-admin` o `/config`. Su enumeración es un paso clave en el proceso de ataque.
    

---

## 3. Procedimientos Prácticos

### 1. Escaneo de Servicios con Nmap
El escaneo con `nmap` es la fase principal para el descubrimiento de servicios.
* **Comando básico**: `nmap -sV -vv 192.168.186.132`.
    * `-sV`: Este parámetro es esencial para la detección de versiones, lo que permite identificar el tipo de software (ej. Apache, Nginx) y su versión, información clave para buscar vulnerabilidades conocidas.
    * `-vv`: Aumenta la verbosidad para obtener una salida más detallada de los resultados del escaneo.
* **Escaneo de puertos específicos**: Para un análisis más profundo, se puede limitar el escaneo a puertos específicos utilizando el parámetro `-p`. Por ejemplo, `nmap -p 21,80,443 <target>`.
* **Uso de scripts**: `nmap` permite ejecutar scripts de su base de datos para obtener más información. El parámetro `--script` se usa para filtrar por scripts específicos. Por ejemplo, el comando `nmap -sV -p 21 192.168.186.132 --script "*ftp*"` escanea el puerto `21` y ejecuta todos los scripts relacionados con **FTP**.

### 2. Enumeración de Recursos Sensibles
Una vez que se conocen los servicios, se buscan archivos y directorios vulnerables.
* **Ataques de fuerza bruta**: Se utilizan diccionarios con herramientas como **Dirsearch** para buscar rutas comunes de archivos y directorios de administración, o rutas específicas de tecnologías de servidor web (**Apache**, **Nginx**) y **CMS** (**WordPress**, **Drupal**).

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
Una configuración de servidor segura es la primera línea de defensa de una aplicación web. El beneficio de entender esta fase es que los administradores pueden aplicar una configuración de "mínimo privilegio", habilitando solo los puertos y servicios estrictamente necesarios. Esto reduce drásticamente la superficie de ataque y la sobrecarga de gestión.

### Puntos de Aprendizaje Clave
* **La información del escaneo es la base**: La salida de `nmap` proporciona una hoja de ruta para la auditoría, permitiendo al atacante pasar de una enumeración general a pruebas de penetración dirigidas a puertos y servicios específicos.
* **El control de acceso es fundamental**: Los directorios sensibles, como las interfaces de administración o las carpetas de copias de seguridad, deben estar protegidos con un control de acceso riguroso para evitar que usuarios no autorizados accedan a ellos.

### Relevancia Técnica
El dominio de herramientas como `nmap` y las técnicas de enumeración es una habilidad crucial para los profesionales de la ciberseguridad. Permite evaluar de manera proactiva la postura de seguridad de un sistema y prevenir ataques basados en configuraciones incorrectas o la exposición de información sensible.

---

Documentos de Referencia: "AWEB - Configuración de servidores.pdf"

# Informe Técnico: Configuración de Servidores Web, Métodos, Cabeceras y Cookies

## 1. Resumen Ejecutivo
Este informe técnico profundiza en la auditoría de la configuración de servidores web, centrándose en el análisis de los **métodos HTTP**, las **cabeceras de seguridad** y las **cookies**. Se establece una conexión lógica entre el escaneo inicial de servicios y la posterior revisión detallada de la configuración. A través de un ejercicio práctico utilizando `nmap`, `Burp Suite` y otras herramientas, se demuestra cómo un auditor puede identificar configuraciones seguras y vulnerables en sitios web reales. El objetivo es resaltar la importancia de estas capas de defensa para una postura de seguridad robusta.

---

## 2. Conceptos Fundamentales

### El Flujo de una Auditoría Web
En una auditoría de seguridad web, la información obtenida en cada fase es crucial para la siguiente. El proceso comienza con el **escaneo pasivo** (sin conexión directa al objetivo) y el **escaneo activo**. Con herramientas como `nmap`, se descubren los servicios expuestos en un servidor. Este conocimiento inicial permite pasar a un análisis más granular, centrado en cómo la aplicación maneja las peticiones a través de **métodos HTTP**, cómo se defiende con **cabeceras de seguridad** y cómo gestiona el estado con **cookies**.

### Métodos HTTP o Verbos
Los métodos HTTP son las acciones que se pueden realizar sobre un recurso en un servidor web. Cada método tiene un propósito específico:
* **`GET`**: Obtiene información.
* **`HEAD`**: Obtiene solo las cabeceras de la respuesta.
* **`POST`**: Envía datos para crear o actualizar un recurso.
* **`OPTIONS`**: Muestra los métodos que un servidor acepta para un recurso.
* **`PUT` y `DELETE`**: Se utilizan para reemplazar o eliminar un recurso. Su uso indiscriminado representa un riesgo significativo de seguridad.

### Cabeceras de Seguridad HTTP
Estas cabeceras son directivas que el servidor envía al navegador para reforzar la seguridad. Las principales son:
* **`Strict-Transport-Security` (HSTS)**: Fuerza al navegador a usar **HTTPS** en lugar de **HTTP**, asegurando que el tráfico esté cifrado.
* **`X-Frame-Options`**: Evita que una página se cargue en un `<iframe>`, previniendo ataques de *clickjacking*.
* **`Content-Security-Policy` (CSP)**: Ayuda a prevenir ataques de inyección como **XSS** al especificar qué fuentes de contenido son seguras.
* **`X-XSS-Protection`**: Una cabecera para proteger contra ataques de inyección de **JavaScript**.
* **`X-Content-Type-Options`**: Obliga al navegador a respetar el tipo de contenido (`MIME type`), previniendo ataques de "adivinación de tipo de contenido".

### Cookies y sus Banderas de Seguridad
Las cookies son esenciales para que el protocolo **HTTP**, que es sin estado, pueda mantener la sesión y el estado del usuario. Se configuran con la directiva `Set-Cookie` y pueden tener banderas de seguridad que añaden capas de defensa:
* **`HttpOnly`**: Impide que `JavaScript` acceda al valor de la cookie, protegiendo contra el robo de cookies en ataques **XSS**.
* **`Secure`**: Garantiza que la cookie solo se envíe a través de una conexión **HTTPS**.
* **`SameSite`**: Previene los ataques de **Cross-Site Request Forgery (CSRF)** al restringir el envío de la cookie a peticiones que provengan del mismo sitio.

---

## 3. Procedimientos Prácticos

### 1. Escaneo de Servicios con `nmap`
El ejercicio comienza con un escaneo a la máquina virtual **Metasploitable** (`192.168.186.132`) para identificar sus servicios.
* **Comando**: `nmap -sV -vv -A 192.168.186.132`.
* **Resultado**: `nmap` identifica el puerto `80` con un servidor web **Apache httpd 2.2.8**. Más importante aún, los *scripts* de `nmap` (`-A`) revelan que los métodos HTTP soportados son `GET`, `HEAD`, `POST` y `OPTIONS`.

### 2. Análisis de Cabeceras en Sitios Web Conocidos
Se auditan tres sitios web (`apple.com`, `tesla.com`, `wikipedia.org`) para analizar sus cabeceras de seguridad.
* **Burp Suite y Navegador**: Usando el proxy de Burp o el inspector de elementos del navegador, se examinan las cabeceras de respuesta. Por ejemplo, `apple.com` tiene una configuración robusta, con `Content-Security-Policy`, `HSTS`, `X-Content-Type-Options`, `X-XSS-Protection` y `X-Frame-Options`. En cambio, un sitio como Wikipedia muestra solo `Strict-Transport-Security` y `X-Content-Type-Options`.
* **`shcheck`**: Para una verificación automatizada, la herramienta `shcheck` confirma la presencia o ausencia de estas cabeceras. Por ejemplo, en `0xword.com`, el resultado muestra que `Strict-Transport-Security` está presente.

### 3. Análisis de Métodos HTTP Disponibles
Se utiliza la herramienta **Repeater** de `Burp Suite` para enviar peticiones `OPTIONS` a los sitios web.
* **Tesla.com**: El servidor responde con `200 OK` y una cabecera `Allow` que lista los métodos soportados (`GET`, `HEAD`, `POST`, `OPTIONS`).
* **Apple.com y Wikipedia.org**: Sus servidores responden con `403 Forbidden` o `405 Method Not Allowed`. Esto es una buena práctica de seguridad que impide la enumeración de métodos.

### 4. Análisis de Cookies y sus Flags de Seguridad
Se examinan las cookies de los sitios web para ver qué banderas de seguridad tienen configuradas.
* **Wikipedia**: Las cookies tienen el *flag* `Secure`, lo cual es una buena práctica.
* **Apple**: En una cookie específica, se observa que no tiene las banderas `HttpOnly`, `Secure` o `SameSite`, lo que contrasta con sus robustas cabeceras de seguridad y representa un posible punto débil.
* **Tesla**: Las cookies están configuradas con los *flags* `HttpOnly` y `Secure`, lo que demuestra una sólida defensa contra el robo y la manipulación de cookies.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La auditoría de la configuración del servidor no es una tarea aislada, sino una parte integral de un proceso de reconocimiento más amplio. La evaluación de los métodos HTTP, las cabeceras de seguridad y las cookies permite a los auditores obtener una visión completa del perfil de seguridad de una aplicación, lo que es esencial para la defensa y la remediación.

### Puntos de Aprendizaje Clave
* **La seguridad es un espectro**: Los resultados de la auditoría demuestran que la seguridad no es un estado binario, sino que depende de múltiples capas de defensa. Un sitio puede ser robusto en sus cabeceras, pero tener debilidades en sus cookies.
* **Metodología de auditoría**: El uso de herramientas como `nmap`, `Burp Suite` y `shcheck` en un flujo de trabajo estructurado permite pasar de un escaneo general a un análisis granular de las configuraciones de seguridad, lo cual es la clave para una auditoría exitosa.
* **El contexto es fundamental**: El análisis de la respuesta del servidor es crucial. Un `403 Forbidden` puede no ser un error, sino una medida de seguridad que impide la enumeración de métodos por parte de un atacante.

### Relevancia Técnica
El dominio de estas técnicas es una habilidad indispensable para cualquier profesional de la ciberseguridad. Permite evaluar de manera proactiva la postura de seguridad de una organización, identificar vectores de ataque potenciales y recomendar medidas de protección efectivas.