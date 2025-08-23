# Informe Detallado sobre Windows Security: Solución Antimalware Integral

Documentos de Referencia: "5-13 Windows security.pdf", "FSW Clase 13 – Protección de Seguridad de Windows.pdf"

Windows Security, anteriormente conocido como Windows Defender, es una solución antimalware completa preinstalada en los sistemas operativos Windows. Aunque su inclusión ha sido objeto de debate, la creciente complejidad de las amenazas de malware y software malicioso ha hecho que sea una característica esencial para la defensa del sistema. Microsoft ha invertido considerablemente en su mejora, especialmente en las últimas versiones como Windows 10 y Windows 11, añadiendo múltiples características de protección.

Windows Security centraliza la gestión de diversas características de seguridad en un panel único. Algunas de estas características son inherentes a este panel, mientras que otras redirigen a diferentes consolas de administración del sistema operativo.

Las áreas de protección de Windows Security incluyen:
* **Protección contra Virus y Amenazas**
* **Protección de Cuentas**
* **Protección de Firewall y Red**
* **Control de Aplicaciones y Navegador**
* **Seguridad del Dispositivo**
* **Reducción de la Superficie de Ataque**
* Otras características como el estado de salud y rendimiento del dispositivo, y las opciones de control parental.

## 1. Protección contra Virus y Amenazas

Esta es la sección más reconocida de un software antimalware. Ofrece una solución completa para escanear software malicioso y mantener actualizada la base de firmas para las detecciones.

Dentro de esta categoría, se encuentran las siguientes configuraciones y funcionalidades:
* **Protección en tiempo real**: Habilitada por defecto, detiene ataques basados en comportamientos maliciosos conocidos.
* **Escaneos periódicos**: Permite realizar análisis del sistema operativo y los datos almacenados en busca de malware.
* **Protección basada en la nube (Cloud-delivered protection)**: Aumenta y acelera la protección mediante el envío automático de muestras.
* **Envío automático de muestras**: Ayuda a proteger al usuario y a otros de amenazas futuras.
* **Exclusiones**: Permite añadir carpetas o archivos que no serán analizados por el antimalware.
* **Historial de protección**: Muestra las acciones de protección más recientes.
* **Amenazas permitidas**: Permite designar software que puede ser detectado como malware pero que el usuario desea permitir su ejecución, como herramientas de seguridad informática.

### Protección contra Ransomware: Acceso Controlado a Carpetas (Controlled Folder Access)

Dentro de la categoría de Protección contra Virus y Amenazas, una característica destacada es la **Protección contra Ransomware**, la cual incluye el **Acceso Controlado a Carpetas**. Esta es una medida de seguridad excelente que protege al usuario contra ataques de ransomware, un tipo de malware que cifra los datos del usuario y exige un rescate para su recuperación.

El Acceso Controlado a Carpetas permite definir un conjunto de carpetas protegidas a las que solo se les permitirá el acceso (escritura) a aplicaciones previamente autorizadas. Un malware, al no ser una aplicación autorizada, no tendrá permisos de escritura en estas carpetas, impidiendo que cifre los datos.

**Configuración del Acceso Controlado a Carpetas:**
1.  **Habilitar/Deshabilitar**: Se puede activar o desactivar desde la sección de Protección contra Ransomware.
2.  **Carpetas protegidas**: Se pueden añadir carpetas personalizadas a la lista de protección, además de las carpetas del sistema que ya vienen protegidas por defecto (como Documentos).
3.  **Permitir una aplicación a través del Acceso Controlado a Carpetas**: Se pueden autorizar aplicaciones específicas para que tengan permisos de escritura en las carpetas protegidas. Por ejemplo, es lógico permitir que aplicaciones como Microsoft Word o Excel puedan modificar archivos en la carpeta de documentos.
4.  **Recuperación de datos de Ransomware**: Ofrece la opción de configurar la copia inmutable de estos datos en OneDrive, asegurando una posibilidad de recuperación en la nube incluso si el sistema local falla.

