Documentos de Referencia: "Fortificación de bases de datos - MYSQL.pdf"

# Informe Técnico: Fortificación del Servicio MySQL

### 1. Resumen Ejecutivo

Este informe detalla la fortificación de sistemas de bases de datos, centrándose específicamente en **MySQL**. Se explican los conceptos de fortificación y la importancia de la seguridad en las bases de datos, destacando los riesgos y amenazas comunes como la inyección SQL y el robo de datos. Se presentan los procedimientos prácticos para instalar, configurar y asegurar un servidor MySQL en una máquina Ubuntu. Esto incluye la creación de nuevos usuarios con privilegios mínimos, el cambio del nombre del usuario `root`, la eliminación de usuarios anónimos y la restricción de la dirección de escucha. Además, se aborda el uso del script `mysql_secure_installation` para automatizar estas tareas y se explican los mecanismos para controlar los privilegios de los usuarios y la carga de archivos locales.

***

### 2. Conceptos Fundamentales

* **Fortificación de Bases de Datos:** Se refiere a la implementación de medidas de seguridad para proteger la **integridad**, **confidencialidad** y **disponibilidad** de la información almacenada en las bases de datos. Esto incluye la aplicación de políticas de seguridad, buenas prácticas y el uso de herramientas adicionales, como firewalls, para mitigar accesos no autorizados, pérdida de datos y otros ataques cibernéticos.
    * **Importancia:** Las bases de datos a menudo contienen información crítica y sensible, como datos personales, comerciales y financieros. Un compromiso de la base de datos puede causar pérdidas económicas y de reputación, así como violaciones regulatorias.

* **Amenazas y Riesgos Comunes:**
    * **Acceso no autorizado:** Intrusiones con el objetivo de robar información.
    * **Denegación de servicio (DDoS):** Ataques que impiden a los usuarios legítimos conectarse a las bases de datos.
    * **Inyección SQL (SQL Injection):** Ataques que explotan vulnerabilidades para ejecutar comandos SQL maliciosos, robar o manipular datos.
    * **Pérdida de datos:** Puede ocurrir debido a errores humanos, que pueden llevar a la corrupción o borrado accidental de datos.
    * **Robo de información:** Los atacantes pueden tener motivaciones financieras o maliciosas para robar datos confidenciales.

* **Objetivos de la Fortificación:**
    * **Confidencialidad:** Proteger la información almacenada de la exposición.
    * **Integridad:** Garantizar que los datos no sean modificados de forma no autorizada.
    * **Disponibilidad:** Asegurar que los usuarios autorizados puedan acceder a los datos cuando sea necesario.
    * **Cumplimiento:** Adherirse a requisitos legales y regulatorios relacionados con la privacidad y seguridad de la información.

* **MySQL:** Es un sistema de gestión de bases de datos relacionales (SGBDR) de código abierto, popular por su flexibilidad, escalabilidad y facilidad de uso. A pesar de ser muy utilizado, es crucial fortificarlo para proteger la información de miles o millones de aplicaciones que se alojan en él.

***

### 3. Procedimientos Prácticos

A continuación, se detallan los procedimientos para fortificar un servidor MySQL en una máquina virtual Ubuntu.

#### 3.1. Instalación y Primer Acceso

1.  **Actualizar e instalar MySQL Server:**
    * **Comando:** `sudo apt install mysql-server`.
    * **Explicación:** Este comando descarga e instala el servidor MySQL en el sistema.

2.  **Verificar el estado del servicio:**
    * **Comando:** `sudo systemctl status mysql`.
    * **Explicación:** Se comprueba que el servicio de MySQL está cargado y en ejecución. La salida muestra detalles como el PID, la memoria utilizada y el tiempo de actividad de la CPU, como se muestra en la captura de pantalla.

3.  **Primer acceso a la base de datos:**
    * **Comando:** `sudo mysql -u root`.
    * **Explicación:** Este comando se utiliza para acceder a la base de datos con el usuario `root`. El uso de `sudo` permite la conexión sin necesidad de una contraseña.
    * **Comando:** `SHOW DATABASES;`.
    * **Explicación:** Una vez en el prompt de MySQL, se usa esta sentencia SQL para listar las bases de datos existentes, como se muestra en la captura de pantalla.

4.  **Salir de la sesión de MySQL:**
    * **Comando:** `exit`.
    * **Explicación:** Se cierra la sesión interactiva con el servidor de bases de datos.

#### 3.2. Configuración Inicial de Seguridad (Sentencias SQL)

1.  **Crear un usuario con privilegios de administrador:**
    * **Comando:** `CREATE USER 'aromero'@'localhost' IDENTIFIED BY 'aromero147';`.
    * **Explicación:** Crea un nuevo usuario con una contraseña para su uso como administrador, en lugar de depender exclusivamente del usuario `root`.
    * **Comando:** `GRANT ALL PRIVILEGES ON *.* TO 'aromero'@'localhost';`.
    * **Explicación:** Asigna todos los privilegios al nuevo usuario.
    * **Comando:** `FLUSH PRIVILEGES;`.
    * **Explicación:** Recarga los privilegios para que los cambios surtan efecto.

