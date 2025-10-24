# La Capa de Aplicación: Interfaz con el Usuario y Protocolos Clave (HTTP, DNS, FTP)

La **Capa de Aplicación** es la capa superior en los modelos de red TCP/IP y OSI, sirviendo como la interfaz directa entre las aplicaciones del usuario y los servicios de red subyacentes. Su función principal es proporcionar a las aplicaciones (ya sean de usuario o de sistema) la capacidad de acceder a los servicios de las demás capas y definir los protocolos que estas aplicaciones utilizan para intercambiar datos.

El usuario, por lo general, no interactúa directamente con esta capa en su nivel más bajo (ej., no envía peticiones GET manualmente), sino que lo hace a través de programas (como navegadores web o clientes de correo) que ocultan la complejidad subyacente.

## 1\. La Capa de Aplicación en TCP/IP vs. OSI

Existe una diferencia notable en cómo la capa de aplicación es conceptualizada en ambos modelos:

  * **Modelo TCP/IP:** La Capa de Aplicación es un **único estrato** o nivel que combina las funciones de las tres capas superiores del modelo OSI.
  * **Modelo OSI:** La capa de aplicación se divide en tres capas distintas:
      * **Capa de Aplicación (Application Layer):** Se limita estrictamente a proporcionar la interfaz entre el *software* de aplicación y las capas inferiores del modelo.
      * **Capa de Presentación (Presentation Layer):** Se encarga de tareas específicas como la **representación de los datos** (formato, cifrado, compresión), asegurando que los datos se presenten en un formato que la aplicación pueda entender.
      * **Capa de Sesión (Session Layer):** Se encarga del **mantenimiento de la comunicación** entre aplicaciones, estableciendo, gestionando y terminando sesiones de diálogo.

En el modelo TCP/IP, estas funciones de presentación y sesión se combinan dentro de la Capa de Aplicación para simplificar el modelo.

| Característica                       | Capa de Aplicación (TCP/IP) | Capa de Aplicación (OSI) |
| :----------------------------------- | :-------------------------- | :----------------------- |
| **Número de Capas/Estratos** | 1                           | 3 (Aplicación, Presentación, Sesión) |
| **Representación de Datos** | Combinada en una sola capa  | Capa de Presentación     |
| **Mantenimiento de Comunicación** | Combinada en una sola capa  | Capa de Sesión           |
| **Interfaz con el Software de Aplicación** | Directa                     | Capa de Aplicación       |

### 1.1. Unidad de Datos en la Capa de Aplicación

A diferencia de las capas inferiores donde hablamos de **tramas** (Capa de Enlace), **paquetes** o **datagramas** (Capa de Internet), y **segmentos** (Capa de Transporte), en la Capa de Aplicación, nos referimos principalmente a **datos en términos de mensajes**. Estos mensajes serán posteriormente encapsulados por las capas inferiores para su transmisión.

### 1.2. Principales Protocolos de Aplicación

En esta capa encontramos una multitud de protocolos que son esenciales para el funcionamiento de Internet y las aplicaciones modernas:

  * **HTTP (Hypertext Transfer Protocol):** Protocolo fundamental para transferir datos en la Web.
  * **DNS (Domain Name System):** Sistema para traducir nombres de dominio legibles por humanos (ej., `ejemplo.com`) a direcciones IP numéricas.
  * **FTP (File Transfer Protocol):** Utilizado para transferir archivos entre un cliente y un servidor en una red.
  * **SSH (Secure Shell Protocol):** Permite a los usuarios conectarse de forma segura a un servidor remoto a través de una conexión cifrada.
  * **SMTP (Simple Mail Transfer Protocol):** Estándar para el envío de correos electrónicos entre servidores de correo electrónico a través de Internet.

## 2\. Protocolo HTTP (Hypertext Transfer Protocol)

**HTTP** es el protocolo de transferencia de hipertextos utilizado para acceder a los datos de la Web. Se basa en el protocolo de transporte **TCP**. El cliente inicia una conexión TCP al servidor, el servidor la acepta, se transfieren los mensajes (datos) y, finalmente, la conexión TCP se cierra.

### 2.1. Naturaleza Sin Estado de HTTP

