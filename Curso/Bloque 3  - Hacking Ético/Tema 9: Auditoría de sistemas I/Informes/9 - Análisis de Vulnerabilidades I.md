Documentos de Referencia: "AS-I - Análisis de Vulnerabilidades: Clasificación, Corporaciones y Conceptos.pdf"

# Informe Técnico: Conceptos, Clasificación y Categorización de Vulnerabilidades

## 1. Resumen Ejecutivo
Este informe técnico profundiza en los conceptos fundamentales del análisis de vulnerabilidades. Se diferencia entre software seguro y confiable, y se definen términos clave como `bug`, `vulnerability`, `zero-day` y `bug bounty`. El documento clasifica y explica los diferentes tipos de `malware`, incluyendo `ransomware`, `virus`, `gusanos` y `troyanos`. Además, se detallan las organizaciones de estandarización más importantes a nivel global, como **NIST**, **MITRE** y **FIRST**, y se describen sus estándares, como **CVE**, **CPE**, **CVSS** y **CWE**. Finalmente, se explican los pasos para registrar una vulnerabilidad y se presentan recursos útiles para la investigación de vulnerabilidades.

---

## 2. Conceptos Fundamentales

### 2.1. Seguridad vs. Fiabilidad
* **Software Confiable (`Reliable`):** Es un software que cumple su propósito, se ejecuta sin errores inesperados y mantiene la integridad de los datos y la funcionalidad del sistema.
* **Software Seguro (`Secure`):** Cumple lo que hace el software confiable y nada más. Resiste ataques, protege contra accesos no autorizados y minimiza las vulnerabilidades que pueden ser explotadas por actores maliciosos. La fuente de inseguridades, vulnerabilidades y riesgos a menudo proviene de las funcionalidades adicionales, no esenciales, conocidas como "algo más".

### 2.2. Bugs y Vulnerabilidades
* **Bug:** En el contexto de la ciberseguridad, un `bug` es un error o defecto en el software que puede ser explotado por un atacante para obtener acceso no autorizado a un sistema o red. Los `bugs` son causados por errores en el código, la configuración o el diseño. No todos los `bugs` son vulnerabilidades; puede haber `bugs` en la lógica o visuales que no deriven en una vulnerabilidad.
* **Vulnerabilidad:** Una debilidad en un sistema, sus procedimientos de seguridad, controles internos o implementación que podría ser explotada por una amenaza. La vulnerabilidad de **Heartbleed**, descubierta en abril de 2014 en OpenSSL, permitía a un atacante leer la memoria del servidor o cliente, obteniendo acceso a información confidencial.
* **Zero-Day:** Una vulnerabilidad de software que es desconocida para el proveedor, quien ha tenido "0 días" para corregirla antes de ser explotada. Son vulnerabilidades no conocidas, difíciles de detectar y para las que no existen parches o firmas de virus disponibles, por lo que son altamente explotables. Un ejemplo de `zero-day` fue la vulnerabilidad **CVE-2017-0144** en el protocolo SMB de Microsoft.

### 2.3. Bug Bounty
Un `bug bounty` es un programa de seguridad colaborativo donde una organización ofrece una recompensa a los investigadores por encontrar y reportar vulnerabilidades en sus sistemas. Las principales plataformas son HackerOne y Bugcrowd.
* **Beneficios:** Las empresas mejoran su seguridad, aumentan la confianza de los usuarios y reducen costes. Los investigadores ganan dinero, prestigio y conocimiento.
* **Recompensas:** Según un informe de HackerOne, la recompensa promedio es de **$3.700**, con el percentil 90 alcanzando los **$12.000**. Las recompensas más altas se encuentran en los sectores de criptomonedas y `blockchain` (hasta 100 mil dólares) y servicios en línea (hasta 21 mil dólares).

### 2.4. Exploit
Un `exploit` es una pieza de software, un conjunto de datos o una secuencia de comandos que aprovecha una vulnerabilidad para causar un comportamiento no intencionado. El `payload` es la carga útil de un `exploit`, el código que se ejecuta para realizar una acción maliciosa, como robar datos o instalar `malware`. Un ejemplo es en un `buffer overflow`, donde el `exploit` desborda el búfer y el `payload` inyecta una `shell`. ExploitDB es una base de datos pública de `exploits` de código abierto.

### 2.5. Malware
`Malware` es cualquier software diseñado intencionadamente para dañar o infiltrarse en un sistema sin el consentimiento del usuario.
* **Ransomware:** Cifra los datos de la víctima y exige un rescate a cambio de la clave de descifrado. Hay dos tipos: el que cifra archivos y el que bloquea la pantalla.
* **Virus:** Un programa malicioso que se autorreplica, infectando otros archivos o sistemas. Su objetivo es robar información, dañar archivos o molestar.
* **Gusanos (`Worms`):** `Malware` independiente que se replica automáticamente a través de la red, explotando vulnerabilidades para infectar tantos dispositivos como sea posible. El gusano Morris de 1988 infectó al 10% de los servidores de la red ARPANET.
* **Troyanos (`Trojans`):** `Malware` que se disfraza como un programa legítimo para engañar a los usuarios y que lo instalen. Una vez instalado, puede dar a los atacantes acceso remoto, permitiendo el robo de datos o la instalación de otro `malware`.

---

