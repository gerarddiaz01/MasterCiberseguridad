### Informe de Ciberseguridad: Seguridad Física, BIOS y Prevención de Inyección de Código en Sistemas Windows

#### Introducción a la Seguridad Física y la BIOS

La seguridad de un sistema operativo Windows comienza incluso antes de que el sistema operativo se cargue, en la capa del **hardware**. La **BIOS (Basic Input-Output System)** es un **software** fundamental diseñado en la placa base que se encarga de localizar y reconocer todos los dispositivos necesarios para iniciar el sistema operativo. La correcta configuración de la BIOS, junto con otras medidas de seguridad física, constituye el primer paso crítico para fortificar un dispositivo frente a ataques maliciosos.

#### Medidas de Protección de la BIOS

Para proteger la BIOS y, por extensión, el sistema, se deben implementar varias medidas de seguridad:

* **Establecer una Contraseña en la BIOS**: Es fundamental proteger el acceso a la configuración de la BIOS mediante una contraseña. Esto evita que usuarios no autorizados modifiquen las opciones de arranque o deshabiliten las características de seguridad.
* **Deshabilitar el Arranque desde Dispositivos Extraíbles**: Una de las vulnerabilidades más comunes es el arranque desde dispositivos USB o CD/DVD. Deshabilitar esta opción previene que un atacante inicie el sistema desde un medio externo malicioso para acceder a los datos o inyectar **Malware**.
* **Seguridad Física del Dispositivo**: El acceso físico al equipo es un factor crítico. Si un atacante tiene acceso al dispositivo, podría intentar resetear la contraseña de la BIOS extrayendo la pila (CMOS battery). Sin embargo, en equipos más modernos, esta técnica es más difícil debido a que la contraseña de la BIOS se almacena en una memoria auxiliar como la **EEPROM**.
* **Contraseñas de Fabricante de la BIOS**: Es un ataque conocido el uso de contraseñas de administrador predeterminadas publicadas por los fabricantes. Los atacantes pueden utilizar estas contraseñas para restablecer la BIOS a sus valores de fábrica y luego manipularla.

#### Gestión de Contraseñas de la BIOS desde el Sistema Operativo

Existen herramientas que permiten administrar las contraseñas de la BIOS desde el propio sistema operativo. Una de las más populares es **Cmospwd**. Esta herramienta requiere privilegios de ejecución, ya que necesita instalarse como un servicio.

##### Comandos de Terminal para Cmospwd:

* **`ioperm.exe -i`**
    * **Sintaxis:** `ioperm.exe -i`
    * **Elementos:**
        * `ioperm.exe`: Ejecutable de la herramienta.
        * `-i`: Parámetro para instalar `ioperm` como un servicio.
    * **Porqué de la acción:** Permite que Cmospwd tenga los permisos necesarios para interactuar con la BIOS a bajo nivel.
    * **Cómo se realiza:** Se ejecuta el comando en una terminal con privilegios administrativos para instalar el controlador o servicio.
    * **Objetivo:** Habilitar la comunicación entre el sistema operativo y la BIOS para la gestión de contraseñas.

* **`net Start ioperm`**
    * **Sintaxis:** `net Start ioperm`
    * **Elementos:**
        * `net Start`: Comando de Windows para iniciar un servicio.
        * `ioperm`: Nombre del servicio a iniciar.
    * **Porqué de la acción:** Una vez instalado, el servicio debe ser iniciado para que Cmospwd pueda operar.
    * **Cómo se realiza:** Se ejecuta el comando en una terminal con privilegios administrativos.
    * **Objetivo:** Poner en funcionamiento el servicio `ioperm` para que Cmospwd pueda interactuar con la BIOS.

* **`Cmospwd_win`**
    * **Sintaxis:** `Cmospwd_win`
    * **Elementos:** Este comando es el ejecutable principal de Cmospwd.
    * **Porqué de la acción:** Inicia la aplicación Cmospwd para interactuar con las contraseñas de la BIOS.
    * **Cómo se realiza:** Se ejecuta el comando en la terminal. Ofrece opciones como "Kill cmos" o "Kill cmos (try to keep date and time)".
    * **Objetivo:** Gestionar, eliminar o intentar restablecer las contraseñas de la BIOS.

