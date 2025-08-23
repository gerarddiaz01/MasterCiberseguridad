Documentos de Referencia: "5-17 Seguridad de servidores.pdf", "FSW Clase 17 – Gestión de seguridad de servidores.pdf"

### Informe Detallado: Gestión de Seguridad de Servidores y Windows Server

#### 1. Seguridad Informática, Activos de la Organización y Fortificación de Sistemas

La seguridad informática es la disciplina encargada de analizar, planificar y proteger los activos de una organización relacionados con los sistemas informáticos. Un activo es un recurso con un valor determinado para la organización, que puede ser un equipo, un servicio o un dato.

Para gestionar la seguridad, es crucial seguir un proceso estructurado. Lo primero es identificar y clasificar los activos en función de su importancia para el modelo de negocio. Por ejemplo, una base de datos de un hospital que maneja datos confidenciales de pacientes tiene una importancia mucho mayor que una base de datos de una tienda online que solo lista productos. Incluso dentro de una misma empresa, una base de datos de productos es menos crítica que la que contiene datos personales, bancarios o de pago de los clientes.

Una vez que los activos están identificados y clasificados, el siguiente paso es identificar las amenazas y riesgos asociados a cada uno de ellos para poder mitigarlos. Los riesgos varían según el tipo de activo y su ubicación. Por ejemplo, una página web expuesta en internet tendrá riesgos diferentes a los de una base de datos alojada en la infraestructura interna de la organización. Para mitigar estos riesgos, se aplican medidas de seguridad, que pueden ser configuraciones en la propia tecnología (servidor o dispositivo) o el despliegue de tecnologías complementarias, como un firewall o un IPS (Intrusion Prevention System). Un IPS, por ejemplo, puede filtrar el tráfico entre un servidor web y una base de datos para prevenir un ataque de inyección de SQL.

#### 2. La Tríada de la Ciberseguridad: Confidencialidad, Integridad y Disponibilidad

La seguridad informática se basa en tres pilares fundamentales, conocidos como la tríada de la ciberseguridad:

* **Confidencialidad:** Garantiza que los datos solo sean accesibles por personal autorizado. Su importancia varía según el tipo de información. Un listado de productos de una tienda online no requiere confidencialidad, ya que está diseñado para ser público, mientras que los datos personales y bancarios de los clientes sí la necesitan.
* **Integridad:** Asegura que los datos no sean modificados de forma no autorizada. Esto es vital para evitar alteraciones maliciosas.
* **Disponibilidad:** Se refiere a la accesibilidad de los datos y servicios cuando se necesitan. Para una empresa como PayPal o Visa, la disponibilidad de sus servidores es crítica, ya que su modelo de negocio se detendría si estos cayeran. La disponibilidad necesaria varía; algunos datos históricos pueden no requerir estar disponibles constantemente, mientras que otros, críticos para la operación diaria, deben estarlo en todo momento.

#### 3. Premisas Básicas para Fortificar Sistemas

Según el experto en seguridad Bruce Schneier, "la seguridad no es un producto, es un proceso". Esto significa que la fortificación de la infraestructura no es una tarea puntual, sino un plan dinámico que debe ser revisado y actualizado constantemente. La infraestructura cambia con el tiempo debido a nuevas actualizaciones, el descubrimiento de vulnerabilidades o la obsolescencia de herramientas. Por ello, las medidas de seguridad deben adaptarse continuamente.

Es fundamental asumir que la seguridad al 100% no existe. La mayoría de las organizaciones planifican un modelo de acción con procesos reactivos para minimizar el impacto en caso de una brecha de seguridad.

Para fortificar los sistemas, se aplican tres premisas básicas:

* **Defensa en Profundidad (Defense in Depth):** Consiste en implementar múltiples capas de seguridad. Si una barrera falla, otras capas detendrán el ataque o impedirán el acceso no autorizado. Esto proporciona un tiempo de reacción para que el personal de seguridad pueda detectar y actuar ante la intrusión.
* **Mínima Exposición (Minimum Exposure):** Un sistema debe utilizar únicamente los componentes necesarios para su función. Si un servidor es un servidor web y de DNS, debe tener solo esos roles. Es crucial desinstalar servicios que ya no se usan para evitar que se conviertan en vulnerabilidades por falta de mantenimiento. En muchas organizaciones, servidores antiguos se dejan en funcionamiento, lo que puede crear una brecha de seguridad que un atacante puede usar para pivotar y atacar servicios más modernos o internos.
* **Mínimo Privilegio Asignado (Minimum Assigned Privilege):** Se debe asignar a cada usuario, identidad o servicio solo los permisos estrictamente necesarios para realizar su tarea. Por ejemplo, un usuario que realiza backups solo debe tener permisos de operador de backups, no de administrador del dominio. Esto reduce el impacto si la identidad de ese usuario es comprometida por malware o si sus credenciales son robadas.

