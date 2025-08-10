Documentos de Referencia: "5-17 Windows Server.pdf", "FSW Clase 18 – Introducción a Windows Server.pdf"

### Informe Detallado: Introducción y Administración de Windows Server

#### 1. Introducción a Windows Server

Windows Server es un sistema operativo de servidor que proporciona un conjunto de herramientas para configurar y desplegar servicios y aplicaciones, así como para monitorear y analizar procesos, servicios y el propio sistema operativo. A diferencia de un equipo o PC de escritorio, Windows Server está diseñado para funcionar como un servidor, un rol que exige un comportamiento óptimo y configuraciones correctas para evitar conflictos y degradar el funcionamiento de los servicios. Para una administración correcta, es crucial entender el funcionamiento de sus herramientas y la relación entre los diferentes roles y características. Un **servidor local** se refiere al servidor en el que se está trabajando directamente.

#### 2. Server Manager: Herramienta Central de Administración

El **Administrador del servidor** o **Server Manager** es la herramienta principal de administración en los sistemas operativos con entorno gráfico de Windows Server. Su función es permitir la administración local del servidor y ejecutar tareas de forma remota en otros dispositivos.

##### 2.1. Panel de Configuración y Dashboard

Al iniciar sesión en Windows Server, la primera herramienta que se abre es Server Manager, que actúa como un panel de control centralizado. Desde el dashboard, se pueden realizar varias operaciones clave:

* **Add roles and features (Añadir roles y características):** Permite instalar o eliminar roles, servicios o características en el servidor.
* **Add other servers to manage (Añadir otros servidores para administrar):** Facilita la administración centralizada de múltiples servidores. Los servidores pueden ser añadidos desde Active Directory, a través del servicio DNS o mediante un archivo de importación.
* **Create a server group (Crear un grupo de servidores):** Agrupa servidores para realizar una administración conjunta y centralizada.
* **Connect this server to cloud services (Conectar este servidor a servicios en la nube):** Permite integrar el servidor con servicios en la nube.

El dashboard también muestra elementos dinámicos que varían según el número de servidores y los roles desplegados, como el estatus de los roles y servicios instalados.

##### 2.2. Propiedades del Servidor Local (Local Server)

Dentro de Server Manager, la sección **Local Server** muestra información detallada y las consolas de administración para las tareas habituales del servidor. Desde aquí se pueden gestionar las siguientes propiedades:

* **Computer name (Nombre del equipo):** Es una tarea crucial que se debe realizar inmediatamente después de la instalación. Cambiar el nombre del equipo más tarde, especialmente en un servidor o controlador de dominio con varios roles instalados, puede generar conflictos en la infraestructura, ya que las configuraciones de otras máquinas pueden estar asociadas al nombre original.
* **Workgroup/Domain (Grupo de trabajo/Dominio):** Permite cambiar el nombre del grupo de trabajo o unir el equipo a un dominio. Para unirse a un dominio, se debe proporcionar un nombre de dominio válido y credenciales de usuario y contraseña autorizadas. Tanto el cambio de nombre como la unión a un dominio requieren reiniciar el servidor. Esto es un factor importante a considerar en entornos de producción.
* **Windows Defender Firewall:** La configuración del firewall de Windows puede ser gestionada desde aquí.
* **Remote Management (Administración remota):** Permite la administración del servidor desde otros dispositivos a través de Server Manager. Por defecto, la administración remota está habilitada.
* **Remote Desktop (Escritorio remoto):** Por razones de seguridad, el escritorio remoto suele estar deshabilitado por defecto debido a los ataques conocidos contra sus puertos y servicios. La administración remota a través de Server Manager se considera una alternativa más segura.
* **NIC Teaming:** Permite agrupar varios adaptadores de red para que funcionen como uno solo, una opción útil para la alta disponibilidad y el rendimiento de la red.
* **Propiedades del Adaptador de Red:** Desde aquí se puede acceder a la configuración del adaptador de red para configurar opciones como la dirección IP, la puerta de enlace y los servidores DNS.
* **Actualizaciones y Seguridad:** Se pueden gestionar las actualizaciones y la protección del navegador. Es una buena práctica de ciberseguridad no usar servidores para navegar por Internet. La protección en tiempo real de Windows Defender está disponible para navegadores si el servidor debe ser usado para navegar.

#### 3. Herramientas de Administración y Gestión Práctica

La sección **Tools (Herramientas)** de Server Manager proporciona acceso a una lista de consolas de administración. Esta lista es dinámica y varía según los roles y características instalados en el servidor. Algunas de las herramientas disponibles por defecto son:

* **Event Viewer (Visor de eventos):** Permite revisar los logs de eventos del sistema.
* **Performance Monitor (Monitor de rendimiento):** Muestra el impacto y la actividad del hardware del dispositivo.
* **Services (Servicios):** Consola para gestionar los servicios en el servidor.
* **Computer Management (Administración de equipos):** Consola de administración completa.
* **Registry Editor (Editor del Registro):** Permite editar el registro de Windows.
* **Windows PowerShell:** Consola de línea de comandos para la automatización de tareas.
* **Windows Defender Firewall with Advanced Security:** Herramienta para la gestión avanzada del firewall.

##### 3.1. Roles y Características

Windows Server se administra a través de **roles** y **características**.
* **Roles:** Son la función principal que desempeña el servidor en la red (ej. DHCP Server, DNS Server, Active Directory Domain Services).
* **Características:** Son funcionalidades adicionales que pueden ser instaladas para complementar un rol o funcionar de forma independiente.

Un aspecto crucial es que al instalar un rol, no se instalan todas sus características por defecto. El administrador debe saber qué características adicionales necesita y añadirlas posteriormente si es necesario. El proceso de instalación se realiza a través de un asistente al seleccionar **Add Roles and Features** en el dashboard de Server Manager.

##### 3.2. Creación de una Consola de Administración (ejemplo DNS)

Cuando se instala un rol, se añade automáticamente la consola de administración correspondiente en la sección de herramientas de Server Manager. Por ejemplo, al instalar el rol de servicio DNS, se crea la consola de administración de DNS.

* **Zonas (Zones):** Son bases de datos que contienen registros DNS. Existen zonas de búsqueda directa y de búsqueda inversa.
* **Registros (Records):** Son entradas dentro de una zona que asocian nombres a direcciones IP, como un registro `A`.

El proceso de configuración de estos servicios varía en complejidad; la instalación de un rol puede ser sencilla, pero su configuración, como en el caso de Active Directory, puede ser muy compleja y requiere un conocimiento profundo.

#### 4. Relación con la Ciberseguridad

Windows Server y sus herramientas son fundamentales para la ciberseguridad y la fortificación de sistemas.

* **Administración Segura:** La opción de administración remota a través de Server Manager, con el escritorio remoto deshabilitado por defecto, ofrece una alternativa más segura para gestionar servidores, ya que evita los riesgos asociados a los ataques conocidos contra los servicios de escritorio remoto.
* **Mínima Exposición:** Windows Server permite a los administradores instalar únicamente los roles y características necesarios, adhiriéndose al principio de mínima exposición. Esto reduce la superficie de ataque, ya que los componentes no instalados no pueden ser objetivo de un ataque.
* **Monitoreo y Análisis:** Las herramientas como el visor de eventos y el monitor de rendimiento permiten a los administradores supervisar el sistema en busca de actividades inusuales o problemas de seguridad, ayudando a detectar posibles amenazas y a mantener la infraestructura protegida.
* **Control de Acceso y Red:** Las configuraciones de firewall y la gestión de la red a través de NIC Teaming y las propiedades de los adaptadores de red, permiten un control estricto sobre las conexiones y el tráfico, impidiendo que agentes maliciosos penetren en el sistema.

---

Documentos de Referencia: "5-21 Event viewer.pdf", "FSW Clase 21 – Visor de Eventos.pdf"

### Visor de Eventos (Event Viewer) y Monitorización de Registros en Windows Server

#### 1. Configuración y Relación de los Registros con la Seguridad

El registro de eventos en Windows Server proporciona información detallada sobre el funcionamiento del sistema operativo, las aplicaciones y los servicios. Los registros se clasifican en eventos de información, advertencia, error y seguridad. La monitorización de estos registros es fundamental para la fortificación del sistema, ya que una actividad inusual en los logs puede ser un indicio de un ataque, un fallo en el sistema o una configuración incorrecta.

No todos los registros se generan de forma automática. Algunos, como los registros de auditoría de seguridad o de depuración (`debugging`), requieren una configuración previa para ser activados. Sin esta configuración, los eventos no se generarán y no se podrán visualizar. Esta relación entre la configuración y la monitorización es vital para una gestión de seguridad proactiva.

Existen varias maneras de configurar los registros, entre las que se incluyen:
* **Configuración Local:** Habilitar manualmente los registros necesarios para tareas específicas, como la auditoría.
* **Configuración Centralizada mediante Directivas de Grupo (GPO):** Se pueden configurar los ajustes del registro de eventos de forma centralizada para múltiples equipos. La ruta para esta configuración se encuentra en `Configuración de equipo\Políticas\Plantillas administrativas\Componentes de Windows\Servicio de registro de eventos`. Esta es una forma recomendada de mantener una configuración coherente y segura en toda la infraestructura.

#### 2. Visor de Eventos (Event Viewer)

El Visor de Eventos es la consola principal para ver los registros que se generan en el sistema operativo. Se puede acceder a ella desde el menú de `Herramientas` de `Server Manager`.

##### 2.1. Secciones del Visor de Eventos

Para facilitar la consulta, el Visor de Eventos divide la información en cuatro secciones principales:

* **Vistas Personalizadas (Custom Views):** Permiten agrupar eventos de un rol específico o crear vistas personalizadas con filtros sobre los eventos que nos interesa monitorizar. Si el servidor tiene roles instalados, se generarán automáticamente vistas para esos roles (por ejemplo, para el servicio DNS o Active Directory). Esto permite a un administrador centrarse en los registros relevantes para una tarea o función específica.
* **Registros de Windows (Windows Logs):** Estos se clasifican en las siguientes categorías:
    * `Application`: Eventos generados por las aplicaciones.
    * `Security`: Eventos de auditoría de seguridad, como los inicios de sesión. Para que se generen ciertos eventos de seguridad, la auditoría debe estar previamente activada.
    * `Setup`: Eventos relacionados con la instalación del sistema operativo y sus componentes.
    * `System`: Eventos del sistema operativo y sus componentes.
* **Registros de Aplicaciones y Servicios (Applications and Services Events):** Organiza los eventos por aplicación y fabricante. Dentro de la carpeta de Microsoft/Windows, se pueden encontrar los eventos asociados a componentes específicos de Windows, lo que es muy útil para diagnosticar problemas en una funcionalidad concreta como `BitLocker` o `DFS`.
* **Suscripciones (Subscriptions):** Esta sección se utiliza para gestionar las suscripciones de eventos, que permiten a un servidor actuar como un contenedor central para los registros de otros equipos. Los eventos recibidos se muestran en la sección de **Eventos reenviados (Forwarded Events)**.

##### 2.2. Funcionalidades Prácticas del Visor de Eventos

* **Propiedades de Eventos:** Al seleccionar un evento, se pueden ver sus propiedades y detalles técnicos. En algunos casos, incluso puede ofrecer posibles soluciones al problema.
* **Anclar Tareas a Eventos:** Una función poderosa es la capacidad de anclar una tarea a un evento específico. Por ejemplo, se puede configurar para que, ante múltiples fallos de inicio de sesión de un usuario administrador, se envíe un correo electrónico de alerta. Esto ayuda a detectar ataques de fuerza bruta. También se puede programar un script para reiniciar un servicio que ha fallado, automatizando la solución de problemas.
* **Filtros:** Se pueden crear filtros personalizados para buscar eventos específicos, como los de seguridad (`Security`) que sean críticos o de error en los últimos 30 días. Esto facilita la revisión de eventos importantes sin tener que examinar todos los registros.
* **Registro Centralizado:** Los registros pueden ser exportados y guardados, lo que permite su análisis por otros colegas o su almacenamiento para futuras auditorías.

#### 3. Suscripción de Eventos (Event Subscription)

La suscripción de eventos es una forma de centralizar la monitorización. Permite que varios equipos envíen sus registros a un servidor que actúa como contenedor central.

##### 3.1. Ventajas de la Suscripción de Eventos

* **Seguridad:** Un atacante puede tratar de borrar los registros de un equipo para ocultar su actividad. Si esos registros se han enviado a un servidor central, será mucho más difícil eliminarlos. Los registros en el servidor central serán más fiables para un análisis forense.
* **Fiabilidad:** Si un equipo deja de funcionar y no se puede acceder a sus registros, los logs enviados al servidor central pueden ayudar a entender la causa del fallo.

##### 3.2. Proceso de Configuración de la Suscripción de Eventos

Para habilitar la suscripción de eventos, se deben seguir estos pasos:

1.  **Permisos de Administrador:** El equipo que actuará como contenedor central debe ser añadido al grupo de administradores locales de cada equipo origen que enviará los datos.
2.  **Configuración del Origen:** En cada equipo que enviará los registros, se debe ejecutar el siguiente comando en una consola con privilegios elevados:
    * `winrm quickconfig`
3.  **Configuración del Contenedor Central:** En el servidor que recibirá los registros, se debe ejecutar el siguiente comando en una consola:
    * `wecutil qc`
4.  **Configurar la Suscripción:** Una vez configurados los permisos y ejecutados los comandos, se debe configurar la suscripción en el servidor de destino.
5.  **Verificar la Replicación:** Los eventos recibidos aparecerán en la sección `Eventos reenviados`, con el nombre de la máquina que los originó.

#### 4. Gestión de Eventos desde Server Manager y Directivas de Grupo

Los eventos del sistema también se pueden gestionar y visualizar de forma centralizada desde `Server Manager`. Aunque Server Manager muestra los registros de eventos de los servidores conectados, es importante tener en cuenta que habilitar un gran número de eventos para ser vistos en esta consola puede ralentizar su rendimiento.

Para una configuración a gran escala, se pueden utilizar **objetos de directiva de grupo (GPO)** para configurar los ajustes de los registros de eventos de forma centralizada en toda la organización, en lugar de hacerlo manualmente en cada equipo. Esto permite una gestión más eficiente y uniforme de las políticas de auditoría y seguridad.

---

Documentos de Referencia: "5-19 Ejercicio windows server.pdf", "FSW Clase 19 – Solución Ejercicio.pdf"

### Instalación y Verificación de Internet Information Services (IIS) en Windows Server

Este informe detalla el proceso paso a paso para instalar el rol de servidor web de Microsoft, **Internet Information Services (IIS)**, y verificar su correcto funcionamiento en un entorno de Windows Server.

#### 1. Proceso de Instalación de IIS en Windows Server

Para instalar el rol de IIS, se debe utilizar la herramienta principal de administración de Windows Server, el **Administrador del servidor (Server Manager)**. Siga los pasos a continuación:

1.  **Acceder al Administrador del servidor:** Desde el panel de administración de Windows Server, navegue hasta la sección `Manage` (Administrar) en la parte superior derecha de la ventana.
2.  **Iniciar el asistente de instalación:** Dentro del menú `Manage`, seleccione `Add Roles and Features` (Añadir roles y características). Esto abrirá un asistente que le guiará a través del proceso.
3.  **Configuración inicial:** En las primeras pantallas del asistente, haga clic en `Next` (Siguiente) en tres ocasiones para pasar por las opciones de `Before you begin`, `Installation Type` y `Server Selection`.
4.  **Seleccionar el rol de servidor:** En la pantalla `Select server roles` (Seleccionar roles de servidor), busque y marque la opción `Web Server (IIS)`.
5.  **Añadir características requeridas:** Al seleccionar el rol de IIS, aparecerá una ventana emergente para añadir las características de administración y otras herramientas necesarias. Haga clic en `Add Features` (Añadir características).
6.  **Confirmar la instalación:** Regrese al asistente de instalación y haga clic en `Next` (Siguiente) varias veces hasta llegar a la pantalla de confirmación. Aquí, verifique que `Web Server (IIS)` esté seleccionado y haga clic en `Install` (Instalar).
7.  **Finalizar la instalación:** El proceso de instalación se ejecutará en segundo plano. Una vez completado, el asistente mostrará un mensaje de éxito. Haga clic en `Close` (Cerrar).

#### 2. Verificación del Funcionamiento de IIS

Una vez finalizada la instalación, es crucial verificar que el servidor web está funcionando correctamente.

1.  **Abrir el navegador:** En el servidor, abra un navegador web (por ejemplo, Microsoft Edge).
2.  **Navegar a la página por defecto:** En la barra de direcciones, escriba `localhost` y presione Enter.
3.  **Confirmar la página de bienvenida:** Si la instalación fue exitosa, el navegador mostrará la página de bienvenida de Internet Information Services, confirmando que el servidor web está operativo.

#### 3. Administración y Opciones de Configuración de IIS

La instalación del rol de IIS agrega una consola de administración específica a la sección `Tools` (Herramientas) de Server Manager, llamada `Internet Information Services (IIS) Manager`. Esta consola es el punto central para configurar el servicio.

##### 3.1. Navegación en la Consola de Administración de IIS

* **Sitios (Sites):** En la consola, en el panel de `Connections` (Conexiones), se encuentra la sección de `Sites`. Por defecto, se crea un `Default Web Site` para propósitos de conectividad. Desde aquí, se pueden administrar los sitios web alojados en el servidor.
* **Opciones de Configuración:** Al seleccionar el servidor o un sitio específico, se muestran diferentes opciones de configuración, tanto a nivel de máquina como de sitio y de `Application Pools`.

##### 3.2. Roles y Características Adicionales de IIS

Durante la instalación inicial, el rol de IIS solo instala las características básicas. Existen muchas otras funcionalidades de diagnóstico, rendimiento y seguridad que se pueden añadir posteriormente.

Para agregar más características:

