Documentos de Referencia: "AWEB - Introducción y Teoría.pdf"

# Informe Técnico: Ataques en Auditorías de Aplicaciones Web y Estrategias de Defensa

## 1. Resumen Ejecutivo
Este informe técnico aborda las auditorías de seguridad en aplicaciones web, introduciendo conceptos de hacking ético y metodologías de evaluación. Se centra en la organización **OWASP** y sus recursos clave, como entornos de laboratorio y *proxies* para el análisis de tráfico. Se describen diversas categorías de vulnerabilidades comunes, como fallos de autenticación, fallos de autorización y la validación de entradas, que son explotadas por los atacantes y auditadas por los profesionales de la seguridad para mejorar la postura defensiva de una organización.

---

## 2. Conceptos Fundamentales

### OWASP
**OWASP** (Open Worldwide Application Security Project) es una comunidad global sin fines de lucro dedicada a mejorar la seguridad del *software*. Proporciona recursos abiertos y gratuitos, como metodologías, herramientas y guías, para ayudar a los desarrolladores y a los profesionales de la seguridad a construir y evaluar aplicaciones seguras. 
### Entornos de Laboratorio
Para practicar la auditoría de aplicaciones web y el *hacking* ético de forma segura, se utilizan entornos de laboratorio vulnerables de forma intencionada. Algunos de los entornos más comunes y recomendados en la industria son:
* **DVWA (Damn Vulnerable Web Application)**: Una aplicación web con vulnerabilidades intencionadas diseñada para ayudar a los profesionales a probar sus habilidades.
* **Web for Pentester**: Un entorno de laboratorio enfocado en la prueba de penetración web.
* **Juice Shop**: Una aplicación web de comercio electrónico intencionalmente insegura utilizada para la formación en ciberseguridad.

### Proxies de Interceptación
Un **proxy** de interceptación es una herramienta fundamental en las auditorías de seguridad web. Permite a los profesionales capturar, inspeccionar y modificar el tráfico entre el navegador y el servidor web. La herramienta de *proxy* más popular es **Burp Suite**, que facilita el análisis de peticiones y respuestas **HTTP/HTTPS** para identificar fallos de seguridad.

### Categorías de Vulnerabilidades
La auditoría de aplicaciones web se enfoca en la detección de fallos en varias categorías, que incluyen:
* **Fallas de Autenticación**: Vulnerabilidades que permiten a un atacante eludir los controles de autenticación, como la fuerza bruta de contraseñas o el robo de credenciales.
* **Fallas de Autorización**: Fallos que permiten a un usuario acceder a recursos o a funcionalidades para las que no tiene permiso.
* **Fallas de Validación de Entradas**: Debilidades que se producen cuando la aplicación no valida, filtra o sanea las entradas de los usuarios de forma adecuada, lo que puede dar lugar a ataques como la inyección **SQL** o el *Cross-Site Scripting* (**XSS**).
* **Fallas de Configuración del Servidor**: Configuración incorrecta del servidor web, del servidor de aplicaciones o de otros componentes, que pueden exponer datos sensibles o permitir el acceso no autorizado.
* **Divulgación de Información**: Exposición de información sensible, como errores detallados, datos de configuración o código fuente.
* **Criptografía Débil**: Uso de algoritmos de cifrado obsoletos, contraseñas mal almacenadas o fallas en la gestión de claves, lo que hace que los datos sensibles sean vulnerables.

---

## 3. Procedimientos Prácticos

### 1. Preparación del Entorno
Antes de comenzar la auditoría, el profesional debe configurar su entorno de trabajo:
* **Elección de la herramienta**: Se debe seleccionar una herramienta de *proxy* como **Burp Suite** para interceptar el tráfico web.
* **Configuración del *proxy***: Se configura el navegador para que dirija todo su tráfico a través del *proxy* de la herramienta. Esto permite al auditor ver cada petición y respuesta entre el cliente y el servidor.
* **Acceso al laboratorio**: El auditor accede a uno de los entornos de laboratorio vulnerables, como **DVWA** o **Juice Shop**, para comenzar la evaluación.

### 2. Metodología de Auditoría
El proceso de auditoría generalmente sigue una metodología estructurada:
* **Reconocimiento**: Se recopila información sobre la aplicación, su arquitectura, sus tecnologías y sus puntos de entrada.
* **Análisis de vulnerabilidades**: Se utiliza el *proxy* para inspeccionar el tráfico y se analizan las peticiones y respuestas para encontrar fallos de seguridad en las categorías mencionadas (autenticación, autorización, validación de entradas, etc.).
* **Explotación (opcional)**: Si el objetivo de la auditoría es el *hacking* ético, se intentan explotar las vulnerabilidades encontradas para demostrar el impacto potencial de un ataque. Por ejemplo, si se encuentra una falla de validación de entradas, se podría intentar inyectar código para obtener información de la base de datos.
* **Informes**: El auditor documenta todas las vulnerabilidades encontradas, su impacto, y recomendaciones para mitigarlas.

