# IPTables: El Firewall del Kernel Linux para la Seguridad de Redes

**IPTables** es una utilidad de espacio de usuario que permite a los administradores de sistema configurar las reglas de filtrado de paquetes del firewall del kernel de Linux, implementadas como diferentes módulos de Netfilter. Las reglas definidas por IPTables se utilizan para el filtrado de paquetes, la traducción de direcciones de red (**NAT - Network Address Translation**) y la traducción de puertos, que pueden aplicarse a los paquetes en diferentes puntos del proceso de enrutamiento.

IPTables es un firewall completo basado en reglas para controlar el tráfico de entrada y salida, siendo una herramienta crítica en la arquitectura de cualquier red para la seguridad avanzada y la optimización del rendimiento.

## 1\. Conceptos Fundamentales de IPTables

IPTables se basa en una estructura jerárquica de **tablas**, las cuales gestionan **cadenas (chains)**, que a su vez contienen **reglas** concretas.

### 1.1. Cadenas (Chains) Principales

Existen tres tipos de cadenas principales predefinidas que controlan el flujo del tráfico:

  * **INPUT**: Filtra los paquetes **entrantes** destinados al sistema local, controlando el acceso a servicios locales como SSH o servidores web.
  * **FORWARD**: Maneja los paquetes que están siendo **enrutados a través del sistema**, típicamente utilizada en routers o firewalls para filtrar el tráfico entre diferentes segmentos de red.
  * **OUTPUT**: Filtra los paquetes **salientes** generados por procesos locales antes de ser enviados, controlando las conexiones de salida desde el sistema.

Estas cadenas permiten un control granular sobre el tráfico de red en diferentes etapas: entrante, de reenvío y saliente.

### 1.2. Consejos Básicos para el Hardening de un Cortafuegos con IPTables

Para una configuración robusta de un firewall con IPTables, es esencial seguir ciertas prácticas:

  * **Realizar un Backup de la Configuración**: Antes de realizar cualquier cambio significativo, es crucial guardar la configuración actual para poder restaurarla en caso de problemas.
  * **Orden Jerárquico de las Reglas**: El orden de las reglas es **jerárquico**. Las reglas más específicas deben colocarse al principio de la cadena, y las más genéricas al final.
  * **Utilizar Listas Blancas (Whitelist)**: Para permitir el acceso a grupos específicos de usuarios o IPs (ej. personal de IT), se recomienda usar listas blancas.
  * **Establecer una Política por Defecto (`DROP`)**: La política por defecto para las cadenas debe ser `DROP` (descartar todo el tráfico). Esto significa que solo el tráfico explícitamente permitido pasará.
  * **Abrir Solo Puertos Necesarios**: Estudiar cada caso y abrir únicamente los puertos que sean estrictamente necesarios para los servicios.
  * **Limitar el Número de Conexiones**: Es una solución efectiva para mitigar ataques de **denegación de servicio distribuido (DDoS)**, controlando la tasa de conexiones.
  * **Mantenimiento de Reglas**: Realizar un mantenimiento periódico de las reglas, eliminando aquellas que ya no se utilicen para evitar problemas potenciales de seguridad y mantener la configuración limpia.

## 2\. Administración Básica de Reglas con IPTables

Vamos a ver cómo administrar el tráfico de red de manera efectiva mediante comandos básicos de IPTables.

### 2.1. Mostrar las Reglas Actuales de IPTables

Para ver la configuración actual del firewall.

  * **Comando**: `sudo iptables -L`
  * **Sintaxis**:
    ```bash
    sudo iptables -L
    ```
  * **Explicación**:
      * `sudo`: Ejecuta el comando con privilegios de superusuario.
      * `iptables`: El comando principal para gestionar el firewall.
      * `-L`: Lista todas las reglas actuales en todas las cadenas (INPUT, FORWARD, OUTPUT).
  * **Objetivo**: Obtener una visión general de las políticas predeterminadas y cualquier regla específica aplicada.
  * **Resultado Esperado**: Muestra las tres cadenas principales con su política por defecto (`(policy ACCEPT)`) y cualquier regla que se haya añadido. Inicialmente, no habrá reglas específicas.

