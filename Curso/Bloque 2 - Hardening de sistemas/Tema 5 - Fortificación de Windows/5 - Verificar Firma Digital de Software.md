Documentos de Referencia: "5-12 Seguridad Digital.pdf", "FSW Clase 12 – Verificar Firma Digital de Software.pdf"

# Informe sobre la Firma Digital de Software y Ciberseguridad

## 1. Protección de Ejecución de Código y Seguridad de las Aplicaciones

La seguridad del sistema operativo no termina con su configuración inicial. Es fundamental revisar las características y capacidades de ejecución de las aplicaciones y programas para evitar que se ejecute software malicioso. El objetivo principal es asegurar que las aplicaciones que se descargan de internet no contengan malware que pueda comprometer el dispositivo.

### Verificación de la Integridad del Software

Una estrategia clave para validar la integridad de un archivo o aplicación es verificar su **firma criptográfica** o **hash**. Esta firma, un valor único asociado al archivo, se publica junto con este. Al descargar el archivo, el usuario puede calcular su hash y compararlo con el valor publicado. Si ambos coinciden, se tiene la garantía de que el software no ha sido modificado. Aunque esta medida es efectiva, existen casos en los que los atacantes pueden comprometer el sitio web y modificar tanto el archivo como su hash, lo que resulta en un hash asociado a un archivo malicioso.

Para realizar esta verificación, el sistema operativo Windows ofrece la herramienta **PowerShell**, que incluye el comando `get-filehash`.

### Firma Criptográfica del Fabricante

Una de las garantías más sólidas para ejecutar software legítimo es la **firma criptográfica del fabricante**. Un **certificado digital** legitima la autoría de un producto y hace extremadamente difícil la modificación del software para inyectar malware. Estos certificados digitales pueden ser verificados para asegurar que son correctos y que pertenecen genuinamente al fabricante del software.

## 2. Herramientas para la Verificación de Firmas y Certificados Digitales

Existen diversas herramientas, tanto integradas en el sistema operativo como externas, que permiten verificar el origen y la integridad del software.

### 2.1. Administrador de Tareas (Task Manager)

El Administrador de Tareas de Windows permite verificar el certificado digital de un proceso en ejecución. Al navegar a la sección de "Detalles", se puede seleccionar un proceso, acceder a sus propiedades y, en la pestaña de "Detalles", ver las firmas asociadas, el nombre del producto y el copyright.

### 2.2. Sysinternals Suite Tools

La suite de herramientas Sysinternals, disponible para descarga gratuita desde el sitio oficial de Microsoft, ofrece una amplia gama de utilidades para propósitos de seguridad, diagnóstico y gestión. Estas herramientas se caracterizan por su bajo impacto en el sistema, la no necesidad de instalación y por dejar un rastro mínimo. Además, muchas de ellas no requieren privilegios de administrador para su ejecución, aunque se obtiene más información si se ejecutan con ellos.

Dos herramientas clave dentro de la suite para la verificación de firmas digitales son **Sigcheck** y **Process Explorer**.

#### Sigcheck

**Sigcheck** es una herramienta de línea de comandos diseñada específicamente para verificar firmas de archivos.

**Sintaxis y uso:**

* `sigcheck [-a][-h][-i][-e][-I][-n][[-s]|[-c-ct]|[-m]] [-q] [-r][-u][-vt] [-v[r][s]][-f catalog file] <file or directory>`
    * Este comando se utiliza para verificar la firma de un archivo o directorio.
* `sigcheck-d [-cl-ct] <file or directory>`
    * Utilizado para volcar información de certificados.
* `sigcheck -o [-vt][-v[r]] <sigcheck csv file>`
    * Permite escanear un archivo CSV generado por Sigcheck.
* `sigcheck-t[u][v] [-i] [-cl-ct] <certificate store name *>`
    * Sirve para listar el contenido de los almacenes de certificados.

#### Process Explorer

**Process Explorer** es una herramienta mucho más potente que el Administrador de Tareas de Windows. Permite una revisión exhaustiva de los procesos en ejecución, incluyendo la verificación de la firma digital asociada al ejecutable o a la librería que lo lanzó.

**Pasos para verificar la firma digital con Process Explorer:**

1.  Ejecutar Process Explorer (se recomienda como administrador para obtener más información).
2.  Seleccionar un proceso de la lista.
3.  Acceder a las propiedades del proceso.
4.  En la ventana de propiedades, se puede verificar la firma digital. En una columna habilitada para tal fin, se mostrará la verificación del certificado digital.

**Funcionalidades Adicionales de Process Explorer:**

Process Explorer no solo permite verificar firmas digitales, sino que también ofrece la posibilidad de enviar el hash del ejecutable a **VirusTotal** para un análisis más detallado.

## 3. VirusTotal: Un Servicio de Análisis Antimalware

**VirusTotal** es un servicio web que permite a los usuarios enviar archivos para que sean analizados por una gran cantidad de motores antimalware (se mencionan 76 motores en los documentos). Este servicio proporciona un resultado que indica cuántos de esos motores detectan el archivo como malicioso.

**Cómo funciona la integración con Process Explorer:**

* Cuando se envía un proceso a VirusTotal por primera vez desde Process Explorer, la herramienta envía el hash del archivo. VirusTotal revisa su base de datos para ver si ese hash ya ha sido analizado y si está asociado a alguna actividad maliciosa.
* Si se reenvía el archivo, VirusTotal realiza un análisis más exhaustivo del archivo en sí, no solo del hash.

**Pasos para usar VirusTotal desde Process Explorer:**

1.  Dentro de Process Explorer, se puede hacer clic derecho en cualquiera de los procesos en ejecución.
2.  Seleccionar la opción para chequear el proceso con VirusTotal.
3.  Esto enviará el hash del ejecutable que lanzó el proceso a VirusTotal para su análisis.
4.  El resultado del análisis se mostrará directamente en la interfaz de Process Explorer, indicando si el certificado digital es válido y el número de detecciones de VirusTotal.

Esta integración facilita la detección de software malicioso al aprovechar la potencia de múltiples motores antimalware sin necesidad de salir del entorno de diagnóstico.

## Conclusión

La protección de la ejecución de código y la verificación de la firma digital son pilares fundamentales en la ciberseguridad. Herramientas como PowerShell, el Administrador de Tareas y, de manera más avanzada, la suite de Sysinternals (con Sigcheck y Process Explorer), permiten a los profesionales y usuarios verificar la legitimidad del software. La integración con servicios como VirusTotal amplía aún más estas capacidades, proporcionando un análisis integral que ayuda a identificar y mitigar la ejecución de software malicioso. La suite de Sysinternals, en particular, ofrece un conjunto de utilidades invaluables que, al ser ejecutadas desde un dispositivo externo, garantizan una lectura fidedigna del estado de un equipo comprometido.