# **Social Engineering Toolkit (SET): Un Framework Esencial para la Evaluación de Seguridad**

En el contexto de un máster en ciberseguridad, la herramienta **Social Engineering Toolkit (SET)** representa un *framework* fundamental para la simulación y la práctica de ataques de Ingeniería Social. SET consolida una colección de utilidades que facilitan la ejecución de ejercicios de *penetration testing* (*pentesting*), Ingeniería Social y *Red Team*.

SET, que significa *Social Engineering Toolkit*, fue creado por **TrustedSec** y está desarrollado en **Python**. Aunque su desarrollo ha sido menos activo en los últimos tres o cuatro años (lo cual es un factor a considerar), sigue siendo un recurso *open source* de fácil acceso y una excelente herramienta para aprender los fundamentos de estos ataques.

### **I. Características y Vectores de Ataque de SET**

SET es conocida como una herramienta de **"botón gordo"** (*fat button tool*) debido a la facilidad con la que permite desplegar ataques complejos mediante la selección de opciones en su menú. Ofrece una amplia gama de vectores de ataque:

* **Phishing:** Creación de plantillas de correo y ataques de envío masivo (*spear phishing*).  
* **Clonación Web:** Clonación transparente de sitios web para la recolección de credenciales.  
* **Creación de *Payloads*:** Generación de archivos maliciosos (*malware*) con *payloads* precargados que permiten establecer una conexión de escucha (*listener*) con la máquina del atacante.  
* **Vectores Adicionales:** Ataques *phishing* orientados a *hardware* (Arduino), Wi-Fi, generación de códigos QR maliciosos y módulos de ataque con PowerShell.

### **II. Instalación y Ejecución de SET en Kali Linux**

SET generalmente viene **preinstalada en Kali Linux**. En caso de que no lo esté, su instalación es sencilla utilizando el gestor de paquetes `apt`.

#### **1\. Instalación (Si es Necesaria)**

Para instalar SET, se utiliza el siguiente comando en la terminal:

`sudo apt install set`

* **Sintaxis y Propósito:** `sudo` (permisos de superusuario) se utiliza para ejecutar `apt install`, que es la función de `apt` (gestor de paquetes de Debian/Kali) para descargar e instalar la herramienta `set`.

#### **2\. Ejecución de la Herramienta**

Es crucial que SET se ejecute siempre con **permisos elevados** (`sudo` o `root`), ya que requiere privilegios para realizar operaciones a nivel de sistema, *networking* y para integrarse con herramientas como Metasploit. Si se intenta ejecutar sin `sudo`, la herramienta informará que no se está ejecutando como *root* y no se levantará.

`sudo setoolkit`

* **Propósito:** La ejecución levanta la interfaz de menú de SET. La primera vez que se ejecuta, la herramienta presentará un **aviso *advisor*** con un fragmento en rojo. Este mensaje subraya que la herramienta está diseñada para **fines éticos** (pruebas de seguridad) y requiere que el usuario acepte las condiciones de uso legal, generalmente ingresando un "sí".

### **III. Navegación y Funcionalidades Principales del Menú**

Una vez ejecutado `sudo setoolkit`, se presenta el menú principal de opciones. Aunque existe un dibujo que va cambiando (a menudo con referencias a *F Society* o similares), el foco es el menú de selección, que es el *core* del *framework*.

Las opciones del menú principal y sus descripciones son:

1. **Social-Engineering Attacks (Ataques de Ingeniería Social):**  
   * **Propósito:** Es el foco principal de la herramienta. Centraliza varios vectores de ataque como *phishing*, ataques a sitios web, generación de archivos infecciosos y recolección de credenciales. Permite simular y probar escenarios centrados en el **factor humano**.  
2. **Penetration Testing (Fast-Track) (Pruebas de Penetración de Pista Rápida):**  
   * **Propósito:** Ofrece opciones rápidas y automatizadas para pruebas de penetración que a menudo se integran con funcionalidades de Metasploit.  
