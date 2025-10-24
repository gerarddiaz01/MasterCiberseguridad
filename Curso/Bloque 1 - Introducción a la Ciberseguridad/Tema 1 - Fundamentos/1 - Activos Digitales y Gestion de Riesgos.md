# Protección de Activos Digitales y Gestión de Riesgos en Ciberseguridad

## 1. Protección de Activos Digitales: El Ciclo NIST/ENISA

La ciberseguridad tiene como objetivo principal proteger los **activos digitales**, que son cualquier información en soporte digital que permite a una empresa realizar su actividad de negocio. La protección de estos activos se basa en un ciclo iterativo y de mejora continua, guiado por fases clave propuestas por marcos como **NIST** y **ENISA**.

Las cinco fases interconectadas para la protección de activos digitales son:

* **Identificar**: Adquirir conocimiento profundo de la organización, sus activos, riesgos y sistemas. Esto sienta las bases para el plan de ciberseguridad, comprende la situación actual, el historial de incidentes (como **ransomware**, **phishing**, estafas del CEO) y los problemas potenciales futuros. Aspectos clave incluyen desarrollar un plan director de seguridad, establecer un ISMS (Information Security Management System), definir controles e indicadores de compromiso, y realizar auditorías y análisis de riesgo.
* **Proteger**: Diseñar e implementar medidas, controles y salvaguardas de seguridad para mitigar o minimizar el impacto de un incidente. Esto incluye la integración de la seguridad en el ciclo de desarrollo (**DevSecOps**) mediante pruebas como *code reviews*, *pentests* y análisis estáticos de código. También implica la integración de soluciones de seguridad (IDS, IPS, **firewall**, **VPN**), la segmentación de redes (DMZ, **VLANs**, subredes) y entornos (desarrollo, preproducción, producción). La generación de guías de *hardening* de sistemas y la aplicación de políticas de seguridad son fundamentales.
* **Detectar**: Establecer actividades para reconocer y monitorear la presencia de atacantes o amenazas en los sistemas lo antes posible. Una detección temprana es clave para una respuesta eficaz. Esta fase busca identificar vulnerabilidades potenciales antes de que se conviertan en incidentes o detectar un incidente en su fase más temprana. Aspectos clave incluyen la gestión de vulnerabilidades, servicios de **SOC** (Security Operations Center), ejercicios de **Red Team** para emular adversarios y probar la capacidad de detección del **Blue Team**, revisiones de código fuente, monitoreo continuo de infraestructura, *penetration testing* e inteligencia de amenazas.
* **Responder**: Tomar acciones adecuadas y aplicar medidas correctivas ante un incidente o intrusión. El objetivo es entender qué ocurrió, quién lo realizó y en qué sistemas. Esto involucra el *thread hunting* (detectar amenazas por comportamientos anómalos), el análisis forense (para investigar lo ocurrido *post-mortem*) y planes de respuesta a incidentes.
* **Recuperar**: Restablecer la actividad normal del negocio después de un incidente, reparando el daño y erradicando la amenaza. Aquí entra en juego el concepto de **resiliencia**. Se utilizan planes de continuidad de negocio y pruebas de continuidad para verificar que la actividad puede reanudarse sin problemas.

Este ciclo se aplica a cualquier organización, desde grandes corporaciones hasta **PyMEs**. Para estas últimas, a menudo afectadas por **ransomware**, la falta de medidas adecuadas (como copias de seguridad aisladas de la red) puede impedir una recuperación normal.

## 2. Principios Fundamentales de la Ciberseguridad

Estos principios se aplican para proteger la información y los sistemas en cualquier nivel (usuario, sistema, empresa) y permiten entender los riesgos existentes.

### 2.1. Menor Privilegio Posible (Least Privilege)

Todo usuario, proceso o servicio debe ejecutar sus acciones con el **menor privilegio posible**. Si un servicio expuesto es comprometido, un atacante tendrá que realizar una **escalada de privilegios** adicional para obtener control administrativo, lo que añade una traba y dificulta su éxito.

### 2.2. Mínima Exposición (Least Exposure)

Las máquinas y servicios deben exponer la menor cantidad posible de elementos. Cuantos más servicios se ejecuten en una misma máquina, mayor es la superficie de ataque y la probabilidad de que una vulnerabilidad o un fallo de configuración permita el acceso.

* Lo ideal es **reducir la superficie de ataque** ejecutando un servicio por máquina o usando microservicios.
* Las máquinas con servicios deben estar **aisladas o segmentadas** para evitar que un compromiso permita pivotar a otros sistemas o la red interna.
* Este principio también se aplica a la **información**: exponer menos información al exterior reduce el conocimiento que los atacantes pueden obtener.

### 2.3. Defensa en Profundidad (Defense in Depth)