1.  **Volver al asistente:** En Server Manager, vaya a `Manage` y seleccione `Add Roles and Features`.
2.  **Explorar las características de IIS:** En el asistente, vaya a la sección `Web Server (IIS)` y expanda sus opciones. Verá que hay muchas características, especialmente en el apartado de `Security` (Seguridad), que no están instaladas por defecto.
3.  **Habilitar la autenticación de Windows:** Por ejemplo, para requerir que los usuarios tengan una cuenta y contraseña de Windows para ver el sitio web, se puede deshabilitar la `Anonymous Authentication` (Autenticación anónima) y habilitar la `Windows Authentication` (Autenticación de Windows).
4.  **Instalar y verificar:** Después de seleccionar las nuevas características, continúe con el proceso de instalación. Una vez finalizado, al abrir la consola de IIS y seleccionar el panel de `Authentication` (Autenticación), se verán las nuevas características disponibles.

Este proceso demuestra que, si bien la instalación de un rol es sencilla, la configuración completa requiere comprender y habilitar las características específicas necesarias para aprovechar al máximo las tecnologías y ventajas que el rol ofrece. La administración centralizada de Server Manager facilita la instalación y configuración de estos roles y sus características.

---

Documentos de Referencia: "5-20 Monitorizar windows server.pdf", "FSW Clase 20 – Monitorizar Windows Server.pdf"

### Informe Detallado: Monitorización en Windows Server y sus Herramientas

#### 1. Importancia de la Monitorización en Windows Server

Windows Server ofrece un conjunto de herramientas esenciales para monitorizar procesos, servicios y aplicaciones. La monitorización es fundamental para la seguridad del sistema porque permite analizar su comportamiento, detectar problemas en componentes que no funcionan eficientemente y encontrar elementos que, por una configuración incorrecta u otras razones, generen conflictos. Una carga de trabajo inusual en los componentes del sistema puede ser un indicativo de un ataque, un mal funcionamiento o una mala configuración.

Las principales herramientas de monitorización disponibles son:
* **Administrador de Tareas**
* **Monitor de Recursos**
* **Monitor de Rendimiento**
* **Monitor de Confiabilidad**

#### 2. Administrador de Tareas (Task Manager)

El Administrador de Tareas es la primera herramienta que se utiliza cuando un programa, servicio o el sistema operativo no funciona correctamente. Se puede lanzar con la combinación de teclas `Ctrl+Alt+Del` o haciendo clic derecho en la barra de tareas. Ofrece una vista preliminar de lo que está sucediendo en el dispositivo.

##### 2.1. Funcionalidades Detalladas del Administrador de Tareas

El Administrador de Tareas está dividido en varias secciones para clasificar la información:

* **Processes (Procesos):** Muestra las aplicaciones en ejecución y los procesos relacionados. Permite ver el consumo de recursos de CPU, memoria, disco y red.
* **Performance (Rendimiento):** Muestra gráficos de la carga de trabajo en la CPU, memoria, disco y red. Desde aquí, se puede lanzar el Monitor de Recursos.
* **Users (Usuarios):** Proporciona información sobre los procesos asociados a cada usuario.
* **Services (Servicios):** Lista los servicios en ejecución, su estado y el tipo de inicio (`Automático`, `Manual`, etc.). Desde aquí, se puede abrir la consola de servicios para una administración más detallada.
* **Details (Detalles):** Es la parte más completa. Muestra todos los procesos en ejecución con información detallada. Desde aquí se puede:
    * Finalizar un proceso o un árbol de procesos.
    * Ver la prioridad de ejecución del proceso.
    * Analizar la cadena de espera (`Analyze wait chain`).
    * Crear un volcado de memoria (`Create dump file`) para su posterior análisis.
    * Abrir la ubicación del archivo (`Open file location`), lo cual es útil para detectar si un proceso o un ejecutable se encuentra en una ubicación extraña, lo que podría ser un indicativo de malware.
    * Ver las propiedades y la firma digital del proceso, incluyendo el certificado digital, para verificar su legitimidad.
    * **Seleccionar Columnas:** Se pueden añadir columnas adicionales para obtener más información sobre los procesos, como `Virtualización del UAC`, `Privilegios elevados`, o el uso de tecnologías de seguridad como `Control Flow Guard`, lo que ayuda a determinar si un proceso es legítimo y más difícil de atacar.

#### 3. Monitor de Recursos (Resource Monitor)

El Monitor de Recursos es una herramienta de diagnóstico excelente para detectar rápidamente **cuellos de botella** en el sistema. Muestra gráficos y estadísticas en tiempo real sobre la carga de trabajo de la CPU, disco, red y memoria. Es especialmente útil para identificar qué procesos están causando una carga masiva en un componente específico.

* **Identificación de Problemas:** Ayuda a determinar si un componente está fallando, si un servicio no funciona correctamente, o si un rol instalado requiere más potencia de hardware (por ejemplo, más memoria RAM).
* **Análisis Detallado:** Permite ordenar los procesos por su impacto en cada componente (disco, CPU, etc.) y seleccionar procesos específicos para ver su actividad detallada en el gráfica, facilitando el aislamiento de la causa de un problema.

#### 4. Monitor de Rendimiento (Performance Monitor)

El Monitor de Rendimiento (`perfmon`) es una herramienta más avanzada que genera informes y estadísticas sobre el funcionamiento de los componentes del sistema a lo largo del tiempo, utilizando **contadores de rendimiento**.

* **Data Collector Sets (Recopiladores de datos):** El Monitor de Rendimiento trabaja con estos conjuntos para almacenar información específica del funcionamiento del sistema. Estos recopiladores pueden ser personalizados para ser muy específicos en lo que monitorizan.
* **Generación de Informes:** Los Data Collector Sets generan informes que pueden ser almacenados para crear una **línea base** de cómo funciona el sistema en condiciones normales. Esta línea base es crucial para detectar anomalías en el futuro.
* **Personalización:** Se pueden crear recopiladores de datos personalizados (`User Defined`) para monitorizar solo los componentes que interesan, decidiendo qué datos se capturan, cuándo y con qué frecuencia (`Sample Interval`). Esto permite crear análisis muy específicos y adaptados a las necesidades del administrador.
* **Alertas:** Es posible configurar alertas asociadas a los Data Collector Sets que se activarán cuando se cumplan ciertas condiciones, como que un valor supere un umbral específico.
* **Informes Detallados:** Los informes generados por el monitor de rendimiento son extremadamente detallados y contienen información exhaustiva sobre la CPU, memoria, disco, red y procesos, lo que ayuda a diagnosticar problemas complejos.

#### 5. Monitor de Confiabilidad (Reliability Monitor)

El Monitor de Confiabilidad es una herramienta que genera un gráfico con un índice de estabilidad del sistema, en una escala del 1 (muy inestable) al 10 (muy estable). Este monitor registra la estabilidad a lo largo del tiempo, basándose en la instalación de aplicaciones, actualizaciones de drivers y fallos del sistema.

* **Detección de Inestabilidad:** Permite detectar qué elementos han generado inestabilidad en el sistema, incluso si estos problemas pasaron desapercibidos en su momento.
* **Diagnóstico de Causa Raíz:** El gráfico muestra caídas en el índice de estabilidad asociadas a una fecha y hora específicas. Esto permite al administrador correlacionar la inestabilidad con un evento, como la instalación de una actualización o un nuevo driver.
* **Resolución de Problemas:** Al identificar el origen de la inestabilidad, se puede resolver el problema de manera más rápida y eficiente. Por ejemplo, si una caída en la estabilidad coincide con la instalación de un programa, se puede concluir que ese programa es la causa del mal funcionamiento.

#### 6. Aplicación Práctica de las Herramientas de Monitorización

La práctica de la monitorización en Windows Server implica un flujo de trabajo lógico:

1.  **Vista Preliminar (Administrador de Tareas):** Ante un problema, se comienza con el Administrador de Tareas para tener una visión general de los procesos y el consumo de recursos.
2.  **Identificación de Cuellos de Botella (Monitor de Recursos):** Si se detecta un componente saturado (por ejemplo, la CPU o el disco), se lanza el Monitor de Recursos para identificar rápidamente los procesos responsables.
3.  **Análisis a Largo Plazo (Monitor de Rendimiento):** Para un análisis más profundo y la creación de una línea base de rendimiento, se utiliza el Monitor de Rendimiento. Se pueden crear recopiladores de datos personalizados para monitorizar componentes específicos durante un período prolongado.
4.  **Diagnóstico de Inestabilidad (Monitor de Confiabilidad):** Si el sistema presenta una inestabilidad general, el Monitor de Confiabilidad se usa para identificar el momento exacto en que comenzaron los problemas y qué eventos (instalaciones, actualizaciones) están relacionados con esas caídas en la estabilidad.

El uso combinado de estas herramientas permite a un administrador no solo reaccionar a los problemas, sino también analizarlos, prevenir futuros fallos y fortalecer la seguridad del sistema mediante la identificación de comportamientos anómalos o configuraciones defectuosas.

---

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

Documentos de Referencia: "FSW Clase 26 – Objetos de Directiva de Grupo GPO.pdf", "5-26 Administración de GPO.pdf"

# Informe Detallado sobre los Objetos de Directiva de Grupo (GPO)

## Introducción a los GPO y su Rol en la Ciberseguridad

Los **Objetos de Directiva de Grupo (GPO)** son una herramienta fundamental para la administración y la seguridad en entornos de Windows. Permiten la gestión centralizada de configuraciones de cuentas de usuarios y equipos, siendo aplicadas a nivel de **Sitio**, **Dominio** o **Unidad Organizativa (OU)**. Esta capacidad de aplicar configuraciones de forma masiva y específica hace que los GPO sean un recurso excelente para la aplicación de medidas de seguridad, políticas de acceso y configuraciones estandarizadas en empresas de cualquier tamaño. La configuración de los GPO se realiza una única vez y puede ser reutilizada para aplicarse a un gran número de usuarios o equipos de manera muy eficiente.

---

## Relación con Active Directory y Windows Server

Los GPO están intrínsecamente ligados a los **Servicios de Dominio de Active Directory (AD DS)**. La gestión de los GPO se realiza a través de la consola de **Group Policy Management** en **Server Manager**.

Existen dos GPO predeterminados que se crean al configurar un dominio:

* **Default Domain Policy**: Se aplica por defecto a toda la estructura del dominio, es decir, a todos los elementos del Active Directory. Esta directiva establece configuraciones de seguridad a nivel de dominio, como las políticas de contraseña y las políticas de tickets de Kerberos.
* **Default Domain Controllers Policy**: Se aplica exclusivamente a los equipos que actúan como controladores de dominio (DC o Domain Controllers). Esta directiva contiene configuraciones de seguridad adicionales específicas para proteger estos servidores críticos.

Cuando un servidor es promovido a controlador de dominio, su cuenta de equipo se mueve del contenedor de `Computers` a la Unidad Organizativa de `Domain Controllers`, momento en el que se le aplican las directivas de la `Default Domain Controllers Policy`.

---

## Teoría y Fundamentos de los GPO

El elemento más básico de un GPO es una configuración individual que define una política específica sobre un componente del sistema. Un solo GPO puede contener múltiples configuraciones, como políticas de **Firewall**, **VPN** o del **adaptador de red**. Las GPO se aplican a intervalos regulares de **90 a 120 minutos**, pero también se aplican en el reinicio del equipo (configuraciones de equipo) o al iniciar sesión (configuraciones de usuario).

Existen dos tipos principales de configuraciones en los GPO:

* **Configuración de Equipo**: Se aplican al sistema operativo al momento del arranque, independientemente del usuario que inicie sesión.
* **Configuración de Usuario**: Se aplican al perfil del usuario al momento de iniciar sesión, independientemente del equipo que utilice.

---

## Administrative Templates

Las **Administrative Templates** son el esquema de todas las configuraciones posibles dentro de un GPO. Sirven como un repositorio de ajustes que se pueden habilitar, deshabilitar o dejar sin configurar.

Los estados que pueden tener las plantillas administrativas son tres:

1.  **Not Configured (No Configurado)**: La configuración no está definida por la GPO y el sistema utiliza su valor predeterminado o la configuración de una GPO de menor precedencia.
2.  **Enabled (Habilitado)**: La característica se activa, aplicando la configuración específica.
3.  **Disabled (Deshabilitado)**: La característica se desactiva, impidiendo su uso.

---

## Consola de Administración de GPO (Group Policy Management)

La consola de **Group Policy Management** es la herramienta principal para gestionar los GPO. Se accede a ella desde **Server Manager > Tools**. Dentro de una GPO, las configuraciones se dividen en dos categorías principales:

### 1. Directivas (Policies)

Son configuraciones **impositivas** y obligatorias que el usuario **no puede modificar**. Si un usuario intenta cambiar una configuración establecida por una directiva, los paneles de control estarán deshabilitados o se mostrará un mensaje indicando que la característica está controlada por la empresa.

Dentro de las Directivas, encontramos las siguientes subcategorías:

* **Software Settings**
* **Windows Settings**
* **Administrative Templates**

### 2. Preferencias (Preferences)

Son un conjunto de configuraciones que se pueden desplegar de la misma manera que las directivas, pero a diferencia de estas, **el usuario sí puede modificarlas posteriormente**. Se utilizan para establecer configuraciones habituales de manera cómoda, sin imponerlas de forma estricta.

Las subcategorías de las Preferencias incluyen:

* **Windows Settings**
* **Control Panel Settings**

---

## Herencia de las GPO (LSDOU)

La herencia es un concepto fundamental que define cómo se aplican las políticas en la jerarquía de Active Directory. Las GPO se procesan en un orden específico, conocido como **LSDOU**.

| Orden | Nivel | Descripción |
| :---: | :---: | :--- |
| **1** | **Local** | Se aplican primero las políticas del ordenador local. |
| **2** | **Site (Sitio)** | Le siguen las GPO enlazadas a los sitios de Active Directory. |
| **3** | **Domain (Dominio)** | Se aplican las GPO del dominio. |
| **4** | **OU (Unidad Organizativa)** | Por último, se aplican las GPO enlazadas a las OU, en el orden en que aparecen en la lista de enlaces. Las OU anidadas (una dentro de otra) se aplican de la más externa a la más interna. |

La lógica de esta herencia es que las configuraciones más específicas prevalecen sobre las más generales. Por ejemplo, una GPO en una OU puede sobrescribir una política de dominio, ya que la OU representa un nivel más granular de la jerarquía.

Existen varios elementos que pueden influir en la herencia de las GPO:

* **Link Order**: El orden de los enlaces de las GPO dentro de un mismo nivel determina la precedencia.
* **Enforced (Obligatorio)**: Si una GPO se marca como "Enforced", sus configuraciones tendrán la máxima prioridad, incluso si la herencia está bloqueada a un nivel inferior.
* **Block Inheritance (Bloquear Herencia)**: Un administrador puede bloquear la herencia en una OU para evitar que las GPO de niveles superiores (Sitio, Dominio) afecten a esa OU.

---

## Configuración y Administración de GPO

### Cómo se Crean y Enlazan

Para crear un GPO, se navega al contenedor **Group Policy Objects** en la consola de `Group Policy Management`, se hace clic derecho y se selecciona `New`. Una vez creada, la GPO debe ser **enlazada** a un contenedor, como un Dominio, un Sitio o una Unidad Organizativa, para que sus configuraciones surtan efecto.

**Enlazar** una GPO significa asociarla a un contenedor de Active Directory para que las políticas que contiene se apliquen a los usuarios y equipos dentro de ese contenedor. La principal potencia de enlazar GPO es la flexibilidad y granularidad que ofrece. Permite centralizar políticas globales a nivel de dominio y segmentar políticas personalizadas a nivel de OU para grupos específicos. Es importante destacar que no se puede enlazar GPO a los contenedores de `Computers` o `Users`.

### Edición de GPO

Para configurar una GPO, se hace clic derecho sobre ella y se selecciona `Edit`. Esto abre el **Group Policy Management Editor**, donde se pueden modificar las políticas de equipo y de usuario.

### Filtrado de Seguridad

El filtrado de seguridad permite aplicar una GPO solo a un conjunto específico de usuarios, grupos o equipos dentro del contenedor al que está enlazada. Esto se configura en la pestaña `Scope` de la GPO. Un administrador puede, por ejemplo, aplicar una política de `Firewall` a una OU, pero filtrarla para que solo se aplique a un grupo de seguridad específico dentro de esa OU, eliminando a los `Authenticated Users` por defecto.

### Mejores Prácticas y Consejos

* Crear GPO pequeños y específicos enlazados a las OU para facilitar la identificación y solución de problemas.
* Utilizar la opción `Enforced` con precaución, ya que tiene la máxima prioridad y puede anular políticas más específicas.
* Conocer el orden de procesamiento de las GPO (LSDOU) es crucial para evitar conflictos y entender el comportamiento de las políticas.
* Usar el filtrado de seguridad para aplicar políticas de forma precisa.

---

## Generación de Reportes con RSoP

El **Conjunto Resultante de Políticas (RSoP - Resultant Set of Policy)** es una herramienta esencial para la verificación de las configuraciones aplicadas. Muestra el efecto final de todas las GPO sobre un usuario o equipo, considerando la herencia, el orden de los enlaces, el filtrado de seguridad y los filtros WMI. Esto es vital para solucionar conflictos entre políticas.

Se pueden usar varios asistentes y comandos para generar estos reportes:

* **Group Policy Results Wizard**: Asistente gráfico en la consola de `Group Policy Management` que guía al usuario para seleccionar un equipo y un usuario, y luego genera un informe detallado de las configuraciones aplicadas.
* **Group Policy Modeling Wizard**: Permite simular qué configuraciones se aplicarían a un usuario o equipo específico bajo ciertas condiciones, lo que ayuda a planificar cambios.
* **GPResult.exe**: Un comando de línea que muestra las configuraciones de GPO aplicadas.

### Comandos de Terminal para GPO

A continuación se detallan los comandos clave de **Windows PowerShell** para la administración y verificación de GPO.

#### `GpUpdate /Force`

