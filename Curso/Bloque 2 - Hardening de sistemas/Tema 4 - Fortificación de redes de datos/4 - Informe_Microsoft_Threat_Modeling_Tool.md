# Ejercicio Práctico de Modelado de Amenazas con Microsoft Threat Modeling Tool: Implementación y Análisis de Resultados

Este informe guiará a los estudiantes a través de un ejercicio práctico de modelado de amenazas utilizando la **Microsoft Threat Modeling Tool**. Se detallará la implementación de una arquitectura de red sencilla, su representación en la herramienta, la validación del diagrama y el análisis exhaustivo de las amenazas identificadas en el informe generado, preparando el terreno para comprender los fallos y proponer mejoras.

## 1\. Objetivo del Ejercicio

El objetivo principal de este ejercicio es doble:

1.  **Comprender el Uso de la Herramienta**: Aprender a utilizar la **Microsoft Threat Modeling Tool** para construir una representación visual de una arquitectura de red.
2.  **Identificar Amenazas Automáticamente**: Procesar la arquitectura diseñada para que la herramienta genere un listado de posibles amenazas que puedan inferir directamente contra ella.

Este ejercicio es sencillo y básico, sirviendo como fundamento para construir modelos más complejos y completos en el futuro.

## 2\. Diseño de la Arquitectura Propuesta

La arquitectura que vamos a construir es una configuración de red básica que incluye una máquina virtual principal (VM), una base de datos local y una base de datos en la nube.

### 2.1. Elementos de la Arquitectura

Los componentes clave que utilizaremos son:

  * **Máquina Principal (VM)**: Representa nuestro servidor principal o máquina virtual. En la herramienta, usaremos el *stencil* "Virtual Machine".
  * **Base de Datos SQL Local (SQL DB)**: Una base de datos ubicada en la red interna o local, a la que llamaremos "SQL Database". Usaremos el *stencil* "SQL Database".
  * **Base de Datos en la Nube (Cloud DB / Cloud Storage)**: Una base de datos o almacenamiento ubicado en un servicio de nube. Usaremos el *stencil* "Cloud Storage".

### 2.2. Interconexiones y Flujos de Datos

Las conexiones entre estos elementos, también conocidas como *dataflows*, se diseñarán de la siguiente manera:

  * **VM a SQL DB**:
      * Una conexión de **VM hacia SQL DB** utilizando el protocolo **HTTP**. Esta elección se hace intencionadamente para *forzar* que el informe de la herramienta genere más fallos de seguridad, lo que permitirá un análisis más detallado de las vulnerabilidades.
      * Una conexión de **SQL DB hacia VM** utilizando el protocolo **HTTPS**.
  * **VM a Cloud DB**:
      * Una conexión de **VM hacia Cloud DB** utilizando el protocolo **HTTPS**.

En resumen, la arquitectura tendrá dos conexiones HTTPS y una conexión HTTP.

### 2.3. Definición de Límites (Boundaries)

Es crucial establecer los **límites (boundaries)** para marcar las diferentes zonas de la arquitectura. Incluiremos una **separación hacia Internet**.

  * El *boundary* de Internet debe **cortar al menos un *dataflow*** (línea de conexión). Este es el indicador que le dice a la herramienta que esa parte o conexión se dirige *hacia afuera*, es decir, hacia Internet. En el esquema implementado, el *boundary* corta la conexión entre la máquina virtual y el Cloud Storage. Esto es vital para que el modelo de amenazas interprete correctamente las implicaciones de seguridad de los flujos de datos que cruzan esa frontera.

A continuación, se presenta el borrador del esquema de la arquitectura a construir:

## 3\. Realización del Ejercicio con Microsoft Threat Modeling Tool

Para realizar este ejercicio, asumimos que la Microsoft Threat Modeling Tool ya está instalada y lista para usarse. El objetivo es plasmar el esquema a mano alzada directamente en la herramienta.

### 3.1. Pasos para Diseñar la Arquitectura en la Herramienta

1.  **Iniciar la Herramienta y Crear un Nuevo Modelo**: Abre la Microsoft Threat Modeling Tool y selecciona la plantilla adecuada, como la "SDL TM Knowledge Base (SDLTM.tmt)", para acceder a los *stencils*. Luego, haz clic en "Create a Model".

2.  **Añadir Elementos Principales**:

      * Arrastra el *stencil* **"Virtual Machine"** y re-nómbralo a "VM".
      * Arrastra el *stencil* **"SQL Database"** y colócalo cerca de la VM.
      * Arrastra el *stencil* **"Cloud Storage"** y colócalo también en el área de dibujo.

3.  **Dibujar las Conexiones (Dataflows)**:

      * Para la conexión **SQL DB a VM (HTTPS)**: Arrastra un *dataflow* de tipo **"HTTPS"** desde la "SQL Database" hasta la "Virtual Machine".
      * Para la conexión **VM a Cloud DB (HTTPS)**: Arrastra un *dataflow* de tipo **"HTTPS"** desde la "Virtual Machine" hacia el "Cloud Storage".
      * Para la conexión **VM a SQL DB (HTTP)**: Arrastra un *dataflow* de tipo **"HTTP"** desde la "Virtual Machine" hacia la "SQL Database".

    La interconexión de estos elementos se asemeja a "poner piezas de diferentes puzles e interconectarlas".

