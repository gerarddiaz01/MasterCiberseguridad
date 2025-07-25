# Encrypting File System (EFS): Cifrado de Archivos y Carpetas en Windows

## 1. ¿Qué es Encrypting File System (EFS)?

**EFS (Encrypting File System)** es una característica de cifrado integrada en el sistema operativo Windows que permite a los usuarios **cifrar archivos y carpetas de forma selectiva** para proteger su contenido contra accesos no autorizados. A diferencia de BitLocker, que cifra unidades completas, EFS opera a nivel de archivo.

### 1.1. Funcionamiento de EFS

* **Cifrado a Nivel de Archivo**: EFS cifra los archivos individualmente, utilizando una clave de cifrado única asociada a cada archivo o carpeta.
* **Protección de Claves**: La clave de cifrado de EFS se almacena en el sistema operativo y está protegida mediante la **PKI (Infraestructura de Clave Pública)** de Windows, garantizando su seguridad.
* **Transparencia para el Usuario**: Una de las principales ventajas de EFS es su **funcionalidad transparente**. Esto significa que el cifrado y descifrado de los archivos ocurren de manera automática, sin requerir ninguna acción adicional por parte del usuario final. Los usuarios pueden trabajar con archivos cifrados de la misma manera que lo harían con archivos no cifrados.
* **Integración con Permisos NTFS**: EFS se integra perfectamente con los permisos de archivos **NTFS**, lo que permite que los archivos cifrados puedan compartirse de manera segura mientras se mantienen protegidos.
* **Integración con Autenticación de Windows**: Se integra estrechamente con la autenticación de Windows. Los usuarios pueden acceder a archivos cifrados utilizando sus credenciales de inicio de sesión, lo que simplifica la gestión de claves y el acceso en entornos empresariales con autenticación centralizada (como Active Directory).

### 1.2. EFS vs. BitLocker

La principal diferencia entre EFS y BitLocker radica en el nivel de cifrado:

| Característica | EFS (Encrypting File System)                                    | BitLocker                                    |
| :------------- | :-------------------------------------------------------------- | :------------------------------------------- |
| **Nivel de Cifrado** | Cifra **archivos y carpetas individuales** (granularidad).    | Cifra **unidades o discos completos** (protección integral). |
| **Integración**| Se integra con los permisos de archivos NTFS.                   | Se integra con el sistema operativo Windows y puede usar TPM. |

Mientras que EFS es más granular, BitLocker proporciona una protección más integral a nivel de unidad de almacenamiento.

## 2. Implementación y Uso Práctico de EFS en Windows

A continuación, se detalla el proceso paso a paso para activar y configurar EFS en un sistema Windows 11. El proceso es similar en versiones anteriores como Windows 10.

### 2.1. Crear la Carpeta o Archivo a Cifrar

1.  **Crear una Nueva Carpeta**: Crea una nueva carpeta en el escritorio, por ejemplo, llamada `test`.
2.  **Crear un Archivo de Prueba**: Dentro de la carpeta `test`, crea un documento de texto simple (ej. con Notepad o WordPad) y escribe un contenido (ej. "hello"). Guarda este archivo dentro de la carpeta `test`.

### 2.2. Cifrar la Carpeta o Archivo

1.  **Acceder a Propiedades**: Haz clic derecho sobre la carpeta (`test` en este ejemplo) y selecciona **Propiedades**.
2.  **Opciones Avanzadas**: Dentro de la ventana de Propiedades, dirígete a la pestaña **General** y haz clic en el botón **Opciones avanzadas...**.
3.  **Habilitar Cifrado**: En la sección "Atributos de cifrado o compresión", marca la casilla **"Cifrar contenido para proteger datos"**.

    * Al intentar acceder a los detalles en este punto, puede que la opción aún no esté disponible.
4.  **Aplicar Cambios**: Haz clic en **Aceptar** y luego en **Aplicar**.

    * (Ver imagen Encrypting File System.pdf, página 2)

### 2.3. Aplicar Cifrado a Subdirectorios y Archivos

Después de hacer clic en "Aplicar", el sistema preguntará cómo desea aplicar el cifrado:

