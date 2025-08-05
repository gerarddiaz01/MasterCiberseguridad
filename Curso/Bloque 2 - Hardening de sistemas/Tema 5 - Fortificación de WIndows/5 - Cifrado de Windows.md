Documentos de Referencia: "5-14 Cifrado en Windows.pdf", "FSW Clase 14 – Cifrado de Windows.pdf"

# Cifrado en Windows: EFS y BitLocker para la Protección de Datos

Los servicios de cifrado integrados en Windows son herramientas fundamentales para salvaguardar la privacidad de los datos de una organización y prevenir el robo de información en caso de hurto del equipo o acceso físico no autorizado. Windows ofrece de forma nativa dos sistemas de cifrado principales: **Encrypted File System (EFS)** y **BitLocker**.

## 1. Encrypted File System (EFS)

EFS es un sistema de cifrado de archivos basado en el sistema de archivos NTFS. Permite a los usuarios cifrar carpetas y archivos individuales sin necesidad de instalaciones o configuraciones adicionales, lo que proporciona una forma sencilla de asegurar el acceso no autorizado a estos elementos.

### Funcionamiento de EFS
Cuando se cifra un archivo o carpeta con EFS:
* Utiliza un **sistema de clave simétrica** para el cifrado de los datos. El algoritmo por defecto es **AES (Advanced Encryption Standard)** con una clave de cifrado simétrica de 256 bits.
* Esta clave simétrica, a su vez, se cifra mediante la **clave pública** del certificado digital del usuario.
* El certificado del usuario, que contiene tanto su clave pública como su clave privada (o claves asimétricas), se almacena en el perfil del usuario.
* Las claves de cifrado se almacenan en la cabecera del archivo cifrado.

### Vulnerabilidades y Consideraciones de EFS
La protección que ofrece EFS está directamente ligada a la identidad del usuario:
* Si el usuario que cifró los datos tiene la sesión iniciada en el dispositivo, podrá acceder a todo el contenido cifrado de forma transparente, sin necesidad de introducir contraseñas adicionales. EFS identifica la contraseña del certificado del usuario y la utiliza para desbloquear la clave compartida con todo el contenido cifrado por EFS.
* Sin embargo, esta característica implica una vulnerabilidad. Si un atacante logra comprometer la seguridad del usuario y es capaz de iniciar sesión con sus credenciales, tendrá acceso completo a todos los archivos y documentos cifrados con EFS.
* Por otro lado, si alguien accede físicamente al dispositivo con la sesión del usuario cerrada o intenta montar el disco en otro sistema operativo, no podrá ver los archivos cifrados con EFS, ya que no tendrá acceso a la clave del usuario.
* EFS protege la información siempre y cuando no se vulnere la identidad del usuario que realizó el cifrado.

### Implementación Práctica de EFS

**Paso a paso para cifrar una carpeta con EFS:**
1.  **Crear una carpeta**: En un espacio común como la unidad C: (para asegurar que otros usuarios no tengan permiso para acceder si se crea en el escritorio del usuario), crear una nueva carpeta, por ejemplo, llamada "Confidencial".
2.  **Crear documentos de ejemplo**: Dentro de la carpeta "Confidencial", crear algunos documentos, como un documento de texto y una imagen.
3.  **Acceder a Propiedades de la Carpeta**: Hacer clic derecho sobre la carpeta "Confidencial" y seleccionar "Propiedades".
4.  **Configurar Atributos Avanzados**: En la pestaña "General" de las propiedades de la carpeta, hacer clic en el botón "Opciones avanzadas...".
5.  **Habilitar Cifrado**: Marcar la opción "Cifrar contenido para proteger datos" y hacer clic en "Aceptar".
6.  **Aplicar Cambios**: En la ventana de propiedades de la carpeta, hacer clic en "Aplicar". Se preguntará si se desea aplicar los cambios solo a esta carpeta o también a los archivos y subcarpetas contenidos en ella. Seleccionar la opción deseada y hacer clic en "Aceptar".
7.  **Verificación del Cifrado**: Una vez cifrada, los iconos de los documentos dentro de la carpeta "Confidencial" mostrarán un candado, indicando que están cifrados.

**Para descifrar una carpeta con EFS:**
1.  **Acceder a Propiedades de la Carpeta**: Hacer clic derecho sobre la carpeta cifrada y seleccionar "Propiedades".
2.  **Configurar Atributos Avanzados**: En la pestaña "General", hacer clic en "Opciones avanzadas...".
3.  **Deshabilitar Cifrado**: Desmarcar la opción "Cifrar contenido para proteger datos" y hacer clic en "Aceptar".
4.  **Aplicar Cambios**: En la ventana de propiedades, hacer clic en "Aplicar" y confirmar la acción. El candado desaparecerá de los iconos, indicando que la carpeta y su contenido han sido descifrados.

## 2. BitLocker

