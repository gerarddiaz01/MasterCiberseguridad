## Informe Técnico: Evilginx: Proxy Inverso y Evasión del Doble Factor de Autenticación (MFA)

Documentos de Referencia: "IS - Evilginx.pdf"

### 1. Resumen Ejecutivo

Este informe técnico detalla el uso y la arquitectura de **Evilginx**, un *framework* avanzado de **proxy inverso** diseñado para campañas de *phishing* de nivel profesional. Su principal capacidad es la de eludir el **Doble Factor de Autenticación (MFA)** al interceptar las *cookies* de sesión válidas. El documento aborda la arquitectura del ataque, los prerrequisitos de instalación, la configuración del entorno, la mitigación a través de la autenticación resistente al *phishing* (FIDO/U2F), y la simulación práctica de un ataque dirigido.

### 2. Conceptos Fundamentales

A continuación, se presentan los conceptos clave para comprender el mecanismo de ataque de Evilginx:

* **Evilginx:** Es un *framework* de **proxy inverso** avanzado para *phishing*. Está diseñado para la captura de sesiones válidas, permitiendo a los atacantes **bypassear el MFA**.
* **Proxy Inverso (Reverse Proxy):** Es el mecanismo central de Evilginx. Evilginx actúa como un intermediario o *man-in-the-middle* entre la víctima y el sitio web legítimo, gestionando todo el tráfico de forma transparente.
* **Ataque Man-in-the-Middle (MITM) y SSL/TLS:** El servidor Evilginx establece una conexión cifrada con SSL/TLS con la víctima, mostrando el ícono de seguridad (candado verde) en el navegador, lo que hace que la URL falsa parezca legítima y segura.
* **Evasión de MFA:** A diferencia del *phishing* tradicional, Evilginx intercepta en tiempo real tanto las credenciales (usuario y contraseña) como el código MFA (SMS o TOTP). Utiliza inmediatamente estos elementos para completar la autenticación con el servidor real.
* **Captura de Cookies de Sesión (Session Hijacking):** La ganancia real del ataque. Una vez que la autenticación es exitosa, el sitio web real envía al Evilginx Server una **cookie de sesión válida y autorizada** (un *token* de sesión). Evilginx intercepta y almacena este *token*, permitiendo al atacante suplantar completamente a la víctima en el futuro sin necesidad de credenciales.
* **Phishlet:** Son archivos de configuración en formato **YAML** que actúan como plantillas de *proxy* inverso. Definen cómo clonar un servicio específico (ej., Google, Microsoft), incluyendo la configuración de subdominios, filtros de contenido (*sub\_filters*), y las *keys* de las *cookies* de sesión a capturar (*auth\_tokens*).
* **Lures:** Es el módulo dentro de Evilginx para la **generación de URLs de *phishing***. Permite al analista configurar la ruta específica (ej., `/login`) y generar el enlace completo de ataque (ej., `https://example.com/login`).
* **Autenticación Resistente al Phishing (FIDO/U2F):** La contramedida más efectiva contra Evilginx. Las **Passkeys** o **llaves de seguridad físicas** (ej., YubiKey) bajo los estándares **FIDO/U2F** funcionan con el **Principio de Vinculación de Dominio**. La llave verifica automáticamente el dominio real en el navegador; si es el dominio falso (controlado por Evilginx), la llave se niega a autenticar.

---

### 3. Procedimientos Prácticos

El uso de Evilginx requiere la instalación de prerrequisitos y una configuración lógica de sus componentes (*phishlets* y *lures*).

#### 3.1 Prerrequisitos del Entorno Operativo

Evilginx no es una herramienta de "descargar y ejecutar" y requiere un **Servidor Virtual Privado (VPS)** o un entorno Linux (ej., Ubuntu, Debian, o Kali) con una dirección **IP pública estática**.

* **Puertos Esenciales:** Los siguientes puertos deben estar abiertos y disponibles en el VPS para gestionar el tráfico y el servidor DNS local:
    * **80 (HTTP):** Para tráfico no cifrado.
    * **443 (HTTPS):** Para el tráfico cifrado del *proxy* inverso (el más crítico).
    * **53 (DNS):** Para la resolución local de nombres de dominio.