Se dice que HTTP es un **protocolo sin estado** (stateless), lo que significa que el servidor no guarda ninguna información sobre peticiones anteriores de un mismo cliente. Cada petición HTTP se procesa de forma independiente. Para mantener el estado entre peticiones, se utilizan mecanismos adicionales como las *cookies*.

### 2.2. HTTP Persistente vs. No Persistente

Históricamente, HTTP ha evolucionado en cómo maneja las conexiones TCP:

  * **HTTP No Persistente:** En las primeras versiones (ej., HTTP/1.0), se establecía y cerraba una **conexión TCP única para cada objeto** solicitado. Si una página web contenía tres objetos (HTML, imagen, CSS), se requerían tres conexiones TCP separadas (establecer, transferir, cerrar, repetir).

  * **HTTP Persistente:** A partir de HTTP/1.1 y extendiéndose en HTTP/2, se establece la conexión TCP una única vez y se **aprovecha para enviar múltiples objetos** a través de la misma conexión antes de cerrarla. Esto reduce la sobrecarga de establecer y cerrar conexiones repetidamente.

### 2.3. HTTP/3 y QUIC/UDP

Con la versión **HTTP/3**, lanzada en 2022, se abandonó el uso de TCP. En su lugar, HTTP/3 utiliza un protocolo llamado **QUIC** (Quick UDP Internet Connections), desarrollado por Google, que opera sobre **UDP**. Esta transición busca reducir la latencia y mejorar el rendimiento, especialmente en redes inestables.

### 2.4. Métodos de Petición HTTP

HTTP define varios **métodos de petición** (verbos) que indican la acción deseada para un recurso. Los más conocidos son:

| Método  | Descripción                                         | ¿Body en Request? | ¿Body en Response? | RFC Relacionado        |
| :------ | :-------------------------------------------------- | :---------------- | :----------------- | :--------------------- |
| **GET** | Solicita una representación del recurso especificado. | Opcional          | Sí                 | RFC 7231               |
| **POST** | Envía datos para ser procesados a un recurso específico. | Sí                | Sí                 | RFC 7231               |
| **PUT** | Reemplaza todas las representaciones actuales del recurso destino con la carga útil de la petición. | Sí                | Sí                 | RFC 7231               |
| **DELETE** | Elimina el recurso especificado.                    | Opcional          | Sí                 | RFC 7231               |
| **HEAD** | Solicita las cabeceras de un recurso, sin el cuerpo. | Opcional          | No                 | RFC 7231               |
| **OPTIONS** | Solicita los métodos HTTP admitidos por un recurso. | Opcional          | Sí                 | RFC 7231               |
| **PATCH** | Aplica modificaciones parciales a un recurso.       | Sí                | Sí                 | RFC 5789               |

### 2.5. Estructura de una Solicitud y Respuesta HTTP

Una solicitud HTTP y su respuesta se componen de una línea de inicio, cabeceras, una línea en blanco y, opcionalmente, un cuerpo.

**Solicitud HTTP (Request):**

```
GET / HTTP/1.1                <-- Línea de inicio: Método, Recurso, Versión
Host: www.example.com         <-- Cabecera: Nombre de dominio del servidor
User-Agent: Mozilla/5.0
Accept: text/html,...
Accept-Language: en-GB,...
Accept-Encoding: gzip,...
Connection: keep-alive

                      <-- Línea en blanco (separador de cabeceras y cuerpo)
[BODY OPCIONAL]       <-- Cuerpo de la petición (ej. en peticiones POST/PUT)
```

La cabecera `Host` es esencial, ya que indica el nombre de dominio del servidor al que se está solicitando el recurso.

**Respuesta HTTP (Response):**

```
HTTP/1.1 200 OK                     <-- Línea de estado: Versión, Código de estado, Mensaje
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 155
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"        <-- Cabecera ETag
Accept-Ranges: bytes
Connection: close

                      <-- Línea en blanco
<html>                  <-- Cuerpo de la respuesta (ej. documento HTML)
<head>
<title>An Example Page</title>
</head>
<body>
<p>Hello World, this is a very simple HTML document.</p>
</body>
</html>
```

La línea de estado (`HTTP/1.1 200 OK`) es crucial e incluye un **código de estado** que indica el resultado de la petición.

