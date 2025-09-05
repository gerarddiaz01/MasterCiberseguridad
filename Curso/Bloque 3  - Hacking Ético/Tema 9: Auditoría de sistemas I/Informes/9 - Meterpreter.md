Documentos de Referencia: "AS-I - Post-Explotación_Meterpreter.pdf"

# Informe Técnico: Post-Explotación con Meterpreter

### 1. Resumen Ejecutivo
Este informe técnico profundiza en la fase de post-explotación de un ataque de ciberseguridad, con un enfoque particular en el uso de Meterpreter. Se explican sus capacidades como herramienta avanzada para la persistencia, la escalada de privilegios y la exfiltración de datos. El informe detalla procedimientos prácticos, incluyendo la obtención de información del sistema, la manipulación de archivos, el espionaje a través de la webcam y el micrófono, y la limpieza de evidencias mediante la manipulación de los registros de eventos de Windows.

---

### 2. Conceptos Fundamentales

#### Post-Explotación y Meterpreter

La **post-explotación** es la etapa final de un ataque cibernético, que ocurre después de que un atacante ha logrado acceder a un sistema. En esta fase, el objetivo principal es maximizar el control y el acceso para lograr distintos propósitos, como mantener una presencia duradera en el sistema, escalar privilegios, y filtrar datos valiosos.

**Meterpreter** es una carga útil (payload) avanzada que forma parte del **Metasploit Framework**. A diferencia de Metasploit, que es un conjunto de herramientas para pruebas de penetración, Meterpreter es un módulo de post-explotación diseñado para ejecutarse en la máquina de la víctima y proporcionar control remoto. Se ejecuta a un nivel muy bajo en el sistema, lo que lo hace difícil de detectar.

Meterpreter permite realizar una amplia gama de tareas de manera remota, como interactuar con el sistema de archivos, el teclado y la webcam. La versión de Meterpreter para Windows es la más completa en cuanto a funcionalidades, aunque algunas características pueden no estar disponibles en sistemas como Linux o macOS.

#### Ficheros de Autenticación y Cuentas de Usuario

* **Security Account Manager (SAM) en Windows:** El **SAM** es un archivo de base de datos en los sistemas operativos Microsoft Windows que almacena nombres de usuario y contraseñas. Se localiza en la ruta `C:\Windows\System32\config\SAM` y está montado en el registro del sistema en `HKEY_LOCAL_MACHINE\SAM`. Los datos en este archivo están cifrados y solo son accesibles con permisos de `SYSTEM`, el nivel de privilegio más alto. Durante el inicio de sesión, el sistema verifica el nombre de usuario y la contraseña contra esta base de datos. La base de datos SAM almacena los hashes LM y NTLM de las contraseñas.

* **`/etc/passwd` y `/etc/shadow` en Linux:** Estos dos archivos son los análogos de la base de datos SAM en sistemas Linux.
    * **`/etc/passwd`**: Contiene la información básica de los usuarios registrados, como el nombre de inicio de sesión, el User ID (UID), el grupo principal, y la ruta del directorio principal y la shell. La contraseña se representa con una "x", lo que indica que el hash de la contraseña está almacenado en el archivo `/etc/shadow`. Este archivo tiene permisos de solo lectura para todos los usuarios, excepto el propietario (`root`), que puede leer y escribir en él.
    * **`/etc/shadow`**: Almacena de forma segura las contraseñas cifradas y con sal (hashed) de los usuarios. Este archivo es mucho más restrictivo y solo es accesible por el usuario `root`. Los atributos de cada entrada están separados por dos puntos y contienen el nombre de usuario, el hash de la contraseña, la fecha del último cambio de contraseña, la antigüedad mínima y máxima de la contraseña, y los días de advertencia e inactividad antes de la desactivación de la cuenta.

#### Windows Event Log

