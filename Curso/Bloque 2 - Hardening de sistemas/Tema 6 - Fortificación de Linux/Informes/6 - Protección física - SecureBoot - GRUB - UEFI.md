Documentos de Referencia: "FSL Clase 02 – Protección física.pdf"

### Documentos de Referencia: "FSL Clase 02 – Protección física.pdf"

# Informe Técnico: Protección Física en Linux

### 1. Resumen Ejecutivo

Este informe detalla los aspectos clave de la protección física de sistemas, con un enfoque particular en entornos Linux. Se abordan los riesgos asociados con el acceso físico no autorizado a un equipo y se describen las medidas de seguridad esenciales para mitigar dichos riesgos. Los temas principales incluyen la protección a nivel de BIOS/UEFI, la gestión de gestores de arranque como GRUB, el cifrado de archivos y particiones, y la seguridad física del hardware. Se exploran las vulnerabilidades que permiten ataques "offline" y se presentan las estrategias para proteger los sistemas contra estas amenazas, proporcionando una base sólida para la implementación de defensas robustas.

### 2. Conceptos Fundamentales

* **Protección Física (Physical Protect):** Se refiere a las medidas de seguridad para proteger un sistema de ataques que requieren acceso físico al hardware. Un sistema sin protección física puede ser vulnerable a un atacante que manipula el equipo directamente. El acceso físico permite a un atacante realizar diversas acciones, como arrancar un sistema operativo desde una unidad externa, si tiene acceso a la BIOS para cambiar el orden de arranque.
* **Ataques Offline:** Este tipo de ataque se produce cuando el atacante no utiliza el sistema operativo instalado en la máquina, sino que arranca con otro sistema operativo cargado en memoria, a menudo desde una unidad USB o un DVD. El acceso offline permite la manipulación del sistema de archivos. Si las particiones o el disco duro no están cifrados, los datos del sistema pueden ser vulnerables a este tipo de acceso.
* **BIOS (Basic Input/Output System):** Es un firmware legacy que ha sido ampliamente utilizado en computadoras durante décadas. Proporciona una interfaz básica para configurar y controlar el hardware de la computadora, incluyendo la configuración del sistema y la secuencia de arranque. Sin embargo, tiene limitaciones en cuanto a la compatibilidad con dispositivos modernos, la capacidad de almacenamiento de datos de arranque y la seguridad.
* **UEFI (Unified Extensible Firmware Interface):** Es una tecnología más reciente diseñada para reemplazar a la BIOS. Ofrece una interfaz más avanzada y extensible para la inicialización del hardware y el arranque del sistema operativo. Soporta características modernas como discos duros de más de 2 TB, Secure Boot y particiones GUID (GPT). Además, proporciona una interfaz más segura y evolucionada en comparación con la BIOS.
* **Secure Boot:** Es una característica de seguridad que garantiza que solo se cargue software de confianza y firmado digitalmente durante el proceso de arranque del sistema operativo. Esto ayuda a prevenir la carga de software malicioso o no autorizado durante el inicio del sistema. Secure Boot funciona verificando la integridad y la firma digital de los componentes de software de arranque y, si alguno no puede ser validado, se evita que el sistema operativo se inicie.
* **GRUB (Grand Unified Bootloader):** Es un gestor de arranque múltiple desarrollado por GNU, utilizado principalmente en sistemas GNU/Linux. Su función es gestionar el arranque del sistema operativo y sus componentes necesarios. Por defecto, GRUB es editable y no tiene protección, lo que lo convierte en una pieza crítica a proteger. La modificación de GRUB puede permitir que un atacante inicie una shell de root con acceso completo al sistema.

### 3. Procedimientos Prácticos

El documento describe un procedimiento para realizar un ataque offline a través de la modificación de GRUB y las medidas para protegerse de él.

#### Ataque Offline mediante GRUB

El ataque aprovecha la capacidad de edición de GRUB por defecto para obtener acceso privilegiado al sistema. El procedimiento es el siguiente:
1.  Al iniciar el sistema y aparecer la pantalla de GRUB, el atacante presiona la tecla `e` para entrar en el modo de edición de GRUB, como se indica en la captura de pantalla de la página 8.
2.  Dentro del editor de GRUB, el atacante localiza la línea que carga la imagen del kernel, que suele contener parámetros como `ro quiet splash $vt_handoff`.
3.  El atacante sustituye o modifica estos parámetros para inicializar una terminal de `bash` en lugar del sistema operativo normal. Un ejemplo de la línea modificada es `quiet splash rw init=/bin/bash`.
4.  Después de modificar la línea, el atacante presiona `f10` para arrancar el sistema con las nuevas instrucciones.
5.  El sistema no arranca el sistema operativo, sino que inicia directamente un terminal de bash con permisos de root, lo que permite al atacante tener acceso completo al sistema y modificar o extraer información, como el fichero `shadow`. El ataque se considera offline porque el sistema operativo residente no ha sido arrancado.

