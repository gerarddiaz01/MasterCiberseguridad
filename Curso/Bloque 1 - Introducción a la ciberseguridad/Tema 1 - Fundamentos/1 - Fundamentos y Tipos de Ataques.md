# Ciberseguridad: Conceptos Fundamentales y Tipos de Ataques

## 1. Introducción a la Ciberseguridad

La ciberseguridad es el proceso de proteger la **confidencialidad**, la **disponibilidad** y la **integridad** de la información siempre en un **soporte digital**. A diferencia de la seguridad de la información (que abarca la protección de la información independientemente del soporte), la ciberseguridad se enfoca exclusivamente en el entorno digital. Es una rama fundamental dentro de la seguridad de la información.

Dentro del campo de la ciberseguridad, existen diversos perfiles, que incluyen la seguridad ofensiva y defensiva, entre otros.

## 2. Motivación de los Atacantes

Comprender la motivación de los atacantes es crucial para establecer defensas efectivas en cualquier organización o a nivel de usuario. Las principales motivaciones incluyen:

* **Baja o Inexistente Seguridad**: La falta de seguridad o una seguridad deficiente es una de las principales razones por las que las organizaciones son atacadas. Invertir en seguridad reduce significativamente el porcentaje de posibles atacantes.
* **Alta Exposición**: Una mayor exposición de activos en Internet incrementa el riesgo de ataque, contraviniendo el principio de **mínima exposición** en ciberseguridad.
* **Motivación Económica**:
    * **Espionaje Industrial**: Obtener información para venderla a terceros o a la competencia.
    * **Ataque/Incidente Financiero**: Búsqueda de rédito económico directo.
* **Descontento Interno (**Insider**)**: Empleados insatisfechos con las políticas de la organización, su trabajo, o que puedan ser "vendidos" a terceros. Un **insider** es una persona dentro de la empresa con acceso a información que puede hacer un mal uso de ella. Es esencial implementar controles internos y trazabilidad para mitigar esta amenaza.
* **Hacktivismo**: Motivación de protesta o reivindicación, sin buscar un beneficio económico. A menudo se relaciona con ataques de **denegación de servicio**.
* **Ponerse a Prueba**: Individuos autodidactas que buscan probar sus habilidades. Es crucial destacar que estas pruebas deben realizarse en entornos controlados (laboratorios propios, entornos virtualizados, distribuciones con vulnerabilidades preinstaladas) y nunca en sistemas reales debido a las implicaciones legales.

## 3. Incidentes de Ciberseguridad Reales

Se han presentado varios casos históricos que ilustran la relevancia de la ciberseguridad:

* **Mossack Fonseca (2016)**: Robo de varios terabytes de información de clientes. Se planteó la hipótesis de un ataque externo coordinado o de un **insider**. Este caso resalta la amenaza de los **insiders** y la importancia de la trazabilidad interna.
* **Ashley Madison (Data Breach)**: Incidente masivo de **data breach** con un gran robo y publicación de millones de identidades digitales de usuarios. Los **data breach** son un concepto que acompaña al mundo de la ciberseguridad desde hace más de una década. Leyes como el **GDPR** a nivel europeo exigen la notificación de estos incidentes a los usuarios. Estos incidentes, aunque negativos, han puesto en valor la necesidad de la ciberseguridad.
    * **Herramienta útil**: `Have I Been Pwned` (HIBP) es un servicio que permite verificar si una dirección de correo electrónico se encuentra en algún **data breach** registrado. Si es el caso, se recomienda cambiar contraseñas y aplicar el segundo factor de autenticación (2FA).
* **Celebgate (Phishing)**: Afectó a algunas actrices de Hollywood a través de campañas de **phishing** que llevaron al robo de credenciales de **iCloud** y la posterior fuga de fotografías (**fotoleak**). El **phishing** implica la virtud del atacante para presentar un mundo ficticio que parece real a los ojos del usuario, quien confía y concede sus credenciales o información. Los culpables fueron condenados, lo que subraya las implicaciones legales de estos ataques.

## 4. Tipos de Ataques Comunes

La ciberseguridad se enfrenta a una variedad de ataques, algunos de los más comunes incluyen:

* **Malware**: Software malicioso comúnmente conocido con diferentes tipos de infecciones y funcionalidades, que son grandes amenazas para las organizaciones.
    * Se clasifica en tipos como **troyanos**, **virus**, **ransomware** y **spyware**.
    * El **ransomware** es particularmente crítico, ya que secuestra y cifra información importante de las organizaciones, exigiendo un rescate. Para grandes empresas, la mitigación puede implicar planes de copias de respaldo y restauración, pero para las PyMEs, la falta de acceso a información vital puede incluso provocar su desaparición si no tienen planes de mitigación.
