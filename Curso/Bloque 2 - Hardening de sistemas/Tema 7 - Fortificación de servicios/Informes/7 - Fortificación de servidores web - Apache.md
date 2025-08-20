Documentos de Referencia: "FS - Fortificación de servidores web - Apache.pdf"

# Informe Técnico: Fortificación de Servidores Web Apache

### 1\. Resumen Ejecutivo

Este informe técnico analiza la fortificación de servidores web, con un enfoque en **Apache HTTP Server**. Se describen los conceptos fundamentales de los servidores web, su funcionamiento y los principales tipos disponibles, junto con las amenazas más comunes a las que se enfrentan. A través de demostraciones prácticas, se muestra cómo obtener información sobre un servidor web expuesto y cómo mitigar la divulgación de información sensible. El informe detalla los procedimientos para la instalación, configuración inicial y avanzada de Apache, incluyendo la gestión de módulos y la configuración de logs. Finalmente, se abordan medidas de seguridad críticas como la implementación de un firewall de aplicaciones web (**mod\_security**) y la habilitación de tráfico cifrado con **HTTPS**, lo que demuestra la importancia de adoptar una postura de seguridad proactiva.

-----

### 2\. Conceptos Fundamentales

  * **Servidor Web:** Un servidor web es un software que procesa solicitudes a través de protocolos como **HTTP** o **HTTPS** para entregar contenido web a un cliente. El funcionamiento se basa en el modelo cliente-servidor: el cliente envía una petición y el servidor responde con los recursos necesarios.

      * **Componentes principales:**
          * **Servidor:** El software que maneja las peticiones y proporciona respuestas como imágenes, videos o código HTML.
          * **Protocolo:** Los protocolos utilizados son **HTTP** (menos seguro) y **HTTPS**, que emplea cifrado **SSL/TLS** para una comunicación segura y encriptada.
          * **Contenido:** Son los archivos y datos que componen el sitio web (HTML, CSS, JavaScript, imágenes) y que se envían al cliente.
      * **Tipos de peticiones:** Los dos tipos principales de peticiones son **GET**, utilizada para obtener datos del servidor (ej. acceder a una página web), y **POST**, utilizada para enviar datos al servidor (ej. rellenar un formulario).

  * **Tipos de Servidores Web:**

      * **Apache HTTP Server:** Uno de los servidores web más populares y utilizados a nivel mundial. Es de código abierto, multiplataforma y destaca por su modularidad y estabilidad.
      * **Nginx:** Un servidor web y proxy inverso de alto rendimiento, conocido por su eficiencia en el manejo de un gran número de conexiones simultáneas.
      * **Internet Information Services (IIS):** Desarrollado por Microsoft e integrado en sistemas operativos Windows. Se integra con tecnologías de Microsoft y ofrece una interfaz gráfica de usuario para su administración.

  * **Importancia de la Seguridad en Servidores Web:** Los servidores web son un objetivo principal para los atacantes debido a su exposición pública en Internet. Una seguridad deficiente puede resultar en la pérdida de datos, daños a la reputación e interrupción del servicio.

      * **Principales amenazas:**
          * **Ataques de denegación de servicio (DDoS):** Saturan el servidor con un gran volumen de tráfico malicioso, impidiendo que responda a solicitudes legítimas.
          * **Inyección SQL (SQL Injection):** Permite la manipulación y extracción de datos sensibles o la ejecución de comandos no autorizados.
          * **Cross-Site Scripting (XSS):** Los atacantes inyectan scripts maliciosos en el navegador de un usuario para robar información de sesión o realizar acciones no deseadas.
          * **Directory Traversal:** Aprovecha fallos de validación para acceder a directorios sensibles o ejecutar archivos no autorizados en el servidor.
          * **Ingeniería Social (Social Engineering):** Ataques como el phishing para obtener acceso no autorizado a sistemas.
          * **Botnets:** Redes de dispositivos comprometidos utilizadas para lanzar ataques coordinados o realizar otras actividades maliciosas.

  * **Apache Core (`httpd`):** El componente central del servidor Apache, encargado de administrar las solicitudes HTTP, procesar la configuración y gestionar las aplicaciones internas.

  * **`mod_security`:** Un módulo de Apache que actúa como un **Web Application Firewall (WAF)**. Permite filtrar y proteger el servidor de ataques web comunes mediante un conjunto de reglas conocido como **Core Rule Set (CRS)**.