Este modelo es un enfoque por **capas** para la seguridad, similar a la construcción de un edificio con cimientos sólidos. La idea es que, si una capa de seguridad falla, las siguientes capas actúen como respaldo, dificultando significativamente el ataque y aumentando los recursos y el tiempo que le costaría al atacante lograr su objetivo.

Las capas principales, desde la base hasta la cúspide, son:

* **Personas**: La base de la seguridad. Las personas deben tener **concienciación, formación y entrenamiento** sobre los riesgos y amenazas a los que se enfrentan en su día a día laboral. Es crucial identificar roles y responsabilidades, y que la alta dirección establezca políticas de seguridad que se comuniquen a toda la organización.
* **Físico**: Acceso físico a las instalaciones y equipos. Incluye elementos como tornos, cámaras de seguridad, tarjetas de identificación, cerraduras y acceso restringido a CPDs (Centros de Procesamiento de Datos). Si la seguridad física es débil, la seguridad digital es vulnerable.
* **Redes**: Protección de diferentes tipos de redes (DMZ, redes internas). Medidas incluyen:
    * **Firewalls**: Fundamentales, a veces con configuraciones de *frontend* y *backend* para controlar el tráfico entre redes (ej. entre DMZ y red interna).
    * **VPN (Virtual Private Network)**: Para el acceso remoto seguro de empleados a servicios internos.
    * **VLANs (Virtual Local Area Networks)**: Para segmentar redes LAN virtuales, aislando grupos de máquinas (ej. contabilidad, desarrollo) y limitando la propagación de compromisos.
    * **Segmentación de Red**: Evitar redes planas; crear subredes con **listas de control de acceso (ACLs)** para controlar el tráfico entre ellas, especialmente en zonas sensibles.
    * **IDS/IPS (Intrusion Detection/Prevention Systems)**: El **IDS** detecta amenazas en la red y las notifica; el **IPS** detecta y previene bloqueando la amenaza (ej. modificando reglas del firewall).
    * **Cifrado**: Cifrar comunicaciones con servicios internos y bases de datos críticas, incluso dentro de la organización.
* **Sistemas/Hosts**: Seguridad a nivel de equipos individuales. Incluye:
    * **GPOs (Group Policy Objects)**: Políticas de seguridad aplicadas a nivel de dominio (en Active Directory), como políticas de contraseñas.
    * **HIDS (Host Intrusion Detection Systems)**: Agentes en los sistemas que detectan anomalías, como cambios de integridad en archivos o configuraciones.
    * **Antimalware**: Suites para detectar y prevenir infecciones.
    * **Logs**: Elementos fundamentales para responder a incidentes, permitiendo verificar lo ocurrido. Se recomienda centralizar los logs para análisis y detección de anomalías.
    * **Sistemas de Actualización**: Mantener el parque de equipos actualizado para protegerse contra vulnerabilidades conocidas.
    * **WAF (Web Application Firewall)**: Firewall que opera a nivel de aplicación web para detectar y bloquear consultas maliciosas dirigidas a explotar vulnerabilidades web (ej. **SQL injection**, *cross-site scripting*).
* **Aplicaciones**: Seguridad específica de las aplicaciones. Incluye:
    * Cifrado de bases de datos y listas de control de acceso a nivel de aplicación.
    * **DLP (Data Loss Prevention)**: Prevención de la fuga de datos.
* **Datos**: La capa más alta, enfocada en la protección de la información sensible. Incluye cifrado de particiones o carpetas.

#### DMZ (Segmentación de redes)

La DMZ (Zona Desmilitarizada) es una subred física o lógica que se encuentra entre la red interna (privada) de una organización y una red externa, generalmente Internet. Su propósito principal es añadir una capa extra de seguridad para los servicios que se exponen públicamente.

**¿En qué consiste la DMZ en la segmentación de redes?**

- Servicios Públicos: La DMZ está diseñada para albergar servicios que necesitan ser accesibles desde Internet, como servidores web, servidores de correo electrónico, DNS públicos o servidores FTP. Al colocar estos servicios en la DMZ, se aíslan de la red interna de la organización.

- Capa de Seguridad Intermedia: Funciona como una red intermedia, una especie de "colchón" de seguridad entre la red confiable (interna) y la red no confiable (Internet). Si un atacante logra comprometer un servicio en la DMZ, aún tendría que superar otra capa de seguridad (un segundo firewall, por ejemplo) para acceder a la red interna y a la información crítica o sensible de la organización.

- Firewalls Dobles: Comúnmente, se utilizan dos firewalls para crear y proteger una DMZ.
* Un firewall de frontend (o externo) se coloca entre Internet y la DMZ, controlando el tráfico que entra a la organización y dirigiendo el tráfico a los servicios públicos en la DMZ.
* Un firewall de backend (o interno) se sitúa entre la DMZ y la red interna. Este firewall controla el tráfico entre la DMZ y la red interna, asegurando que solo el tráfico legítimo y autorizado pueda pasar a la red más crítica.

