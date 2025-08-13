Documentos de Referencia: "FSL Clase 16 – Linux Capabilities.pdf"

# Informe Técnico: Hardening de Servidores GNU/Linux con Capabilities

## 1. Resumen Ejecutivo
El presente informe técnico detalla los conceptos, procedimientos y buenas prácticas para la configuración de **Linux Capabilities**. Este mecanismo de seguridad, introducido en el kernel de Linux versión 2.2, ofrece una alternativa más segura y granular a los permisos de usuario tradicionales, como los del usuario **root**. El informe explora la definición de las *capabilities*, su interacción con el kernel, sus beneficios, y los procedimientos prácticos para su gestión, incluyendo la obtención, asignación y eliminación de las mismas. Además, se presenta un caso de prueba para ilustrar cómo una configuración incorrecta puede ser explotada para obtener privilegios de superusuario y cómo mitigar dicha vulnerabilidad.

---

## 2. Conceptos Fundamentales

### ¿Qué son las Linux Capabilities?
Las **Linux Capabilities** son un mecanismo de seguridad que permite otorgar permisos específicos y granulares a procesos o ejecutables para realizar tareas que normalmente solo el usuario **root** podría ejecutar. Esto ofrece una alternativa más segura que los permisos tradicionales, ya que un usuario no necesita asumir la identidad completa de **root** para realizar una tarea privilegiada, como ocurre con el comando **sudo**. En su lugar, el usuario solo puede realizar la acción para la que se le concedió el privilegio específico.

### Interacción con el Kernel
Las **capabilities** interactúan directamente con el **kernel** del sistema operativo. Antes de permitir que se realice una operación privilegiada, el kernel verifica las capacidades asignadas a un proceso. Esto ocurre no solo al ejecutar un proceso, sino también antes de interactuar con un archivo.

### Beneficios del uso de Linux Capabilities
* **Mayor Granularidad:** Permite asignar únicamente los permisos necesarios para tareas específicas. Por ejemplo, se puede otorgar permiso de lectura a un archivo sin permitir su modificación o borrado. Esto facilita la implementación del **principio de mínimo privilegio**.
* **Reducción de Riesgos:** Limitar la capacidad de acción de un usuario sobre un recurso disminuye la superficie de ataque.
* **Mayor Seguridad y Confiabilidad:** Ayuda a prevenir la ejecución de código no deseado y la escalada de privilegios.
* **Facilidad de Administración:** Simplifica la labor de asignar permisos a perfiles, roles o grupos de usuarios.

### Tipos de Capabilities
Las **capabilities** pueden aplicarse a nivel de archivos ejecutables y de procesos. Existen cinco tipos principales:
* **Capinh (Inherited)**: Son las capacidades heredadas del proceso padre. Un nuevo proceso adquiere las capacidades de su padre, pero con la restricción de que no puede obtener capacidades que el proceso padre no poseía.
* **CapEff (Effective)**: Representan las capacidades reales y activas que un proceso utiliza en un momento dado.
* **CapPrm (Permitted)**: Establece el conjunto máximo de capacidades que un proceso puede poseer. Funciona como un límite superior para las capacidades que un proceso puede adquirir.
* **CapBnd (Limitations)**: Define un límite para las capacidades que un proceso puede adquirir en cualquier momento de su ciclo de vida. Son útiles para restringir posibles escaladas de privilegios.
* **CapAmb (Environmental)**: Su propósito es conservar ciertas capacidades a través de llamadas al sistema como **execve**, que normalmente reiniciarían las capacidades del proceso.

### Valores Posibles
A cada tipo de **capability** se le pueden asignar tres valores:
* **P (Permitted)**: Habilita la *capability* para que pueda ser efectiva o heredada.
* **E (Effective)**: Aplica la *capability* al proceso.
* **I (Inheritable)**: Permite que la *capability* sea heredada por los subprocesos.

---

## 3. Procedimientos Prácticos

### Búsqueda de Información sobre Capabilities
Para obtener una lista completa de las **Linux Capabilities** disponibles, se pueden usar dos métodos:
1.  **Comando `man`**: Se utiliza el comando `man capabilities` para acceder a la página del manual del sistema. Esta página no solo lista las capacidades, sino que también ofrece una breve descripción de cada una y la versión del kernel de Linux en la que fueron introducidas.
2.  **Archivo del Kernel**: Las definiciones y estructuras de las *capabilities* se encuentran en el archivo de cabecera del kernel **linux/capabilities.h**. Sin embargo, no se recomienda el acceso ni la modificación directa de este archivo por motivos de seguridad, ya que podría causar inestabilidad en el sistema.

