# BitLocker Encryption: Protección de Datos en Sistemas Windows

## 1. ¿Qué es BitLocker?

**BitLocker** es una función de cifrado de disco completo (Full Disk Encryption) integrada de forma nativa en los sistemas operativos Windows. Su propósito principal es proteger los datos almacenados en unidades de disco duro y dispositivos extraíbles (como unidades USB) mediante la codificación de toda la información. Esto asegura que solo las personas con la clave de cifrado adecuada puedan acceder a los datos.

### 1.1. Características Destacadas

* **Seguridad Robusta**: Utiliza el algoritmo de cifrado **AES (Advanced Encryption Standard)** con claves de 128 o 256 bits, considerado actualmente como altamente seguro.
* **Integración Nativa**: Al estar preinstalado en Windows, facilita su configuración y uso sin necesidad de software adicional.
* **Flexibilidad en la Implementación**: Ofrece varios modos de operación para adaptarse a diferentes necesidades de seguridad.

### 1.2. Modos de Operación

BitLocker protege la clave de cifrado mediante una combinación de factores, lo que garantiza que solo los usuarios autorizados puedan acceder a los datos:

* **Modo TPM (Trusted Platform Module)**: Utiliza el chip TPM del *hardware* para almacenar y proteger las claves de cifrado. Proporciona una capa adicional de seguridad contra ataques físicos.
* **Modo de Autenticación de Usuario**: Requiere que el usuario proporcione una contraseña o una llave USB para desbloquear la unidad cifrada.

## 2. Casos de Uso de BitLocker

BitLocker es una herramienta versátil ideal para:

* Proteger datos sensibles en dispositivos de almacenamiento local.
* Garantizar el cumplimiento de normativas de seguridad en entornos empresariales.
* Proporcionar un respaldo seguro de datos en dispositivos extraíbles, como unidades USB.

## 3. Consideraciones Importantes Antes de Implementar BitLocker

Antes de activar BitLocker, es crucial tener en cuenta lo siguiente:

* **Compatibilidad de Hardware y Software**: Es fundamental verificar que el equipo (hardware y software) sea compatible con BitLocker.
    * **TPM**: Si el dispositivo no cuenta con un chip TPM, la activación de BitLocker es diferente. Se requiere configurar las políticas de grupo para permitir BitLocker sin TPM y, además, disponer de una memoria USB extraíble para almacenar las claves, ya que BitLocker lo exigirá.
* **Copias de Seguridad de Claves de Recuperación**: Es esencial realizar copias de seguridad de las claves de recuperación de BitLocker para evitar la pérdida permanente e irrecuperable del acceso a los datos en caso de olvidar la contraseña.

## 4. Proceso de Activación y Configuración de BitLocker en Windows

A continuación, se detalla el proceso paso a paso para activar y configurar BitLocker en una máquina con Windows 11.

### 4.1. Iniciar la Configuración de BitLocker

1.  **Abrir Búsqueda**: Dirígete a la barra de búsqueda de Windows.
2.  **Buscar BitLocker**: Escribe "BitLocker" en la búsqueda.
3.  **Acceder a la Administración de BitLocker**: Selecciona la opción de administración de BitLocker que aparece en la sección de seguridad del Panel de Control.

    * **Verificación de TPM**: En esta ventana, es posible verificar la administración del TPM para asegurarse de que esté listo.

### 4.2. Activación de BitLocker para la Unidad del Sistema (Unidad C:)

1.  **Activar BitLocker**: En la sección de "Unidades de disco duro", localiza la unidad C: (o la unidad del sistema) y haz clic en "Activar BitLocker".

### 4.3. Guardar la Clave de Recuperación

Después de iniciar la activación, BitLocker realizará una preparación para verificar la compatibilidad. Luego, solicitará guardar una copia de seguridad de la clave de recuperación. Esto es crucial en caso de que se olvide la contraseña. Se ofrecen tres opciones:

1.  **Guardar en su cuenta de Microsoft**: Si tienes una cuenta de Microsoft vinculada.
2.  **Guardar en un archivo**: Para guardar la clave en un archivo local.
3.  **Imprimir la clave de recuperación**: Para obtener una copia física de la clave.

    * **Recomendación de los apuntes**: Para el ejemplo, se elige la opción de "imprimir la clave", que en este caso genera un PDF.
    * **Guardar el PDF**: Se guarda el archivo como `key.pdf` en el escritorio.
    * **Contenido de la Clave de Recuperación**: Este PDF contiene un identificador único que debe corresponderse al que se muestra durante el proceso de descifrado, permitiendo recuperar el contenido de la unidad cifrada.

### 4.4. Elegir el Modo de Cifrado de Unidad

Después de guardar la clave de recuperación, se presentan dos opciones para el cifrado:

1.  **Cifrar únicamente el espacio en disco usado (Más rápido y mejor para nuevos ordenadores y unidades)**: Esta opción es más rápida y se recomienda para unidades o equipos nuevos.
2.  **Cifrar la unidad completa (Más lento, pero mejor para ordenadores en uso y unidades)**: Esta opción es más lenta, pero se recomienda para ordenadores que ya llevan tiempo en uso o unidades con datos existentes.

    * **Recomendación de los apuntes**: Se opta por cifrar la unidad completa para un ordenador en uso.

### 4.5. Seleccionar el Modo de Cifrado AES

Se debe elegir el tipo de cifrado AES a utilizar:

1.  **Modo de cifrado nuevo (XTS-AES)**: Introducido desde Windows 10, es el modo recomendado para sistemas modernos.
2.  **Modo compatible (AES-CBC)**: Si la unidad cifrada se va a utilizar en otros ordenadores o versiones anteriores de Windows (previas a Windows 10), se recomienda el modo compatible.

    * **Recomendación de los apuntes**: Para el ejemplo en Windows 11, se selecciona el **modo nuevo (XTS-AES)**.

### 4.6. Iniciar el Cifrado

1.  **Ejecutar Comprobación del Sistema**: Se indica que el tiempo de cifrado dependerá del tamaño del disco. Es necesario ejecutar una comprobación del sistema (`System check`) antes de reiniciar.
2.  **Reiniciar Windows**: Una vez que la comprobación es compatible, se debe reiniciar Windows para que el cifrado comience.

    * **Proceso de Cifrado en Marcha**: Tras el reinicio, un mensaje indicará que el cifrado está en marcha.
    * **Estado del Cifrado**: El cifrado del disco se realiza mientras se inicia sesión en la cuenta. Una vez completado, la unidad estará protegida.

### 4.7. Opciones Post-Cifrado

Una vez que el cifrado se ha completado, las opciones de BitLocker cambian:

* **Suspender la Protección**: Permite deshabilitar temporalmente BitLocker.
* **Desactivar BitLocker**: Para apagar BitLocker permanentemente y descifrar la unidad.
* **Hacer Copia de Seguridad de la Clave de Recuperación**: Permite volver a guardar o imprimir la clave de recuperación si es necesario.

## 5. Funcionamiento y Protección Post-Activación

Una vez que la unidad está completamente cifrada, los datos están protegidos. Si el disco duro es robado e intentado montar en otro sistema operativo, su contenido estará cifrado por BitLocker y será inaccesible de manera externa sin la clave correcta.

BitLocker es una herramienta poderosa y versátil que brinda una capa adicional de seguridad al prevenir el acceso no autorizado a los datos almacenados en sistemas Windows.