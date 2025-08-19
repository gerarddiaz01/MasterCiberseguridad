Documentos de Referencia: "FSL Clase 21 – Logging.pdf"

# Informe Técnico: Fundamentos y Gestión de Logging en GNU/Linux

### 1\. Resumen Ejecutivo

Este informe técnico se centra en el tema del logging, un proceso fundamental en la administración y seguridad de sistemas GNU/Linux. Se exploran conceptos clave como qué es un log y el proceso de logging, sus propósitos, y la importancia de su correcta configuración para mejorar la disponibilidad y seguridad del sistema. El informe detalla la clasificación de los logs por severidad, los componentes básicos de un sistema de logging, la ubicación de los archivos de log más comunes y, finalmente, un desglose de los procedimientos prácticos para configurar, gestionar y rotar logs utilizando herramientas como **rsyslog** y **logrotate**.

### 2\. Conceptos Fundamentales

  * **¿Qué es un Log?:** Un log, también conocido como registro, es un archivo o registro cronológico que contiene información detallada sobre eventos, acciones y mensajes relevantes que ocurren en un sistema informático. Los eventos son generados por los servicios y utilidades del sistema. Ejemplos de eventos que generan logs incluyen la apertura de un archivo, un inicio de sesión en el sistema o un error al realizar una acción no permitida. Además, programas y herramientas externas también pueden generar sus propios logs. El resultado del logging es un historial detallado de lo que ha ocurrido en el sistema.

  * **¿Qué es el Logging?:** El logging es el proceso o la actividad de registrar y almacenar los eventos y actividades del sistema para su posterior revisión.

  * **Propósitos del Logging:**

      * **Monitorización:** Permite el seguimiento de las actividades que tienen lugar en el sistema para monitorear su estado.
      * **Detección de Errores:** Ayuda a identificar la causa de un error para poder resolverlo.
      * **Investigación de Incidentes de Seguridad:** Contribuye a determinar la causa de un posible ataque y tomar medidas preventivas.
      * **Análisis Forense:** Facilita la recopilación de información sobre eventos pasados para buscar posibles causas en un incidente informático.

  * **Clasificación de Mensajes en rsyslogd:**

      * **Facility:** Indica el componente del sistema que generó el evento y lo dirige a un destino. Ejemplos incluyen `auth` (sistema de autenticación), `cron` (tareas programadas), `kern` (kernel), `mail`, y `syslog`.
      * **Severity:** Define el nivel de gravedad o importancia de un mensaje.
          * **Emergency (0, emerg):** Errores críticos que requieren atención inmediata.
          * **Alert (1, alert):** Errores graves que pueden afectar la funcionalidad del sistema.
          * **Critical (2, crit):** Errores que afectan el funcionamiento normal del sistema, aunque no son críticos.
          * **Error (3, err):** Errores no críticos que pueden afectar el funcionamiento normal.
          * **Warning (4, warning):** Alertas sobre posibles problemas que no son lo suficientemente graves como para ser considerados errores.
          * **Notice (5, notice):** Información normal pero significativa.
          * **Informational (6, info):** Mensajes sobre el funcionamiento normal del sistema.
          * **Debug (7, debug):** Mensajes introducidos por desarrolladores para identificar y corregir errores en el código.

  * **Componentes Básicos de Logging en GNU/Linux:**

      * **Syslog:** Un demonio del sistema que recibe, procesa y almacena mensajes en archivos de log.
      * **Rsyslog:** Una aplicación que implementa el protocolo syslog, con la capacidad de actuar como servidor y cliente para la captura, registro y procesamiento de logs. Permite centralizar el logging de múltiples máquinas.
      * **Journalctl:** Un demonio que recopila logs de todas las fuentes disponibles y los almacena en un formato binario. La herramienta de línea de comandos `journalctl` se usa para visualizar y manipular estos registros.

  * **Consideraciones de Logging:**

      * Los logs se crean por defecto como ficheros de texto plano.
      * **Separación de los logs del resto del sistema:** Es una buena práctica aislar los logs en una partición separada para evitar que su crecimiento cause problemas en la partición raíz.
      * **Rotación de los logs:** Es crucial gestionar el crecimiento indefinido de los archivos de log.
      * **Conocer el funcionamiento de las aplicaciones:** Se debe saber si las aplicaciones usan logs del sistema o generan sus propios logs.
      * **Alertas:** Es importante configurar alertas a partir de la evaluación periódica de los logs para notificar eventos importantes.
      * **Infraestructura de logging:** En entornos con múltiples servidores, puede ser necesario centralizar la gestión de los logs para facilitar su análisis.

  * **Ubicación de Logs Comunes:** La ubicación de los logs puede variar según la distribución GNU/Linux.

      * **/var/log/syslog:** Registros generales del sistema.
      * **/var/log/dmesg:** Registra únicamente los mensajes del kernel.
      * **/var/log/messages:** Contiene eventos generales del sistema en distribuciones como CentOS o Fedora.
      * **/var/log/auth.log:** Almacena los registros de autenticación y autorización, como inicios de sesión correctos y fallidos.

