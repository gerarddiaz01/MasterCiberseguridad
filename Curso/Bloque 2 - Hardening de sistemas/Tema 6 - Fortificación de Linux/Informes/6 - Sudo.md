Documentos de Referencia: "FSL Clase 06 – Sudo - Sudoers.pdf"

# Informe Técnico: Sudo y Sudoers

## 1. Resumen Ejecutivo

Este informe detalla el uso del comando **sudo** en sistemas GNU/Linux, una herramienta esencial para la administración segura de servidores. Se explora el principio de mínimo privilegio, la estructura y los componentes de **sudo** (el comando, el archivo de configuración **sudoers** y el editor **visudo**), y se demuestran sus aplicaciones prácticas. El objetivo principal es capacitar a los administradores para ejecutar comandos con privilegios elevados de forma controlada, evitando el uso frecuente de la cuenta **root**, lo que mejora la seguridad y la auditabilidad del sistema.

***

## 2. Conceptos Fundamentales

* **Usuario root**: El usuario **root** es la cuenta del sistema con **privilegios absolutos** y acceso total al sistema. El uso indiscriminado de esta cuenta puede ocasionar acciones accidentales o maliciosas que pongan en riesgo el correcto funcionamiento del sistema. Por ello, se recomienda no usar la cuenta **root** con demasiada frecuencia y no compartir sus credenciales.
* **Principio del mínimo privilegio (least privilege principle)**: Una práctica de seguridad recomendada que consiste en otorgar a los usuarios solo los **privilegios mínimos** necesarios para realizar sus tareas correctamente, y nunca más allá de esos mínimos privilegios. El uso de **sudo** permite adherirse a este principio.
* **Sudo**: Acrónimo de "**superuser do**". Es una herramienta disponible en sistemas GNU/Linux que permite a los usuarios ejecutar comandos simulando ser otro usuario, generalmente **root**. Esto posibilita a los usuarios realizar tareas de administración, como la instalación de software, actualizaciones o la configuración de servicios, sin la necesidad de iniciar sesión como **root**.
* **Sesión activa de sudo**: Por defecto, al ejecutar **sudo**, se crea una sesión de **root** con una duración de 15 minutos. Durante este tiempo, los usuarios pueden ejecutar comandos con privilegios de **root** sin necesidad de reingresar la contraseña. Esta sesión se puede invalidar manualmente con el parámetro `-k`.
* **Componentes de sudo**: Sudo se compone de tres elementos principales:
    * **El comando `sudo`**: La herramienta que se usa para ejecutar otros comandos con privilegios elevados.
    * **El archivo `sudoers`**: Un archivo de configuración ubicado en `/etc/sudoers` que define qué usuarios o grupos pueden ejecutar qué comandos y con qué opciones.
    * **El comando `visudo`**: El editor recomendado para modificar el archivo `sudoers`. Se utiliza para evitar errores sintácticos que podrían dejar el sistema en un estado inconsistente.

***

## 3. Procedimientos Prácticos

### 3.1. Creación de un Usuario y Obtención de su ID

Para este ejercicio, se debe crear un nuevo usuario y obtener su identificador para su uso posterior.

1.  **Crear el usuario `sudotest`**:
    * **Comando**: `sudo useradd sudotest`.
    * **Propósito**: Crea un nuevo usuario en el sistema. Se necesita `sudo` ya que la creación de usuarios requiere permisos de administrador. El sistema solicitará la contraseña del usuario que ejecuta el comando para verificar sus permisos.
2.  **Obtener el identificador (ID) del nuevo usuario**:
    * **Comando**: `cat /etc/passwd`.
    * **Propósito**: Muestra el contenido del archivo `/etc/passwd`, que contiene una lista de todos los usuarios del sistema y sus IDs.
    * **Ejecución**: Al ejecutar el comando, se debe buscar el registro del usuario `sudotest` para encontrar su identificador. Como se muestra en la captura de pantalla del documento, el ID para `sudotest` es `1003`.

### 3.2. Ejecución de un Comando como Otro Usuario

Este procedimiento demuestra cómo ejecutar un comando con los privilegios de un usuario específico, en lugar de usar **root**.

1.  **Levantar una shell como el usuario `sudotest` utilizando su nombre**:
    * **Comando**: `sudo su sudotest`.
    * **Propósito**: Permite levantar una nueva shell con los privilegios del usuario especificado (`sudotest`).