BitLocker es una solución de cifrado de volumen completo que permite cifrar unidades enteras, incluyendo el volumen del sistema operativo y dispositivos extraíbles (BitLocker To Go). A diferencia de EFS, que cifra a nivel de archivo/carpeta, BitLocker opera a nivel de volumen, lo que proporciona una capa de seguridad más robusta. BitLocker es una característica del sistema en Windows (viene preinstalado en clientes y es una característica instalable en Windows Server).

### Requisitos y Características de BitLocker
* **Chip TPM (Trusted Platform Module)**: BitLocker requiere un chip criptográfico TPM para aprovechar plenamente algunas de sus funcionalidades, especialmente para cifrar el volumen del sistema. El TPM almacena claves y secretos, lo que permite que BitLocker funcione incluso durante el proceso de arranque del sistema operativo. Los dispositivos modernos suelen integrar este chip.
* **Cifrado de volumen completo**: Cifra todo el volumen del disco. Esto significa que, aunque se obtengan las credenciales del usuario o se intente montar el disco en otro sistema, si no se conoce la clave de cifrado, no se podrá acceder a los datos.
* **Protección del arranque del sistema**: BitLocker puede configurarse para proteger el proceso de arranque del sistema operativo. Al cifrar el volumen del sistema, BitLocker comprueba que no haya habido modificaciones en componentes críticos de arranque como:
    * La BIOS y extensiones de plataforma.
    * Código de memoria de solo lectura (ROM) opcional.
    * Código del Master Boot Record (MBR).
    * El sector de arranque de NTFS.
    * El Windows Boot Manager.
    * El Core Root of Trust for Measurement.
* **Factores de autenticación adicionales**: Además del chip TPM, BitLocker puede configurarse para requerir un segundo factor de autenticación, como un PIN, una contraseña o una llave USB para el arranque del dispositivo.

### Vulnerabilidades y Consideraciones de BitLocker
* **Clave de recuperación**: Es crucial almacenar la clave de recuperación de BitLocker en un lugar seguro y diferente al dispositivo cifrado. Si se olvida la contraseña y se pierde la clave de recuperación, los datos cifrados pueden ser irrecuperables. Si alguien accede a la clave de recuperación, podrá descifrar el volumen.
* **Tipos de disco**: BitLocker no es compatible con **discos dinámicos**. Solo puede cifrar **discos básicos**.

### Implementación Práctica de BitLocker

**Paso a paso para cifrar un volumen con BitLocker:**
1.  **Crear un disco adicional y volumen**:
    * Acceder al `Administrador de Discos` (se puede buscar en el menú de inicio).
    * Si es necesario, inicializar un nuevo disco.
    * Crear un "Nuevo volumen simple" en un disco `básico` (no dinámico). Asignar una letra de unidad (ej. `E:`) y formatearlo con el sistema de archivos NTFS.

2.  **Iniciar BitLocker**:
    * Abrir el `Explorador de Archivos`.
    * Hacer clic derecho sobre el volumen recién creado (ej. `Nuevo Volumen (E:)`) y seleccionar "Activar BitLocker". (Si no aparece la opción, verificar que el disco sea `básico`).
    * Si se está en Windows Server, la característica de BitLocker debe instalarse previamente.

3.  **Asistente de Cifrado**:
    * Se iniciará el asistente de BitLocker.
    * **Método de desbloqueo**: Elegir cómo desbloquear la unidad. Se puede optar por una `Smart Card` o una `Contraseña`.
    * **Generar y guardar la clave de recuperación**: El asistente preguntará dónde guardar la clave de recuperación. Es la clave para descifrar el dispositivo en caso de olvidar la contraseña. Las opciones incluyen:
        * Guardar en la cuenta de Microsoft (para sistemas online).
        * Guardar en una unidad flash USB.
        * Guardar en un archivo (puede ser en un servicio de nube como OneDrive o en un dispositivo extraíble).
        * Imprimir la clave de recuperación.
        * **¡Advertencia!**: No se recomienda guardar la clave de recuperación en el mismo dispositivo que se está cifrando. Para la práctica en una máquina virtual, puede guardarse en el escritorio si no hay otra opción, pero en un entorno real es una mala práctica de seguridad.

4.  **Seleccionar el modo de cifrado**:
    * **Cifrar solo el espacio de disco usado (más rápido y mejor para PC y unidades nuevas)**: Cifra solo los datos existentes. Los nuevos datos se cifrarán automáticamente.
    * **Cifrar la unidad completa (más lento y mejor para PC y unidades ya en uso)**: Cifra todo el volumen. Esto asegura que incluso los datos eliminados que aún puedan ser recuperables estén cifrados.

5.  **Iniciar Cifrado**:
    * Hacer clic en "Siguiente" y luego en "Iniciar cifrado".
    * El proceso de cifrado comenzará. Puede tardar un tiempo, dependiendo del tamaño del volumen.

### Administración de BitLocker