El **Windows Event Log** es un registro digital que documenta eventos significativos en un sistema Windows, como funciones del sistema, acciones de aplicaciones y cuestiones de seguridad. Estos eventos se almacenan en la ruta `C:\Windows\System32\winevt\Logs` y se dividen en tres tipos esenciales: `Aplicación`, `Seguridad` y `Sistema`. Cada evento contiene información detallada, como la gravedad, la fecha y hora, la fuente, un Event ID (un identificador que especifica el tipo de evento), y el nombre de usuario asociado al evento.

---

### 3. Procedimientos Prácticos

A continuación, se describen los procedimientos prácticos para el manejo de una sesión de Meterpreter, basados en el entorno de laboratorio que incluye una máquina Kali Linux y una máquina Windows, con la vulnerabilidad EternalBlue ya explotada.

#### Gestión de la Sesión de Meterpreter

1.  **Poner la sesión en segundo plano:** Si se desea volver a la consola de Metasploit sin cerrar la sesión de Meterpreter, se usa el comando **`background`**. Esto permite continuar con otras tareas en la consola `msfconsole` mientras la sesión se mantiene activa.
2.  **Visualizar sesiones activas:** Para ver todas las sesiones activas, se ejecuta el comando **`sessions`**. Esto mostrará un listado con el ID de cada sesión.
3.  **Retomar una sesión:** Para volver a una sesión específica, se usa el comando **`sessions -i [id]`**, donde `[id]` es el número de la sesión que se desea retomar.

#### Obtención de Información del Sistema

1.  **Información de usuario y proceso:**
    * **`getuid`**: Muestra el nombre del usuario de la sesión actual. El valor `NT AUTHORITY\SYSTEM` indica el nivel más alto de privilegios en Windows.
    * **`getpid`**: Muestra el ID del proceso actual en el que se está ejecutando la sesión de Meterpreter.
    * **`ps`**: Lista todos los procesos en ejecución en la máquina comprometida, permitiendo identificar procesos más estables y duraderos a los cuales migrar la sesión.
2.  **Migración de procesos:**
    * **`migrate [pid]`**: Permite mover la sesión de Meterpreter a otro proceso en el sistema. Por ejemplo, se puede migrar a un proceso del servidor SSH, que suele ser más estable, para asegurar la persistencia de la sesión.
3.  **Información del sistema operativo:**
    * **`sysinfo`**: Proporciona información detallada sobre el sistema remoto, como el nombre de la computadora, el sistema operativo, la arquitectura, el lenguaje del sistema y los usuarios conectados.

#### Interacción con el Sistema de Archivos

Meterpreter utiliza comandos de la interfaz `stdapi` para interactuar con el sistema de archivos del objetivo. Los comandos son muy similares a los de un sistema Unix, pero Meterpreter los traduce para que sean compatibles con el sistema operativo subyacente.

* **`ls`**: Lista los archivos y directorios en la ruta actual. En la práctica de laboratorio, al migrar al proceso del servidor SSH, la ruta por defecto es `C:\Program Files\OpenSSH`.
* **`pwd`**: Muestra la ruta del directorio de trabajo actual.
* **`cd [directorio]`**: Cambia el directorio de trabajo.
* **`cat [archivo]`**: Muestra el contenido de un archivo en la pantalla.
* **`rm [archivo]`**: Elimina un archivo.

#### Extracción de Hashes de Contraseñas

1.  **Volcado de la base de datos SAM:**
    * **`hashdump`**: Este comando es fundamental para la recolección de credenciales, ya que vuelca el contenido de la base de datos SAM de Windows. El resultado es una lista de usuarios con sus identificadores relativos (RID), hashes LM y NTLM.
2.  **Procesamiento de los hashes:** Los hashes se pueden guardar en un archivo y luego se pueden manipular en una terminal de Kali para extraer únicamente los hashes NTLM (la cuarta columna de la salida de `hashdump`). Por ejemplo, el comando `cut -d ":" -f4 hashes.txt` extrae la cuarta columna, utilizando los dos puntos como delimitador.
3.  **Crackeo de hashes:** Los hashes NTLM extraídos se pueden crackear para obtener las contraseñas en texto plano.

#### Espionaje y Control de la Interfaz de Usuario