* **Sintaxis**: `GpUpdate /Force`
* **Descripción**: Este comando obliga al sistema a actualizar inmediatamente todas las directivas de grupo que se le aplican.
* **Porqué**: Se utiliza para forzar la aplicación de los GPO sin tener que esperar el intervalo de refresco automático de 90 a 120 minutos. Esto es útil para verificar que los cambios realizados en las políticas surtan efecto de inmediato.
* **Cómo se realiza**: Se ejecuta el comando en una terminal de Windows PowerShell o Command Prompt con privilegios de administrador. El sistema mostrará un mensaje indicando que las políticas de equipo y usuario se han actualizado exitosamente. En algunos casos, especialmente con las configuraciones de equipo, puede ser necesario reiniciar el equipo para que los cambios se apliquen por completo.
* **Objetivo**: Asegurar la aplicación instantánea de las configuraciones de GPO.

#### `GpResult /R`

* **Sintaxis**: `GPResult /R`
* **Descripción**: Muestra un informe detallado en la terminal sobre las GPO que se están aplicando actualmente tanto a nivel de equipo como a nivel de usuario.
* **Porqué**: Permite a los administradores verificar las políticas efectivas sobre un usuario o equipo específico para diagnosticar conflictos o confirmar que las configuraciones deseadas se están aplicando correctamente en el entorno de GPO complejo.
* **Cómo se realiza**: Se ejecuta el comando en una terminal de Windows PowerShell o Command Prompt. El sistema mostrará un resumen de las políticas aplicadas, incluyendo las GPO ganadoras, el `Winning GPO`, para cada configuración.
* **Objetivo**: Proporcionar visibilidad sobre las políticas de grupo en vigor en un equipo o usuario concreto.

---

## Demo Práctica de la Consola de Group Policy Management

La demo práctica en una máquina virtual ilustra cómo trabajar con la consola de `Group Policy Management`.

1.  **Crear un GPO**: Se crea un nuevo GPO, por ejemplo, llamado `Firewall`, en el contenedor `Group Policy Objects`. Este GPO está ahora disponible para ser enlazado.
2.  **Enlazar un GPO**: Se hace clic derecho en el dominio o en una OU, se selecciona `Link an Existing GPO` y se elige el GPO `Firewall` para enlazarlo. Se observa que el GPO se aplica al contenedor y se puede ver su orden y herencia.
3.  **Editar el GPO**: Se hace clic derecho en el GPO `Firewall` y se selecciona `Edit`. Se navega a **Computer Configuration > Policies > Windows Settings > Security Settings > Windows Defender Firewall with Advanced Security**. Aquí se pueden crear reglas de entrada (`Inbound Rules`), reglas de salida (`Outbound Rules`) y reglas de seguridad de conexión.
4.  **Configurar una regla**: Se crea una nueva regla de entrada personalizada para el protocolo `ICMPv4` que solo permite las solicitudes de `Echo`, se aplica exclusivamente al perfil de dominio y se le asigna un nombre descriptivo.
5.  **Verificar la herencia**: En la pestaña `Group Policy Inheritance` de una OU, se puede observar el orden de precedencia de los GPO aplicados. Se demuestra que al desactivar un enlace o bloquear la herencia, un GPO deja de tener efecto en la OU.
6.  **Forzar una GPO**: Al marcar una GPO como `Enforced`, se demuestra que esta adquiere la máxima prioridad, incluso si la herencia está bloqueada en la OU, colocándose la primera en el orden de precedencia.
7.  **Filtrado de Seguridad**: En la pestaña `Scope` de un GPO, se muestra cómo agregar un grupo de seguridad específico y eliminar a `Authenticated Users` para que la política se aplique de forma exclusiva a ese grupo.
8.  **Generar un reporte RSoP**: Se utiliza el `Group Policy Results Wizard` para seleccionar un usuario y un equipo y generar un informe. Este informe enumera todas las configuraciones que se aplicarán al usuario al iniciar sesión en el equipo seleccionado, incluyendo el `Winning GPO` (la GPO que prevalece) para cada configuración.

---

Documentos de Referencia: "5-27 Directivas de configuracion de seguridad.pdf", "FSW Clase 27 – Directivas de Configuración de Seguridad.pdf"

# Informe sobre Directivas de Configuración de Seguridad en Windows Server

## Introducción a las Directivas de Configuración de Seguridad y su Relación con las GPO

Las **Directivas de Configuración de Seguridad** son un conjunto de políticas que permiten la gestión centralizada de elementos críticos para la seguridad del sistema en un entorno de **Active Directory Domain Services (AD DS)**. Estas directivas, gestionadas a través de los **Objetos de Directiva de Grupo (GPO)**, son un excelente punto de partida para establecer una **línea base de seguridad** que fortalezca la infraestructura de una organización. Los GPO tienen una gran repercusión en la configuración de la seguridad, ya que la mayoría de las tecnologías de seguridad de Microsoft se despliegan mediante ellos.

### Plantillas Administrativas

Las **Plantillas Administrativas** son archivos que se almacenan en formatos `.admx` (y en formatos antiguos como `.adm` en Windows Server 2003 y versiones anteriores). Estas plantillas se utilizan para realizar modificaciones en claves específicas del registro, tanto a nivel de usuario (`HKEY_CURRENT_USER`) como a nivel de equipo (`HKEY_LOCAL_MACHINE`).

Es posible crear un **repositorio central** de plantillas administrativas en un dominio con múltiples controladores de dominio (DC). Esto se logra manualmente creando una carpeta llamada `Policy Definitions` en la ruta `\\FQDN\SYSVOL\FQDN\Policies`. Una vez creada, todos los DC del dominio detectarán y utilizarán este repositorio. Las plantillas de seguridad también se pueden importar y exportar mediante herramientas como `Secedit.exe`, el complemento de plantillas de seguridad, la consola de Group Policy Management o el Security Compliance Manager (SCM).

Para importar una plantilla de seguridad en un GPO existente, se debe seguir el siguiente procedimiento:

1.  Crear y editar un GPO.
2.  En el `Group Policy Management Editor`, navegar a la ruta `Computer Configuration\Policies\Windows Settings\Security Settings`.
3.  Hacer clic derecho en `Security Settings` y seleccionar la opción `Import Policy`.
4.  Elegir el archivo de la plantilla de seguridad deseada.

---

## Directivas de Cuenta

Las **Directivas de Cuenta** gestionan las características de inicio de sesión y autenticación de los usuarios. Se configuran dentro de `Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies` y se dividen en tres categorías:

### 1. Directivas de Contraseña (Password Policy)

Estas directivas, que son únicas para todo el dominio, solo pueden definirse en la **Default Domain Policy**. Algunas configuraciones incluyen:

* **Enforce password history**: Define la cantidad de contraseñas que se recordarán para evitar su reutilización.
* **Maximum password age**: Establece la vigencia máxima de una contraseña antes de que expire.
* **Minimum password length**: Determina la longitud mínima que debe tener una contraseña.
* **Password must meet complexity requirements**: Requiere que las contraseñas contengan mayúsculas, minúsculas, números y caracteres especiales.

Si se desea una directiva de contraseña diferente para un grupo de usuarios específico, se deben utilizar los **Password Settings Objects (PSOs)**, que son una herramienta ajena a los GPO.

### 2. Directivas de Bloqueo de Cuenta (Account Lockout Policy)

Estas directivas gestionan el número de intentos de inicio de sesión fallidos permitidos antes de que una cuenta se bloquee. Su configuración es clave para mitigar los ataques de **fuerza bruta** contra las identidades de usuario. Al limitar los intentos, se ralentiza significativamente la capacidad de un atacante para probar múltiples contraseñas. Un ejemplo de configuración sería bloquear la cuenta por 30 minutos después de 5 intentos fallidos.

### 3. Directivas de Kerberos (Kerberos Policy)

**Kerberos** es el protocolo de autenticación utilizado en Active Directory. El controlador de dominio (DC) emite tickets TGT (Ticket Granting Ticket) a los usuarios al autenticarse. Estos tickets se utilizan para acceder a los diferentes recursos de la red. Las directivas de Kerberos permiten configurar los tiempos de vigencia de estos tickets y otros valores relacionados.

---

## Directivas Locales

Las **Directivas Locales** se encuentran en `Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies` y son esenciales para el proceso de fortificación (**hardening**) de Active Directory. Se dividen en tres secciones:

### 1. Directivas de Auditoría (Audit Policy)

Estas directivas permiten habilitar registros específicos en el **Visor de Eventos** para monitorizar eventos del sistema. Es posible auditar el **éxito** o el **fallo** de una acción, como el inicio de sesión de un usuario. Esto es crucial para detectar actividades sospechosas o accesos no autorizados. Por ejemplo, al auditar los fallos de inicio de sesión, el sistema generará un registro cada vez que un usuario se equivoque en su contraseña.

### 2. Derechos de Usuario (User Rights)

Los derechos de usuario son los privilegios que tiene un usuario. Estas directivas definen las acciones que un usuario puede o no puede realizar. La mayoría de estas directivas no vienen definidas por defecto, lo que significa que un usuario estándar puede realizar ciertas acciones a menos que se restrinjan explícitamente a través de un GPO. Algunos ejemplos de derechos de usuario incluyen:

* Unir un equipo al dominio.
* Iniciar sesión localmente.
* Conectarse por escritorio remoto (RDS).
* Realizar copias de seguridad de archivos o directorios.

### 3. Opciones de Seguridad (Security Options)

Son configuraciones básicas que pueden tener un impacto significativo en la seguridad de un entorno de Active Directory. Ejemplos de estas opciones son:

* No mostrar el nombre del último usuario que inició sesión.
* Renombrar la cuenta de administrador para dificultar los ataques dirigidos.
* Configurar opciones relacionadas con dispositivos extraíbles o la instalación de drivers.

### Directivas Avanzadas de Auditoría

Las **Directivas Avanzadas de Auditoría** ofrecen un control más granular y específico sobre los registros de eventos que se generan. Son más detalladas que las directivas de auditoría convencionales. Para evitar conflictos, es crucial habilitar la directiva `Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings` en `Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options` si se van a utilizar las directivas de auditoría avanzadas.

---

## Resolución de Ejercicio Práctico

A continuación, se detalla la resolución del ejercicio propuesto, que cubre la configuración de directivas de cuenta y auditoría, y la verificación de los registros en el Visor de Eventos.

### Paso 1: Configurar Directivas de Contraseña y Bloqueo de Cuenta

1.  En el `Server Manager`, ir a `Tools` y abrir la consola de `Group Policy Management`.
2.  Expandir el árbol del dominio, hacer clic derecho en `Default Domain Policy` y seleccionar `Edit`.
3.  Navegar a `Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Account Lockout Policy`.
4.  Hacer doble clic en `Account lockout threshold` y definir el número de intentos fallidos. En este caso, se define en `5`.
5.  Aceptar. Esto configurará automáticamente `Account lockout duration` (por 30 minutos por defecto) y `Reset account lockout counter after`.
6.  Editar `Account lockout duration` y establecer el valor a `3` minutos para un bloqueo más breve.
7.  Ahora, para la directiva de contraseñas, ir a `Account Policies > Password Policy`.
8.  Aquí se pueden ajustar valores como `Minimum password length`, `Password must meet complexity requirements`, etc., según las políticas de la organización.

### Paso 2: Configurar Auditoría de Inicio de Sesión y Acceso a Objetos

1.  En el `Group Policy Management Editor`, navegar a `Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Audit Policy`.
2.  Hacer doble clic en `Audit account logon events` y `Audit object access`.
3.  En cada una de ellas, marcar las casillas **Success** y **Failure** para auditar ambos tipos de eventos.
4.  Cerrar el editor de GPO.

### Paso 3: Verificar los Registros en el Visor de Eventos

1.  Asegurarse de que las directivas se apliquen forzando la actualización en PowerShell con el comando `gpupdate /force`.
2.  Reiniciar el equipo para que las configuraciones de equipo se apliquen correctamente.
3.  Una vez reiniciado, se realizan las siguientes acciones para generar registros:
    * Intentar iniciar sesión varias veces con una contraseña incorrecta para generar eventos de `Failure`.
    * Iniciar sesión correctamente para generar eventos de `Success`.
    * Acceder a una carpeta y a sus documentos, como una carpeta de nombre `Confidencial`, en la que se ha habilitado la auditoría de acceso a objetos desde sus propiedades de seguridad. Esto generará registros de `Audit object access`.
4.  Abrir el `Event Viewer` desde `Server Manager > Tools`.
5.  En el `Event Viewer`, navegar a `Windows Logs > Security`. Aquí se pueden ver los registros correspondientes a los intentos de inicio de sesión (éxitos y fallos) y los accesos a los objetos que se han auditado.
6.  Haciendo doble clic en un evento, como el **Event ID 4771** para un intento de inicio de sesión fallido, se pueden ver los detalles, incluyendo el nombre del usuario, la hora y otra información relevante.
7.  Para una monitorización continua, se puede anclar una tarea a un evento específico, como el **Event ID 4771**, para recibir notificaciones por correo electrónico cuando se genere dicho evento.

---

# Administración de Identidades y Herramientas de Seguridad en Windows Server

## Introducción a la Administración de Identidades 

La administración de identidades es uno de los desafíos más importantes en la fortificación de cualquier entorno tecnológico. Una gestión adecuada de las credenciales y las autorizaciones a los recursos es un paso fundamental para reducir el riesgo de accesos no autorizados. Un control deficiente podría permitir que un atacante o un malware utilice una identidad, un token o un ticket TGT para acceder a servicios a los que no debería tener permiso. Windows Server ofrece varias herramientas para proteger cuentas de usuario o servicio y administrar políticas de contraseñas de forma específica para las necesidades de cada organización.

Las principales recomendaciones para mitigar ataques conocidos incluyen:
* **Asegurar las cuentas de usuario y contraseñas**.
* **Gestionar adecuadamente los grupos con privilegios**.
* **Auditar los cambios en recursos críticos** de la organización.
* **Implementar autenticaciones seguras** y utilizar segundos factores de autenticación.
* **Proteger la actividad de la red** para detectar tráfico inusual y segregar servicios importantes mediante la autenticación con certificados.
* **Establecer la administración de cuentas**, aprovisionamiento y políticas para usuarios y equipos, planificando no solo la creación, sino también la desactivación o eliminación de identidades.
* **Gestionar la seguridad física de los equipos**.

***

## Herramientas Clave para la Securización de Identidades

Windows Server proporciona varias herramientas integradas y descargables para securizar la gestión de identidades, cada una con un propósito específico.

### Grupos Restringidos (Restricted Groups)

Los **Grupos Restringidos** son una característica de seguridad dentro de los **Objetos de Directiva de Grupo (GPO)** que permite a los administradores controlar de forma estricta la pertenencia a los grupos locales de los equipos del dominio. Su función principal es asegurar que solo los usuarios y grupos de confianza formen parte de grupos de alto privilegio en los equipos locales, como el grupo de `Administradores`. Esto es crucial para la seguridad, ya que evita la escalada de privilegios por parte de usuarios no autorizados.

**Importante**: Los grupos restringidos se utilizan para administrar la pertenencia a **grupos locales de equipos**, no a grupos de dominio.

La configuración de un grupo restringido ofrece dos opciones principales para gestionar la pertenencia, cada una con un comportamiento diferente:

* **Members of this group (Miembros de este grupo)**: Si se utiliza esta opción, la lista de usuarios o grupos que se añadan será la **única** permitida en el grupo local restringido. Todos los miembros actuales que no estén en la lista, a excepción del grupo de administradores del dominio, serán eliminados automáticamente. Se utiliza para establecer una lista de miembros exclusiva.
* **This group is a member of (Este grupo es miembro de)**: Esta opción solo añade el grupo a un grupo local existente sin eliminar a otros miembros. Los grupos o usuarios que ya tuvieran privilegios de administración local en los equipos del dominio **permanecerán**. Se utiliza para agregar privilegios sin sobrescribir la configuración existente.

### Grupo de Usuarios Protegidos (Protected Users Security Group)

El **Grupo de Usuarios Protegidos** es un grupo de seguridad especial en Active Directory, disponible desde Windows Server 2012 R2, diseñado para mitigar amenazas de robo de credenciales como los ataques Pass-the-Hash (PtH) y Pass-the-Ticket (PtT). Cuando un usuario o un grupo se añade a este grupo, se aplican automáticamente una serie de medidas de seguridad adicionales:

* Se prohíbe el uso de protocolos de autenticación considerados inseguros, como **NTLM**, Digest authentication o Credential Security Support Provider (**CredSSP**).
* Se desactiva la delegación Kerberos restringida o no restringida.
* El cifrado de Kerberos debe soportar **AES**, y se deshabilitan los tipos de cifrado antiguos como **DES** y **RC4**.
* No se guardan las contraseñas en caché, lo que hace que los dispositivos que dependan de estos protocolos no puedan autenticarse en el dominio.
* El tiempo de vida de los tickets TGT de Kerberos se establece por defecto en **cuatro horas**.

Este grupo está pensado para cuentas específicas y de alto privilegio o con acceso a información confidencial, no para todos los usuarios de la organización, ya que puede romper la compatibilidad con servicios que dependan de los protocolos deshabilitados.

### Demo práctica: Gestión de Usuarios Protegidos

En una demo práctica, se muestra cómo gestionar el grupo `Protected Users`:

1.  En la consola de `Active Directory Administrative Center (ADAC)`, se navega a la parte de `Users` del dominio.
2.  Se localiza el grupo `Protected Users`, que viene creado por defecto.
3.  Se accede a las propiedades del grupo y, en la pestaña de `Members`, se hace clic en `Add`.
4.  Se selecciona un grupo de seguridad de dominio, como el grupo `IT` o `Auditores`, y se añade a la lista de miembros.
5.  Una vez añadido, los miembros de ese grupo heredan automáticamente las protecciones adicionales contra el robo de credenciales.

### Objetos de Configuración de Contraseña (PSO)

