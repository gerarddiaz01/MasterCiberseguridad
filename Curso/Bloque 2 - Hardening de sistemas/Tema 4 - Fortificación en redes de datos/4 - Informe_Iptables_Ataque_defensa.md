# Informe Detallado: Ejercicio de Ataque y Defensa con IPTables

Este informe presenta una resolución detallada del ejercicio de ataque y defensa utilizando el firewall IPTables en un entorno de máquinas virtuales. El objetivo es proporcionar una comprensión práctica de la configuración de reglas de firewall para proteger sistemas contra diversas amenazas, así como explorar conceptos fundamentales de IPTables y su aplicación en un entorno Linux.

## 1. Introducción al Ejercicio

El ejercicio busca que los estudiantes adquieran experiencia práctica en la configuración de reglas de firewall con IPTables para defender una máquina virtual (VM2 Defender) contra una serie de ataques simulados desde otra máquina virtual (VM1 Attacker). Se aprenderá a analizar patrones de ataque, ajustar reglas de firewall para mejorar la seguridad y asegurar la accesibilidad de servicios legítimos.

**Requisitos:**
* Dos máquinas virtuales (VMs) en la misma red: VM1 Attacker y VM2 Defender.
* Herramientas necesarias en la VM atacante: **nmap**, **curl**, **ssh**, y **hydra**.

**Ataques a Realizar:**
* **Escaneo de Puertos:** Utilizar **nmap** para identificar puertos abiertos en la VM defensora.
* **Petición HTTP:** Intentar acceder a un servicio web en la VM defensora usando **curl**.
* **Intento de Conexión SSH:** Intentar establecer una conexión SSH con la VM defensora.
* **Ataque de Fuerza Bruta SSH:** Usar **hydra** para realizar un ataque de fuerza bruta sobre el servicio SSH de la VM defensora.

**Estrategias de Defensa (IPTables):**
* Implementar reglas para detectar y bloquear intentos de escaneo de puertos.
* Bloquear peticiones HTTP no deseadas y limitar el acceso SSH a IPs conocidas.
* Utilizar la limitación de tasa (rate limiting) para defenderse contra ataques de fuerza bruta.
* Registrar (log) los intentos de conexión para un análisis posterior.

## 2. Preparación de las Máquinas Virtuales

Para el ejercicio, se utilizan dos máquinas virtuales en la misma red. La máquina atacante (VM1 Attacker) tiene la IP 10.211.55.5 y la máquina defensora (VM2 Defender) tiene la IP 10.211.55.17.

### 2.1 Preparación de la Máquina Atacante (VM1 Attacker)

Antes de lanzar los ataques, es crucial verificar la conectividad y preparar las herramientas necesarias.

#### 2.1.1 Verificación de Conectividad

Se comprueba la conectividad entre la VM atacante y la defensora mediante un comando `ping`.
* **Comando:** `ping 10.211.55.17`
    * **Sintaxis:** `ping [dirección_IP]`
    * **Elementos:**
        * `ping`: Utilidad de red para probar la accesibilidad de un host en una red IP.
        * `10.211.55.17`: Dirección IP de la máquina defensora.
    * **Propósito:** Confirmar que ambas máquinas están en la misma red y se pueden comunicar.
    * **Resultado Inicial:** La conexión es exitosa, lo que indica que las máquinas están en la misma red y se "ven" entre sí.

#### 2.1.2 Instalación de Herramientas de Ataque

Se instalan las herramientas necesarias en la máquina atacante.
* **Nmap:** Herramienta para exploración de redes y auditorías de seguridad.
    * **Comando:** `sudo apt install nmap`
* **Curl:** Herramienta de línea de comandos para transferir datos con sintaxis URL, útil para probar servicios web.
    * **Comando:** `sudo apt install curl` (No se muestra explícitamente en el texto, pero se infiere por el uso posterior. La transcripción menciona `ssh` como siguiente herramienta, pero `curl` es vital para las pruebas HTTP).
* **SSH (OpenSSH Client):** Cliente para conexiones seguras a través de SSH.
    * **Comando:** `sudo apt install open-ssh-client` (Aunque suele estar preinstalado)
