Documentos de Referencia: "5-22 Active Directory.pdf", "FSW Clase 22 – Active Directory.pdf"

# Informe Detallado sobre Active Directory y Active Directory Domain Service

## ¿Qué es un Dominio y un Controlador de Dominio?

Un **dominio** es un entorno de administración centralizada que opera en un contexto de confianza. Permite la creación de cuentas para usuarios, grupos y equipos. La administración centralizada se encarga de los procesos de autenticación y autorización. Un dominio requiere de uno o más **controladores de dominio (DC)**, que son servidores esenciales para su funcionamiento. Estos servidores tienen la responsabilidad de almacenar una copia de la base de datos del directorio activo. Esta base de datos se mantiene sincronizada de forma permanente entre todos los controladores de dominio que pertenecen al mismo dominio.

Debido a que el servicio que ofrecen los controladores de dominio es crítico, se recomienda tener al menos dos servidores por cada dominio. Si uno de los controladores deja de funcionar, los procesos de autenticación y autorización se verían comprometidos, pero con un segundo DC, el servicio puede continuar respaldado.

## Directorio Activo, Active Directory Domain Services y Bosques

El **Directorio Activo** es el servicio de directorio que organiza y administra los recursos de red. El **Active Directory Domain Services (AD DS)** es el rol principal que se instala en un servidor para convertirlo en un controlador de dominio. A través de este servicio, se pueden crear dominios, árboles de dominio y bosques.

Un **árbol de dominio** es una estructura jerárquica que puede contener dominios hijos. Por ejemplo, si existe el dominio `EMPRESA.COM`, un dominio hijo podría ser `MAIL.EMPRESA.COM`. Los dominios dentro del mismo árbol comparten una relación de confianza y seguridad. Un **bosque** es una estructura de ámbito superior que contiene dominios. Cuando se crea el primer dominio, también se crea un bosque, que normalmente tiene el mismo nombre que el dominio.

La frontera de seguridad en un entorno de Active Directory se establece a nivel de bosque. Todos los dominios que forman parte del mismo bosque tienen una relación de confianza implícita. Para tener dominios completamente independientes a nivel de seguridad, es necesario configurarlos en bosques distintos.

## Instalación Práctica de un Controlador de Dominio

La instalación de un controlador de dominio se puede realizar a través de Windows PowerShell o mediante el entorno gráfico. A continuación se describe el proceso utilizando el Server Manager:

1.  **Añadir el Rol**: En el Server Manager, se navega a "Manage" (Administrar) y se selecciona "Add Roles and Features" (Añadir roles y características). Después de avanzar, se selecciona el servidor y, en la lista de roles, se marca "Active Directory Domain Services". Este es el rol principal, aunque existen otros roles relacionados como Certificate Service o Federation Service. Se procede a instalar el rol.
2.  **Promover el Servidor**: Una vez que la instalación de las características termina, se presenta la opción de promover el servidor a controlador de dominio. Durante este proceso, un asistente guía al usuario. En la primera opción, se decide qué se quiere desplegar.
3.  **Seleccionar la Operación de Despliegue**: Las opciones principales son:
    * `Add a domain controller to an existing domain`: Para añadir un DC a un dominio ya existente.
    * `Add a new domain to an existing forest`: Para crear un dominio hijo o un dominio nuevo dentro de un bosque ya existente.
    * `Add a new forest`: Se utiliza para crear el primer dominio y, por consiguiente, un nuevo bosque.
4.  **Configurar el Nivel Funcional**: Durante la configuración, se pregunta por el nivel funcional del bosque y del dominio. Este nivel, que puede ir de 2008 a 2016, determina las características de Active Directory disponibles. Un nivel funcional de `Windows Server 2016` no permite tener controladores de dominio con versiones de sistema operativo inferiores a 2016.
5.  **Opciones del Controlador de Dominio**:
    * Se puede configurar el servidor para que sea también un **servidor DNS**. Se recomienda que todos los controladores de dominio actúen como servidores DNS para resolver las peticiones del dominio.
    * Se debe seleccionar si el servidor será un **Catálogo Global**, lo cual es obligatorio para el primer controlador de dominio de un nuevo dominio.
    * Se puede elegir si será un **controlador de dominio de solo lectura (RODC)**. Un RODC es una copia secundaria que no puede realizar cambios en el Directorio Activo y es útil en sucursales donde la seguridad es una preocupación. El primer DC de un dominio nunca puede ser un RODC.