### 3. Técnicas de Explotación
En la fase de explotación, un auditor podría aplicar técnicas como:
* **Inyección de SQL**: Insertar código malicioso en una consulta **SQL** a través de una entrada de usuario para obtener información o manipular la base de datos.
* **Fuerza Bruta**: Intentar adivinar credenciales de acceso a través de un diccionario de contraseñas.
* **Escalada de Privilegios**: Aprovechar una falla de autorización para acceder a un recurso restringido.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
Las auditorías de aplicaciones web son una parte crítica del ciclo de vida del desarrollo de *software* seguro. Al identificar y remediar las vulnerabilidades antes de que sean explotadas por atacantes maliciosos, las organizaciones pueden proteger sus datos, su reputación y la confianza de sus usuarios. Herramientas y recursos de **OWASP** permiten a los profesionales realizar estas evaluaciones de manera sistemática y efectiva.

### Puntos de Aprendizaje Clave
* **El uso de herramientas**: Dominar herramientas como **Burp Suite** es esencial para cualquier profesional que se dedique a la auditoría web. El *proxy* de interceptación es el "laboratorio" donde se diseccionan los ataques.
* **La importancia de la validación**: Muchos de los ataques más comunes se basan en fallos de validación de entradas. Un auditor debe aprender a pensar como un atacante para identificar dónde la aplicación confía ciegamente en las entradas del usuario.
* **La disciplina metodológica**: La auditoría no es una tarea aleatoria. Seguir una metodología estructurada, como las guías de **OWASP**, asegura que la evaluación sea exhaustiva y no se pasen por alto las vulnerabilidades.

### Relevancia Técnica
El conocimiento de las técnicas de auditoría web y la familiaridad con los recursos de **OWASP** son habilidades de alta demanda en el mercado laboral de la ciberseguridad. Son fundamentales para los roles de *pentester*, analista de seguridad y desarrollador de *software* seguro. El dominio de estas habilidades permite a los profesionales proteger activamente las aplicaciones web contra una amplia gama de amenazas.

---

Documentos de Referencia: "AWEB - Introducción y Teoría .pdf"

# Informe Técnico: Introducción a la Auditoría de Aplicaciones Web y Metodologías de Seguridad

## 1. Resumen Ejecutivo
Este informe técnico proporciona una visión general del *hacking* y las auditorías de aplicaciones web. Se presenta a la organización **OWASP** como la principal entidad de referencia y se detalla una metodología de auditoría en cuatro fases: **planificación**, **enumeración**, **explotación** e **informe**. Además, se describen seis categorías principales de vulnerabilidades web, desde fallos de configuración hasta criptografía débil, y se introduce el sistema **CVSS** como herramienta para medir la criticidad de los hallazgos. El documento resalta la importancia de adoptar un enfoque metódico para garantizar una revisión de seguridad exhaustiva y eficaz.

---

## 2. Conceptos Fundamentales

### Auditorías Web
Una auditoría web es un ejercicio de ciberseguridad diseñado para encontrar el mayor número posible de vulnerabilidades en una aplicación web en un tiempo limitado. El objetivo es realizar una evaluación exhaustiva y entregar un informe que documente los hallazgos sin falsos positivos. Las auditorías combinan el uso de herramientas automáticas con pruebas manuales para obtener resultados más completos.

### Tipos de Auditoría
El enfoque de una auditoría web varía según los objetivos del cliente y se clasifica en tres tipos principales:
* **Caja Blanca (White Box)**: Simula un ataque interno, con conocimiento completo de la aplicación, el código fuente, los componentes, etc..
* **Caja Negra (Black Box)**: Simula un ataque completamente externo, sin ningún conocimiento previo de la aplicación, excepto la URL de inicio.
* **Caja Gris (Grey Box)**: Es el tipo más común. Proporciona un punto de partida con información básica, como credenciales de usuario y acceso a diferentes roles, para simular un ataque que sea lo más completo posible dentro de un tiempo acotado.

### OWASP (Open Web Application Security Project)
**OWASP** es una organización sin ánimo de lucro dedicada a mejorar la seguridad del *software* de código abierto. Su misión es hacer visible la seguridad de las aplicaciones. Proporciona una guía integral para probar la seguridad de las aplicaciones web, conocida como **OWASP Web Security Testing Guide (WSTG)**, que es la metodología recomendada para realizar auditorías web.

