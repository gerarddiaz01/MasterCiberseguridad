# Diferencia entre Herramientas y Técnicas de Ciberseguridad

En ciberseguridad, estas herramientas y técnicas, aunque relacionadas, tienen enfoques y objetivos distintos:

### OSINT (Open-Source Intelligence)

**OSINT** se refiere a la recopilación y análisis de **información disponible públicamente** para obtener inteligencia accionable. Esta información puede provenir de una vasta gama de fuentes abiertas, como redes sociales, sitios web, foros públicos, registros gubernamentales, noticias, blogs, e incluso datos filtrados en la *dark web* siempre que sean accesibles legalmente.

* **Objetivo**: Transformar datos brutos y dispersos en inteligencia útil. En ciberseguridad, se utiliza para:
    * **Reconocimiento**: Recopilar información sobre un objetivo (organización o individuo) antes de un ataque simulado o real. Esto puede incluir detalles de infraestructura de TI, correos electrónicos, números de teléfono, nombres de usuario, etc.
    * **Inteligencia de Amenazas**: Identificar posibles amenazas, monitorear actividades de adversarios, detectar fugas de datos sensibles de la organización o empleados, y evaluar riesgos.
    * **Gestión de Vulnerabilidades**: Revelar información pública sobre activos internos que podrían ser vulnerables.
* **Legalidad y Ética**: Aunque la información es pública, su uso debe ser ético y legal, cumpliendo con normativas como el GDPR. No implica *hacking*, suplantación o acceso no autorizado a grupos privados.

### Ingeniería Social (Social Engineering)

La **Ingeniería Social** es una táctica que explota el **error humano** mediante la manipulación psicológica o la influencia para engañar a las personas y obtener información sensible, conseguir acceso a sistemas o inducir a realizar acciones que comprometan la seguridad.

* **Objetivo**: Obtener información o acceso no autorizado sin necesidad de explotar vulnerabilidades técnicas del sistema, sino manipulando a los individuos.
* **Mecanismos**: Puede ser tan simple como una conversación o tan sofisticada como llamadas generadas por IA (*deepfakes* de voz o video), correos electrónicos falsos (**phishing**), o sitios web fraudulentos. Se basa en la persuasión, la confianza, la urgencia o la manipulación de emociones.
* **Ejemplos**:
    * **Phishing**: Envío de correos electrónicos engañosos para robar credenciales.
    * **Estafa del CEO**: Suplantación de una figura de autoridad para solicitar pagos urgentes.
    * **Baiting**: Usar una falsa promesa para atraer a la víctima a una trampa.
    * **Pretexting**: Crear un escenario falso (pretexto) para ganarse la confianza de la víctima.
* **Relación con OSINT**: OSINT puede ser utilizada como una fase inicial de reconocimiento para recopilar datos sobre el objetivo (nombres, roles, relaciones) que luego se utilizan para hacer los ataques de ingeniería social más creíbles y dirigidos.

### Explotación de Sistemas (System Exploitation)

La **Explotación de Sistemas** (o simplemente **Exploit**) se refiere al acto de aprovechar una **vulnerabilidad** o fallo de seguridad en un sistema, aplicación, hardware o red para causar un comportamiento no deseado o no anticipado. Un *exploit* es el código, software o técnica específica diseñada para materializar esa vulnerabilidad.

* **Objetivo**: Obtener acceso no autorizado, escalar privilegios, robar datos, interceptar información, causar una denegación de servicio o modificar la funcionalidad del sistema.
* **Cómo Funciona**: Un *exploit* busca una debilidad existente (la vulnerabilidad) y la utiliza para lograr un efecto malicioso. Por ejemplo, un *exploit* puede aprovechar un **buffer overflow** o **stack overflow** para inyectar y ejecutar código arbitrario en un sistema.
* **Tipos de Vulnerabilidades Explotadas**: Incluyen fallos en el *software*, configuraciones incorrectas, errores de diseño, o debilidades en los protocolos de red o en el hardware.
* **Impacto**: Puede variar desde la corrupción de datos, caídas del sistema, hasta el compromiso total del sistema o la red.
* **Prevención**: Mantener los sistemas actualizados con los últimos parches de seguridad, usar software seguro, y configurar correctamente los sistemas son claves para prevenir la explotación.