* **Dominio y Certificado SSL/TLS:** Se necesita registrar un **Dominio de Phishing** (parecido a la marca suplantada) que apunte al VPS. Evilginx automatiza la obtención de un **Certificado SSL/TLS** (el candado verde) para el dominio de *phishing*, típicamente usando Let's Encrypt.
* **Dependencias de Software:** Evilginx está escrito en el lenguaje **Go (Golang)** y usa **Node.js** para algunos componentes.

#### 3.2 Instalación y Configuración Inicial

El proceso se basa en la descarga de dependencias y la compilación del código fuente de Evilginx.

1.  **Instalación de Golang:** Descargar y descomprimir el archivo de Golang (ej., `go1.22.1.linux-amd64.tar.gz`) en la ruta `/usr/local`.
    * *Comando:* `sudo tar -C /usr/local -xzf go1.22.1.linux-amd64.tar.gz`
        * *Propósito:* **`sudo`** otorga permisos de *root*. **`tar`** descomprime (`x`) y extrae (`z`), colocando (`-C`) el contenido en `/usr/local`.
    * **Añadir al PATH:** El directorio binario de Go debe añadirse a la variable de entorno `PATH` para poder ejecutar los comandos de Go.
        * *Comando:* `export PATH=$PATH:/usr/local/go/bin`
2.  **Instalación de Node.js:** Necesario para componentes de la herramienta.
    * *Comando:* `sudo apt-get -y install nodejs`
3.  **Configuración del Núcleo (Kernel):** Se requiere para permitir que procesos sin privilegios clonen espacios de nombres de usuario.
    * *Comando:* `sudo sysctl -w kernel.unprivileged_userns_clone=1`
4.  **Descarga y Compilación del Binario:**
    * **Descarga:** Descargar el código fuente de Evilginx (ej., `evilginx2-3.2.0.zip`) y extraerlo.
        * *Comando:* `unzip evilginx2-3.2.0.zip`
    * **Compilación:** Navegar a la carpeta y usar `make` para compilar el código Go y generar el binario ejecutable.
        * *Comando:* `cd evilginx2-3.2.0` y luego `make`
5.  **Ejecución Inicial (Modo Developer - para pruebas locales):**
    * *Comando:* `sudo ./build/evilginx -p ./phishlets -r ./redirectors -developer`
        * *Propósito:* **`sudo`** otorga permisos elevados. **`./build/evilginx`** es el ejecutable. **`-p ./phishlets`** indica la ruta de los archivos de configuración. **`-developer`** habilita el modo local de prueba.

#### 3.3 Configuración y Lanzamiento del Ataque (CLI)

Evilginx se gestiona desde una interfaz de línea de comandos (*shell*) interactiva. El orden de configuración es fundamental.

1.  **Configuración General:** Establecer el dominio base para el *phishing* y la IP de escucha.
    * *Comandos:* `config domain example.com`, `config ipv4 127.0.0.1`
2.  **Configuración del Phishlet Hostname y Hosts:** (Crucial para pruebas locales).
    * **Definir el Subdominio Específico:** Asociar un *hostname* (nombre de *host*) específico al *phishlet*.
        * *Comando:* `phishlets hostname example example.test.com`
    * **Generar Línea Hosts:** Obtener la línea necesaria para agregar al archivo `/etc/hosts`.
        * *Comando:* `phishlets get-hosts example`
        * *Acción:* La línea generada (ej., `127.0.0.1 academy.example.test.com`) debe pegarse en el archivo `/etc/hosts` para que el sistema operativo redirija el tráfico del dominio falso a la IP local del *listener*.
3.  **Creación del Lure (URL de Phishing):** Se crea una instancia del *lure* y se modifica la ruta para que sea más creíble.
    * *Comandos:* `lures create example`, `lures edit 0 path login`
4.  **Activación:** Habilitar el *phishlet* para que Evilginx comience a escuchar y a actuar como *proxy* en el puerto 443.
    * *Comando:* `phishlets enable example`
