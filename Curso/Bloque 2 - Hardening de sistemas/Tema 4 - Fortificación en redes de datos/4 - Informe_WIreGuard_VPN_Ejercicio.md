# Informe de Ejercicio: Configuración Exitosa de VPN WireGuard en un Entorno Virtual

## 1\. Contexto del Laboratorio Virtual y Conectividad Inicial

Para este ejercicio práctico de configuración de una **VPN (Virtual Private Network)** con **WireGuard**, hemos utilizado un entorno de máquinas virtuales que simula una red corporativa interna con acceso a Internet.

  * **Máquina Servidor WireGuard**: Tu máquina **Ubuntu Desktop**, con dirección IP **`192.168.1.103`** en la red interna.
  * **Máquina Cliente WireGuard**: Tu máquina **Kali Linux**, con dirección IP **`192.168.1.104`** en la red interna.

Ambas máquinas virtuales están conectadas a una **Red Interna (`intnet`)** gestionada por una máquina virtual **pfSense**.

### 1.1. Ventajas de la Arquitectura de Red con pfSense y `intnet`

La decisión de conectar Ubuntu Desktop y Kali Linux únicamente a la `intnet` gestionada por pfSense (en lugar de usar configuraciones de doble adaptador como NAT + Internal Network en cada VM) fue crucial por varias razones:

  * **Asignación de IPs Únicas y Sin Conflictos**: El servidor DHCP de pfSense en la `intnet` asigna direcciones IP únicas a cada máquina virtual, eliminando el riesgo de conflictos de IP que ocurren con frecuencia cuando múltiples VMs se conectan a la misma red NAT básica de VirtualBox y obtienen la misma dirección. Esto garantiza una base de red estable y predecible.
  * **Control Centralizado del Enrutamiento y DNS**: pfSense actúa como el **gateway** (puerta de enlace) y el servidor **DNS** para toda la `intnet`. Esto simplifica la configuración de las VMs cliente, ya que obtienen automáticamente la ruta a Internet y los servidores DNS correctos a través de DHCP.
  * **Simulación de un Entorno Realista**: Una `intnet` gestionada por un firewall/router como pfSense es una simulación mucho más precisa de una red corporativa real, donde todos los dispositivos internos se conectan a través de un único punto de acceso seguro a Internet.
  * **Mayor Flexibilidad para Seguridad**: Tener pfSense permite implementar reglas de firewall, proxies y otras características de seguridad que, aunque nos causaron problemas iniciales, son herramientas poderosas para el **hardening de redes** y el control del tráfico, lo cual es muy valioso para futuros ejercicios de ciberseguridad.

### 1.2. Verificación de Conectividad Inicial

Antes de configurar WireGuard, es fundamental asegurarse de que las máquinas tienen conectividad de red básica.

  * **Ping entre VMs**: Realizamos un `ping` entre Ubuntu Desktop y Kali Linux (usando sus IPs de `intnet`). Esto confirmó que podían comunicarse dentro de la red interna.

      * **Comando (ejemplo desde Kali Linux)**: `ping -c 3 192.168.1.103`
      * **Explicación**: El comando `ping` envía pequeños paquetes de prueba (`ICMP Echo Request`) a la dirección IP especificada y espera respuestas (`ICMP Echo Reply`). `-c 3` limita el número de paquetes a 3.
      * **Objetivo**: Verificar la conectividad de Capa 3 (IP) entre las dos máquinas en la misma subred.
      * **Resultado**: Los pings fueron exitosos (0% packet loss), confirmando la comunicación.

  * **Ping a Internet (IP)**: Luego, se verificó la conectividad a Internet por IP.

      * **Comando (ejemplo desde Kali Linux)**: `ping -c 3 8.8.8.8`
      * **Explicación**: Se hace ping a un servidor DNS público conocido (Google DNS) por su dirección IP.
      * **Objetivo**: Confirmar que las máquinas pueden alcanzar destinos en Internet a nivel de IP, pasando por pfSense.
      * **Resultado**: Exitoso.

  * **Ping a Internet (Dominio)**: Finalmente, se probó la resolución de nombres y el acceso a Internet por dominio.

      * **Comando (ejemplo desde Kali Linux)**: `ping -c 3 google.com`
      * **Explicación**: Se hace ping a un dominio, lo que requiere que el sistema resuelva el nombre del dominio a una dirección IP usando los servidores DNS configurados.
      * **Objetivo**: Confirmar que la resolución DNS y la conectividad a Internet funcionan correctamente.
      * **Resultado**: Exitoso.

  * **Preparación para Descarga de WireGuard**: Una vez confirmada la conectividad a Internet, procedimos a actualizar los repositorios de paquetes y a instalar WireGuard en ambas máquinas.

      * **Comando (actualizar repositorios)**: `sudo apt update`

      * **Explicación**: Este comando descarga los últimos índices de paquetes de los repositorios configurados en el sistema. Es crucial para obtener información sobre el software más reciente y las actualizaciones de seguridad.

      * **Objetivo**: Preparar el sistema para instalar software.

      * **Resultado**: Exitoso, una vez que se solucionaron los problemas de intercepción SSL de Squid Proxy en pfSense.

      * **Comando (instalar WireGuard)**: `sudo apt install wireguard`

      * **Explicación**: Este comando descarga e instala el paquete `wireguard` y sus herramientas (`wireguard-tools`).

      * **Objetivo**: Instalar el software WireGuard, necesario para crear el túnel VPN.

      * **Resultado**: Exitoso en ambas máquinas.