### Auditoría Web (Web Auditing)

Una **Auditoría Web** (o Auditoría de Seguridad Web) es un examen sistemático y detallado del marco de seguridad de un sitio web o aplicación web para identificar vulnerabilidades y riesgos. Los apuntes mencionan el **WAF (Web Application Firewall)**, que es una herramienta de seguridad que se aplica sobre aplicaciones web para detectar y bloquear consultas maliciosas en busca de explotaciones de vulnerabilidades web.

* **Objetivo**: Descubrir debilidades y corregirlas antes de que sean explotadas por ciberdelincuentes.
* **Alcance**: Evalúa el código, los *plugins*, las configuraciones del servidor, los controles de acceso y las políticas de seguridad de una aplicación web.
* **Métodos**: Generalmente combina **escaneos de vulnerabilidades** automatizados con **pruebas manuales** para identificar fallos que las herramientas automáticas podrían pasar por alto.
* **Resultados**: Proporciona una lista de vulnerabilidades técnicas y ofrece recomendaciones para mejorar la seguridad.

### Pentesting (Penetration Testing)

El **Pentesting** (prueba de penetración) es un **ataque simulado autorizado** contra un sistema informático para evaluar su seguridad. Los *pen-testers* (hackers éticos) utilizan las mismas herramientas, técnicas y procesos que los atacantes reales para encontrar y demostrar el impacto de las debilidades en un sistema.

* **Objetivo**: Identificar vulnerabilidades explotables y probar la robustez de las medidas de seguridad existentes bajo un escenario de ataque real.
* **Metodología**:
    1.  **Planificación y Alcance**: Definir los sistemas a probar, los objetivos y las reglas de *engagement*. En **Bug Bounty**, por ejemplo, se establecen reglas estrictas y qué vulnerabilidades se buscan.
    2.  **Recopilación de Información (Reconocimiento)**: Utilizar técnicas como **OSINT** y escaneo de red para reunir datos sobre el objetivo.
    3.  **Análisis de Vulnerabilidades**: Identificar debilidades potenciales.
    4.  **Explotación**: Intentar aprovechar las vulnerabilidades encontradas para obtener acceso, escalar privilegios, etc.
    5.  **Post-Explotación**: Mantener el acceso, explorar la red interna y determinar el impacto real.
    6.  **Reporte**: Documentar las vulnerabilidades, las explotaciones exitosas y las recomendaciones para remediarlas.
* **Tipos**: Puede ser externo (dirigido a tecnología expuesta a Internet), interno (desde dentro de la red), *black-box* (sin conocimiento previo del sistema), *white-box* (con conocimiento completo), o *gray-box*. También pueden incluir pruebas de **ingeniería social** o seguridad física.
* **Diferencia con Auditoría Web**: Aunque el *pentesting* puede incluir una auditoría web como parte de su alcance, el *pentesting* es más amplio y se enfoca en la explotación activa y la simulación de un ataque, mientras que la auditoría web es un examen más sistemático de las vulnerabilidades. El *pentesting* es una de las pruebas que permiten medir la eficiencia de los controles de seguridad y las inversiones en seguridad.

En resumen:

* **OSINT** se enfoca en **recopilar información pública**.
* **Ingeniería Social** se centra en **manipular personas** para obtener información o acceso.
* **Explotación de Sistemas** es la **ejecución de un ataque** para aprovechar una vulnerabilidad específica.
* **Auditoría Web** es un **examen sistemático** para identificar vulnerabilidades en sitios web.
* **Pentesting** es una **simulación de ataque autorizada** y activa para evaluar la seguridad de un sistema o red, que puede integrar las otras técnicas.

## Metasploit