Una vez cifrado, el volumen mostrará un candado en el Explorador de Archivos. Al hacer clic derecho sobre el volumen cifrado y seleccionar "Administrar BitLocker", se accederá a la consola de administración, donde se pueden:
* Realizar copias de seguridad de la clave de recuperación.
* Cambiar la contraseña.
* Eliminar la contraseña.
* Añadir una Smart Card.
* Activar el auto-desbloqueo.
* Desactivar BitLocker.
* Ver información sobre el chip TPM.
* Acceder al Administrador de Discos.

### Verificación del Cifrado de BitLocker con otro Usuario

Para demostrar la efectividad de BitLocker:
1.  Cerrar la sesión del usuario que cifró el volumen.
2.  Iniciar sesión con un usuario diferente en el mismo dispositivo.
3.  Intentar acceder al volumen cifrado con BitLocker. El sistema solicitará la contraseña para desbloquear el volumen. Sin la contraseña (o la clave de recuperación), el otro usuario no podrá acceder a los datos.
4.  Si se ingresa la contraseña correcta, el volumen se desbloqueará y los datos serán accesibles.
5.  Si se extrae el disco duro y se intenta montar en otro sistema operativo o se utilizan herramientas forenses, el volumen seguirá cifrado, haciendo muy difícil el acceso a los datos sin la clave.

## 3. Resolución del Ejercicio Propuesto

El ejercicio planteado consiste en:
1.  Crear una carpeta llamada "Confidencial" y cifrarla con EFS.
2.  Crear un disco adicional, configurar un volumen para datos y cifrarlo con BitLocker.

### Implementación del Ejercicio

**Parte 1: Cifrado con EFS**
1.  **Crear la carpeta "Confidencial"**: En la unidad `C:`, se crea una nueva carpeta llamada `Confidencial`.
2.  **Crear documentos de ejemplo**: Dentro de `Confidencial`, se añaden un par de documentos (ej. un archivo de texto y una imagen).
3.  **Cifrar la carpeta**:
    * Clic derecho en `Confidencial` > `Propiedades` > `Opciones avanzadas...`.
    * Marcar "Cifrar contenido para proteger datos" > `Aceptar`.
    * `Aplicar` > `Aceptar` (confirmando aplicar a la carpeta y subcarpetas).
4.  **Verificación**: Se observa que los iconos de los documentos dentro de `Confidencial` muestran un candado, confirmando el cifrado.

**Parte 2: Cifrado con BitLocker**
1.  **Preparar un disco adicional**:
    * Abrir el `Administrador de Discos`.
    * Se crea un nuevo volumen simple (`E:`) en un disco `básico`. Se le da formato NTFS.
    * **Nota importante**: Se verifica que si se intenta cifrar un disco `dinámico` (como el `F:`, si se hubiera creado), la opción de BitLocker no estará disponible. BitLocker solo funciona con discos `básicos`.

2.  **Activar BitLocker en el volumen básico (`E:` por ejemplo)**:
    * En el `Explorador de Archivos`, clic derecho en `Nuevo Volumen (E:)` > "Activar BitLocker".
    * Se establece una contraseña para el volumen.
    * Se guarda la clave de recuperación en un archivo (para el ejercicio, en el escritorio; en un entorno real, en una ubicación segura externa).
    * Se selecciona "Cifrar la unidad completa" (o "Cifrar solo el espacio de disco usado", según la necesidad).
    * Se inicia el cifrado.

### Verificación de la Protección con Otro Usuario

1.  **Cerrar sesión** del usuario actual.
2.  **Iniciar sesión** con un usuario diferente del mismo dispositivo.
3.  **Intentar acceder al volumen cifrado con BitLocker (`E:`)**:
    * Al intentar abrir la unidad, se solicitará la contraseña.
    * Si se introduce una contraseña incorrecta, el acceso será denegado, demostrando la protección de BitLocker.
    * Si se introduce la contraseña correcta, el volumen se desbloqueará y será accesible.
4.  **Intentar acceder a la carpeta cifrada con EFS (`Confidencial` en `C:`)**:
    * Se puede acceder a la carpeta `Confidencial`.
    * Sin embargo, al intentar abrir los documentos dentro de ella, se mostrará un mensaje de que no se tienen permisos para ver los archivos, ya que están cifrados con la clave del otro usuario. Esto demuestra que EFS protege la confidencialidad de los datos para otros usuarios del mismo sistema, incluso si tienen acceso a la ubicación física de los archivos.

## Conclusión

Windows ofrece dos sistemas de cifrado nativos y muy eficientes: EFS para archivos y carpetas individuales, y BitLocker para volúmenes completos y la protección del arranque. EFS garantiza la privacidad de los datos para otros usuarios, siempre que no se comprometa la identidad del usuario que cifró los datos. BitLocker, por su parte, ofrece una protección más robusta a nivel de volumen, dificultando el acceso a los datos incluso si el dispositivo es robado y el disco es extraído. Ambas tecnologías pueden combinarse para crear un entorno de seguridad de datos mucho más robusto.