### Obtención de Capabilities
Existen varios comandos para ver las **capabilities** asociadas a archivos y procesos:
* **Comando `getcap <file_name>`**: Muestra las capacidades de un archivo ejecutable.
    * **Ejemplo:** `getcap /bin/ping` devuelve `/bin/ping cap_net_raw=ep`, lo que indica que el comando **ping** tiene la capacidad `cap_net_raw` en los conjuntos efectivo y permitido.
* **Comando `sudo getpcaps <process_pid>`**: Se utiliza para obtener las **capabilities** a nivel de un proceso activo.
    * **Ejemplo:** Para el proceso `ping 127.0.0.1` con PID 2996, el comando `sudo getpcaps 2996` devuelve `2996: cap_net_raw=p`, mostrando que la capacidad `cap_net_raw` está permitida para ese proceso.
* **Comando `getcap -r / 2>/dev/null`**: Muestra todas las *capabilities* asociadas a los ejecutables del usuario actual de forma recursiva desde el directorio raíz. Esto es útil para auditorías de seguridad, ya que permite identificar configuraciones erróneas o vulnerabilidades.

### Configuración y Eliminación de Capabilities
* **Asignación de Capabilities:** El comando `setcap` permite asignar *capabilities* a programas específicos.
    * **Sintaxis:** `sudo setcap <capability>=<value> [/path/to/binary]`.
    * **Ejemplo:** Para darle a `nc.openbsd` la capacidad `cap_net_bind_service` para que sea efectiva y permitida, se usa `sudo setcap cap_net_bind_service=ep /bin/nc.openbsd`.
    * **Consideración:** Se debe utilizar la ruta del ejecutable real, no de un enlace simbólico. Esto se puede verificar con el comando `file`.
* **Eliminación de Capabilities:** Para eliminar las capacidades de un ejecutable, se utiliza el comando `setcap` con la opción `-r`.
    * **Sintaxis:** `sudo setcap -r </path/to/binary>`.
    * **Ejemplo:** Para eliminar las capacidades de `nc.openbsd`, se usa `sudo setcap -r /bin/nc.openbsd`.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
Las **Linux Capabilities** son un pilar fundamental en el **hardening** de sistemas, ya que permiten una asignación de privilegios mucho más granular y controlada que los permisos tradicionales. Al limitar los privilegios de los procesos, se reduce significativamente la superficie de ataque y el posible impacto de una vulnerabilidad. Un sistema con *capabilities* bien configuradas se adhiere al **principio de mínimo privilegio**, lo que previene ataques de escalada de privilegios y ayuda a mantener un estado de seguridad consistente y confiable.

### Puntos de Aprendizaje Clave
* **Diferenciación de permisos:** Las **capabilities** son más granulares, específicas y pueden ser temporales, a diferencia de los permisos tradicionales que se basan en identidades de usuario/grupo y tienden a ser permanentes.
* **Gestión:** Se debe realizar una administración cuidadosa de las capacidades asignadas para evitar vulnerabilidades.
* **Auditoría:** La monitorización y auditoría regular de las asignaciones de *capabilities* es crucial para detectar errores de configuración y vulnerabilidades.
* **Ejemplos prácticos:** Se demostró cómo comandos como **ping** y **netcat** utilizan `capabilities` específicas (`cap_net_raw` y `cap_net_bind_service`) para realizar sus funciones.
* **Riesgo de mala configuración:** Una configuración errónea, como la asignación de `CAP_SETUID` a un ejecutable como **vim**, puede ser explotada para obtener una *shell* de **root**, evidenciando la importancia de una gestión adecuada.
* **Relevancia Técnica:** El conocimiento y la aplicación de las **Linux Capabilities** son esenciales para cualquier profesional de la ciberseguridad y la administración de sistemas. La capacidad de auditar (`getcap`, `getpcaps`) y configurar (`setcap`) estas capacidades permite no solo asegurar el sistema de manera proactiva, sino también mitigar fallos de seguridad una vez detectados. La prueba de concepto mostró cómo un error de configuración simple puede llevar a una escalada de privilegios, subrayando la necesidad de una revisión periódica y una gestión rigurosa de estos permisos. Además de los comandos de línea, herramientas como **Libcap** y **PolicyKit** demuestran la integración de las **capabilities** en el desarrollo y la gestión de permisos a mayor escala en entornos profesionales.