### 3\. Procedimientos Prácticos

#### 3.1. Visualización de Logs con `journalctl`

Este procedimiento muestra cómo utilizar la herramienta `journalctl` para visualizar los logs del sistema, una herramienta que recopila datos de todas las fuentes disponibles y los almacena en un formato binario para una manipulación más sencilla.

1.  **Ver los logs del arranque actual:**

      * **Comando:** `journalctl -b`
      * **Descripción:** El parámetro `-b` (boot) muestra todos los registros que se han generado desde el último arranque del sistema. La salida de este comando es muy extensa, y la tecla `Enter` permite avanzar por las líneas, como se aprecia en la captura de pantalla.

2.  **Ver un listado de los últimos arranques:**

      * **Comando:** `journalctl --list-boots`
      * **Descripción:** Muestra un listado detallado y ordenado de los últimos arranques del sistema, incluyendo una fecha de inicio y finalización, así como un identificador único por cada arranque. Esto permite una monitorización fácil de todos los arranques de la máquina.

3.  **Filtrar logs por nivel de severidad:**

      * **Comando:** `journalctl -p 3 -b`
      * **Descripción:** El parámetro `-p` permite filtrar logs por nivel de prioridad o superior. En este caso, el valor `3` corresponde a errores (`err`), por lo que se mostrarán todos los errores de este nivel, así como los de mayor severidad (crítico, alerta y emergencia), del arranque actual (`-b`). Esto es útil para localizar rápidamente problemas en el sistema.

#### 3.2. Configuración de Rsyslog para Redirigir Logs

Este procedimiento detalla cómo configurar el servicio `rsyslog` para redirigir los eventos de un nivel de severidad específico a un archivo de log personalizado.

1.  **Crear el archivo de log personalizado:**

      * **Comando:** `sudo touch /var/log/custom.log`
      * **Descripción:** Se crea un nuevo archivo llamado `custom.log` en el directorio `/var/log`. Se utiliza `sudo` para asegurar los permisos necesarios.

2.  **Asignar permisos y propiedad al archivo:**

      * **Comando 1:** `sudo chown syslog:syslog /var/log/custom.log`
      * **Descripción:** Con el comando `chown`, se cambia el propietario y el grupo del archivo a `syslog`, lo que permite al servicio `rsyslog` escribir en él.
      * **Comando 2:** `sudo chmod 664 /var/log/custom.log`
      * **Descripción:** Con el comando `chmod`, se establecen los permisos de acceso al archivo: `664` significa que el propietario (`syslog`) y el grupo (`syslog`) tienen permisos de lectura y escritura, mientras que otros usuarios solo tienen permisos de lectura.

3.  **Modificar el archivo de configuración de rsyslog:**

      * **Comando:** `sudo nano /etc/rsyslog.d/50-default.conf`
      * **Descripción:** Se edita el archivo de configuración por defecto de `rsyslog` usando el editor `nano`. Se añade una nueva regla al final del archivo para redirigir los logs de severidad `debug`. La regla tiene la siguiente sintaxis: `<facility>.<severity> <action>`.
      * **Regla a añadir:** `*.debug /var/log/custom.log`
      * **Explicación:** El comodín `*` indica que la regla se aplica a cualquier `facility`. La severidad se establece como `debug`, y la acción es guardar el log en el archivo `/var/log/custom.log`.

4.  **Reiniciar el servicio de rsyslog:**

      * **Comando:** `sudo systemctl restart rsyslog`
      * **Descripción:** Este comando reinicia el servicio `rsyslogd` para que cargue la nueva configuración.

5.  **Simular un evento de debug:**

      * **Comando:** `logger -p local0.debug "This is a debug example"`
      * **Descripción:** Se usa el comando `logger` para simular un evento de log con la `facility` `local0` y la severidad `debug`. Se añade un mensaje de ejemplo.

