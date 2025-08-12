Documentos de Referencia: "FSL Clase 9 – Sudoers.pdf"

# Informe Técnico: Sudoers

## 1. Resumen Ejecutivo

Este informe detalla la configuración del archivo **sudoers** en sistemas GNU/Linux, un componente crucial para la seguridad del sistema. Se analizan sus secciones principales (Defaults, Alias, ACLs e Include) y su sintaxis. A través de ejemplos prácticos, se demuestra cómo configurar permisos granulares, crear alias para usuarios y comandos, y gestionar la autenticación para diferentes perfiles de usuario. El objetivo es proporcionar una guía exhaustiva para aplicar buenas prácticas de seguridad, como el principio del mínimo privilegio, y evitar vulnerabilidades mediante una configuración cuidadosa y legible del archivo **sudoers**.

***

## 2. Conceptos Fundamentales

* **Sudoers**: Es un archivo de configuración esencial en sistemas GNU/Linux que determina qué usuarios tienen permisos para ejecutar qué comandos con los privilegios de otro usuario, comúnmente el usuario **root**. Su importancia radica en que permite definir **permisos granulares**, controlando el acceso a comandos privilegiados y reduciendo el riesgo de abuso o daño por parte de usuarios no autorizados.
* **Ubicación y Edición del Archivo**: El archivo **sudoers** se encuentra en la ruta `/etc/sudoers`. La práctica recomendada para modificar este archivo es utilizar el editor **visudo**. Este editor realiza una comprobación interna de sintaxis antes de guardar, asegurando que el archivo no quede en un estado inconsistente y previniendo posibles errores graves en el sistema.
* **Secciones Principales de `sudoers`**: El archivo está organizado en varias secciones que permiten una configuración estructurada de permisos.
    * **Defaults**: Esta sección permite establecer opciones predeterminadas que se aplican a todas las ejecuciones de `sudo`. Puede modificar comportamientos como el tiempo de sesión de la contraseña (`timestamp_timeout`), la duración del password (`passwd_timeout`), la activación del registro de comandos (`log_input`, `log_output`), y el uso de un pseudo terminal (`use_pty`). También puede aplicarse de forma global o a usuarios específicos.
    * **Alias**: La sección de alias permite definir nombres para agrupar usuarios, comandos, grupos o hosts. Los alias facilitan la legibilidad y simplifican la configuración, permitiendo agrupar usuarios en roles como "administradores" o "desarrolladores". Existen tres tipos de alias: `User_Alias` (para usuarios), `Host_Alias` (para máquinas) y `Cmnd_Alias` (para comandos).
    * **ACLs (Access Control Lists)**: Estas son las reglas específicas que definen qué usuarios pueden ejecutar comandos con los privilegios de otro usuario. En el archivo por defecto, se definen reglas para el usuario **root** y los grupos **admin** y **sudo**. El uso de la palabra reservada `ALL` indica que una regla se aplica a cualquier máquina o usuario.
    * **Include**: Esta directiva, ubicada al final del archivo, permite cargar la configuración de ficheros adicionales alojados en el directorio `/etc/sudoers.d/`. Es una práctica recomendada para mantener la configuración del archivo principal limpia y organizada.

***

## 3. Procedimientos Prácticos

### 3.1. Configuración de la Sección Defaults

Esta sección muestra cómo configurar directivas globales y específicas para usuarios.

1.  **Añadir un mensaje personalizado para contraseña incorrecta**:
    * **Comando**: `sudo visudo defaults`
    * **Propósito**: Abre el archivo `defaults` en el editor **visudo** para modificarlo.
    * **Acción**: Se añade la siguiente línea: `Defaults:lucas badpass_message="Hello Lucas, you were wrong, try again."`. Esto configura un mensaje personalizado para el usuario `lucas` cuando ingresa una contraseña incorrecta.
    * **Verificación**: Se utiliza el comando `su lucas` para cambiar de usuario. Luego, se ejecuta un comando como `sudo date` e se introduce una contraseña incorrecta. El sistema mostrará el mensaje personalizado en lugar del mensaje por defecto, como se ilustra en la captura de pantalla.

2.  **Configurar intentos de contraseña**:
    * **Comando**: `sudo visudo defaults`
    * **Propósito**: Modificar el archivo `defaults`.
    * **Acción**: Se añaden las siguientes líneas: `Defaults passwd_tries=3` (para establecer 3 intentos globales) y `Defaults:DEVELOPER passwd_tries=1` (para limitar el alias `DEVELOPER` a un solo intento). La directiva global se aplica a todos, mientras que la específica para el alias sobreescribe la global para los miembros de ese grupo.
    * **Verificación**: Se cambia de usuario a `lucas` (miembro del grupo `PERSONAL`) e se introduce una contraseña incorrecta tres veces, lo que resulta en la finalización de la ejecución. Posteriormente, se cambia de usuario a `luci` (miembro del grupo `DEVELOPER`) y se introduce una contraseña incorrecta una sola vez, lo que también finaliza la ejecución.

### 3.2. Configuración de Alias y ACLs (Reglas)

Este procedimiento demuestra cómo crear alias para usuarios y comandos, y luego aplicar reglas de acceso basadas en ellos.

