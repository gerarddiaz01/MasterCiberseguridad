### Informe de Ciberseguridad: Perfiles de Usuario, Gestión y Proceso de Arranque en Windows

#### Introducción: La Ley del Mínimo Privilegio

Una de las bases fundamentales de la seguridad informática es la **Ley del Mínimo Privilegio**. Esta ley establece que un usuario debe tener solo los permisos necesarios para realizar sus tareas, y no más. Desde Windows Vista, el usuario administrador está deshabilitado por defecto, y la práctica ideal es tener una cuenta de usuario con privilegios de administrador para tareas específicas y otra, de uso habitual, que sea una cuenta de usuario estándar sin privilegios. Una política adecuada de uso y administración de usuarios ayuda a mitigar los efectos del **Malware** y reduce la capacidad de operación de **software** malicioso.

#### Perfiles de Usuario en Windows

Los usuarios de un equipo tienen un directorio personal (`users`) donde se almacena su documentación y configuraciones, al cual solo ese usuario puede acceder. En un entorno de dominio, las identidades de usuario se gestionan de forma centralizada desde un controlador de dominio. En entornos locales, se recomienda almacenar los datos del usuario en un volumen separado del sistema operativo para facilitar la gestión de permisos, cuotas de disco y procesos de respaldo.

* **Ubicación del Perfil:** Los perfiles de usuario se almacenan junto con su identificador de seguridad (**SID**) en el registro de Windows, en la ruta `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`.
* **Modificación de la Ruta:** Se puede modificar la ruta del perfil de usuario alterando el valor `ProfileImagePath` en el registro. También se puede cambiar la ruta base de creación de perfiles modificando una variable del sistema. Es importante copiar las carpetas `Default User` y `All Users` manteniendo sus permisos originales al reubicar los perfiles para que Windows pueda aplicar el perfil modelo a los nuevos usuarios.

#### Proceso de Arranque del Sistema (Boot Process)

El proceso de arranque del sistema es un elemento clave para evitar que programas no autorizados permanezcan instalados y se ejecuten en cada inicio de sesión o arranque del equipo. Un **Malware** puede tratar de alojarse en puntos de ejecución durante este proceso para pasar desapercibido y persistir en el sistema.

* **Etapas del Arranque:**
    1.  **Session Manager (smss.exe):** Inicia el modo de usuario. Antes de esto, se ejecutan programas como `autocheck` para verificar la integridad del disco.
    2.  **Servicios:** Se ejecutan los servicios en modo automático.
    3.  **Interfaz de Inicio de Sesión:** Aparece la pantalla de usuario y contraseña.
    4.  **Carga de la Interfaz Gráfica:** La librería `GINA` (`Graphical Identification and Authentication`) lanza `explorer.exe` (que maneja el escritorio y la barra de tareas) y `userinit.exe` (que crea el entorno del usuario).
    5.  **Ejecución de Programas de Inicio:** Finalmente, se ejecutan los programas definidos en las claves `Run` del registro y los programas en la carpeta `Startup`.

El **Malware** suele alojarse en las claves de registro `HKEY_LOCAL_MACHINE` o `HKEY_CURRENT_USER`. En versiones recientes de Windows, el usuario estándar tiene menos privilegios y no puede escribir en la rama global (`HKEY_LOCAL_MACHINE`), por lo que los ataques se concentran más en el contexto de usuario actual (`HKEY_CURRENT_USER`).

#### Herramientas para la Gestión de Usuarios y el Arranque

Windows ofrece diversas consolas para la administración de usuarios y la configuración del arranque, lo que es esencial para fortificar el sistema:

