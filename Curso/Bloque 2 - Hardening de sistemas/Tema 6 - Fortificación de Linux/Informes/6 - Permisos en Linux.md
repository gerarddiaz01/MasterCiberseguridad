Documentos de Referencia: "FSL Clase 18 – Permisos en Linux.pdf"

# Informe Técnico: Gestión de Permisos en GNU/Linux

## 1. Resumen Ejecutivo
El presente informe técnico abarca la gestión de permisos en sistemas operativos GNU/Linux, un elemento crucial para la seguridad y el correcto funcionamiento del sistema. Se analizan los conceptos de permisos básicos y avanzados, incluyendo la identificación de usuarios (propietario, grupo y otros), los permisos fundamentales de lectura, escritura y ejecución, y su representación en la terminal. El informe también detalla los permisos especiales (setuid, setgid y sticky) y los atributos de archivos (append e inmutable), explicando cómo se visualizan, modifican y aplican. A través de ejercicios prácticos, se demuestra la importancia de estos permisos para proteger información, prevenir la corrupción de archivos y evitar la ejecución de código malicioso.

---

## 2. Conceptos Fundamentales

### ¿Qué son los Permisos en GNU/Linux?
Los permisos en GNU/Linux son un conjunto de reglas que definen qué usuarios o grupos de usuarios pueden acceder a un archivo o directorio y qué acciones (leer, escribir, ejecutar) pueden realizar sobre ellos. Estos permisos son esenciales para garantizar la seguridad del sistema y la privacidad de los usuarios. Una gestión adecuada de los permisos busca proteger la información confidencial, evitar la corrupción de archivos, prevenir la ejecución de código malicioso y asegurar el correcto funcionamiento del sistema.

### Identificación de Usuarios
En relación con los permisos, se identifican tres tipos de usuarios que pueden interactuar con un archivo, directorio o recurso:
* **Propietario (Owner):** El usuario que creó el recurso.
* **Grupo (Group):** Un grupo de usuarios que comparten permisos sobre el recurso.
* **Otros (Others):** El resto de usuarios del sistema que no son el propietario ni miembros del grupo.

### Permisos Básicos
Existen tres permisos básicos en los sistemas GNU/Linux, representados por las letras **r**, **w** y **x**:
* **Lectura (r):** Permite leer el contenido de un archivo o directorio.
* **Escritura (w):** Permite modificar el contenido de un archivo o directorio.
* **Ejecución (x):** Permite ejecutar un archivo como un programa.

### Permisos Especiales
Son permisos adicionales que otorgan a archivos o directorios capacidades que no están disponibles para usuarios normales. Al visualizarlos con `ls -al`, se utiliza la tercera posición de cada tríada de permisos, que normalmente corresponde al permiso de ejecución (x). Se distinguen por una letra mayúscula o minúscula en esa posición:
* **setuid (s):** Permite que un archivo se ejecute con los permisos del usuario propietario, independientemente de quién lo ejecute. Se representa con una **s** minúscula si el permiso de ejecución también está activo, o una **S** mayúscula si no lo está.
* **setgid (s):** Similar a setuid, pero aplica a los grupos de usuarios. Permite que el archivo se ejecute con los permisos del grupo propietario.
* **sticky (t):** Este permiso hace que solo el propietario del archivo o el usuario root puedan eliminar o renombrar archivos dentro de un directorio. Es especialmente útil en directorios con permisos `777` (acceso total).

### Atributos Avanzados
Los atributos son características adicionales que se pueden asignar a los archivos para mejorar su seguridad e integridad. Se visualizan con el comando `lsattr` y se modifican con `chattr`. Dos atributos clave son:
* **append (a):** Permite que se añadan datos a un archivo solo al final, sin permitir la modificación o eliminación del contenido existente. Es útil para archivos de registro o colaboración.
* **inmutable (i):** Bloquea cualquier tipo de modificación, eliminación o cambio de nombre del archivo. Ni siquiera el usuario root puede alterar el archivo mientras este atributo esté activo. Es ideal para proteger archivos críticos del sistema.

---

## 3. Procedimientos Prácticos

### Visualización de Permisos con `ls -al`
El comando `ls -al <fichero>` se utiliza para ver la información detallada de los permisos de un archivo o directorio. La salida muestra una cadena de diez caracteres que se lee de la siguiente manera:
1.  **Tipo de Recurso:** El primer carácter indica el tipo de recurso. Un guion (`-`) representa un archivo, mientras que una `d` representa un directorio.
2.  **Máscara de Permisos:** Los siguientes nueve caracteres se organizan en tres tríadas, una para cada tipo de usuario: propietario, grupo y otros. Cada tríada contiene los permisos de lectura (`r`), escritura (`w`) y ejecución (`x`) para ese grupo de usuarios.
3.  **Propietario y Grupo:** A continuación, se muestran el nombre del usuario propietario y el grupo al que pertenece.
4.  **Tamaño y Fecha:** Siguen el tamaño del archivo y la última fecha de modificación.
5.  **Nombre:** Finalmente, se muestra el nombre del archivo o directorio.
    * **Ejemplo:** `ls -al /etc/passwd` muestra `-rw-r--r-- 1 root root ... /etc/passwd`. Esto significa que el propietario (`root`) tiene permisos de lectura y escritura (`rw-`), mientras que el grupo (`root`) y otros usuarios tienen solo permiso de lectura (`r--`).