6.  **Modo de Restauración**: Se debe establecer una contraseña para el modo de restauración del Directorio Activo. Esta clave es necesaria para restaurar la base de datos a un estado anterior, por ejemplo, a partir de una copia de seguridad. Es crucial no confundirla con la clave de administrador del dominio.
7.  **Almacenamiento de la Base de Datos**: Se especifica la ubicación para la base de datos de Active Directory (`NTDS.dit`) y la carpeta `SYSVOL`. En un entorno de producción, es una buena práctica almacenar estos archivos en un volumen de disco separado del volumen del sistema.
8.  **Verificación de Prerrequisitos e Instalación**: El sistema verifica los prerrequisitos. Es común que aparezcan advertencias relacionadas con el servicio DNS, ya que el servidor se encarga de instalarlo si no existe. Se procede con la instalación y, al finalizar, se requiere un reinicio obligatorio del servidor.

### La importancia del servicio DNS

La resolución de la mayoría de los recursos en el Directorio Activo se realiza a través de peticiones del servicio DNS. Los controladores de dominio utilizan registros de servicio (SRV) para permitir la resolución de recursos del tipo `_Service._Protocol.DomainName`.

## Catálogo Global

El **catálogo global** es una base de datos parcial de solo lectura que contiene todos los objetos del Directorio Activo. Su función principal es permitir la localización de recursos en otros dominios que pertenecen al mismo bosque. Un catálogo global es obligatorio en el primer controlador de dominio instalado en un nuevo dominio.

## Proceso de Autenticación

El proceso de autenticación en un dominio se realiza de la siguiente manera:

1.  El usuario se autentica en el controlador de dominio. El usuario debe demostrar su identidad, lo cual puede implicar el uso de una contraseña, autenticación multifactor, etc.
2.  Una vez que el usuario ha superado el proceso de autenticación, el controlador de dominio le emite un ticket TGT (Ticket Granting Ticket).
3.  El usuario utiliza este ticket TGT para acceder a los recursos de la red.
4.  El controlador de dominio, a través del servicio Kerberos y un sistema de distribución de claves (Key Distribution Center - KDC), valida el ticket y emite permisos para que el usuario acceda a los recursos solicitados.

## Herramientas y Consolas de Administración

Una vez que se ha instalado el rol de Active Directory, se dispondrá de una serie de herramientas de administración accesibles desde el menú "Tools" del Server Manager:

* **Active Directory Administrative Center**: Proporciona una interfaz gráfica para la administración general.
* **Active Directory Users and Computers**: Permite crear y gestionar usuarios, grupos y cuentas de equipos. También se pueden crear **Unidades Organizativas (OU)**, que son contenedores especiales para aplicar delegaciones o políticas de grupo (GPOs).
* **Active Directory Sites and Services**: Para la administración de la topología de la red.
* **Active Directory Domains and Trusts**: Para gestionar las relaciones de confianza entre dominios.
* **Active Directory Schema snap-in**: Permite la gestión del esquema del directorio activo, que define los atributos de los objetos (como usuarios, equipos, etc.). Por ejemplo, el atributo `distinguishedName` identifica un objeto de forma única, mientras que el `objectSID` es un identificador de seguridad único.
* **Active Directory module for Windows PowerShell**: Para la administración del Directorio Activo a través de la línea de comandos.
* **Consola de administración del servicio DNS**: Es una herramienta crucial, ya que la resolución de recursos del directorio activo se realiza a través de DNS.

## Ejercicio: Instalación del Rol de AD DS, Creación de Dominio y Unión de un Equipo Cliente

A continuación, se detalla el proceso para realizar el ejercicio propuesto:

### 1. Configuración de la Conectividad de Red
Antes de iniciar, es fundamental asegurarse de que las máquinas virtuales (el servidor y el cliente) estén en la misma red virtual. Para ello, se accede a la configuración de red de las máquinas y se selecciona la misma "red interna".

### 2. Preparación del Servidor
En el servidor que será el controlador de dominio, se deben realizar las siguientes configuraciones previas:
* **Dirección IP**: Se asigna una dirección IP estática en la misma subred que los equipos cliente. Por ejemplo, `192.168.1.11`.
* **Servidor DNS**: Se configura la dirección DNS del servidor para que apunte a sí mismo (`192.168.1.11` o `127.0.0.1`).
* **Nombre del Equipo**: Es muy importante cambiar el nombre del equipo antes de instalar el rol de AD DS para evitar conflictos.

### 3. Instalación del Rol de Active Directory Domain Services
1.  En el Server Manager, se selecciona "Manage" > "Add Roles and Features".
2.  Se avanza hasta la sección "Server Roles" y se marca "Active Directory Domain Services". Se aceptan las características adicionales y se procede a la instalación.
3.  Una vez finalizada la instalación, se hace clic en el enlace para "Promote this server to a domain controller" (Promover este servidor a controlador de dominio).

### 4. Creación de un Nuevo Dominio en un Nuevo Bosque
1.  En el asistente de configuración, se selecciona la opción "Add a new forest" (Añadir un nuevo bosque).
2.  Se introduce un nombre de dominio válido, por ejemplo, `HackersAcademy.com`.
3.  Se establece la contraseña para el modo de restauración del Directorio Activo.
4.  Se especifican las ubicaciones para la base de datos del Directorio Activo y la carpeta `SYSVOL`. Se reitera que en un entorno de producción, deben estar en un volumen de disco separado.
5.  Se revisan las opciones de configuración y se procede a la instalación. El equipo solicitará un reinicio al finalizar.

### 5. Configuración del Equipo Cliente y Unión al Dominio
1.  En el equipo cliente (por ejemplo, Windows 11), se accede a la configuración de red.
2.  Se asigna una dirección IP estática en la misma subred del servidor (ej. `192.168.1.5`).
3.  Se configura el servidor DNS para que apunte a la dirección IP del controlador de dominio (`192.168.1.11`).
4.  Se accede a la configuración del sistema, se navega a "About" y se selecciona "Domain or Workgroup" para cambiar la pertenencia del equipo.
5.  Se elige la opción "Domain" y se introduce el nombre del dominio creado (`HackersAcademy.com`).
6.  Se solicita un usuario y una contraseña con permisos para unir equipos al dominio. Al introducirlos, el equipo se une al dominio.
7.  El equipo cliente requerirá un reinicio obligatorio.

### 6. Verificación en el Servidor
Una vez que el equipo cliente se ha reiniciado:
* En el Server Manager del controlador de dominio, se abre la consola de "Active Directory Users and Computers".
* En el contenedor de "Computers", se debería ver la cuenta del equipo cliente que se acaba de unir.
* En la consola de DNS, en la zona de búsqueda directa del dominio, aparecerá el registro del equipo cliente con su dirección IP correspondiente.

---

Documentos de Referencia: "5-24 usuarios y grupos.pdf", "FSW Clase 24 – Usuarios y Equipos de Active Directory.pdf"

# Usuarios y Equipos en Active Directory

## Cuentas de Usuario y sus Propiedades

Las cuentas de usuario representan una identidad que un usuario o trabajador del dominio utiliza para acceder a los recursos de la red. Permiten o deniegan el acceso a equipos, procesos, recursos y servicios. También se usan para administrar los permisos de los recursos de red. Las cuentas de usuario pueden crearse a través de diferentes herramientas:

* **Active Directory Users and Computers**
* **Active Directory Administrative Center**
* **Windows PowerShell**
* **Línea de comandos** con utilidades como `dsadd`.