3. **Third Party Modules (Módulos de Terceros):**  
   * **Propósito:** Permite la integración con otras herramientas dentro del ecosistema de Kali o módulos desarrollados por terceros, ampliando las capacidades del *framework*.  
4. **Update the Social-Engineer Toolkit (Actualizar SET):**  
   * **Propósito:** Actualiza la herramienta SET a la última versión disponible en el repositorio de TrustedSec.  
5. **Update SET configuration (Actualizar Configuración de SET):**  
   * **Propósito:** Permite actualizar el archivo de configuración interno de SET, el cual puede ser modificado por el usuario para personalizar *paths* o ajustar parámetros del *framework*.  
6. **Help, Credits, and About (Ayuda y Créditos):**  
   * **Propósito:** Muestra información sobre los creadores y los agradecimientos (como la integración con Metasploit, etc.).  
7. **Exit the Social-Engineer Toolkit (Salir):**  
   * **Propósito:** Cierra la herramienta.

#### **Profundizando en los Ataques de Ingeniería Social (Opción 1\)**

Al seleccionar la Opción 1 (*Social-Engineering Attacks*), se despliega un submenú que detalla los métodos específicos:

* **Spear Phishing Attack:** Permite la creación de ataques de envío masivo de correos, o la generación de *payloads* en un formato específico, o la creación de plantillas de correo (*template*) para el engaño.  
* **Website Attack Vectors (Ataques a Sitios Web):** Permite, por ejemplo, la creación de ataques para la recolección de credenciales (clonación web).  
* **Infectious Media Generator:** Permite la creación de archivos con *payloads* precargados (simulando *malware*) para infectar medios.  
* **Create a Payload and Listener:** Facilita la creación de un *payload* y la configuración de un *listener* (un programa a la espera de una conexión de la víctima).

### **IV. Consideraciones Éticas y Técnicas**

SET es una herramienta de ejecución muy sencilla que facilita las funcionalidades típicas y los ataques más comunes de Ingeniería Social. Sin embargo, el analista debe ser consciente de sus limitaciones para ejercicios profesionales:

* **Detección:** Si se utilizan las funcionalidades básicas y por defecto de SET (ej. *payloads* sin modificar), es posible que los **antivirus** o los sistemas de seguridad de la víctima los detecten.  
* **Personalización:** Para que un ejercicio de Ingeniería Social sea exitoso y creíble, la configuración base de SET debe ser **modificada y personalizada** al máximo, superando la detección básica y alineándose con el *pretexting* único del ataque.

En resumen, SET es la introducción perfecta a la ejecución activa de ataques, y sirve como base para comprender cómo los conceptos teóricos se traducen en acciones prácticas.

# Demostración Práctica con SET: Captura de Credenciales mediante *Credential Harvester*

En esta sesión, nos centraremos en una de las funcionalidades principales de **Social Engineering Toolkit (SET)**: el método **Credential Harvester Attack Methods** (Métodos de Ataque de Captura de Credenciales). Este módulo permite al analista simular un ataque de *phishing* clonando una página web para interceptar los nombres de usuario y las contraseñas que la víctima introduce.

El objetivo didáctico es comprender la simplicidad con la que se puede montar una campaña de recolección de credenciales para fines éticos, como la **concienciación de empleados**.

---

### **I. Procedimiento y Comandos en la Terminal**

Para utilizar el *Credential Harvester* con SET en Kali Linux, se deben seguir una serie de selecciones de menú que dirigen la herramienta hacia la clonación web:

#### **1\. Iniciar SET y Seleccionar Ataques**

La herramienta debe ejecutarse con permisos de superusuario (`sudo`) para garantizar que todas las funcionalidades y dependencias (como el servidor web y los *listeners*) funcionen correctamente.

1. **Comando de Ejecución:**  
   `sudo setoolkit`

   1. **Propósito:** Inicia el *framework* SET.