Los **Password Settings Objects (PSO)**, también conocidos como **Fine-Grained Password Policies (FGPP)**, permiten aplicar diferentes políticas de contraseñas a usuarios o grupos específicos dentro de un mismo dominio. Anteriormente, solo se podía aplicar una única política de contraseñas a todo el dominio a través de la `Default Domain Policy`.

Los PSO se aplican a objetos de usuario, `InetOrgPerson` o grupos de seguridad global. Para aplicar un PSO, se modifica un atributo llamado **`msDS-PSOApplied`**. La **precedencia** se gestiona con el atributo `msDS-PasswordSettingsPrecedence`, donde el valor numérico más bajo indica la prioridad más alta en caso de que un usuario pertenezca a varios grupos con PSO diferentes.

Los PSO se pueden configurar de dos maneras:
* **Windows PowerShell**: Utilizando cmdlets como `New-ADFineGrainedPasswordPolicy` para crear el PSO y `Add-ADFineGrainedPasswordPolicySubject` para asignarlo a un grupo o usuario.
* **Active Directory Administrative Center (ADAC)**: Se navega a `Dominio/System/Password Settings Container` para crear un nuevo PSO y luego se asigna a través de las propiedades del usuario o grupo.

### Demo Práctica: Gestión de Objetos de Configuración de Contraseña (PSO)

Esta demostración detalla cómo crear y asignar un PSO específico a un grupo de seguridad en Active Directory, en este caso, el grupo **Auditores**. La finalidad es aplicar una política de contraseñas más estricta a este grupo, sin afectar al resto del dominio.

#### Paso 1: Acceder al Contenedor de Configuración de Contraseñas
1.  Abre el **Centro de Administración de Active Directory (ADAC)** desde `Server Manager > Tools`.
2.  En el panel de navegación, selecciona el nodo del dominio y navega hasta la ruta `System > Password Settings Container`.

#### Paso 2: Crear un Nuevo PSO
1.  Haz clic derecho en `Password Settings Container` y selecciona `New > Password Settings`.
2.  Se abrirá un panel de configuración para definir la nueva política. Asigna el nombre **AuditorsPSO** al objeto.
3.  Establece una **precedencia** para el PSO. La precedencia es un valor numérico que determina la prioridad en caso de conflicto con otras políticas. Un valor más bajo indica una mayor prioridad. Para este ejemplo, se le asigna un valor de `7`.
4.  Configura las características de la contraseña según sea necesario (por ejemplo, longitud mínima, requisitos de complejidad, historial, etc.). También es posible habilitar la parte de bloqueo de cuenta desde aquí.

#### Paso 3: Asignar el PSO al Grupo de Seguridad
1.  Dentro del panel de configuración del PSO, busca la sección `Directly Applies To` o una opción similar para asignar la política.
2.  Haz clic en `Add` y selecciona el grupo de seguridad **Auditores** para enlazar la política a este grupo.
3.  Confirma la configuración y cierra el panel.

#### Verificación de la Asignación
1.  Para verificar que la asignación se realizó correctamente, navega a las propiedades del grupo **Auditores** en el ADAC.
2.  En la pestaña `Password Settings`, se debería ver el PSO **AuditorsPSO** listado y asociado.
3.  Si revisas la configuración de un usuario que sea miembro del grupo `Auditores`, como el usuario `Tom`, verás que el PSO `AuditorsPSO` no aparece en su configuración de contraseña individual, pero sí se le aplica porque pertenece al grupo. Este comportamiento es normal y muestra que la política está siendo heredada a través de la pertenencia al grupo de seguridad.

***

## LAPS (Local Administrator Password Solution)

**LAPS** es una herramienta de Microsoft que soluciona el problema de tener la misma contraseña de administrador local en todos los equipos del dominio. LAPS genera una contraseña aleatoria y **única** para la cuenta de administrador local de cada equipo.

El funcionamiento de LAPS incluye los siguientes pasos:
1.  Verifica si la contraseña de la cuenta de administrador local ha expirado.
2.  Cambia la contraseña a un nuevo valor aleatorio y largo.
3.  Transmite la nueva contraseña y la fecha de expiración a Active Directory, donde se almacena en un atributo especial y sensible del objeto de la cuenta de equipo.
4.  Solo los usuarios y grupos autorizados, como los administradores de dominio, pueden leer estas contraseñas.

El uso de LAPS mejora significativamente la seguridad contra ataques de **movimiento lateral**.

**Requisitos de LAPS**:
* Equipos con Windows x86 o x64 en un dominio.
* Nivel funcional de dominio de Windows Server 2003 o superior.
* Requiere extender el esquema de Active Directory.
* Instalar el cliente de LAPS en los equipos a gestionar.
* Requiere .NET Framework 4.0 y PowerShell 2.0 o superior.

***

## Resolución del Ejercicio Propuesto

El ejercicio práctico consiste en crear un grupo de seguridad, asignarlo a `Protected Users` y aplicarle un PSO personalizado.

### Paso 1: Crear un grupo de seguridad y un usuario

1.  En el `Server Manager`, ir a `Tools` y abrir `Active Directory Users and Computers`.
2.  Seleccionar el contenedor `Users` y crear un nuevo usuario llamado **Tom**.
3.  Crear un nuevo grupo de seguridad llamado **Auditores**. Es crucial que sea un **grupo de seguridad global** para poder asignarle un PSO más adelante.
4.  Añadir al usuario `Tom` como miembro del grupo `Auditores`.

### Paso 2: Asignar el grupo "Auditores" a "Usuarios Protegidos"

1.  En el `Server Manager`, ir a `Tools` y abrir el `Active Directory Administrative Center`.
2.  En la navegación, ir a `Users` y buscar el grupo **`Protected Users`**.
3.  Acceder a las propiedades del grupo `Protected Users`, ir a la pestaña `Members` y hacer clic en `Add`.
4.  Se selecciona el grupo **`Auditores`** y se confirma. De esta forma, el grupo `Auditores` y sus miembros obtendrán las protecciones adicionales.

### Paso 3: Crear y asignar un Objeto de Configuración de Contraseña (PSO)

1.  En `Active Directory Administrative Center`, navegar a `System` y buscar el contenedor **`Password Settings Container`**.
2.  Hacer clic derecho en el contenedor y seleccionar `New > Password Settings`.
3.  Configurar un nuevo PSO llamado **`AuditorsPSO`** con las políticas deseadas, como una longitud mínima de contraseña o la duración del bloqueo de cuenta.
4.  Asignar una **precedencia**; por ejemplo, `1`.
5.  En la sección `Directly Applies To`, hacer clic en `Add` y seleccionar el grupo **`Auditores`** para enlazar la política.
6.  Verificar que el PSO se ha asignado correctamente revisando las propiedades del grupo `Auditores` en la pestaña `Password Settings`.
7.  Al revisar las propiedades del usuario `Tom`, se observa que en la pestaña `Member Of`, pertenece al grupo `Auditores`. Aunque el PSO no se muestra directamente en la configuración de contraseña del usuario `Tom`, las configuraciones de `AuditorsPSO` se le aplican porque es miembro del grupo `Auditores`.

---


Documentos de Referencia: "FSW Clase 31 – Protección de Identidad.pdf", "5-31 Protección de Identidades.pdf"

# Informe Detallado y Enriquecido sobre Protección de Identidades y Credenciales

## Introducción a la Protección de Identidades y Credenciales

La gestión de identidades y credenciales es un proceso crítico en las organizaciones actuales, y Windows Server ofrece un conjunto de tecnologías para afrontar los desafíos de seguridad inherentes a este proceso. Por defecto, las credenciales de las últimas 10 cuentas de usuario se almacenan en caché de forma local en los equipos, lo que representa un riesgo de seguridad que podría ser explotado en un ataque contra las credenciales de la organización. Para mitigar estos riesgos, Microsoft ha desarrollado varias tecnologías.

-----

## Tecnologías para la Protección de Identidades en Active Directory

### Protected User Group

El **Protected User Group** es una característica de seguridad que ayuda a prevenir el almacenamiento en caché de perfiles y credenciales en los equipos. Para su funcionamiento, requiere autenticación mediante **Kerberos** y limita la duración de los tickets de concesión de tickets (TGT) a un máximo de cuatro horas. Una limitación importante de esta característica es que no permite el inicio de sesión sin conexión (offline).

-----

### Authentication Policies

Las **Authentication Policies** son un nuevo tipo de objeto en el Directorio Activo (AD DS) que permiten configurar políticas de autenticación de manera más restrictiva para cuentas de usuario, servicio y equipos. Estas políticas ofrecen la posibilidad de personalizar los **tickets TGT** y, lo que es más importante, pueden utilizar **claims** de **Dynamic Access Control (DAC)** para definir condiciones de acceso personalizadas.

#### Dynamic Access Control (DAC) y Claims

DAC es una tecnología muy interesante que enriquece el sistema de permisos al permitir la creación de "claims". Un claim es un pequeño token o pieza de información que se puede adjuntar a cualquier objeto de Active Directory, ya sea un usuario, un servicio, una aplicación o un documento. Esto permite establecer condiciones de acceso mucho más específicas.

Por ejemplo, se podría configurar una política de acceso a una carpeta que permita a un usuario leer y escribir de forma local, pero solo leer si el acceso es remoto. Sin embargo, si ese usuario tuviera un claim con la etiqueta "Jefe de Departamento", se le podría conceder permiso para modificar la carpeta incluso de forma remota, anulando la restricción general. Esta tecnología también se puede integrar con otros servicios, como los servicios federados del Directorio Activo (Federation Service).

#### Requisitos para las Authentication Policies

Para poder implementar Authentication Policies, el entorno debe cumplir con los siguientes requisitos:

  * Todos los controladores de dominio deben ser **Windows Server 2012 R2** o una versión posterior.
  * El nivel funcional del dominio debe ser al menos **Windows 2012 R2**.
  * Los controladores de dominio deben estar configurados para soportar **Dynamic Access Control (DAC)**.
  * Las computadoras deben estar configuradas para soportar **DAC**.

#### Parámetros de Configuración de Authentication Policies

Al configurar una política de autenticación, se pueden establecer los siguientes parámetros:

  * **Nombre y Descripción**: Para identificar la política.
  * **Modo de Aplicación**: La política puede aplicarse de manera restrictiva o en **modo de auditoría**. El modo de auditoría permite validar las restricciones y generar registros sin que la política evite la acción, lo que es útil para observar su funcionamiento antes de un despliegue completo.
  * **Cuentas**: Se pueden definir las cuentas de usuario, servicio y equipos de forma separada.
  * **Condiciones de Control de Acceso**: Es posible definir el tiempo de vida de los tickets TGT y las condiciones de control de acceso utilizando los claims de DAC, para especificar qué usuarios o servicios pueden utilizar qué dispositivos.

-----

### Authentication Policy Silos

Los **Authentication Policy Silos** son objetos de AD DS diseñados para simplificar la administración. Permiten a los administradores agrupar cuentas de usuario, servicio y equipos en un mismo ámbito de seguridad para aplicarles de forma centralizada la misma política de autenticación. Además de agrupar cuentas, los silos pueden restringir el acceso a estructuras de archivos únicamente a las identidades validadas por un silo específico. Al igual que las Authentication Policies, los silos pueden configurarse en modo de auditoría o restrictivo.

-----

## Credential Guard y Remote Credential Guard

### Credential Guard

**Credential Guard** es una tecnología que aísla las credenciales para protegerlas de ataques. En un sistema Windows sin esta protección, las credenciales, como los hashes NTLM y los tickets TGT de Kerberos, se almacenan en la memoria del proceso de la **Local Security Authority (LSA)**. Este proceso es vulnerable a ataques de extracción de credenciales mediante herramientas como Mimikatz.

Credential Guard contrarresta esto moviendo las credenciales a un proceso de **LSA aislado** que permanece separado del resto del sistema mediante virtualización. Este proceso aislado contiene un conjunto mínimo de binarios firmados por un certificado de confianza y se comunica con la LSA principal mediante **RPC** (Remote Procedure Call). Si un atacante intenta realizar un volcado de memoria de la LSA principal, no encontrará secretos ni credenciales. Si intenta volcar la memoria de la LSA aislada, los datos estarán cifrados, haciendo que los ataques de extracción de credenciales sean inútiles.

Algunos atacantes intentan deshabilitar Credential Guard reiniciando el dispositivo. Sin embargo, si la protección está configurada para el arranque **UEFI**, el sistema operativo Windows protege las características para evitar su modificación, lo que frustra esta estrategia. Una configuración adecuada de Credential Guard dificulta los ataques de **escalada horizontal o vertical**, donde un atacante utiliza credenciales robadas para acceder a otros dispositivos o escalar privilegios.

#### Inconvenientes y Requisitos de Credential Guard

La implementación de Credential Guard es compleja, especialmente en máquinas virtuales, debido a sus estrictos requisitos de hardware:

  * **Arquitectura**: Se requiere una arquitectura **x64**.
  * **Firmware**: Se necesita una versión de firmware **UEFI 2.3.1** o superior.
  * **TPM**: Se requiere un Módulo de Plataforma Segura (**TPM**) versión 1.2 o 2.0.
  * **Sistema Operativo**: Compatible con **Windows Server 2016**, **Windows 10 Enterprise** y **Windows Enterprise IoT**.
  * **Virtualización**: Debe haber soporte para las extensiones de virtualización **Intel VT-x**.
  * **Arranque Seguro**: Requiere un proceso de actualización de firmware seguro, **Secure Boot**, **Secure MOR**, y soporte de firmware para la protección **SMM** (System Management Mode) a través de Windows Update.
  * **Protección DMA**: La protección **DMA** y la opción Secure Boot en las políticas de grupo requieren hardware compatible.

Debido a su dependencia de la virtualización, es complicado usar Credential Guard en máquinas virtuales, ya que los hipervisores (como VirtualBox o VMware) a menudo no exponen todas las capacidades de virtualización del hardware físico a la máquina virtual. Para que funcione en una VM, se necesita un entorno con **virtualización anidada**. Por ejemplo, **Hyper-V** permite que una VM actúe como un hipervisor, dándole acceso al hardware subyacente y a sus capacidades de virtualización, lo que permite que Credential Guard se active.

Credential Guard también restringe el uso de ciertos protocolos considerados inseguros: no permite la delegación irrestricta de Kerberos, el cifrado DES ni el uso de protocolos como **NTLMv1**, **MS-CHAPv2**, Digest y **CredSSP**.

#### Configuración Práctica de Credential Guard

La configuración se realiza a través del **Editor de administración de directivas de grupo (Group Policy Management Editor)**. Los pasos son:

1.  En la GPO, navegar a **Computer Configuration** -\> **Policies** -\> **Administrative Templates** -\> **System** -\> **Device Guard**.
2.  Habilitar la opción **Turn On Virtualization Based Security**. En sus opciones, se pueden proteger varios parámetros del arranque con el **bloqueo UEFI** (UEFI lock). Si se combina con BitLocker para el cifrado de arranque, se dificulta aún más el acceso malicioso.
3.  Configurar la opción **Credential Guard Configuration** y seleccionar **Enabled with UEFI lock** para impedir su desactivación remota.

-----

### Remote Credential Guard

**Remote Credential Guard** protege las credenciales durante una conexión de escritorio remoto. Al activarlo, las credenciales del usuario permanecen en el equipo cliente y no se exponen al host remoto. En cambio, la solicitud de autenticación Kerberos se redirige al host de origen (el cliente) para la validación, lo que permite un inicio de sesión único y seguro.

#### Requerimientos para Remote Credential Guard

  * El entorno debe pertenecer al mismo dominio de Active Directory o a uno con una relación de confianza.
  * Se requiere autenticación **Kerberos**.
  * Los sistemas operativos compatibles son **Windows 10, versión 1607** o **Windows Server 2016**.

#### Métodos de Configuración de Remote Credential Guard

**Remote Credential Guard** se puede configurar de varias maneras:

  * **Registro de Windows**: Se puede habilitar en la ruta `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` creando o modificando un valor `DWORD` llamado `DisableRestrictedAdmin` con un valor de `0`.
  * **Línea de Comandos**: Utilizando el comando `reg add`:
    ```bash
    reg add "HKLM\SYSTEM\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /d 0 /t REG_DWORD
    ```
      * `reg add`: Comando para añadir una clave o valor al registro.
      * `"HKLM\SYSTEM\CurrentControlSet\Control\Lsa"`: La ruta de la clave del registro.
      * `/v DisableRestrictedAdmin`: El nombre del valor a agregar.
      * `/d 0`: El valor de los datos.
      * `/t REG_DWORD`: El tipo de datos de la entrada.
  * **Políticas de Grupo (GPO)**: Se configura en `Computer Configuration/Administrative Templates/System/Credentials Delegation`. En la opción `Restrict delegation of credentials to remote servers`, se puede habilitar la política y elegir el modo de restricción, como `Require Remote Credential Guard` o `Require Restricted Admin`.
  * **Parámetro de Conexión de Escritorio Remoto**: Al iniciar una conexión con `mstsc.exe`, se pueden usar los parámetros `/remoteGuard` o `/RestrictedAdmin`.

-----

## Windows Defender Application Control

**Windows Defender Application Control (WDAC)** es una tecnología de protección que utiliza la **seguridad basada en virtualización (VBS)** para aislar el servicio **Hypervisor Code Integrity (HVCI)**. Esto permite que WDAC proteja los procesos y los controladores en el modo kernel de exploits, vulnerabilidades y ataques de **zero-day**.

WDAC funciona creando una "lista blanca" de los elementos que se pueden ejecutar en el sistema, impidiendo la ejecución de cualquier código no firmado o no incluido en dicha lista. En el modo kernel, WDAC garantiza que los controladores estén firmados por una entidad de confianza **WHQL** o que pertenezcan a una lista de controladores seguros definidos por la política.

Esta tecnología también previene la carga dinámica de código y los intentos de modificar código en la memoria. Adicionalmente, WDAC proporciona protección en el modo de usuario (**UMCI user-mode protection**) mediante políticas de integridad de código que definen qué elementos están autorizados a ejecutar código en cada servidor. Aunque es una de las tecnologías más restrictivas, también es una de las más seguras para prevenir la ejecución de malware, incluso de ataques **zero-day**.