- Aislamiento y Riesgo Reducido: Al segmentar la red de esta manera, se minimiza el riesgo si un servicio expuesto es vulnerado. El atacante queda contenido en la DMZ y no obtiene acceso directo a los sistemas internos de la empresa. Esto es un ejemplo claro del principio de mínima exposición y de defensa en profundidad.

### 2.4. Zero Trust

El modelo **Zero Trust** surge como respuesta a la evolución del panorama de seguridad, donde los sistemas ya no están solo "in house" (en casa), sino que son **híbridos o totalmente *cloud***. Esto ha llevado a una pérdida de control sobre cada activo, ya que no todo se encuentra dentro de un perímetro físico tradicional.

* **Nuevo Perímetro**: En Zero Trust, la **identidad de cada usuario** y de cada servicio en la *cloud* se convierte en el nuevo perímetro, reemplazando el perímetro de red delimitado por firewalls.
* **Desconfianza por Defecto**: El principio central es **"nunca confiar, siempre verificar"**. Se propone la creación de **microperímetros** y la validación de la identidad en cada interacción con cualquier servicio o sistema, ya que se asume que ninguno está inherentemente seguro.
* **Similitud con Defensa en Profundidad**: Aunque el enfoque es diferente, ambos modelos proponen la aplicación de medidas de seguridad en múltiples capas. Zero Trust adapta estas medidas a un entorno distribuido y desconfía de cualquier interacción, sin importar su origen.

## 3. Risk Assessment: ISO 27001, Gestión y Análisis de Riesgos

La **gestión de riesgos** es una herramienta fundamental para evaluar el estado de la seguridad de una organización y permitir la mejora continua.

### 3.1. ISO 27001

La **ISO 27001** es una norma que especifica los requisitos para establecer, implementar, mantener y mejorar un **ISMS (Information Security Management System)** documentado. Proporciona un framework o marco de trabajo para la gestión de riesgos y la mejora continua en la seguridad de la información.

### 3.2. El Framework ISMS (Information Security Management System)

Un **ISMS** o **SGSI** (Sistema de Gestión de Seguridad de la Información) es un *framework* o marco de trabajo que involucra a **personas, procesos, políticas y salvaguardas (controles)** para mejorar continuamente la protección de la **confidencialidad, integridad y disponibilidad** de la información. No es una aplicación, sino un conjunto integral de elementos que buscan la mejora constante de la seguridad.

La mejora se logra mediante la implantación y seguimiento de controles, auditorías (como *pentests* o *hacking ético*) y decisiones para mejorar dichos controles. Un SGSI incluye la definición de la política de seguridad y su alcance, y es fundamental la **evaluación y gestión del riesgo** para seleccionar controles adecuados.

### 3.3. Análisis y Evaluación del Riesgo

El **análisis de riesgos** es un proceso que permite tomar decisiones objetivas sobre la seguridad.

* **Propósito**: Identificar los riesgos a los que está expuesta la organización, medir el impacto potencial de las amenazas si se materializan, y determinar qué controles aplicar para mitigar dicho impacto.
* **Proceso Cíclico**: Es un proceso continuo. Los riesgos se identifican, se evalúa su impacto, se aplican controles para mitigarlos, lo que reduce el **riesgo potencial** a un **riesgo residual**. Luego, se vuelve a evaluar para ver si el riesgo residual es aceptable y si se necesita más inversión en seguridad.
* **Herramienta de Medición**: Permite medir la eficiencia y eficacia de las inversiones en seguridad, ayudando a las empresas a saber si deben mejorar sus protecciones. Es la herramienta que el ISMS framework utiliza para retroalimentarse.

**Conceptos Básicos de Evaluación del Riesgo:**

* **Activo (*Asset*)**: Cualquier cosa con valor para la organización (ej. un servicio, una página web, un servidor, un sistema de información, recursos).
* **Riesgo (*Risk*)**: La probabilidad de que una amenaza se materialice contra un activo, provocando un impacto o daño.
* **Protección (*Control/Safeguard*)**: Un elemento o medida que disminuye la probabilidad de ocurrencia de un riesgo o su impacto en caso de materializarse (ej. un **firewall**, un IPS, un antivirus).
* **Riesgo Potencial (*Inherent Risk*)**: El riesgo identificado sobre un activo antes de aplicar cualquier control o salvaguarda.
* **Riesgo Residual (*Residual Risk*)**: El riesgo resultante después de aplicar uno o varios controles. La seguridad 100% no existe, por lo que siempre habrá un umbral de riesgo residual aceptable que la organización debe definir.
* **Amenaza (*Threat*)**: Una situación que puede provocar un incidente de seguridad y causar daño a los activos (ej. un **insider** que roba información, una vulnerabilidad que es explotada, un error de configuración).