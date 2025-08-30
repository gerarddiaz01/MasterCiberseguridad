Documentos de Referencia: "AS-I - Análisis de Vulnerabilidades_Metasploit.pdf"

# Informe Técnico: Metasploit Framework y Pentesting

## 1. Resumen Ejecutivo
Este informe detalla el uso de **Metasploit Framework**, una herramienta de código abierto fundamental para profesionales de ciberseguridad. Se diferencia entre el **pentesting** y el **análisis de vulnerabilidades**, y se explican las fases de un pentest. El documento describe la arquitectura modular de Metasploit, sus componentes y módulos principales, así como las distintas ediciones disponibles. Además, se incluyen procedimientos prácticos para el uso de la consola, la gestión de módulos y la interacción con objetivos, con el objetivo de demostrar su importancia estratégica tanto para **equipos ofensivos (Red Team)** como **defensivos (Blue Team)**.

---

## 2. Conceptos Fundamentales
* **Pentesting vs. Análisis de Vulnerabilidades:** Aunque se complementan, son conceptos distintos. El **análisis de vulnerabilidades** es un escaneo automatizado que identifica posibles debilidades en un sistema. En cambio, el **pentesting** es la práctica de explotar activamente estas debilidades para evaluar la resistencia de las defensas y obtener control sobre los sistemas o datos sensibles, simulando un ataque real de un hacker. Un análisis de vulnerabilidades dice *qué* posibles agujeros hay, mientras que un pentesting demuestra si se puede *entrar* por ellos.
* **Metasploit Framework:** Es un *framework* de explotación de código abierto, diseñado para realizar pentesting y ejecutar *exploits*. Fue creado en 2003 y adquirido por la empresa Rapid7, que lo reescribió en el lenguaje de programación **Ruby**. Su principal potencial reside en la **normalización de *exploits* y *payloads***, lo que permite a los profesionales optimizar el tiempo, evitando la investigación manual, adaptación y ejecución de código.
* **Arquitectura Modular:** El poder de Metasploit radica en su diseño modular, que permite a la comunidad de desarrolladores y a Rapid7 añadir rápidamente nuevos componentes para vulnerabilidades recién descubiertas.
    * **Librerías:** Son la base técnica del *framework*. **Rex** es la librería de bajo nivel para operaciones de red. **MSF Core** es el núcleo que carga y ejecuta los módulos, y **MSF Base** provee una API simplificada para los desarrolladores.
    * **Módulos:** Son las unidades funcionales del *framework*, agrupadas por su propósito. Hay varios tipos:
        * ***Exploits***: Código que aprovecha una vulnerabilidad para obtener acceso inicial a un sistema.
        * **Auxiliares:** Herramientas para tareas arbitrarias que no implican la ejecución de un *payload*, como escaneo de puertos, recolección de información o *fuzzing* de datos.
        * **Post-explotación:** Herramientas para acciones posteriores a la intrusión, como la escalada de privilegios, la captura de datos y el mantenimiento del acceso.
        * ***Payloads***: El código que se ejecuta en el sistema objetivo una vez que el *exploit* tiene éxito. Permiten controlar el sistema, abrir una *shell* y transferir archivos.
        * **Codificadores (*Encoders*):** Modifican el código de los *payloads* para evitar la detección por antivirus o sistemas de detección de intrusos.
        * **Evasión (*Evasion*):** Módulo específico para evadir antivirus, ofuscando el código para volverlo indetectable.
        * ***NOPs*:** Generadores de instrucciones nulas para rellenar búferes y estabilizar *exploits* en lenguaje ensamblador.
* **Ediciones de Metasploit:**
    * **Metasploit Framework:** Edición gratuita de línea de comandos, orientada a desarrolladores e investigadores de seguridad.
    * **Metasploit Express:** Versión de pago con interfaz gráfica, ya descontinuada, que se enfocaba en equipos de TI.
    * **Metasploit Pro:** Versión de pago con licencia de pago que continúa en uso. Ofrece una interfaz web, automatización avanzada y funciones como *phishing* dirigido.
    * **Metasploit Community:** Versión gratuita con interfaz web, descontinuada en 2019, que se dirigía a pequeñas empresas y estudiantes.

---

## 3. Procedimientos Prácticos
### Fases de un Pentesting
Los pasos de un pentesting, según la documentación de Rapid7, son:
1.  **Establecer el alcance (*Set the Scope*):** Definir claramente los objetivos, sistemas y aplicaciones a cubrir en la prueba de intrusión.
2.  **Reconocimiento y Descubrimiento:** Recopilar toda la información posible sobre los sistemas, servicios, puertos y usuarios.
3.  **Explotación:** Atacar los sistemas o aplicaciones vulnerables mediante fuerza bruta, *exploits* o ingeniería social.
4.  **Toma de Control y Pivoteo:** Una vez dentro, se pivota para acceder a otros activos de la red.
5.  **Recopilar Evidencia y Limpiar (*Gather Evidence and Cleanup*):** Se capturan pruebas (capturas de pantalla, *hashes*, archivos) y se eliminan los rastros para no dejar evidencia de la intrusión.
6.  **Reporte y Remediación:** Se redacta un informe detallado con las vulnerabilidades encontradas y se sugieren soluciones.

### Uso de la Consola de Metasploit (msfconsole)
La consola es la interfaz principal para interactuar con Metasploit. Al ejecutar el comando `msfconsole`, el *framework* se inicia y muestra un *banner* con el número de *exploits*, módulos auxiliares y *payloads* disponibles.

