Documentos de Referencia: "AWEB - Set up de entornos y Proxies.pdf"

# Informe Técnico: Montaje de Entornos de Laboratorio y Configuración de Burp Suite

## 1. Resumen Ejecutivo
Este informe detalla el proceso de creación de un entorno de laboratorio local para practicar el *hacking* y las auditorías de aplicaciones web de forma segura y legal. Se presentan tres entornos vulnerables intencionalmente: **DVWA**, **Web for Pentester** y **Juice Shop**. Adicionalmente, se explica la configuración y el uso de **Burp Suite** como un proxy web esencial para interceptar y manipular el tráfico **HTTP/HTTPS**. El informe subraya la importancia de estas herramientas y entornos para que los profesionales de la ciberseguridad puedan comprender y explotar vulnerabilidades de manera efectiva.

---

## 2. Conceptos Fundamentales

### Entornos de Laboratorio
Los entornos de laboratorio son máquinas virtuales o aplicaciones diseñadas intencionalmente para ser vulnerables. Su propósito es servir como un espacio controlado para que los profesionales y estudiantes puedan practicar la detección y explotación de fallos en la lógica de las aplicaciones web, sin incurrir en problemas legales. Estos entornos ofrecen:

* **DVWA (Damn Vulnerable Web Application)**: Una aplicación con vulnerabilidades comunes de auditoría web. Cuenta con cuatro niveles de seguridad (**Low**, **Medium**, **High**, **Impossible**), que permiten a los usuarios escalar la dificultad y refinar sus técnicas de explotación.
* **Web for Pentester**: Dos máquinas virtuales con una gran variedad de vulnerabilidades y ejemplos prácticos. La dificultad aumenta progresivamente desde el ejemplo 1 en adelante.
* **Juice Shop**: Un entorno que simula una tienda en línea real. Es menos guiado, lo que obliga a los usuarios a buscar vulnerabilidades de forma más autónoma, como lo harían en un escenario de auditoría real. El entorno está gamificado y tiene un *dashboard* secreto para seguir el progreso.

### Proxy Web y Burp Suite
Un **proxy web** es un intermediario entre el navegador de un usuario y la aplicación web a la que intenta acceder. Su función en las auditorías de seguridad es interceptar, analizar y modificar las peticiones y respuestas para encontrar vulnerabilidades.

**Burp Suite** es la herramienta de proxy web más utilizada por los auditores. Su versión gratuita, **Burp Suite Community Edition**, ofrece funcionalidades clave como:
* **Proxy**: La funcionalidad central que permite interceptar peticiones y respuestas.
* **Repeater**: Una herramienta para manipular una petición capturada y reenviarla al servidor varias veces para observar su comportamiento.
* **Intruder**: Una herramienta avanzada para automatizar ataques personalizados, como la fuerza bruta, las inyecciones **SQL** y **XSS**, contra puntos específicos de una petición.
* **Decoder**: Una utilidad para codificar y decodificar datos en varios formatos (**Base64**, **URL**, etc.), lo que es útil para analizar la información en *cookies* o parámetros.
* **Comparer**: Una herramienta para comparar visualmente dos peticiones o respuestas y detectar diferencias sutiles que podrían indicar una vulnerabilidad.

---

## 3. Procedimientos Prácticos

