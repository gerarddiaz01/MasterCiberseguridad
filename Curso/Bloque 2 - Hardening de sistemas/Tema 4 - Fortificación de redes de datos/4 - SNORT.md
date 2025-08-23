# Uso de Snort: Monitorización, Detección y Prevención de Intrusiones

Snort es un sistema de código abierto versátil que combina las funcionalidades de un **Intrusion Detection System (IDS)**, un **Network Intrusion Detection System (NIDS)** y un **Intrusion Prevention System (IPS)**. Permite registrar alertas y ataques de todo tipo, siendo una herramienta fundamental para la monitorización, detección y prevención de intrusiones. Una de sus características más potentes es su sofisticado sistema de gestión de reglas, que permite crear filtros personalizados para detectar una amplia gama de amenazas, como ataques de denegación de servicio distribuido (**DDoS**), escaneos con **Nmap** y **backdoors**. Además de su función como NIDS, Snort puede operar en modo **sniffer** o **packet logger**, lo que permite crear registros detallados a nivel de paquete.

La base de datos de firmas y tipos de ataques de Snort se actualiza constantemente a través de Internet, lo que garantiza una alta fiabilidad y resiliencia ante amenazas recientes.

## Instalación y Configuración Básica de Snort

El primer paso para utilizar Snort es su instalación. Se realiza en un entorno Linux a través del gestor de paquetes `apt`.

### Comandos de Instalación

1.  **Actualizar la lista de paquetes:**

    ```bash
    sudo apt update
    ```

    Este comando actualiza el índice de paquetes disponibles en los repositorios, asegurando que se obtengan las versiones más recientes de los paquetes.

2.  **Instalar Snort:**

    ```bash
    sudo apt install snort
    ```

    Este comando descarga e instala el paquete `snort` y todas sus dependencias. Durante la instalación, un asistente de configuración pedirá información esencial.

      * **Interfaz de red:** Se debe especificar la interfaz de red que Snort monitorizará. Por defecto, suele ser `eth0` o similar. Es crucial conocer las interfaces del sistema para elegir la correcta.
      * **Subred (CIDR):** El asistente solicitará la subred en la que Snort debe operar, por ejemplo `10.211.55.0/24`. Esta configuración define la `HOME_NET`, la red a proteger.

### Verificación de la Instalación

Una vez instalado, es importante verificar que Snort se haya configurado correctamente y que no haya errores de sintaxis en el archivo de configuración.

1.  **Verificar la versión de Snort:**

    ```bash
    snort --version
    ```

    Este comando muestra la versión de Snort instalada, confirmando que la instalación se realizó con éxito.

2.  **Probar la configuración:**

    ```bash
    sudo snort -A console -q -c /etc/snort/snort.conf -i eth0 -T
    ```

    Este comando es una prueba de configuración que verifica la sintaxis de las reglas y el archivo de configuración sin ejecutar realmente el sistema de detección.

      * `-A console`: Muestra las alertas y mensajes en la consola.
      * `-q`: Ejecuta Snort en modo silencioso, minimizando la salida de mensajes innecesarios.
      * `-c /etc/snort/snort.conf`: Especifica la ruta del archivo de configuración principal de Snort.
      * `-i eth0`: Designa la interfaz de red (`eth0` en este caso) a monitorizar.
      * `-T`: Es el parámetro que indica que se realice una prueba de configuración.

### Modificación del Archivo de Configuración

Para personalizar el funcionamiento de Snort, se puede editar el archivo de configuración `snort.conf`.

1.  **Editar el archivo `snort.conf`:**
    ```bash
    sudo nano /etc/snort/snort.conf
    ```
    Dentro de este archivo, se puede modificar la variable `HOME_NET`. Por defecto, podría estar configurada como `any`, lo que hace que Snort escanee toda la red. Para centrar la monitorización en un host específico (como un **HIDS**), se debe cambiar `any` por la dirección IP de la máquina a proteger.
      * `ipvar HOME_NET 10.211.55.5`
      * Esta modificación restringe el escaneo a la IP `10.211.55.5`, lo que es ideal para proteger un servidor específico.

### Permisos de Directorios

Es fundamental asegurarse de que Snort tenga los permisos adecuados para acceder, leer y escribir en sus directorios de configuración y de logs.

1.  **Modificar permisos de directorios:**
    ```bash
    sudo chmod 5775 /etc/snort/
    sudo chmod -R 5775 /var/log/snort
    ```
      * `chmod`: Es el comando para cambiar los permisos de archivos y directorios.
      * `-R`: La opción recursiva se utiliza para aplicar los permisos a todos los archivos y subdirectorios dentro del directorio de logs.
      * `5775`: Es el código de permisos que se asigna.