-----

### 3\. Procedimientos Prácticos

A continuación, se describen los procedimientos prácticos en una máquina con sistema operativo Ubuntu.

#### 3.1. Instalación y Verificación de Apache

1.  **Actualización del listado de paquetes:**

      * **Comando:** `sudo apt update`.
      * **Explicación:** Se actualizan las fuentes de paquetes del sistema para asegurar que se instalen las últimas versiones.

2.  **Instalación de Apache:**

      * **Comando:** `sudo apt install apache2`.
      * **Explicación:** Instala el paquete de Apache 2 y sus módulos por defecto de forma automatizada.

3.  **Verificación del estado del servicio:**

      * **Comando:** `sudo systemctl status apache2`.
      * **Explicación:** Muestra el estado del servicio **Apache**. La salida del comando indica que el servicio está cargado (`loaded`), habilitado (`enabled`), y activo (`active (running)`), como se muestra en la captura de pantalla.

4.  **Acceso a la página de prueba:**

      * **Acción:** Se accede a `http://localhost` desde un navegador en la misma máquina o a `http://ip_servidor` desde otra máquina en la misma red.
      * **Resultado:** Se muestra la página por defecto de Apache, lo que confirma que el servicio está operativo y es accesible, como se muestra en las capturas de pantalla.

#### 3.2. Fortificación de la Información del Servidor

1.  **Obtener información del servidor expuesta:**

      * **Comando:** `wget --server-response --spider http://www.as.com`.
      * **Explicación:** Se usa `wget` para simular una petición web. `--server-response` muestra las cabeceras de respuesta del servidor y `--spider` evita descargar el contenido, solo rastrea la página. El comando demuestra cómo se puede obtener información del servidor web, como el tipo, versión y sistema operativo, como se muestra en la captura de pantalla.

2.  **Deshabilitar la firma del servidor:**

      * **Acción:** Se edita el archivo de configuración de seguridad, `security.conf`, y se configuran las directivas `ServerTokens` y `ServerSignature`.
      * **Comandos:**
          * `sudo nano /etc/apache2/conf-available/security.conf`.
          * Se busca y se modifica `ServerTokens` a `Prod` para que solo muestre el nombre del servidor.
          * Se busca y se modifica `ServerSignature` a `Off` para eliminar la firma del servidor de las páginas de error.
      * **Reiniciar Apache:** `sudo systemctl restart apache2`.
      * **Resultado:** Al forzar un error 404, la página ya no muestra información detallada sobre la versión de Apache o el sistema operativo, lo que reduce la información disponible para un atacante, como se muestra en la captura de pantalla.

#### 3.3. Gestión de Módulos de Apache

1.  **Desactivar módulos innecesarios:**

      * **Comando:** `sudo a2dismod autoindex`.
      * **Explicación:** El comando `a2dismod` desactiva un módulo de Apache. El módulo `autoindex` muestra una lista del contenido de un directorio si no hay un archivo de índice, lo que puede exponer información sensible. Para desactivarlo, el sistema solicita una frase de confirmación.

2.  **Verificar el cambio:**

      * **Comando:** `sudo a2dismod`.
      * **Explicación:** El comando sin parámetros lista los módulos que se pueden deshabilitar. Una vez desactivado `autoindex`, este ya no aparecerá en la lista.

#### 3.4. Implementación del Web Application Firewall (`mod_security`)

1.  **Instalación:**

      * **Comando:** `sudo apt install libapache2-mod-security2`.
      * **Explicación:** Instala el módulo de Apache para el firewall de aplicaciones web.

2.  **Configuración inicial:**

      * **Comando:** `sudo mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf`.
      * **Explicación:** Renombra el archivo de configuración recomendado para activarlo como el principal.
      * **Comando:** `sudo a2enmod security2`.
      * **Explicación:** Habilita el módulo de seguridad en Apache.
      * **Comando:** `sudo nano /etc/modsecurity/modsecurity.conf`.
      * **Explicación:** Se edita el archivo y se cambia la directiva `SecRuleEngine` de `DetectionOnly` a `On` para que el módulo bloquee las peticiones maliciosas en lugar de solo detectarlas.