6.  **Verificar el resultado:**

      * **Comando:** `cat /var/log/custom.log`
      * **Descripción:** Al ejecutar este comando, se puede verificar que la traza del evento de debug simulado se ha escrito correctamente en el archivo `custom.log`, confirmando que la configuración fue exitosa.

#### 3.3. Configuración y Rotación de Logs con `logrotate`

Este procedimiento explica cómo configurar la rotación de logs utilizando la utilidad `logrotate` para prevenir que los archivos crezcan indefinidamente.

1.  **Crear el archivo de configuración de rotación:**

      * **Comando:** `sudo nano /etc/logrotate.d/custom`
      * **Descripción:** Se crea un nuevo archivo de configuración llamado `custom` en el directorio `logrotate.d`. El archivo contendrá las reglas para la rotación del archivo `custom.log`.

2.  **Añadir las reglas de rotación:**

      * **Reglas:**
        ```
        /var/log/custom.log {
            su syslog syslog
            compress
            rotate 1
            create 0644 syslog syslog
        }
        ```
      * **Explicación de las reglas:**
          * `su syslog syslog`: Indica que la rotación se ejecutará con el usuario y grupo `syslog`.
          * `compress`: Comprime los archivos de log antiguos para ahorrar espacio.
          * `rotate 1`: Mantiene solo una copia de seguridad del archivo rotado.
          * `create 0644 syslog syslog`: Crea un nuevo archivo de log vacío con los permisos `0644` y el propietario/grupo `syslog` después de la rotación.

3.  **Verificar la configuración de rotación:**

      * **Comando:** `sudo logrotate -d /etc/logrotate.d/custom`
      * **Descripción:** El parámetro `-d` (`debug`) de `logrotate` permite verificar la sintaxis y el funcionamiento del archivo de configuración sin ejecutar la rotación realmente. La salida mostrará que el archivo ha sido leído y que se ha creado un nuevo estado sin errores.

4.  **Forzar la rotación del log:**

      * **Comando:** `sudo logrotate -f /etc/logrotate.d/custom`
      * **Descripción:** El parámetro `-f` (`force`) fuerza la rotación del log, ignorando las condiciones normales (como la frecuencia o el tamaño).
      * **Verificación:** Después de ejecutar el comando, se puede usar `ls` en el directorio `/var/log` para ver que el archivo `custom.log` original ha sido rotado y comprimido (aparecerá como `custom.log.1.gz`), y que se ha creado un nuevo archivo `custom.log` vacío.

### 4\. Conclusiones y Puntos Clave

  * **Importancia y Beneficios de Seguridad:** El logging es una herramienta fundamental en la administración y seguridad de sistemas GNU/Linux. Una configuración robusta del logging permite la detección temprana de intrusiones, la prevención de ataques y la investigación de incidentes de seguridad, lo que mejora la disponibilidad del sistema y reduce el tiempo de inactividad. Además, es crucial para el cumplimiento de normativas y regulaciones que exigen almacenar registros durante periodos específicos.

  * **Puntos de Aprendizaje Clave:**

      * Se ha aprendido la distinción entre un log (el registro en sí) y el logging (el proceso de crearlo).
      * Se han conocido los diferentes propósitos y la importancia del logging para la monitorización, la detección de errores y el análisis forense.
      * Se ha comprendido la clasificación de logs por tipo y por niveles de severidad, lo que permite priorizar la atención a los problemas más críticos.
      * Se ha familiarizado con los componentes clave de un sistema de logging, como **Syslog**, **Rsyslog** y **Journalctl**.
      * Se ha aprendido a configurar y manipular los archivos de log comunes en distribuciones como Ubuntu, utilizando comandos de terminal para la visualización y filtrado.

  * **Relevancia Técnica:** Los procedimientos aprendidos son de gran relevancia en un entorno profesional. La capacidad de configurar y gestionar logs de manera eficiente y segura es una habilidad esencial para administradores de sistemas y profesionales de la ciberseguridad. La personalización de reglas de logging con `rsyslog` y la automatización de la rotación con `logrotate` son prácticas estándar que garantizan la estabilidad del sistema, el ahorro de espacio y la facilidad de análisis, permitiendo una respuesta rápida y eficaz ante cualquier incidente. El uso de comandos como `journalctl` y la manipulación de archivos con `grep` y `cat` son herramientas indispensables para las tareas de auditoría y análisis diario.