| Herramienta | Uso Principal | Características Clave |
| :--- | :--- | :--- |
| **Configuración de Windows** | Gestión de cuentas de usuario, opciones de inicio de sesión y sincronización con cuentas de la nube. | Interfaz moderna, permite añadir usuarios, cambiar el tipo de cuenta y configurar preguntas de seguridad (con precaución). |
| **Administración de Equipos** | Creación y gestión avanzada de usuarios y grupos locales. | Permite crear usuarios, asignar contraseñas, modificar la pertenencia a grupos (ej., `Administrators`), y redirigir perfiles a rutas locales o en la red. |
| **`msconfig`** | Herramienta gráfica para gestionar el arranque del sistema. | Permite modificar elementos de inicio, ver servicios (pudiendo ocultar los de Microsoft para un análisis más claro), y lanzar otras herramientas de recuperación. En las últimas versiones de Windows, la gestión de programas de inicio se ha trasladado al Administrador de Tareas. |

#### Solución del Ejercicio: Creación de Usuarios Locales sin Privilegios

El ejercicio propuesto consiste en crear dos usuarios locales sin privilegios de administración utilizando dos consolas diferentes. A continuación, se detalla el procedimiento paso a paso:

##### 1. Crear el Primer Usuario desde la Configuración de Windows

* **Paso 1: Navegar a la configuración de usuarios.**
    * Ir a **Inicio** > **Configuración**.
    * Seleccionar **Cuentas**.
    * Hacer clic en **Otros usuarios** y luego en **Agregar otra persona a este equipo**.
* **Paso 2: Crear la cuenta local.**
    * Seleccionar la opción "No tengo la información de inicio de sesión de esta persona".
    * Elegir "Agregar un usuario sin una cuenta de Microsoft".
* **Paso 3: Ingresar los detalles de la cuenta.**
    * Introducir un nombre de usuario y una contraseña.
* **Paso 4: Configurar las preguntas de seguridad.**
    * Este paso es obligatorio. Es crucial responder estas preguntas con información falsa o que no sea personal. Esto evita que un atacante, mediante un ataque de **ingeniería social**, pueda responderlas para obtener acceso no autorizado a la cuenta si olvida la contraseña.
* **Paso 5: Verificar el tipo de cuenta.**
    * Una vez creado, el usuario por defecto es "estándar", sin privilegios de administrador. Si se desea, se puede cambiar el tipo de cuenta aquí.

##### 2. Crear el Segundo Usuario desde la Administración de Equipos

* **Paso 1: Abrir la consola de Administración de Equipos.**
    * Hacer clic derecho en el botón de **Inicio** y seleccionar **Administración de Equipos**.
* **Paso 2: Navegar a la sección de usuarios.**
    * En el panel izquierdo, ir a **Usuarios y grupos locales** > **Usuarios**.
* **Paso 3: Crear el nuevo usuario.**
    * Hacer clic derecho en el panel de usuarios y seleccionar **Usuario nuevo...**.
* **Paso 4: Ingresar los detalles de la cuenta.**
    * Completar el nombre de usuario, nombre completo y descripción.
    * Establecer una contraseña y confirmar las opciones de la misma (ej., "El usuario debe cambiar la contraseña en el siguiente inicio de sesión").
* **Paso 5: Configurar la cuenta.**
    * El usuario se crea por defecto como miembro del grupo de "Usuarios", sin privilegios de administrador. Desde las propiedades del usuario, en la pestaña "Miembro de", se puede ver y modificar su pertenencia a grupos.

##### 3. Revisar las Opciones de Configuración del Usuario Local

Desde las consolas de administración, se pueden revisar y configurar diversas opciones para el usuario, tales como:
* **Contraseña:** Cambiar la contraseña de la cuenta.
* **Perfil:** Administrar la ruta de almacenamiento del perfil del usuario.
* **Pertenencia a Grupos:** Asignar o eliminar al usuario de grupos como `Administrators`.
* **Opciones de Inicio de Sesión:** Sincronización de datos con cuentas de la nube (si aplica).

#### Conclusión

La administración de identidades es un punto clave de la seguridad moderna. Una política de usuarios bien definida, basada en el principio de mínimo privilegio, es crucial para fortificar un sistema Windows. El conocimiento del proceso de arranque y el uso de herramientas como `msconfig` o el Administrador de Tareas son esenciales para detectar y prevenir que programas no autorizados se ejecuten, asegurando la integridad del sistema desde el inicio.