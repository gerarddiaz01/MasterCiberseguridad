# Informe de Ejercicio: Defensa Avanzada con IPTables contra Ataques de Reconocimiento y Fuerza Bruta

**Éste ejercicio no ha sido muy efectivo, en el siguiente informe si tengo un buen ejercicio bien realizado de ataques con nmap, curl, ssh y hydra, cómo preparar la máquina de defensa con itables y veremos cómo logramos defender la máquina y analizar los logs. Pero hacer éste ejercicio de abajo nos ha permitido tener mas soltura con itables y entender cómo funciona todo esto.**

## 1\. Introducción al Ejercicio: Ataque y Defensa en un Entorno Controlado

Este ejercicio práctico está diseñado para proporcionar experiencia directa en la configuración de reglas de firewall utilizando **IPTables** para defender una máquina virtual contra una serie de ataques simulados desde otra máquina virtual. A través de esta práctica, aprenderemos a analizar patrones de ataque, ajustar las reglas del firewall para una seguridad mejorada y asegurar la accesibilidad de los servicios legítimos.

El objetivo principal es demostrar la eficacia de `iptables` en la protección de una infraestructura Linux frente a amenazas comunes. Al final, los logs de las conexiones intentadas serán cruciales para el análisis de seguridad.

## 2\. Preparación del Entorno de Laboratorio Virtual

Para este ejercicio, hemos configurado un laboratorio virtual con dos máquinas Linux en la misma red local, simulando un escenario de ataque y defensa:

  * **Máquina Atacante (Attacker VM)**: Tu máquina **Kali Linux**. Es una distribución especializada en pruebas de penetración, equipada con las herramientas necesarias para simular ataques.
      * **Dirección IP**: `192.168.1.104`
  * **Máquina Defensora (Defender VM)**: Tu máquina **Ubuntu Desktop**. Esta máquina será el objetivo de los ataques y donde configuraremos las defensas con `iptables`.
      * **Dirección IP**: `192.168.1.103`

Ambas máquinas virtuales están conectadas a una **Red Interna (`intnet`)** cuya conectividad a Internet es proporcionada y gestionada por una máquina virtual **pfSense**. Esta configuración garantiza que ambas VMs reciban IPs únicas y tengan un gateway y DNS centralizados, creando un entorno de red estable y representativo de una infraestructura real. Hemos verificado la conectividad básica entre las VMs y el acceso a Internet en ambas.

### 2.1. Verificación de Herramientas y Servicios Necesarios

Antes de iniciar el ejercicio, confirmamos que la máquina atacante posee las herramientas de ataque y que la máquina defensora tiene el servicio SSH activo.

#### 2.1.1. Herramientas en la Máquina Atacante (Kali Linux)

  * **Nmap**: Verificado (`nmap --version`). Herramienta para escaneo de puertos.
  * **cURL**: Verificado (`curl --version`). Herramienta para peticiones HTTP/HTTPS.
  * **SSH Client**: Verificado (`ssh -V`). Cliente para conexiones SSH.
  * **Hydra**: Verificado e instalado (`sudo apt install hydra`). Herramienta para ataques de fuerza bruta.

#### 2.1.2. Servicio SSH en la Máquina Defensora (Ubuntu Desktop)

El servicio SSH debe estar activo para que sea el objetivo de nuestros ataques y defensas.

  * **Verificación**: `sudo systemctl status ssh`
  * **Acción si no está activo**: En tu caso, el servicio SSH no estaba activo por defecto, por lo que fue necesario iniciarlo y habilitarlo.
      * **Comandos**:
        ```bash
        sudo systemctl enable ssh # Habilita el servicio para que inicie con el sistema
        sudo systemctl start ssh  # Inicia el servicio inmediatamente
        ```
      * **Explicación**: `systemctl enable ssh` crea los enlaces simbólicos necesarios para que el servicio `ssh` (el servidor OpenSSH) se inicie automáticamente cada vez que el sistema arranque. `systemctl start ssh` inicia el servicio en la sesión actual.
      * **Objetivo**: Asegurar que el servidor SSH esté escuchando en el puerto 22 y listo para aceptar conexiones.