### Vulnerabilidades Web
El documento clasifica las vulnerabilidades en seis tipologías principales:
* **Divulgación de Información (`Information disclosure`)**: Exposición de datos internos sobre el objetivo, como la versión de componentes o detalles de configuración que pueden ser aprovechados por un atacante.
* **Configuración del Servidor (`Server configuration`)**: Fallos en la configuración por defecto o en la gestión de errores del servidor que pueden revelar información sensible o dar ventajas a un atacante.
* **Fallas de Autenticación (`Authentication failures`)**: Problemas en el proceso de inicio de sesión que permiten a un atacante saltarse la autenticación, como el uso de credenciales por defecto o la vulnerabilidad de las credenciales.
* **Fallas de Autorización (`Authorization failures`)**: Un usuario puede acceder a recursos o realizar operaciones para las que no tiene permisos, lo que le permite ver información de otros usuarios o elevar privilegios.
* **Validación de Entradas (`Input validation`)**: Inyecciones de código que se producen cuando los datos enviados por el cliente no se procesan, validan o sanean correctamente. Aquí se incluyen vulnerabilidades como **SQL Injection**, **Cross-Site Scripting (XSS)** y **Command Injection**.
* **Criptografía Débil (`Weak Cryptography`)**: Fallos en el cifrado de datos sensibles, como el uso de algoritmos obsoletos o el envío de información sin cifrar, lo que compromete la confidencialidad de la información.

### Common Vulnerability Scoring System (CVSS)
El **CVSS** es un sistema estándar para medir la criticidad de una vulnerabilidad. La puntuación se mide en una escala de 0 a 10, donde un número más alto indica una mayor criticidad. La versión 3.0 del **CVSS** divide la puntuación en cinco categorías de severidad: **None** (0.0), **Low** (0.1-3.9), **Medium** (4.0-6.9), **High** (7.0-8.9) y **Critical** (9.0-10.0). Para el cálculo, se tienen en cuenta tres grupos de métricas: **base**, **temporal** y **de entorno**.

---

## 3. Procedimientos Prácticos

### Fases de una Auditoría Web
Una auditoría web se organiza en cuatro fases principales:

1.  **Planificación (`Planning`)**: Es la fase inicial y más crítica. Se establecen los acuerdos con el cliente, se define el alcance, las fechas, los objetivos y si la auditoría será de caja blanca, gris o negra. También se designa una persona de contacto para resolver imprevistos.
2.  **Enumeración (`Enumeration`)**: Se recopila información sobre el objetivo mediante la búsqueda activa y pasiva. Se utiliza **OSINT** (Open Source Intelligence) para encontrar datos expuestos o pistas que puedan conducir a vulnerabilidades. Se identifican puntos de la aplicación que interactúan con el usuario, como formularios de inicio de sesión o de contacto.
3.  **Explotación (`Exploitation`)**: Es la fase más larga y central de la auditoría. Aquí se realizan pruebas para confirmar y explotar las vulnerabilidades identificadas. Se usan herramientas y *scripts* especializados para la detección y explotación, y se recopilan evidencias de cada hallazgo. Si se encuentra una vulnerabilidad de alta criticidad, es común reportarla de inmediato.
4.  **Informe (`Report`)**: La fase final y de vital importancia. El informe documenta todo el trabajo realizado y se divide en dos partes:
    * **Informe Ejecutivo**: Un resumen de alto nivel con los principales riesgos detectados, dirigido a un público no técnico.
    * **Informe Técnico**: Un documento detallado para desarrolladores y personal técnico, que explica las vulnerabilidades encontradas, su ubicación, las evidencias y las recomendaciones para su corrección, de forma que sean replicables.

### Metodologías de Pentesting
Además de la guía de **OWASP**, el documento hace referencia a otras metodologías para la organización de pruebas de penetración:
* **OSSTMM**: Un manual de código abierto que divide la auditoría en 7 fases genéricas, desde el lanzamiento del proyecto hasta la resolución de deficiencias.
* **PTES**: Un estándar que se centra en los ejercicios de *pentesting* y los divide también en 7 fases, que van desde las interacciones previas hasta la post-explotación.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
Las auditorías web son esenciales para garantizar la seguridad de las aplicaciones que usamos a diario, protegiendo tanto los datos de las empresas como los de los usuarios. Al seguir una metodología estructurada, los profesionales de la seguridad pueden identificar sistemáticamente las debilidades y proporcionar información valiosa para fortalecer las defensas de un sistema.

### Puntos de Aprendizaje Clave
* **Enfoque personalizado**: El análisis de una aplicación web debe ser personalizado en función de sus funcionalidades. Por ejemplo, no tiene sentido buscar vulnerabilidades de autenticación si la aplicación no tiene un formulario de inicio de sesión.
* **El poder del informe**: Un informe de auditoría bien elaborado es tan importante como el trabajo técnico en sí. Refleja la calidad de la auditoría y permite al cliente entender los hallazgos y las acciones correctivas necesarias.
* **La experiencia es clave**: Aunque existen guías y herramientas de apoyo, la experiencia del auditor es crucial para identificar vulnerabilidades complejas y elegir las técnicas de prueba más adecuadas.

### Relevancia Técnica
Para un profesional de la ciberseguridad, el dominio de una metodología de auditoría es fundamental. Permite organizar el trabajo de forma eficiente, documentar los hallazgos de manera profesional y comunicar los riesgos de forma clara. La familiaridad con los proyectos de **OWASP**, como el **WSTG** y el **Top 10**, proporciona una base sólida para realizar auditorías de seguridad en cualquier aplicación web.