#### Configuración de Windows Defender Application Control

Para configurar WDAC a través de GPO, se debe acceder a **Device Guard** y seleccionar `Deploy Windows Defender Application Control`. Es necesario habilitar la opción y especificar la ruta del archivo de política de integridad de código (`Code Integrity Policy file path`) que contiene la lista de programas seguros permitidos.

-----

## Delegación de Credenciales

La **delegación de credenciales** es el proceso mediante el cual un servicio puede utilizar la identidad de un usuario para acceder a otro servicio en su nombre. Es uno de los aspectos más importantes a configurar durante el proceso de fortificación de un sistema operativo o una infraestructura. Una gestión adecuada de la delegación de credenciales es crucial para evitar la suplantación de identidad y los ataques de movimiento lateral. La consola de administración de GPO ofrece diversas opciones de configuración para la delegación de credenciales que deben ser revisadas cuidadosamente.

-----

## Demo Práctica y Verificación en una Máquina Virtual

En un servidor Windows, es posible verificar el estado de las tecnologías de virtualización y sus protecciones utilizando el comando `msinfo32`. Al abrir la consola de `msinfo32`, se puede inspeccionar la información del sistema para ver el estado de tecnologías como la protección DMA del kernel, VBS (Virtualization-based security), Secure Boot y Credential Guard.

En una máquina virtual, incluso si las políticas de grupo están configuradas para habilitar estas tecnologías, es posible que no se estén ejecutando. Por ejemplo, la seguridad basada en virtualización (VBS) puede aparecer como `Enabled but not running`. Esto se debe a que el hipervisor de la VM (por ejemplo, VirtualBox) no expone los requisitos de hardware necesarios para que estas tecnologías se activen. Para que funcionen en un entorno virtualizado, se requiere la **virtualización anidada**.


---


Documentos de Referencia: "5-32 Cuentas de Servicio.pdf", "FSW Clase 32 – Cuentas de Servicio Administradas.pdf"

# Informe Detallado sobre la Administración de las Cuentas de Servicio

## Introducción a las Cuentas de Servicio Administradas (Group Managed Service Accounts)

En entornos empresariales, es común la necesidad de utilizar identidades asociadas al funcionamiento de un rol, un servicio o una aplicación que se ejecutan 24/7. Tradicionalmente, los administradores a menudo crean cuentas de usuario con contraseñas que nunca caducan para evitar interrupciones en el servicio, una práctica que introduce un riesgo de seguridad significativo. Una cuenta de servicio con una contraseña que no expira puede ser aprovechada por malware para obtener acceso indefinido a los recursos del sistema y operar de forma inadvertida.

Para solucionar este desafío, Microsoft propone el uso de las **Cuentas de Servicio Administradas** (Group Managed Service Accounts o gMSA). La principal ventaja de estas identidades es que Windows se encarga del mantenimiento y la actualización de las propiedades de la cuenta, incluyendo la renovación periódica y automática de la contraseña. De esta manera, el controlador de dominio genera una contraseña compleja y la renueva a intervalos regulares, lo que garantiza una administración segura y automatizada para las aplicaciones y servicios. Esto convierte a las gMSA en una excelente opción para mantener la gestión de las cuentas de servicio de forma segura a lo largo del tiempo.

-----

## Requisitos y Pasos para Desplegar las Cuentas de Servicio Administradas

Para poder utilizar las Cuentas de Servicio Administradas, se deben cumplir ciertos requisitos previos en el entorno de Active Directory. Estos son:

  * El esquema del Directorio Activo en el bosque de dominio debe estar actualizado, al menos a la versión de **Windows Server 2012**.
  * El valor del atributo `CN=Schema,CN=Configuration,DC=[Dominio],DC=Com` debe ser `52`.
  * Debe crearse un grupo de seguridad para la nueva cuenta gMSA aprovisionada.
  * Si la clave raíz (root key) de primer maestro del Directorio Activo no está implementada o creada en el dominio, debe crearse.

El resultado de la creación de la clave raíz se puede verificar en el registro del servicio **KdsSvc** buscando el **ID de evento 4004**.

### Paso a Paso y Comandos de PowerShell para la Administración de gMSA

El proceso para trabajar con estas cuentas de servicio administradas se realiza a través de una serie de comandos de **Windows PowerShell**. A continuación se detallan los pasos y comandos utilizados en la demo:

#### 1\. Creación de la Clave Raíz (Root Key)

El primer paso es crear la clave raíz. Esto se hace con el comando `Add-KdsRootKey`.

```powershell
Add-KdsRootKey -EffectiveTime ((get-date).addhours(-10))
```

  * **Comando**: `Add-KdsRootKey`
  * **Parámetro**: `-EffectiveTime`
  * **Valor**: `((get-date).addhours(-10))`
  * **Acción**: Este comando crea la clave raíz necesaria para que las gMSA funcionen. La hora efectiva se establece 10 horas antes de la hora actual. Tras su ejecución, se muestra un identificador asociado a la clave raíz creada.

#### 2\. Creación y Adición de las Cuentas de Servicio

Una vez creada la clave raíz, se pueden crear las cuentas de servicio y asociarlas al equipo que las utilizará. En la demo, se crean dos cuentas de servicio: `DataShared` y `Webservice`.

**Para la cuenta `DataShared`:**

```powershell
New-ADServiceAccount -Name DataShared -DNSHostName DC01 -PrincipalsAllowedToRetrieveManagedPassword DC01$
```

  * **Comando**: `New-ADServiceAccount`
  * **Parámetros**:
      * `-Name`: El nombre de la cuenta de servicio, en este caso `DataShared`.
      * `-DNSHostName`: El nombre de host del controlador de dominio, `DC01` en este ejemplo.
      * `-PrincipalsAllowedToRetrieveManagedPassword`: Define qué principal puede recuperar la contraseña administrada. En este caso, el equipo `DC01`.

<!-- end list -->

```powershell
Add-ADComputerServiceAccount -identity DC01 -ServiceAccount DataShared
```

  * **Comando**: `Add-ADComputerServiceAccount`
  * **Parámetros**:
      * `-identity`: El equipo al que se va a añadir la cuenta de servicio.
      * `-ServiceAccount`: El nombre de la cuenta de servicio que se va a añadir.
  * **Acción**: Se crea una nueva cuenta de servicio y se añade al equipo especificado.

**Para la cuenta `Webservice`:**

```powershell
New-ADServiceAccount -Name Webservice -DNSHostName DC01 -PrincipalsAllowedToRetrieveManagedPassword DC01$
```

```powershell
Add-ADComputerServiceAccount -identity DC01 -ServiceAccount Webservice
```

#### 3\. Verificación de las Cuentas Creadas

Se puede verificar que las cuentas de servicio se han creado correctamente con el siguiente comando:

```powershell
Get-ADServiceAccount -Filter *
```

  * **Comando**: `Get-ADServiceAccount`
  * **Parámetro**: `-Filter *`
  * **Acción**: Muestra todas las cuentas de servicio creadas en el dominio.

#### 4\. Instalación de las Cuentas de Servicio

Una vez creadas, las cuentas deben instalarse para que puedan ser utilizadas en los servidores correspondientes.

```powershell
Install-ADServiceAccount -Identity DataShared
```

  * **Comando**: `Install-ADServiceAccount`
  * **Parámetro**: `-Identity`
  * **Valor**: El nombre de la cuenta de servicio, por ejemplo, `DataShared` o `Webservice`.
  * **Acción**: Instala la cuenta de servicio especificada en el servidor donde se ejecuta el comando.

-----

## Demo Práctica: Configuración y Asociación de Cuentas de Servicio

La demostración práctica ilustra cómo configurar y asociar las cuentas de servicio a diferentes servicios en una máquina virtual.

### 1\. Asociación a un Servicio Local (Data Sharing Service)

1.  Se accede a la consola de **Servicios** a través de **Server Manager** -\> **Tools** -\> **Services**.
2.  Se localiza el servicio deseado, por ejemplo, `Data Sharing Service`, se hace clic derecho y se selecciona `Properties`.
3.  En la pestaña `Log On`, se selecciona la opción `This account` y se introduce el nombre de la cuenta de servicio, por ejemplo, `seguridadjabali\DataShared$`. Es crucial que el nombre de la cuenta termine con el símbolo de dólar `$`.
4.  Se eliminan los campos de contraseña, ya que el controlador de dominio se encargará de su gestión y renovación.
5.  Se da clic en `OK` para asociar la cuenta de servicio al servicio.

### 2\. Asociación a un Pool de Aplicaciones de IIS

1.  Desde **Server Manager**, se accede a **Tools** -\> **Internet Information Services (IIS) Manager**.
2.  En la consola de IIS, se expande el nombre del servidor, se selecciona `Application Pools` y se elige el pool por defecto, por ejemplo, `DefaultAppPool`.
3.  En el panel de acciones de la derecha, se hace clic en `Advanced Settings`.
4.  Dentro de la sección `Process Model`, se hace clic en `Identity` y luego en los tres puntos (...).
5.  En el cuadro de diálogo `Application Pool Identity`, se selecciona `Custom account` y luego `Set...`.
6.  En el cuadro de diálogo `Set Credentials`, se introduce la cuenta de servicio, por ejemplo, `seguridadjabali\Webservice$`. Se da clic en `OK` tres veces.
7.  Se detiene el servicio y luego se inicia nuevamente desde el panel de acciones (`Stop` y `Start`) para que la nueva identidad de la cuenta de servicio (`Webservice`) se aplique al pool de aplicaciones de IIS.

## Consideraciones Adicionales y Fortificación

Para un funcionamiento correcto, dependiendo del rol o aplicación, puede ser necesario realizar **configuraciones adicionales** para las cuentas de servicio. Por ejemplo, en el caso de servicios de autenticación como **AD FS (Active Directory Federation Service)**, es posible que las cuentas de servicio deban ser añadidas a grupos de administración local o a otros grupos específicos que les permitan funcionar como servicio. Esto se puede lograr a través de la configuración de objetos de directiva de grupo (GPOs). Si no se realizan estas configuraciones, es posible que el servicio falle al reiniciarse, generando un error que indicará la necesidad de incluir la cuenta en los grupos adecuados.

La delegación del mantenimiento y la renovación de credenciales a los controladores de dominio es una tarea periódica y automatizada. Esto hace que las Cuentas de Servicio Administradas sean una opción segura para la gestión a largo plazo.


---

Documentos de Referencia: "FSW Clase 33 – Controlador de Dominio de Solo Lectura.pdf"

# Informe Detallado sobre el Controlador de Dominio de Solo Lectura (RODC)

## 1. Concepto y Propósito del RODC

Un **Controlador de Dominio de Solo Lectura** (RODC, por sus siglas en inglés, Read Only Domain Controller) es un tipo de controlador de dominio diseñado para ser implementado en ubicaciones como sucursales u oficinas remotas donde, por razones de seguridad, no se puede colocar un controlador de dominio con permisos para modificar el esquema de Active Directory. El propósito principal de un RODC es permitir a los usuarios de la sucursal resolver las peticiones de autenticación y autorización de forma local, sin comprometer la seguridad de la base de datos de Active Directory.

A diferencia de un controlador de dominio estándar, un RODC puede responder a las solicitudes de autenticación y autorización, pero no puede realizar ninguna modificación en los elementos del Directorio Activo. Esto significa que las credenciales no tienen que salir de la sucursal para ser validadas, mejorando la eficiencia y reduciendo el tráfico de red.

Una de las características de seguridad más importantes del RODC es que permite controlar qué credenciales de usuario se pueden almacenar en caché en el dispositivo. Esto asegura que, en caso de robo o acceso no autorizado al equipo, no se encuentren las credenciales de usuarios con altos privilegios del dominio, como los administradores. De este modo, el RODC permite tener un servidor que atiende peticiones de Active Directory de forma local sin comprometer un elemento tan crítico para la organización como lo es la seguridad del Directorio Activo.

***

## 2. Demostración de la Configuración de un RODC

La configuración de un RODC es un proceso que se puede dividir en varios pasos, comenzando por la preparación del entorno y finalizando con la instalación y verificación.

### 2.1. Creación de un Nuevo Sitio en Active Directory

El primer paso para la implementación de un RODC en una sucursal es crear un sitio dedicado para esa ubicación en la consola de **Active Directory Sites and Services**.

1.  Abrir la herramienta **Active Directory Sites and Services** desde el menú **Tools** en **Server Manager**.
2.  Dentro de la consola, navegar a la carpeta `Sites`.
3.  Hacer clic derecho en la carpeta `Sites` y seleccionar `New Site`.
4.  Asignar un nombre al nuevo sitio, por ejemplo, `Boston`.

Para una configuración completa, cada sitio debería estar asociado a una subred específica, lo que permite que los controladores de dominio atiendan las peticiones de forma local. Sin embargo, para los fines de esta demostración, la creación del sitio es suficiente.

### 2.2. Pre-creación de la Cuenta de Equipo del RODC

A continuación, se pre-crea la cuenta de equipo para el RODC en el controlador de dominio principal. Esto se realiza en el **Active Directory Administrative Center**.

1.  Abrir la herramienta **Active Directory Administrative Center** desde el menú **Tools** en **Server Manager**.
2.  Navegar a la unidad organizativa **Domain Controllers**.
3.  En el panel de tareas (Tasks), en la sección `Domain Controllers`, hacer clic en `Pre-create a Read-only domain controller`.
4.  Se abrirá un asistente. Hacer clic en `Next`.
5.  Especificar el nombre del equipo que se unirá como RODC, por ejemplo, `SRV007`. Este nombre debe coincidir exactamente con el del servidor de destino.
6.  Seleccionar el sitio creado previamente, por ejemplo, `Boston`.
7.  Designar un grupo o usuario para la delegación de la instalación y administración del RODC. Para el ejemplo, se selecciona un usuario pre-creado.
8.  Hacer clic en `Finish` para pre-crear la cuenta del RODC.

Después de estos pasos, la cuenta de controlador de dominio de solo lectura aparecerá en la unidad organizativa **Domain Controllers** del **Active Directory Administrative Center**.

### 2.3. Instalación y Promoción del Servidor a RODC

El siguiente paso se realiza en el servidor que se convertirá en RODC (SRV007).

1.  En la máquina `SRV007`, que inicialmente está en un grupo de trabajo, ir a **Server Manager** y hacer clic en `Manage` -> `Add Roles and Features`.
2.  En el asistente, navegar hasta `Server Roles` y marcar la casilla **Active Directory Domain Services**.
3.  Añadir las características requeridas y continuar con la instalación de los roles.
4.  Una vez finalizada la instalación de los roles, hacer clic en la notificación en la parte superior derecha de **Server Manager** y seleccionar `Promote this server to a domain controller`.
5.  Se abrirá el asistente de configuración. Seleccionar la opción `Add a domain controller to an existing domain`.
6.  Proporcionar el nombre del dominio (`Hackers.Academy`) y las credenciales de un usuario del dominio con privilegios para realizar la promoción.
7.  En la pantalla `Domain Controller Options`, el asistente detectará automáticamente que el servidor es un RODC (Read only domain controller) debido a la cuenta pre-creada. Se puede ver que las opciones de **DNS Server** y **Global Catalog** están seleccionadas por defecto.
8.  Introducir una contraseña para el **Modo de Restauración de Servicios de Directorio (DSRM)**.
9.  Completar el resto del asistente y hacer clic en `Install` para comenzar la promoción. El servidor se reiniciará automáticamente al finalizar.

Al reiniciar, el servidor ahora será parte del dominio `Hackers.Academy` y funcionará como un RODC.

### 2.4. Configuración de la Política de Replicación de Contraseñas (Password Replication Policy)

Una vez que el RODC está en funcionamiento, se puede configurar qué credenciales se pueden almacenar en caché. Esto se hace en las propiedades del RODC en el **Active Directory Administrative Center**.

1.  En el controlador de dominio principal, abrir el **Active Directory Administrative Center**.
2.  Navegar a **Domain Controllers** y seleccionar el RODC (`SRV007`).
3.  Hacer clic derecho en el RODC y seleccionar `Properties`.
4.  En la ventana de propiedades, ir a la pestaña `Extensions`.
5.  Seleccionar la pestaña `Password Replication Policy` y hacer clic en `Add` para añadir grupos con permisos.
6.  En la ventana para agregar grupos, se puede elegir si el grupo tendrá permisos de `Allow` (Permitir) o `Deny` (Denegar) para la replicación de contraseñas.
7.  Por defecto, en la pestaña `Password Replication Policy`, ya existen grupos que tienen explícitamente denegada la replicación de contraseñas, como los **Domain Admins**, **Enterprise Admins** y **Schema Admins**. Esto protege por defecto las credenciales de los usuarios más privilegiados del dominio.
8.  Se puede verificar que un usuario como **`Administrator`** tiene la replicación de contraseña denegada (`Deny Implicit`). En cambio, un usuario estándar, si se añade al grupo permitido (por ejemplo, `Boston RODC`), tendrá la replicación permitida (`Allow`).

Esto demuestra cómo el RODC proporciona un control granular sobre el almacenamiento en caché de credenciales, fortaleciendo la seguridad del Directorio Activo.

***

## 3. Conclusiones y Conceptos Clave

El despliegue de un **Controlador de Dominio de Solo Lectura (RODC)** es una estrategia de seguridad efectiva para infraestructuras con sucursales o entornos distribuidos.

Los conceptos clave aprendidos son:
* **Protección del Directorio Activo**: Un RODC permite resolver peticiones de autenticación y autorización localmente sin permitir modificaciones en la base de datos de Active Directory, lo que lo hace ideal para entornos con menor seguridad física.
* **Control de Credenciales**: Los RODC permiten un control preciso sobre qué credenciales de usuario se almacenan en caché. Por defecto, los grupos con altos privilegios, como los administradores de dominio, tienen denegada la replicación de contraseñas, lo que minimiza el riesgo en caso de robo o intrusión del servidor.
* **Delegación de la Administración**: El proceso de pre-crear la cuenta del RODC y delegar la instalación a un usuario o grupo específicos permite una administración segura y controlada del proceso de despliegue.
* **Configuración Granular**: La **Política de Replicación de Contraseñas** (`Password Replication Policy`) en las propiedades del RODC ofrece la capacidad de definir explícitamente los grupos y usuarios a los que se permite o se deniega el almacenamiento en caché de credenciales, adaptando la seguridad a las necesidades de la organización.