## 3\. Conducción de Ataques Simulados

Desde la Máquina Atacante (Kali Linux, `192.168.1.104`), realizamos una serie de ataques contra la Máquina Defensora (Ubuntu Desktop, `192.168.1.103`) antes de configurar las defensas. Esto nos da una línea base del comportamiento sin firewall.

### 3.1. Escaneo de Puertos (Port Scanning) - Usando `nmap`

  * **Comando**: `nmap 192.168.1.103`
  * **Explicación**: `nmap` se utiliza para descubrir puertos abiertos en el objetivo. Un escaneo inicial de puertos es la primera fase del reconocimiento para un atacante.
  * **Resultado**: Nmap identificó que la máquina estaba activa (`Host is up`) y que el puerto `22/tcp` (SSH) estaba `open`. También mostró `999 filtered tcp ports (no-response)`, lo que indica que no había otros servicios comunes abiertos.

### 3.2. Petición HTTP (HTTP Request) - Usando `curl`

  * **Comando**: `curl http://192.168.1.103`
  * **Explicación**: Este comando simula un intento de acceso a un servicio web en el puerto HTTP estándar (80).
  * **Resultado**: La petición `curl` se quedó colgada. Esto es el comportamiento esperado si no hay un servidor web activo en el puerto 80.

### 3.3. Intento de Conexión SSH (SSH Connection Attempt) - Usando `ssh`

  * **Comando**: `ssh gerard@192.168.1.103`
  * **Explicación**: Intento directo de un atacante de establecer una conexión SSH con un usuario.
  * **Resultado**: El servicio SSH en la Máquina Defensora respondió solicitando una contraseña, confirmando que está activo y accesible. Tras introducir una contraseña incorrecta, la conexión fue denegada (`Permission denied`).

### 3.4. Ataque de Fuerza Bruta SSH (SSH Brute-Force Attack) - Usando `hydra`

  * **Comando**: `hydra -l gerard -P password_list.txt ssh://192.168.1.103`
  * **Explicación**: Hydra intenta adivinar contraseñas probando múltiples combinaciones desde un archivo de lista de palabras (`password_list.txt`).
  * **Resultado (Sin defensas)**: En el primer intento (antes de aplicar las defensas), Hydra encontró la contraseña `1234` para el usuario `gerard` en apenas 2 segundos. Esto subraya la vulnerabilidad de las contraseñas débiles o adivinables sin protección de tasa.

## 4\. Implementación de Estrategias de Defensa con IPTables

Ahora, configuraremos las reglas de `iptables` en la Máquina Defensora (Ubuntu Desktop, `192.168.1.103`) para mitigar los ataques simulados. La clave de `iptables` es su **jerarquía**: las reglas se procesan de arriba hacia abajo, y la primera regla que coincide con un paquete determina su acción. Una política por defecto de `DROP` para el tráfico entrante es esencial para una postura de "prohibido por defecto".

### 4.1. Configuración de Reglas de IPTables en la Máquina Defensora