### 2.2. Bloquear Todo el Tráfico entre Dos Máquinas

Para demostrar el control de tráfico, bloquearemos toda la comunicación entre dos máquinas virtuales. Asumiremos que estamos en la **Máquina 2 (IP: `10.211.55.17`)** y queremos bloquear el tráfico hacia/desde la **Máquina 1 (IP: `10.211.55.5`)**.

  * **Comando (Bloquear tráfico entrante de la Máquina 1)**:

    ```bash
    sudo iptables -A INPUT -s 10.211.55.5 -j DROP
    ```

  * **Explicación**:

      * `-A INPUT`: Añade (`-A`) una regla al final de la cadena `INPUT` (tráfico entrante al sistema local).
      * `-s 10.211.55.5`: Especifica la dirección IP de origen (`-s` de *source*) de los paquetes a los que se aplicará la regla (en este caso, la Máquina 1).
      * `-j DROP`: Define la acción (`-j` de *jump*) a tomar con los paquetes que coincidan con la regla. `DROP` descarta el paquete silenciosamente, sin enviar ninguna notificación al origen.

  * **Objetivo**: Bloquear cualquier paquete que provenga de la Máquina 1 y que esté destinado a la Máquina 2.

  * **Comando (Bloquear tráfico saliente hacia la Máquina 1)**:

    ```bash
    sudo iptables -A OUTPUT -d 10.211.55.5 -j DROP
    ```

  * **Explicación**:

      * `-A OUTPUT`: Añade una regla al final de la cadena `OUTPUT` (tráfico saliente generado por el sistema local).
      * `-d 10.211.55.5`: Especifica la dirección IP de destino (`-d` de *destination*) de los paquetes a los que se aplicará la regla (en este caso, la Máquina 1).
      * `-j DROP`: Descarta el paquete.

  * **Objetivo**: Bloquear cualquier paquete generado por la Máquina 2 que intente ir hacia la Máquina 1.

  * **Verificación (Ping)**: Si ahora intentas hacer `ping 10.211.55.5` desde la Máquina 2, verás `ping: sendmsg: Operation not permitted` o `Request timed out`, indicando que el cortafuegos está bloqueando la conexión.

### 2.3. Habilitar Tráfico SSH y la Importancia del Orden de las Reglas

Ahora, intentaremos permitir el tráfico SSH (puerto 22) desde la Máquina 1 hacia la Máquina 2.

  * **Comando (Permitir SSH entrante desde Máquina 1)**:

    ```bash
    sudo iptables -A INPUT -p tcp --dport 22 -s 10.211.55.5 -j ACCEPT
    ```

  * **Explicación**:

      * `-p tcp`: Especifica el protocolo (`-p`) a TCP.
      * `--dport 22`: Especifica el puerto de destino (`--dport`) a 22 (puerto estándar de SSH).
      * `-s 10.211.55.5`: Origen es la Máquina 1.
      * `-j ACCEPT`: Permite el paquete.

  * **Objetivo**: Permitir conexiones SSH entrantes desde la Máquina 1.

  * **Comando (Permitir SSH saliente hacia Máquina 1)**:

    ```bash
    sudo iptables -A OUTPUT -p tcp --sport 22 -d 10.211.55.5 -j ACCEPT
    ```

  * **Explicación**:

      * `--sport 22`: Especifica el puerto de origen (`--sport`) a 22.
      * `-d 10.211.55.5`: Destino es la Máquina 1.

  * **Objetivo**: Permitir conexiones SSH salientes hacia la Máquina 1.

  * **Problema de Jerarquía**: Si intentas conectar por SSH ahora, verás que **no funciona**. Esto se debe a la **jerarquía de las reglas**. Las reglas `DROP` que bloquean todo el tráfico se añadieron *antes* que las reglas `ACCEPT` para SSH. IPTables procesa las reglas en orden: si un paquete coincide con una regla `DROP` anterior, nunca llegará a la regla `ACCEPT` posterior.