#### 4. Riesgos de Seguridad

Existen diversos riesgos de seguridad que amenazan la infraestructura informática.

* **Malware:** Software malicioso que incluye:
    * **Virus, Gusanos y Troyanos:** El software malicioso camuflado en programas legítimos, que a menudo establecen una conexión inversa para descargar más payloads o permitir el control del dispositivo.
    * **Rootkits y Keyloggers:** Programas diseñados para pasar desapercibidos y capturar información, como contraseñas, pulsaciones de teclado, capturas de pantalla y datos bancarios.
    * **Backdoor:** Abren una puerta trasera en el dispositivo para que un atacante pueda conectarse en el futuro.
    * **Ransomware:** Cifra los datos del dispositivo y exige un rescate monetario para proporcionar la clave de descifrado. Es un negocio muy rentable que afecta a empresas de todos los tamaños.
    * **Phishing:** Sitios web maliciosos que suplantan páginas legítimas para robar credenciales. Estos ataques pueden ser automatizados y diseñados específicamente para una organización.
* **Otros Riesgos:**
    * **Robo de credenciales:** Obtención de contraseñas de forma física, observando al usuario.
    * **Fuga de datos confidenciales:** Pérdida de información sensible, que puede ser accidental o intencionada (por ejemplo, empleados que venden datos a la competencia).
    * **Robo de equipos.**
    * **Repercusiones legales y pérdida de imagen:** Una empresa atacada puede ser utilizada de forma involuntaria para lanzar ataques contra otras organizaciones, lo que genera consecuencias legales y daña su reputación.

#### 5. Buenas Prácticas de Seguridad

Un conjunto de buenas prácticas es esencial para mantener la seguridad de la infraestructura. La planificación de la seguridad debe ser dinámica, con revisiones y mejoras constantes.

* **Política de Actualización:** Es fundamental diseñar una política de actualización de aplicaciones. Mantener todo actualizado es más importante que depender únicamente de una solución antimalware.
* **Principio de Mínimo Privilegio:** Aplicar este principio y restringir el uso de cuentas privilegiadas es una buena práctica clave.
* **Cuentas Específicas:** Usar cuentas de usuario específicas para cada tarea.
* **Control de Acceso Físico:** Diseñar un plan de control de acceso físico a los dispositivos, especialmente a los servidores críticos y controladores de dominio, es vital para evitar que personal no autorizado acceda a ellos.

El primer paso para proteger cualquier tecnología es entender cómo funciona y configurarla correctamente. Una vez que el dispositivo, sistema operativo o servicio está configurado de forma segura, se pueden implementar medidas adicionales para reforzar la seguridad.

#### 6. Introducción a Windows Server y Server Manager

Windows Server es el sistema operativo de servidor de Microsoft. El **Windows Server Evaluation Center** permite descargar la imagen ISO de Windows Server 2022 para laboratorios. Al instalarlo, se puede elegir entre dos versiones principales: **Standard** y **Datacenter**.

* La versión **Standard** está diseñada para entornos con hasta dos máquinas virtuales.
* La versión **Datacenter** está pensada para entornos que requieren más de dos máquinas virtuales.

Ambas versiones pueden instalarse con o sin la **Experiencia de Escritorio**, es decir, con o sin entorno gráfico. Para los laboratorios, se recomienda la versión Datacenter con experiencia de escritorio para tener acceso a todas las funcionalidades y poder trabajar con la interfaz gráfica. El licenciamiento de Windows Server se basa en el número de núcleos (cores) del dispositivo, no por equipo.

Una vez instalado, el primer componente que se ejecuta es el **Administrador del servidor (Server Manager)**. Esta es la consola de administración principal que permite realizar la mayoría de las tareas de gestión en Windows Server.

* **Panel de Control del Servidor:** Desde el panel de control se pueden instalar roles, servicios o características, tanto en el servidor local como en otras máquinas de la infraestructura.
* **Administración Local y Remota:** La sección **Local Server** proporciona información detallada del hardware y permite monitorizar la actividad del dispositivo, incluyendo logs de eventos, servicios y rendimiento. Una de las características más interesantes de Server Manager es su capacidad para conectarse y administrar de forma remota otros servidores, incluso aquellos que no tienen entorno gráfico (Server Core). Esto hace que los servidores sin interfaz gráfica sean más eficientes, ya que no necesitan actualizaciones de componentes gráficos y tienen menos vulnerabilidades.
* **Gestión de Servidores:** Desde el menú **Manage**, se pueden agregar otros servidores a la consola o crear grupos de servidores para una administración centralizada.

El informe concluye que la seguridad de la infraestructura debe ser un proceso dinámico y constante. Es crucial entender cómo funciona cada tecnología para poder configurarla correctamente y, a partir de ahí, implementar medidas de seguridad adicionales.