* **Hydra:** Herramienta de ataque de fuerza bruta para probar múltiples servicios de red.
    * **Comando:** `sudo apt install hydra` (o `sudo apt install hydra-gtk` si se desea la interfaz gráfica)
    * **Verificación:** `hydra --help`
    * **Propósito:** Tener las herramientas listas para ejecutar los diferentes tipos de ataques.

### 2.2 Preparación de la Máquina Defensora (VM2 Defender)

En la máquina defensora, es necesario levantar un servicio web para las pruebas y ajustar la configuración SSH para el ataque de fuerza bruta.

#### 2.2.1 Levantamiento de un Servicio Web (Puerto 8000)

Se inicia un servidor HTTP simple para simular un servicio web vulnerable.
* **Comando:** `python3 -m http.server 8000`
    * **Sintaxis:** `python3 -m http.server [puerto]`
    * **Elementos:**
        * `python3 -m http.server`: Módulo de Python que inicia un servidor HTTP simple.
        * `8000`: Puerto en el que el servidor escuchará las peticiones.
    * **Propósito:** Publicar un servicio web en el puerto 8000 que pueda ser atacado y luego defendido.
    * **Resultado Inicial:** El servidor muestra un listado de directorios accesibles a través de `http://0.0.0.0:8000/`.

#### 2.2.2 Deshabilitar Límite de Intentos SSH (Para el Ataque Inicial)

Para demostrar la vulnerabilidad a los ataques de fuerza bruta, se modifica temporalmente la configuración del servidor SSH en la máquina defensora para eliminar cualquier límite de intentos de conexión.
* **Archivo de Configuración:** `/etc/ssh/sshd_config`
* **Modificación:** Se busca la entrada `MaxAuthTries` (o `MaxSessions` en algunas versiones) y se establece a 0, o se comenta para quitar la limitación por defecto.
    * **Propósito:** Permitir intentos ilimitados de conexión SSH, lo que es un escenario inseguro pero necesario para demostrar la efectividad de **hydra** y la posterior defensa con IPTables.
* **Reiniciar Servicio SSH:** Después de modificar el archivo de configuración, es fundamental reiniciar el servicio SSH para que los cambios surtan efecto.
    * **Comando:** `sudo systemctl restart ssh`

## 3. Realización de Ataques (Sin Defensa)

Una vez preparadas ambas máquinas, se procede a ejecutar la secuencia de ataques para observar su éxito antes de implementar las defensas.

### 3.1 Escaneo de Puertos con Nmap

* **Comando:** `nmap -p- 10.211.55.17`
    * **Sintaxis:** `nmap [opciones] [dirección_IP]`
    * **Elementos:**
        * `nmap`: Herramienta de escaneo de puertos.
        * `-p-`: Opción para escanear todos los puertos (del 1 al 65535).
        * `10.211.55.17`: Dirección IP de la VM defensora.
    * **Propósito:** Identificar los puertos abiertos en la máquina defensora.
    * **Resultado Inicial:** **nmap** reporta que el puerto 8000 está abierto y el servicio `http-alt` está ejecutándose. Esto expone información valiosa al atacante.

### 3.2 Petición HTTP con Curl

* **Comando:** `curl http://10.211.55.17:8000`
    * **Sintaxis:** `curl [URL]`
    * **Elementos:**
        * `curl`: Herramienta para transferir datos desde o hacia un servidor.
        * `http://10.211.55.17:8000`: URL del servicio web en la máquina defensora.
    * **Propósito:** Intentar acceder al contenido del servicio web descubierto.
    * **Resultado Inicial:** **curl** devuelve el listado de directorios del servidor web, confirmando el acceso sin restricciones al servicio HTTP.

### 3.3 Intento de Conexión SSH

Se simula un intento de conexión SSH, asumiendo que el atacante conoce un usuario válido (por ejemplo, `user`) a través de técnicas de OSINT.
* **Comando:** `ssh user@10.211.55.17`
    * **Sintaxis:** `ssh [usuario]@[dirección_IP]`
    * **Elementos:**
        * `ssh`: Cliente para conexiones SSH.
        * `user`: Nombre de usuario en la máquina defensora.
        * `10.211.55.17`: Dirección IP de la VM defensora.
    * **Propósito:** Verificar si el servicio SSH está operativo y accesible.
    * **Resultado Inicial:** El servidor SSH responde, indicando que el servicio está operativo y que se puede intentar una conexión.

