Documentos de Referencia: "FSL Clase 23 – Herramientas de Auditoría - Lynis - OpenVAS.pdf"

# Informe Técnico: Herramientas de Auditoría de Seguridad - Lynis y OpenVAS

### 1. Resumen Ejecutivo

Este informe técnico se centra en el uso de herramientas de auditoría de seguridad, con un enfoque en **Lynis** y **OpenVAS**. Se explican los conceptos fundamentales de una auditoría de seguridad y la importancia de estas herramientas en la fortificación de sistemas GNU/Linux. Se detalla la instalación, ejecución y análisis de resultados de **Lynis** como un analizador de configuración, y se presenta a **OpenVAS** como una herramienta esencial para el escaneo de vulnerabilidades. El informe también describe los procedimientos para generar reportes en HTML con **Lynis** y el proceso para iniciar y utilizar la interfaz gráfica de **OpenVAS**. El objetivo es proporcionar una guía completa y didáctica para la realización de auditorías de seguridad en entornos de servidores.

***

### 2. Conceptos Fundamentales

* **Auditoría de Seguridad:** Una auditoría de seguridad es un proceso sistemático y exhaustivo para evaluar la seguridad de un sistema informático. Este proceso implica el análisis de sus componentes, incluyendo configuraciones, archivos de registro, permisos, usuarios y servicios.
    * **Objetivos:** Los objetivos principales de una auditoría son identificar vulnerabilidades y riesgos, verificar el cumplimiento de políticas y estándares, detectar intrusiones, facilitar la respuesta a incidentes y mejorar la eficiencia del sistema.

* **Herramientas de Auditoría:** Son programas de software diseñados para automatizar la evaluación de la seguridad y el cumplimiento de los sistemas. Se utilizan para identificar vulnerabilidades, detectar configuraciones incorrectas y evaluar el estado de seguridad de manera automática.
    * **Tipos de herramientas:**
        * **Escáneres de Vulnerabilidades:** Buscan y reportan debilidades en sistemas o aplicaciones, como OpenVAS o Nessus.
        * **Analizadores de Configuración:** Revisan la configuración del sistema para detectar errores y riesgos, como **Lynis**.
        * **Detectores de Intrusiones:** Vigilan el tráfico de red para detectar actividades sospechosas, como Snort o Suricata.
    * **Ventajas:** Las herramientas de auditoría ofrecen ventajas como el ahorro de tiempo, mayor precisión, escalabilidad, la actualización constante de sus bases de datos y la capacidad de generar documentación detallada.

* **Lynis:** Es una herramienta de código abierto para realizar auditorías de seguridad en sistemas GNU/Linux. Su objetivo es identificar vulnerabilidades, configuraciones incorrectas y áreas de mejora en la seguridad de un sistema.
    * **Características:** Realiza un escaneo exhaustivo del sistema, cubre más de 100 chequeos, genera informes detallados con recomendaciones, permite personalización de las pruebas y es compatible con una gran cantidad de distribuciones.

* **OpenVAS (Open Vulnerability Assessment Scanner):** Una herramienta de código abierto para el escaneo de vulnerabilidades y pruebas en sistemas y redes. Es eficaz para encontrar vulnerabilidades conocidas y fallos de configuración.
    * **Características:** Ofrece escaneos exhaustivos, posee una amplia base de conocimiento que se actualiza constantemente, genera informes detallados y permite personalizar los escaneos.

***

### 3. Procedimientos Prácticos

#### 3.1. Instalación y Uso de Lynis en Ubuntu

1.  **Instalación:**
    * Para sistemas basados en Debian/Ubuntu, se utiliza el gestor de paquetes `apt`.
    * **Comando:** `sudo apt install lynis`.
    * **Explicación:** Se ejecuta con `sudo` para obtener los permisos de administrador necesarios para instalar el paquete `lynis`. Alternativamente, para otras distribuciones, se recomienda clonar el repositorio de GitHub.

2.  **Visualización de la ayuda:**
    * **Comando:** `lynis help`.
    * **Explicación:** Este comando muestra la ayuda de la herramienta, incluyendo su sintaxis básica (`lynis command [options]`) y los comandos disponibles como `audit`, `show` y `update`.

3.  **Ejecución de una auditoría local completa:**
    * **Comando:** `sudo lynis audit system`.
    * **Explicación:** El comando `audit system` realiza un escaneo de seguridad local. `sudo` es necesario porque se requieren permisos de administrador para escanear el sistema de manera exhaustiva. La herramienta mostrará los resultados de los chequeos categorizados por secciones (ej., `Boot and services`, `Kernel`, `Users, Groups and Authentication`), usando un sistema de semáforos de colores (verde para `OK`, amarillo para `Suggestions` y rojo para `Warnings` o `Unsafe`), tal como se muestra en la captura de pantalla.