En resumen, el RODC es una excelente opción para desplegar controladores de dominio de forma segura en ubicaciones donde la administración o la seguridad física podrían estar en riesgo, sin comprometer la integridad y confidencialidad del Directorio Activo principal.


---

Documentos de Referencia: "FSW Clase 34 – Fortificación de Windows Server.pdf"

# Informe Técnico: Hardening de Windows Server

## 1\. Resumen Ejecutivo

El siguiente informe técnico detalla los conceptos y procedimientos para la fortificación de servidores Windows, un proceso conocido como **Hardening**. Se exploran tres tecnologías principales: **Privileged Access Management (PAM)**, **Just Enough Administration (JEA)** y la combinación de **Microsoft Passport y Windows Hello**. Se explica cómo estas herramientas ayudan a mitigar riesgos de seguridad al limitar los privilegios de los usuarios, implementar la pertenencia temporal a grupos y utilizar métodos de autenticación más seguros. El informe profundiza en la configuración de estas tecnologías, desde la estructura de bosques de Active Directory hasta la configuración de políticas de grupo, destacando la importancia de cada paso para fortalecer la infraestructura de Microsoft.

## 2\. Conceptos Fundamentales

### **Hardening de Windows Server**

El hardening es un proceso de fortificación de servidores Windows que busca reforzar la seguridad de la infraestructura general de Microsoft. Se aplican configuraciones y tecnologías a la infraestructura en su conjunto, y en etapas posteriores se pueden fortificar servicios específicos como DNS o servidores web.

### **Privileged Access Management (PAM)**

PAM es una tecnología que, en conjunto con **Microsoft Identity Manager (MIM)**, separa las cuentas sensibles en un bosque independiente conocido como **Bosque Bastión (Bastion Forest)**. Este enfoque dificulta los ataques "pass-the-hash" y "pass-the-ticket".

  * **Funcionamiento:** PAM se basa en dos entornos separados con una relación de confianza unidireccional. Las identidades con privilegios, como los administradores de dominio, se almacenan en el Bosque Bastión. Cuando un usuario necesita realizar una tarea que requiere privilegios, se emite una solicitud que debe ser aprobada para conceder un permiso temporal para usar esa cuenta desde el Bosque Bastión.
  * **Proceso de Autorización:** El usuario recibe un ticket de autorización por un tiempo limitado en lugar de las credenciales reales del grupo privilegiado. Una vez que el tiempo expira, el token caduca, y el usuario vuelve a ser un usuario estándar.

### **Group Member Expiration**

Esta característica permite automatizar la pertenencia temporal a un grupo, la cual está deshabilitada por defecto y requiere un nivel funcional de Windows Server 2016. El tiempo de pertenencia se refleja como un atributo **time-to-live (TTL)** que se propaga a la emisión de tickets TGT de Kerberos. Esto obliga a renovar el ticket TGT cuando la pertenencia al grupo expira, momento en el que se emite un nuevo ticket TGT sin los privilegios de administrador.

### **Just Enough Administration (JEA)**

JEA es una tecnología que se complementa con el principio "Just-in-Time" de PAM. Define un conjunto de comandos de Windows PowerShell específicos para actividades privilegiadas. Los administradores autorizan o habilitan los privilegios necesarios justo antes de que un usuario realice una tarea, y estos privilegios se otorgan por un tiempo determinado.

  * **Características:** JEA habilita la administración delegada con Windows PowerShell. Forma parte del paquete **Windows Management Framework 5.0**, compatible desde Server 2008 R2, y proporciona un control de acceso basado en roles **(RBAC)**.

### **Microsoft Passport y Windows Hello**

Microsoft Passport, en combinación con Windows Hello, utiliza un sistema de claves asimétricas para la autenticación. La clave pública se almacena en el controlador de dominio o en otro proveedor de identidad, mientras que la clave privada se aloja en un chip criptográfico TPM en el dispositivo del usuario.

  * **Proceso de Autenticación:** El usuario prueba su identidad con Windows Hello (o un PIN) para usar la clave privada, completando así la autenticación. El dispositivo actúa como un segundo factor de autenticación. Este método evita el uso de contraseñas, haciendo más complejos los ataques de robo de credenciales.
  * **Requisitos:** Microsoft Passport funciona con cuentas de Microsoft, AD DS o Azure AD en dispositivos con Windows 10 Professional o Enterprise. Para las organizaciones que utilizan Windows Server 2012 R2, también se necesita una suscripción a Microsoft Azure.

## 3\. Procedimientos Prácticos

### **Habilitación y configuración de Group Member Expiration**

La característica de pertenencia temporal a un grupo se gestiona a través de Windows PowerShell.

  * **Paso 1: Habilitar la característica.** Para habilitar la función de acceso con privilegios en el bosque, se utiliza el siguiente comando.
    ```
    Enable-ADOptionalFeature -Identity 'Privileged Access Management Feature' -Target (Get-ADForest) -Scope ForestOrConfigurationSet
    ```
  * **Paso 2: Añadir un miembro con pertenencia temporal.** Para agregar un usuario al grupo de administradores de dominio por un período específico (por ejemplo, 13 días), se usa el siguiente comando.
    ```
    Add-ADGroupMember -Identity 'Domain Admins' -Members 'InfoSecSvcAcct' -MemberTimeToLive (New-TimeSpan -Days 13)
    ```

### **Configuración de Just Enough Administration (JEA)**

Para configurar JEA, se debe crear un archivo de configuración de PowerShell.

  * **Paso 1: Crear el archivo de configuración.** Se usa el cmdlet `New-PSSessionConfigurationFile` para crear un archivo con la extensión ".pssc".
  * **Paso 2: Consultar la documentación oficial.** Se hace referencia a la documentación de Microsoft para obtener información detallada sobre la configuración de la infraestructura de JEA y la administración con comandos de Windows PowerShell.

### **Configuración de Microsoft Passport y Windows Hello**

Para habilitar estas tecnologías, es necesario realizar una serie de pasos que incluyen la configuración de la infraestructura de clave pública (PKI) y la implementación de políticas de grupo.

  * **Pasos para la implementación:**

    1.  Implementar certificados de usuario específicos para Microsoft Passport.
    2.  Instalar **Microsoft System Center Configuration Manager (SCCM)**.
    3.  Habilitar una infraestructura de clave pública (PKI) para los certificados. Esta infraestructura puede ser montada con servidores del propio Active Directory que emitan certificados digitales válidos.
    4.  Configurar **Group Policy Objects (GPO)** para los equipos que utilizarán esta tecnología.

  * **Procedimiento de configuración de GPO:**

    1.  Abrir el **Server Manager** y navegar a **Tools**.
    2.  Seleccionar **Group Policy Management**.
    3.  Editar la **Default Domain Policy**, como se muestra en la captura de pantalla.
    4.  Dentro de la **Default Domain Policy**, navegar a la ruta: **Computer Configuration** \> **Policies** \> **Administrative Templates** \> **Windows Components**.
    5.  En la sección de **Windows Components**, buscar y seleccionar la opción de **Windows Hello for Business**.
    6.  En esta sección se encuentran diversas configuraciones para los procesos de autenticación, incluyendo la emulación de tarjetas inteligentes, la recuperación de PIN, el uso de hardware de seguridad, biometría y bloqueo dinámico, como se aprecia en la captura de pantalla.

## 4\. Conclusiones y Puntos Clave

### **Importancia y Beneficios de Seguridad**

La implementación de medidas de hardening, como PAM y JEA, es fundamental para reducir la exposición de credenciales en una organización. Al separar las cuentas privilegiadas en un Bosque Bastión y limitar la duración de los privilegios, se dificulta enormemente que un atacante capture una identidad con altos privilegios. De la misma manera, la adopción de Microsoft Passport y Windows Hello elimina la dependencia de contraseñas, lo que neutraliza una de las vías de ataque más comunes: el robo de credenciales. Estas tecnologías proporcionan una seguridad mucho más robusta y moderna, mejorando la defensa contra ataques de ingeniería social y malware.

### **Puntos de Aprendizaje Clave**

  * **Principio de Privilegios Mínimos:** La pertenencia temporal a grupos y JEA son aplicaciones directas del principio de "Just-in-Time" y "Just Enough Administration", que restringen los privilegios a lo estrictamente necesario y por un tiempo limitado.
  * **Separación de Entornos:** La creación de un Bosque Bastión para cuentas privilegiadas es una estrategia de seguridad clave para aislar identidades sensibles y mitigar ataques.
  * **Autenticación sin Contraseña:** El uso de claves asimétricas, chips criptográficos TPM y autenticación biométrica o PIN (Microsoft Passport y Windows Hello) ofrece un método de autenticación más seguro y difícil de comprometer que las contraseñas tradicionales.
  * **Uso de GPO:** Las directivas de grupo (GPO) son una herramienta poderosa para administrar de forma centralizada las configuraciones de seguridad en toda la organización, permitiendo la aplicación de políticas específicas a diferentes niveles de la estructura.

### **Relevancia Técnica**

Los procedimientos detallados, como la configuración de GPO para Windows Hello y la habilitación de la pertenencia temporal a grupos con PowerShell, son habilidades críticas para cualquier profesional de seguridad en un entorno de Microsoft. Comprender la estructura de bosques de Active Directory y cómo las relaciones de confianza impactan la seguridad es fundamental para implementar correctamente tecnologías como PAM. El despliegue de una infraestructura de clave pública (PKI) es un proyecto complejo pero altamente beneficioso para la seguridad, ya que habilita una amplia gama de funcionalidades, desde la autenticación de aplicaciones hasta el cifrado de comunicaciones.


---

Documentos de Referencia: "FSW Clase 35 – Proteger la ejecución de código.pdf"

# Informe Técnico: Protección de la Ejecución de Código en Windows Server

### 1. Resumen Ejecutivo
Este informe técnico detalla los mecanismos de seguridad disponibles en Windows Server para controlar la ejecución de software. Aborda específicamente las políticas de restricción de software y el uso de AppLocker para gestionar la ejecución de aplicaciones no autorizadas. Además, se explora el rol de Microsoft Defender como solución antimalware, su administración centralizada a través de GPOs y PowerShell, y las distintas configuraciones que permiten adaptar su comportamiento a las necesidades de una organización. El objetivo principal es proporcionar un entendimiento técnico y práctico de cómo proteger los sistemas contra software malicioso y no autorizado.

### 2. Conceptos Fundamentales
A continuación se describen los conceptos y herramientas clave para la protección de la ejecución de código en entornos Windows Server.

* **Restricción de Software (Software Restriction Policies):** Se trata de un mecanismo de seguridad en Windows Server que permite evitar el uso de software no autorizado en una organización. Estas políticas definen reglas de ejecución de software basándose en el hash, la ruta, la firma digital o la zona de Internet del archivo. Pueden controlar archivos ejecutables, archivos DLL, scripts e instaladores de Windows. Sin embargo, estas políticas son rígidas, ya que no permiten controlar cada tipo de archivo por separado y solo generan una única colección de reglas, lo que las hace obsoletas en entornos modernos.

* **AppLocker:** Esta es una herramienta más moderna y flexible que las políticas de restricción de software. Permite definir reglas de control de aplicaciones para tipos de archivos específicos, como archivos ejecutables, archivos DLL, scripts, paquetes de aplicaciones e instaladores. A diferencia de las políticas de restricción, AppLocker permite importar y exportar reglas, generar reglas automáticamente a partir de aplicaciones instaladas y definir reglas que se aplican a usuarios o grupos específicos, con la capacidad de configurar excepciones. AppLocker soporta una amplia variedad de extensiones, incluyendo `.exe`, `.com`, `.ps1`, `.bat`, `.cmd`, `.vbs`, `.js`, `.msi`, `.msp`, `.mst`, `.dll`, `.ocx` y `.appx`.

* **Microsoft Defender:** Es la solución antimalware integrada en Windows Server. Puede ser gestionada de manera centralizada a través de WMI, directivas de grupo (GPO) o comandos de Windows PowerShell. En versiones recientes de Windows Server, Microsoft Defender viene instalado por defecto con una consola de administración similar a la de las versiones de cliente (Windows 10/11). Su administración puede incluir la configuración de exclusiones, la programación de escaneos y la definición de políticas de protección en tiempo real y remediación.

### 3. Procedimientos Prácticos
#### **A. Configuración de Políticas de Restricción de Software**
Este procedimiento se realiza a través de la consola de administración de políticas de grupo (Group Policy Management).
1.  **Creación de la GPO:** Se crea un nuevo objeto de política de grupo (GPO) y se vincula a una unidad organizativa específica, por ejemplo, "ProtectedServer". En el ejemplo, la GPO se nombra como `Software Restriction`.
2.  **Edición de la GPO:** Para configurar las políticas, se debe editar la GPO recién creada. La ruta para acceder a las políticas de restricción es `Computer Configuration / Policies / Windows Settings / Security Settings`.
3.  **Creación de Reglas:** Para definir nuevas políticas, se hace clic derecho en `Software Restriction Policies` y se selecciona `New Software Restriction Policies`. Esto crea un nuevo conjunto de reglas configurables.
4.  **Desuso:** A pesar de la posibilidad de configuración, estas directivas se consideran obsoletas y no se recomiendan para entornos modernos.
#### **B. Configuración de AppLocker**
AppLocker es la alternativa flexible y recomendada para el control de aplicaciones.
1.  **Acceso a AppLocker:** Desde la GPO que se está editando, se navega hasta `Application Control Policies` y se selecciona `AppLocker`.
2.  **Creación de Reglas por Defecto:** Antes de crear reglas de denegación (`Deny`), es una práctica recomendada crear reglas por defecto para asegurar el funcionamiento de componentes esenciales de Windows y otras aplicaciones. Estas reglas se generan automáticamente al seleccionar `Create Default Rules` dentro de la sección del tipo de archivo deseado (por ejemplo, `Executable Rules`).
3.  **Creación de una Regla de Denegación:**
    * **Inicio:** Se selecciona la opción para crear una nueva regla (`Create New Rule`) y se avanza al siguiente paso.
    * **Selección de Permiso:** Se elige si la regla será de `Allow` (permitir) o `Deny` (denegar). En el caso de controlar software no deseado, se elige `Deny`.
    * **Asignación de Grupo:** Se puede aplicar la regla a un grupo de seguridad específico (por ejemplo, `Backup Operators`) en lugar de a todos los usuarios (`Everyone`).
    * **Condiciones:** Se puede definir la condición de la regla basándose en tres criterios principales:
        * **Hash del Archivo (File Hash):** Permite prohibir la ejecución de un software basándose en su firma digital, sin importar dónde se encuentre. No obstante, los programas maliciosos pueden modificar su hash para evadir esta restricción.
        * **Ruta (Path):** Prohíbe la ejecución de software instalado en una ruta de archivo específica. Sin embargo, esta restricción se puede eludir si el software se instala en una ruta diferente.
        * **Editor (Publisher):** Esta es la opción más flexible, ya que se basa en la firma digital de un publicador de software legítimo. Esto es útil para controlar software autorizado que la organización decide no permitir, como Internet Explorer. Se navega hasta el archivo ejecutable (`iexplore.exe` en el ejemplo) y se define la regla para prohibir la ejecución del producto (`Internet Explorer`) del publicador (`O=MICROSOFT CORPORATION...`).
    * **Excepciones:** Se pueden añadir excepciones a la regla. Por ejemplo, dentro de una regla de denegación para Internet Explorer, se puede añadir una excepción para permitir la ejecución solo de una versión específica (ej., versión 11).
    * **Creación y Aplicación:** Tras configurar las excepciones, se finaliza la creación de la regla. Las reglas de AppLocker, incluyendo las reglas por defecto y las reglas personalizadas, se muestran en la consola de GPO.
#### **C. Gestión de Microsoft Defender**
La gestión de Microsoft Defender se puede realizar a través de PowerShell o GPOs.
1.  **Instalación y Verificación (versiones anteriores):** En versiones de Windows Server anteriores a la instalación por defecto, el motor antimalware y la interfaz gráfica se podían instalar con comandos de PowerShell. Para verificar su estado, se usaba el comando `SC Query Windefend`.
2.  **Configuración mediante GPOs:** Al igual que con las políticas de restricción, la gestión de Defender se realiza en el `Group Policy Management Editor`. La ruta específica es `Computer Configuration / Administrative Templates / Windows Components / Microsoft Defender Antivirus`.
3.  **Opciones de Configuración:** Las GPOs ofrecen una gran cantidad de configuraciones para adaptar Defender a las necesidades de la organización, incluyendo:
    * **Client Interface**
    * **Exclusions:** Exclusiones por extensión, ruta, dirección IP o proceso.
    * **Exploit Guard:** Incluye configuraciones para la reducción de la superficie de ataque (`Attack Surface Reduction`), el acceso controlado a carpetas (`Controlled Folder Access`) y la protección de red (`Network Protection`).
    * **MpEngine**
    * **Network Inspection System**
    * **Quarantine**
    * **Real-Time Protection**
    * **Remediation**
    * **Reporting**
    * **Scan**
    * **Security Intelligence Updates**
    * **Threats**
4.  **Administración Centralizada:** La capacidad de gestionar estas configuraciones a través de GPOs permite desplegar una política de seguridad antimalware coherente y específica para diferentes partes de la organización, como departamentos o sucursales, asegurando el comportamiento deseado del software de seguridad.