#### 2.5.1. Códigos de Estado HTTP

Los códigos de estado HTTP se agrupan en cinco categorías, indicando si una petición ha sido exitosa o si ha ocurrido algún problema:

  * **1XX (Informacionales):** Indican que la petición ha sido recibida y el proceso continúa.
  * **2XX (Satisfactorias/Successful):** Indican que la petición fue recibida, entendida y aceptada correctamente (ej., `200 OK`).
  * **3XX (Redirecciones):** Indican que se necesita una acción adicional para completar la petición (ej., `301 Moved Permanently`).
  * **4XX (Errores del Cliente/Client Error):** Indican que ha habido un error por parte del cliente al realizar la petición (ej., `404 Not Found`, `403 Forbidden`).
  * **5XX (Errores del Servidor/Server Error):** Indican que el servidor falló al completar una petición aparentemente válida (ej., `500 Internal Server Error`, `503 Service Unavailable`).

La cabecera **ETag** (`Entity Tag`) es un identificador único para el recurso solicitado. Se utiliza para la caché del navegador, indicando si el contenido del servidor ha cambiado desde la última vez que fue descargado. Si el ETag coincide con la versión en caché, el servidor puede responder con un `304 Not Modified`, ahorrando ancho de banda.

### 2.6. Laboratorio Práctico: Servidor HTTP con Flask en Kali Linux

Este laboratorio demuestra cómo levantar un servidor HTTP simple con **Flask** (un microframework de Python) en Kali Linux y cómo interactuar con él usando el comando `curl`.

#### 2.6.1. Configuración del Servidor Flask

El *script* `server.py` define varios *endpoints* para manejar peticiones HTTP:

  * `/add` (método POST): Para añadir datos.
  * `/update/<key>` (método PUT): Para modificar datos existentes.
  * `/get/<key>` (método GET): Para obtener datos por clave.

1.  **Instalar Flask:**

    ```bash
    pip install flask
    ```

      * **Explicación:** `pip` es el instalador de paquetes para Python. Este comando descarga e instala el *framework* Flask y sus dependencias necesarias.
      * **Objetivo:** Preparar el entorno de Python para ejecutar el servidor web.

2.  **Ejecutar el Servidor Flask:**

    ```bash
    python server.py
    ```

      * **Explicación:** Este comando ejecuta el *script* de Python que contiene el servidor Flask.
      * **Objetivo:** Iniciar el servidor HTTP que escuchará peticiones en el puerto predeterminado (por defecto, 5000 para Flask en modo de desarrollo). La salida muestra que el servidor está activo y la dirección en la que escucha (`http://127.0.0.1:5000`).

#### 2.6.2. Interacción con el Servidor HTTP usando `curl`

El comando `curl` es una herramienta versátil de línea de comandos para transferir datos con sintaxis de URL. Es muy potente para realizar peticiones HTTP.

1.  **Añadir datos (Petición POST):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"key": "1", "value": "John Doe"}' http://localhost:5000/add
    ```

      * **`curl`:** El comando principal para realizar peticiones.
      * **`-X POST`:** Especifica que el método HTTP de la petición es **POST**.
      * **`-H "Content-Type: application/json"`:** Añade la cabecera `Content-Type`, indicando al servidor que el cuerpo de la petición está en formato **JSON**.
      * **`-d '{"key": "1", "value": "John Doe"}'`:** Proporciona los datos del cuerpo de la petición. En este caso, un objeto JSON con una clave (`key`) y un valor (`value`).
      * **`http://localhost:5000/add`:** La URL del *endpoint* del servidor al que se envía la petición.
      * **Objetivo:** Enviar datos al servidor para que los almacene, imitando el envío de un formulario o datos de una aplicación. El servidor responde con un mensaje de éxito: `{"message": "Data added successfully"}`.

2.  **Obtener datos (Petición GET):**

    ```bash
    curl http://localhost:5000/get/1
    ```

      * **`curl`:** El comando principal. Si no se especifica `-X`, `curl` utiliza **GET** por defecto.
      * **`http://localhost:5000/get/1`:** La URL del *endpoint* `/get` con la clave `1` como parámetro, indicando qué dato se desea obtener.
      * **Objetivo:** Recuperar el valor asociado a la clave `1` del servidor. La respuesta muestra el dato almacenado: `{"1": "John Doe"}`.