#### Protección contra Ataques a GRUB

Para proteger GRUB de este tipo de ataques, se deben tomar las siguientes medidas:
* **Establecer una contraseña:** Se debe configurar una contraseña para GRUB para que no se pueda editar sin las credenciales. Esto se puede lograr editando el archivo `grub.cfg` o usando una utilidad como `grub2-mkpasswd-pbkdf2`.
* **Restringir el acceso al archivo de configuración:** Es crucial asegurar que solo los usuarios autorizados tengan permisos para modificar el archivo de configuración de GRUB.
* **Utilizar Secure Boot:** Secure Boot ayuda a prevenir la carga de componentes de software no firmados o potencialmente maliciosos. Aunque no es una protección directa para la edición de GRUB, complementa la seguridad del proceso de arranque.

### 4. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

La protección física es un pilar fundamental de la ciberseguridad. Un sistema sin esta protección es inherentemente vulnerable a manipulaciones que pueden eludir las defensas de software tradicionales. Al implementar medidas de seguridad como contraseñas en la BIOS/UEFI, la protección de GRUB y el cifrado del sistema de archivos, se crea una defensa en profundidad que dificulta significativamente los ataques offline. El cifrado de particiones y archivos añade una segunda capa de protección, asegurando que incluso si el atacante logra romper la primera capa de cifrado, aún tendría que superar una segunda para acceder a los datos sensibles.

#### Puntos de Aprendizaje Clave

* La protección física es tan importante como la protección lógica.
* Los ataques offline son una amenaza seria que puede ser ejecutada con acceso físico a un equipo.
* La BIOS y UEFI son componentes críticos que deben ser protegidos con contraseña para controlar el orden de arranque.
* GRUB, como gestor de arranque, es un punto de vulnerabilidad si no se protege, ya que permite la edición para arrancar el sistema en modo privilegiado.
* El cifrado a nivel de partición y a nivel de archivo son medidas esenciales para proteger los datos de un sistema.
* La seguridad física del hardware, como el uso de candados, es importante para evitar la manipulación interna del equipo.
* Secure Boot es una característica de UEFI que mejora la seguridad al garantizar que solo se ejecute software firmado digitalmente.

#### Relevancia Técnica

La comprensión de estos procedimientos es vital para cualquier profesional de la seguridad. Saber cómo se realiza un ataque a través de GRUB permite implementar las defensas adecuadas y robustas para proteger los sistemas de manera proactiva. La capacidad de configurar correctamente las opciones de seguridad en la BIOS/UEFI, establecer contraseñas en GRUB y utilizar cifrado de disco son habilidades técnicas cruciales para mantener la integridad y confidencialidad de los datos en un entorno profesional.

---

# Informe Técnico: Protección física en Linux y el ataque offline a GRUB

## 1. Resumen Ejecutivo
El presente informe técnico detalla el concepto de ataque offline y su aplicación práctica, específicamente en el gestor de arranque GRUB de sistemas Linux. Se explora cómo un atacante con acceso físico a un dispositivo puede manipular el sistema operativo para obtener acceso total, incluso sin conexión a una red. Se revisan las protecciones existentes y se presenta un ejemplo práctico de cómo explotar una vulnerabilidad en GRUB para obtener una *shell* de *root*. Finalmente, se discuten las consecuencias de este tipo de ataque y se mencionan las medidas de protección necesarias para mitigar estos riesgos.

## 2. Conceptos Fundamentales
* **Ataque Offline (Offline Attack):** Un ataque offline se produce cuando un atacante, con acceso físico a una máquina, manipula o accede a los datos del sistema sin necesidad de una conexión a la red o acceso remoto. Esto permite modificar archivos del sistema operativo, cambiar configuraciones y acceder a datos sensibles.
* **GRUB (Grand Unified Bootloader):** Es el gestor de arranque de un sistema operativo Linux. Permite elegir qué sistema operativo arrancar si hay varios instalados y ofrece opciones avanzadas. Por defecto, GRUB no es seguro.
* **Protecciones Físicas:** Son medidas de seguridad esenciales para prevenir ataques offline. Incluyen:
    * Establecer una contraseña en la BIOS.
    * Cambiar el orden de arranque para que el equipo siempre intente iniciar desde el disco duro interno.
    * Cifrar particiones o carpetas, utilizando diferentes niveles de cifrado.