### 2.4. Limpiar Reglas y Establecer la Jerarquía Correcta

Para solucionar el problema de jerarquía, la estrategia es: **primero permitir lo específico (SSH), y luego bloquear todo lo demás**.

1.  **Eliminar Todas las Reglas Existentes**:

      * **Comando**: `sudo iptables -F`
      * **Sintaxis**:
        ```bash
        sudo iptables -F
        ```
      * **Explicación**:
          * `-F`: Elimina (`-F` de *Flush*) todas las reglas de todas las cadenas por defecto (INPUT, FORWARD, OUTPUT).
      * **Objetivo**: Resetear el firewall a un estado limpio sin reglas.
      * **Verificación**: `sudo iptables -L` mostrará las cadenas vacías.

2.  **Habilitar SSH (Reglas `ACCEPT`)**:

      * **Comando (SSH entrante)**:
        ```bash
        sudo iptables -A INPUT -p tcp --dport 22 -s 10.211.55.5 -j ACCEPT
        ```
      * **Comando (SSH saliente)**:
        ```bash
        sudo iptables -A OUTPUT -p tcp --sport 22 -d 10.211.55.5 -j ACCEPT
        ```
      * **Explicación**: Se añaden las reglas `ACCEPT` para SSH al final de las cadenas `INPUT` y `OUTPUT`.

3.  **Bloquear Todo lo Demás (Reglas `DROP`)**:

      * **Comando (Bloquear todo entrante desde Máquina 1)**:
        ```bash
        sudo iptables -A INPUT -s 10.211.55.5 -j DROP
        ```
      * **Comando (Bloquear todo saliente hacia Máquina 1)**:
        ```bash
        sudo iptables -A OUTPUT -d 10.211.55.5 -j DROP
        ```
      * **Explicación**: Se añaden las reglas `DROP` al final de las cadenas. Como se añaden *después* de las reglas `ACCEPT` de SSH, el tráfico SSH será permitido, y luego el resto del tráfico de esa IP será descartado.
      * **Verificación (`sudo iptables -L`)**: Verás las reglas `ACCEPT` para SSH primero, seguidas de las reglas `DROP`.

<!-- end list -->

  * **Resultado**: Ahora, si intentas una conexión SSH desde la Máquina 1 a la Máquina 2, **sí te dejará conectar**. Sin embargo, si intentas hacer `ping` a la Máquina 1, **no funcionará** debido a la regla `DROP` general que bloquea todo excepto SSH.

### 2.5. Limitar la Tasa de Conexiones SSH (Mitigación de Fuerza Bruta)

IPTables permite un control muy granular, como limitar la tasa de conexiones para mitigar ataques de **fuerza bruta** o **DoS**. Limitaremos las conexiones SSH a un máximo de 4 por minuto.

1.  **Eliminar las Reglas `DROP` Anteriores**:
    Para aplicar la nueva lógica, eliminaremos las reglas `DROP` genéricas que pusimos.

      * **Comando (Eliminar DROP saliente)**: `sudo iptables -D OUTPUT -d 10.211.55.5 -j DROP`
      * **Comando (Eliminar DROP entrante)**: `sudo iptables -D INPUT -s 10.211.55.5 -j DROP`
      * **Explicación**: `-D` (Delete) elimina una regla específica. Debes especificar la regla exactamente como la añadiste.
      * **Alternativa (Mover Reglas)**: En lugar de eliminar y añadir, también se pueden mover reglas. El comando `sudo iptables -R <chain> <rule_num> <rule>` reemplaza una regla en una posición, y `sudo iptables -I <chain> <rule_num> <rule>` inserta una regla en una posición específica, desplazando las demás. Por ejemplo, `sudo iptables -R INPUT 3 -s 10.211.55.5 -j DROP` reemplazaría la regla en la posición 3.

