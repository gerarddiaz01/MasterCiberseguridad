Aquí tienes un informe detallado sobre **OWASP**, utilizando la información de los pantallazos proporcionados y siguiendo la estructura de formato Markdown.

---

# OWASP: Un Pilar Fundamental en la Seguridad del Software y Aplicaciones Web

Este informe profundiza en la **OWASP (Open Web Application Security Project)**, una organización de gran relevancia en el ámbito de la ciberseguridad. Se explicará qué es OWASP, sus características clave, sus contribuciones al **hardening** de la red, y se presentarán sus principales listas de riesgos, incluyendo el **OWASP Top 10** y el **OWASP Top 10 API Security Risks**.

## 1. ¿Qué es OWASP?

**OWASP**, o **The Open Web Application Security Project**, es una **organización impulsada por la comunidad** que se enfoca en **mejorar la seguridad del software**. Proporciona **recursos, herramientas y directrices** para ayudar a las organizaciones a mejorar la postura de seguridad de sus aplicaciones web y redes.

Las contribuciones de OWASP juegan un **papel crucial en el hardening de la red** al:
* Identificar vulnerabilidades comunes.
* Promover las mejores prácticas.
* Facilitar el desarrollo de soluciones de software seguro.
* Reducir en última instancia el riesgo de **ciberataques** y **Data Leaks**.

### 1.1. Características Clave de OWASP

OWASP se destaca por varias características que la convierten en una referencia fundamental en la seguridad de aplicaciones:
* **Referencia Autorizada**: Es una fuente fiable y reconocida en la industria de la ciberseguridad.
* **Enfoque Proactivo**: Fomenta una aproximación anticipada a la seguridad, buscando identificar y mitigar riesgos antes de que sean explotados.
* **Recursos Prácticos**: Ofrece una amplia gama de herramientas, documentación y guías que son directamente aplicables por desarrolladores y profesionales de la seguridad.
* **Comunidad Colaborativa**: Su fuerza reside en su naturaleza de *código abierto* y su comunidad global de expertos que colaboran en proyectos y conocimientos.
* **Adaptabilidad y Evolución**: Se mantiene al día con las nuevas amenazas y tecnologías, actualizando constantemente sus recursos y listas de riesgos.

## 2. OWASP Top 10: Los Riesgos Críticos de Seguridad en Aplicaciones Web

El **OWASP Top 10** es un informe estándar de concientización para desarrolladores y seguridad de aplicaciones web. Representa un consenso de los riesgos de seguridad más críticos para las aplicaciones web.

### 2.1. Comparativa 2017 vs. 2021

La evolución del OWASP Top 10 refleja los cambios en el panorama de amenazas y vulnerabilidades. A continuación, se presenta una tabla comparativa de las listas de 2017 y 2021:

| OWASP Top 10 - 2017                   | OWASP Top 10 - 2021                             | Categoría Nueva (2021)   |
| :------------------------------------ | :---------------------------------------------- | :----------------------- |
| A01:2017-Injection                    | A01:2021-Broken Access Control                  |                          |
| A02:2017-Broken Authentication        | A02:2021-Cryptographic Failures                 |                          |
| A03:2017-Sensitive Data Exposure      | A03:2021-Injection                              |                          |
| A04:2017-XML External Entities (XXE)  | **[New]** A04:2021-Insecure Design              | Insecure Design          |
| A05:2017-Broken Access Control        | A05:2021-Security Misconfiguration              |                          |
| A06:2017-Security Misconfiguration    | A06:2021-Vulnerable and Outdated Components     |                          |
| A07:2017-Cross-Site Scripting (XSS)   | A07:2021-Identification and Authentication Failures |                          |
| A08:2017-Insecure Deserialization     | **[New]** A08:2021-Software and Data Integrity Failures | Software and Data Integrity Failures |
| A09:2017-Using Components with Known Vulnerabilities | A09:2021-Security Logging and Monitoring Failures* |                          |
| A10:2017-Insufficient Logging & Monitoring | **[New]** A10:2021-Server-Side Request Forgery (SSRF)* | Server-Side Request Forgery |

* * indica que la categoría fue añadida a partir de una encuesta.

Esta tabla ilustra cómo algunas vulnerabilidades han cambiado de prioridad o han sido renombradas, y cómo nuevas categorías emergieron debido a la evolución de las aplicaciones y técnicas de ataque.

## 3. OWASP Top 10 API Security Risks - 2023

Con el creciente uso de las API (Application Programming Interfaces), OWASP también publica una lista específica de los 10 riesgos de seguridad más críticos para las APIs.

| Riesgo API (2023)                                  | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API1:2023-Broken Object Level Authorization** | Las APIs tienden a exponer *endpoints* que manejan identificadores de objetos, creando una amplia superficie de ataque de Autorización a Nivel de Objeto. Las comprobaciones de autorización a nivel de objeto deben considerarse en cada función que accede a una fuente de datos usando un ID del usuario.                                                                                                                                |
| **API2:2023-Broken Authentication** | Los mecanismos de autenticación a menudo se implementan incorrectamente, permitiendo a los atacantes comprometer los *tokens* de autenticación o explotar fallos de implementación para asumir la identidad de otros usuarios temporal o permanentemente. Comprometer un sistema para identificar a los clientes usuarios compromete la seguridad general de la API.                                                                                   |
| **API3:2023-Broken Object Property Level Authorization** | Esta categoría combina "API2:2019 Excessive Data Exposure" y "API4:2019 Missing Function Level Authorization", centrándose en la causa raíz de la falta de una correcta validación de autorización a nivel de propiedad del objeto. Esto puede llevar a la exposición o manipulación de información no autorizada.                                                                                                                             |
| **API4:2023-Unrestricted Resource Consumption** | Satisfacer las solicitudes de API a menudo requiere recursos como ancho de banda de red, CPU, memoria y almacenamiento, entre otros. Otros recursos como el envío de SMS/llamadas telefónicas o el uso de *proxies* se hacen disponibles por los proveedores de servicios de API o integraciones, y se pagan por solicitud. Las solicitudes exitosas pueden llevar a la **Denegación de Servicio (DoS)** o a un aumento excesivo de los costos operativos. |
| **API5:2023-Broken Function Level Authorization** | Las políticas de control de acceso complejas con diferentes jerarquías, grupos y roles, y una separación poco clara entre la autorización administrativa y la regular, a menudo conducen a fallos en la autorización. Al explotar estos problemas, los atacantes pueden obtener acceso a recursos de usuario o funciones administrativas adicionales.                                                                                                              |

Esta lista es crucial para las organizaciones que desarrollan y utilizan APIs, ya que resalta las áreas donde se deben enfocar los esfuerzos de seguridad.

## 4. Conclusión

OWASP, o el **Open Web Application Security Project**, es una organización clave impulsada por la comunidad, dedicada a mejorar la seguridad del software. Proporciona **recursos, herramientas y directrices** esenciales para ayudar a las organizaciones a fortalecer la postura de seguridad de sus aplicaciones web y redes.

Las contribuciones de OWASP son fundamentales para el **hardening** de la red, ya que identifican vulnerabilidades comunes, promueven las mejores prácticas, y facilitan el desarrollo de soluciones de software seguro. Todo esto se traduce en una **reducción significativa del riesgo de ciberataques y Data Leaks**.

---