#### Comandos Principales
* **Comandos de ayuda:**
    * `help` o `?`: Muestra información general sobre comandos.
    * `banner`: Muestra un *banner* aleatorio de Metasploit.
* **Comandos de búsqueda y módulo:**
    * `search <palabra_clave>`: Permite buscar módulos (*exploits*, auxiliares, etc.) basándose en palabras clave, CVEs, plataformas o autores. Por ejemplo, `search eternalblue`. Se pueden usar filtros como `type` (ej. `search type:exploit`) o `rank` (ej. `search type:exploit -s rank`) para ordenar los resultados.
    * `info <nombre_o_ID_de_módulo>`: Muestra información detallada sobre un módulo específico, incluyendo la plataforma, si requiere privilegios, el *rank* de explotabilidad y opciones básicas.
    * `use <nombre_o_ID_de_módulo>`: Selecciona un módulo para interactuar con él, cambiando el *prompt* de la consola.
    * `back`: Sale del contexto del módulo actual y regresa a la raíz de la consola.
    * `show`: Muestra los módulos de un tipo específico (ej. `show exploits`, `show nops`). También puede usarse para ver opciones de un módulo con `show options`.
* **Comandos de configuración e interacción:**
    * `set <variable> <valor>`: Asigna un valor a una variable local del módulo activo. Por ejemplo, `set RHOSTS 10.0.1.9` para establecer la dirección IP del objetivo.
    * `unset <variable>`: Desasocia el valor de una variable local del módulo.
    * `setg <variable> <valor>`: Establece un valor para una variable **global** en todo Metasploit, que persistirá entre diferentes módulos.
    * `unsetg <variable>`: Desasocia el valor de una variable global.
    * `connect <host> <puerto>`: Permite la comunicación con un *host* remoto de forma similar a Netcat.
    * `load <plugin>`: Carga un *plugin* en el *framework*, como `nessus` o `sqlmap`, para integrar funcionalidades de otras herramientas. El comando `load -l` lista los *plugins* disponibles.
    * `unload <plugin>`: Descarga un *plugin*.
    * `loadpath <ruta>`: Permite cargar un módulo directamente desde una ruta del sistema de archivos sin necesidad de moverlo a la estructura de Metasploit y reiniciar.
    * `check`: Evalúa si un sistema objetivo es vulnerable antes de lanzar el *exploit*.
    * `exploit` o `run`: Lanza el *exploit* seleccionado para iniciar el ataque.
    * `sessions`: Muestra las conexiones o *shells* abiertas. Con `sessions -i <ID>` se puede interactuar con una sesión específica.
    * `jobs`: Lista los trabajos que se ejecutan en segundo plano. Se pueden terminar con `kill <ID_de_job>`.
    * `reload_all`: Recarga todos los módulos de Metasploit, similar a un reinicio, para aplicar cambios.
    * `save`: Guarda la configuración y el estado global de Metasploit.
    * `makerc <ruta_archivo>`: Guarda los comandos ejecutados recientemente en un archivo de texto. Por ejemplo, `makerc "/home/kali/Desktop/commands.txt"`.

---

## 4. Conclusiones y Puntos Clave
### Importancia y Beneficios de Seguridad
Metasploit no es solo una herramienta ofensiva; su verdadero valor radica en su capacidad para validar y fortalecer las defensas de una organización. Para el **Red Team**, facilita la simulación de ataques para identificar vulnerabilidades explotables. Para el **Blue Team**, permite reproducir escenarios de ataque para verificar las fallas detectadas por escáneres, priorizar la remediación de las más críticas y afinar los sistemas de detección y respuesta (IDS/IPS). Metasploit ayuda a reducir los **falsos positivos** y proporciona una comprensión profunda de las tácticas y técnicas de los atacantes, lo cual es esencial para diseñar controles de red efectivos.

### Puntos de Aprendizaje Clave
* El **pentesting** es una práctica estratégica y no un ataque al azar. La metodología, que incluye la recopilación de información, la validación y la post-explotación, es tan importante como la herramienta en sí.
* La **arquitectura modular** de Metasploit es su mayor fortaleza, ya que permite que la herramienta se mantenga actualizada y se adapte a las nuevas amenazas y vulnerabilidades descubiertas.
* El uso del comando **`check`** es crucial para validar la vulnerabilidad de un objetivo antes de lanzar un *exploit*, minimizando el riesgo de interrupción del sistema.
* Dominar la herramienta no se limita a memorizar comandos. La verdadera competencia reside en la capacidad de razonar como un atacante y aplicar la herramienta de forma inteligente y ética.
* La herramienta **Meterpreter** es el *payload* preferido por los profesionales debido a su capacidad de **evasión** y su flexibilidad para la post-explotación.

### Relevancia Técnica
El conocimiento de Metasploit es una habilidad indispensable en ciberseguridad. Su consola, **msfconsole**, integra una vasta gama de funcionalidades que van más allá de la simple explotación. Los procedimientos para la gestión de módulos, la configuración de variables locales y globales, la integración con otras herramientas como **Nessus** o **Nmap** (a través de *plugins* y comandos como `db_nmap`) y la gestión de sesiones y trabajos en segundo plano, demuestran la complejidad y el poder de este *framework*. Estas habilidades son aplicables en cualquier entorno de auditoría de seguridad y son una señal de un profesional que comprende el ciclo de vida de un ataque y sabe cómo defenderse de él.