3.  **Modificar datos (Petición PUT):**

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"value": "Jane Doe"}' http://localhost:5000/update/1
    ```

      * **`-X PUT`:** Especifica que el método HTTP es **PUT**.
      * **`-H "Content-Type: application/json"`:** Indica que el cuerpo es JSON.
      * **`-d '{"value": "Jane Doe"}'`:** Proporciona el nuevo valor para la clave.
      * **`http://localhost:5000/update/1`:** El *endpoint* `/update` y la clave `1` del dato a modificar.
      * **Objetivo:** Actualizar el valor asociado a la clave `1`. El servidor responde con `{"message": "Data updated successfully"}`.

4.  **Verificar modificación (Petición GET):**

    ```bash
    curl http://localhost:5000/get/1
    ```

      * **Objetivo:** Comprobar que el dato ha sido actualizado. La respuesta debería ser: `{"1": "Jane Doe"}`.

## 3\. Sistema de Nombres de Dominio (DNS - Domain Name System)

Las personas preferimos utilizar nombres de dominio (ej., `wikipedia.org`) en lugar de direcciones IP numéricas para acceder a recursos en Internet, ya que son más fáciles de recordar. El **DNS** es el sistema que hace posible esta traducción.

### 3.1. Naturaleza Jerárquica y Distribuida de DNS

El DNS es una **base de datos distribuida e implementada en una jerarquía de muchos servidores de nombres**. No es un sistema centralizado, lo que es crucial para evitar un único punto de fallo y enormes latencias si un solo servidor tuviera que manejar todo el tráfico mundial.

El proceso de resolución de un nombre de dominio a una dirección IP sigue una jerarquía:

1.  **Consulta del Cliente (DNS Iterador):** Cuando un usuario escribe un nombre de dominio (ej., `www.wikipedia.org`) en su navegador, el sistema operativo o el *router* local envía una consulta a un **servidor DNS recursivo** (también llamado DNS Iterador o Resolutor).
2.  **Servidor Raíz (Root Nameserver):** Si el servidor recursivo no tiene la información en caché, envía la consulta al **servidor DNS raíz** (ej., `198.41.0.4`). Este es el primer punto de contacto en la jerarquía DNS. El servidor raíz no conoce la IP del dominio final, pero sí las IP de los **servidores TLD** (Top-Level Domain) para cada dominio de nivel superior (ej., `.com`, `.org`, `.net`, `.es`). Responde al servidor recursivo con la dirección de un servidor TLD relevante (ej., "Try 204.74.112.1" para `.org`).
3.  **Servidor TLD (Top-Level Domain Nameserver):** El servidor recursivo consulta al servidor TLD indicado (ej., `204.74.112.1` para `.org`). El servidor TLD conoce la dirección del **servidor DNS autoritativo** para el dominio específico (ej., `wikipedia.org`). Responde al servidor recursivo con la dirección del servidor autoritativo (ej., "Try 207.142.131.234" para `wikipedia.org`).
4.  **Servidor Autoritativo (Authoritative Nameserver):** El servidor recursivo consulta al servidor DNS autoritativo (ej., `207.142.131.234` para `wikipedia.org`). Este servidor es el que contiene el registro DNS final para el nombre de dominio. Responde al servidor recursivo con la dirección IP del servidor web (ej., "It's at xxx.xx.xx.xxx" para `www.wikipedia.org`).
5.  **Caché:** Finalmente, el servidor recursivo envía la dirección IP al cliente. Tanto el servidor recursivo como el navegador del usuario almacenan este registro en **caché** para futuras consultas, acelerando el acceso a sitios web ya visitados.

### 3.2. Tipos de Registros DNS