* **Ingeniería Social**: Ataques que explotan el componente humano de una organización, presentando un mundo que parece real para que las personas confíen en los atacantes y realicen algún tipo de acción.
    * **Phishing**: El ejemplo más común, donde los usuarios reciben correos electrónicos engañosos que los dirigen a páginas falsas para solicitar credenciales o información, incluyendo datos de tarjetas de crédito.
    * **Evolución del Phishing**: Ha evolucionado con la llegada de dispositivos móviles, tecnologías como la autenticación de voz y la **inteligencia artificial** (IA), que permiten la acumulación de voces o la creación de imágenes (**deepfakes**) que parecen reales.
    * **Estafa del CEO**: Un tipo particular de **phishing** donde se envía un correo electrónico haciéndose pasar por el CEO o una persona importante de la empresa para solicitar pagos urgentes. Esto ha evolucionado a videollamadas o llamadas de plataformas como Skype o Teams, donde una persona generada por IA puede simular ser el CEO.
* **Denegación de Servicio (DoS) y Denegación de Servicio Distribuido (DDoS)**: Afectan directamente la **disponibilidad** de la información. Un ataque DoS o DDoS puede colapsar un servicio, muchos servicios, o incluso la operativa completa de una empresa en Internet, dejando su negocio no disponible y causando pérdidas críticas. Existen soluciones anti-DDoS, y las pruebas de **hacking ético** permiten medir su eficiencia.
* **Ataques de Inyección**: Vulnerabilidades comunes en el software (ya sea de terceros o propio) que permiten la inyección de código o comandos. Agrupan muchos tipos de vulnerabilidades, como **SQL injection**, **NoSQL injection**, **LDAP injection** y ejecución de comandos. Son vías de ataque que los atacantes utilizan para comprometer la seguridad.
* **Fuerza Bruta**: Proceso por el cual se prueban contraseñas hasta dar con la correcta para un usuario.
    * Los sistemas deben poder detectar y banear conexiones que realicen este tipo de pruebas.
    * Una mala configuración o política de contraseñas (uso de contraseñas fácilmente adivinables, palabras comunes, o que se encuentran en diccionarios) aumenta el riesgo.
    * La aplicación de complejidad suficiente a las contraseñas (mayúsculas, minúsculas, números, caracteres especiales, longitud) reduce la capacidad de la fuerza bruta.
    * La implementación del **segundo factor de autenticación** (2FA) hace que la fuerza bruta pierda sentido.
    * En servicios estándar (ej. SSH en el puerto 22), se recomienda usar autenticación por clave pública y puertos no estándar para reducir las posibilidades de ataque.
    * **Password Spraying**: Una variante de fuerza bruta donde se fija una contraseña y se prueba en un listado de usuarios, buscando si alguno de ellos la utiliza.
* **Man-in-the-Middle (MitM)**: No es un solo tipo de ataque, sino una categoría donde un equipo se coloca en medio de una comunicación con el objetivo de observar la información, e incluso manipularla (inyectando certificados o modificando el tráfico en texto plano).
    * Se mitigan con el uso de canales seguros, cifrado punto a punto, y **certificate pinning**.
* **Explotación de Memoria**: Vulnerabilidades en aplicaciones (ej. *buffer overflow*, *stack overflow*) que se producen por una codificación incorrecta. Pueden ser explotadas a través de un **exploit**.
    * Un **exploit** es una aplicación que sabe cómo aprovecharse de una vulnerabilidad de un software en una versión concreta, con el objetivo de ejecutar código y proporcionar control de la máquina a un atacante o a un *pentester* en el ámbito del **hacking ético**.
    * La mitigación incluye aislar el servicio vulnerable, actualizarlo si existe un parche, o poner protecciones alrededor para detectar intentos de explotación (ej. IDS/IPS).

## 5. Conceptos Básicos en Ciberseguridad

### 1. 0-day (Zero-Day)

Un **0-day** es una vulnerabilidad de seguridad desconocida por el desarrollador y sin parche disponible. Son extremadamente valiosas para los atacantes, ya que permiten ataques sigilosos y son difíciles de detectar. Suelen emplearse en ataques sofisticados como las **APT**. La mitigación implica aislar los servicios vulnerables o usar protecciones como **IDS/IPS** para detectar *payloads* maliciosos.

### 2. SSDLC (Secure Software Development Life Cycle)