## 2\. Generación de Claves Criptográficas

Cada extremo de la conexión WireGuard necesita un par único de claves (una privada y una pública) para la autenticación y el cifrado de la comunicación.

**Claves Generadas (¡Verificadas y Correctas\!):**

| Máquina            | Rol       | Clave Privada (¡Mantener secreta\!)                                   | Clave Pública (¡Compartir con el par\!)                                    |
| :----------------- | :-------- | :------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| **Ubuntu Desktop** | Servidor  | `yWJeTkchQMHLTNAl08E5KX7AzcbMgjNlU8eU5WLpLpVIC=` | `HCt7FAQ4QQu8iqYCBWguZe5JhpICyMNkAgguOBUx+6j0=` |
| **Kali Linux** | Cliente   | `CWHhNIjQIyanWM4LZ3cBH83WNzjTtnb9tGz6VjJbnCIs=`    | `cVYCZRFFr8RWGKBPNWQCFOw7FT5LWtE8OrPZITObIw=` |

### 2.1. Proceso de Generación de Claves y Depuración

La generación de claves se realizó en **ambas máquinas**.

1.  **Primer Intento (fallido)**:

      * **Comando Propuesto**: `wg genkey | tee privatekey && wg pubkey > publickey`
      * **Explicación del Fallo**: Este comando intentaba generar la clave privada, mostrarla y guardarla en `privatekey` (`tee privatekey`), y luego generar la clave pública a partir de ella y guardarla en `publickey` (encadenado con `&&`). Sin embargo, el comando se quedaba `parado` o `suspendido` después de generar la clave privada, lo que provocaba que el archivo `publickey` quedara vacío o no se creara. Esto fue un problema de cómo el shell manejaba la secuencia de comandos en ese entorno específico.
      * **Importancia de este error para el futuro**: Si te encuentras con un comando que se `suspende` o se `congela` después de una parte, y estás usando `pipes` (`|`) o encadenamientos (`&&`), considera que el problema podría ser de sincronización o que el shell no está completando el proceso correctamente.
      * **Revisando el error creo que si hacemos** `wg genkey | tee privatekey | wg pubkey > publickey` hubiese funcionado, hay que probar.

2.  **Segundo Intento (Exitoso: Paso a Paso)**:
    Para solucionar el problema de la congelación, se optó por un método más robusto y secuencial:

      * **Comando 1 (Generar clave privada)**: `wg genkey > privatekey`

          * **Sintaxis**:
            ```bash
            wg genkey > privatekey
            ```
          * **Explicación**: `wg genkey` genera una clave privada y el símbolo `>` redirige su salida directamente al archivo `privatekey`. Esto asegura que la clave privada se guarde de forma aislada.
          * **Objetivo**: Crear el archivo `privatekey` con la clave privada de la máquina actual.

      * **Comando 2 (Generar clave pública a partir de la privada)**: `wg pubkey < privatekey > publickey`

          * **Sintaxis**:
            ```bash
            wg pubkey < privatekey > publickey
            ```
          * **Explicación**: `wg pubkey` lee la clave privada del archivo `privatekey` (indicado por `< privatekey`) y genera la clave pública. Luego, la salida de `wg pubkey` se redirige (`>`) al archivo `publickey`.
          * **Objetivo**: Crear el archivo `publickey` con la clave pública correspondiente.

      * **Verificación**: Con `cat privatekey` y `cat publickey`, se confirmó que ambos archivos contenían las claves correctamente generadas en ambas máquinas.