### 3.4 Ataque de Fuerza Bruta SSH con Hydra

Se lanza un ataque de fuerza bruta contra el servicio SSH, aprovechando que el límite de intentos ha sido deshabilitado. Se utiliza un archivo de contraseñas (`password.txt`) con 50 entradas.
* **Comando:** `hydra -l user -P password.txt ssh://10.211.55.17`
    * **Sintaxis:** `hydra -l [usuario] -P [archivo_contraseñas] [servicio]://[dirección_IP]`
    * **Elementos:**
        * `hydra`: Herramienta para ataques de fuerza bruta.
        * `-l user`: Especifica el nombre de usuario (`user`) a probar.
        * `-P password.txt`: Especifica la ruta al archivo que contiene la lista de contraseñas a intentar.
        * `ssh://10.211.55.17`: Indica el protocolo (SSH) y la dirección IP del servidor objetivo.
    * **Propósito:** Demostrar cómo se puede descubrir una contraseña si no hay limitación en los intentos de conexión.
    * **Resultado Inicial:** **hydra** logra encontrar una contraseña (`batman123`) dentro del archivo `password.txt` y accede al servidor SSH. Esto confirma que, sin defensas adecuadas, el sistema es vulnerable a este tipo de ataques.

En resumen, los cuatro ataques iniciales han tenido éxito, obteniendo información del servidor, accediendo al servicio web y logrando una conexión SSH, e incluso comprometiendo una contraseña. Esto subraya la necesidad de implementar defensas robustas.

## 4. Configuración de IPTables (Defensa)

Ahora, se procede a configurar las reglas de IPTables en la máquina defensora (VM2 Defender) para mitigar los ataques probados anteriormente. La configuración se realiza de forma jerárquica para asegurar un comportamiento de firewall predecible y seguro.

### 4.1 Establecimiento de Políticas por Defecto

Es una práctica fundamental establecer las políticas por defecto de las cadenas INPUT, OUTPUT y FORWARD antes de añadir reglas específicas. Esto asegura que el comportamiento general del sistema sea el deseado, bloqueando o permitiendo tráfico por defecto.

#### 4.1.1 Política por Defecto de la Cadena INPUT

* **Comando:** `sudo iptables -P INPUT DROP`
    * **Sintaxis:** `iptables -P [cadena] [política]`
    * **Elementos:**
        * `iptables`: Utilidad para configurar las tablas de reglas del firewall de Linux.
        * `-P`: Establece la política por defecto (Default Policy) para una cadena.
        * `INPUT`: Cadena que controla los paquetes entrantes al sistema.
        * `DROP`: Política que descarta silenciosamente los paquetes que no coinciden con ninguna regla específica en la cadena.
    * **Propósito:** Bloquear por defecto todo el tráfico entrante que no sea explícitamente permitido por otras reglas. Esto es crucial para un modelo de "denegar por defecto, permitir explícitamente".

#### 4.1.2 Política por Defecto de la Cadena OUTPUT

* **Comando:** `sudo iptables -P OUTPUT ACCEPT`
    * **Sintaxis:** `iptables -P [cadena] [política]`
    * **Elementos:**
        * `OUTPUT`: Cadena que controla los paquetes salientes del sistema.
        * `ACCEPT`: Política que permite por defecto todos los paquetes salientes.
    * **Propósito:** Permitir que el servidor inicie conexiones hacia afuera sin restricciones, a menos que haya una regla explícita que las bloquee. Esto es común en servidores que necesitan acceder a actualizaciones o servicios externos.

#### 4.1.3 Consideración de la Cadena FORWARD

* **Comentario:** No se aplica una política `DROP` a la cadena `FORWARD` en este ejercicio (`sudo iptables -P FORWARD DROP`) porque la máquina defensora no actúa como un router ni reenvía paquetes entre diferentes redes.
    * **Propósito:** Simplificar la configuración, ya que esta regla no es necesaria para el escenario planteado. En un router, sería una política por defecto recomendada.