2.  **Levantar una shell utilizando el ID del usuario**:
    * **Comando**: `sudo -s -u#1003`.
    * **Sintaxis y elementos**:
        * `sudo`: El comando principal para ejecutar con privilegios elevados.
        * `-s`: Parámetro que permite levantar una nueva shell.
        * `-u`: Parámetro que especifica el usuario con el que se desea ejecutar el comando, en lugar de usar **root** por defecto.
        * `#1003`: El identificador del usuario `sudotest`, precedido por `#` para indicar que se usa el ID en lugar del nombre.
    * **Verificación**: Se puede ejecutar el comando `whoami` dentro de la nueva shell para verificar que el usuario actual es `sudotest`.

### 3.3. Gestión de la Sesión Activa de Sudo

Estos pasos ilustran cómo gestionar la sesión de 15 minutos que **sudo** crea por defecto.

1.  **Levantar una shell como root con la sesión activa**:
    * **Comando**: `sudo -s`.
    * **Propósito**: Levanta una nueva shell con privilegios de **root**. Si ya existe una sesión activa (de menos de 15 minutos), no se solicitará la contraseña.
2.  **Invalidar la sesión activa de sudo**:
    * **Comando**: `sudo -k`.
    * **Propósito**: Invalida la sesión actual de **root**, eliminando la capacidad de ejecutar comandos sin reingresar la contraseña.
3.  **Verificar la invalidación de la sesión**:
    * **Acción**: Después de ejecutar `sudo -k`, se debe volver a ejecutar `sudo -s`.
    * **Resultado**: El sistema solicitará nuevamente la contraseña del usuario actual, confirmando que la sesión anterior fue terminada.

### 3.4. Obtención de Ayuda y Listado de Permisos

Estos procedimientos muestran cómo obtener información sobre las opciones de `sudo` y los permisos del usuario.

1.  **Obtener el listado de comandos permitidos**:
    * **Comando**: `sudo -l`.
    * **Propósito**: Muestra los permisos actuales de **sudo** para el usuario que ejecuta el comando. Como se muestra en la captura de pantalla, la salida `(ALL: ALL) ALL` indica que el usuario puede ejecutar cualquier comando como cualquier usuario o grupo.
2.  **Ver la ayuda del comando**:
    * **Comando**: `sudo -h`.
    * **Propósito**: Muestra todas las opciones y parámetros disponibles para el comando `sudo`.

***

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

El uso de **sudo** es una práctica fundamental en el endurecimiento de servidores GNU/Linux. Permite a los administradores delegar tareas específicas sin la necesidad de compartir las credenciales de la cuenta **root**, lo cual reduce significativamente el riesgo de incidentes de seguridad. Al implementar el principio de mínimo privilegio, se limita el daño potencial que podría causar un error accidental o una acción maliciosa. Además, `sudo` facilita la auditoría, ya que permite identificar qué usuarios han realizado acciones con privilegios de **root**.

### 4.2. Puntos de Aprendizaje Clave

* **Evitar el uso de `root`**: La cuenta `root` debe usarse lo menos posible debido a sus privilegios absolutos y el riesgo que conlleva.
* **Uso de `sudo`**: El comando `sudo` permite ejecutar tareas de administración de forma segura, simulando ser otro usuario, sin la necesidad de iniciar sesión como `root`.
* **Componentes de `sudo`**: La funcionalidad de `sudo` se basa en tres componentes: el comando `sudo`, el archivo de configuración `sudoers` y el editor `visudo`.
* **Gestión de sesiones**: `sudo` crea una sesión activa de 15 minutos por defecto, que se puede invalidar con el parámetro `-k`.
* **Configuración del archivo `sudoers`**: Este archivo, ubicado en `/etc/sudoers`, es crucial para definir los permisos de los usuarios. La edición de este archivo debe realizarse únicamente con el comando `visudo` para evitar errores sintácticos que podrían dejar el sistema inestable.

### 4.3. Relevancia Técnica

El dominio de **sudo** es esencial para cualquier profesional que administre sistemas GNU/Linux. La capacidad de controlar y auditar quién puede realizar tareas administrativas es un pilar de la seguridad informática. Conocer los parámetros (`-s`, `-u`, `-k`, `-l`, `-h`), la estructura del archivo `sudoers` y el uso del editor `visudo` proporciona las herramientas necesarias para implementar políticas de seguridad robustas y granulares. Esto permite a los administradores restringir permisos de manera precisa, asegurando que cada usuario solo tenga acceso a lo que necesita para su trabajo, en línea con el principio de mínimo privilegio.