2. **Navegación Inicial del Menú:**  
   1. **Selección:** `1` (Social-Engineering Attacks)  
   2. **Selección:** `2` (Website Attack Vectors)  
      1. *Propósito:* Acceder a las opciones relacionadas con la explotación de páginas web.  
   3. **Selección:** `3` (Credential Harvester Attack Methods)  
      1. *Propósito:* Elegir el módulo dedicado a la captura de credenciales.

#### **2\. Configurar el Servidor y el Vector de Clonación**

Tras seleccionar el *Credential Harvester*, SET presenta varias opciones de clonación y solicita la configuración del *listener* (servidor que recibirá las credenciales).

* **Opciones de Credential Harvester:**  
  1. **Web Templates (Templates Web):** Utilizar una lista de plantillas de sitios web predefinidas y cargadas en SET (utilizado para la demostración).  
  2. **Site Cloner (Clonador de Sitio):** Clonar una URL específica proporcionada por el atacante (generalmente un método más profesional).  
  3. **Custom Import (Importación Personalizada):** Una opción para importaciones más avanzadas y manuales.  
* **Selección y Configuración:**  
  1. **Selección:** `1` (Web Templates)  
  2. **IP del *Listener*:** SET pregunta qué **dirección IP** utilizará para el *listener* (donde se recibirán los datos). Si se presiona `Enter`, tomará la IP local por defecto (ej. `192.168.111.139`). Esta IP es donde el atacante recibirá el usuario y la contraseña.  
  3. **Redirección Post-Ataque:** SET indica que, tras la ejecución de la petición `POST` (envío de credenciales), el usuario necesita ser redirigido. Por defecto, esto se configura en el archivo `/etc/setoolkit/set.config`, pero la plantilla lo hace de forma automática a la URL real que se está clonando.

#### 

#### 

#### **3\. Elegir la Plantilla y Lanzar el Ataque**

* **Selección de Plantilla:** Se elige el número correspondiente a la plantilla web que se desea suplantar (ej. la opción `2` para Google, o en un segundo ejemplo, la opción para Twitter).  
* **Lanzamiento:** SET inicia el servidor web (generalmente **Apache**), que escucha en el **puerto 80** (sin HTTPS) con la página de *phishing* activa.

### **II. Simulación y Captura de Credenciales**

Una vez que el servidor de *phishing* está activo, el ataque se simula accediendo a la IP del atacante desde el navegador.

1. **Acceso a la Página de *Phishing*:**  
   * El atacante (o la víctima en la simulación) navega a la **IP del *listener*** (ej. `http://192.168.111.139`).  
   * El navegador muestra la página clonada (ej. Google o Twitter, aunque se observa que, al estar las *templates* desactualizadas, el *look and feel* no se corresponde con las interfaces modernas de X/Google, lo cual es un factor de detección a considerar).  
2. **La Captura:**  
   * La víctima introduce un usuario (ej. `marta@gmail.com`) y una contraseña (ej. `Test123!`) y pulsa **Sign In**.  
   * La página realiza una petición `POST` con estos datos al servidor web malicioso.  
   * Inmediatamente, el servidor web (controlado por SET) registra la información capturada: "Possible username found: \[usuario\]" y "Possible password found: \[contraseña\]".  
   * El navegador de la víctima es **redirigido automáticamente** a la página real (ej. `google.com` o `twitter.com`), haciendo que la víctima piense simplemente que ha introducido mal sus credenciales.

3. **Resultado en la Terminal del Atacante:**

El *log* de SET en la terminal muestra la salida de la petición y la información capturada:  
\[...\]

\[+\] Possible username found: marta@gmail.com

\[+\] Possible password found: Test123\!

\[...\]

### **III. Aplicación Práctica y Consideraciones de *Red Team***

Este ejercicio, aunque simple, ilustra el núcleo de un ataque de *phishing* de recolección.

#### **Caso Práctico: Campaña de Concienciación**