Al gestionar usuarios, es crucial considerar que el nombre de usuario debe tener un formato único. El **User Principal Name (UPN)**, por ejemplo, `nombredeusuario@sufijoUPN`, es el nombre con el que el usuario inicia sesión. Por otro lado, el **distinguishedName** es una cadena de texto con un formato específico (por ejemplo, `CN=Angel,CN=Users,DC=Hackers,DC=com`) que sirve como identificador para que Active Directory reconozca el objeto. El **Identificador de Seguridad (SID)**, por su parte, es un objeto único que se crea al dar de alta un usuario. Es el SID, y no el nombre de usuario o el UPN, lo que se asocia a los permisos que se otorgan a los recursos, servicios o aplicaciones.

Las propiedades de usuario se dividen en categorías:

* **Cuenta**: Contiene el nombre y los apellidos del usuario, así como los nombres de inicio de sesión **UPN** y **SAMAccountName**. También incluye configuraciones sobre las horas de inicio de sesión, la fecha de expiración de la cuenta y opciones de contraseña.
* **Organización**: Almacena datos descriptivos de la empresa como el departamento o la compañía.
* **Perfil**: Permite configurar perfiles de usuario, especificando si los datos se almacenan en el dispositivo local o en un servidor centralizado en una ubicación de red. Se puede usar el formato **Universal Naming Convention (UNC)** con la variable `%username%` para la ruta del perfil, como `\\LON-FS\profile$\%username%`.
* **Miembro de**: Muestra los grupos a los que pertenece el usuario.
* **Password Settings**: Opciones avanzadas de contraseña.
* **Policy & Authentication policy silos**: Se utilizan para los procesos de autenticación.
* **Extensiones**: Permite ver atributos de un objeto, como el `distinguishedName` y el `SID`.

### Gestión Práctica de Cuentas de Usuario

Desde el **Active Directory Administrative Center**, en la sección del dominio, se pueden gestionar objetos. Es recomendable activar la **papelera de reciclaje (Recycle Bin)** del dominio, lo cual crea un contenedor de objetos eliminados para facilitar la recuperación.

Para crear un usuario, se va a "Users" y se selecciona "New" > "User". Se deben introducir el **UPN** y la contraseña, ya que son datos cruciales para el inicio de sesión.

La configuración de las propiedades del usuario es una medida de seguridad importante. Por ejemplo:
* **Log on hours**: Permite restringir las horas en las que un usuario puede iniciar sesión. Si un empleado no trabaja el fin de semana, se puede denegar el inicio de sesión durante ese periodo, lo que reduce la superficie de ataque y mejora la capacidad de reacción ante un posible incidente.
* **Log on to**: Permite especificar en qué equipos el usuario puede iniciar sesión, limitando su acceso a los dispositivos que realmente necesita, lo cual es una medida de seguridad adicional.

Para las tareas de gestión, también se puede utilizar la consola **Active Directory Users and Computers**. Por defecto, esta consola no muestra todas las opciones, pero si se habilita "Advanced Features" en el menú "View", se hacen visibles pestañas adicionales, como el "Attribute Editor".

Para eliminar un usuario, simplemente se hace clic derecho sobre él y se selecciona "Delete". Si la papelera de reciclaje está activada, el usuario se moverá al contenedor de "Deleted Objects". Desde allí, se puede restaurar a su ubicación original o a otra unidad organizativa.

Otra acción de seguridad es **desactivar un usuario**. Esto es útil cuando un empleado está de vacaciones o de baja, ya que evita que la cuenta sea utilizada y limita la superficie de ataque.

## Grupos de Active Directory

Para una gestión eficiente de los permisos en organizaciones grandes, los usuarios se organizan en **grupos**. Los permisos se otorgan a los grupos en lugar de a usuarios individuales, lo que simplifica su mantenimiento.

Existen dos tipos principales de grupos:

1.  **Grupos de Distribución**: Se usan principalmente para el envío de correo electrónico. No tienen un SID, por lo que no se les pueden asignar permisos de seguridad.
2.  **Grupos de Seguridad**: Tienen un SID, lo que permite asignarles permisos de seguridad para acceder a recursos.

Los grupos también tienen diferentes áreas de ámbito:

