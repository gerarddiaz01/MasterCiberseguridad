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