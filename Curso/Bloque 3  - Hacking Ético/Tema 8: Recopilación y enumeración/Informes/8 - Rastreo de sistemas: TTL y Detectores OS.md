Documentos de Referencia: "RE - Rastreo de sistemas_ TTL y Detectores OS.pdf"

# Informe Técnico: Rastreo de Sistemas con TTL y Detectores de OS

## 1. Resumen Ejecutivo

Este informe detalla las técnicas para la detección del sistema operativo (OS) de hosts activos en una red. Se centra en el análisis del valor del campo **TTL (Time to Live)** en los paquetes IP como un indicador preliminar del tipo de sistema. El documento profundiza en el uso de dos herramientas clave: **Nmap**, para la detección activa del sistema operativo mediante el envío de paquetes, y **P0f (passive OS fingerprinting)**, una herramienta de análisis puramente pasivo que no interfiere con el host objetivo. A través de un entorno de laboratorio controlado, se demuestra cómo estas herramientas permiten identificar de manera efectiva si un sistema es Linux o Windows, destacando la importancia de estas habilidades para la ciberseguridad.

---

## 2. Conceptos Fundamentales

### 2.1. El Valor del Campo TTL

El **TTL (Time to Live)**, también conocido como "hop limit", es un mecanismo de red que restringe la vida útil de un paquete de datos para evitar que circule indefinidamente en la red. Cada vez que un router procesa un paquete, el valor del TTL se decrementa. Cuando el valor llega a cero, el paquete se descarta y se envía un mensaje de error al remitente.

* **Valores por defecto:** Los diferentes sistemas operativos asignan valores iniciales de TTL por defecto a sus paquetes, lo que permite inferir el tipo de sistema. Por ejemplo:
    * Sistemas **Linux** y **macOS** suelen tener un TTL inicial de **64**.
    * Sistemas **Windows** suelen tener un TTL inicial de **128**.
* **Limitaciones:** El valor del TTL puede ser modificado por los administradores en los sistemas operativos y también puede ser alterado por routers en la ruta de un paquete.
* **Configuración:** Es posible modificar el valor del TTL en diferentes sistemas operativos. Por ejemplo, en Linux se usa el comando `sudo sysctl -w net.ipv4.ip_default_ttl=NEW_TTL_VALUE`, mientras que en Windows se debe modificar el Registro en una ruta específica.

### 2.2. Detección de OS con Nmap

Nmap es una herramienta para la detección activa de sistemas operativos. Su proceso implica:
* **Mecanismo:** Nmap envía una serie de paquetes TCP y UDP al host remoto y analiza la respuesta de cada bit. Las pruebas incluyen muestreo de números de secuencia TCP, soporte y orden de opciones en los encabezados TCP, y verificación del tamaño inicial de la ventana de contexto.
* **Base de datos:** Los resultados se comparan con su base de datos de más de 2,600 perfiles de sistemas operativos conocidos.
* **Resultados:** Si se encuentra una coincidencia, Nmap proporciona detalles como la descripción del SO, el fabricante, la generación, y el tipo de dispositivo.

### 2.3. Detección de OS con P0f

P0f es una herramienta de detección de sistemas completamente pasiva.
* **Mecanismo:** A diferencia de Nmap, P0f no interfiere con el host de destino, ya que solo escucha y analiza el tráfico TCP/IP existente para identificar el sistema detrás de las comunicaciones. Utiliza una variedad de métricas de los encabezados IPv4, IPv6, TCP y del payload a nivel de aplicación para identificar sistemas.
* **Funcionalidades:** P0f puede detectar no solo el sistema operativo, sino también el software de algunas conexiones HTTP, el tiempo que el sistema ha estado encendido, las preferencias de idioma y la distancia entre redes.
* **Análisis offline:** La herramienta es capaz de procesar capturas de Wireshark como entrada para reconocer y analizar conexiones de red.

---

## 3. Procedimientos Prácticos

El siguiente laboratorio se lleva a cabo en un entorno con una máquina Kali Linux (10.0.1.5), una Ubuntu Server (10.0.1.4) y una Windows (10.0.1.7).

### 3.1. Detección de OS con un Simple Ping