### 4.2 Permitir Tráfico Local (Loopback)

Es vital permitir el tráfico en la interfaz de loopback (`lo`) para que los procesos internos del sistema puedan comunicarse entre sí.
* **Comando INPUT:** `sudo iptables -A INPUT -i lo -j ACCEPT`
    * **Sintaxis:** `iptables -A [cadena] -i [interfaz] -j [acción]`
    * **Elementos:**
        * `-A INPUT`: Añade la regla al final de la cadena INPUT.
        * `-i lo`: Coincide con paquetes que provienen de la interfaz de loopback.
        * `-j ACCEPT`: Permite el tráfico.
* **Comando OUTPUT:** `sudo iptables -A OUTPUT -o lo -j ACCEPT`
    * **Sintaxis:** `iptables -A [cadena] -o [interfaz] -j [acción]`
    * **Elementos:**
        * `-A OUTPUT`: Añade la regla al final de la cadena OUTPUT.
        * `-o lo`: Coincide con paquetes que van a la interfaz de loopback.
        * `-j ACCEPT`: Permite el tráfico.
    * **Propósito:** Asegurar que las aplicaciones y servicios locales puedan comunicarse internamente sin ser bloqueados por el firewall.

### 4.3 Permitir Conexiones Establecidas y Relacionadas

Esta regla es fundamental para permitir las respuestas a conexiones que han sido iniciadas por el propio host. Sin ella, las conexiones salientes no recibirían sus respuestas, rompiendo la funcionalidad normal del sistema.
* **Comando:** `sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`
    * **Sintaxis:** `iptables -A [cadena] -m [módulo] --ctstate [estados] -j [acción]`
    * **Elementos:**
        * `-A INPUT`: Añade la regla a la cadena INPUT.
        * `-m conntrack`: Utiliza el módulo `conntrack` para realizar coincidencias basadas en el estado de la conexión.
        * `--ctstate ESTABLISHED,RELATED`: Coincide con paquetes que son parte de una conexión ya establecida (`ESTABLISHED`) o que están relacionados con una conexión existente (como FTP pasivo, que abre nuevos puertos, `RELATED`).
        * `-j ACCEPT`: Permite el tráfico.
    * **Propósito:** Asegurar que el tráfico de respuesta legítimo sea permitido, evitando que el firewall bloquee el flujo normal de datos para conexiones ya iniciadas por el sistema.

### 4.4 Defensas Específicas contra Ataques

Una vez establecidas las políticas básicas, se implementan reglas más específicas para contrarrestar cada tipo de ataque.

#### 4.4.1 Bloqueo de Escaneo de Puertos (Nmap)

El objetivo es ralentizar o bloquear la capacidad de herramientas como **nmap** para identificar puertos abiertos, especialmente detectando el patrón de paquetes `RST` que a menudo se generan durante los escaneos de puertos a puertos cerrados.

* **Regla 1: Limitar la tasa de paquetes RST**
    * **Comando:** `sudo iptables -A INPUT -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --tcp-flags [flags_mask] [flags_set] -m limit --limit [tasa] -j [acción]`
        * **Elementos:**
            * `-p tcp`: La regla se aplica a paquetes TCP.
            * `--tcp-flags SYN,ACK,FIN,RST RST`: Especifica que la regla busca paquetes TCP que tengan el flag `RST` (reset) establecido, ignorando los demás flags (`SYN`, `ACK`, `FIN`) en la máscara. Los paquetes `RST` son generados cuando se recibe una solicitud de conexión en un puerto donde no hay un servicio escuchando.
            * `-m limit --limit 1/s`: Utiliza el módulo `limit` para establecer una tasa máxima de un paquete por segundo que coincida con esta regla. Esto ralentiza el escaneo.
            * `-j ACCEPT`: Acepta los paquetes que cumplen con esta limitación.
        * **Propósito:** Ralentizar significativamente la capacidad de un atacante para determinar qué puertos están abiertos, ya que las respuestas `RST` a puertos cerrados estarán limitadas.