1.  **Crear usuarios y agregarlos al grupo `sudo`**:
    * **Comandos**: `sudo useradd marco`, `sudo useradd lucas`, `sudo useradd sara`, `sudo useradd luci`. Luego, `sudo passwd` para establecer contraseñas para cada uno. Finalmente, `sudo usermod -aG sudo marco` y se repite para los otros tres usuarios.
    * **Propósito**: Se crean los usuarios y se les otorgan permisos iniciales para usar el comando `sudo`.

2.  **Crear alias de usuario**:
    * **Comando**: `sudo visudo alias`.
    * **Acción**: Se crea un archivo de alias separado en `/etc/sudoers.d/alias`. Se añaden los alias de usuario `ADMINISTRATOR`, `DEVELOPER` y `PERSONAL` con sus respectivos miembros, como se muestra en la captura de pantalla.
    * **Sintaxis**: `User_Alias ALIAS_NAME = user1, user2`.

3.  **Crear alias de comandos**:
    * **Comando**: `sudo visudo alias`.
    * **Acción**: Se crean dos alias de comando en el mismo archivo: `POWER` para comandos de apagado y reinicio, y `BASIC` para comandos básicos, negando los comandos de `POWER` y cualquier comando en `/bin`, excepto `date`.
    * **Sintaxis**: `Cmnd_Alias ALIAS_NAME = /path/to/command1, /path/to/command2`.

4.  **Crear reglas de acceso (ACLs)**:
    * **Comando**: `sudo visudo rules`.
    * **Acción**: Se crea un archivo de reglas en `/etc/sudoers.d/rules`.
        * Para el grupo `PERSONAL`, se establece la regla: `PERSONAL ALL=BASIC`. Esto permite a los usuarios del alias `PERSONAL` ejecutar solo los comandos del alias `BASIC`.
        * Para los `DEVELOPER`, se establece la regla: `DEVELOPER ALL=!BIN, !SBIN, /sbin/ip`. Esto niega la ejecución de todos los comandos en `/bin` y `/sbin`, pero permite específicamente el comando `/sbin/ip`.
        * Para los `ADMINISTRATOR`, se establece la regla: `ADMINISTRATOR ALL=(ALL) NOPASSWD: BIN, SBIN`. Esto permite a los administradores ejecutar cualquier comando en `/bin` y `/sbin` con cualquier usuario, sin necesidad de contraseña (`NOPASSWD`).

5.  **Verificación de reglas**:
    * Se cambia de usuario y se prueba la ejecución de comandos. Por ejemplo, al intentar `sudo reboot` como `lucas` (Personal), el sistema deniega el permiso, pero `sudo date` funciona. Al intentar `sudo ls` como `luci` (Developer), el sistema deniega el permiso, pero `sudo ip` funciona. Al intentar `sudo id` como `marco` (Administrator), el comando se ejecuta sin solicitar contraseña.

***

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

El archivo **sudoers** es un elemento crítico para la seguridad de los sistemas GNU/Linux, ya que su correcta configuración es fundamental para mitigar riesgos y prevenir vulnerabilidades. Al aplicar el **principio del mínimo privilegio**, se asegura que cada usuario tenga solo los permisos necesarios para su trabajo, evitando el abuso de la cuenta **root**. La utilización de alias y grupos mejora la legibilidad y el mantenimiento del archivo, haciendo que la gestión de permisos sea más clara y menos propensa a errores. Es vital evitar configuraciones inseguras y mantener el archivo actualizado, revisando periódicamente a los usuarios activos y las reglas definidas.

### 4.2. Puntos de Aprendizaje Clave

* **Edición Segura**: Siempre se debe utilizar **visudo** para modificar el archivo `sudoers` y sus inclusiones, ya que el editor valida la sintaxis para prevenir configuraciones inconsistentes.
* **Organización del Archivo**: La estructura de `sudoers` se basa en secciones como `Defaults`, `Alias` y `ACLs`, que permiten una configuración modular y organizada.
* **Uso de Inclusiones**: La directiva `include` permite delegar la configuración en archivos separados en el directorio `/etc/sudoers.d/`, mejorando la organización y facilitando la gestión de reglas complejas.
* **Sintaxis de las Reglas**: Las reglas de acceso (ACLs) se definen con una sintaxis específica, donde `User_Alias` y `Cmnd_Alias` permiten agrupar usuarios y comandos. El uso del símbolo `!` permite negar permisos, otorgando un control más granular.
* **Pruebas de Configuración**: Es crucial realizar pruebas exhaustivas para verificar que las reglas se aplican correctamente y que los usuarios tienen los permisos esperados, ni más ni menos.

### 4.3. Relevancia Técnica

Los procedimientos detallados en el documento son de gran relevancia técnica, ya que cubren el ciclo completo de la gestión de permisos en un entorno profesional. Desde la creación de usuarios y la asignación de grupos hasta la definición de políticas de seguridad personalizadas, cada paso está diseñado para construir un sistema seguro y auditable. La capacidad de configurar mensajes de error, limitar intentos de contraseña y restringir el acceso a comandos específicos demuestra un control avanzado sobre el sistema. La práctica de utilizar archivos de configuración adicionales (`/etc/sudoers.d/`) es un estándar en la administración de sistemas modernos, lo que hace que los conocimientos adquiridos sean directamente aplicables a entornos reales.