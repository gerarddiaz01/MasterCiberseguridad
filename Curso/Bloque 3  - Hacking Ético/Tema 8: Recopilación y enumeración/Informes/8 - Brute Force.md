Documentos de Referencia: "RE - Fuerza Bruta.pdf"

# Informe Técnico: Ataques de Fuerza Bruta y Generación de Diccionarios

## 1. Resumen Ejecutivo
Este informe examina en profundidad los **ataques de fuerza bruta**, una técnica de ciberseguridad que involucra el envío de múltiples intentos de contraseñas con la esperanza de encontrar la correcta. Se describen sus objetivos y los límites teóricos que justifican la importancia de contraseñas fuertes. Se detallan los diferentes tipos de ataques de fuerza bruta, como los simples, de diccionario, híbridos, inversos y `credential stuffing`. Se presenta un análisis de herramientas como **Hydra**, **Medusa**, **Crunch** y **Cupp**, demostrando su uso práctico para atacar servicios como **SSH**, **FTP** y formularios web. Finalmente, se discuten las contramedidas esenciales para protegerse de este tipo de ataques.

---

## 2. Conceptos Fundamentales

### 2.1. ¿Qué es la Fuerza Bruta?
La fuerza bruta es una técnica de ataque que consiste en probar numerosas contraseñas o frases de acceso hasta dar con la correcta. Es una forma de conseguir algo "a la fuerza". Los objetivos principales de un ataque de fuerza bruta pueden ser crackear una contraseña, descifrar datos encriptados o conseguir acceso no autorizado a sistemas, redes o servicios. Históricamente, se han construido máquinas especializadas para este fin, como la máquina de descifrado DES de 1998, que constaba de más de 1.800 chips personalizados y era capaz de realizar 90 billones de intentos por segundo.

### 2.2. Límites Teóricos
Los límites teóricos de la fuerza bruta demuestran la importancia de la longitud y complejidad de las contraseñas. Por ejemplo, al construir una contraseña a partir de una combinación de 75 caracteres (54 letras mayúsculas y minúsculas, 10 números del 0 al 9, y 11 símbolos):
* Una contraseña de 10 caracteres tendría 5 sextillones de combinaciones posibles.
* Una contraseña con una longitud variable de 4 a 50 caracteres podría tener hasta 5.73 x $10^{93}$ combinaciones posibles.

A la velocidad de la máquina de descifrado DES (90 billones de intentos por segundo), se tardarían billones de años en romper una contraseña de 4 a 50 caracteres.

### 2.3. Tipos de Ataques de Fuerza Bruta
* **Ataques de fuerza bruta simples:** Se prueban contraseñas sencillas y comunes de forma manual o automatizada. Es fundamental evitar contraseñas débiles, como fechas de cumpleaños, nombres o contraseñas simples, ya que este tipo de ataque existe debido a su uso.
* **Ataques de diccionario:** El atacante utiliza una lista predefinida de posibles contraseñas, conocida como diccionario, para probarlas contra el nombre de usuario de una víctima. Kali Linux incluye diccionarios por defecto con contraseñas comunes como "password", "12345678" y "computer".
* **Ataques de fuerza bruta híbridos:** Este ataque combina la fuerza bruta simple con los ataques de diccionario. Un atacante toma una palabra de un diccionario y le agrega caracteres, letras o números para crear nuevas contraseñas, como se ilustra en la imagen con la palabra "football".
* **Ataques de fuerza bruta inversos:** En este caso, el atacante utiliza una contraseña conocida (obtenida de una brecha de datos) y la prueba contra una lista de millones de nombres de usuario para encontrar una coincidencia. Este método levanta menos sospechas que el ataque convencional, ya que no se realizan múltiples intentos de inicio de sesión contra el mismo usuario repetidamente.
* **Credential stuffing (reutilización de contraseñas):** Esta técnica se aprovecha del hábito de los usuarios de utilizar la misma contraseña en diferentes plataformas. Los atacantes usan combinaciones de usuario y contraseña filtradas para intentar acceder a cuentas en otros servicios.