## 2. Protección de Cuentas

Esta sección de Windows Security está ligada a la administración de cuentas del usuario y las **opciones de inicio de sesión**, permitiendo configurar diversas opciones de autenticación.

### Bloqueo Dinámico (Dynamic Lock)

Una opción innovadora en Windows 11 es el **Bloqueo Dinámico**. Esta característica permite que el dispositivo se bloquee automáticamente cuando un elemento emparejado vía Bluetooth (como un teléfono móvil) se aleja o sale del rango de alcance del PC. El sistema interpreta que el usuario no está cerca del dispositivo y lo bloquea para evitar accesos no autorizados.

**Configuración del Bloqueo Dinámico:**
1.  Acceder a `Cuentas` > `Opciones de inicio de sesión`.
2.  Dentro de `Opciones de inicio de sesión`, ir a `Configuraciones adicionales`.
3.  Habilitar el **Bloqueo Dinámico**.

## 3. Protección de Firewall y Red

Esta sección de Windows Security enlaza con las configuraciones del **Firewall de Windows**, permitiendo gestionar quién y qué puede acceder a las redes. Aquí se pueden configurar las opciones del firewall para redes de dominio, privadas y públicas, así como permitir aplicaciones a través del firewall, ver notificaciones y acceder a configuraciones avanzadas.

## 4. Control de Aplicaciones y Navegador

Windows Security protege el dispositivo de aplicaciones, archivos o sitios web maliciosos mediante un sistema basado en reputación. Incluye **SmartScreen** para el navegador (Microsoft Edge) y para aplicaciones de la Tienda, así como protección contra **Phishing**. Muchas de estas características vienen configuradas por defecto y activadas.

### Protección basada en reputación
* **Comprobación de aplicaciones y archivos**: Microsoft Defender SmartScreen analiza aplicaciones y archivos no reconocidos descargados de la web.
* **SmartScreen para Microsoft Edge**: Protege contra sitios maliciosos y descargas peligrosas.
* **Protección contra Phishing**: Protege la contraseña del usuario de aplicaciones y sitios maliciosos, además de advertir sobre aplicaciones y sitios maliciosos, reuso de contraseñas y almacenamiento inseguro de contraseñas.
* **Bloqueo de aplicaciones potencialmente no deseadas**: Protege el dispositivo de aplicaciones de baja reputación que pueden causar comportamientos inesperados.

### Protección contra Exploit (Exploit Protection)

La **Protección contra Exploit** está habilitada por defecto en Windows 11. Protege contra vulnerabilidades de seguridad y mitiga diversos tipos de ataques, incluyendo aquellos que intentan inyectar código en procesos legítimos. Muchas de sus características se heredan o integran de **Enhanced Mitigation Experience Toolkit (EMET)**, una herramienta anterior de Microsoft para configuraciones de protección contra ataques.

Las mitigaciones de Exploit Protection pueden configurarse en estado **activado**, **desactivado** o con el **valor por defecto**. Muchas configuraciones por defecto ya vienen activadas, lo que contribuye a un sistema operativo más seguro.

**Modo Auditoría (Audit Mode)**: Algunas configuraciones pueden probarse en modo auditoría. Este modo permite observar cómo actuarían las mitigaciones sin que realmente bloqueen el comportamiento, registrando los eventos para su revisión. Esto es útil para evaluar el impacto sin afectar el uso del PC.

**Configuración de mitigaciones:**
* **Configuración del sistema**: Se aplican a nivel de sistema operativo.
* **Configuración de programas**: Permite definir configuraciones específicas para programas individuales, incluso sobrescribiendo las configuraciones por defecto del sistema. Esto incluye características como **Control Flow Guard (CFG)**, **Data Execution Prevention (DEP)**, y **ASLR (Address Space Layout Randomization)** como `Force randomization for images` y `Randomize memory allocations`. También se pueden configurar el bloqueo de imágenes de baja integridad, imágenes remotas y fuentes no confiables.

