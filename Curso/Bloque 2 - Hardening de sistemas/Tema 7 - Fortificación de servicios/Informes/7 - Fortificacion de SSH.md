Documentos de Referencia: "FS - Fortificación del servicio SSH.pdf"

# Informe Técnico: Fortificación del Servicio SSH en GNU/Linux

### 1\. Resumen Ejecutivo

Este informe técnico detalla el protocolo **Secure Shell (SSH)**, su funcionamiento y la importancia de su correcta fortificación en entornos de servidores GNU/Linux. Se explican los conceptos clave de SSH, sus características de seguridad y las mejores prácticas para su configuración. Se abordan procedimientos prácticos en un entorno de laboratorio virtual, incluyendo la instalación, la realización de una conexión básica y la simulación de un ataque de fuerza bruta para demostrar la importancia de las medidas de seguridad. El informe profundiza en la configuración segura del servicio SSH, el uso de diferentes mecanismos de autenticación (como contraseñas y claves públicas), y la integración de herramientas adicionales como **Fail2ban** y **Multi-Factor Authentication (MFA)** para reforzar la seguridad. Además, se exploran otros casos de uso de SSH, como la transferencia segura de archivos mediante **SCP** y **SFTP**, y la creación de túneles SSH para asegurar protocolos de red inseguros.

-----

### 2\. Conceptos Fundamentales

  * **SSH (Secure Shell):** Es un protocolo de red utilizado para acceder de forma segura a sistemas remotos a través de una conexión encriptada. Se basa en el intercambio de claves del algoritmo criptográfico Diffie-Hellman para establecer un canal seguro, lo que lo hace una alternativa mucho más segura a protocolos obsoletos como Telnet o rlogin. Consta de dos componentes principales: el cliente SSH, que inicia la conexión, y el servidor SSH, que la acepta.

      * **Usos principales:**
          * Tareas de administración y mantenimiento en sistemas remotos.
          * Transferencia segura de archivos con utilidades como **SCP** (Secure Copy Protocol) y **SFTP** (SSH File Transfer Protocol).
          * Creación de túneles para asegurar otros protocolos (HTTP, FTP, VNC).
          * Autenticación segura mediante claves RSA.

  * **Características de seguridad de SSH:**

      * **Confidencialidad:** Cifra los datos en tránsito, garantizando que solo el cliente y el servidor puedan acceder a ellos.
      * **Autenticación segura:** Utiliza pares de claves públicas y privadas para verificar la identidad de los usuarios y evitar accesos no autorizados.
      * **Integridad:** Detecta cualquier manipulación de los datos en tránsito utilizando algoritmos hash, como SHA2.
      * **Reenvío de puertos:** Permite el reenvío seguro de puertos a través de TCP/IP, facilitando el acceso remoto.

  * **Importancia de la fortificación de SSH:** Una configuración incorrecta de SSH puede comprometer gravemente la seguridad de un sistema, exponiéndolo a robos de información, ataques de fuerza bruta y denegación de servicio. La fortificación adecuada es esencial para proteger el acceso al sistema, asegurar la integridad y confidencialidad de los datos, y garantizar el cumplimiento de normativas de seguridad como GDPR o PCI.

  * **Mecanismos de Autenticación en SSH:**

      * **Contraseña:** Es el método más común, pero también el más vulnerable a ataques de fuerza bruta y de diccionario. Su seguridad depende de la complejidad de la contraseña.
      * **Clave Pública/Privada:** Un método de autenticación más seguro. El cliente genera un par de claves (pública y privada); la clave pública se almacena en el servidor y la clave privada se utiliza para autenticarse. Este método es menos susceptible a ataques de fuerza bruta y robo de credenciales.
      * **Multi-Factor Authentication (MFA):** Un método de seguridad que requiere más de una forma de autenticación, como una contraseña y un código de un token físico o una aplicación de teléfono móvil. Mitiga riesgos asociados con el robo de contraseñas y la suplantación de identidad.

  * **Funcionamiento Básico de SSH:** El proceso de conexión SSH sigue una serie de pasos:

    1.  **Three-way handshake:** Se establece la conexión TCP/IP.
    2.  **Versions:** Se validan las versiones del protocolo y se negocian los algoritmos de cifrado.
    3.  **Host Key Exchange:** El servidor envía su clave pública de host al cliente.
    4.  **Key validation:** El cliente valida la clave pública del servidor.
    5.  **Encrypted tunnel:** Se crea un túnel encriptado para el resto de la sesión.
    6.  **Authentication:** El usuario se autentica con contraseña o claves.
    7.  **Remote command execution:** El cliente puede ejecutar comandos en el servidor.
    8.  **Sign Out:** El cliente cierra la conexión.

  * **Ficheros de Configuración de SSH:** La configuración del servicio SSH se realiza en los siguientes archivos, ubicados en el directorio `/etc/ssh`:

      * `sshd_config`: Archivo de configuración del servidor SSH.
      * `ssh_config`: Archivo de configuración del cliente SSH.
      * Otros archivos importantes incluyen los que contienen las claves públicas y privadas del host (ej. `ssh_host_rsa_key` y `ssh_host_rsa_key.pub`).