2.  **Añadir Reglas de Limitación de Tasa para SSH (en la Máquina 2)**:
    Estas reglas se aplican a la cadena `INPUT` para controlar las conexiones entrantes.

      * **Comando (Primera regla de limitación)**:

        ```bash
        sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set -j ACCEPT
        ```

      * **Explicación**:

          * `-m state --state NEW`: Utiliza el módulo `state` para aplicar la regla solo a **conexiones nuevas** (`NEW`).
          * `-m recent --set`: Utiliza el módulo `recent` para registrar la dirección IP de origen de la conexión en una lista de conexiones recientes.
          * `-j ACCEPT`: Si la conexión es nueva y se registra, se acepta inicialmente.

      * **Objetivo**: Registrar las IPs de origen de las nuevas conexiones SSH.

      * **Comando (Segunda regla de limitación y descarte)**:

        ```bash
        sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
        ```

      * **Explicación**:

          * `-m recent --update`: Actualiza la marca de tiempo de la IP en la lista de conexiones recientes.
          * `--seconds 60`: Define un período de tiempo de 60 segundos.
          * `--hitcount 4`: Establece un límite de 4 conexiones.
          * `-j DROP`: Si una IP intenta más de 4 conexiones nuevas en 60 segundos, los paquetes posteriores de esa IP serán descartados.

      * **Objetivo**: Bloquear ataques de fuerza bruta limitando la tasa de nuevas conexiones SSH.

<!-- end list -->

  * **Resumen de las Reglas de Limitación**: La primera regla establece una marca de tiempo para la IP de origen cuando se inicia una nueva conexión SSH. La segunda regla verifica si esa IP ha intentado más de 4 conexiones SSH en los últimos 60 segundos. Si se supera el límite, los paquetes de conexión posteriores de esa IP serán descartados.

### 2.6. Almacenar y Restaurar Reglas de IPTables

Las reglas de IPTables son **volátiles**; se pierden al reiniciar el sistema. Para que persistan, deben guardarse.

1.  **Almacenar las Reglas**:

      * **Comando**: `sudo iptables-save > /etc/iptables/rules.v4`
      * **Sintaxis**:
        ```bash
        sudo iptables-save > /etc/iptables/rules.v4
        ```
      * **Explicación**: `iptables-save` vuelca la configuración actual de IPTables a la salida estándar, y `>` redirige esa salida a un archivo (por convención, `/etc/iptables/rules.v4` para IPv4).
      * **Objetivo**: Guardar la configuración actual del firewall en un archivo para su persistencia.

2.  **Restaurar las Reglas**:

      * **Comando**: `sudo iptables-restore < /etc/iptables/rules.v4`
      * **Sintaxis**:
        ```bash
        sudo iptables-restore < /etc/iptables/rules.v4
        ```
      * **Explicación**: `iptables-restore` lee las reglas de un archivo (indicado por `<`) y las aplica al firewall.
      * **Objetivo**: Cargar una configuración de firewall guardada previamente.
      * **Persistencia al Inicio**: Para que las reglas se carguen automáticamente al inicio del sistema, este comando se suele añadir a un script de inicio o se utiliza un paquete como `iptables-persistent`.

## 3\. Compartir Conexión a Internet (NAT con IPTables)

IPTables es fundamental para configurar **NAT (Network Address Translation)**, permitiendo que una máquina con acceso a Internet actúe como gateway para otra máquina sin acceso directo.

**Escenario**: Máquina 1 (IP: `10.211.55.5`, con Internet) actuará como gateway para Máquina 2 (IP: `10.211.55.17`, sin Internet).

### 3.1. Habilitar el Enrutamiento (IP Forwarding) en la Máquina 1

La Máquina 1 debe ser capaz de reenviar paquetes entre sus interfaces.

  * **Comando (Editar archivo de configuración)**: `sudo nano /etc/sysctl.conf`

  * **Sintaxis**:

    ```bash
    sudo nano /etc/sysctl.conf
    ```

  * **Explicación**: Abre el archivo de configuración del kernel.

  * **Modificación**: Descomenta la línea (elimina el `#` al principio) que dice:

    ```
    net.ipv4.ip_forward=1
    ```

  * **Guardar y salir**: `Ctrl+O`, `Enter`, `Ctrl+X`.

  * **Comando (Aplicar el cambio sin reiniciar)**: `sudo sysctl -p`

  * **Sintaxis**:

    ```bash
    sudo sysctl -p
    ```

  * **Explicación**: Recarga las configuraciones del kernel desde `/etc/sysctl.conf`.

  * **Objetivo**: Habilitar el reenvío de paquetes IPv4 en el kernel de la Máquina 1.