Los registros DNS son las entradas en los servidores de nombres que proporcionan información sobre los dominios. Aquí algunos de los tipos más comunes:

  * **NS (Name Server Record):** Indica qué servidores de nombres son autorizados para un dominio específico.
      * Ejemplo: `example.com NS ns1.example.com`
  * **A (Address Record):** Asocia un nombre de dominio con una dirección **IPv4** específica.
      * Ejemplo: `example.com A 192.0.2.1`
      * Ejemplo: `www.example.com A 192.0.2.2`
  * **AAAA (IPv6 Address Record):** Asocia un nombre de dominio con una dirección **IPv6** específica.
      * Ejemplo: `example.com AAAA 2001:0db8::1`
  * **CNAME (Canonical Name Record):** Crea un **alias** para un nombre de dominio, apuntando a otro nombre de dominio.
      * Ejemplo: `ftp.example.com CNAME example.com` (ftp.example.com es un alias de example.com)
  * **MX (Mail Exchange Record):** Especifica el servidor de correo responsable de recibir correos electrónicos para un dominio específico, incluyendo una prioridad.
      * Ejemplo: `example.com MX 10 mail.example.com`
  * **TXT (Text Record):** Permite almacenar texto arbitrario. Se utiliza a menudo para políticas de seguridad como **SPF (Sender Policy Framework)** y **DKIM (DomainKeys Identified Mail)** para la validación del dominio.
      * Ejemplo: `_domainkey.example.com TXT "o=~"`
      * Ejemplo: `default._domainkey.example.com TXT "p=..."`

## 4\. Protocolo FTP (File Transfer Protocol)

El **Protocolo FTP** es un estándar de la Capa de Aplicación utilizado para transferir archivos entre un cliente y un servidor en una red. Utiliza los protocolos de la Capa de Transporte **TCP** y de la Capa de Internet **IP**.

### 4.1. Casos de Uso de FTP

  * **Desarrollo de Sitios Web:** Utilizado para subir archivos (HTML, CSS, JavaScript, imágenes) a un servidor web.
  * **Compartición de Archivos:** Permite compartir archivos entre usuarios.
  * **Copias de Seguridad y Almacenamiento:** Utilizado para subir copias de seguridad a servidores remotos.
  * **Distribución de Software y Medios:** Históricamente, las compañías lo usaban para distribuir *software* o actualizaciones al público.

### 4.2. Clientes FTP y Comandos Populares

Existen varios clientes FTP, tanto gráficos (como **FileZilla**, **Cyberduck**, ambos de código abierto y gratuitos) como de línea de comandos.

Los comandos FTP más comunes en la terminal son:

  * **`ls`:** Lista los archivos y directorios en el directorio actual del servidor remoto.
  * **`cd <directorio>`:** Cambia el directorio actual en el servidor remoto.
  * **`pwd`:** Muestra el directorio de trabajo actual en el servidor remoto.
  * **`mkdir <nombre_directorio>`:** Crea un nuevo directorio en el servidor remoto.
  * **`rmdir <nombre_directorio>`:** Elimina un directorio vacío en el servidor remoto.
  * **`get <archivo_remoto> [archivo_local]`:** Descarga un archivo desde el servidor remoto al cliente local.
  * **`put <archivo_local> [archivo_remoto]`:** Sube un archivo desde el cliente local al servidor remoto.
  * **`delete <archivo_remoto>`:** Elimina un archivo en el servidor remoto.
  * **`rename <nombre_antiguo> <nombre_nuevo>`:** Renombra un archivo en el servidor remoto.
  * **`chmod <permisos> <archivo_remoto>`:** Cambia los permisos de un archivo en el servidor remoto.
  * **`quit`:** Cierra la conexión FTP y sale del cliente.
  * **`help`:** Muestra una lista de los comandos FTP disponibles.

### 4.3. Laboratorio Práctico: Servidor FTP en Ubuntu Server y Cliente FTP en Kali Linux

Este laboratorio demuestra cómo configurar un servidor FTP (`vsftpd`) en Ubuntu Server y cómo interactuar con él desde Kali Linux.

#### 4.3.1. Configuración del Servidor FTP en Ubuntu Server

1.  **Instalar el Servidor FTP (`vsftpd`):**

    ```bash
    sudo apt update; sudo apt install vsftpd -y
    ```

      * **`sudo apt update`:** Actualiza la lista de paquetes disponibles en los repositorios de Ubuntu.
      * **`sudo apt install vsftpd -y`:** Instala el paquete `vsftpd` (Very Secure FTP Daemon), que es un servidor FTP. La opción `-y` confirma automáticamente cualquier prompt de instalación.
      * **Objetivo:** Instalar el *daemon* del servidor FTP en la máquina Ubuntu Server.