2.  **Renombrar el usuario `root`:**
    * **Comando:** `UPDATE mysql.user SET user="ubuntu" WHERE user="root";`.
    * **Explicación:** Se cambia el nombre del usuario `root` para dificultar los ataques dirigidos a este usuario predecible. Se verifica el cambio con `SELECT user FROM mysql.user;`.

3.  **Eliminar usuarios anónimos:**
    * **Comando:** `SELECT user, host FROM mysql.user WHERE user="";`.
    * **Explicación:** Se busca cualquier usuario sin nombre, que se crea por defecto en algunas instalaciones y puede suponer un riesgo de seguridad.
    * **Comando:** `DROP USER ""@"localhost";`.
    * **Explicación:** Se elimina el usuario anónimo encontrado. Se verifica el cambio volviendo a ejecutar el comando `SELECT`.

#### 3.3. Configuración de Seguridad Adicional (Archivo de Configuración)

1.  **Restringir la dirección de escucha:**
    * **Comando:** `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`.
    * **Explicación:** Se edita el archivo de configuración principal de MySQL. Se busca la directiva `bind-address` y se cambia su valor a `127.0.0.1` en lugar de `0.0.0.0`, lo que restringe el acceso al servidor solo desde el **localhost**, impidiendo conexiones desde hosts remotos como una máquina Kali Linux, como se muestra en la captura de pantalla.
    * **Comando:** `sudo systemctl restart mysql`.
    * **Explicación:** Se reinicia el servicio para aplicar la nueva configuración.
    * **Verificación:** Un intento de conexión desde una máquina remota (`mysql -h 10.0.2.15`) ahora resultará en un error de conexión, confirmando que la restricción funciona, como se muestra en la captura de pantalla.

2.  **Controlar la carga de archivos locales:**
    * **Comando:** `sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`.
    * **Explicación:** Se edita el mismo archivo para comentar la directiva `secure_file_priv`. Inicialmente, al estar vacía, la directiva permitía la lectura de cualquier archivo del sistema. Al comentarla, se asigna un valor por defecto que restringe la lectura a un directorio específico (`/var/lib/mysql-files/`), lo que previene que un atacante lea archivos sensibles del sistema como `/etc/passwd`.
    * **Comando de verificación:** `SHOW VARIABLES LIKE 'secure_file_priv';`.
    * **Resultado:** La salida del comando muestra el valor por defecto de la directiva, confirmando que la lectura de archivos está restringida a un directorio seguro, como se muestra en la captura de pantalla.

3.  **Control de privilegios:**
    * **Comando:** `SELECT DISTINCT(grantee) FROM information_schema.user_privileges;`.
    * **Explicación:** Lista los usuarios que tienen privilegios en el sistema.
    * **Comando:** `SHOW GRANTS FOR 'aromero'@'localhost';`.
    * **Explicación:** Muestra los permisos específicos de un usuario.
    * **Recomendación:** La buena práctica es revisar estos privilegios y asignar el principio de mínimo privilegio, concediendo solo los permisos estrictamente necesarios, ya que el usuario de demostración tenía permisos totales como se muestra en la captura de pantalla.

#### 3.4. Script de Instalación Segura

1.  **Ejecutar el script de seguridad:**
    * **Comando:** `sudo mysql_secure_installation`.
    * **Explicación:** Este script guía al usuario a través de una serie de preguntas para aplicar configuraciones de seguridad de forma rápida y automatizada. Incluye opciones para validar contraseñas, eliminar usuarios anónimos, deshabilitar el acceso remoto del usuario `root` y eliminar la base de datos de prueba, como se muestra en las capturas de pantalla.

***

### 4. Conclusiones y Puntos Clave

* **Importancia y Beneficios de Seguridad:** La fortificación de bases de datos es un aspecto fundamental de la ciberseguridad, dado el valor de la información que contienen. La aplicación de medidas de seguridad proactivas, como las políticas de usuario y el control de acceso, es crucial para proteger la confidencialidad, integridad y disponibilidad de los datos.

* **Puntos de Aprendizaje Clave:**
    * Se ha comprendido la importancia de fortificar las bases de datos y se han identificado las principales amenazas a las que se enfrentan.
    * Se han aprendido las medidas de seguridad clave para un servidor MySQL, como el uso de contraseñas seguras, la creación de usuarios con privilegios limitados y la auditoría constante.
    * Se ha dominado la instalación de MySQL y su configuración inicial.
    * Se han aprendido a realizar tareas de fortificación manuales con sentencias SQL, como renombrar el usuario `root`, eliminar usuarios anónimos y controlar la carga de archivos.
    * Se ha explorado la utilidad del script `mysql_secure_installation` como una herramienta eficiente para automatizar la configuración de seguridad básica.

* **Relevancia Técnica:** Los procedimientos de fortificación de MySQL son habilidades esenciales para cualquier profesional de la administración de sistemas o la ciberseguridad. Implementar el principio de mínimo privilegio, asegurar el acceso remoto y automatizar la configuración inicial son prácticas estándar que garantizan que las bases de datos, que a menudo son el activo más valioso de una organización, estén protegidas contra una amplia gama de amenazas. El conocimiento de las herramientas y los comandos adecuados permite una administración más segura y eficiente del servicio de bases de datos.