## 3. Procedimientos Prácticos: Ejemplo de ataque offline a GRUB
El documento describe un ataque offline a un sistema Ubuntu 20.04 que utiliza GRUB versión 2.04. El procedimiento detallado para obtener acceso de *root* es el siguiente:

1.  **Inicio del sistema:** Al arrancar el sistema, el menú de GRUB se muestra en pantalla. Se puede ver una lista de opciones para iniciar el sistema operativo, ejecutar pruebas de memoria, entre otras.
2.  **Edición del menú de arranque:** En el menú de GRUB, se selecciona la opción de Ubuntu y se presiona la tecla 'e' para editar los comandos de arranque. Esto abre un editor de texto rudimentario con los parámetros de arranque del sistema.
3.  **Modificación de parámetros:** Dentro del editor, el atacante localiza la línea que contiene los parámetros de arranque del núcleo de Linux, que suele incluir la frase `"ro quiet splash $vt_handoff"`.
4.  **Inyección de comandos:** Se reemplaza el parámetro `"ro quiet splash $vt_handoff"` por `"rw init=/bin/bash"`.
    * `rw`: Monta el sistema de archivos de *root* en modo de lectura y escritura.
    * `init=/bin/bash`: Indica al núcleo que, en lugar de iniciar el proceso estándar de *init* (el primer proceso del sistema), debe ejecutar directamente el programa `/bin/bash` como el proceso principal. Esto concede una *shell* con privilegios de *root*.
5.  **Ejecución de la *shell*:** Después de la modificación, se presiona la combinación de teclas `Ctrl+x` o la tecla `F10` para arrancar el sistema con los nuevos parámetros.
6.  **Verificación del acceso:** El sistema arranca directamente en una *shell* de *root*. Para verificar que se tienen los privilegios de *root*, se puede ejecutar el comando `id`. La salida `uid=0(root) gid=0(root) groups=0(root)` confirma que el atacante tiene acceso total al sistema operativo, al sistema de archivos y a cualquier configuración.

## 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** Un ataque offline a GRUB es "demasiado sencillo y rápido". Permite que un atacante con acceso físico obtenga una *shell* de *root* en segundos. Una vez dentro, el atacante puede realizar una gran cantidad de acciones, como ver y modificar el archivo `/etc/shadow`, crear nuevos usuarios con permisos de *root*, manipular la configuración de servicios como SSH, o borrar registros de actividad (*logs*). Proteger el gestor de arranque es crucial para evitar que la información no cifrada quede expuesta.
* **Puntos de Aprendizaje Clave:**
    * Los ataques offline son una amenaza real, especialmente para dispositivos portátiles.
    * El gestor de arranque GRUB en Linux no es seguro por defecto y debe protegerse para evitar la manipulación.
    * La protección del GRUB puede incluir la configuración de usuarios y contraseñas para editar las entradas, lo que previene que cualquier persona sin autorización pueda realizar cambios.
    * La información en movimiento, como la que se encuentra en los portátiles de empleados, es especialmente vulnerable si el dispositivo es robado o perdido.
* **Relevancia Técnica:** La vulnerabilidad demostrada subraya la necesidad de implementar múltiples capas de seguridad. En un entorno profesional, la protección del gestor de arranque y el uso de cifrado en disco completo son medidas de seguridad fundamentales. Estas protecciones son vitales para cualquier equipo que pueda ser manipulado físicamente, ya sea un servidor o un equipo cliente. El documento concluye que es necesario proteger las herramientas por defecto y fortificar el sistema para mitigar este tipo de ataques. En sesiones posteriores se abordarán las formas de proteger GRUB.

---

Documentos de Referencia: "FSL Clase 02 – Protección física (1).pdf"

# Informe Técnico: Protección física en Linux y la seguridad de GRUB

## 1. Resumen Ejecutivo
Este informe detalla las técnicas para proteger el gestor de arranque GRUB en sistemas Linux. Se enfoca en cómo prevenir un ataque offline mediante la implementación de usuarios y contraseñas. El documento explica la estructura de configuración de GRUB 2 y guía a través de un procedimiento práctico para crear un **superuser** que pueda editar las entradas de arranque, así como la generación de una contraseña con *hash*. Se discuten las implicaciones de estas protecciones y se enfatiza la importancia de asegurar el acceso físico para evitar la manipulación del sistema.