Un ataque de *Spear Phishing* altamente efectivo en campañas de concienciación se basa en explotar el **Deseo** de la víctima:

* **Pretexting Creíble:** Se utiliza una historia como un "descuento exclusivo para empleados" de una marca de tecnología popular (ej. Apple, Samsung), justificado por el tamaño de la empresa.  
* **El Engaño:** Se envía un enlace al empleado donde debe **logarse con sus credenciales internas** (usuario y contraseña de la organización) para "certificar" que trabaja allí y así acceder al descuento.  
* **La Vulnerabilidad:** Al buscar obtener ese **premio/descuento**, el empleado introduce sus credenciales de la organización directamente en la web de *phishing* (el *Credential Harvester*).

#### **Inconvenientes y Profesionalización del Ataque**

Aunque SET es fácil de usar, la necesidad de profesionalizar un ataque implica superar sus limitaciones:

* **Desactualización de Templates:** Las plantillas de SET suelen estar desactualizadas (como se vio con Twitter/X), haciendo que el *look and feel* sea un factor de detección para empleados atentos.  
* **Clonación Imprecisa:** La opción de "Clonar Sitio" tampoco clona correctamente la mayoría de las páginas web modernas, especialmente aquellas que utilizan **HTTPS** y peticiones `POST` complejas en sus formularios.  
* **Trabajo Manual Requerido:** Para una campaña de *phishing* con una alta tasa de éxito, el formulario de *login* debe ser **clonado de forma personalizada y manual** para que sea idéntico al de la organización.  
* **Despliegue y Evasión:** El servidor de *phishing* debe subirse a un **VPS** (*Virtual Private Server*), utilizar un **dominio parecido** al real y gestionar la configuración para evadir la detección básica.

Como conclusión, SET es una **herramienta de "botón gordo"** excelente para el aprendizaje, pero la sofisticación de un ataque real requiere superar las limitaciones de sus *templates* y aplicar una metodología de **personalización manual** para aumentar la probabilidad de éxito.

# SET y la Ingeniería Social: Clonación de Sitios con *Site Cloner* para la Captura de Credenciales

En esta sesión, continuaremos explorando las funcionalidades de **Social Engineering Toolkit (SET)**, enfocándonos en el módulo **Credential Harvester Attack Methods** y la técnica de **Site Cloner**. Esta técnica permite al analista de ciberseguridad clonar paneles de *login* de sitios web existentes para simular ataques de *phishing* dirigidos a la **captura de credenciales**, todo con fines éticos y de **concienciación**.

El *Credential Harvester* opera levantando un servidor web (**Apache**) con la página suplantada (el cebo) y configurando un *listener* para recopilar el nombre de usuario y la contraseña que la víctima ingrese.

---

### **I. Procedimiento de Clonación con *Site Cloner***

A diferencia del método de *Web Templates* (que utiliza plantillas predefinidas), el *Site Cloner* requiere que el atacante defina una **URL específica** para la suplantación.

#### **1\. Comandos de Terminal para Navegación**

El proceso comienza con la ejecución de SET con permisos elevados y la selección de las opciones de ataque de clonación:

* **Comando de Ejecución:**  
  `sudo setoolkit`

  1. **Propósito:** Iniciar el *framework* SET con los permisos necesarios para levantar servicios de red.  
* **Navegación del Menú Paso a Paso:**  
  1. **Selección:** `1` (Social-Engineering Attacks)  
  2. **Selección:** `2` (Website Attack Vectors)  
  3. **Selección:** `3` (Credential Harvester Attack Method)  
  4. **Selección:** `2` (Site Cloner)  
     * **Propósito:** Indicar a SET que clone una URL específica en lugar de usar una plantilla preexistente.

#### **2\. Configuración y Lanzamiento del Servidor**