5.  **Obtención de la URL de Phishing:** Obtener el enlace final que se incluirá en el correo electrónico de *phishing*.
    * *Comando:* `lures get-url 0`
    * *Resultado:* Una URL como `http://academy.example.test.com/login`.

#### 3.4 Procedimiento de Creación de un Phishlet Propio

La creación de un *phishlet* propio requiere investigación de la web objetivo y la definición precisa de los bloques:

* **`proxy_hosts` (Configuración del Dominio):** Define el mapeo entre las URL de *phishing* y el sitio original. El parámetro **`session`** debe ser `true` para rastrear y capturar las *cookies*.
* **`credentials` (Captura de Credenciales):** Define qué credenciales (usuario/contraseña) buscar y robar de las peticiones POST.
    * El parámetro **`key`** es crítico; es el nombre del campo HTML (`<input name="..." >`) que contiene la credencial (ej., `email`, `password`).
* **`auth_tokens` (Captura de Cookies de Sesión):** Este es el bloque que permite eludir el 2FA.
    * El parámetro **`keys`** es CRÍTICO: es la lista de nombres de las *cookies* que actúan como *tokens* de sesión (ej., `cookie_name`). Estos nombres se identifican con herramientas de desarrollador tras un inicio de sesión exitoso.
* **`sub_filters` (Filtros de Contenido):** Permite reescribir enlaces y corregir problemas de JavaScript/HTML. Reemplaza un texto de búsqueda (`search`) por otro (`replace`) en el contenido del sitio.

---

### 4. Conclusiones y Puntos Clave

#### 4.1 Importancia y Beneficios de Seguridad

* **El Mito del MFA Roto:** Evilginx demuestra que el **MFA tradicional** (basado en SMS o TOTP) **no protege completamente contra el *phishing***, ya que el *proxy* inverso captura el código de un solo uso en tiempo real.
* **La Defensa con FIDO/U2F:** La medida de seguridad más efectiva es el uso de **Passkeys o llaves de seguridad físicas (FIDO/U2F)**. Su principio de **Vinculación de Dominio** asegura que la autenticación solo se complete en el dominio real, deteniendo el ataque de *proxy* inverso en seco.
* **Estrategia Zero Trust:** Las organizaciones deben implementar un modelo **Zero Trust** para monitorear comportamientos inusuales después de un inicio de sesión que pudieran indicar una toma de cuenta (*Account Takeover*).

#### 4.2 Puntos de Aprendizaje Clave

* **Captura de Sesión > Captura de Credenciales:** El verdadero valor de Evilginx es la captura de las **cookies de sesión válidas**, que permite la suplantación completa de la identidad sin necesidad de conocer la contraseña o el MFA en el futuro.
* **Concienciación Crucial:** La defensa manual requiere **inspeccionar con atención la barra de direcciones** en busca de dominios inusuales o caracteres homógrafos. Los usuarios nunca deben usar el enlace de un correo para iniciar sesión; deben abrir una nueva ventana y escribir la URL legítima directamente.
* **Necesidad de Actualización Constante:** Los servicios de alta seguridad (Google, Microsoft) implementan **cambios de seguridad continuos**. Un *phishlet* debe actualizarse constantemente o crearse uno propio, ya que puede dejar de ser funcional rápidamente.

#### 4.3 Relevancia Técnica

* **Phishlets vs. Clonación Simple:** Los *phishlets* de Evilginx son archivos YAML complejos pero mucho más potentes que la simple clonación HTML (*Gophish*), ya que gestionan activamente la comunicación de *proxy* inverso y la captura de *cookies*.
* **Orden Lógico de Configuración:** La ejecución de Evilginx en un entorno profesional requiere un orden de configuración estricto: primero la **Configuración General** (`config domain`, `config ipv4`), luego el **Phishlet** y el **Host**, después la **Creación/Edición del Lure**, y finalmente la **Activación** (`phishlets enable`).
* **Uso Profesional:** Evilginx es una herramienta de alto nivel utilizada por profesionales en ejercicios de **Red Team** para simular *phishing* avanzado, lo que subraya la necesidad de entender la arquitectura de *proxy*, la sintaxis de YAML para *phishlets* y la post-explotación con *tokens* de sesión.