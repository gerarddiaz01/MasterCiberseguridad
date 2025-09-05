Documentos de Referencia: "AS-I - Post-Explotación_Meterpreter - Metasploit.pdf"

# Informe Técnico: Módulos de Post-Explotación de Metasploit

### 1. Resumen Ejecutivo
Este informe detalla el uso de los módulos de post-explotación de Metasploit en sesiones de Meterpreter para sistemas Windows y Linux. Se explican los procedimientos para descubrir, filtrar y ejecutar estos módulos, los cuales permiten realizar tareas avanzadas como la enumeración de aplicaciones y usuarios, la recolección de credenciales y la detección de vulnerabilidades. Además, se aborda una técnica avanzada de ataque de Man-in-the-Middle (MITM) utilizando un túnel VPN y la herramienta `sslstrip` para interceptar tráfico de red, demostrando el amplio potencial de Metasploit más allá de la explotación inicial.

---

### 2. Conceptos Fundamentales

#### Módulos de Post-Explotación de Metasploit
Los **módulos de post-explotación** son herramientas especializadas dentro de Metasploit Framework, diseñadas para ser ejecutadas después de que se ha establecido una sesión en un sistema comprometido, como una sesión de Meterpreter. Estos módulos han reemplazado a los antiguos "scripts" y se utilizan para una variedad de tareas, incluyendo la recolección de información, la escalada de privilegios y el mantenimiento de la persistencia. Se pueden buscar, filtrar y clasificar por tipo (`type:post`) y por ranking (`s rank`).

#### Ataque de Man-in-the-Middle (MITM) con VPN
Un ataque de **Man-in-the-Middle** es una forma de ciberataque en la que el atacante intercepta la comunicación entre dos partes para escuchar, manipular o robar datos. En el contexto de este informe, se utiliza una VPN para llevar a cabo este ataque, convirtiendo a la máquina Kali en un intermediario. El **Point to Point Tunneling Protocol (PPTP)** se utiliza para crear un servidor de red privada virtual (VPN) que los clientes se conectan, permitiendo que todo su tráfico de red pase a través de la máquina del atacante.

* **`iptables`**: Es una utilidad de línea de comandos en sistemas Linux para configurar las reglas de firewall del kernel. Se utiliza para redirigir y enmascarar el tráfico de red. La regla `MASQUERADE` reemplaza la dirección IP de origen de los paquetes de la víctima por la dirección IP de la máquina Kali antes de enviarlos a una red externa.
* **`sslstrip`**: Esta es una herramienta que fuerza a las víctimas a navegar por sitios web usando **HTTP** en lugar de **HTTPS** al degradar la seguridad de la conexión. Al hacerlo, el atacante puede capturar credenciales y otros datos sensibles que de otro modo estarían cifrados. La herramienta escucha en un puerto específico y redirige el tráfico HTTPS al puerto HTTP.

---

### 3. Procedimientos Prácticos

A continuación se detallan los procedimientos para utilizar los módulos de post-explotación de Metasploit y para realizar un ataque MITM.

#### Uso de Módulos de Post-Explotación en Windows

1.  **Búsqueda de módulos:** Para encontrar módulos de post-explotación, se usa el comando `search type:post` en la consola de Metasploit. Se puede refinar la búsqueda con parámetros adicionales como `s rank` para ordenar por calificación o agregando términos de búsqueda como `checkvm`.
2.  **Ejecución de módulos:** Los módulos se pueden ejecutar de dos maneras:
    * **Desde la sesión de Meterpreter:** Con el comando `run [nombre_del_módulo]`. Esto es más conveniente cuando el módulo no requiere una configuración extensa.
    * **Desde la consola principal de Metasploit:** Se usa el comando `use [nombre_del_módulo]` y se configuran las opciones necesarias, como la sesión, con `set session [id]`.

#### Ejemplos de Módulos de Post-Explotación para Windows

* **`enum_applications`**: Enumera las aplicaciones instaladas en el sistema de la víctima.
    * Comando: `run post/windows/gather/enum_applications`.
    * Resultado: Muestra una lista de aplicaciones y sus versiones, información que podría ser útil para encontrar vulnerabilidades conocidas. Los resultados se guardan en el directorio `loot` de Metasploit.

* **`enum_logged_on_users`**: Recopila información sobre los usuarios que han iniciado sesión actualmente o recientemente.
    * Comando: `run post/windows/gather/enum_logged_on_users`.
    * Resultado: Muestra el SID (Security Identifier) y el nombre de los usuarios conectados, así como su ruta de perfil.

* **`usb_history`**: Obtiene el historial de dispositivos USB conectados al sistema de la víctima.
    * Comando: `run post/windows/gather/usb_history`.
    * Resultado: Muestra una lista de los discos y dispositivos, como unidades de CD-ROM o disquetes, que se han conectado.

* **`local_exploit_suggester`**: Escanea el sistema en busca de posibles vulnerabilidades y sugiere módulos de Metasploit que podrían explotarlas.
    * Comando: `run post/multi/recon/local_exploit_suggester`.
    * Resultado: Tras una revisión de exploits, el módulo identifica los que pueden ser potencialmente explotables en el sistema de la víctima, proporcionando una breve descripción.

* **Módulos de navegador:** Existen módulos para recolectar información de navegadores como Firefox, Chrome y Internet Explorer.
    * Comando: `search type:post s rank firefox` o `search type:post s rank chrome`.
    * Un ejemplo es `enum_ie` para Internet Explorer, que extrae el historial y las cookies de sesión.

#### Uso de Módulos de Post-Explotación en Linux