3.  **Instalar reglas de seguridad:**

      * **Comando:** `sudo apt install modsecurity-crs`.
      * **Explicación:** Instala las reglas de seguridad predefinidas de **OWASP CRS** (Core Rule Set) para proteger el servidor de ataques comunes.

4.  **Prueba de concepto:**

      * **Acción:** En una terminal, se utiliza `sudo tail -f /var/log/apache2/modsec_audit.log` para monitorear los logs de `mod_security` en tiempo real. En otra terminal, se simulan dos ataques:
          * **Inyección de comandos:** `curl -X GET "http://localhost/?exec=/bin/bash"`.
          * **Inyección SQL:** `curl -X GET "http://localhost/?id=1%20OR%201=1"`.
      * **Resultado:** En ambos casos, el navegador muestra un error `403 Forbidden`. El log de `mod_security` registra y detalla la detección de la inyección de comandos (`Remote Command Execution: Unix Shell Code Found`) y de la inyección SQL (`SQL Injection Attack Detected via libinjection`), como se muestra en las capturas de pantalla.

#### 3.5. Configuración de HTTPS y Redirección Automática

1.  **Habilitar SSL:**

      * **Comando:** `sudo a2ensite default-ssl`.
      * **Comando:** `sudo a2enmod ssl`.
      * **Explicación:** Se habilitan el sitio por defecto para SSL y el módulo SSL en Apache, lo que permite el uso del protocolo HTTPS. Es necesario reiniciar Apache después de la configuración.

2.  **Configurar la redirección automática a HTTPS:**

      * **Comando:** `sudo a2enmod rewrite`.
      * **Explicación:** Habilita el módulo de reescritura de URLs de Apache.
      * **Comando:** `sudo nano /etc/apache2/sites-available/000-default.conf`.
      * **Explicación:** Se edita el archivo de configuración del sitio por defecto para añadir las siguientes directivas, como se muestra en la captura de pantalla:
        ```
        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule ^(.*)$ https://localhost/$1 [L,R]
        ```
      * **Resultado:** Al intentar acceder a `http://localhost`, el navegador se redirige automáticamente a `https://localhost`, lo que garantiza que todo el tráfico se realice a través del protocolo seguro.

-----

### 4\. Conclusiones y Puntos Clave

  * **Importancia y Beneficios de Seguridad:** Fortificar los servidores web es una tarea crítica para cualquier organización, ya que estos son el principal punto de contacto con el público. La correcta fortificación protege la **integridad, confidencialidad y disponibilidad** de los datos y servicios, previniendo daños reputacionales y pérdidas económicas. Conocer las amenazas más comunes permite adoptar una postura de seguridad proactiva y eficaz.

  * **Puntos de Aprendizaje Clave:**

      * Se ha comprendido el funcionamiento de los servidores web, sus componentes y los tipos de peticiones que manejan.
      * Se ha aprendido a obtener información de un servidor web y a mitigar la exposición de datos sensibles como la versión del servidor y el sistema operativo.
      * Se ha dominado la instalación y verificación de Apache, así como la gestión de sus módulos para una configuración más segura.
      * Se ha aprendido a implementar un firewall de aplicaciones web (**mod\_security**) y a configurar reglas de seguridad para interceptar ataques comunes como la inyección SQL y la ejecución remota de comandos.
      * Se ha comprendido la importancia de **HTTPS** para la encriptación de datos y se ha aprendido a configurar la redirección automática de HTTP a HTTPS, lo que asegura que todas las comunicaciones sean seguras.

  * **Relevancia Técnica:** Los procedimientos detallados en este informe son esenciales para los administradores de sistemas y profesionales de la ciberseguridad. La capacidad de fortificar Apache, un servidor ampliamente utilizado, mediante la gestión de módulos, la configuración de cabeceras de respuesta y la implementación de herramientas como **mod\_security** y la redirección a **HTTPS**, son habilidades cruciales en el mundo profesional para mantener los servidores seguros y funcionales. El análisis de logs es vital para la detección y respuesta a incidentes, reforzando la postura de seguridad de un sistema.