2.  **Modificar el Fichero de Configuración:**

    ```bash
    sudo nano /etc/vsftpd.conf
    ```

      * **`sudo nano`:** Abre el editor de texto `nano` con privilegios de superusuario para editar el archivo.
      * **`/etc/vsftpd.conf`:** Ruta del archivo de configuración principal de `vsftpd`.
      * **Acción:** Dentro del archivo, se debe buscar y **descomentar la línea `write_enable=YES`**. Esto habilita la capacidad de escritura para los usuarios locales, permitiéndoles subir archivos al servidor FTP. Guardar y salir (`Ctrl+O`, `Enter`, `Ctrl+X`).
      * **Objetivo:** Permitir operaciones de escritura (subida de archivos) en el servidor FTP, ya que por defecto la escritura suele estar deshabilitada por seguridad.

3.  **Reiniciar y Verificar el Servicio FTP:**

    ```bash
    sudo systemctl restart vsftpd.service
    sudo systemctl status vsftpd.service
    ```

      * **`sudo systemctl restart vsftpd.service`:** Reinicia el servicio `vsftpd` para que los cambios en el archivo de configuración surtan efecto.
      * **`sudo systemctl status vsftpd.service`:** Muestra el estado actual del servicio `vsftpd`.
      * **Objetivo:** Asegurarse de que el servidor FTP está funcionando correctamente (`Active: active (running)`).

#### 4.3.2. Cliente FTP en Kali Linux

Una vez que el servidor FTP está activo, se puede conectar a él desde la máquina Kali Linux.

1.  **Conectarse al Servidor FTP:**

    ```bash
    ftp <IP_del_Ubuntu_Server>
    # Ejemplo: ftp 10.0.1.13
    ```

      * **`ftp`:** El comando cliente FTP.
      * **`<IP_del_Ubuntu_Server>`:** La dirección IP de la máquina Ubuntu Server donde está corriendo el servidor FTP.
      * **Objetivo:** Iniciar una sesión FTP con el servidor remoto. El cliente solicitará un nombre de usuario y una contraseña para autenticarse.

2.  **Ver Comandos Disponibles:**

    ```bash
    help
    ```

      * **Objetivo:** Mostrar una lista de todos los comandos FTP que son soportados por la implementación actual del cliente FTP.

3.  **Listar Contenido del Directorio Remoto:**

    ```bash
    ls
    ```

      * **Objetivo:** Mostrar los archivos y directorios presentes en el directorio de trabajo actual del servidor FTP remoto.

4.  **Descargar un Fichero (`get`):**

    ```bash
    get hello.txt
    ```

      * **`get`:** Comando FTP para descargar un archivo.
      * **`hello.txt`:** Nombre del archivo en el servidor remoto que se desea descargar.
      * **Objetivo:** Descargar el archivo `hello.txt` desde el servidor FTP a la máquina Kali Linux, en el directorio donde se ejecutó el comando `ftp`.

5.  **Verificar el Fichero Descargado (en Kali):**

    ```bash
    cat hello.txt
    ```

      * **`cat`:** Comando de Linux para concatenar y mostrar el contenido de archivos.
      * **`hello.txt`:** El nombre del archivo descargado localmente.
      * **Objetivo:** Confirmar que el archivo `hello.txt` se descargó correctamente y ver su contenido (`Hello from server1`).

6.  **Subir un Fichero (`put`):**

    ```bash
    put server.py
    # O si el archivo está en un subdirectorio: put /path/to/server.py
    ```

      * **`put`:** Comando FTP para subir un archivo.
      * **`server.py`:** Nombre del archivo local en la máquina Kali que se desea subir al servidor remoto.
      * **Objetivo:** Transferir el archivo `server.py` desde el cliente Kali al directorio de trabajo actual en el servidor FTP remoto.

Este laboratorio proporciona una experiencia práctica con el uso de clientes y servidores FTP, mostrando cómo las aplicaciones interactúan con la capa de aplicación para la transferencia de archivos.

-----