| Tipo de Grupo | Descripción |
| :--- | :--- |
| **Grupos Locales** | Permiten acceso a recursos solo en el equipo local. |
| **Grupos Locales de Dominio** | Otorgan acceso a los recursos del dominio. |
| **Grupos Globales** | Brindan acceso a objetos en todo el bosque. |
| **Grupos Universales** | Combinan características de los grupos globales y locales, ideales para redes con múltiples dominios. |

Los grupos globales, por defecto, otorgan privilegios a lo largo de todos los dominios de un bosque. Esta es la razón por la que un usuario de un dominio puede acceder a recursos de otro dominio si ambos están en el mismo bosque, gracias a la relación de confianza implícita.

### Grupos con Privilegios

Existen grupos de seguridad especiales y con privilegios controlados por el sistema operativo:

| Grupo | Ubicación |
| :--- | :--- |
| **Enterprise Admins** | Contenedor de usuarios del dominio raíz del bosque. |
| **Schema Admins** | Contenedor de usuarios del dominio raíz del bosque. |
| **Administrators** | Contenedor `Built-in` de cada dominio. |
| **Domain Admins** | Contenedor de usuarios de cada dominio. |
| **Server Operators** | Contenedor `Built-in` de cada dominio. |
| **Account Operators** | Contenedor `Built-in` de cada dominio. |
| **Backup Operators** | Contenedor `Built-in` de cada dominio. |
| **Print Operators** | Contenedor `Built-in` de cada dominio. |
| **Cert Publishers** | Contenedor de usuarios de cada dominio. |

Estos grupos deben ser gestionados con mucho cuidado, y es vital tener control sobre qué usuarios pertenecen a ellos y cuándo utilizan sus privilegios.

## Cuentas de Equipo y Canales Seguros

Las **cuentas de equipo** representan los dispositivos que se han unido a un dominio. Por defecto, estas cuentas se almacenan en el contenedor `Computers`, pero es recomendable usar **Unidades Organizativas (UO)** para una mejor administración. Las UO permiten delegar el control y personalizar la configuración a través de políticas de grupo.

Cuando un equipo se une a un dominio, se establece un **canal seguro** entre el equipo y el controlador de dominio (DC). El servicio `Net Logon` utiliza las credenciales de la cuenta de equipo para establecer este canal. El equipo almacena una contraseña que se actualiza automáticamente cada 30 días, y esta debe coincidir con la del DC para que la comunicación sea correcta.

Este canal seguro puede romperse en varias situaciones:
* Al reinstalar un equipo con el mismo nombre, lo que genera un nuevo SID y contraseña.
* Si la contraseña del equipo no coincide con la del DC.
* Al restaurar un equipo desde una copia de seguridad o un punto de control de virtualización.
* Al sacar un equipo del dominio y volver a unirlo, lo que genera un nuevo SID.

El problema de obtener un nuevo SID es que si se habían otorgado permisos basados en el SID anterior, estos permisos dejarán de funcionar, ya que el SID del equipo ha cambiado.

Para restaurar el canal seguro sin sacar el equipo del dominio, se pueden usar las siguientes opciones:

* **Comando `nltest`**: `nltest /server:servername /sc_reset:domain\domaincontroller`.
* **Comando `netdom`**: `netdom reset MachineName /domain DName /UserO UName /PasswordO {Password *}`.
* **Windows PowerShell**: `Test-Computer SecureChannel -Repair`.
* **Consola gráfica**: En "Active Directory Users and Computers" o "Administrative Center", se puede usar la opción "Reset Account" (Restablecer cuenta).

## Conclusiones

Comprender el funcionamiento de los objetos en AD DS es fundamental para mantener la seguridad de todo el dominio. Una correcta planificación de grupos, permisos y la estructura de contenedores basada en unidades organizativas (UO) permite crear organizaciones seguras y escalables.

---

Documentos de Referencia: "5-25 Unidades organizativas.pdf", "FSW Clase 25 – Unidades Organizativas y Delegaciones.pdf"

# Informe Detallado sobre Unidades Organizativas (UO) en Active Directory

## Unidades Organizativas: Concepto, Utilidad y Repercusiones en Seguridad

