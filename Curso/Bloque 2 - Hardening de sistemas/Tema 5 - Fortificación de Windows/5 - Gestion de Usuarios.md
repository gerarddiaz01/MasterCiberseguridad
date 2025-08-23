# Gestión de Permisos y Usuarios en Windows

El sistema de permisos de Windows sobre NTFS es un recurso fundamental para gestionar los privilegios de los usuarios sobre los archivos y recursos del sistema. Permite ajustar detalladamente las opciones de acceso, definiendo qué puede hacer y qué puede acceder cada usuario. El protocolo NTFS está bien diseñado, sin problemas de seguridad graves reportados y con configuraciones por defecto que no son excesivamente permisivas. Sin embargo, para un control preciso de los permisos NTFS, es crucial entender los grupos de usuarios de Windows.

## Usuarios de Windows

Existen diferentes tipos de usuarios en Windows, cada uno con un nivel de privilegio específico:

* **Administrador**: Este usuario posee el control absoluto del sistema. No puede ser eliminado y, por defecto, está deshabilitado a partir de Windows Vista. Sin embargo, si el sistema se inicia en modo seguro (a prueba de fallos), este usuario se habilitará automáticamente.
* **Invitado**: Permite el acceso al equipo a través de la red a recursos compartidos sin requerir un nombre de usuario y contraseña. No obstante, sus privilegios son restringidos y se encuentra deshabilitado por defecto, siendo recomendable mantenerlo así por seguridad.
* **Usuario Inicial**: Es el usuario que se crea durante el proceso de instalación del sistema operativo y automáticamente se asigna al grupo de administradores.

## Cuentas Especiales del Sistema Operativo

Microsoft Windows utiliza otras cuentas especiales para la ejecución de servicios:

* **System**: Pertenece al grupo de administradores y goza de todos los privilegios sobre el sistema. Un administrador puede ejecutar comandos con privilegios de SYSTEM, por ejemplo, creando una tarea con el comando `at`. Es importante destacar que, a partir de Windows Vista, nada que se ejecute bajo SYSTEM se muestra en pantalla directamente; para lograr una salida en pantalla, se puede utilizar herramientas como `psexec` de SysInternals (ejemplo: `psexec -i -s cmd.exe`).
* **LocalService**: Presenta credenciales anónimas en la red y posee privilegios bajos, con permisos de presentación en el sistema.
* **Network Service**: Actúa como el sistema en la red.

## Grupos de Usuarios de Windows

Para una administración más eficiente de los permisos, se recomienda asignar privilegios a grupos en lugar de a usuarios individuales. Los principales grupos de Windows son:

* **Administradores**: Este grupo tiene permisos completos sobre el sistema. Solo el administrador y el usuario creado para administrar el equipo deberían pertenecer a este grupo.
* **Operadores de copia**: Proporcionan servicios para realizar copias de seguridad. No está destinado para el uso de usuarios directos, sino para programas o tareas del sistema.
* **Invitados**: Los miembros de este grupo tienen acceso limitado al sistema y se recomienda mantenerlo deshabilitado.
* **Operadores de red**: Poseen privilegios para la configuración de TCP/IP del equipo.
* **Usuarios**: Los usuarios dentro de este grupo tienen acceso limitado al sistema. Pueden ejecutar aplicaciones pero no realizar modificaciones críticas. Los usuarios creados por defecto al instalar Windows suelen pertenecer a este grupo.

### Otros Grupos Especiales del Sistema

Además de los grupos anteriores, existen otros grupos especiales cuya pertenencia es gestionada automáticamente por el sistema para diferentes propósitos:

* **Propietarios**: Es el grupo al que pertenece la cuenta que ha creado o tomado posesión de un objeto (como un archivo o carpeta) y tiene control total sobre dicho objeto.
* **Todos**: Incluye a cualquier entidad que tenga acceso al equipo, con o sin contraseña.
* **Interactivo**: Representa a los usuarios locales que inician sesión en el sistema introduciendo un usuario y contraseña.
* **Network**: Agrupa a los usuarios que acceden al sistema a través de la red.
* **Usuarios Autenticados**: Usuarios que acceden al sistema con una identidad y contraseña válidas.
* **Anonymous Logo**: Usuarios anónimos, utilizados, por ejemplo, por servicios web como Internet Information Services cuando se realiza una solicitud de página web sin autenticación.
* **Usuarios de Servidor de Terminal**: Agrupa a los usuarios que se conectan utilizando Terminal Server.

## Visualización y Gestión de Usuarios y Grupos en Windows

Windows ofrece diversas herramientas y comandos para consultar y administrar usuarios y grupos.

### Gestión Gráfica a través de la Administración de Equipos