### 3.2. Configurar Masquerading (NAT de Salida) en la Máquina 1

Esto oculta las direcciones IP internas de la Máquina 2, haciendo que el tráfico saliente parezca venir de la Máquina 1.

  * **Comando**: `sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`
  * **Sintaxis**:
    ```bash
    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    ```
  * **Explicación**:
      * `-t nat`: Especifica que la regla se aplicará a la tabla `nat` (Network Address Translation).
      * `-A POSTROUTING`: Añade la regla a la cadena `POSTROUTING`, que se aplica *después* de que el enrutamiento se ha realizado, justo antes de que el paquete salga de la interfaz.
      * `-o eth0`: Especifica la interfaz de salida (`-o`) a `eth0` (asumiendo que `eth0` es la interfaz principal de salida a Internet de la Máquina 1).
      * `-j MASQUERADE`: La acción `MASQUERADE` es un tipo de NAT de origen (SNAT) que modifica la dirección IP de origen de los paquetes salientes para que parezcan provenir de la IP de la interfaz de salida de la Máquina 1. Es útil cuando la IP de salida es dinámica.
  * **Objetivo**: Configurar la Máquina 1 para que realice NAT de salida, permitiendo que la Máquina 2 comparta su conexión a Internet.

### 3.3. Configurar la Máquina 2 para Usar la Máquina 1 como Gateway

La Máquina 2 debe saber que debe enviar todo su tráfico a la Máquina 1 para acceder a Internet.

  * **Comando (Asignar IP estática a Máquina 2, si no tiene DHCP)**:

    ```bash
    sudo ip addr add 10.211.55.17/24 dev eth0 # Asumiendo eth0 es la interfaz
    ```

      * **Explicación**: Asigna la dirección IP `10.211.55.17` con una máscara `/24` a la interfaz `eth0` de la Máquina 2.

  * **Comando (Establecer gateway predeterminado)**:

    ```bash
    sudo ip route add default via 10.211.55.5
    ```

      * **Explicación**: Añade una ruta por defecto (`default`) que dirige todo el tráfico no especificado a través de la IP `10.211.55.5` (la IP de la Máquina 1).
      * **Objetivo**: Configurar la Máquina 2 para que use la Máquina 1 como su puerta de enlace a Internet.

  * **Comando (Configurar DNS en Máquina 2)**:

      * **Comando**: `sudo nano /etc/resolv.conf`
      * **Sintaxis**:
        ```bash
        sudo nano /etc/resolv.conf
        ```
      * **Modificación**: Añadir o asegurar que haya líneas como:
        ```
        nameserver 8.8.8.8
        nameserver 8.8.4.4
        ```
      * **Objetivo**: Proporcionar servidores DNS a la Máquina 2 para la resolución de nombres.

  * **Verificación**: Desde la Máquina 2, haz `ping www.google.es`. Deberías ver respuestas, confirmando que la Máquina 2 accede a Internet a través de la Máquina 1.

## 4\. Bloquear el Tráfico ICMP (Ping)

El protocolo ICMP (Internet Control Message Protocol), utilizado por `ping`, puede proporcionar mucha información valiosa a un atacante en la fase de reconocimiento. Bloquearlo es una medida de seguridad común.