El **SSDLC** es una metodología que integra la seguridad en **cada fase del ciclo de vida del desarrollo de software**, desde la concepción hasta el despliegue. Su objetivo es asegurar la seguridad desde el diseño, reduciendo vulnerabilidades y costos al identificarlas tempranamente. Está estrechamente relacionado con **DevSecOps**, que fusiona desarrollo, operaciones y seguridad en un flujo continuo.

### 3. Buffer Overflow y Stack Overflow (Explotación de Memoria)

Estos son tipos de vulnerabilidades de **explotación de memoria** donde un programa escribe datos más allá de los límites de un búfer o una sección de memoria asignada, sobrescribiendo áreas adyacentes.

#### 3.1. Buffer Overflow

Ocurre cuando se intenta escribir más datos de los que un búfer puede almacenar, desbordándolo y sobrescribiendo la memoria contigua. Esto puede causar corrupción de datos, caídas del programa o, críticamente, permitir la **ejecución remota de código (RCE)** al inyectar y ejecutar *shellcode* malicioso.

#### 3.2. Stack Overflow

Es un tipo específico de **Buffer Overflow** que sucede en la pila de llamadas (*call stack*). Se produce cuando un búfer local en una función desborda y sobrescribe la dirección de retorno de la función en la pila. Un atacante puede manipular esta dirección para redirigir el flujo de ejecución del programa a su propio código inyectado, obteniendo control del sistema.

**Mitigación General:** Ambas vulnerabilidades se mitigan mediante la validación y saneamiento de entradas, el uso de funciones de biblioteca seguras, protecciones del compilador (como *stack canaries* o DEP), mantener el software actualizado y, si es necesario, aislar servicios o usar IDS/IPS.

### 4. APT (Advanced Persistent Threat)

Una **APT** (Amenaza Persistente Avanzada) es un tipo de ataque que se distingue por requerir mucho tiempo y recursos. Son ataques más avanzados de lo normal, con objetivos muy complejos y difíciles, y no están al alcance de cualquier atacante. Frecuentemente, involucran el estudio de vulnerabilidades **0-day**, es decir, vulnerabilidades no conocidas públicamente o para las cuales no hay parche.

El objetivo principal de un atacante con una APT es lograr el acceso a sistemas o dispositivos y mantener una persistencia en ellos para alcanzar sus metas.

En el ámbito del **hacking ético**, la **simulación de APT** es un servicio que se contrata para poner a prueba las defensas de una organización. Un equipo de *pentesters* intenta lograr un objetivo específico (por ejemplo, acceder a un dispositivo móvil del CEO o CISO de la empresa) de manera legal y ética, lo que representa un reto considerable.

### 5. Bug Bounty

Un **Bug Bounty** es un programa donde las empresas ofrecen recompensas económicas a investigadores de seguridad por encontrar y reportar vulnerabilidades en sus sistemas o aplicaciones. Estos programas son una forma de auditar la seguridad de activos como sitios web o dominios.

Las empresas que ofrecen programas de Bug Bounty establecen un conjunto de reglas claras que los participantes deben seguir estrictamente. Es crucial cumplir con estas reglas, ya que ignorarlas puede llevar a cometer un delito. Los programas también especifican qué tipos de vulnerabilidades les interesan, y una vez que una vulnerabilidad es encontrada y reportada siguiendo las reglas, la empresa paga un dinero como premio.

### 6. DevSecOps

**DevSecOps** es la evolución del concepto **DevOps**. Mientras que **DevOps** integra a los equipos de desarrollo y operaciones en un flujo de trabajo unido, **DevSecOps** añade la seguridad en cada fase de este proceso.

El objetivo de DevSecOps es que la seguridad no se conciba de forma aislada o como una etapa tardía, sino que esté alineada e integrada continuamente a lo largo de todo el ciclo de vida de desarrollo y operaciones. Esto se alinea directamente con los principios del **SSDLC (Secure Software Development Life Cycle)**, donde la seguridad se incorpora desde el principio del diseño y desarrollo de una aplicación.

Es fundamental familiarizarse también con los siguientes términos:

* **Data Leaks / Fuga de Datos**: Ocurre cuando información (generalmente bases de datos con identidades digitales o información propia de la organización) sale fuera de la empresa debido a una vulnerabilidad o a la acción de un **insider**, y es publicada o vendida.

* **Actualización de Software**: Fundamental. Los sistemas deben estar actualizados para evitar vulnerabilidades conocidas, ya que existen muchas fuentes de información pública (como *SecurityFocus* o *Exploit-DB*) donde se publican vulnerabilidades y **exploits**.