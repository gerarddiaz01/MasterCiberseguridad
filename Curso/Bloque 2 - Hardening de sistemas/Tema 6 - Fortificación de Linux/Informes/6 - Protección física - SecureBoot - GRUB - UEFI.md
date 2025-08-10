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