## 3. Organizaciones y Estándares de Estandarización
Para clasificar y categorizar las vulnerabilidades a nivel mundial, existen diversas organizaciones y estándares.

### 3.1. NIST (National Institute of Standards and Technology)
Es una agencia del gobierno de EE. UU. que desarrolla y promueve estándares, medidas y tecnologías para la seguridad de la información.
* **CPE (Common Platform Enumeration):** Un sistema de nomenclatura estandarizado para identificar software, hardware y sistemas de TI. Aunque fue creado por MITRE, NIST mantiene una versión autorizada de la base de datos. La especificación **CPE 2.3** separa los componentes con dos puntos y representa los valores desconocidos con asteriscos. La base de datos, en formato XML, puede ser utilizada en aplicaciones de visualización y enumeración.
* **NVD (National Vulnerability Database):** La base de datos oficial de vulnerabilidades del gobierno de EE. UU., gestionada por el NIST, que contiene información sobre vulnerabilidades conocidas.

### 3.2. MITRE
Organización sin fines de lucro que lidera el desarrollo de taxonomías y herramientas para la gestión de vulnerabilidades.
* **CVE (Common Vulnerabilities and Exposures):** Un diccionario de identificadores únicos y estandarizados para vulnerabilidades conocidas. El CVE-ID está compuesto por las siglas `CVE`, el año de registro y un número secuencial de 4 o más dígitos. Las **CNA (CVE Numbering Authorities)** son entidades acreditadas que asignan nuevos CVE. La base de datos es pública y se puede descargar.
* **CWE (Common Weakness Enumeration):** Un catálogo de debilidades de software y hardware comunes que pueden llevar a vulnerabilidades. MITRE publica anualmente una lista de las 25 debilidades más peligrosas. Este estándar es jerárquico y útil para documentar y validar la seguridad de sistemas.
* **CAPEC (Common Attack Pattern Enumeration and Classification)::** Un catálogo de patrones de ataques comunes que se utiliza para clasificar y analizar vulnerabilidades. La lista de CAPEC se puede navegar por mecanismos o dominios de ataque, como "ingeniería social" o "seguridad física".

### 3.3. FIRST (Forum of Incident Response and Security Teams)
Organización sin ánimo de lucro que reúne a equipos de respuesta a incidentes de seguridad de todo el mundo.
* **CVSS (Common Vulnerability Scoring System):** Un estándar abierto que califica la severidad de las vulnerabilidades en una escala del 0 al 10. La versión 4.0 se compone de cuatro grupos de métricas: **Base**, **Temporal**, **Ambiental** y **Suplementarias**.

### 3.4. CERT (Computer Emergency Response Team)
Los CERT son equipos de respuesta a emergencias informáticas que gestionan y responden a incidentes de seguridad. El primer CERT se creó en 1988 como respuesta al gusano Morris. En España, el **INCIBE-CERT** es el centro de respuesta a incidentes de referencia para ciudadanos y empresas.

### 3.5. OWASP
**OWASP (Open Web Application Security Project):** es una comunidad global sin fines de lucro dedicada a la seguridad de aplicaciones web.
* **OWASP Top 10:** El proyecto más famoso de OWASP, que cataloga los 10 riesgos de seguridad más críticos en aplicaciones web y se actualiza cada cuatro años. El informe de 2021 destaca vulnerabilidades como el **Broken Access Control**, los **Cryptographic Failures** y las **Security Misconfigurations**. También se incluyeron fallos de diseño, en la integridad de datos y el **Server-Side Request Forgery (SSRF)**.

---

## 4. Recursos para la Investigación de Vulnerabilidades
Existen múltiples recursos para buscar y procesar información sobre vulnerabilidades.
* **NVD:** La base de datos oficial del NIST, que permite descargar su contenido completo o utilizar APIs para la automatización.
* **CVEsearch:** Una herramienta de código abierto que permite importar bases de datos de CVE y CPE a una base de datos local MongoDB para realizar búsquedas y procesar datos con mayor flexibilidad.
* **CVE Details:** Un sitio web que presenta las vulnerabilidades de una manera visual y organizada, permitiendo filtrar por tipo, fecha, producto y vendedor.

---

## 5. Conclusiones y Puntos Clave
* Se ha comprendido la distinción entre software seguro y confiable, y la importancia de eliminar funcionalidades no esenciales para reducir los riesgos de seguridad.
* Se ha aprendido que un `bug` puede ser una vulnerabilidad, pero no siempre es así, y se han diferenciado conceptos como `zero-day` y `exploit`.
* Se ha explorado la estructura y el propósito de las organizaciones de estandarización como NIST, MITRE y FIRST, y de las bases de datos y estándares que mantienen, incluyendo CVE, CPE, CVSS y CWE.
* Se ha entendido cómo los diferentes estándares se interrelacionan: una **CVE** se asocia a un **CWE** que se puntúa con **CVSS** y afecta a un sistema identificado con un **CPE**, lo cual es aprovechado por un patrón de ataque **CAPEC**.
* Se ha visto que el registro de una vulnerabilidad es un proceso formal que requiere contactar a una **CNA** y proporcionar información detallada sobre el producto, la versión, el tipo y el impacto de la vulnerabilidad.
* Se han identificado recursos valiosos para la investigación de vulnerabilidades, como NVD, CVEsearch y CVE Details.