* **Regla 2: Descartar paquetes TCP con flag RST (patrón de escaneo)**
    * **Comando:** `sudo iptables -A INPUT -p tcp --tcp-flags SYN,ACK,FIN,RST RST -j DROP`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --tcp-flags [flags_mask] [flags_set] -j [acción]`
        * **Elementos:**
            * `-p tcp`: La regla se aplica a paquetes TCP.
            * `--tcp-flags SYN,ACK,FIN,RST RST`: Coincide con paquetes TCP que tienen el flag `RST` establecido.
            * `-j DROP`: Descarta silenciosamente los paquetes que coinciden con el patrón.
        * **Propósito:** Bloquear directamente los paquetes `RST` que son típicos de los escaneos de puertos, dificultando que el atacante reciba la información sobre puertos cerrados.

#### 4.4.2 Bloqueo de Peticiones HTTP/HTTPS (Curl)

Se bloquea el acceso a los puertos web, en este caso, el puerto 8000 donde se encuentra el servidor HTTP. También se incluyen los puertos 80 y 443 como medida adicional.
* **Bloqueo de puerto 8000 (servicio web publicado):**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 8000 -j DROP`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --dport [puerto] -j [acción]`
        * **Elementos:**
            * `-p tcp`: Protocolo TCP.
            * `--dport 8000`: Puerto de destino 8000.
            * `-j DROP`: Descarta los paquetes.
        * **Propósito:** Bloquear completamente el acceso al servicio web en el puerto 8000.
* **Bloqueo de puerto 80 (HTTP estándar):**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 80 -j DROP`
        * **Propósito:** Bloquear el acceso al puerto HTTP estándar.
* **Bloqueo de puerto 443 (HTTPS estándar):**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 443 -j DROP`
        * **Propósito:** Bloquear el acceso al puerto HTTPS estándar, como medida adicional.

#### 4.4.3 Control de Conexiones SSH

Se establecen reglas para limitar y controlar el acceso SSH, permitiendo solo conexiones desde IPs de confianza y aplicando limitación de tasa para prevenir ataques de fuerza bruta.

* **Permitir SSH solo desde IPs de Confianza:**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 22 -s 10.211.55.10 -j ACCEPT`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --dport [puerto] -s [IP_origen] -j [acción]`
        * **Elementos:**
            * `-p tcp`: Protocolo TCP.
            * `--dport 22`: Puerto de destino 22 (SSH).
            * `-s 10.211.55.10`: Especifica la dirección IP de origen permitida. En este caso, se usa una IP ficticia (`10.211.55.10`) para ilustrar cómo se restringiría el acceso a la IP del atacante (`10.211.55.5`).
            * `-j ACCEPT`: Acepta la conexión.
        * **Propósito:** Restringir el acceso SSH únicamente a las direcciones IP que se consideran seguras, bloqueando el resto por la política por defecto `DROP` de la cadena `INPUT`.

* **Limitar Intentos de Conexión SSH (Protección contra Fuerza Bruta):**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m limit --limit 1/minute --limit-burst 3 -j ACCEPT`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --dport [puerto] -m [módulo] --ctstate [estado] -m limit --limit [tasa] --limit-burst [ráfaga] -j [acción]`
        * **Elementos:**
            * `-p tcp --dport 22`: Aplica la regla a paquetes TCP dirigidos al puerto 22.
            * `-m conntrack --ctstate NEW`: Utiliza el módulo `conntrack` para coincidir solo con **nuevas** conexiones (`NEW`) al puerto 22. Esto evita afectar conexiones SSH ya establecidas.
            * `-m limit --limit 1/minute --limit-burst 3`: Utiliza el módulo `limit` para permitir un máximo de un nuevo intento de conexión SSH por minuto, con una "ráfaga" (burst) inicial de hasta tres paquetes.
            * `-j ACCEPT`: Acepta estos paquetes limitados.
        * **Propósito:** Proteger contra ataques de Denegación de Servicio (DoS) y fuerza bruta al limitar drásticamente la cantidad de nuevas conexiones SSH que se pueden establecer por minuto, dificultando a **hydra** probar múltiples contraseñas.

* **Descartar el resto de intentos SSH no permitidos:**
    * **Comando:** `sudo iptables -A INPUT -p tcp --dport 22 -j DROP`
        * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --dport [puerto] -j [acción]`
        * **Elementos:**
            * `-p tcp --dport 22`: Aplica la regla a paquetes TCP dirigidos al puerto 22.
            * `-j DROP`: Descarta los paquetes.
        * **Propósito:** Asegurar que cualquier intento de conexión SSH que no haya sido permitido por las reglas anteriores (por ejemplo, por no provenir de una IP confiable o por exceder el límite de tasa) sea descartado.