### Modificación de Permisos con `chmod`
El comando `chmod` se usa para modificar los permisos de un archivo o directorio. Una de las formas de hacerlo es a través de su representación octal, que se calcula sumando valores numéricos: `r=4`, `w=2`, `x=1`. La suma de los valores de una tríada da un dígito octal (por ejemplo, `rwx` = `4+2+1=7`).
* **Ejemplo:** Para otorgar a `example.txt` permisos de lectura, escritura y ejecución para todos, se usa `chmod 777 example.txt`. La máscara `777` se desglosa en `rwx` para el propietario, `rwx` para el grupo y `rwx` para otros usuarios.

### Gestión de Permisos Especiales
Se pueden modificar los permisos especiales de un archivo usando `chmod` con una notación simbólica.
* **Añadir setuid:** Para añadir el permiso `setuid` a un ejecutable como `/usr/bin/id`, se usa `sudo chmod u+s /usr/bin/id`. Tras la ejecución del comando, el `ls -al` mostrará una `s` en la tercera posición de la primera tríada (`-rwsr-xr-x...`). Al ejecutar el comando `id` con un usuario regular, se puede observar un cambio en el `euid`, que pasa a ser `root`.
* **Eliminar setuid:** Para revertir el cambio, se usa `sudo chmod u-s /usr/bin/id`. Esto elimina el permiso especial y devuelve el ejecutable a su comportamiento original.

### Gestión de Atributos
Los atributos de archivos se gestionan con los comandos `lsattr` y `chattr`.
* **Añadir el atributo append:** En el ejercicio 1, se crea el archivo `exercise.txt` y se le otorgan permisos completos (`777`). Al intentar sobrescribir su contenido con `echo "1234" > exercise.txt`, se logra exitosamente. Sin embargo, al añadir el atributo `append` con `sudo chattr +a exercise.txt`, la misma operación de sobrescritura falla, mostrando el error "Operation not permitted". Con este atributo, solo es posible añadir contenido al final del archivo usando `echo "abc" >> exercise.txt`.
* **Añadir el atributo inmutable:** En el ejercicio 2, se añade el atributo `inmutable` al mismo archivo con `sudo chattr +i exercise.txt`. Al intentar eliminar el archivo con el comando `rm`, tanto el usuario actual como el usuario `root` reciben el error "Operation not permitted". Para poder eliminar el archivo, primero se debe quitar el atributo `inmutable` con `sudo chattr -i exercise.txt`.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La correcta gestión de permisos y atributos en GNU/Linux es fundamental para la seguridad del sistema. Permite a los administradores controlar el acceso a la información confidencial y proteger la integridad de los archivos contra la corrupción o la alteración maliciosa. La granularidad de los permisos, junto con los permisos especiales y los atributos, permite implementar una estrategia de defensa profunda, limitando la capacidad de los usuarios para realizar operaciones no autorizadas, incluso si poseen privilegios de superusuario en otros contextos. El control preciso sobre quién puede leer, escribir o ejecutar un archivo es la primera línea de defensa contra ataques de escalada de privilegios y la manipulación del sistema.

### Puntos de Aprendizaje Clave
* **Conocimiento de Usuarios y Permisos:** Es vital diferenciar entre el propietario, el grupo y otros usuarios, y comprender los permisos básicos (`r`, `w`, `x`) que se les pueden otorgar.
* **Dominio de Comandos:** El uso correcto de `ls -al` para visualizar permisos y `chmod` para modificarlos es una habilidad esencial para la administración del sistema.
* **Representación Octal:** Comprender cómo se traduce la máscara de permisos a un valor octal (`r=4, w=2, x=1`) es crucial para la configuración rápida y eficiente de permisos con `chmod`.
* **Permisos Especiales y Atributos:** La existencia de permisos avanzados como `setuid`, `setgid`, `sticky` y atributos como `append` e `inmutable` proporciona un nivel de control de seguridad superior al de los permisos básicos, permitiendo alterar el comportamiento de los archivos incluso para el usuario `root`.

### Relevancia Técnica
El conocimiento detallado de los permisos y atributos de archivos es indispensable para la fortificación de servidores GNU/Linux. Los procedimientos aprendidos, como la auditoría de permisos (`ls -al`), la modificación con `chmod` y la gestión de atributos con `chattr`, son tareas rutinarias para los profesionales de la seguridad y los administradores de sistemas. La capacidad de detectar configuraciones de permisos débiles o maliciosas y de aplicar permisos y atributos avanzados para proteger archivos críticos son habilidades técnicas que contribuyen directamente a la integridad y seguridad de la infraestructura de TI. La resolución de los ejercicios prácticos demostró la importancia de estos conceptos en un entorno real, confirmando que una configuración adecuada puede limitar significativamente las capacidades de los usuarios, incluso del propietario del archivo.