### 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** La implementación de políticas de control de software y el uso de soluciones antimalware como Microsoft Defender son esenciales para minimizar el riesgo de ejecución de software no autorizado o malicioso. Al restringir la ejecución de aplicaciones no deseadas, las organizaciones pueden reducir significativamente su superficie de ataque y proteger sus sistemas contra amenazas como el malware. Estas herramientas permiten un control granular que se adapta a las necesidades específicas de la organización.
* **Puntos de Aprendizaje Clave:**
    * Windows Server ofrece varias herramientas para el control de la ejecución de código, como las obsoletas políticas de restricción de software y la más moderna y flexible AppLocker.
    * AppLocker es superior porque permite una configuración más detallada, como la importación/exportación de reglas, la definición de reglas para grupos de usuarios específicos y la creación de excepciones.
    * Microsoft Defender es una solución antimalware robusta, administrable de forma centralizada a través de GPOs, lo que permite un control exhaustivo sobre su comportamiento en toda la infraestructura.
    * La administración centralizada a través de objetos de directiva de grupo es un método clave para desplegar tecnologías de seguridad en entornos empresariales.
* **Relevancia Técnica:** Entender y saber cómo desplegar estas tecnologías es crucial para los profesionales de la ciberseguridad y la administración de sistemas. La capacidad de configurar con precisión herramientas como AppLocker y Microsoft Defender permite adaptar la seguridad a los requisitos de rendimiento y funcionalidad de diferentes equipos o departamentos, equilibrando la protección con la operatividad del negocio. Los procedimientos detallados, como la creación de reglas por defecto en AppLocker o la configuración de exclusiones en Defender, son prácticas fundamentales para una gestión de seguridad efectiva.


---

Documentos de Referencia: "FSW Clase 36 – Windows Server BackUp.pdf"

# Informe Técnico: Copias de Seguridad en Windows Server

## 1. Resumen Ejecutivo
Este informe técnico se centra en el servicio de copias de seguridad de Windows Server, una herramienta fundamental para la seguridad y continuidad de las organizaciones. Se detallan los conceptos clave, las funcionalidades del servicio y los procedimientos prácticos para su instalación, configuración y uso. El objetivo es proporcionar una guía didáctica y técnica sobre cómo implementar una estrategia de backup robusta para proteger los datos contra incidentes de seguridad, como el ransomware.

---

## 2. Conceptos Fundamentales
El documento destaca varios conceptos clave que son cruciales para la planificación y ejecución de una estrategia de copias de seguridad efectiva.

* **Windows Server Backup:** Se trata de una característica o servicio del sistema operativo Windows Server que permite realizar copias de seguridad completas del servidor, de volúmenes, carpetas, archivos, el estado del sistema, máquinas virtuales o clústeres de volúmenes compartidos (CSV). Permite programar y automatizar los backups, así como configurar su rendimiento. También permite la recuperación completa o selectiva de datos a su ubicación original o a una diferente.

* **Recovery Point Objective (RPO):** Este concepto define la cantidad máxima de datos que una organización puede permitirse perder en caso de un incidente. Generalmente, se mide en tiempo y determina la frecuencia con la que se deben realizar las copias de seguridad. Por ejemplo, si el RPO es de una hora, los backups deben realizarse al menos cada hora para asegurar que la pérdida de datos no supere ese límite.

* **Recovery Time Objective (RTO):** Se refiere a la cantidad máxima de tiempo que se puede tardar en recuperar los datos perdidos y restaurar el servicio después de un fallo. Un RTO bajo implica la necesidad de tecnologías de alta disponibilidad, como los clústeres de conmutación por error (`failover clustering`), además del servicio de backup.

* **Otros Factores de Planificación:** Para una estrategia de backup completa, también se deben considerar:
    * **Tiempo de Retención:** El período durante el cual se deben conservar las copias de seguridad, que en algunos casos puede estar definido por requisitos legales.
    * **Alta Disponibilidad:** Tecnologías que aseguran la continuidad del servicio.
    * **Clasificación de Datos:** La categorización de los datos según su importancia y confidencialidad. Esto es crucial para la seguridad, ya que los backups de datos confidenciales deben estar tan protegidos como los datos originales para evitar fugas de información y posibles multas.

---

## 3. Procedimientos Prácticos

A continuación, se detallan los pasos para instalar, configurar y utilizar el servicio de Windows Server Backup.

### **Instalación del Servicio de Windows Server Backup**

El servicio no está instalado por defecto y se puede añadir a través de la consola de Server Manager o mediante PowerShell.

1.  **Acceso a la Consola de Server Manager:** Desde la consola principal, vaya a la sección **"Manage"** (Administrar) en la esquina superior derecha y seleccione **"Add Roles and Features"** (Agregar roles y características).
2.  **Selección de Características:** Siga el asistente hasta la sección **"Features"** (Características). A diferencia de un rol, el servicio de backup se instala como una característica. Desplácese hacia abajo en la lista hasta encontrar **"Windows Server Backup"**.
3.  **Confirmación e Instalación:** Marque la casilla de **"Windows Server Backup"** y complete el asistente dando clic en **"Next"** (Siguiente) e **"Install"** (Instalar). Este proceso añadirá la característica al sistema operativo.
4.  **Verificación:** Una vez completada la instalación, el servicio estará disponible en el menú de **"Tools"** (Herramientas) de la consola de Server Manager.

Alternativamente, la instalación se puede realizar utilizando el siguiente comando en PowerShell:
`Install-WindowsFeature -Name Windows-Server-Backup`.
Este comando automatiza la instalación del servicio, ahorrando tiempo en entornos de múltiples servidores.

### **Creación de un Disco Duro Virtual para Copias de Seguridad**

Se recomienda utilizar un volumen dedicado para almacenar los backups, ya que realizar un respaldo en el mismo volumen que se está copiando no tiene sentido y algunas operaciones de la herramienta no lo permiten.

1.  **Administración de Discos:** Desde la consola de Server Manager, navegue a **"Tools"** > **"Computer Management"** (Administración de equipos) > **"Disk Management"** (Administrador de discos).
2.  **Inicializar y Formatear un Disco:** Si ha añadido un nuevo disco virtual, este aparecerá como no inicializado. Utilice el asistente para inicializarlo y crear un **"New Simple Volume"** (Nuevo volumen simple). Siga los pasos para asignarle una letra y formatearlo.
3.  **Confirmación:** Verifique que el nuevo volumen aparece en la lista de discos disponibles, listo para ser utilizado como destino de las copias de seguridad.

### **Realización de un Backup Programado y Restauración Selectiva**

Este procedimiento detalla cómo configurar un backup de una carpeta específica y cómo restaurar un documento de esa copia de seguridad.

#### **Configuración de un Backup Programado**

1.  **Acceso al Servicio:** Abra el servicio **"Windows Server Backup"** desde el menú **"Tools"** de Server Manager.
2.  **Inicio del Asistente:** En el panel derecho de la consola de **"Local Backup"** (Copia de seguridad local), seleccione **"Backup Schedule"** (Programación de copias de seguridad).
3.  **Tipo de Configuración:** Elija la opción **"Custom"** (Personalizado) en lugar de **"Full Server"** (Servidor completo) para seleccionar elementos específicos.
4.  **Selección de Elementos:** Haga clic en **"Add Items"** (Agregar elementos) para seleccionar la carpeta o archivo que desea respaldar. Por ejemplo, se muestra cómo seleccionar una carpeta llamada **"Data"**.
5.  **Exclusiones (Opcional):** Si es necesario, puede acceder a **"Advanced Settings"** (Configuración avanzada) para añadir exclusiones de archivos o carpetas dentro del volumen seleccionado, lo que puede mejorar la eficiencia del backup.
6.  **Programación de la Frecuencia:** Configure la frecuencia de la copia de seguridad. Puede elegir entre una vez al día o a intervalos más cortos, especificando las horas deseadas para la ejecución del backup.
7.  **Destino del Backup:** Seleccione la ubicación de destino para la copia de seguridad. La opción recomendada es **"Back up to a hard disk that is dedicated for backups"** (Realizar copias de seguridad en un disco duro dedicado) o a un volumen específico, como el disco virtual que se creó previamente.
8.  **Finalización:** Revise la configuración y confirme para iniciar el proceso de programación del backup.

#### **Restauración de Datos**

1.  **Acceso a la Restauración:** En la consola de Windows Server Backup, seleccione **"Recover"** (Recuperar).
2.  **Selección del Origen:** El asistente le preguntará dónde está almacenada la copia de seguridad. Elija la opción correspondiente.
3.  **Selección del Tipo de Recuperación:** Elija el tipo de elementos a recuperar, como **"Files and folders"** (Archivos y carpetas) o **"Volumes"** (Volúmenes).
4.  **Selección de Elementos a Restaurar:** Navegue por la estructura del backup y seleccione los archivos o carpetas específicos que desea recuperar.
5.  **Destino de la Restauración:** Seleccione el destino de la recuperación. Puede ser la ubicación original o una **"Another location"** (otra ubicación) para comparar las versiones o evitar sobrescribir datos accidentalmente.
6.  **Confirmación:** Revise los detalles de la restauración y confirme para iniciar el proceso. La herramienta indicará el progreso y el resultado final.

---

## 4. Conclusiones y Puntos Clave

El servicio de Windows Server Backup es una herramienta integral y estable que se integra directamente en el sistema operativo, utilizando una tecnología idéntica a la empleada en Azure para operaciones de almacenamiento y máquinas virtuales en caliente, lo que garantiza una gran estabilidad y eficiencia.

### **Importancia y Beneficios de Seguridad**

* **Mitigación de Riesgos:** El servicio de backup es la principal defensa contra amenazas como el **ransomware**, que cifra los datos y exige un rescate. Una política de backup bien implementada permite restaurar los datos sin ceder a las demandas de los atacantes.
* **Eficiencia en la Recuperación:** La capacidad de realizar recuperaciones selectivas de archivos y carpetas individuales, sin necesidad de restaurar todo un volumen, optimiza el tiempo de recuperación y minimiza el impacto en la operación del negocio.
* **Flexibilidad en la Restauración:** La opción de restaurar datos a una ubicación diferente de la original proporciona flexibilidad y permite a los administradores comparar versiones de documentos o restaurar datos sin sobrescribir información existente.

### **Puntos de Aprendizaje Clave**

* **Planificación es Fundamental:** Antes de implementar un backup, es crucial definir los objetivos de recuperación (RPO y RTO), el tiempo de retención y la clasificación de los datos.
* **Verificación Constante:** Es vital realizar pruebas de restauración de manera regular para asegurar que las copias de seguridad funcionan correctamente y que los datos son recuperables. Un backup que no puede ser restaurado no tiene valor.
* **Conocimiento y Configuración:** Un conocimiento detallado de los componentes de Windows Server y su correcta configuración son esenciales para fortificar un sistema y marcar la diferencia en caso de un incidente de seguridad.

### **Relevancia Técnica**

Los procedimientos detallados en el material son de gran relevancia profesional, ya que las copias de seguridad son un pilar de la gestión de infraestructuras de TI. La capacidad de instalar y configurar esta herramienta de manera eficiente, así como de planificar y ejecutar estrategias de recuperación, es una habilidad indispensable en el ámbito de la ciberseguridad y la administración de sistemas. La tecnología subyacente del servicio de Windows Server Backup, probada en entornos como Azure, demuestra su fiabilidad y robustez para su uso en entornos corporativos.


---


Documentos de Referencia: "FSW Clase 38 – Windows Server Update Services.pdf"

# Informe Técnico: Windows Server Update Services (WSUS)

---

## 1. Resumen Ejecutivo
El servicio Windows Server Update Services (WSUS) es un rol fundamental en entornos empresariales para la gestión centralizada de actualizaciones de software de Microsoft. Este informe detalla cómo WSUS permite a los administradores gestionar de manera eficiente el despliegue, la aprobación y la supervisión de las actualizaciones. La implementación de WSUS no solo optimiza el tráfico de red y evita cuellos de botella, sino que también es un pilar básico de la ciberseguridad, ayudando a proteger la infraestructura contra vulnerabilidades conocidas.

---

## 2. Conceptos Fundamentales
### Windows Server Update Services (WSUS)
**Windows Server Update Services (WSUS)** es un rol de Windows Server diseñado para administrar y distribuir actualizaciones en una red corporativa. Funciona como un servidor de actualizaciones que centraliza la descarga de parches y los distribuye a los demás equipos de la organización, incluidos otros servidores WSUS, lo que permite crear jerarquías complejas en entornos grandes.

Las principales ventajas y funcionalidades de WSUS incluyen:
* **Administración de Políticas:** Permite configurar diferentes políticas para la aplicación de actualizaciones y gestionar su distribución.
* **Control de Aprobación:** Los administradores pueden aprobar o denegar manualmente las actualizaciones antes de que se desplieguen en la red.
* **Optimización de Red:** En lugar de que cada dispositivo descargue actualizaciones de Internet, el servidor WSUS descarga las actualizaciones una sola vez, reduciendo el tráfico de red, evitando cuellos de botella y disminuyendo el tráfico que debe ser analizado por firewalls.
* **Supervisión y Reportes:** Permite monitorizar el proceso de despliegue y generar informes para identificar equipos que no han recibido o aplicado correctamente las actualizaciones.

### Requisitos de WSUS
Para funcionar, el rol de WSUS tiene los siguientes requisitos y características:
* **Servicios de Información de Internet (IIS):** Utiliza un servicio web para la distribución de actualizaciones.
* **Microsoft .NET Framework 4.6 o superior:** Un componente de software necesario para ejecutar las aplicaciones de WSUS.
* **Microsoft Report Viewer Redistributable 2008 o superior:** Esencial para la generación de informes.
* **Base de Datos:** Requiere una base de datos, que puede ser SQL Server (versiones 2012 con SP1, 2012, 2008 R2 SP2, 2008 R2 SP1) o la base de datos interna de Windows (Windows Internal Database o WID). Por defecto, se utiliza **WID**, que crea un archivo `SUSDB.mdf` en la ruta `%windir%\wid\data` y necesita un mínimo de **40 GB de espacio en disco** para las actualizaciones.
* **Puertos y Capacidad:** Por defecto, utiliza los puertos **8530 para HTTP** y **8531 para HTTPS**. Un servidor con 4 GB de RAM puede soportar hasta 100,000 clientes, demostrando la eficiencia del servicio.

---

## 3. Procedimientos Prácticos
### Instalación del Rol de WSUS
La instalación del rol de WSUS se realiza a través del asistente de Server Manager.

1.  **Iniciar el Asistente:** En Server Manager, vaya a **"Manage"** y seleccione **"Add Roles and Features"**.
2.  **Selección del Rol:** En el asistente, navegue hasta la sección de **"Server Roles"** y marque la casilla de **"Windows Server Update Services"**. Al hacerlo, se le pedirá que agregue características requeridas; haga clic en **"Add Features"**.
3.  **Configuración de la Ubicación del Contenido:** El asistente le solicitará la ubicación donde se almacenarán las actualizaciones. Es necesario un disco formateado con NTFS y al menos 6 GB de espacio libre. Se puede especificar una ruta de acceso local o remota.
4.  **Servicios de Rol:** Mantenga los servicios de rol por defecto para el servidor web y WSUS, y continúe con el asistente.
5.  **Instalación:** Revise la confirmación y haga clic en **"Install"** para iniciar el proceso de instalación.
6.  **Tareas Post-Instalación:** Una vez completada la instalación, se deben ejecutar las tareas de post-instalación para finalizar la configuración del servidor.

### Configuración Inicial de WSUS
Después de la instalación, se utiliza un asistente de configuración para preparar el servidor WSUS.

1.  **Acceso a la Consola:** Desde el menú **"Tools"** de Server Manager, abra la consola **"Windows Server Update Services"**.
2.  **Asistente de Configuración:** Al iniciar, aparecerá un asistente. Es fundamental verificar que el servidor WSUS puede conectarse a un servidor de actualizaciones "upstream" (como Microsoft Update) y que el firewall está configurado para permitir el acceso a los clientes.
3.  **Fuente de Actualizaciones:** Elija si el servidor se sincronizará con **"Microsoft Update"** o con otro servidor WSUS.
4.  **Configuración de Proxy (Opcional):** Si su red requiere un servidor proxy, configure los ajustes necesarios en esta sección.
5.  **Iniciar Conexión:** Inicie la conexión con el servidor "upstream" para descargar la información de actualizaciones disponibles.
6.  **Selección de Opciones:** Posteriormente, el asistente permite elegir los idiomas, productos y clasificaciones de actualizaciones que se desean descargar y sincronizar. También se puede configurar un horario para la sincronización automática.
7.  **Despliegue de GPO:** Para que los equipos cliente descarguen actualizaciones del servidor WSUS local en lugar de Windows Update, se debe configurar una **directiva de grupo (GPO)** que apunte a la dirección del servidor WSUS.

### Gestión y Monitoreo
La consola de WSUS ofrece un panel de control completo para la administración diaria.

* **Estado de la Sincronización:** La consola muestra el estado de sincronización del servidor, incluyendo la fecha y hora de la última sincronización y el resultado.
* **Estado de los Equipos:** Se puede ver un resumen del estado de los equipos, incluyendo los que tienen errores, los que necesitan actualizaciones y los que ya están actualizados.
* **Informes:** La herramienta permite generar una variedad de informes, como el resumen de estado de actualizaciones, el estado detallado de equipos y el resultado de las sincronizaciones.
* **Grupos de Equipos:** Una de las funcionalidades más útiles es la creación de **grupos de equipos**. Esto permite aplicar actualizaciones de forma selectiva a grupos de prueba antes de desplegarlas progresivamente en el resto de la organización.
* **Aprobación de Actualizaciones:** Las actualizaciones deben ser aprobadas manualmente antes de su despliegue, aunque existe la opción de aprobar automáticamente ciertas actualizaciones.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
La gestión de actualizaciones es un pilar fundamental de la ciberseguridad. Muchas amenazas de malware y ataques se basan en **vulnerabilidades conocidas** que ya han sido corregidas mediante actualizaciones. Al mantener los dispositivos actualizados, se reduce significativamente el riesgo de éxito de estos ataques. WSUS proporciona una forma eficiente y segura de lograr esto en un entorno empresarial. Además de la seguridad, los beneficios de WSUS incluyen la optimización del ancho de banda y la capacidad de centralizar el control de las actualizaciones.