## 5. Seguridad del Dispositivo

Esta área permite configurar opciones de seguridad relacionadas con el hardware del dispositivo, siempre que este sea compatible con las tecnologías.

Las opciones de **Seguridad del Dispositivo** incluyen:
* **Aislamiento del Core (Core Isolation)**: Protege las partes centrales del dispositivo utilizando seguridad basada en virtualización. Requiere compatibilidad de hardware.
* **Procesador de seguridad (Security Processor)**: Se refiere al Trusted Platform Module (TPM), un chip que proporciona cifrado adicional para el dispositivo. En dispositivos modernos, el chip TPM suele estar integrado.
* **Arranque seguro (Secure Boot)**: Impide que software malicioso se cargue al inicio del dispositivo.
* **Cifrado de datos (Data Encryption)**: Ayuda a proteger los datos del acceso no autorizado en caso de pérdida o robo del dispositivo. Se gestiona a través de **BitLocker** para cifrar volúmenes de datos y el volumen del sistema. BitLocker también protege el sistema de arranque para evitar la modificación de archivos cargados antes del sistema operativo.

## 6. Reducción de la Superficie de Ataque (Attack Surface Reduction - ASR)

**ASR** es un conjunto de reglas configurables en Windows PowerShell que permiten reducir las posibles vías de ataque al sistema. Estas reglas ayudan a combatir ataques dirigidos a:
* **Office**: Combate ataques que utilizan macros maliciosas.
* **Scripts**: Bloquea la ejecución de Powershell, JavaScript y VBScript maliciosos lanzados por otros programas.
* **Correos**: Bloquea contenido potencialmente peligroso descargado a través de clientes de correo, utilizando reglas configurables que determinan lo que está permitido y lo que no.

**Configuración de ASR a través de Windows PowerShell:**

El comando principal para configurar las reglas de ASR es `Set-MpPreference`.

**Sintaxis:**
`Set-MpPreference -AttackSurfaceReductionRules_Ids <rule ID> -AttackSurfaceReductionRules_Actions Enabled`

* `Set-MpPreference`: Es el cmdlet (comando) en PowerShell para modificar las preferencias de Microsoft Defender.
* `-AttackSurfaceReductionRules_Ids <rule ID>`: Este parámetro se utiliza para especificar el ID de la regla de ASR que se desea configurar. Cada regla de ASR tiene un identificador único (GUID).
* `-AttackSurfaceReductionRules_Actions Enabled`: Este parámetro define la acción para la regla especificada. `Enabled` activa la regla, pero también se pueden usar otros valores como `Disabled` (deshabilita la regla), `AuditMode` (activa el modo auditoría para la regla) o `Warn` (advierte al usuario sin bloquear la acción).

Este comando permite a los administradores de sistemas aplicar políticas de seguridad granulares para protegerse de vectores de ataque comunes que los atacantes suelen explotar.

## 7. Trabajar con las Áreas de Protección de Windows Security (Paso a Paso)

Para interactuar con las diferentes áreas de protección de Windows Security, se siguen los siguientes pasos en el entorno de Windows:

1.  **Acceder a la Configuración de Windows**:
    * Ir a las `Opciones de Configuración` del sistema.
    * Navegar a la categoría de `Privacidad y Seguridad`.

2.  **Explorar la Configuración General de Privacidad**:
    * Dentro de `Privacidad y Seguridad`, se pueden configurar y analizar los permisos utilizados en el equipo.
    * Acceder a configuraciones como el análisis de voz, reconocimiento de voz, personalización, historial de actividad.
    * **Permisos de búsqueda**: Es una opción crucial donde se pueden configurar las opciones de búsqueda y su nivel de protección (moderada, apagada, o estricta).
    * **Excluir carpetas de la búsqueda de Windows**: Permite especificar carpetas (ej. `ProgramData`, archivos del sistema de Windows, backups) para que no sean indexadas durante las búsquedas, mejorando la privacidad y seguridad.
    * **Permisos de aplicaciones**: Revisar y configurar los permisos de acceso a la localización, cámara, micrófono por aplicación, especialmente en dispositivos con estos componentes integrados (portátiles, tablets, móviles).
    * **Encuentra mi dispositivo**: Activar esta opción para localizar un dispositivo perdido o robado, siempre que se use una cuenta de Microsoft 365 o una cuenta en la nube que permita habilitar el posicionamiento.