#### 4.4.4 Registro de Intentos de Conexión SSH (para Análisis)

Aunque no es una regla de bloqueo, el registro es crucial para la seguridad, permitiendo auditar y analizar intentos de acceso, especialmente los sospechosos.
* **Comando:** `sudo iptables -A INPUT -p tcp --dport 22 -j LOG --log-prefix "SSH attempt: "`
    * **Sintaxis:** `iptables -A [cadena] -p [protocolo] --dport [puerto] -j LOG --log-prefix "[prefijo_log]"`
    * **Elementos:**
        * `-A INPUT`: Añade la regla a la cadena INPUT.
        * `-p tcp --dport 22`: Coincide con paquetes TCP destinados al puerto 22.
        * `-j LOG`: La acción es registrar el paquete en los logs del sistema (generalmente `syslog`).
        * `--log-prefix "SSH attempt: "`: Añade un prefijo legible a la entrada del log para facilitar la identificación de los mensajes relacionados con SSH.
    * **Propósito:** Almacenar información sobre los intentos de conexión SSH para su posterior análisis, lo que es vital para la monitorización de seguridad.

### 4.5 Guardar las Reglas de IPTables

Después de configurar todas las reglas, es esencial guardarlas para que persistan después de un reinicio del sistema.
* **Comando:** `sudo iptables-save > /etc/iptables/rules.v4` (El ejercicio menciona `/etc/iptables/rules` pero la convención en sistemas modernos Debian/Ubuntu es `rules.v4`)
    * **Sintaxis:** `iptables-save > [ruta_archivo]`
    * **Elementos:**
        * `iptables-save`: Comando que imprime las reglas de IPTables cargadas actualmente.
        * `>`: Redirige la salida estándar a un archivo.
        * `/etc/iptables/rules.v4`: Ruta y nombre del archivo donde se guardarán las reglas. Es importante asegurar que el directorio `/etc/iptables/` exista; si no, debe crearse.
    * **Propósito:** Persistir las reglas del firewall para que se carguen automáticamente al inicio del sistema, evitando tener que configurarlas manualmente después de cada reinicio.

## 5. Pruebas de Ataque Post-Defensa

Una vez que las reglas de IPTables han sido implementadas y guardadas en la máquina defensora, se repiten los ataques desde la máquina atacante para verificar la efectividad de las defensas.

### 5.1 Ping

* **Comando:** `ping 10.211.55.17`
* **Resultado:** El `ping` no funciona.
    * **Explicación:** La política por defecto `INPUT DROP` de IPTables bloquea el tráfico ICMP (utilizado por `ping`) a menos que se permita explícitamente. Como no se añadió una regla para permitir ICMP, el `ping` es bloqueado, ocultando la presencia de la máquina.

### 5.2 Escaneo de Puertos con Nmap

* **Comando:** `nmap -p- 10.211.55.17`
* **Resultado:** **nmap** ya no reporta el puerto 8000 como abierto; de hecho, puede indicar que el host está "down" o que se están bloqueando las sondas.
    * **Explicación:** Las reglas de IPTables para detectar y descartar paquetes con el flag `RST` y para limitar la tasa de respuesta a escaneos han funcionado, ocultando los puertos abiertos y ralentizando la capacidad de **nmap** para recopilar información.

### 5.3 Petición HTTP con Curl

* **Comando:** `curl http://10.211.55.17:8000`
* **Resultado:** La petición se queda "pensando" y no devuelve ningún paquete ni información.
    * **Explicación:** La regla `iptables -A INPUT -p tcp --dport 8000 -j DROP` ha bloqueado eficazmente el tráfico HTTP dirigido al puerto 8000, impidiendo el acceso al servicio web.