### 2.4. Ventajas y Desventajas
* **Ventajas:** Estos ataques son muy efectivos contra contraseñas débiles, son fáciles de automatizar con scripts y herramientas, y ofrecen una cobertura total de combinaciones posibles en ataques de fuerza bruta pura.
* **Desventajas:** Consumen mucho tiempo y recursos computacionales, especialmente en contraseñas fuertes, y son muy fácilmente detectables debido a la alta actividad que generan.

### 2.5. Contramedidas
* **Contraseñas fuertes:** Como usuarios, es crucial usar contraseñas robustas, y como administradores, se deben implementar políticas que exijan un mínimo de complejidad y longitud.
* **Limitación de intentos:** Se deben limitar los intentos de inicio de sesión para evitar que un atacante pruebe cientos de contraseñas por segundo.
* **CAPTCHAs:** La implementación de CAPTCHAs puede ayudar a evitar el uso de scripts automatizados.
* **Autenticación de dos factores (2FA):** Siempre que sea posible, se debe habilitar un segundo factor de autenticación, ya que esto puede marcar la diferencia entre que un atacante logre o no entrar en el sistema.
* **Restricciones de acceso por IP:** Los administradores deben restringir IPs anónimas o sospechosas para bloquear comportamientos inapropiados.

---

## 3. Procedimientos Prácticos

### 3.1. Herramientas para Ataques de Fuerza Bruta
Se utilizan dos herramientas principales, **Hydra** y **Medusa**, y se explica cómo generar diccionarios con **Crunch** y **Cupp** en un entorno de laboratorio con Kali Linux (10.0.1.5) y un servidor Ubuntu (10.0.1.4) con servicios SSH y FTP activos.

#### Hydra
* **Descripción:** Hydra es una herramienta de código abierto especializada en ataques de fuerza bruta contra protocolos de autenticación. Fue escrita en C, goza de gran popularidad y cuenta con una interfaz de línea de comandos (CLI) y una interfaz gráfica (GUI). Soporta múltiples protocolos como HTTP, FTP y SSH.
* **Comando para SSH:** `hydra -l <user> -P <list> -V <protocol>://<target>`. Por ejemplo, para el usuario `admin` en el servidor Ubuntu, el comando sería `hydra -l admin -P Desktop/passwords.txt -V ssh://10.0.1.4`.
    * **`-l`**: Define el nombre de usuario (`admin`).
    * **`-P`**: Especifica la lista de contraseñas (`passwords.txt`).
    * **`-V`**: Muestra cada intento de usuario/contraseña.
    * **`ssh://10.0.1.4`**: El protocolo y el objetivo.
* **Comando para FTP:** El mismo formato se utiliza para atacar el servicio FTP, con el protocolo `ftp` y el usuario `admin2`.
* **Resultado:** La herramienta encuentra la contraseña correcta, como "thunder" para el usuario `admin` en SSH y "diamond" para el usuario `admin2` en FTP.

#### Medusa
* **Descripción:** Medusa es otra popular herramienta de fuerza bruta, conocida por su velocidad, paralelización y modularidad. Fue escrita en C y solo cuenta con una interfaz de línea de comandos (CLI). Soporta múltiples protocolos como HTTP, FTP y SSH.
* **Comando para SSH:** `medusa -u admin -P Desktop/passwords.txt -h 10.0.1.4 -M ssh`.
    * **`-u`**: Especifica el nombre de usuario.
    * **`-P`**: Define la lista de contraseñas a usar.
    * **`-h`**: Indica el host objetivo.
    * **`-M`**: Especifica el módulo/protocolo de ataque (`ssh`).
* **Comando para FTP:** `medusa -u admin2 -P Desktop/passwords.txt -M ftp -h 10.0.1.4`.
* **Resultado:** Al igual que Hydra, Medusa identifica la contraseña correcta para los usuarios especificados.

### 3.2. Creación de Diccionarios
Se puede crear un diccionario personalizado para un objetivo específico.