* **`enum_config`**: Recopila archivos de configuración de servicios comunes como Apache, MySQL y SSH.
    * Comando: `run post/linux/gather/enum_config`.
    * Resultado: Intenta localizar y extraer archivos de configuración de rutas predefinidas y los guarda en el sistema local, donde se pueden examinar en busca de credenciales u otra información sensible.

* **`enum_network`**: Recolecta información de red, incluyendo la tabla de enrutamiento, reglas de firewall (`iptables`), interfaces y conexiones activas.
    * Comando: `run post/linux/gather/enum_network`.
    * Resultado: Guarda los datos en archivos locales para su posterior análisis.

* **`enum_users_history`**: Extrae el historial de comandos ejecutados por los usuarios, como el archivo `bash_history`.
    * Comando: `run post/linux/gather/enum_users_history`.
    * Resultado: Encuentra y descarga historiales de comandos de diferentes usuarios, lo que puede revelar contraseñas o comandos sensibles, como se observa en el historial de MySQL.

* **`ssh_creds`**: Módulo que busca y descarga claves de SSH, tanto públicas como privadas.
    * Comando: `use post/multi/gather/ssh_creds`.
    * Resultado: Descarga archivos como `authorized_keys`, `id_rsa` e `id_dsa`, permitiendo al atacante utilizar esas claves para acceder a otros sistemas en la red, facilitando el pivoteo.

#### Configuración de un Ataque MITM con VPN y Meterpreter

1.  **Instalación y configuración del servidor VPN (Kali Linux):**
    * Instalar el demonio PPTP con `sudo apt install pptpd -y`.
    * Habilitar el reenvío de IP con `echo 1 > /proc/sys/net/ipv4/ip_forward`.
    * Configurar el archivo `/etc/pptpd.conf` para especificar la IP local del servidor y el rango de IPs a asignar a los clientes.
    * Configurar las credenciales de la VPN en `/etc/ppp/chap-secrets` con el formato `usuario servidor contraseña IP`.
    * Reiniciar el servicio con `systemctl restart pptpd` y verificar su estado con `systemctl status pptpd`.

2.  **Configuración de `iptables` (Kali Linux):**
    * Añadir la regla de enmascaramiento: `iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`. Esto asegura que el tráfico de la víctima parezca originarse en el servidor VPN.
    * Permitir el reenvío de tráfico de la VPN a Internet: `iptables -A FORWARD -i ppp0 -o eth0 -j ACCEPT`.
    * Permitir el retorno de tráfico de Internet a la VPN: `iptables -A FORWARD -i eth0 -o ppp0 -m state --state ESTABLISHED,RELATED -j ACCEPT`.

3.  **Ejecución del módulo `pptp_tunnel` (Metasploit):**
    * El módulo `pptp_tunnel` se utiliza para forzar a la máquina de la víctima a conectarse al servidor VPN.
    * El módulo requiere la configuración de parámetros como `PASSWORD`, `USERNAME`, `SESSION` y `VPNHOST`.
    * Comando: `run` después de configurar las opciones.
    * Resultado: El módulo crea una configuración en la máquina víctima para conectarse a la VPN, y la conexión se establece exitosamente.

4.  **Intercepción de tráfico (`Wireshark` y `sslstrip`):**
    * Una vez que la víctima está conectada a la VPN, su tráfico puede ser capturado en la interfaz `ppp0` de Kali con herramientas como Wireshark.
    * Para capturar credenciales, se puede usar `sslstrip` junto con una regla de `iptables` que redirija el tráfico del puerto 80 a un puerto de escucha de `sslstrip`.
    * Regla: `iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-ports 10000`.

---

### 4. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

El dominio de los módulos de post-explotación de Metasploit es fundamental para los profesionales de la seguridad, ya que les permite comprender las técnicas que los atacantes utilizan para profundizar su acceso y recolectar información sensible. La capacidad de automatizar la enumeración de sistemas, usuarios, redes y aplicaciones, así como la extracción de credenciales, demuestra la necesidad de una defensa en capas que no se limite a la prevención, sino que incluya una sólida detección de amenazas internas. El ataque MITM a través de una VPN es un recordatorio crítico de la importancia de la seguridad en el transporte de datos y de la necesidad de educar a los usuarios sobre la seguridad de las redes.

#### Puntos de Aprendizaje Clave

* **Automatización de tareas:** Los módulos de post-explotación de Metasploit permiten automatizar la recolección de inteligencia y la enumeración de sistemas, lo que ahorra tiempo y asegura que no se pasen por alto datos importantes.
* **Recolección de credenciales y datos:** Módulos específicos pueden extraer información valiosa de navegadores, historiales de comandos y claves SSH, lo que a menudo lleva a la escalada de privilegios o a un movimiento lateral en la red.
* **Análisis de vulnerabilidades post-explotación:** Herramientas como `local_exploit_suggester` pueden ayudar a identificar nuevas formas de comprometer un sistema a partir de información recién obtenida.
* **Ataques de red avanzados:** La combinación de Meterpreter con herramientas de red como `iptables`, `pptpd` y `sslstrip` demuestra cómo un atacante puede establecer un control total sobre el tráfico de una víctima, incluso en redes protegidas por firewall.

#### Relevancia Técnica

Los procedimientos detallados en este informe son esenciales para los `pentesters` y auditores de seguridad. El conocimiento práctico de cómo funcionan estos módulos permite a los profesionales simular ataques realistas para identificar y corregir debilidades en los sistemas de sus clientes. Además, comprender el flujo de un ataque MITM con VPN es crucial para configurar defensas de red efectivas, como la inspección profunda de paquetes y la implementación estricta de protocolos de seguridad como HTTPS. La capacidad de detectar y responder a estos ataques es una habilidad invaluable en el campo de la ciberseguridad.