-----

### 3\. Procedimientos Prácticos

A continuación, se describen los procedimientos prácticos realizados en un entorno de laboratorio con una máquina cliente **Kali Linux** y una máquina servidora **Ubuntu**.

#### 3.1. Instalación y Primera Conexión

1.  **Instalación del servidor SSH:**

      * **Comando:** `sudo apt-get install openssh-server`.
      * **Explicación:** Este comando instala el servidor OpenSSH en el sistema Ubuntu, lo que permite aceptar conexiones SSH entrantes. Una vez finalizada la instalación, se puede verificar la versión instalada con `ssh -V`.

2.  **Realizar la primera conexión:**

      * **Comando:** `ssh testssh@10.0.2.15`.
      * **Explicación:** Desde la máquina Kali Linux, se utiliza el comando `ssh` con el usuario `testssh` y la dirección IP del servidor Ubuntu (`10.0.2.15`). Al ser la configuración por defecto, el sistema solicita la contraseña del usuario para la autenticación. Si la contraseña es correcta, se establece una sesión remota.

#### 3.2. Simulación de un Ataque de Fuerza Bruta y su Mitigación con `iptables`

1.  **Simular el ataque con Hydra:**

      * **Comando:** `hydra -l testssh -P /usr/share/wfuzz/wordlist/others/common_pass.txt 10.0.2.15 ssh -t 4 -v`.
      * **Explicación:** Se utiliza la herramienta preinstalada en Kali Linux, **Hydra**, para realizar un ataque de fuerza bruta.
          * El parámetro `-l` especifica el usuario (`testssh`).
          * `-P` indica el archivo de contraseñas a probar.
          * `10.0.2.15` es la dirección IP del objetivo.
          * `ssh` especifica el protocolo a atacar.
          * `-t 4` lanza 4 hilos de ejecución concurrentes.
          * `-v` activa el modo verboso para ver la información.
      * **Resultado:** El ataque tiene éxito y Hydra encuentra la contraseña, demostrando la vulnerabilidad de la configuración por defecto.

2.  **Mitigar el ataque con `iptables`:**

      * **Comandos:**
          * `sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --set`
          * `sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 4 -j DROP`
      * **Explicación:** Se añaden dos reglas al firewall de Ubuntu (`iptables`) para bloquear intentos de conexión fallidos. La primera regla registra las nuevas conexiones TCP al puerto 22. La segunda regla, `DROP`, bloquea (`DROP`) cualquier conexión desde una IP que haya fallado la autenticación 4 veces (`--hitcount 4`) en 60 segundos (`--seconds 60`).

3.  **Verificación de la mitigación:**

      * Se repite el comando de Hydra. La máquina atacante no podrá encontrar la contraseña, ya que después de 4 intentos, la conexión será rechazada (`Connection refused`), como se muestra en la captura de pantalla.

#### 3.3. Fortificación del Servicio SSH con `sshd_config`

1.  **Cambiar el puerto por defecto:**

      * **Acción:** Se edita el archivo `/etc/ssh/sshd_config` y se descomenta la directiva `Port`, asignándole un número de puerto personalizado (ej. `2226`).
      * **Comando de prueba:** `ssh -p 2226 testssh@10.0.2.15`.
      * **Resultado:** La conexión fallará en el puerto 22, pero tendrá éxito en el puerto personalizado, lo que dificulta los escaneos automáticos.

2.  **Desactivar el acceso `root`:**

      * **Acción:** En el archivo de configuración del servidor, se busca la directiva `PermitRootLogin` y se establece a `no` para denegar la conexión remota con el usuario `root` a través de contraseñas.
      * **Resultado:** Un intento de conexión como `root` con contraseña será denegado, lo que previene ataques de escalada de privilegios.