Para asegurar el orden correcto y la efectividad de las reglas, las insertamos explícitamente en posiciones específicas de la cadena `INPUT`. Primero, limpiamos las reglas existentes y establecemos la política `DROP`.

  * **Limpiar todas las reglas existentes**: `sudo iptables -F`

      * **Explicación**: Elimina todas las reglas cargadas actualmente en las cadenas (`INPUT`, `FORWARD`, `OUTPUT`), dejando un estado limpio para la nueva configuración.

  * **Establecer la política por defecto de `INPUT` a `DROP`**: `sudo iptables -P INPUT DROP`

      * **Explicación**: Cualquier paquete que llegue a la cadena `INPUT` y no coincida con una regla explícita de `ACCEPT` será descartado silenciosamente. Este es el principio de seguridad "lo que no está permitido, está prohibido".

  * **Comandos para añadir reglas (con sintaxis `-I INPUT <posición>` para insertar en el orden correcto)**:

    1.  **Permitir tráfico de Loopback**:

        ```bash
        sudo iptables -I INPUT 1 -i lo -j ACCEPT
        ```

          * **Explicación**: Inserta esta regla en la posición `1`. `-i lo` especifica la interfaz de loopback, que es esencial para el funcionamiento interno del sistema. `ACCEPT` permite todo este tráfico.
          * **Objetivo**: Asegurar la comunicación interna del propio sistema.

    2.  **Permitir Tráfico Relacionado y Establecido**:

        ```bash
        sudo iptables -I INPUT 2 -m state --state ESTABLISHED,RELATED -j ACCEPT
        ```

          * **Explicación**: Inserta en la posición `2`. `-m state --state ESTABLISHED,RELATED` usa el módulo `state` para permitir paquetes que forman parte de una conexión ya establecida o que están relacionados con una conexión existente (ej. respuestas a tus peticiones salientes).
          * **Objetivo**: Permitir que el servidor reciba respuestas legítimas a sus propias conexiones salientes y mantenga sesiones activas.

    3.  **Registrar (Log) Paquetes Descartados**:

        ```bash
        sudo iptables -I INPUT 3 -j LOG --log-prefix "IPTables-Dropped: "
        ```

          * **Explicación**: Inserta en la posición `3`. `-j LOG` hace que los paquetes que coincidan con esta regla se registren en `syslog` (normalmente en `/var/log/syslog`). `--log-prefix` añade un prefijo para facilitar la búsqueda.
          * **Objetivo**: Capturar información sobre el tráfico que será `DROP`eado por reglas posteriores o por la política `DROP` por defecto, vital para la auditoría y detección de ataques.

    4.  **Limitar la Tasa de Peticiones ICMP (Ping)**:

        ```bash
        sudo iptables -I INPUT 4 -p icmp -m limit --limit 1/second --limit-burst 10 -j ACCEPT
        ```

          * **Explicación**: Inserta en la posición `4`. `-p icmp` especifica el protocolo ICMP. `-m limit` con `--limit 1/second` permite 1 paquete por segundo, y `--limit-burst 10` permite una ráfaga inicial de 10 paquetes. Los pings que excedan este límite serán `DROP`eados por la política por defecto y registrados por la regla `LOG` anterior.
          * **Objetivo**: Mitigar los escaneos de ping y evitar la exposición innecesaria de información sobre la actividad del host.

    5.  **Regla de Limitación de Tasa SSH - Registrar y Permitir Inicialmente (SET)**:

        ```bash
        sudo iptables -I INPUT 5 -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH_BRUTE -j ACCEPT
        ```

          * **Explicación**: Inserta en la posición `5`. Se aplica a nuevas conexiones TCP (`-m state --state NEW`) al puerto 22 (SSH). `-m recent --set --name SSH_BRUTE` registra la IP de origen en una lista llamada `SSH_BRUTE`. `-j ACCEPT` permite que estas conexiones iniciales pasen.
          * **Objetivo**: Monitorear y registrar las IPs que intentan nuevas conexiones SSH para el control de tasa.

    6.  **Regla de Limitación de Tasa SSH - Descartar si excede límite (DROP)**:

        ```bash
        sudo iptables -I INPUT 6 -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 10 --hitcount 3 --name SSH_BRUTE -j DROP
        ```

          * **Explicación**: Inserta en la posición `6`. Si una IP en la lista `SSH_BRUTE` ha intentado más de 3 (`--hitcount 3`) conexiones nuevas en los últimos 10 segundos (`--seconds 10`), esta regla la descartará (`-j DROP`).
          * **Objetivo**: Frustrar los ataques de fuerza bruta, haciendo que el atacante sea bloqueado después de un número limitado de intentos en un corto período. Estos descartes serán registrados por la regla `LOG` en la posición 3.

    7.  **Permitir Tráfico SSH para Conexiones Legítimas (no limitadas/establecidas)**:

        ```bash
        sudo iptables -I INPUT 7 -p tcp --dport 22 -j ACCEPT
        ```

          * **Explicación**: Inserta en la posición `7`. Esta regla permite cualquier tráfico TCP al puerto 22. Su posición es crítica: solo se alcanzará si el tráfico no ha sido descartado por la regla de limitación de tasa anterior (Paso 3.6). De esta forma, las conexiones SSH legítimas y las que no exceden el límite son permitidas.
          * **Objetivo**: Asegurar que los usuarios legítimos puedan conectarse vía SSH mientras se bloquean los ataques de fuerza bruta.

  * **Verificación de las Reglas (Comando)**: `sudo iptables -L INPUT -n -v`

      * **Resultado (Consolidado de las capturas previas)**:
        ```
        Chain INPUT (policy DROP X packets, X bytes)
         pkts bytes target     prot opt in     out     source               destination
            X     X ACCEPT     all  --  lo     * 0.0.0.0/0            0.0.0.0/0
            X     X ACCEPT     all  --  * * 0.0.0.0/0            0.0.0.0/0            state RELATED,ESTABLISHED
            X     X LOG        all  --  * * 0.0.0.0/0            0.0.0.0/0            LOG flags 0 level 4 prefix "IPTables-Dropped: "
            X     X ACCEPT     icmp --  * * 0.0.0.0/0            0.0.0.0/0            limit: avg 1/sec burst 10 packets
            X     X ACCEPT     tcp  --  * * 0.0.0.0/0            0.0.0.0/0            tcp dpt:22 state NEW recent: SET name: SSH_BRUTE side: source
            X     X DROP       tcp  --  * * 0.0.0.0/0            0.0.0.0/0            tcp dpt:22 state NEW recent: UPDATE seconds: 10 hit_count: 3 name: SSH_BRUTE side: source
            X     X ACCEPT     tcp  --  * * 0.0.0.0/0            0.0.0.0/0            tcp dpt:22
        ```
          * **Análisis**: Esta es la lista de reglas **correctamente ordenada** para la defensa.