**Escenario**: Bloquear los pings entrantes a la Máquina 1 (IP: `10.211.55.5`).

  * **Comando**: `sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP`

  * **Sintaxis**:

    ```bash
    sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
    ```

  * **Explicación**:

      * `-p icmp`: Especifica el protocolo ICMP.
      * `--icmp-type echo-request`: Filtra específicamente los mensajes `echo-request` (los que envía `ping`).
      * `-j DROP`: Descarta estos paquetes.

  * **Objetivo**: Bloquear los pings entrantes a la Máquina 1.

  * **Verificación**: Si haces `ping 10.211.55.5` desde la Máquina 2, verás que no hay respuesta.

  * **Comando (Eliminar la regla por posición)**:
    Para revertir el bloqueo, puedes eliminar la regla. Primero, lista las reglas con números de línea:

      * `sudo iptables -L INPUT --line-numbers`
      * Luego, elimina la regla ICMP por su número de línea (ej. si es la línea 1):
      * `sudo iptables -D INPUT 1`
      * **Explicación**: `-D INPUT 1` elimina la regla en la posición 1 de la cadena `INPUT`.
      * **Objetivo**: Revertir el bloqueo de ping.

## 5\. Redireccionar Tráfico de un Puerto a Otro (NAT de Destino)

IPTables permite redirigir el tráfico que llega a un puerto hacia otro puerto, incluso en una máquina diferente. Esto es una forma de **DNAT (Destination NAT)**.

**Escenario**: Redireccionar todo el tráfico TCP que llegue al puerto `8080` de la Máquina 1 (gateway) al puerto `80` de la Máquina 2 (servidor web, IP: `10.211.55.17`).

  * **Comando**: `sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.211.55.17:80`
  * **Sintaxis**:
    ```bash
    sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination 10.211.55.17:80
    ```
  * **Explicación**:
      * `-t nat`: Aplica la regla a la tabla `nat`.
      * `-A PREROUTING`: Añade la regla a la cadena `PREROUTING`, que se aplica *antes* de que se realice el enrutamiento. Esto permite modificar el destino de un paquete antes de que el kernel decida a dónde enviarlo.
      * `-p tcp`: Protocolo TCP.
      * `--dport 8080`: Tráfico con puerto de destino 8080.
      * `-j DNAT`: La acción `DNAT` (Destination NAT) reescribe la dirección IP de destino del paquete.
      * `--to-destination 10.211.55.17:80`: Especifica la nueva dirección IP de destino (`10.211.55.17`) y el nuevo puerto de destino (`80`).
  * **Objetivo**: Redireccionar el tráfico del puerto 8080 de la Máquina 1 al puerto 80 de la Máquina 2.

## 6\. Implementar una DMZ (Zona Desmilitarizada) con IPTables

Una **DMZ (Demilitarized Zone)** es una zona de red que actúa como búfer entre una red interna y una red externa (Internet), utilizada para alojar servicios públicos mientras se mantienen seguros los recursos internos. Aquí, la Máquina 1 (gateway) controlará el acceso a la Máquina 2 (servidor web en la DMZ).

### 6.1. Habilitar Masquerading (NAT) en el Gateway (Máquina 1)

Esto ya lo hicimos en la sección de compartir Internet, pero es un paso fundamental para la DMZ.

  * **Comando**: `sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE`
  * **Sintaxis**:
    ```bash
    sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    ```
  * **Explicación**: Configura la Máquina 1 para enmascarar las IPs internas de los paquetes salientes, haciendo que parezcan originarse desde la Máquina 1.

### 6.2. Configurar Reglas de Firewall para la DMZ en el Gateway (Máquina 1)