4.  **Generación de un reporte en HTML:**
    * **Comando:** `lynis audit system | ansi2html -l > report.html`.
    * **Explicación:** Se utiliza un **pipeline** (`|`) para redirigir la salida del comando `lynis audit system` a la herramienta `ansi2html`. `ansi2html` convierte el texto con colores (`ANSI`) de la terminal a formato HTML. El resultado se guarda en un archivo llamado `report.html` mediante la redirección de salida (`>`). Este archivo HTML puede ser abierto en un navegador web para una visualización más detallada y ordenada, facilitando la creación de informes, como se muestra en la captura de pantalla.

5.  **Verificación de la versión:**
    * **Comando:** `lynis update info`.
    * **Explicación:** Este comando muestra información sobre la versión instalada de **Lynis** y la versión más reciente disponible, indicando si la aplicación está obsoleta (`Outdated`).

#### 3.2. Uso de OpenVAS en Kali Linux

1.  **Inicio del servicio:**
    * **Comando:** `gvm-start`.
    * **Explicación:** Este comando inicia el servicio de **OpenVAS** (`gvm-start`), el cual se ejecuta localmente y abre una interfaz web en un puerto específico (ej. `https://127.0.0.1:9392`) para acceder a la herramienta. Las credenciales de acceso se generan durante la instalación y es importante guardarlas.

2.  **Navegación en la interfaz web:**
    * **Descripción:** La interfaz de **OpenVAS** presenta un **dashboard** con un resumen de los escaneos realizados, incluyendo gráficos de severidad y número de vulnerabilidades (CVEs) clasificadas.
    * En la pestaña `Scans`, se puede ver un resumen de las tareas lanzadas, con su estado y severidad. Se puede acceder a los informes generados en la subsección `Reports`, donde se muestra un desglose de los hallazgos por severidad. En la subsección `Results`, se obtiene información detallada de cada vulnerabilidad, incluyendo el host, puerto, protocolo, una descripción, el método de detección y posibles soluciones, como se observa en la captura de pantalla.

3.  **Lanzamiento de un nuevo escaneo:**
    * **Descripción:** Para lanzar un nuevo escaneo, se puede ir a la pestaña `Scans` y hacer clic en `New Task` para una configuración avanzada, o utilizar el `Task Wizard` para un escaneo más rápido.
    * El asistente permite ingresar una dirección IP (por ejemplo, `127.0.0.1` para escanear el propio sistema) y lanzar el escaneo inmediatamente. El estado del escaneo se actualiza en la lista de tareas, mostrando su progreso.

***

### 4. Conclusiones y Puntos Clave

* **Importancia y Beneficios de Seguridad:** Las auditorías de seguridad son procesos esenciales para mantener la seguridad y el correcto funcionamiento de los sistemas GNU/Linux. Al usar herramientas automatizadas, los administradores pueden identificar y mitigar proactivamente riesgos y vulnerabilidades, ahorrando tiempo y recursos. Esto contribuye a una mejora continua de la seguridad y garantiza el cumplimiento de normativas y políticas internas o externas. Realizar estas auditorías de forma regular permite medir la evolución de la seguridad del sistema a lo largo del tiempo.

* **Puntos de Aprendizaje Clave:**
    * Se ha comprendido qué es una auditoría de seguridad y por qué es vital para los sistemas GNU/Linux.
    * Se han diferenciado los tipos de herramientas de auditoría (analizadores de configuración, escáneres de vulnerabilidades, detectores de intrusiones) y sus ventajas.
    * Se ha aprendido a instalar y utilizar **Lynis** para realizar auditorías de seguridad locales, interpretar sus resultados y generar informes en HTML de forma sencilla.
    * Se ha explorado **OpenVAS** como una herramienta más compleja y potente para el escaneo exhaustivo de vulnerabilidades, y se ha visto cómo su interfaz gráfica ofrece una gran cantidad de información visual y detallada para la identificación y mitigación de problemas de seguridad.

* **Relevancia Técnica:** Los procedimientos aprendidos son altamente relevantes en entornos profesionales. El uso de **Lynis** es ideal para auditorías regulares y la verificación de la configuración en entornos de desarrollo y producción. **OpenVAS** es la herramienta recomendada para escaneos exhaustivos de vulnerabilidades en sistemas en red y entornos críticos, así como para cumplir con requisitos de cumplimiento. La elección entre estas herramientas dependerá de las necesidades específicas, los requisitos de seguridad y las capacidades del equipo. Saber cómo utilizar estas herramientas permite a los profesionales de la seguridad y a los administradores de sistemas mantener los servidores fortificados y seguros.