### 1. Configuración de los Entornos de Laboratorio
El informe describe la instalación de los entornos de prueba, prefiriendo **Docker** para su rapidez y sencillez.
* **Instalación de Docker**: El primer paso es instalar Docker en la máquina atacante (Kali). Esto se logra con los comandos `sudo apt update`, `sudo apt install -y docker.io` y `sudo systemctl enable docker --now`. Se verifica su correcto funcionamiento con `sudo docker run hello-world`.
* **Despliegue de DVWA**: Se utiliza Docker para descargar y ejecutar la imagen de DVWA. El comando `sudo docker run -p 80:80 --name dvwa vulnerables/web-dvwa` descarga la imagen, expone el puerto `80` del contenedor al puerto `80` del *localhost* y le asigna el nombre `dvwa`. Para detenerlo, se usa `sudo docker stop dvwa` y para iniciarlo `sudo docker start dvwa`.
* **Despliegue de Juice Shop**: El proceso es similar al de DVWA. Los comandos son `sudo docker pull bkimminich/juice-shop` y `sudo docker run --rm -p 3000:3000 --name juice bkimminich/juice-shop`. Juice Shop se ejecuta en el puerto `3000` y se accede a él a través de `http://localhost:3000`.
* **Instalación de Web for Pentester**: Este entorno se instala importando archivos de máquina virtual (`.ova`) descargados desde **Pentester Lab** o **VulnHub** a un hipervisor como **VMware**.

### 2. Configuración de Burp Suite y FoxyProxy
Para utilizar Burp Suite, es necesario configurar el navegador y el proxy.
* **Configuración del navegador**: Se deben cambiar los ajustes del navegador para que todo el tráfico pase por el proxy de Burp, que se encuentra en la dirección `127.0.0.1` en el puerto `8080`.
* **Certificado HTTPS**: Para interceptar tráfico **HTTPS**, es crucial descargar e instalar el certificado de la **Autoridad de Certificación (CA)** de Burp, ya que de lo contrario el navegador bloqueará las conexiones seguras.
* **Uso de FoxyProxy**: Para gestionar la configuración del proxy de manera eficiente, se recomienda instalar el complemento de navegador **FoxyProxy**. Este permite activar o desactivar el proxy con un solo clic, sin tener que navegar por los ajustes del navegador.

### 3. Ejemplo de Interceptación con Burp
El informe proporciona un ejemplo práctico del uso del proxy de Burp.
* **Interceptar petición**: Se activa la función `Intercept` en Burp Suite. Al intentar iniciar sesión en una aplicación, la petición se detiene en Burp, permitiendo al auditor inspeccionar y modificar los datos antes de que lleguen al servidor.
* **Modificar y reenviar**: Se puede cambiar el valor de un parámetro, por ejemplo, de `hola` a `adios`, y luego reenviar la petición con el botón `Forward`. Esto demuestra cómo se puede manipular el comportamiento de la aplicación en tiempo real.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La configuración de entornos de prueba es el primer paso indispensable para cualquier persona que desee aprender o dedicarse a la ciberseguridad web. Al trabajar en un entorno controlado, se puede practicar de forma ética y eficaz. La herramienta **Burp Suite** es fundamental en este proceso, ya que su capacidad para interceptar y manipular el tráfico web permite un análisis detallado del comportamiento de las aplicaciones, lo cual es imposible de hacer con una simple navegación.

### Puntos de Aprendizaje Clave
* **Práctica ética y legal**: Es imperativo practicar solo en entornos controlados para evitar consecuencias legales. La autorización es obligatoria para auditar cualquier sitio en vivo.
* **La navaja suiza del *pentester***: Burp Suite es una herramienta multifuncional que, más allá de ser un proxy, ofrece un conjunto de utilidades para diversas fases del ataque, desde la enumeración (**Comparer**, **Decoder**) hasta la explotación (**Repeater**, **Intruder**).
* **Metodología estructurada**: La combinación de entornos de prueba con diferentes niveles de dificultad, junto con las herramientas de Burp, permite seguir un proceso de aprendizaje estructurado y metódico para dominar las técnicas de auditoría web.

### Relevancia Técnica
El dominio de la configuración de entornos de laboratorio y del uso de un proxy web como Burp Suite son habilidades técnicas de alta relevancia profesional. Son la base para realizar auditorías de seguridad web, y un profesional que domina estas herramientas puede identificar vulnerabilidades de manera más rápida y organizada. El conocimiento de estas herramientas permite no solo atacar, sino también entender cómo defender una aplicación web de manera más efectiva.