4.  **Insertar el Límite (Boundary)**:

      * Busca el *stencil* **"Boundary"** o "Internet Boundary" y arrástralo al diagrama.
      * Posiciónalo de manera que la línea discontinua **corte la conexión** que deseas que represente un paso por Internet. En este caso, el *boundary* corta la conexión entre la máquina virtual y el servicio en la nube (Cloud Storage).

### 3.2. Validación del Diagrama

Es crucial comprobar que todas las conexiones se han realizado correctamente.

1.  **Usar Diagram Reader**: Haz clic en **"Diagram" \> "Reader" \> "Read Full Diagram"**.

2.  **Verificar Descripción**: La herramienta generará una descripción escrita de cada elemento y sus conexiones. Esto permite comprobar que no hay errores de conexión o elementos no relacionados. En este caso, la descripción confirmará la conexión HTTP entre la VM y la SQL DB, la HTTPS entre SQL DB y VM, y la HTTPS entre VM y Cloud Storage, marcando esta última como "Internet Boundary".

## 4\. Análisis del Informe Generado: Amenazas Identificadas

Una vez que el diagrama es correcto y validado, se procede a la fase de informe.

1.  **Generar el Informe**: Ve a la sección **"Reports"** y selecciona **"Create Full Report"**. Guarda el informe con un nombre adecuado.

El informe del modelado de amenazas mostrará una serie de posibles problemas de seguridad, vulnerabilidades o amenazas genéricas que pueden afectar la arquitectura diseñada. La herramienta analiza los elementos y las interacciones, mostrando un esquema global de la arquitectura y luego detallando los bloques y sus amenazas específicas. En este caso, se encontraron **12 problemas** principales, los cuales analizaremos a continuación.

### 4.1. Amenazas en la Interacción HTTP (VM a SQL DB)

La interacción **HTTP** entre la Máquina Virtual y la Base de Datos SQL es particularmente insegura y genera varios problemas de alta prioridad.

  * **1. Potential Excessive Resource Consumption for Virtual Machine or SQL Database**
      * **Categoría**: Denial Of Service
      * **Descripción**: La Máquina Virtual o la Base de Datos SQL pueden no tomar medidas explícitas para controlar el consumo de recursos. Los ataques de consumo de recursos son difíciles de manejar, y a veces tiene sentido dejar que el sistema operativo haga el trabajo. Se debe tener cuidado de que las solicitudes de recursos no generen *deadlock* y que tengan un *timeout*.
      * **Comentario del profesor**: Un ataque de denegación de servicio (DoS) también se puede provocar internamente si no hay una buena configuración del servidor o de la base de datos, lo que podría llevar a un **auto-denial of service**.
  * **2. Potential SQL Injection Vulnerability for SQL Database**
      * **Categoría**: Tampering
      * **Descripción**: La inyección SQL es un ataque en el que se inserta código malicioso en cadenas que luego se pasan a una instancia de SQL Server para su análisis y ejecución. Cualquier procedimiento que construya sentencias SQL debe ser revisado en busca de vulnerabilidades de inyección, ya que SQL Server ejecutará cualquier consulta sintácticamente válida que reciba. Incluso los datos parametrizados pueden ser manipulados por un atacante hábil y decidido.
      * **Comentario del profesor**: Un ejemplo directo de *Tampering* es un ataque simple de **SQL Injection**.
  * **3. Spoofing of Destination Data Store SQL Database**
      * **Categoría**: Spoofing
      * **Descripción**: La base de datos SQL puede ser suplantada por un atacante, lo que podría llevar a que los datos se escriban en el objetivo del atacante en lugar de la base de datos SQL. Considere usar un mecanismo de autenticación estándar para identificar el almacén de datos de destino.
      * **Comentario del profesor**: La base de datos podría interceptar la información (un ataque **Man-in-the-Middle**) y modificar los datos que van de un sitio a otro, lo cual es un problema muy grave por la alteración de la información.

### 4.2. Amenazas en la Interacción HTTPS (SQL DB a VM y VM a Cloud Storage)