3.  **Abrir Windows Security**:
    * Desde la sección `Privacidad y Seguridad`, hacer clic en `Abrir Windows Security`.
    * Se abrirá un panel centralizado con todas las características de seguridad.

4.  **Navegar por las Áreas de Protección en Windows Security**:

    * **Protección contra Virus y Amenazas**:
        * Acceder a esta sección para gestionar el software antimalware.
        * **Opciones de escaneo**: Iniciar escaneos del dispositivo (escaneo rápido, completo, personalizado, o sin conexión).
        * **Historial de protección**: Ver las amenazas detectadas y las acciones tomadas.
        * **Configuración de protección contra virus y amenazas**: Gestionar la protección en tiempo real, protección basada en la nube, envío automático de muestras y exclusiones.
        * **Protección contra Ransomware**: Configurar el Acceso Controlado a Carpetas, añadiendo carpetas protegidas y permitiendo aplicaciones específicas. También se puede configurar la copia inmutable en OneDrive para la recuperación de datos.

    * **Protección de Cuentas**:
        * Al hacer clic en esta sección, Windows Security redirige a las `Opciones de Inicio de Sesión` en la configuración de `Cuentas`.
        * Aquí se configuran métodos de inicio de sesión como reconocimiento facial (Windows Hello), PIN, clave de seguridad, contraseña, y contraseña con imagen.
        * **Bloqueo Dinámico**: Activar esta función para que el dispositivo se bloquee automáticamente cuando un dispositivo Bluetooth emparejado se aleja.

    * **Firewall y Protección de Red**:
        * Esta sección enlaza con las configuraciones del Firewall de Windows.
        * Permite gestionar las redes de `Dominio`, `Privada` y `Pública`, así como configurar las notificaciones del firewall, permitir aplicaciones y acceder a `Configuraciones avanzadas` del firewall.

    * **Control de Aplicaciones y Navegador**:
        * Permite configurar la protección basada en reputación.
        * **Configuración de protección basada en reputación**: Gestionar la `Comprobación de aplicaciones y archivos`, `SmartScreen para Microsoft Edge`, `Protección contra phishing` (advertencias sobre aplicaciones maliciosas, reuso de contraseñas, almacenamiento inseguro) y el `Bloqueo de aplicaciones potencialmente no deseadas`.
        * **Protección contra Exploit**: Acceder a la configuración de mitigaciones de ataques.
        * **Configuración del sistema**: Ajustar las mitigaciones a nivel global (ej. Control Flow Guard, Prevención de Ejecución de Datos, Randomización de Asignación de Espacio de Direcciones).
        * **Configuración de programas**: Añadir programas específicos y personalizar las mitigaciones para ellos, incluso sobrescribiendo las configuraciones predeterminadas del sistema.

    * **Seguridad del Dispositivo**:
        * Permite configurar características de seguridad relacionadas con el hardware.
        * **Aislamiento del Core**: Habilitar la seguridad basada en virtualización (requiere compatibilidad de hardware).
        * **Procesador de seguridad**: Ver detalles del chip TPM para cifrado adicional.
        * **Arranque seguro**: Asegura que el software malicioso no se cargue al iniciar el dispositivo.
        * **Cifrado de datos**: Administrar BitLocker para cifrar volúmenes de datos y el volumen del sistema, protegiendo también el sistema de arranque.

Este enfoque paso a paso permite a los usuarios y profesionales de la ciberseguridad configurar y gestionar de manera efectiva la protección integral que ofrece Windows Security.