## Sintaxis de Reglas de Snort

Las reglas son la clave del funcionamiento de Snort, ya que definen qué actividades se deben monitorizar y qué acción tomar. Snort ya incluye un conjunto de reglas predefinidas, pero también permite la creación de reglas personalizadas.

Una regla de Snort tiene la siguiente estructura:

`acción protocolo origen_ip origen_puerto -> destino_ip destino_puerto (opciones)`

| Componente | Descripción |
| :--- | :--- |
| **`acción`** | Define la acción que se tomará si la regla coincide con un paquete. Ejemplos: `alert` (genera una alerta), `log` (registra el paquete), `pass` (ignora el paquete). |
| **`protocolo`** | Especifica el protocolo de red a inspeccionar. Ejemplos: `tcp`, `udp`, `icmp`, `ip`. |
| **`origen_ip`** | Dirección IP de origen del tráfico. Puede ser una IP específica, una variable de red como `EXTERNAL_NET` (cualquier red externa) o `any` (cualquier dirección). |
| **`origen_puerto`** | Puerto de origen. Puede ser un puerto específico, un rango o `any` (cualquier puerto). |
| **`->`** | Indica la dirección del tráfico. |
| **`destino_ip`** | Dirección IP de destino del tráfico. Puede ser una IP específica o una variable como `HOME_NET` (la red protegida). |
| **`destino_puerto`** | Puerto de destino. Puede ser un puerto específico, un rango o `any`. |
| **`(opciones)`** | Contiene información detallada sobre la regla, como el mensaje de la alerta, el tipo de clasificación, la firma y el ID de la regla. |

### Ejemplo de una regla de Snort para detectar pings de Nmap

`alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"ICMP PING Nmap"; dsize:0; itype:8; reference:arachnids,162; classtype:attempted-recon; sid:1; rev:3;)`

  * `alert`: La acción es generar una alerta.
  * `icmp`: El protocolo es ICMP (el utilizado por `ping`).
  * `$EXTERNAL_NET any -> $HOME_NET any`: El tráfico proviene de cualquier IP externa, a cualquier puerto, y se dirige a cualquier IP de la red protegida, a cualquier puerto.
  * `msg:"ICMP PING Nmap";`: El mensaje de la alerta es "ICMP PING Nmap".
  * `dsize:0`: El tamaño del datagrama ICMP es de 0 bytes.
  * `itype:8`: El tipo de mensaje ICMP es 8, que corresponde a un **echo request** (`ping`).
  * `reference:arachnids,162`: Proporciona una referencia a una base de datos de amenazas.
  * `classtype:attempted-recon`: Clasifica la regla como un intento de reconocimiento (**reconnaissance**).
  * `sid:1`: El **Signature ID** es `1`. Cada regla tiene un SID único.
  * `rev:3`: La revisión de la regla es `3`.

## Pruebas de Detección de Intrusiones con Snort

A continuación, se detallan las pruebas realizadas para demostrar la capacidad de Snort como sistema de detección.

### 1\. Detección de Pings (ICMP)

La primera prueba consiste en detectar paquetes ICMP enviados desde una máquina atacante hacia la máquina protegida.

1.  **Ejecutar Snort en modo consola:**

    ```bash
    sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
    ```

    Este comando ejecuta Snort en modo de detección, mostrando las alertas directamente en la terminal.

2.  **Lanzar un `ping` desde la máquina atacante:**

    ```bash
    ping <IP_SERVIDOR>
    ```

    Snort detectará el tráfico ICMP y mostrará una alerta en la consola del servidor, indicando la dirección IP de origen y la de destino. Esto demuestra su capacidad para detectar actividades de reconocimiento en la fase de descubrimiento.

### 2\. Detección de un Ataque de Denegación de Servicio (DoS) con Hping3

Se simula un ataque de **Denial of Service (DoS)** enviando una gran cantidad de peticiones ICMP al servidor para saturarlo.

1.  **Instalar `hping3` en la máquina atacante:**

    ````bash
    sudo apt install hping3
    ```hping3` es una herramienta que permite crear y enviar paquetes personalizados, ideal para simular ataques.

    ````

