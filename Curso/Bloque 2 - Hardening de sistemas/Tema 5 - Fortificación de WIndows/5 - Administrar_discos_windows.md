### Informe de Ciberseguridad: Administración de Discos, Parches y Actualizaciones en Windows

Para mayor información ve al tema 5 de ConquerBlocks, y mira FSW Clase 04 – Administrar las características del disco y FSW Clase 05 – Solución del ejercicio. 

#### Introducción: La Importancia de las Actualizaciones

En la ciberseguridad actual, es vital mantener el sistema operativo y todas las aplicaciones actualizadas. Un gran número de ataques y la propagación de **Malware** se basan en la explotación de **vulnerabilidades** conocidas para las que ya existen parches y soluciones. Por ello, es imprescindible establecer una política de actualizaciones efectiva para fortificar el sistema contra estos ataques.

#### Tipos de Actualizaciones de Windows

El sistema de actualizaciones de Windows se divide en dos categorías principales:

* **Actualizaciones de Características (Feature Updates):** Son actualizaciones del propio sistema operativo que introducen nuevas funcionalidades y versiones. Generalmente se despliegan dos veces al año.
* **Actualizaciones de Calidad (Quality Updates):** No cambian la versión del sistema operativo. Son correcciones para problemas o actualizaciones de seguridad que se liberan en cualquier momento, especialmente para solucionar **vulnerabilidades** críticas que están siendo explotadas. Suelen ser acumulativas y se publican, por lo general, el segundo martes de cada mes.

Para entornos profesionales, Microsoft ofrece **Windows Server Update Services (WSUS)**, un rol de servidor que centraliza la gestión de actualizaciones, permitiendo configurar políticas, grupos de equipos y monitorear el despliegue de parches.

#### La Tabla de Particiones y su Seguridad

La **tabla de particiones** es un componente de bajo nivel que se encuentra en los primeros sectores de un disco duro. Un **Malware** instalado en la tabla de particiones puede ejecutarse antes de que el sistema operativo se inicie, lo que hace que sea muy difícil de detectar y eliminar.

* **Master Boot Record (MBR):** Es el primer sector del disco duro, contiene la tabla de particiones principal (**Master Partition Table**) y el código de arranque principal (**Master Boot Code**). El **Master Partition Table** describe hasta cuatro particiones.
* **GUID Partition Table (GPT):** Es una tecnología más moderna que reemplaza al **MBR** y permite utilizar discos dinámicos y arranques más avanzados como **UEFI (Extensible Firmware Interface)**.

La tabla de particiones termina con los caracteres hexadecimales `55 AA`. Es una buena práctica realizar una copia de seguridad de los primeros 63 sectores del disco y verificar periódicamente que no se hayan modificado para detectar la presencia de **Malware**.

#### Administración de Discos y Volúmenes en Windows

Windows ofrece herramientas potentes para la administración de discos y volúmenes que impactan directamente en la seguridad y la resiliencia del sistema.

* **Inicialización de Discos:** Al añadir un nuevo disco, este debe ser inicializado. En este proceso, se debe elegir el estilo de la tabla de particiones: **MBR** o **GPT**.
* **Discos Básicos vs. Dinámicos:**
    * **Discos básicos:** El tipo de disco por defecto, soporta particiones primarias y lógicas.
    * **Discos dinámicos:** Ofrecen mayor flexibilidad y funcionalidades avanzadas como la creación de volúmenes reflejados (**mirrored volumes**) y distribuidos (**spanned volumes**).
    
    Para operaciones avanzadas como la creación de volúmenes reflejados, los discos deben ser obligatoriamente dinámicos.

* **Tipos de Volúmenes:**
    * **Volumen simple:** Utiliza el espacio de un único disco.
    * **Volumen distribuido:** Combina el espacio de varios discos en un solo volumen lógico. Aumenta el espacio, pero si un disco falla, se pierde toda la información.
    * **Volumen reflejado (Mirrored Volume):** Duplica la información de forma idéntica en dos discos diferentes. Esto proporciona **tolerancia a fallos**, ya que si uno de los discos falla, el otro contiene una copia completa y funcional de los datos.

#### Espacios de Almacenamiento (Storage Spaces)

Los espacios de almacenamiento permiten crear una capa de abstracción entre el volumen de datos y el **hardware** físico. Se pueden agrupar discos físicos en un "pool" y, a partir de este, generar discos virtuales. Esto permite una gestión más flexible, añadiendo discos físicos a medida que se necesita más espacio y configurando opciones avanzadas de **tolerancia a fallos**.

#### Optimización y Mantenimiento de Discos

Windows ofrece diversas opciones de administración y mantenimiento de discos:

* **Optimizar Unidades:** Esta opción permite analizar y desfragmentar discos, lo cual mejora el rendimiento del sistema.
* **Programación de Mantenimiento:** Se puede programar el proceso de desfragmentación de forma automática.
* **Opciones de Backup:** Desde la configuración de almacenamiento, se puede acceder a las opciones de backup del sistema, que pueden integrarse con servicios en la nube como **OneDrive** para una mayor seguridad.

#### Configuración de la Administración de Discos en una Máquina Virtual

En un entorno de laboratorio, se puede practicar la administración de discos de la siguiente manera:
1.  **Añadir Discos:** Apagar la máquina virtual y, desde su configuración de almacenamiento, añadir dos o más discos duros virtuales.
2.  **Inicializar Discos:** Al arrancar la máquina virtual, el **Administrador de discos** reconocerá los nuevos discos. Es necesario inicializarlos y seleccionar el estilo de partición (**MBR** o **GPT**).
3.  **Crear un Volumen Reflejado:**
    * Convertir los discos básicos a dinámicos.
    * Desde el **Administrador de discos**, seleccionar la opción de crear un "Nuevo volumen reflejado".
    * Seleccionar los dos discos que formarán el volumen.
    * Asignar una letra de unidad y un sistema de archivos.

El resultado es un volumen que solo tiene el tamaño de uno de los discos, pero con la información duplicada, ofreciendo así una protección contra fallos del **hardware**.

#### Conclusión

Mantener el sistema operativo y las aplicaciones actualizadas es una medida de seguridad básica y vital. La administración avanzada de discos, incluyendo la correcta inicialización con **GPT** y la creación de volúmenes reflejados, añade una capa de **resiliencia** y **tolerancia a fallos** que es fundamental para proteger la información. La vigilancia de la tabla de particiones y la comprensión de las herramientas de gestión de discos son habilidades esenciales para fortificar un sistema Windows de forma integral.