3.  **Limitar el número de intentos de autenticación:**

      * **Acción:** Se modifica la directiva `MaxAuthTries` en `sshd_config`, estableciendo un número máximo de intentos fallidos (ej. `2`).
      * **Resultado:** Después de dos intentos de contraseña incorrecta, la conexión será abortada, lo que protege contra ataques de fuerza bruta.

4.  **Restringir el acceso a usuarios específicos:**

      * **Acción:** Se añade la directiva `AllowUsers` al archivo de configuración, seguida de una lista de los usuarios permitidos (ej. `AllowUsers aromero`).
      * **Resultado:** Solo los usuarios especificados podrán conectarse al servidor.

5.  **Mostrar un banner de seguridad:**

      * **Acción:** Se crea un archivo de texto con un mensaje (ej. `/etc/ssh/banner.txt`) y se añade la directiva `Banner /etc/ssh/banner.txt` a `sshd_config`.
      * **Resultado:** El mensaje de bienvenida se mostrará en la terminal del cliente antes de solicitar la contraseña.

#### 3.4. Autenticación con Claves Públicas y SSH-Keygen

1.  **Generar el par de claves:**

      * **Comando:** `ssh-keygen -b 4096 -t rsa`.
      * **Explicación:** El comando `ssh-keygen` genera un par de claves público-privada. `-b 4096` especifica una longitud de 4096 bits para mayor seguridad, y `-t rsa` selecciona el algoritmo RSA. La clave privada se guarda en `/home/<usuario>/.ssh/id_rsa` y la pública en `/home/<usuario>/.ssh/id_rsa.pub`.

2.  **Copiar la clave pública al servidor:**

      * **Comando:** `ssh-copy-id aromero@10.0.2.15`.
      * **Explicación:** Este comando copia la clave pública del cliente al archivo `~/.ssh/authorized_keys` del usuario `aromero` en el servidor. El usuario del servidor debe introducir su contraseña para autorizar la operación.

3.  **Deshabilitar la autenticación por contraseña en el servidor:**

      * **Acción:** En `/etc/ssh/sshd_config`, se establece la directiva `PasswordAuthentication` a `no`. Adicionalmente, se asegura que `PubkeyAuthentication` esté configurada como `yes`.
      * **Resultado:** Al intentar una nueva conexión SSH, el cliente no solicitará la contraseña, sino que se autenticará automáticamente con la clave privada, lo que demuestra una conexión sin contraseña.

#### 3.5. Transferencia de Archivos con SCP y SFTP

1.  **Copia de archivos con SCP (Secure Copy Protocol):**

      * **Copia de local a remoto:** `scp testscp.txt aromero@10.0.2.15:/home/aromero/scp`. Este comando copia el archivo `testscp.txt` del cliente al directorio `/home/aromero/scp` del servidor.
      * **Copia de un directorio:** `scp -r scp-transfer aromero@10.0.2.15:/home/aromero/scp`. El parámetro `-r` se usa para copiar directorios de forma recursiva.
      * **Copia de remoto a local:** `scp aromero@10.0.2.15:/home/aromero/scp/scpubuntu.txt .`. Se especifica la ruta remota como origen y un punto (`.`) como destino para indicar el directorio actual del cliente.

2.  **Transferencia de archivos con SFTP (SSH File Transfer Protocol):**

      * **Comandos:** `sftp aromero@10.0.2.15`. Se abre una sesión interactiva donde se pueden usar comandos como `put` para subir archivos y `get` para descargarlos.

#### 3.6. Creación de Túneles SSH

1.  **Crear un túnel local:**
      * **Comando:** `ssh -L 8080:10.0.2.7:2020 aromero@10.0.2.15`.
      * **Explicación:** Este comando crea un túnel local que redirige el tráfico del puerto local `8080` de la máquina cliente al puerto remoto `2020` de la máquina `10.0.2.7` (el servidor Tomcat), a través del servidor SSH (`10.0.2.15`).
      * **Verificación:** Al acceder a `localhost:8080` desde el navegador del cliente, se muestra la página del servidor Tomcat, demostrando que el túnel funciona correctamente.

#### 3.7. Configuración de MFA con `google-authenticator`

1.  **Instalar el módulo PAM de Google Authenticator:**

      * **Comando:** `sudo apt-get install libpam-google-authenticator`.
      * **Explicación:** Instala las librerías necesarias para integrar Google Authenticator con los módulos de autenticación enchufables (PAM) del sistema.