Las **Unidades Organizativas (UO)** son un tipo de objeto fundamental que se puede crear dentro de **Active Directory**. Funcionan como contenedores lógicos que permiten almacenar y clasificar otros objetos de infraestructura, tales como **usuarios**, **grupos** y **cuentas de equipo**. La creación de una estructura de UOs adecuada es esencial para una gestión eficiente y segura de los recursos en un dominio.

### Propósito y Organización

El principal propósito de las UOs es facilitar la **clasificación** de los objetos de Active Directory según las necesidades de la organización. Esta clasificación puede basarse en diversos criterios, como:

* **Ubicación geográfica:** Por ejemplo, UOs para países (España, Francia, Inglaterra, Portugal) y, dentro de ellos, para regiones o provincias (Asturias, Madrid, Cataluña, Murcia).
* **Departamentos:** UOs para contabilidad, comercial, directivos, IT, etc.
* **Sucursales:** Permitiendo una organización granular por cada sede de la empresa.

Esta estructura jerárquica, similar a carpetas dentro de carpetas, pero con funcionalidades avanzadas, permite una administración más granular y simplificada. Al clasificar los objetos de esta manera, se pueden aplicar configuraciones o delegar permisos de forma específica a los elementos contenidos en cada UO.

### Repercusiones en Seguridad

Las UOs son un pilar fundamental para mantener la **seguridad** y **planificar las configuraciones** en un dominio. Permiten crear entornos seguros y escalables al:

* **Aplicar configuraciones específicas:** Las UOs son el único elemento, junto con los **Sitios** y **Dominios**, al que se pueden asignar configuraciones mediante **Objetos de Directiva de Grupo (GPO)**. Esto significa que las configuraciones se aplican únicamente a los usuarios, equipos o grupos dentro de una UO específica, evitando la aplicación global de políticas que podrían ser inapropiadas para ciertas partes de la organización.
* **Delegación eficiente de control:** Permiten asignar **privilegios específicos** para tareas determinadas a usuarios o grupos concretos, y lo más importante, en **lugares específicos** de la organización (es decir, dentro de una UO particular). Esto evita la necesidad de añadir usuarios a grupos con privilegios excesivos, como el grupo de administradores de dominio, lo que reduce la superficie de ataque y minimiza el riesgo de acciones no autorizadas.

Es crucial destacar que no se pueden enlazar GPOs directamente a los contenedores por defecto de Active Directory, como el contenedor de **Users** o el de **Computers**, ya que no son Unidades Organizativas. Si todos los usuarios y equipos permanecieran en estos contenedores predeterminados, sería imposible aplicar configuraciones específicas de forma granular.

## ¿Qué son los Group Policy Objects (GPO)?

Los **Group Policy Objects (GPO)**, u Objetos de Directiva de Grupo, son colecciones de configuraciones que se aplican a usuarios y equipos en un entorno de Active Directory. Estas configuraciones pueden abarcar una amplia gama de aspectos, desde políticas de seguridad (como requisitos de contraseña, bloqueo de cuentas), configuraciones de software, scripts de inicio/apagado, hasta configuraciones de escritorio y redirección de carpetas.

La principal ventaja de los GPO es su capacidad para **clasificar y aplicar configuraciones** de manera centralizada y eficiente. Como se mencionó anteriormente, los GPO solo pueden ser enlazados a **Sitios**, **Dominios** o **Unidades Organizativas**. Esto permite a los administradores definir políticas una vez y aplicarlas automáticamente a miles de usuarios o equipos, garantizando la consistencia y el cumplimiento de las políticas de seguridad y operativas en toda la organización.

Por defecto, en un dominio de Active Directory, existen algunas directivas predefinidas:

* **Default Domain Policy:** Una directiva que se aplica a todo el dominio.
* **Default Domain Controllers Policy:** Una directiva específica para los controladores de dominio.

Estas directivas predeterminadas son un punto de partida, pero la verdadera flexibilidad y control se obtienen al crear GPO personalizados y enlazarlos a las UOs para aplicar configuraciones específicas donde se necesiten.

## Organizational Units (OU) Delegate Control