1.  **"Cifrar solo la carpeta"**: Cifrará únicamente la carpeta actual.
2.  **"Cifrar la carpeta y todos los subdirectorios y archivos"**: Esta opción no solo cifrará el directorio actual y su contenido existente, sino que también **cifrará automáticamente cualquier archivo nuevo** que se añada a esta carpeta en el futuro.

    * **Recomendación de los apuntes**: Para una protección integral de la carpeta y su futuro contenido, se recomienda elegir la segunda opción: "Cifrar la carpeta y todos los subdirectorios y archivos".
    * (Ver imagen Encrypting File System.pdf, página 3 - imagen superior)

### 2.4. Gestión del Certificado de Cifrado EFS (Copia de Seguridad)

Una vez que el cifrado se ha aplicado, aparecerá una notificación indicando que el cifrado se ha realizado y se mostrará un candado en el icono de la carpeta (Ver imagen Encrypting File System.pdf, página 3 - imagen inferior). Esta notificación también ofrecerá opciones para gestionar el certificado de cifrado:

1.  **"Hacer una copia de seguridad ahora"**: Opción recomendada para exportar el certificado y su clave privada.
2.  **"Recordar más tarde"**: Posponer la copia de seguridad.
3.  **"No hacer copia de seguridad"**: No recomendado, ya que la pérdida de la clave resultará en la pérdida permanente de acceso a los datos.

    * **Proceso de Copia de Seguridad**:
        1.  Selecciona "Hacer una copia de seguridad ahora" e inicia el asistente de exportación de certificados.
        2.  El formato por defecto será **PKCS #12 (.PFX)**, que incluye el certificado y la clave privada. Haz clic en **Siguiente**.
        3.  **Asignar una Contraseña**: Se solicitará una contraseña para proteger el archivo PFX. Esta contraseña será necesaria para importar el certificado en el futuro.
        4.  **Tipo de Cifrado (Opcional)**: Se puede elegir entre **Triple DES con SHA** o **AES con SHA**. Se recomienda **AES** por ser más robusto y avanzado.
        5.  **Guardar el Certificado**: Define la ubicación para guardar el archivo `.pfx` (ej. en el escritorio con el nombre `key.pfx`).
        6.  **Finalizar**: Un resumen mostrará las opciones seleccionadas. Haz clic en **Finalizar**.
        7.  (Ver imagen Encrypting File System.pdf, página 5)

* **Importar el Certificado**: Si necesitas recuperar el acceso a archivos cifrados en otro sistema o después de una reinstalación, puedes hacer doble clic en el archivo `.pfx` para iniciar el asistente de importación. Se te preguntará dónde almacenar el certificado (usuario actual o máquina local) y se solicitará la contraseña definida al exportarlo.

### 2.5. Verificación y Opciones Adicionales de Gestión de EFS

Una vez que el certificado se ha generado, se pueden verificar los detalles del cifrado y gestionar los certificados existentes:

1.  **Detalles de Cifrado en Propiedades**: Vuelve a las **Propiedades** de la carpeta y a las **Opciones avanzadas...**. El botón **Detalles** ahora estará disponible. Al hacer clic en él, se mostrará qué usuarios tienen acceso a los archivos cifrados y detalles sobre el certificado utilizado. (Ver imagen Encrypting File System.pdf, página 8)
2.  **Administrar Certificados de Cifrado de Archivos**: Si se ha olvidado hacer la copia de seguridad inicial o se desea administrar los certificados EFS existentes, puedes buscar en Windows "Administrar los certificados de cifrado de archivos" (o "Manage file Encryption certificate").
    * Esta opción te mostrará los certificados EFS activos y permitirá realizar un **backup** si no se hizo anteriormente, o verificar su validez y detalles. (Ver imagen Encrypting File System.pdf, página 9)

## 3. Conclusiones sobre EFS

* **Característica Integrada**: EFS es una característica nativa de Windows para cifrar archivos y carpetas de forma selectiva.
* **Granularidad y Permisos NTFS**: Cifra a nivel de archivo y se integra perfectamente con los permisos de archivos NTFS, permitiendo compartir archivos cifrados de manera segura.
* **Funcionalidad Transparente**: El cifrado y descifrado son automáticos para el usuario.
* **Diferencia Clave con BitLocker**: EFS cifra archivos individuales, mientras que BitLocker cifra unidades completas.
* **Estrategia Integral de Seguridad**: Se recomienda utilizar EFS como parte de una estrategia de seguridad más amplia en entornos Windows para proteger archivos sensibles de forma selectiva y mantener la integridad dentro del sistema de archivos.

EFS es una herramienta poderosa para la protección granular y transparente de archivos sensibles en entornos Windows.