* **IP del *Listener*:** La herramienta solicitará la **IP local** a utilizar para recibir la información de vuelta. Esta será la dirección del *host* del atacante donde se ejecutará el servidor web que recopila los datos (ej. `192.168.1.139`).  
* **Definición de la URL a Clonar:** El analista debe ingresar la **URL completa** del panel de *login* o del sitio que se desea clonar (ej. `https://github.com/login`).  
* **Lanzamiento:** SET procede a clonar la página. Se inicia el servidor web en el **puerto 80** y se configura el *listener* para interceptar las peticiones `POST` (que contienen los datos de usuario y contraseña).

### **II. Demostración Práctica: Clonación de un Panel de Login (GitHub)**

Para verificar la funcionalidad del *Site Cloner* y sus capacidades, se realiza una prueba de concepto:

1. **URL de Prueba:** Se introduce la URL del *login* de GitHub (`https://github.com/login`).  
2. **Ejecución:** SET indica que está clonando la página y que el *Credential Harvester* ha sido ejecutado con éxito en el puerto 80\.  
3. **Acceso de la Víctima (Simulación):** Se abre un navegador y se accede a la IP del *listener*. Visualmente, la página clonada se presenta de manera **prácticamente idéntica** a la de GitHub, con imágenes y elementos gráficos bien replicados.  
4. **Captura en la Terminal:**  
   * La víctima introduce el usuario (`0xword`) y la contraseña (`MyPublicInbox`) y hace clic en *Sign In*.  
   * Automáticamente, la página redirige a la URL real de GitHub. La víctima no nota nada, pensando que simplemente se ha confundido o ha metido mal la contraseña.

Simultáneamente, la terminal del atacante (**el *log***) muestra el mensaje de confirmación y, en rojo, la información capturada:  
\[+\] Possible username found: 0xword

\[+\] Possible password found: MyPublicInbox

* De esta forma, se recopila la información sensible de la posible víctima.

### **III. Limitaciones y Fallos de la Clonación en Sitios Modernos**

Si bien la facilidad de uso de SET es evidente, su desactualización (al ser una herramienta *open source* con desarrollo intermitente) genera limitaciones significativas. Esto es crucial para entender por qué las técnicas de *phishing* avanzadas requieren trabajo manual:

1. **Problemas de Conexión y Clonación:** Al intentar clonar sitios de alta seguridad o que utilizan mecanismos avanzados de protección (como Google, Facebook/Meta, Twitter/X o TikTok), SET a menudo falla. El *log* mostrará un error genérico (ej. "no puedo clonar este sitio, revisa tu conexión a Internet") o un error de código específico:  
   * **Error de Código:** La terminal puede mostrar errores como `module ‘urllib’ has no attribute ‘urllopen’`, indicando que las bibliotecas de Python de SET no están actualizadas para manejar las estructuras web modernas o ciertos protocolos.  
2. **Protocolos de Seguridad (HTTPS y POST):** Las páginas modernas utilizan **HTTPS** y complejos mecanismos de validación de formularios que se transmiten mediante peticiones `POST`. Esto dificulta que el clonado automatizado de SET funcione correctamente, ya que está diseñado para estructuras más sencillas.  
3. **Múltiples Factores de Seguridad:** Sitios como Google o Gmail tienen demasiados factores de seguridad involucrados (verificación de usuario/teléfono, *captcha*, etc.) que impiden el clonado simple de la página de *login*.

### **IV. Conclusión: Usabilidad vs. Profesionalización**

El **Social Engineering Toolkit** es una herramienta esencial por su **facilidad de uso** y la simplicidad con la que permite simular funcionalidades típicas de ingeniería social. Sin embargo, esta simplicidad (su naturaleza de "botón gordo") es también su desventaja.

Para que una campaña de *phishing* en un ejercicio de *Red Team* sea exitosa en la actualidad, el analista debe ser consciente de que:

* El clonado automatizado no funcionará con el **100% de las páginas**.  
* Las **páginas clonadas** no siempre tienen el *look and feel* actual.  
* Para lograr la máxima profesionalidad y superar las defensas modernas, se requiere una **personalización más manual y customizada** que la que ofrece el *Site Cloner* de SET, a pesar de su gran valor didáctico.