La función de **OU Delegate Control** (Delegación de Control de Unidad Organizativa) es una de las ventajas más significativas de utilizar las UOs. Permite a los administradores asignar **privilegios específicos** para una determinada tarea a usuarios o grupos, y limitar el alcance de esos permisos a una UO particular.

Esto se logra a través de un **asistente de delegación (Delegation of Control Wizard)** que guía al administrador a través del proceso. En lugar de otorgar permisos amplios a un usuario o grupo (como hacerlos administradores de dominio), la delegación de control permite conceder permisos muy granulares, como:

* Crear, borrar y administrar cuentas de usuario.
* Restablecer contraseñas de usuario y forzar el cambio de contraseña en el siguiente inicio de sesión.
* Leer toda la información de usuario.
* Crear, borrar y administrar grupos.
* Modificar la pertenencia a un grupo.
* Generar un Conjunto Resultante de Política (Resultant Set of Policy o RSoP).
* Crear objetos personalizados (como cuentas de equipo).

La clave de esta funcionalidad es que el usuario o grupo delegado solo podrá realizar la tarea asignada y **solo dentro de la UO o UOs específicas** donde se le ha otorgado ese permiso. Por ejemplo, un usuario podría tener permiso para crear cuentas de equipo, pero únicamente en la UO de su país o departamento. Esto es crucial para el principio de **privilegio mínimo**, donde a los usuarios se les otorgan solo los permisos necesarios para realizar sus funciones, reduciendo el riesgo de errores o abusos.

## Demostración Práctica: Creación y Gestión de Unidades Organizativas y GPO

La demostración práctica en una máquina virtual ilustra el proceso detallado de cómo trabajar con Unidades Organizativas, configurar delegaciones y asignar GPO.

### 1. Acceso a las Herramientas de Administración

El primer paso es acceder a la consola de **Active Directory Users and Computers**. Esto se realiza desde el **Server Manager Dashboard**:

* Navegar a **Tools** (Herramientas).
* Seleccionar **Active Directory Users and Computers** (Usuarios y equipos de Active Directory).

### 2. Creación de Nuevos Objetos de Unidad Organizativa

Una vez en la consola de Active Directory Users and Computers, se procede a crear una nueva UO:

* En el panel izquierdo, seleccionar el dominio principal (ej., `Hackers.Academy`).
* Hacer clic derecho sobre el dominio, seleccionar **New** (Nuevo) y luego **Organizational Unit** (Unidad Organizativa).
* Aparecerá el cuadro de diálogo **New Object - Organizational Unit**.
* **Name:** Introducir el nombre de la nueva UO (ej., `España`).
* **Protect container from accidental deletion:** Es una opción importante que debe mantenerse marcada por defecto para evitar eliminaciones accidentales de la UO.
* Hacer clic en **OK**.

Una vez creada la UO principal, se pueden crear UOs anidadas para construir una estructura jerárquica más detallada. Por ejemplo, dentro de la UO `España`, se pueden crear UOs para `Madrid`, `Barcelona`, etc. Esto se hace seleccionando la UO `España`, haciendo clic derecho, y repitiendo el proceso de "New > Organizational Unit".

### 3. Estructura de un Dominio con Unidades Organizativas

La demostración muestra cómo se puede construir un esqueleto organizativo basado en las necesidades de la empresa. Por ejemplo, una estructura podría ser:

* `Hackers.Academy` (Dominio)
    * `EEUU` (UO)
        * `BOSTON` (UO)
        * `NEW YORK` (UO)
    * `England` (UO)
    * `Spain` (UO)

Una vez que la estructura de UOs está definida, los usuarios y equipos existentes, que por defecto se encuentran en los contenedores `Users` y `Computers`, pueden ser movidos a las UOs correspondientes. Para mover un usuario:

* Navegar al contenedor `Users`.
* Hacer clic derecho sobre el usuario deseado.
* Seleccionar **Move...** (Mover...).
* En el cuadro de diálogo, seleccionar la UO de destino (ej., `España`).
* Hacer clic en **OK**.

Este proceso de mover objetos a las UOs es fundamental para que las configuraciones y delegaciones específicas de UO puedan aplicarse correctamente.