### Puntos de Aprendizaje Clave
* WSUS es una solución eficiente para el despliegue, monitoreo y aplicación de actualizaciones en una red.
* La implementación de WSUS reduce la carga en la red al descargar las actualizaciones una sola vez.
* Permite la creación de grupos de equipos para un despliegue progresivo de actualizaciones.
* La capacidad de generar informes es vital para auditar el estado de seguridad de la red.
* La configuración del cliente mediante GPO es necesaria para que los equipos se dirijan al servidor WSUS en lugar de a Windows Update.

### Relevancia Técnica
El uso de WSUS es una práctica estándar en la administración de sistemas para garantizar que la infraestructura de TI esté protegida contra las últimas amenazas. La capacidad de configurar este servicio, gestionar las actualizaciones de manera granular y auditar el estado de los parches en los equipos es una habilidad técnica esencial para cualquier profesional de IT. La consola de administración y los cmdlets de PowerShell brindan la flexibilidad necesaria para adaptarse a cualquier tamaño de organización, desde pequeñas redes hasta jerarquías de servidores masivas. El conocimiento de WSUS es crucial para mantener un entorno seguro y estable.


---

Documentos de Referencia: "FSW Clase 39 – Seguridad DHCP.pdf"

# Informe Técnico: Seguridad en el Servicio DHCP

---

## 1. Resumen Ejecutivo
El servicio DHCP (Dynamic Host Configuration Protocol) es esencial para la asignación automática de direcciones IP en cualquier red. La correcta administración de este servicio es crítica para la seguridad de toda la red, ya que un servicio DHCP comprometido puede facilitar ataques como la interceptación de información. Este informe técnico explora las funcionalidades de seguridad de DHCP en un entorno de Windows Server, incluyendo la autorización en Active Directory, la configuración de clústeres, la protección de nombres DNS, los registros de auditoría y los filtros MAC. Además, se detallan los procedimientos para implementar estas medidas, demostrando cómo fortalecer la red contra posibles amenazas.

---

## 2. Conceptos Fundamentales
### Funcionamiento del Servicio DHCP
El servicio DHCP opera escuchando constantemente las solicitudes de dispositivos en la red que requieren una dirección IP. Cualquier dispositivo configurado para la asignación automática de IP enviará una solicitud a la red. El primer servidor DHCP que responda ofrecerá la configuración del adaptador de red del dispositivo.

* **Falta de Seguridad por Defecto:** El protocolo DHCP no incluye mecanismos de seguridad por defecto, como la autenticación mediante certificados digitales. Esto permite que cualquier servidor DHCP no autorizado en la red pueda responder a las solicitudes y realizar una configuración maliciosa en los dispositivos.

### Amenazas en el Servicio DHCP
Una suplantación de identidad del servicio DHCP podría configurar de manera maliciosa los adaptadores de red de los equipos, lo que podría facilitar ataques de interceptación de información, o el envío de peticiones a servidores maliciosos diseñados para recopilar datos confidenciales, como contraseñas y datos bancarios.

### Clúster de Servidores DHCP
Desde Windows Server 2016, es posible configurar un **clúster de servidores DHCP** con dos o más servidores.
* **Alta Disponibilidad:** Un clúster de DHCP evita la pérdida del servicio si uno de los servidores falla, ya que los servidores activos mantienen el conjunto de direcciones disponibles.
* **Ventajas sobre versiones anteriores:** En versiones anteriores de Windows Server, se utilizaba un método de división de direcciones (`split-scope`) donde cada servidor gestionaba la mitad del pool de direcciones, lo que desperdiciaba recursos y podía provocar denegaciones de servicio si dos dispositivos recibían la misma IP. El clúster supera estos problemas al permitir que múltiples servidores mantengan el mismo pool de direcciones.

---

## 3. Procedimientos Prácticos
### Instalación y Autorización de DHCP
Para garantizar la seguridad y el correcto funcionamiento del servicio en un entorno de Active Directory, el servidor DHCP debe ser autorizado.

1.  **Instalación del Rol:** Vaya a **Server Manager** y seleccione **"Add Roles and Features"**. Siga el asistente hasta la sección **"Server Roles"** y seleccione **"DHCP Server"**.
2.  **Agregar Herramientas:** Confirme la adición de las herramientas de administración requeridas, como **"Remote Server Administration Tools"** y **"DHCP Server Tools"**.
3.  **Autorización en Active Directory:** Tras la instalación, el servicio DHCP no se iniciará hasta que sea autorizado. Utilice el asistente de post-instalación para autorizar el servidor, lo que requiere credenciales de un usuario con privilegios de dominio.
4.  **Verificación:** Una vez autorizado, los pools de direcciones se activarán y se podrá gestionar el servicio desde la consola de administración de DHCP.

### Medidas de Seguridad Adicionales
Una vez instalado y autorizado el servidor DHCP, se pueden configurar varias características de seguridad.

* **Protección de Nombres DNS:** Por defecto, esta característica está deshabilitada. Al habilitarla, el servidor DHCP registrará los registros `A` y `PTR` en el servidor DNS en nombre de los clientes. Esto asegura que los registros DNS tengan prioridad si provienen de un servidor DHCP autorizado.
* **Registros de Auditoría (DHCP Audit Log):** Es crucial habilitar el servicio de auditoría de DHCP para el análisis de la actividad. Estos registros ayudan a detectar problemas o ataques en la red. En muchos países, la retención de estos registros es obligatoria por ley para justificar la asignación de IP a dispositivos en momentos específicos. Esta configuración se encuentra en las propiedades del servidor, en la pestaña **"Advanced"**.
* **Filtros MAC:** Los filtros MAC se utilizan para permitir o denegar los servicios DHCP a direcciones MAC específicas. Al configurar una **"Deny List"**, el servidor rechazará las solicitudes de los clientes cuyas direcciones MAC se encuentren en esa lista.
* **Protección DHCP en Virtualización (DHCP Guard):** En entornos de virtualización con Hyper-V, se puede habilitar **DHCP Guard** para evitar que máquinas virtuales no autorizadas actúen como servidores DHCP maliciosos. Esta función descarta los mensajes de servidores DHCP no autorizados procedentes de máquinas virtuales.

### Creación de un Clúster de DHCP
1.  **Configurar Failover:** Desde la consola de administración de DHCP, haga clic derecho en el pool (scope) deseado y seleccione **"Configure Failover"**.
2.  **Selección de Servidor:** Siga el asistente para seleccionar los servidores que participarán en el clúster. Se buscarán servidores DHCP autorizados en el dominio para crear una relación de `failover`.
3.  **Configuración de Relación:** Configure cómo se repartirá la carga de trabajo entre los servidores y establezca una contraseña compartida para autenticar la comunicación entre ellos. Una vez finalizado, el clúster estará operativo.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
El servicio DHCP, a pesar de la falta de seguridad inherente en su protocolo, es un pilar fundamental para cualquier red. Una administración adecuada y la configuración de sus características de seguridad aumentan significativamente la protección de la red y de servicios relacionados como DNS. La implementación de medidas como la autorización del servidor, los clústeres de alta disponibilidad y los registros de auditoría permiten detectar intrusiones y prevenir ataques. Además, la protección contra la suplantación de DHCP en entornos virtuales con **DHCP Guard** es crucial para evitar ataques dentro del hipervisor.

### Puntos de Aprendizaje Clave
* La seguridad en DHCP es un tema crítico que debe ser planificado y gestionado con cuidado.
* La autorización de servidores DHCP en Active Directory es un paso esencial para prevenir servidores maliciosos.
* Los clústeres de DHCP mejoran la disponibilidad del servicio y la gestión de la carga de trabajo, reemplazando métodos menos eficientes.
* Habilitar los registros de auditoría es vital para la detección de problemas y ataques, y en algunos casos es un requisito legal.
* La configuración de filtros MAC y de la protección de nombres DNS añade capas adicionales de seguridad a la red.

### Relevancia Técnica
El conocimiento detallado de la seguridad en DHCP es indispensable para los profesionales de IT. Desde la instalación y autorización del servicio hasta la configuración de opciones avanzadas, como la protección de nombres DNS y los clústeres de alta disponibilidad, cada paso es una habilidad técnica valiosa. La capacidad de implementar estas características de seguridad, así como de auditar los registros de actividad, es fundamental para mantener un entorno de red seguro, estable y conforme a las regulaciones. Las herramientas integradas en Windows Server ofrecen un amplio abanico de posibilidades para la gestión de la seguridad en este servicio crítico.

---

Documentos de Referencia: "FSW Clase 40 – Seguridad DNS.pdf"

# Informe Técnico: Seguridad DNS

## 1\. Resumen Ejecutivo

Este informe técnico se centra en la seguridad del servicio DNS, un componente fundamental en la infraestructura de cualquier organización. Se analizan los conceptos básicos del servicio, las consideraciones de seguridad, y las características avanzadas como DNSSEC, las políticas de DNS y el RRL (Response Rate Limiting). El objetivo es proveer una guía exhaustiva sobre cómo administrar y fortificar los servidores DNS para prevenir ataques, detectar intrusiones y mejorar la seguridad general de la red.

## 2\. Conceptos Fundamentales

El servicio de DNS es un protocolo esencial que permite resolver consultas de nombres de dominio, como "https://www.google.com/search?q=google.com" o "wikipedia.org", asociándolas a una dirección de red específica (IPv4 o IPv6). Este servicio es crucial para el funcionamiento de los entornos de red modernos y es indispensable para el Directorio Activo (Active Directory).

A continuación, se detallan los conceptos clave:

  * **Zonas de Búsqueda (Search Zones):** Son agrupaciones de diferentes recursos que corresponden a un nombre de dominio determinado.
      * **Zonas de Búsqueda Directa:** Funcionan cuando una máquina consulta un nombre de dominio y el servidor DNS responde con una dirección IP.
      * **Zonas de Búsqueda Inversa (Reverse Lookup Zones):** Proporcionan el nombre de un recurso a partir de una dirección IP.
  * **Replicación de Zonas:** El protocolo DNS cuenta con un sistema de replicación de zonas que se usa en servidores que no son controladores de dominio o en zonas no integradas en Active Directory. En el caso de zonas integradas en Active Directory, la replicación se realiza a través de su propio protocolo, que incluye procesos de autenticación y cifrado para comunicaciones seguras.
  * **Opciones de Seguridad de DNS:**
      * **DNS Cache Locking:** Evita la sobrescritura de registros en la caché del servidor por el valor de su TTL (Time-To-Live) o un porcentaje del mismo. Esto ayuda a prevenir que software malicioso genere entradas persistentes en la caché del servidor que apunten a sitios maliciosos. El bloqueo se configura como un porcentaje, con un valor por defecto del 100%. Se recomienda configurar el bloqueo de caché a un mínimo del 90%.
      * **DNS Socket Pool:** Es una característica de Windows Server que habilita la aleatorización de puertos de origen para las consultas DNS. Esto dificulta ataques como el DNS spoofing. El tamaño del grupo de sockets es de 2,500 por defecto, y se puede configurar un valor entre 0 y 10,000. Un valor más alto aumenta la protección.
  * **DNSSEC (Domain Name System Security Extensions):** Permite firmar criptográficamente una zona DNS y todos sus registros, utilizando certificados digitales y una infraestructura de clave pública. Los clientes pueden validar la respuesta del servidor DNS, lo que protege contra la falsificación de registros.
      * **Trust Anchor:** Es una entidad autorizada que representa una clave pública asociada a una zona específica. En DNS, el Trust Anchor es el registro de recursos DNSKEY o Delegation Signer (DS). Los clientes usan estos registros para construir cadenas de confianza. El Trust Anchor debe configurarse en la zona de cada servidor DNS del dominio para validar las respuestas. Las zonas integradas en Active Directory pueden distribuir el Trust Anchor a los controladores de dominio.
  * **DNS Policies:** Son directivas en Windows Server que permiten configurar la resolución de servidores con múltiples opciones. Por ejemplo, pueden dirigir una consulta al servidor más cercano geográficamente. También se pueden usar para crear filtros, evitar ataques maliciosos, descartar peticiones mal configuradas y fortificar la resolución de servicios.
  * **Response Rate Limiting (RRL):** Una característica de Windows Server para proteger contra ataques de amplificación DNS. El RRL limita el número de respuestas similares que el servidor enviará a clientes de la misma subred. Esto defiende al servidor para que no sea utilizado involuntariamente en ataques de denegación de servicio distribuido (DDoS).

## 3\. Procedimientos Prácticos

El documento describe una demostración práctica para configurar y administrar la seguridad de DNS. A continuación, se detallan los procedimientos principales.

### **Acceso a la Consola de Administración de DNS**

1.  Abrir el **Server Manager**.
2.  Navegar a la sección de **Tools**.
3.  Seleccionar la consola de **DNS**, tal como se ilustra en las capturas de pantalla.

### **Creación de Registros de Host (A y AAAA)**

1.  En la consola de DNS, seleccionar la zona de búsqueda directa del dominio (ej., Hackers.Academy).
2.  Hacer clic derecho sobre la zona y elegir la opción **New Host (A or AAAA)**, como se muestra en la captura de pantalla.
3.  En la ventana de "New Host", se ingresa un nombre para el host (ej., "serverweb") y su dirección IP.
4.  Se puede marcar la opción para crear el registro de búsqueda inversa (PTR) correspondiente.
5.  Hacer clic en **Add Host**.

### **Creación de Registros de Alias (CNAME)**

1.  En la consola de DNS, hacer clic derecho en la zona de dominio (ej., Hackers.Academy).
2.  Seleccionar la opción **New Alias (CNAME)**.
3.  En la nueva ventana, se introduce el nombre del alias (ej., "www").
4.  Se selecciona el registro de host (tipo A) al que apuntará el alias, en este caso, "serverweb.hackers.academy", navegando a través de las zonas de búsqueda directa, como se muestra en las capturas.
5.  Hacer clic en **OK**.

### **Creación de una Nueva Zona**

1.  En la consola de DNS, hacer clic derecho en **Forward Lookup Zones**.
2.  Seleccionar **New Zone...**.
3.  Se abre el asistente "New Zone Wizard". Se puede elegir entre crear una zona **Primary zone**, **Secondary zone** o **Stub zone**. Se explica que una zona secundaria es una copia de solo lectura.
4.  Al crear una zona, se puede optar por integrarla en **Active Directory**.
      * Si se selecciona esta opción, la replicación se hará de forma segura a través del protocolo de replicación de Active Directory.
      * Si no se selecciona, se utilizará el sistema de replicación por zonas de transferencia del propio protocolo DNS.
5.  Se elige un nombre para la zona (ej., "hola.com") y se finaliza el asistente.

### **Configuración de DNS Cache Locking y RRL**

El documento menciona que estas opciones se pueden configurar a través de la línea de comandos o Windows PowerShell.

  * **Comando para Cache Locking:** `dnscmd /Config /CacheLockingPercent <percent>`.
  * **PowerShell para Cache Locking:** `Set-DnsServerCache -LockingPercent <value>`.
  * **Comandos para RRL:** `Set-DNSServerRRL` y `Get-DNSServerRRL | F.L.`.

### **Firma de una Zona con DNSSEC**

1.  En la consola de DNS, hacer clic derecho en la zona que se desea firmar (ej., "hola.com").
2.  Navegar a **DNSSEC** y seleccionar **Sign the Zone...**.
3.  Se abre el asistente "Zone Signing Wizard".
4.  En la ventana de **Key Signing Key (KSK)**, se selecciona el algoritmo criptográfico y la longitud de la clave, y se hace clic en **Add** para configurar los parámetros, como se muestra en las capturas.
5.  Seguir los pasos del asistente para firmar la zona.
6.  Una vez firmada, al refrescar la zona, aparecerán nuevos registros relacionados con el sistema de claves públicas (DNSKEY, RRSIG, NSEC3, etc.), que respaldan la autenticación de los registros.

## 4\. Conclusiones y Puntos Clave

### **Importancia y Beneficios de Seguridad**

El servicio DNS, aunque intrínsecamente inseguro en su protocolo base, es fundamental para cualquier organización, y su correcta administración es clave para aumentar la seguridad de toda la red. La implementación de medidas de seguridad como DNSSEC, políticas de DNS y RRL no solo protegen el servidor de ataques directos, sino que también evitan que sea utilizado involuntariamente para atacar a otras organizaciones. Los registros de actividad del DNS también son una fuente vital para detectar intrusiones y accesos no autorizados a la red.

### **Puntos de Aprendizaje Clave**

  * Se debe entender la diferencia entre las zonas de búsqueda directa e inversa, así como las opciones de replicación de zonas entre servidores DNS y su relación con Active Directory.
  * Existen tecnologías integradas en Windows Server que permiten mitigar amenazas conocidas, como el DNS Cache Locking contra registros maliciosos persistentes y el DNS Socket Pool contra el spoofing.
  * La firma de zonas con DNSSEC es una característica poderosa para proteger contra la falsificación de registros, proporcionando una infraestructura DNS más segura.
  * Las políticas DNS ofrecen una capacidad avanzada para fortificar la resolución de servicios, permitiendo optimizar el rendimiento y filtrar peticiones maliciosas.
  * RRL es una defensa crucial para evitar que los servidores DNS sean cómplices en ataques de denegación de servicio distribuido (DDoS), lo que ayuda a evitar implicaciones legales y económicas.

### **Relevancia Técnica**

La capacidad de administrar y configurar estas características de seguridad es de suma importancia en un entorno profesional. Un fallo en el servicio DNS o una mala configuración puede llevar a graves problemas, como la denegación de servicio o el envío de peticiones a máquinas no legítimas. Por tanto, los conocimientos sobre cómo implementar DNSSEC, configurar políticas, utilizar RRL y gestionar correctamente las zonas de replicación son fundamentales para un administrador de sistemas o un profesional de la ciberseguridad, asegurando una infraestructura de red robusta y resiliente.