El objetivo es permitir solo el tráfico HTTP (puerto 80) hacia el servidor web en la DMZ (Máquina 2) y bloquear todo lo demás.

  * **Comando (Permitir tráfico HTTP hacia el servidor web en DMZ)**:

    ```bash
    sudo iptables -A FORWARD -p tcp --dport 80 -d 10.211.55.17 -j ACCEPT
    ```

  * **Sintaxis**:

    ```bash
    sudo iptables -A FORWARD -p tcp --dport 80 -d 10.211.55.17 -j ACCEPT
    ```

  * **Explicación**:

      * `-A FORWARD`: Añade la regla a la cadena `FORWARD`, que maneja el tráfico que atraviesa el firewall (de Internet a la DMZ).
      * `-p tcp --dport 80`: Especifica tráfico TCP al puerto 80 (HTTP).
      * `-d 10.211.55.17`: El destino es la IP del servidor web en la DMZ (Máquina 2).
      * `-j ACCEPT`: Permite este tráfico.

  * **Objetivo**: Permitir que las solicitudes HTTP desde Internet lleguen al servidor web en la DMZ.

  * **Comando (Bloquear todo lo demás hacia la DMZ)**:

    ```bash
    sudo iptables -A FORWARD -d 10.211.55.17 -j DROP
    ```

  * **Sintaxis**:

    ```bash
    sudo iptables -A FORWARD -d 10.211.55.17 -j DROP
    ```

  * **Explicación**:

      * `-d 10.211.55.17`: Todos los paquetes destinados a la Máquina 2.
      * `-j DROP`: Serán descartados.
      * **Importancia del Orden**: Esta regla `DROP` debe ir *después* de la regla `ACCEPT` del puerto 80, para que el HTTP sea la excepción.

  * **Objetivo**: Bloquear cualquier otro tipo de tráfico no deseado hacia el servidor en la DMZ (ej. SSH, FTP, etc.).

  * **Comando (Bloquear todo el tráfico saliente desde la DMZ hacia la red interna)**:

    ```bash
    sudo iptables -A FORWARD -s 10.211.55.17 -j DROP
    ```

  * **Sintaxis**:

    ```bash
    sudo iptables -A FORWARD -s 10.211.55.17 -j DROP
    ```

  * **Explicación**:

      * `-s 10.211.55.17`: Todos los paquetes originados desde la Máquina 2.
      * `-j DROP`: Serán descartados.

  * **Objetivo**: Impedir que el servidor en la DMZ inicie conexiones hacia la red interna (lo que es una práctica de seguridad clave para DMZs).

### 6.3. Prueba de la DMZ

1.  **Levantar un Servidor Web Simple en la Máquina 2 (DMZ)**:

      * **Comando**: `sudo python3 -m http.server 80`
      * **Sintaxis**:
        ```bash
        sudo python3 -m http.server 80
        ```
      * **Explicación**: Inicia un servidor web básico en Python 3 en el puerto 80, sirviendo los archivos del directorio actual.
      * **Objetivo**: Simular un servicio web accesible públicamente en la DMZ.

2.  **Acceder al Servidor Web desde la Máquina 1 (o externa)**:

      * **Comando (usando `curl`)**: `curl http://10.211.55.17`
      * **Sintaxis**:
        ```bash
        curl http://10.211.55.17
        ```
      * **Explicación**: `curl` es una herramienta de línea de comandos para transferir datos con URL. Intenta acceder al servidor web en la Máquina 2.
      * **Objetivo**: Verificar que el tráfico HTTP está permitido a la DMZ.
      * **Resultado**: Deberías ver el listado de directorios del servidor web, confirmando el acceso.

3.  **Probar Acceso SSH (Bloqueado)**:

      * **Comando**: `ssh user@10.211.55.17`
      * **Sintaxis**:
        ```bash
        ssh user@10.211.55.17
        ```
      * **Explicación**: Intenta una conexión SSH al servidor en la DMZ.
      * **Objetivo**: Confirmar que otros protocolos (como SSH) están bloqueados hacia la DMZ.
      * **Resultado**: Verás "Connection refused" o "Connection timed out", confirmando que SSH está bloqueado por las reglas `DROP`.

## Conclusión

IPTables demuestra ser una herramienta increíblemente potente y granular para el control de red. Ofrece un filtrado de paquetes muy detallado y mecanismos de enrutamiento sofisticados, lo que lo convierte en un pilar fundamental para la seguridad avanzada de redes y la optimización del rendimiento. Su gran adaptabilidad a cualquier tipo de arquitectura de red lo hace indispensable para securizar infraestructuras, mitigar una gran variedad de amenazas asociadas a la red y evitar accesos no autorizados. El conocimiento profundo de IPTables es una habilidad valiosa para cualquier profesional de ciberseguridad.