2.  **Sincronizar con el dispositivo del usuario:**

      * **Comando:** `google-authenticator`.
      * **Explicación:** Este comando inicia un proceso interactivo que genera un código QR en la terminal. El usuario escanea este código con su aplicación de Google Authenticator en el móvil, sincronizando el servidor con el dispositivo. Se generan también códigos de emergencia para casos de pérdida del dispositivo.

3.  **Configurar SSH para MFA:**

      * **Acción 1:** En `/etc/pam.d/sshd`, se añade `auth required pam_google_authenticator.so nullok` para integrar el módulo de autenticación.
      * **Acción 2:** En `/etc/ssh/sshd_config`, se añade la directiva `ChallengeResponseAuthentication yes` para habilitar el soporte de SSH para la autenticación por desafío-respuesta.
      * **Resultado:** Al intentar una conexión SSH, el sistema solicitará primero la contraseña y luego el código de verificación de Google Authenticator, confirmando la activación del doble factor.

#### 3.8. Configuración de `Fail2ban`

1.  **Instalar `Fail2ban`:**

      * **Comando:** `sudo apt-get install fail2ban`.
      * **Explicación:** Instala la herramienta de protección de ataques de fuerza bruta en el servidor.

2.  **Configurar el bloqueo de IP:**

      * **Acción:** Se crea o edita el archivo `/etc/fail2ban/jail.local` y se añaden las siguientes líneas:
        ```
        [sshd]
        maxretry = 3
        bantime = 10800
        ```
      * **Explicación:** La configuración `[sshd]` se aplica al servicio SSH. `maxretry = 3` establece el número máximo de intentos fallidos antes de un bloqueo, y `bantime = 10800` define el tiempo de bloqueo en segundos (3 horas).
      * **Comando:** `sudo systemctl restart fail2ban.service`.
      * **Explicación:** Se reinicia el servicio para aplicar los cambios.

3.  **Verificación del bloqueo:**

      * **Acción:** Desde la máquina Kali Linux, se realizan 3 intentos de conexión SSH con una contraseña incorrecta.
      * **Resultado:** El tercer intento falla y la IP del cliente es bloqueada. Se puede verificar el estado con `sudo fail2ban-client status sshd` en el servidor, lo que mostrará que la IP del cliente ha sido baneada, como se muestra en la captura de pantalla.

-----

### 4\. Conclusiones y Puntos Clave

  * **Importancia y Beneficios de Seguridad:** Fortificar el servicio SSH es un paso crítico en la seguridad de servidores, ya que es la puerta de entrada a los sistemas remotos. La correcta configuración no solo protege contra ataques de fuerza bruta y escalada de privilegios, sino que también garantiza la confidencialidad e integridad de los datos en tránsito. La implementación de las mejores prácticas, como deshabilitar el acceso `root` y usar autenticación con claves públicas, reduce significativamente la superficie de ataque.

  * **Puntos de Aprendizaje Clave:**

      * Se ha comprendido el funcionamiento interno y las características de seguridad del protocolo SSH.
      * Se ha aprendido a identificar y modificar los archivos de configuración clave (`sshd_config` y `ssh_config`) para aplicar directivas de seguridad esenciales.
      * Se ha demostrado la vulnerabilidad de la configuración por defecto ante ataques de fuerza bruta y se ha aprendido a mitigar este riesgo con herramientas como **iptables** y **Fail2ban**.
      * Se ha dominado la configuración de la autenticación con claves públicas, un método superior a las contraseñas, y se ha implementado un sistema de **MFA** para una seguridad aún mayor.
      * Se ha visto la versatilidad de SSH para la transferencia segura de archivos con **SCP** y **SFTP**, y para la creación de túneles que protegen el tráfico de red de otros protocolos.

  * **Relevancia Técnica:** Los procedimientos detallados en este informe son habilidades fundamentales para cualquier profesional de la ciberseguridad o administrador de sistemas. La capacidad de fortificar SSH, gestionar usuarios y autenticación, y utilizar herramientas adicionales como **Fail2ban** y **MFA** es crucial para mantener la integridad, disponibilidad y confidencialidad de los sistemas en un entorno profesional. La comprensión de estos conceptos y la práctica de estos procedimientos garantizan que los servidores estén protegidos contra una amplia gama de amenazas.