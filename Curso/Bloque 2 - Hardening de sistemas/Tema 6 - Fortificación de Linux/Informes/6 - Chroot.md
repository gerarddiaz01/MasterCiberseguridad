Documentos de Referencia: "FSL Clase 05 – Chroot.pdf"

# Informe Técnico: Hardening de servidores GNU/Linux con jaulas Chroot

## 1. Resumen Ejecutivo
Este informe técnico aborda el tema de las **jaulas Chroot** como una técnica de seguridad para sistemas GNU/Linux. Se introduce el concepto de "sandbox" o caja de arena como analogía para entender el aislamiento de procesos. El informe detalla cómo las jaulas Chroot modifican el directorio raíz de un proceso, limitándolo a un entorno virtual específico. Se exploran casos de uso comunes, como la ejecución de software no confiable y el testeo de aplicaciones. Finalmente, se presenta una prueba de concepto práctica en un sistema Ubuntu, ilustrando la creación y configuración de una jaula, así como la verificación de su correcto aislamiento.

---

## 2. Conceptos Fundamentales
* **Jaulas Chroot (Chroot Jails):** Una técnica de aislamiento utilizada en sistemas GNU/Linux. Proporciona un entorno virtual y limitado para la ejecución de un proceso. El concepto se asemeja a una "sandbox".
* **Cambio de Raíz (Chroot):** La palabra **chroot** es la abreviación de "change root". Su función principal es modificar la raíz del sistema de archivos de un proceso para que apunte a un nuevo directorio específico. Esto limita al proceso a interactuar únicamente con los archivos, herramientas y aplicaciones que se definan dentro de ese nuevo directorio, aislándolo del resto del sistema.
* **Comando `chroot`:** Es la llamada al sistema que permite realizar la operación de cambio de raíz. Generalmente viene preinstalado en la mayoría de las distribuciones de Linux, como Ubuntu. Su parámetro principal es el nuevo directorio que servirá como la raíz del sistema.

* **Casos de uso y beneficios:**
    * **Seguridad:** Aumenta la seguridad del sistema al confinar los procesos, lo que dificulta la escalada de privilegios y protege contra intrusiones y *malware*.
    * **Software no confiable:** Permite ejecutar software de fuentes desconocidas o potencialmente malicioso en un entorno seguro y aislado para analizar su comportamiento.
    * **Testeo de software:** Facilita la creación de entornos de prueba para testear código nuevo, actualizaciones, librerías o dependencias sin afectar al sistema principal.
    * **Servidores web:** Es útil para la implementación de servidores web y aplicaciones, garantizando un entorno más seguro y controlado.

* **Limitaciones:**
    * Las jaulas Chroot no son una solución de seguridad infalible.
    * No protegen contra todos los tipos de ataques; por ejemplo, no son eficaces contra ataques de tipo *kernel*.
    * Un atacante que logre modificar permisos o instalar software vulnerable dentro de la jaula podría explotar una vulnerabilidad para salir de ella.
    * Nunca deben ser la única medida de seguridad; deben combinarse con otras prácticas como una correcta configuración de permisos y actualizaciones de seguridad.

---

## 3. Procedimientos Prácticos
El documento describe una prueba de concepto (*Proof of Concept*, PoC) para crear una jaula Chroot en una máquina virtual Ubuntu. El objetivo es configurar un entorno aislado para ejecutar un *shell* de Bash y verificar que el aislamiento funciona correctamente.

### 3.1. Preparación del Entorno
1.  **Creación del directorio de la jaula:** Se crea un nuevo directorio que servirá como la nueva raíz del sistema. Se utiliza el comando `mkdir /var/chroot` para crear un directorio llamado `chroot` dentro de `/var`.
2.  **Identificación del usuario y grupo:** Se crea un usuario llamado `jailuser` para la prueba. Para su uso posterior, es necesario conocer su ID de usuario (UID) y su ID de grupo (GUID). Esto se obtiene ejecutando el comando `cat /etc/passwd | grep jailuser`, que filtra el archivo de usuarios del sistema y muestra la línea correspondiente al usuario creado. El resultado `jailuser:x:1002:1002::/home/jattuser:/bin/sh` revela que el UID y GUID son **1002**.