* **`ioperm -u`**
    * **Sintaxis:** `ioperm -u`
    * **Elementos:**
        * `ioperm`: Ejecutable de la herramienta.
        * `-u`: Parámetro para desinstalar `ioperm` como un servicio.
    * **Porqué de la acción:** Una vez finalizada la operación con Cmospwd, es buena práctica desinstalar el servicio para evitar posibles vulnerabilidades.
    * **Cómo se realiza:** Se ejecuta el comando en una terminal con privilegios administrativos para desinstalar el controlador o servicio.
    * **Objetivo:** Limpiar y desinstalar el servicio `ioperm` del sistema.

#### Protección del Disco Duro Mediante Contraseña en la BIOS

Algunas BIOS modernas ofrecen la posibilidad de proteger el acceso al disco duro mediante una contraseña, conocida como **DriveLock** o **ATA Password**. Es importante destacar que esta solución no cifra el disco duro. Lo que hace es prevenir el acceso a sistemas compatibles a nivel del **driver**. Los sistemas que no sean compatibles con esta tecnología no serán capaces de reconocer el disco.

#### Prevención de Inyección de Código (DEP)

La **inyección de código (Code injection)** es una técnica de ataque donde el atacante introduce código malicioso en un proceso en ejecución. Para contrarrestar esto, el **hardware** incluye una tecnología que permite marcar páginas de memoria como "no ejecutables". Esta tecnología tiene varios nombres dependiendo del fabricante: **NX**, **XN**, **XD**, **DEP (Data Execution Prevention)** o **Enhanced Virus Protection**.

* **Funcionamiento de DEP:** El sistema operativo debe ser capaz de reconocer y utilizar esta tecnología del procesador. Windows ha incorporado DEP desde Windows XP Service Pack 2.
* **Requisitos de Software:** Para que el **software** aproveche DEP, debe ser compilado específicamente para utilizar esta tecnología de prevención de ejecución de datos.
* **Verificación de DEP:** Para determinar si una aplicación utiliza esta tecnología, se pueden inspeccionar las cabeceras del archivo **PE (Portable Executable)**. Herramientas como **PEStudio**, **PE Tools** o **Explorer Suite** son útiles para esta tarea.
* **Administrador de Tareas:** El Administrador de Tareas de Windows permite verificar si un proceso tiene activada la protección de ejecución de datos (DEP).
    * Para visualizar esta información, se debe ir a la pestaña "Detalles" del Administrador de Tareas.
    * Hacer clic derecho en cualquier columna y seleccionar "Seleccionar columnas".
    * Habilitar la opción "Prevención de ejecución de datos" (Data execution prevention) o "Virtualización del control de cuentas de usuario" (UAC virtualization).
    * En la mayoría de los procesos modernos, esta característica viene habilitada por defecto, indicando que las características de seguridad se han aplicado de forma más generalizada en las versiones recientes del sistema operativo.

#### Otras Opciones de Seguridad en la BIOS

Además de las medidas mencionadas, hay otras configuraciones de la BIOS que contribuyen a la seguridad del dispositivo:

* **Contraseña de Acceso al Sistema**: Establecer una contraseña para acceder al sistema operativo desde la BIOS añade una capa adicional de seguridad.
* **Configuración del Orden de Arranque**: Es crucial configurar el orden de arranque para que el disco duro sea la primera opción, y deshabilitar o mover a una posición inferior otras opciones como el arranque por red (**Wake on LAN**) o desde USB/CD. Deshabilitar opciones innecesarias como el arranque por red evita que un atacante pueda encender el dispositivo remotamente para explotar vulnerabilidades.
* **Servicios Anti-robo (según fabricante)**: Algunos fabricantes incorporan medidas o servicios adicionales en la BIOS para proteger el dispositivo en caso de robo.
* **Chip Criptográfico (TPM - Trusted Platform Module)**: Los dispositivos actuales suelen incluir un chip **TPM**. Este chip criptográfico es fundamental para almacenar secretos, certificados digitales y otras claves de seguridad. Por ejemplo, **BitLocker** utiliza el chip TPM para guardar las claves de cifrado del volumen del sistema, lo que permite un arranque seguro del sistema operativo.

#### Conclusión

La configuración adecuada de la BIOS es el punto de partida esencial para **securizar** un sistema operativo. La efectividad de estas medidas dependerá en gran medida del fabricante del **hardware** y de las características específicas disponibles en cada dispositivo. Comprender y configurar correctamente estas características es el primer paso indispensable en la implementación de la seguridad de un dispositivo.