## 3\. Configuración del Túnel VPN (Creación de los archivos `wg0.conf`)

La configuración de WireGuard se realiza a través de archivos de texto plano que definen las interfaces virtuales, las claves y los pares con los que se comunicará. Ambos extremos del túnel necesitan un archivo de configuración que tenemos que crear nosotros y escoger el nombre, aqui hemos utilziado `wg0`.

### 3.1. Archivo de Configuración del Servidor WireGuard (Ubuntu Desktop)

  * **Comando**: `sudo nano /etc/wireguard/wg0.conf`
  * **Ubicación**: `/etc/wireguard/wg0.conf`
  * **Contenido (¡Validado y Correcto\!)**:
    ```ini
    [Interface]
    Address = 10.0.0.1/24       # IP del servidor dentro del túnel VPN.
    SaveConfig = true           # Guardar automáticamente los cambios dinámicos en el archivo.
    PrivateKey = yWJeTkchQMHLTNAl08E5KX7AzcbMgjNlU8eU5WLpLpVIC= # Clave privada de Ubuntu Desktop.
    ListenPort = 51820          # Puerto UDP en el que el servidor escuchará conexiones.

    [Peer]
    PublicKey = cVYCZRFFr8RWGKBPNWQCFOw7FT5LWtE8OrPZITObIw=  # Clave pública de Kali Linux (cliente).
    AllowedIPs = 10.0.0.2/32    # Permite tráfico para la IP del cliente (10.0.0.2) a través de este peer.
    ```
  * **Explicación**:
      * `[Interface]`: Define la configuración del lado del servidor del túnel.
          * `Address = 10.0.0.1/24`: Asigna la IP `10.0.0.1` a la interfaz virtual `wg0` del servidor. Hemos elegido el rango `10.0.0.0/24` para el túnel VPN porque es un **rango de IP privado** comúnmente utilizado para redes internas o VPNs, lo que evita conflictos con redes locales existentes (como la `192.168.1.x` que ya tenemos) y lo hace fácil de recordar. `10.0.0.1` es la primera IP asignable en esa subred.
          * `SaveConfig = true`: Garantiza que cualquier cambio realizado a la configuración de WireGuard mientras está activo se guarde automáticamente.
          * `PrivateKey`: La clave privada generada para la máquina Ubuntu Desktop.
          * `ListenPort = 51820`: El puerto UDP en el que el servidor WireGuard estará escuchando las conexiones entrantes de los clientes. `51820` es el puerto estándar de WireGuard.
      * `[Peer]`: Define la configuración para cada cliente que se conectará al servidor.
          * `PublicKey`: La clave pública del cliente (Kali Linux). WireGuard utiliza este par de claves públicas para autenticar la conexión.
          * `AllowedIPs = 10.0.0.2/32`: Indica al servidor que cualquier tráfico con destino a la IP `10.0.0.2` (la IP del túnel del cliente) debe ser enrutado a través de este peer. El `/32` indica una única IP específica.