Aunque HTTPS es más seguro, la herramienta aún identifica amenazas, especialmente en el cruce del *Internet Boundary*.

  * **4. Spoofing of Destination Data Store Cloud Storage**
      * **Categoría**: Spoofing
      * **Descripción**: El almacenamiento en la nube puede ser suplantado por un atacante, lo que podría llevar a que los datos se escriban en el objetivo del atacante en lugar del almacenamiento en la nube. Considere usar un mecanismo de autenticación estándar para identificar el almacén de datos de destino.
  * **5. Spoofing the Virtual Machine Process**
      * **Categoría**: Spoofing
      * **Descripción**: La máquina virtual puede ser suplantada por un atacante, lo que podría llevar a un acceso no autorizado al almacenamiento en la nube. Considere usar un mecanismo de autenticación estándar para identificar el proceso de origen.
  * **6. The Cloud Storage Data Store Could Be Corrupted**
      * **Categoría**: Tampering
      * **Descripción**: Los datos que fluyen a través de HTTPS pueden ser manipulados por un atacante. Esto puede llevar a la corrupción del almacenamiento en la nube. Asegure la integridad del flujo de datos hacia el almacén de datos.
  * **7. Data Store Denies Cloud Storage Potentially Writing Data**
      * **Categoría**: Repudiation
      * **Descripción**: El almacenamiento en la nube afirma que no escribió datos recibidos de una entidad al otro lado del límite de confianza. Considere usar el registro o la auditoría para registrar la fuente, la hora y el resumen de los datos recibidos.
  * **8. Potential Excessive Resource Consumption for Virtual Machine or Cloud Storage**
      * **Categoría**: Denial Of Service
      * **Descripción**: ¿La Máquina Virtual o el Almacenamiento en la Nube toman medidas explícitas para controlar el consumo de recursos? Los ataques de consumo de recursos pueden ser difíciles de manejar, y a veces tiene sentido dejar que el sistema operativo haga el trabajo. Tenga cuidado de que sus solicitudes de recursos no generen *deadlock* y que tengan un *timeout*.
  * **9. Data Flow HTTPS Is Potentially Interrupted**
      * **Categoría**: Denial Of Service
      * **Descripción**: Un agente externo interrumpe el flujo de datos a través de un límite de confianza en cualquier dirección.
  * **10. Data Store Inaccessible**
      * **Categoría**: Denial Of Service
      * **Descripción**: Un agente externo impide el acceso a un almacén de datos al otro lado del límite de confianza.
  * **11. Weak Access Control for a Resource**
      * **Categoría**: Information Disclosure
      * **Descripción**: La protección inadecuada de datos en la base de datos SQL puede permitir que un atacante lea información no destinada a su divulgación. Revise la configuración de autorización.
  * **12. Spoofing of Source Data Store SQL Database**
      * **Categoría**: Spoofing
      * **Descripción**: La base de datos SQL puede ser suplantada por un atacante, lo que podría llevar a que se entreguen datos incorrectos a la Máquina Virtual. Considere usar un mecanismo de autenticación estándar para identificar el almacén de datos de origen.

El informe demuestra que la conexión hacia Internet (la que cruza el *boundary* hacia el Cloud Storage) es la que "posiblemente más fallos de seguridad nos puede ofrecer" y presenta "muchas más posibilidades de que sufra algún tipo de problema de seguridad".

### 4.3. Propuestas de Mejora

Para mitigar los fallos de seguridad detectados, las mejoras fundamentales serían:

  * **Transición a HTTPS**: La mejora más crítica es **reemplazar todas las conexiones HTTP por HTTPS**. HTTPS cifra el tráfico, lo que protege contra la divulgación de información y la manipulación de datos en tránsito. Esto abordaría directamente las amenazas de *Information Disclosure* y *Tampering*.
  * **Implementación de Controles de Acceso Estrictos**: Asegurar que solo las entidades autorizadas puedan acceder a la VM, SQL DB y Cloud DB.
  * **Autenticación Robusta**: Utilizar mecanismos de autenticación fuertes para todas las comunicaciones, especialmente para identificar los almacenes de datos y procesos de origen/destino y evitar *Spoofing*.
  * **Manejo de Consumo de Recursos**: Implementar pasos explícitos para controlar el consumo de recursos en la VM y las bases de datos, asegurando *timeouts* y evitando *deadlocks* para prevenir ataques de *Denial of Service*.
  * **Monitoreo y Registro (Logging & Monitoring)**: Implementar sistemas de monitoreo para detectar actividades sospechosas y registrar eventos para análisis forense, especialmente para contrarrestar la **Repudiation**.
  * **Validación de Entradas**: Asegurar que todas las entradas de datos sean validadas para prevenir ataques de inyección, como la **SQL Injection**.
  * **Segmentación de Red y *Firewalls***: Utilizar *firewalls* y segmentación de red para aislar componentes y limitar el alcance de un posible compromiso, lo que ayuda a prevenir interrupciones del flujo de datos o inaccesibilidad del *datastore* por agentes externos.

La herramienta de Threat Modeling no solo nos mostrará los fallos, sino que también nos permitirá documentarlos y priorizarlos para su corrección, siendo un paso clave en el ciclo de vida de desarrollo de la seguridad.

## 5\. Conclusión del Ejercicio

El ejercicio realizado resalta la efectividad de la Microsoft Threat Modeling Tool para fortalecer la seguridad de una arquitectura. Permite comprender la importancia de las medidas de seguridad preventivas y aplicar técnicas de modelado de amenazas de una manera práctica, sencilla, rápida y escalable. Esto es fundamental para identificar y abordar fallos de seguridad, mejorando la **resiliencia** de nuestros sistemas frente a las **ciberamenazas**.

-----