#### Crunch
* **Descripción:** Crunch es una herramienta de línea de comandos para generar listas de palabras basadas en criterios específicos como longitud, conjuntos de caracteres y patrones. Es una herramienta muy popular para crear diccionarios personalizados y dirigidos.
* **Comandos de ejemplo:**
    * `crunch <min> <max> a1b2c3 -o output.txt`: Genera contraseñas con una longitud entre un mínimo y un máximo, usando los caracteres `a`, `1`, `b`, `2`, `c` y `3`, y guarda el resultado en el archivo `output.txt`.
    * `crunch <min> <max> -p hello world`: Combina las palabras "hello" y "world" para crear un diccionario.
    * `crunch <min> <max> -t,@@*`: Utiliza un patrón personalizado donde `,` representa mayúsculas, `@` minúsculas y `*` un símbolo.

#### Cupp
* **Descripción:** Cupp (Common User Passwords Profiler) es un script de Python de código abierto que genera diccionarios de contraseñas basándose en información personal de la víctima. Pregunta información como nombre, fecha de nacimiento, familiares y mascotas.
* **Comando interactivo:** `python3 cupp.py -i`.
    * **Proceso:** La herramienta hace una serie de preguntas y con las respuestas, genera un diccionario único y personalizado.
* **Resultado:** Se crea un archivo de texto con contraseñas que tienen una alta probabilidad de ser usadas por la víctima. Se demostró con el usuario "pepe" y la contraseña "p3p3_1990", la cual fue encontrada por Hydra utilizando el diccionario generado por Cupp.

### 3.3. Ataques de Fuerza Bruta en Formularios Web
Se muestra cómo atacar un formulario de inicio de sesión de una aplicación web vulnerable (DVWA) utilizando Hydra.
* **Proceso:**
    1.  Se instala el servidor web vulnerable DVWA con `docker compose up -d` y se verifica que está activo en el puerto 4280.
    2.  Se utilizan las Herramientas de Desarrollador (DevTools) del navegador para inspeccionar la petición HTTP del formulario de inicio de sesión.
    3.  Se identifica la petición `GET` al path `/vulnerabilities/brute/index.php` con los parámetros `username`, `password` y `Login`.
    4.  Se identifica el mensaje de error (`Username and/or password incorrect`) que indica un fallo de inicio de sesión, lo cual es crucial para la configuración del ataque.
    5.  Se forma el comando Hydra con el protocolo `http-get-form` y se reemplazan los valores de usuario y contraseña con las palabras clave `^USER^` y `^PASS^`. Se añaden los headers de cookie para mantener la sesión y el mensaje de error para detectar los fallos.
* **Resultado:** Hydra prueba las contraseñas del diccionario `rockyou.txt` y encuentra que la contraseña para el usuario `admin` es "password", que es la cuarta contraseña en la lista.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
Comprender los ataques de fuerza bruta es esencial para cualquier profesional de la ciberseguridad. Estos ataques representan una amenaza constante y, a menudo, son exitosos debido a la debilidad de las contraseñas y la falta de medidas de seguridad. Al conocer cómo funcionan, los profesionales pueden implementar contramedidas efectivas y realizar auditorías de contraseñas para fortalecer las defensas de un sistema.

### 4.2. Puntos de Aprendizaje Clave
* **Tipos de Ataques:** Se ha aprendido a diferenciar los distintos tipos de ataques de fuerza bruta, desde los simples y de diccionario hasta los más avanzados como los híbridos y `credential stuffing`.
* **Herramientas de Fuerza Bruta:** Hydra y Medusa son herramientas de código abierto muy potentes y populares para automatizar ataques de fuerza bruta contra diversos servicios de autenticación.
* **Creación de Diccionarios:** Herramientas como Crunch y Cupp permiten crear diccionarios personalizados y muy efectivos, adaptados a la información específica de un objetivo.
* **Ataques a Formularios Web:** Se ha demostrado cómo utilizar Hydra para atacar formularios web, entendiendo la importancia de analizar las peticiones HTTP y el mensaje de error para configurar el ataque correctamente.

### 4.3. Relevancia Técnica
El dominio de las herramientas y técnicas de fuerza bruta es una habilidad técnica fundamental. La capacidad de identificar y explotar vulnerabilidades de autenticación es crucial para las pruebas de penetración. Este conocimiento también es vital para los defensores, ya que les permite comprender las amenazas y aplicar contramedidas proactivas, como la implementación de políticas de contraseñas robustas, el uso de autenticación de dos factores y la monitorización de intentos de inicio de sesión sospechosos.