### 3.2. Archivo de Configuración del Cliente WireGuard (Kali Linux)

  * **Comando**: `sudo nano /etc/wireguard/wg0.conf`
  * **Ubicación**: `/etc/wireguard/wg0.conf`
  * **Contenido (¡Validado y Correcto\!)**:
    ```ini
    [Interface]
    Address = 10.0.0.2/24       # IP del cliente dentro del túnel VPN.
    PrivateKey = CWHhNIjQIyanWM4LZ3cBH83WNzjTtnb9tGz6VjJbnCIs= # Clave privada de Kali Linux.

    [Peer]
    PublicKey = HCt7FAQ4QQu8iqYCBWguZe5JhpICyMNkAgguOBUx+6j0== # Clave pública de Ubuntu Desktop (servidor).
    Endpoint = 192.168.1.103:51820 # IP de Ubuntu Desktop en la red intnet (servidor VPN):Puerto de escucha.
    AllowedIPs = 10.0.0.0/24    # Rutea todo el tráfico de la red 10.0.0.0/24 a través del túnel VPN.
    PersistentKeepalive = 25    # Envía paquetes cada 25 segundos para mantener la conexión.
    ```
  * **Explicación**:
      * `[Interface]`: Define la configuración del lado del cliente del túnel.
          * `Address = 10.0.0.2/24`: Asigna la IP `10.0.0.2` a la interfaz virtual `wg0` del cliente. `10.0.0.2` es la siguiente IP asignable en la subred `10.0.0.0/24`.
          * `PrivateKey`: La clave privada generada para la máquina Kali Linux.
      * `[Peer]`: Define la configuración para conectarse al servidor.
          * `PublicKey`: La clave pública del servidor (Ubuntu Desktop).
          * `Endpoint = 192.168.1.103:51820`: Esta es la dirección IP de la máquina Ubuntu Desktop en la red `intnet` (`192.168.1.103`) y el puerto UDP (`51820`) del servidor WireGuard al que el cliente intentará conectarse. Esta es la IP "real" o subyacente para establecer el túnel.
          * `AllowedIPs = 10.0.0.0/24`: Le dice al cliente que cualquier tráfico destinado a la red `10.0.0.0/24` (que es la red del túnel) debe ser enrutado a través de esta conexión VPN. Esto es crucial para que el cliente pueda comunicarse con el servidor a través del túnel.
          * `PersistentKeepalive = 25`: Envía paquetes de mantenimiento ("keepalive") cada 25 segundos. Esto es útil para mantener la conexión activa, especialmente si hay dispositivos NAT o firewalls intermedios que puedan cerrar sesiones inactivas.

## 4\. Configuración del Firewall en el Servidor WireGuard (Ubuntu Desktop)

Para que el cliente pueda iniciar la conexión al servidor WireGuard, el puerto de escucha del servidor (`51820/UDP`) debe estar abierto en su firewall.

1.  **Permitir el tráfico en el puerto de WireGuard**:

      * **Comando**: `sudo ufw allow 51820/udp`
      * **Sintaxis**:
        ```bash
        sudo ufw allow 51820/udp
        ```
      * **Explicación**: Este comando añade una regla al firewall `ufw` de Ubuntu Desktop para permitir las conexiones de entrada (`in`) al puerto `51820` que utilizan el protocolo `UDP`.
      * **Objetivo**: Abrir el puerto necesario en el firewall del servidor para que el cliente pueda contactarlo.

2.  **Habilitar el Firewall (si no estaba ya activo)**:

      * **Comando**: `sudo ufw enable`
      * **Sintaxis**:
        ```bash
        sudo ufw enable
        ```
      * **Explicación**: Este comando activa el servicio del firewall `ufw`. Si ya estaba activo, no hará cambios significativos, solo confirmará su estado.
      * **Objetivo**: Asegurar que el firewall está funcionando y aplicando las reglas de apertura de puerto.

## 5\. Levantar las Interfaces WireGuard

Una vez que las configuraciones de `wg0.conf` están en su lugar y el firewall del servidor está configurado, podemos activar las interfaces WireGuard en ambas máquinas para establecer el túnel.

  * **Comando**: `sudo wg-quick up wg0`
  * **Sintaxis**:
    ```bash
    # En Ubuntu Desktop (Servidor)
    sudo wg-quick up wg0

    # En Kali Linux (Cliente)
    sudo wg-quick up wg0
    ```
  * **Explicación**: El script `wg-quick` lee el archivo de configuración `/etc/wireguard/wg0.conf` para la interfaz `wg0`. Configura la interfaz de red virtual `wg0`, asigna la dirección IP del túnel, establece las claves y configura las rutas necesarias para que el tráfico fluya a través del túnel.
  * **Objetivo**: Activar el túnel VPN WireGuard en ambos extremos.
  * **Errores Comunes en este Paso**: Si los archivos `wg0.conf` tienen errores de sintaxis (ej. un espacio donde no debe ir, una clave mal copiada, un `ListenPort` duplicado) o permisos incorrectos, este comando dará un error. `wg-quick` es muy estricto con el formato.

## 6\. Verificación del Túnel VPN WireGuard

Una vez que las interfaces están levantadas, es crucial verificar que el túnel VPN se ha establecido correctamente.