1.  **Control de la webcam y el micrófono:**
    * **`record_mic -d [segundos]`**: Graba audio del micrófono por el número de segundos especificado.
    * **`webcam_list`**: Lista las webcams disponibles en el sistema.
    * **`webcam_snap -v`**: Toma una instantánea de la webcam y la muestra automáticamente.
    * **`webcam_stream -v`**: Inicia una transmisión de video en tiempo real desde la webcam y la muestra automáticamente en un navegador.

2.  **Manipulación del teclado y la pantalla:**
    * **`keyscan_start`**: Comienza a capturar las pulsaciones del teclado.
    * **`keyscan_dump`**: Muestra las pulsaciones de teclas que han sido capturadas desde que se inició el escáner del teclado.
    * **`keyscan_stop`**: Detiene la captura de pulsaciones de teclas.
    * **`screenshot -v`**: Toma una captura de pantalla del escritorio y la muestra al instante.
    * **`screenshare -v`**: Permite ver el escritorio del usuario en tiempo real.
    * **`keyboard_send [texto]`**: Envía una cadena de texto al sistema remoto. Los espacios deben enviarse con comandos separados.
    * **`mouse [acción] [x] [y]`**: Envía eventos del ratón, como mover, hacer clic o hacer clic con el botón derecho.

#### Limpieza de Evidencias

1.  **Limpiar los registros de eventos de Windows:**
    * **`clearev`**: Borra todos los registros de los eventos en los logs de Aplicación, Sistema y Seguridad de Windows. Esto elimina la evidencia de la actividad del atacante en el sistema, dificultando su detección. Es importante tener privilegios de `SYSTEM` para realizar esta acción, lo cual se logra con el comando `getsystem`.

---

### 4. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

La fase de post-explotación y el uso de herramientas como Meterpreter son críticas para entender las capacidades de un atacante una vez que ha comprometido un sistema. Para los profesionales de la ciberseguridad, dominar estos conceptos es vital para diseñar defensas efectivas. La habilidad para migrar procesos, obtener privilegios elevados, y limpiar evidencias demuestra que un atacante puede establecer una presencia persistente y evadir la detección. Por tanto, la monitorización constante de la red y los sistemas, así como la implementación de políticas de seguridad robustas, son esenciales para mitigar este tipo de amenazas.

#### Puntos de Aprendizaje Clave

* **Meterpreter como Herramienta central:** Meterpreter no es un programa independiente, sino un componente clave de Metasploit, que simplifica y facilita las tareas de post-explotación.
* **Adaptabilidad del Payload:** La reversa shell es una técnica eficaz para evadir firewalls al invertir el flujo de la conexión, permitiendo que la máquina de la víctima inicie la conexión saliente hacia el atacante.
* **Persistencia y Evasión:** Comandos como `migrate` permiten que una sesión de Meterpreter se mueva a un proceso más estable y menos propenso a ser detectado, asegurando la continuidad del acceso.
* **Recolección de Credenciales:** La capacidad de volcar los hashes de contraseñas de la base de datos SAM en Windows es un paso crucial para la escalada de privilegios y el movimiento lateral en una red.
* **Análisis Forense y Anti-forense:** La limpieza de los registros de eventos (`clearev`) es una técnica anti-forense que los atacantes utilizan para eliminar rastros. La comprensión de los Event Logs de Windows y su funcionamiento es fundamental para el análisis forense y la detección de incidentes de seguridad.

#### Relevancia Técnica

El conocimiento de Meterpreter y sus comandos es directamente aplicable en pruebas de penetración y auditorías de seguridad. Los procedimientos aprendidos, como el manejo de sesiones, el control de procesos y la recolección de información, son habilidades esenciales para un `pentester`. Entender cómo un atacante utiliza estas herramientas permite a un profesional de la seguridad fortalecer las defensas de un sistema, ya sea a nivel de configuración de red, gestión de permisos o monitorización de registros. El control de la interfaz de usuario, así como la capacidad de limpiar evidencias, resalta la importancia de la seguridad en profundidad y la auditoría continua.