### 5.4 Intento de Conexión SSH

* **Comando:** `ssh user@10.211.55.17`
* **Resultado:** La conexión es directamente "rechazada" (`Connection refused`).
    * **Explicación:** La regla que permite SSH solo desde IPs de confianza (en este caso, una IP ficticia `10.211.55.10`) y la política por defecto `DROP` para el resto han impedido que la VM atacante establezca una conexión SSH, ya que su IP no está en la lista de permitidas.

### 5.5 Ataque de Fuerza Bruta SSH con Hydra

#### 5.5.1 Prueba Inicial de Hydra (con la IP del atacante aún bloqueada)

* **Comando:** `hydra -l user -P password.txt ssh://10.211.55.17`
* **Resultado:** **hydra** no logra realizar ningún intento y se detiene, indicando que no puede conectarse.
    * **Explicación:** Al igual que en el intento de conexión SSH simple, las reglas de IPTables impiden que la conexión inicial se establezca, haciendo que **hydra** sea ineficaz.

#### 5.5.2 Habilitar Temporalmente la IP del Atacante para SSH (Demostración de Rate Limiting)

Para demostrar la efectividad de la limitación de tasa contra **hydra** incluso si el atacante logra evadir la restricción por IP, se habilita temporalmente la IP de la máquina atacante en la regla SSH.
* **Comando en la VM defensora:** `sudo iptables -A INPUT -p tcp --dport 22 -s 10.211.55.5 -j ACCEPT`
    * **Elementos:**
        * `-s 10.211.55.5`: Ahora se especifica la dirección IP de la máquina atacante para permitirle el acceso.
    * **Propósito:** Permitir que la IP del atacante (`10.211.55.5`) se conecte vía SSH, permitiendo así que las reglas de limitación de tasa de IPTables se activen y demuestren su función.

#### 5.5.3 Prueba de Hydra con IP del Atacante Habilitada

* **Comando:** `hydra -l user -P password.txt ssh://10.211.55.17`
* **Resultado:** **hydra** comienza el ataque, pero termina sin éxito, indicando que no puede continuar con las pruebas o que no logra reconectar.
    * **Explicación:** La regla `iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m limit --limit 1/minute --limit-burst 3 -j ACCEPT` entra en juego. Aunque la IP del atacante está permitida, la limitación de un nuevo intento de conexión por minuto con una ráfaga de 3 impide que **hydra** realice suficientes intentos de forma rápida para probar todas las contraseñas. El ataque de fuerza bruta es ineficaz debido a la limitación de tasa.

En resumen, todas las defensas implementadas han funcionado correctamente, bloqueando los diferentes tipos de ataques y demostrando la versatilidad de IPTables para proteger un sistema.

## 6. Conceptos Aprendidos en el Contexto de IPTables y Linux

A través de este ejercicio, se han consolidado varios conceptos fundamentales relacionados con IPTables y la seguridad en Linux:

### 6.1 Creación, Eliminación y Movimiento de Reglas

* **Creación (`-A` / `--append`):** Las reglas se añaden al final de una cadena utilizando la opción `-A`. Por ejemplo, `iptables -A INPUT ...`.
* **Eliminación (`-D` / `--delete`):** Las reglas pueden eliminarse especificando su número de línea o su sintaxis exacta.
* **Inserción (`-I` / `--insert`):** Permite añadir una regla en una posición específica de la cadena, lo cual es crucial para la jerarquía.
* **Reemplazo (`-R` / `--replace`):** Permite modificar una regla existente por su número de línea.
* **Limpieza (`-F` / `--flush`):** Elimina todas las reglas de una cadena o de todas las cadenas si no se especifica ninguna.
* **Eliminación de Cadenas (`-X` / `--delete-chain`):** Elimina una cadena personalizada (no se aplica a las cadenas predefinidas como INPUT, OUTPUT, FORWARD).

### 6.2 Funcionamiento de la Jerarquía de Reglas

