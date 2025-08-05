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