Para una gestión visual, se puede acceder a la herramienta de **Administración de Equipos**. Dentro de esta, en la sección **Usuarios y grupos locales**, se pueden visualizar los usuarios y grupos existentes en el dispositivo. Al seleccionar un usuario, se puede acceder a sus **Propiedades** para ver opciones de configuración, verificar su pertenencia a grupos específicos, añadirlo a nuevos grupos o revisar su perfil. De manera similar, en la sección de **Grupos**, se listan todos los grupos disponibles con una descripción de su función.

### Consulta de Usuarios y Grupos mediante la Línea de Comandos (PowerShell/CMD)

La línea de comandos proporciona una forma eficiente de obtener información detallada sobre usuarios y grupos.

* **Listar cuentas de usuario completas**:
    * **Comando**: `wmic useraccount list full`
    * **Sintaxis y Elementos**:
        * `wmic`: (Windows Management Instrumentation Command-line) es una utilidad de línea de comandos que permite interactuar con WMI para realizar diversas tareas de administración.
        * `useraccount`: Especifica que se desea trabajar con la clase de objetos `useraccount`.
        * `list full`: Indica que se deben listar todas las propiedades (información completa) de las cuentas de usuario.
    * **Porqué de la acción**: Este comando es fundamental para obtener una visión exhaustiva de todas las cuentas de usuario en el sistema, incluyendo atributos como `Disabled` (si la cuenta está deshabilitada), `Domain` (dominio al que pertenece), `LocalAccount` (si es una cuenta local), `Name` (nombre de usuario), `PasswordChangeable` (si la contraseña puede ser cambiada), `PasswordExpires` (si la contraseña expira), `SID` (identificador de seguridad), y `Status` (estado de la cuenta).
    * **Cómo se realiza**: Ejecutando el comando en una consola de PowerShell o CMD.
    * **Objetivo**: Obtener un informe detallado de las características y atributos de todas las cuentas de usuario en el sistema.

* **Mostrar información completa del usuario actual**:
    * **Comando**: `whoami /all`
    * **Sintaxis y Elementos**:
        * `whoami`: Comando que muestra el nombre de usuario del usuario actual, el SID (Security Identifier) y los grupos a los que pertenece.
        * `/all`: Modificador que indica que se debe mostrar toda la información disponible, incluyendo el nombre de usuario, el SID del usuario, los grupos a los que pertenece con sus respectivos SIDs y atributos (como "Mandatory group", "Enabled by default", "Group owner"), y los privilegios (permisos) asociados al usuario.
    * **Porqué de la acción**: Es esencial para verificar rápidamente la identidad y los privilegios efectivos del usuario que está ejecutando la sesión, lo cual es crítico para la gestión de permisos y la resolución de problemas de acceso.
    * **Cómo se realiza**: Ejecutando el comando en una consola de PowerShell o CMD.
    * **Objetivo**: Obtener una visión completa de la información del usuario actual, incluyendo pertenencia a grupos y privilegios.

* **Mostrar grupos a los que pertenece el usuario actual**:
    * **Comando**: `whoami /groups`
    * **Sintaxis y Elementos**:
        * `whoami`: Comando que muestra el nombre de usuario del usuario actual, el SID (Security Identifier) y los grupos a los que pertenece.
        * `/groups`: Modificador que especifica que solo se debe mostrar la información relacionada con los grupos a los que pertenece el usuario actual.
    * **Porqué de la acción**: Es útil para obtener una lista concisa de los grupos de seguridad que afectan los permisos del usuario actual, sin la información adicional proporcionada por `/all`.
    * **Cómo se realiza**: Ejecutando el comando en una consola de PowerShell o CMD.
    * **Objetivo**: Identificar rápidamente los grupos a los que pertenece el usuario actual para entender sus permisos heredados.

## Permisos NTFS y Listas de Control de Acceso (ACLs)

En el sistema de archivos NTFS, las Listas de Control de Acceso (ACLs) son fundamentales para definir los permisos que usuarios, grupos o programas tienen sobre los objetos (archivos y carpetas).

Existen tres tipos de Listas de Control de Acceso:

* **DACL (Discretionary Access Control List)**: Son discrecionales, lo que significa que son definidas por el administrador o el propietario del objeto. Permiten otorgar o denegar permisos específicos a usuarios y grupos.
* **MACL (Mandatory Access Control List)**: Son obligatorias y predefinidas por el sistema. No están bajo el control del usuario o propietario de un objeto y no existe una forma gráfica de establecerlas o administrarlas.
* **SACL (System Access Control List)**: Son reglas del sistema que permiten auditar el acceso a los objetos. Se utilizan para registrar eventos de seguridad, como intentos de acceso exitosos o fallidos.

### Gestión de Permisos NTFS

El sistema de permisos NTFS se puede gestionar tanto gráficamente como por línea de comandos.