2.  **Lanzar el ataque desde la máquina atacante:**

    ```bash
    sudo hping3 -c 5 -i 10000 -1 10.211.55.5
    ```

      * `-c 5`: Envía 5 paquetes.
      * `-i 10000`: Establece un intervalo de 10,000 microsegundos (10 ms) entre paquetes.
      * `-1`: Especifica que se envíen paquetes ICMP de tipo 8 (echo request, como un `ping`).
      * `10.211.55.5`: Es la dirección IP del servidor objetivo.

3.  **Observar el resultado en Snort:**
    Snort en el servidor detecta los 5 paquetes ICMP enviados por `hping3` y genera alertas por cada uno, demostrando su capacidad para identificar y alertar sobre intentos de saturación de red.

### 3\. Detección de un Escaneo de Puertos con Nmap

Se realiza un escaneo de puertos desde la máquina atacante para ver cómo Snort reacciona.

1.  **Lanzar el escaneo desde la máquina atacante:**

    ```bash
    nmap -p- 10.211.55.5
    ```

    Este comando realiza un escaneo a todos los puertos del servidor (`10.211.55.5`).

2.  **Observar el resultado en Snort:**
    Snort detecta los intentos de conexión de `Nmap` y genera alertas que indican la actividad sospechosa, aunque `Nmap` no se muestre directamente en el mensaje. Snort identifica los patrones de tráfico utilizados por `Nmap` para intentar obtener información del sistema.

## Creación de Reglas Personalizadas

Snort permite a los usuarios crear sus propias reglas para detectar amenazas muy específicas. Es importante que los **Signature IDs (SID)** de las reglas personalizadas comiencen a partir del número `1,000,000` para evitar conflictos con las reglas predefinidas.

### Pasos para crear una regla SSH personalizada

1.  **Crear un archivo de reglas:**

    ```bash
    sudo nano /etc/snort/rules/ssh-new.rules
    ```

    Se crea un archivo de texto con la extensión `.rules` en el directorio de reglas de Snort.

2.  **Escribir la regla en el archivo:**

    ```bash
    alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (msg:"OJO: Prueba de intento SSH"; flow:stateless; flags:S; sid:1000001; rev:1;)
    ```

      * `alert tcp`: Genera una alerta para el protocolo TCP.
      * `$EXTERNAL_NET any -> $HOME_NET 22`: El tráfico viene de cualquier IP externa, a cualquier puerto, y se dirige a la red protegida en el puerto 22, el puerto estándar de SSH.
      * `msg:"OJO: Prueba de intento SSH";`: Mensaje personalizado de la alerta.
      * `flow:stateless`: Se aplica a sesiones que no han sido establecidas, es decir, solo se detecta el intento de conexión inicial.
      * `flags:S`: La regla se activará al detectar un paquete TCP con el **flag SYN** establecido, indicando un inicio de conexión.
      * `sid:1000001`: Se asigna un SID único.
      * `rev:1`: La revisión de la regla es `1`.

3.  **Incluir la nueva regla en el archivo de configuración:**
    Se debe editar el archivo `snort.conf` y añadir la nueva regla.

    ```bash
    sudo nano /etc/snort/snort.conf
    ```

    Se busca la sección `site specific rules` y se añade la ruta del nuevo archivo.

      * `include $RULE_PATH/ssh-new.rules`

4.  **Lanzar una conexión SSH desde la máquina atacante:**

    ```bash
    ssh 10.211.55.5
    ```

    Snort detectará el intento de conexión y mostrará el mensaje personalizado en la consola, confirmando que la regla ha sido activada con éxito.

## Gestión y Análisis de Logs de Snort

La gestión de logs es una parte crucial del uso de Snort, ya que los logs son la clave para el éxito en la detección de amenazas.

### Ubicación de los Logs

Los logs de Snort se almacenan en el directorio `/var/log/snort/`.

1.  **Acceder al directorio:**
    ```bash
    cd /var/log/snort/
    ```

### Visualización de los Logs

Los logs de Snort son archivos binarios, por lo que no se pueden leer directamente con comandos como `cat`. Se necesita una herramienta específica para visualizarlos en un formato legible.

1.  **Leer el log con `u2spewfoo`:**
    ```bash
    u2spewfoo snort.log
    ```
    Esta herramienta, incluida con Snort, convierte el archivo binario `snort.log` en un formato legible que muestra un nivel de detalle minucioso sobre cada paquete y evento registrado, incluyendo `flags`, protocolos y el contenido del paquete.

En conclusión, Snort destaca por ser un sistema altamente configurable y flexible, tanto a nivel de reglas como de actuación. Su exhaustivo control de registro de eventos facilita un análisis completo y un seguimiento detallado de todo tipo de eventos de seguridad.