### 3.2. Configuración de la Jaula Chroot
1.  **Intento de ejecución inicial:** Se navega al directorio recién creado (`cd /var/chroot/`) y se intenta ejecutar la jaula con el comando `chroot ./`. El comando falla con un error "No such file or directory". Esto ocurre porque el directorio está vacío y el sistema no encuentra el *shell* de Bash que se supone que debe ejecutar.
2.  **Identificación de dependencias:** Para que el *shell* de Bash funcione, se deben copiar los archivos binarios y sus dependencias necesarias en la jaula. Para listar las dependencias de `/bin/bash`, se usa el comando `ldd /bin/bash`. Las dependencias identificadas son `libtinfo.so.6`, `libc.so.6` y `ld-linux-x86-64.so.2`.
3.  **Creación de la estructura de directorios:** Es necesario replicar la estructura de directorios original dentro de la jaula para alojar los archivos binarios y sus dependencias. Se usan los comandos `mkdir bin`, `mkdir -p lib/x86_64-linux-gnu` y `mkdir -p lib64` para crear los directorios `bin`, `lib/x86_64-linux-gnu` y `lib64` dentro de `/var/chroot`.
4.  **Copia de archivos:** Se copian los archivos binarios y sus dependencias a los directorios recién creados. Los comandos utilizados son:
    * `cp /bin/bash /var/chroot/bin`
    * `cp /lib/x86_64-linux-gnu/libtinfo.so.6 /var/chroot/lib/x86_64-linux-gnu`
    * `cp /lib/x86_64-linux-gnu/libc.so.6 /var/chroot/lib/x86_64-linux-gnu`
    * `cp /lib64/ld-linux-x86-64.so.2 /var/chroot/lib64`

### 3.3. Verificación del Aislamiento
1.  **Ejecución de la jaula con usuario específico:** Se ejecuta nuevamente la jaula, pero esta vez especificando el usuario y el directorio con el comando `chroot --userspec=1002:1002 /var/chroot/`. Esto inicia un *shell* de Bash dentro del entorno aislado.
2.  **Prueba de comandos:** Para verificar el aislamiento, se intenta ejecutar un comando que no fue copiado a la jaula. Al ejecutar `whoami`, la terminal devuelve el error "`bash: whoami: command not found`". Esto demuestra que la jaula está funcionando correctamente y limitando el acceso a los recursos del sistema principal.
3.  **Segunda prueba de verificación:** Se copian el binario de `whoami` y sus dependencias al directorio de la jaula. Sin embargo, al ejecutar `whoami` dentro de la jaula, el comando falla con el error "`whoami: cannot find name for user ID 1002: No such file or directory`". Este error confirma el aislamiento, ya que el *shell* de Bash no tiene acceso al archivo `/etc/passwd` del sistema principal para resolver el nombre del usuario.

---

## 4. Conclusiones y Puntos Clave
* **Importancia y Beneficios de Seguridad:** Las jaulas Chroot son una herramienta de seguridad poderosa para los sistemas GNU/Linux, ya que proporcionan flexibilidad y eficiencia en la administración del sistema. Su principal beneficio es el **aislamiento de procesos**, lo que dificulta la escalada de privilegios y protege contra *malware* e intrusiones. Al confinar un proceso a un entorno limitado, se reduce el riesgo de daños mayores al resto del sistema.

* **Puntos de Aprendizaje Clave:**
    * Una jaula Chroot debe configurarse manualmente, replicando la estructura de directorios y copiando todos los archivos binarios y sus dependencias (`ldd`) necesarios para el funcionamiento del proceso dentro del entorno aislado.
    * El aislamiento se evidencia cuando un comando que existe en el sistema principal no funciona dentro de la jaula, ya sea porque el binario o sus dependencias no están presentes, o porque carece de acceso a archivos del sistema como `/etc/passwd`.
    * El comando `chroot` no es una solución de seguridad infalible y debe usarse de manera responsable, en combinación con otras medidas de seguridad, como una correcta configuración de permisos y actualizaciones.

* **Relevancia Técnica:** La capacidad de crear entornos aislados es fundamental en el *hardening* de servidores, especialmente para ejecutar servicios web o aplicaciones críticas. Permite a los administradores de sistemas GNU/Linux probar software, nuevas configuraciones y dependencias de forma segura, minimizando el impacto de posibles fallos o vulnerabilidades. El conocimiento de cómo funciona `chroot` y sus dependencias es una habilidad técnica esencial para garantizar un aislamiento efectivo y proteger los sistemas contra ataques.