## 2. Conceptos Fundamentales
* **GRUB 2:** Es la versión del gestor de arranque de Linux más ampliamente utilizada. Ofrece una gran **flexibilidad** para la configuración y permite la creación de **usuarios y contraseñas** específicos para el gestor de arranque, distintos de los usuarios del sistema operativo.
* **Archivos de Configuración de GRUB:** Los *scripts* que generan las entradas de GRUB se encuentran en el directorio `/etc/grub.d`. Específicamente, el archivo `/etc/grub.d/40_custom` es el lugar designado para crear los usuarios y contraseñas que se utilizarán para la protección de GRUB.
* **Superuser de GRUB:** Un **superuser** es un rol especial de usuario dentro de GRUB. Un usuario con este rol tiene la capacidad de editar la configuración de arranque y seleccionar cualquier sistema operativo presente en el gestor.
* **Generación de Contraseñas:** Las contraseñas para los usuarios de GRUB se pueden generar utilizando el comando `grub-mkpasswd-pbkdf2`, que produce un *hash* seguro de la contraseña. Aunque es posible usar contraseñas en texto plano, esto no se considera una buena práctica ya que el archivo de configuración es legible por otros usuarios del sistema.

## 3. Procedimientos Prácticos
El proceso para proteger GRUB implica la configuración de un **superuser** y su contraseña. A continuación se detallan los pasos:

1.  **Acceso al Directorio de Configuración:** Abrir una terminal y navegar al directorio `/etc/grub.d` usando el comando `cd /etc/grub.d/`.

2.  **Edición del Archivo de Configuración:** Utilizar un editor de texto con privilegios de administrador para abrir el archivo `40_custom`. Esto se hace con el comando `sudo nano 40_custom`.

3.  **Declaración del Superuser:** Dentro del archivo `40_custom`, en la parte superior, se declara el **superuser** con la sintaxis `set superusers="<usuario>"`. Se pueden listar varios usuarios si es necesario.

4.  **Generación de la Contraseña:** Abrir una segunda terminal y ejecutar el comando `grub-mkpasswd-pbkdf2` para generar el *hash* de la contraseña deseada. Se solicita la contraseña dos veces y el comando devuelve el *hash* correspondiente.

5.  **Adición de la Contraseña al Archivo de Configuración:** Copiar el *hash* generado y agregarlo al archivo `40_custom` bajo la declaración de `superusers`. El formato es `password_pbkdf2 <usuario> <hash>`. El documento advierte que no es seguro usar contraseñas en texto plano como `password luis 1234`.

6.  **Actualización de GRUB:** Después de guardar y cerrar el archivo de configuración, se debe actualizar GRUB para que los cambios surtan efecto. Esto se realiza con el comando `sudo update-grub2`. El comando generará un nuevo archivo de configuración de GRUB, incorporando los usuarios y contraseñas definidos.

7.  **Verificación de la Protección:** Reiniciar la máquina. Al intentar editar las opciones de arranque en el menú de GRUB con la tecla 'e', el sistema pedirá un nombre de usuario y una contraseña. Solo al introducir las credenciales correctas del **superuser** se permitirá la edición. Si las credenciales son incorrectas, el sistema no permitirá la edición y volverá al menú principal de GRUB.

También es posible proteger entradas individuales del menú de arranque utilizando el parámetro `--users` en los *scripts* de GRUB como `10_linux`.

## 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** La protección de GRUB es fundamental para la **seguridad física** de un sistema Linux. Con acceso físico, un atacante puede manipular fácilmente el gestor de arranque para obtener acceso total, como se vio en un ataque offline anterior. La implementación de un **superuser** y una contraseña evita que cualquier persona pueda editar el arranque del sistema, protegiendo así la información sensible incluso cuando la máquina está apagada.
* **Puntos de Aprendizaje Clave:**
    * GRUB 2 permite una gestión de usuarios y contraseñas específica y distinta de la del sistema operativo.
    * El archivo `/etc/grub.d/40_custom` es el lugar recomendado para definir los usuarios y contraseñas de GRUB.
    * El comando `grub-mkpasswd-pbkdf2` debe usarse para generar contraseñas seguras con *hash* en lugar de almacenarlas en texto plano.
    * El comando `sudo update-grub2` debe ejecutarse para aplicar los cambios de configuración.
* **Relevancia Técnica:** Proteger el gestor de arranque es una capa de seguridad crítica, especialmente para servidores que se reinician o equipos que están en tránsito. Un atacante con acceso físico ya no podrá explotar una vulnerabilidad en GRUB, lo que refuerza la seguridad del sistema contra ataques offline. Aunque se pueden crear usuarios para restringir el arranque de sistemas operativos específicos, la práctica más común es proteger la edición del GRUB.