1.  **Verificar el estado del túnel y del `handshake`**:

      * **Comando**: `sudo wg show`
      * **Sintaxis**:
        ```bash
        sudo wg show
        ```
      * **Explicación**: Este comando es fundamental para diagnosticar el estado del túnel. Muestra información detallada sobre la interfaz `wg0` y sus pares configurados.
          * **`interface: wg0`**: Confirma que la interfaz está activa.
          * **`public key: ...` y `private key: (hidden)`**: Muestra tus claves (la privada oculta).
          * **`listening port: 51820` (servidor) / `5xxxx` (cliente)**: Muestra el puerto de escucha.
          * **`peer: <clave_publica_del_otro_extremo>`**: Identifica el par configurado.
          * **`endpoint: <IP_del_par_en_la_red_fisica>:51820`**: Muestra la dirección a la que se conecta o desde la que se recibe la conexión.
          * **`allowed ips: ...`**: Muestra las IPs que se enrutarán a través de este par.
          * **`latest handshake: <tiempo> seconds ago`**: ¡**Esta es la línea más importante\!** Indica que la autenticación criptográfica entre los dos extremos del túnel se ha completado con éxito y que la conexión VPN está activa. Un tiempo reciente (pocos segundos o minutos) confirma que el túnel está funcionando correctamente.
          * **`transfer: ... received, ... sent`**: Muestra la cantidad de datos que han pasado por el túnel.
      * **Objetivo**: Confirmar que el túnel VPN está establecido a nivel criptográfico y lógico.

2.  **Comprobar la Conectividad a Través del Túnel (Ping)**:
    Finalmente, probamos que el tráfico puede fluir correctamente a través del túnel WireGuard utilizando las IPs virtuales que hemos asignado.

      * **Desde Kali Linux (Cliente - IP del túnel: 10.0.0.2)**:

          * **Comando**: `ping -c 3 10.0.0.1`
          * **Sintaxis**:
            ```bash
            ping -c 3 10.0.0.1
            ```
          * **Explicación**: Se envía un ping a la dirección IP interna del túnel del servidor (Ubuntu Desktop). El tráfico de este ping viajará **cifrado** a través del túnel VPN.
          * **Objetivo**: Confirmar que el tráfico bidireccional dentro del túnel VPN funciona.
          * **Resultado**: Muestra `3 packets transmitted, 3 received, 0% packet loss`, confirmando la comunicación exitosa a través del túnel.

      * **Desde Ubuntu Desktop (Servidor - IP del túnel: 10.0.0.1)**:

          * **Comando**: `ping -c 3 10.0.0.2`
          * **Sintaxis**:
            ```bash
            ping -c 3 10.0.0.2
            ```
          * **Explicación**: Se envía un ping a la dirección IP interna del túnel del cliente (Kali Linux).
          * **Objetivo**: Confirmar la comunicación bidireccional a través del túnel VPN desde el servidor al cliente.
          * **Resultado**: Muestra `3 packets transmitted, 3 received, 0% packet loss`, confirmando la comunicación exitosa.

## 7\. Gestión del Túnel VPN: Desactivar la Interfaz WireGuard

Una vez que el ejercicio ha sido completado y verificado, es una buena práctica saber cómo desactivar la interfaz VPN si no se necesita activada de forma continua.

  * **Comando**: `sudo wg-quick down wg0`
  * **Sintaxis**:
    ```bash
    sudo wg-quick down wg0
    ```
  * **Explicación**: Este comando lee el archivo `/etc/wireguard/wg0.conf` y deshace la configuración que `wg-quick up wg0` había aplicado. Desactiva la interfaz de red virtual `wg0`, elimina sus direcciones IP y las rutas asociadas.
  * **Objetivo**: Desactivar el túnel VPN WireGuard y liberar los recursos asociados.
  * **Consideraciones para el futuro**:
      * **Liberación de Recursos**: Desactivar el túnel libera los pequeños recursos del sistema que consume.
      * **Seguridad**: Si no necesitas el túnel VPN, es mejor desactivarlo. Aunque WireGuard es muy seguro, una interfaz de red activa es siempre un punto de exposición.
      * **Evitar Conflictos**: Si futuros ejercicios de red utilizan los mismos rangos de IP (`10.0.0.x`) o requieren configuraciones de red específicas que puedan entrar en conflicto con el túnel WireGuard, desactivarlo previene problemas.
      * **Facilidad de Reactivación**: Reactivar el túnel es tan sencillo como volver a ejecutar `sudo wg-quick up wg0`.