### 4. Configuración de Organizational Unit Delegate Control

Para configurar la delegación de control en una UO:

* Hacer clic derecho sobre la UO deseada (ej., `España`).
* Seleccionar **Delegate Control...** (Delegar control...).
* Se abrirá el **Delegation of Control Wizard** (Asistente para la delegación de control).
* **Welcome to the Delegation of Control Wizard:** Hacer clic en **Next** (Siguiente).
* **Users or Groups:** Hacer clic en **Add...** (Agregar...) para seleccionar el usuario o grupo al que se le delegarán los permisos.
    * Introducir el nombre del usuario o grupo (ej., `angel`) y hacer clic en **Check Names** (Comprobar nombres) para verificarlo.
    * Hacer clic en **OK** y luego en **Next**.
* **Tasks to Delegate:** Aquí se seleccionan las tareas comunes que se desean delegar. Se puede elegir entre:
    * **Delegate the following common tasks:** Una lista de tareas predefinidas (ej., "Create, delete, and manage user accounts", "Reset user passwords and force password change at next logon").
    * **Create a custom task to delegate:** Permite una personalización más profunda de los permisos. Si se elige esta opción:
        * **Active Directory Object Type:** Se puede especificar si la delegación se aplica a "This folder, existing objects in this folder, and creation of new objects in this folder" o a tipos de objetos específicos (ej., "Computer objects", "User objects").
        * **Permissions:** Se seleccionan los permisos específicos (ej., "Full Control", "Read", "Write", "Create All Child Objects", "Delete All Child Objects", "Read All Properties").
* Hacer clic en **Next** y luego en **Finish** para completar la delegación.

Este proceso permite otorgar permisos muy específicos a usuarios o grupos, limitando su alcance a una UO determinada, lo que es una práctica de seguridad recomendada para evitar el exceso de privilegios.

### 5. Asignación de Configuraciones mediante Objetos de Directivas de Grupo (GPO)

Finalmente, la demostración aborda cómo asignar configuraciones a las UOs mediante GPO.

* Desde el **Server Manager Dashboard**, navegar a **Tools** (Herramientas).
* Seleccionar **Group Policy Management** (Administración de directivas de grupo).
* En la consola de **Group Policy Management**, se puede ver la estructura del dominio.
* Navegar a la UO a la que se desea enlazar un GPO (ej., `España`).
* Hacer clic derecho sobre la UO y seleccionar **Link an Existing GPO...** (Vincular un GPO existente...) o **Create a GPO in this domain, and Link it here...** (Crear un GPO en este dominio y vincularlo aquí...).

Al enlazar un GPO a una UO, todas las configuraciones definidas en ese GPO se aplicarán a los usuarios y equipos contenidos en esa UO, así como a las UOs anidadas, siguiendo la herencia de GPO. Esto proporciona un control granular sobre las políticas aplicadas en diferentes segmentos de la organización.

## Conceptos Aprendidos

Este informe ha detallado la importancia de las Unidades Organizativas en Active Directory como contenedores lógicos para la clasificación de usuarios, grupos y equipos. Hemos explorado cómo estas UOs son fundamentales para la seguridad y la eficiencia administrativa, permitiendo la aplicación granular de configuraciones a través de los Group Policy Objects (GPO) y la delegación de control específica.

Se ha enfatizado que los GPO solo pueden enlazarse a Sitios, Dominios o Unidades Organizativas, lo que subraya la necesidad de una estructura de UOs bien diseñada para una gestión efectiva. La delegación de control de UO se presenta como una herramienta poderosa para implementar el principio de privilegio mínimo, permitiendo a los usuarios realizar tareas específicas dentro de un ámbito limitado sin otorgarles permisos excesivos.

La demostración práctica ha ilustrado el flujo de trabajo para crear UOs, organizar objetos dentro de ellas, delegar control y vincular GPO, proporcionando una comprensión completa de cómo estas funcionalidades se aplican en un entorno real de Active Directory. La correcta implementación de UOs y GPO es crucial para mantener un entorno de red seguro, escalable y fácilmente administrable.

---