1.  **Identificación de hosts:** Primero, se utiliza una herramienta de descubrimiento como `netdiscover` para confirmar que los hosts `10.0.1.4` y `10.0.1.7` están activos en la red.
2.  **Ping a Ubuntu Server:** Se ejecuta el comando `ping 10.0.1.4` desde la máquina Kali.
3.  **Análisis del TTL:** La respuesta del ping muestra un `ttl=64`, lo que indica que la máquina es un sistema operativo Linux, confirmando que `10.0.1.4` es el Ubuntu Server.
4.  **Ping a Windows:** Se ejecuta el comando `ping 10.0.1.7` desde la máquina Kali.
5.  **Análisis del TTL:** La respuesta del ping muestra un `ttl=128`, lo que indica que la máquina es de tipo Windows.

### 3.2. Detección de OS con Nmap

1.  **Escaneo a Ubuntu Server:** Se ejecuta el comando `sudo nmap -O 10.0.1.4` para activar la detección de OS.
    * **Resultado:** El escaneo identifica que el host está "up" y detecta puertos abiertos. En la sección **OS details**, se muestra `Linux 4.15-5.8`, confirmando que el sistema operativo es un kernel de Linux.
2.  **Escaneo a Windows:** Se ejecuta el comando `sudo nmap -O 10.0.1.7`.
    * **Resultado:** Nmap identifica el sistema operativo como `Microsoft Windows 10` y proporciona detalles de la versión. También se listan puertos abiertos específicos de sistemas Windows, como `135/tcp open msrpc` y `445/tcp open microsoft-ds`.

### 3.3. Detección de OS con P0f

1.  **Instalación y Configuración:** En la máquina Kali, se instala P0f con `sudo apt install P0f` y se inicia un servidor web Apache con `sudo systemctl start apache2`.
2.  **Análisis pasivo de Ubuntu Server:**
    * Se inicia P0f en modo de escucha pasiva en la interfaz de red `eth0` con `sudo P0f -i eth0`.
    * Desde la máquina Ubuntu Server, se realiza una solicitud al servidor web de Kali con `wget 10.0.1.5`.
    * **Resultado en P0f:** La herramienta P0f en Kali detecta la conexión y la identifica como proveniente de un sistema **Linux 2.2.x-3.x**, con un idioma genérico y detalles sobre la conexión como el MTU. También detecta que el servicio web al que se accedió es Apache.
3.  **Análisis pasivo de Windows:**
    * Se vuelve a iniciar P0f en Kali.
    * Desde la máquina Windows, se accede al servidor web de Kali (10.0.1.5) a través de un navegador.
    * **Resultado en P0f:** P0f detecta la conexión y, basándose en el **User-Agent** del navegador, identifica que el cliente es un sistema **Windows NT kernel**. También se detectan detalles del navegador (`Mozilla`, `Chrome`), el idioma (`English`) y que el servicio web es Apache.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

El rastreo de sistemas para identificar el OS subyacente es un paso crítico en una auditoría de seguridad. Permite a los profesionales de la seguridad adaptar sus estrategias de ataque o defensa a las características específicas de cada sistema. El análisis del TTL proporciona una pista rápida y sencilla sobre el tipo de OS, mientras que herramientas más sofisticadas como Nmap y P0f ofrecen una precisión mucho mayor. La capacidad de realizar tanto un análisis activo (Nmap) como pasivo (P0f) es fundamental para evadir la detección y obtener inteligencia de manera discreta.

### 4.2. Puntos de Aprendizaje Clave

* **TTL como indicador de OS:** El campo TTL es un valor numérico en los paquetes IP que puede dar una indicación inicial del sistema operativo, con valores comunes de 64 para Linux/macOS y 128 para Windows.
* **Nmap para detección activa:** Nmap es una herramienta poderosa que realiza un escaneo activo, enviando paquetes y comparando respuestas con una extensa base de datos para identificar el sistema operativo con gran detalle y precisión.
* **P0f para detección pasiva:** P0f es una herramienta de análisis pasivo que escucha el tráfico de red sin interferir. Esto es ideal para obtener información de forma sigilosa y puede detectar detalles adicionales como el software de aplicaciones y las preferencias de idioma.
* **Diferenciación de técnicas:** Se ha aprendido a diferenciar entre técnicas de detección activas y pasivas, y a aplicar la herramienta adecuada según el escenario de la auditoría.

### 4.3. Relevancia Técnica

Los procedimientos detallados en este informe son de alta relevancia técnica para cualquier profesional de la ciberseguridad. La capacidad de utilizar tanto un comando simple como `ping` para obtener información inicial, hasta el uso de herramientas especializadas como `Nmap` y `P0f`, es una habilidad indispensable. Combinar la detección activa y pasiva permite obtener una visión completa y robusta de la red, facilitando la toma de decisiones informadas sobre las posibles vulnerabilidades y la estrategia de mitigación.