# Generación de Medios Maliciosos con SET: El Ataque *Infectious Media Generator*

En esta sesión, continuaremos explorando las funcionalidades activas del **Social Engineering Toolkit (SET)**, centrándonos en el módulo **Infectious Media Generator** (Generador de Medios Infecciosos). Esta herramienta permite al analista crear un *payload* ejecutable y los archivos necesarios para montar un **USB malicioso**, simulando un ataque de *baiting* (cebo) que se ejecuta automáticamente al ser conectado a la máquina víctima, devolviendo una conexión remota (una *shell* o consola) al atacante.

Este ejercicio tiene un objetivo de **concienciación** y **prueba de concepto**, demostrando cómo la curiosidad de un empleado puede ser explotada para comprometer un sistema.

---

## I. Creación del *Payload* Malicioso con SET

El *Infectious Media Generator* aprovecha la potencia de **Metasploit** para crear un ejecutable que, al ser lanzado, establece una conexión inversa (`reverse_tcp`) a la máquina del atacante.

### **`1. Navegación en el Menú de SET`**

Para iniciar el proceso, es necesario ejecutar SET con permisos de *root* y navegar a la opción correspondiente:

* **Comando de Ejecución:**  
  `sudo setoolkit`

  1. **Propósito:** Iniciar el *framework* con permisos elevados.  
* **Navegación del Menú Paso a Paso:**  
  1. **Selección:** `1` (Social-Engineering Attacks)  
  2. **Selección:** `3` (Infectious Media Generator)  
     * **Propósito:** Activar el módulo para crear archivos infecciosos destinados a medios extraíbles (CD/DVD/USB).  
  3. **Selección:** `2` (Standard Executable/Meterpreter)  
     * **Propósito:** Elegir la opción de crear un *payload* ejecutable estándar de Metasploit, que es el más común y versátil.

### **`2. Configuración del Payload (Reverse TCP)`**

Una vez seleccionado el ejecutable estándar, se elige el tipo de *payload* que establecerá la conexión remota con la máquina atacante (el *listener*).

* **Selección del *Payload*:** Se selecciona la opción `2` (Windows Meterpreter Reverse TCP)  
  * **Propósito:** Generar un *payload* de **Meterpreter** (la *shell* avanzada de Metasploit) optimizado para sistemas Windows, utilizando una conexión **Reverse TCP**. Esto significa que la máquina víctima se conectará a la máquina atacante a través del protocolo TCP, eludiendo a menudo las restricciones de *firewall* locales.  
* **Configuración del *Listener* (LHOST/LPORT):**  
  * **LHOST (Local Host):** Se introduce la **IP del atacante** (la máquina Kali, ej. `192.168.111.139`), que es donde el *payload* intentará conectarse.  
  * **LPORT (Local Port):** Se define el **puerto de escucha** (ej. `4443`).

### **`3. Generación y Localización de los Archivos`**

SET genera los archivos y proporciona su ubicación en el sistema:

* **Payload.exe:** El archivo ejecutable malicioso se guarda en el directorio por defecto: `/root/.set/payload.exe`.  
* **Archivos para USB:** El ataque se configura para auto-ejecutarse, creando la estructura necesaria para un USB malicioso en la subcarpeta **autorun**.  
  * **Ubicación:** `/root/.set/autorun`  
  * **Contenido:**  
    * **`AUTORUN.INF`**: Archivo de configuración que indica al sistema operativo (en versiones antiguas de Windows o con ciertas políticas) que debe ejecutar automáticamente un programa al conectar el USB.  
    * **`PROGRAM.EXE`**: El ejecutable del *payload* de Metasploit.

## II. Despliegue en el USB y Ejecución del Ataque

El objetivo es copiar los archivos generados al USB y luego engañar al usuario para que ejecute el *payload*.

### **`1. Copia y Ofuscación del Archivo`**