IPTables procesa las reglas de una cadena secuencialmente, desde la primera hasta la última. La primera regla que coincide con un paquete determina la acción (ACCEPT, DROP, REJECT, LOG, etc.).
* **Orden Lógico:** Las reglas más específicas deben colocarse antes que las más generales. Por ejemplo, una regla para permitir una IP específica al puerto SSH debe ir antes de una regla para bloquear todo el tráfico al puerto SSH.
* **Políticas por Defecto:** Las políticas por defecto (`-P`) actúan como una regla "catch-all" al final de la cadena. Si ningún paquete coincide con ninguna regla explícita en la cadena, se aplica la política por defecto. Esto es fundamental para implementar un modelo de "denegar por defecto".

### 6.3 Compartición de Conexión a Internet entre Máquinas (NAT / FORWARD)

Aunque no se implementó directamente en este ejercicio (ya que las VMs estaban en la misma red), la compartición de conexión a internet (Network Address Translation - NAT) y el reenvío de paquetes se gestionan con IPTables:
* **Cadena `FORWARD`:** Es la cadena principal para controlar el tráfico que pasa a través de la máquina (cuando actúa como router).
* **Tabla `nat`:** Utilizada para reescribir las direcciones IP y puertos de los paquetes (ej., `POSTROUTING` para SNAT y `PREROUTING` para DNAT).
* **Comando Ejemplo (NAT):** `sudo iptables -t nat -A POSTROUTING -o [interfaz_salida] -j MASQUERADE`

### 6.4 Bloqueo de Ping y ICMP entre Máquinas

Como se demostró en el ejercicio, bloquear `ping` (que utiliza ICMP) se logra al establecer la política por defecto de `INPUT` a `DROP` y no añadir ninguna regla explícita para permitir el tráfico ICMP.
* **Concepto:** El protocolo ICMP (Internet Control Message Protocol) es utilizado para mensajes de error y operaciones, como `ping`. Al no permitir el ICMP entrante, la máquina defensora se vuelve "invisible" a los escaneos básicos de presencia.

### 6.5 Redirección de Tráfico de un Puerto a Otro (DNAT)

Aunque no se realizó en el ejercicio, IPTables permite redirigir el tráfico de un puerto a otro, o de una IP a otra (port forwarding). Esto se logra en la tabla `nat` y la cadena `PREROUTING`.
* **Comando Ejemplo:** `sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:8080`
    * **Propósito:** Redirigir el tráfico entrante al puerto 80 a un servidor interno en la IP 192.168.1.100 en el puerto 8080.

### 6.6 Creación de una DMZ con sus Respectivas Reglas

La DMZ (Demilitarized Zone) es una subred que expone servicios orientados a Internet a una red más grande y no confiable, mientras protege la red interna (LAN). IPTables es fundamental para implementar las reglas de firewall que definen una DMZ:
* **Reglas Clave:**
    * Permitir el tráfico de Internet a la DMZ solo a puertos específicos de los servicios públicos (HTTP, HTTPS, DNS, etc.).
    * Restringir el tráfico de la DMZ a la red interna (LAN), permitiendo solo el tráfico necesario para el funcionamiento de los servicios.
    * Permitir el tráfico de la LAN a la DMZ (para administración).
    * Bloquear el tráfico directo de Internet a la LAN.
* **Implementación:** Implicaría el uso de múltiples interfaces de red y un conjunto complejo de reglas en las cadenas `INPUT`, `OUTPUT` y `FORWARD`, así como en la tabla `nat` si se requiere traducción de direcciones.

## 7. Conclusiones

Este ejercicio proporciona una comprensión práctica y profunda de la configuración de reglas de firewall con IPTables en un entorno Linux. Se ha demostrado cómo aplicar diferentes técnicas de defensa para mitigar ataques comunes, desde el escaneo de puertos hasta los ataques de fuerza bruta. La experiencia práctica con IPTables es esencial para cualquier profesional de la ciberseguridad, ya que esta herramienta es omnipresente en los sistemas Linux y constituye una primera capa de protección fundamental en entornos cada vez más complejos y peligrosos.

La resolución de este tipo de ejercicios mejora la comprensión del funcionamiento de un firewall, la importancia de la jerarquía de reglas y la versatilidad de IPTables para proteger activos digitales.