## 5\. Repetición de Ataques con Defensas Activadas

Una vez que las reglas de `iptables` se aplicaron correctamente en la Máquina Defensora, repetimos los ataques desde Kali Linux.

### 5.1. Re-Escaneo de Puertos (Port Scanning) - Usando `nmap`

  * **Comando**: `nmap 192.168.1.103`
  * **Resultado**: Nmap sigue mostrando el `Host is up` y el puerto `22/tcp` como `open`. Sin embargo, `999 filtered tcp ports (no-response)` sigue apareciendo.
  * **Análisis**: El firewall está haciendo que el servidor sea más "silencioso". Aunque el puerto 22 es visible (porque está permitido), el resto de los puertos no dan una respuesta de "cerrado", lo que dificulta el reconocimiento detallado. La limitación de ICMP también actúa sobre los pings de Nmap.

### 5.2. Re-Petición HTTP (HTTP Request) - Usando `curl`

  * **Comando**: `curl http://192.168.1.103`
  * **Resultado**: La petición `curl` se siguió colgando.
  * **Análisis**: Esto confirma que la política `DROP` por defecto para `INPUT` está bloqueando eficazmente el tráfico al puerto 80 (HTTP), ya que no hay una regla `ACCEPT` específica para este puerto.

### 5.3. Re-Intento de Conexión SSH (SSH Connection Attempt) - Usando `ssh`

  * **Comando**: `ssh gerard@192.168.1.103`
  * **Resultado**: El servicio SSH siguió pidiendo la contraseña, confirmando que el acceso legítimo no está bloqueado.
  * **Análisis**: La conexión SSH inicial es aceptada por la regla `ACCEPT` del puerto 22, lo que permite la fase de autenticación.