Los archivos `AUTORUN.INF` y `PROGRAM.EXE` deben copiarse a la raíz del USB (ej. `/media/marta/USB_INFECT1`).

* **Comandos de Copia (Ejemplo de Terminal):**  
  `cp /root/.set/autorun/autorun.inf /media/marta/USB_INFECT1`  
  `cp /root/.set/autorun/program.exe /media/marta/USB_INFECT1`

* **Ofuscación:** Para aumentar la credibilidad, el ejecutable debe ser renombrado (ofuscación por nombre).  
  `mv /media/marta/USB_INFECT1/program.exe /media/marta/USB_INFECT1/WinUpdate.exe`

  * **Propósito:** El nombre `WinUpdate.exe` (Actualización de Windows) es menos sospechoso que `program.exe`, explotando el principio de **confianza**.

### **`2. Levantamiento del Listener (Metasploit)`**

SET pregunta si se desea levantar el *listener* de Metasploit. Al responder **sí**, SET lo configura y lanza automáticamente:

* **Acción de SET:** Ejecuta comandos de Metasploit para configurar el *handler* (el *listener*) en la IP y puerto especificados (ej. `192.168.111.139` en el puerto `4443`). El comando se lanza con la opción `-j` para ejecutarlo en *background* y esperar la conexión.

### **`3. Simulación de la Infección (Baiting)`**

* **Conexión a la Víctima:** El USB debe conectarse a la máquina víctima (en este caso, un Windows con las defensas desactivadas para la prueba).  
* **Ejecución del Engaño:** Si la función de auto-ejecución del *AUTORUN.INF* no funciona (algo común en sistemas modernos), la víctima debe ser engañada para que ejecute el archivo, por ejemplo, al verlo y pensar: "¿Qué es este archivo de actualización?". Se ejecuta `WinUpdate.exe`.  
* **Apertura de la Sesión:** Al ejecutarse, el *payload* se conecta al *listener* en la máquina Kali, abriendo una **sesión de Meterpreter**. El *log* de SET notifica: `meterpreter session 2 open...`

## III. Interacción con Meterpreter

Una vez abierta la sesión (ej. `sessions -i 2`), el analista puede interactuar con la máquina víctima a través de la *shell* de Meterpreter.

**Comandos de Acceso:**  
`sessions         # Muestra todas las sesiones activas (ej. 1 y 2)`

`sessions -i 2    # Interactúa con la sesión 2`

`whoami           # Identifica el usuario con el que se está ejecutando (ej. 'root' si se ejecutó con permisos de administrador)`

`help             # Muestra la lista de comandos disponibles en Meterpreter`

`sysinfo          # Muestra información detallada del sistema (SO, arquitectura, etc.)`

**Nota Crítica de Seguridad:** Para que esta prueba de concepto funcione, las **defensas de Windows** (como **Windows Defender** y el *Firewall*) deben ser **desactivadas**. En un entorno real, los antivirus modernos detectan y eliminan automáticamente los *payloads* genéricos de Metasploit (como este `reverse_tcp`) al contacto o al intentar ejecutarse.

## IV. Conclusiones Metodológicas

El módulo *Infectious Media Generator* de SET es un excelente recurso para la **concienciación** y para demostrar el peligro del *baiting* y del *malware* en USB.

* **Objetivo de Concienciación:** Se demuestra a los empleados el riesgo que corren al conectar USBs encontrados ("tirados en el suelo"). El mensaje clave es **pensar dos veces antes de conectar** cualquier medio desconocido.  
* **Limitación de "Botón Gordo":** SET es una herramienta de **"botón gordo"** y no está diseñada para realizar pruebas altamente sofisticadas en entornos reales. Si se requiere un ataque de *baiting* profesional, es necesario trabajar a **más bajo nivel** (personalización del *payload*, *encoding* o evasión) para eludir los sistemas de seguridad avanzados que, de lo contrario, detectarían el *payload* de Metasploit.