El Metasploit Framework es una de las herramientas más populares y potentes en el campo de la ciberseguridad ofensiva, utilizada por *pentesters*, *hackers* éticos, e incluso por atacantes maliciosos. Es una plataforma de código abierto que facilita el desarrollo, prueba y ejecución de *exploits*.

### ¿Qué es Metasploit?

Metasploit es un marco de trabajo (framework) modular que proporciona una infraestructura para realizar pruebas de penetración. No es un *exploit* en sí mismo, sino una colección de *exploits*, *payloads*, *auxiliares*, *encoders* y *post-explotación*, todo organizado de una manera que permite a los usuarios interactuar con estos componentes de forma efectiva.

### Componentes Clave de Metasploit

1.  **Exploits**: Son piezas de código que aprovechan vulnerabilidades específicas en sistemas, aplicaciones o redes para obtener acceso. Metasploit alberga una vasta base de datos de *exploits* para una gran variedad de plataformas y servicios.
2.  **Payloads**: Una vez que un *exploit* ha logrado su objetivo (por ejemplo, ha ganado acceso a un sistema), el *payload* es el código que se ejecuta en la máquina objetivo. Los *payloads* pueden tener diversas funciones, como:
    * **Shell inverso (Reverse Shell)**: Establece una conexión desde la máquina objetivo de vuelta al atacante, permitiendo al atacante ejecutar comandos.
    * **Shell directo (Bind Shell)**: Abre un puerto en la máquina objetivo al que el atacante puede conectarse.
    * **Meterpreter**: Un *payload* avanzado que ofrece una interfaz interactiva potente con capacidades de post-explotación como la carga de módulos en memoria, captura de pantallazos, control de webcam, entre otros.
3.  **Auxiliares**: Módulos que realizan tareas de apoyo que no implican directamente la explotación de una vulnerabilidad, pero son útiles en las fases de reconocimiento, escaneo o recolección de información. Ejemplos incluyen escáneres de puertos, enumeradores de servicios o módulos de fuerza bruta.
4.  **Encoders**: Herramientas que se utilizan para codificar *payloads* con el fin de evadir la detección por parte de antivirus y sistemas de detección de intrusiones (IDS). Esto ofusca el código malicioso para que no sea reconocido por las firmas de seguridad.
5.  **Post-Explotación**: Módulos que se ejecutan una vez que el control inicial del sistema ha sido establecido. Permiten realizar acciones como la escalada de privilegios, la persistencia en el sistema, la recopilación de credenciales, el movimiento lateral en la red, o la exfiltración de datos.

### Fases de un Ataque con Metasploit (típicas de un Pentest)

Aunque Metasploit es una herramienta, su uso sigue las fases de un *pentest*:

1.  **Reconocimiento y Escaneo**: Utilizar módulos auxiliares para recopilar información sobre el objetivo (direcciones IP, puertos abiertos, servicios en ejecución, versiones de software).
2.  **Análisis de Vulnerabilidades**: Identificar posibles vulnerabilidades en los servicios y software detectados, a menudo correlacionando con bases de datos como CVE.
3.  **Selección y Configuración del Exploit**: Elegir el *exploit* adecuado para la vulnerabilidad identificada y configurar sus parámetros (por ejemplo, la dirección IP del objetivo, el puerto, el *payload* a usar).
4.  **Explotación**: Ejecutar el *exploit* contra el objetivo.
5.  **Post-Explotación**: Una vez que se obtiene acceso, utilizar módulos de post-explotación para profundizar en el compromiso, escalar privilegios, recopilar más información o mantener la persistencia.

### Versiones de Metasploit

* **Metasploit Framework (Community Edition)**: La versión de código abierto y gratuita, altamente popular entre la comunidad de ciberseguridad.
* **Metasploit Pro / Express**: Versiones comerciales que ofrecen funcionalidades adicionales, como interfaces gráficas, automatización de tareas, generación de informes y funciones avanzadas para equipos.

Metasploit es una herramienta esencial para cualquier profesional de la ciberseguridad que busque comprender cómo se realizan los ataques, evaluar la resistencia de los sistemas y mejorar las defensas de una organización.