### 5.4. Re-Ataque de Fuerza Bruta SSH (SSH Brute-Force Attack) - Usando `hydra`

Este fue el punto crucial para verificar la efectividad de las reglas de limitación de tasa.

  * **Comando**: `hydra -l gerard -P password_list.txt ssh://192.168.1.103`
  * **Resultado (Con contraseña en el diccionario)**:
      * Hydra tardó aproximadamente **32 segundos** en completarse (frente a los 2 segundos iniciales).
      * **Encontró la contraseña `1234`**.
  * **Resultado (Sin contraseña en el diccionario)**:
      * Hydra tardó **32 segundos**.
      * **No encontró ninguna contraseña válida**.
  * **Análisis**:
      * La defensa de `iptables` con el módulo `recent` funcionó: **ralentizó drásticamente el ataque de fuerza bruta (16 veces más lento)**. Esto demuestra que la máquina atacante fue bloqueada temporalmente después de un número limitado de intentos, teniendo que esperar para continuar.
      * Al no encontrar la contraseña correcta (o si la contraseña es lo suficientemente compleja), el atacante se ve frustrado, ya que el ataque se vuelve inviable en un tiempo razonable.

### 5.5. Monitoreo de Logs en la Máquina Defensora (Ubuntu Desktop)

  * **Comando**: `sudo tail -f /var/log/syslog | grep "IPTables-Dropped"`
  * **Resultado**: Se observó una **gran cantidad de entradas `IPTables-Dropped:`** en los logs. Estas entradas mostraban paquetes TCP destinados al puerto 22 (SSH) desde la IP de Kali (`192.168.1.104`) que estaban siendo descartados.
  * **Análisis**: Esto confirma que la regla `LOG` está funcionando correctamente y que el firewall `iptables` está activamente descartando los intentos de conexión SSH que exceden el límite de tasa. Estos logs son vitales para la detección de intrusiones, el análisis forense y la mejora de las políticas de seguridad.

## 6\. Impacto del Ejercicio en un Ataque Real en una Empresa

Este ejercicio práctico es directamente aplicable a la **ciberseguridad empresarial** y demuestra la importancia del **hardening de sistemas** a través de `iptables`:

  * **Reducción de la Superficie de Ataque**: Al implementar una política `DROP` por defecto y permitir explícitamente solo los servicios necesarios, la empresa reduce drásticamente los puntos vulnerables expuestos a posibles atacantes.
  * **Mitigación de Reconocimiento Activo**: El firewall hace más difícil y lento para un atacante mapear la red y los servicios, ocultando la infraestructura interna. Esto aumenta el "costo" del ataque para el adversario.
  * **Defensa contra Fuerza Bruta**: La limitación de tasa para servicios como SSH es una defensa crítica. Aunque una contraseña débil podría ser adivinada, el firewall ralentiza el ataque de forma exponencial, convirtiéndolo en inviable en la mayoría de los casos y proporcionando tiempo valioso para que los **Sistemas de Detección de Intrusiones (IDS)** o los administradores reaccionen (bloqueando la IP ofensora, forzando un cambio de contraseña).
  * **Auditoría y Detección de Incidentes**: La generación de logs es invaluable. En una empresa, estos logs se enviarían a un sistema **SIEM (Security Information and Event Management)** para alertar sobre actividades sospechosas (como múltiples intentos de inicio de sesión fallidos o escaneos de puertos), permitiendo una respuesta rápida y proactiva a las amenazas.
  * **Control Granular**: `iptables` permite un control extremadamente granular sobre el tráfico, permitiendo a las empresas aplicar el **Principio de Mínimo Privilegio** a nivel de red, aceptando solo el tráfico esencial y denegando todo lo demás.

En resumen, este ejercicio demuestra que `iptables` no es solo una herramienta de configuración de red, sino un componente vital en una estrategia de **defensa en profundidad**, protegiendo activamente los servicios críticos y proporcionando la visibilidad necesaria para una ciberseguridad robusta.