* **Gestión Gráfica**: Se realiza a través de las propiedades de los objetos (archivos o carpetas) en la pestaña **Seguridad**. Esta pestaña permite añadir o remover usuarios/grupos y asignar permisos como "Control total", "Modificar", "Lectura y ejecución", "Lectura" y "Escritura".

    * **Concepto de Herencia de Permisos**: Los permisos pueden ser heredados de la carpeta padre a los objetos hijos. Es posible modificar o configurar la herencia de permisos para un objeto determinado. También se pueden convertir los permisos heredados en permisos propios del objeto o eliminar la herencia.
    * **Permisos Efectivos**: La pestaña de "Permisos efectivos" o "Acceso efectivo" ofrece la posibilidad de auditar el acceso de un usuario específico, mostrando los permisos resultantes de la combinación de los grupos a los que pertenece y los permisos asignados directamente.

* **Gestión por Línea de Comandos con `icacls`**:

    * **Comando**: `icacls`
    * **Sintaxis y Elementos**: `icacls <NombreRuta> [/grant[:r] <SID|Nombre>:<Perms>...] [/deny <SID|Nombre>:<Perms>...] [/remove[:g|:p] <SID|Nombre>...] [/t] [/c] [/l] [/q] [/setowner <SID|Nombre>] [/findsid <SID|Nombre> [/t] [/c] [/l] [/q]] [/verify [/t] [/c] [/l] [/q]] [/save <ArchivoACL> [/t] [/c] [/l] [/q]] [/restore <ArchivoACL> [/c] [/l] [/q]] [/setintegritylevel <Nivel>:<OID>...] [/inheritance:e|d|r]`. Este comando tiene numerosos parámetros para la administración detallada de ACLs. Algunos de los parámetros más comunes son:
        * `<NombreRuta>`: La ruta al archivo o directorio sobre el que se aplicarán los permisos.
        * `/grant[:r] <SID|Nombre>:<Perms>`: Otorga los permisos especificados (`<Perms>`) al SID o nombre de usuario/grupo. El `:r` opcional significa reemplazar los permisos existentes.
        * `/deny <SID|Nombre>:<Perms>`: Deniega los permisos especificados.
        * `/remove[:g|:p] <SID|Nombre>`: Elimina todos los permisos para el SID o nombre. `:g` remueve permisos concedidos, `:p` remueve permisos denegados.
        * `/t`: Realiza la operación en todos los archivos y subdirectorios.
        * `/c`: Continúa la operación incluso si ocurren errores.
        * `/l`: Opera sobre el vínculo simbólico en lugar del destino.
        * `/q`: Suprime los mensajes de éxito.
        * `/setowner <SID|Nombre>`: Cambia el propietario del objeto.
        * `/inheritance:e|d|r`: Controla la herencia de permisos. `e` habilita la herencia, `d` deshabilita la herencia copiando las ACEs heredadas, `r` deshabilita la herencia eliminando las ACEs heredadas.
    * **Porqué de la acción**: `icacls` es la herramienta de línea de comandos estándar para ver, modificar, respaldar y restaurar ACLs de archivos y carpetas NTFS. Es indispensable para la automatización de tareas y para administraciones remotas o en entornos de scripting.
    * **Cómo se realiza**: Se ejecuta en una consola de PowerShell o CMD. Permite una granularidad y control que la interfaz gráfica no siempre ofrece.
    * **Objetivo**: Administrar de forma precisa los permisos NTFS, permitiendo la automatización y el control avanzado sobre los accesos a los objetos del sistema.

### Recomendaciones para la Gestión de Permisos

* **Configuración por "Permitir"**: La forma correcta de trabajar con permisos de seguridad es configurar permisos de "permitir". Si algo no está permitido, se asume una denegación implícita.
* **Uso Prudente de "Denegar"**: Los permisos de "denegar" solo deben asignarse en situaciones muy específicas, ya que prevalecen sobre los permisos de "permitir" y pueden llevar a configuraciones complejas y difíciles de depurar.
* **Asignación a Grupos y Carpetas**: Se recomienda asignar permisos a grupos en lugar de a usuarios individuales, y a carpetas en lugar de a archivos. Esto permite una administración más eficiente, especialmente en entornos con muchos usuarios y recursos.
* **Movimiento y Copia de Archivos**: Al mover o copiar archivos entre volúmenes con sistemas NTFS, los permisos propios del objeto se conservan, pero no los permisos heredados.

## Conclusiones

La gestión de identidades y un buen conocimiento de los grupos asignados a los usuarios, junto con la administración de permisos sobre los objetos del sistema, ofrecen un mecanismo eficiente para gestionar correctamente el acceso a datos, servicios y dispositivos. Es fundamental entender las características y detalles de todos estos elementos para mantener niveles adecuados de seguridad en el sistema de archivos NTFS y los objetos de Windows.