# Seguridad Avanzada en Redes: IPv6, Zero Trust y Protección con Fail2ban

En el ámbito de la ciberseguridad moderna, la protección de las infraestructuras de red requiere un enfoque integral que abarque desde la evolución de los protocolos de comunicación hasta filosofías de seguridad avanzadas y herramientas de defensa activas. Esta sesión explora **IPv6** como el futuro del direccionamiento, la estrategia de **Zero Trust** para una seguridad sin concesiones, y la implementación práctica de **Fail2ban** para mitigar ataques de fuerza bruta.

## 1. IPv6: El Futuro del Protocolo de Internet y sus Implicaciones en Seguridad

**IPv6** es la versión más reciente del Protocolo de Internet y está diseñado para superar las limitaciones de IPv4, principalmente la escasez de direcciones IP. Utiliza direcciones de **128 bits**, lo que permite una cantidad virtualmente ilimitada de conexiones de dispositivos, asegurando el crecimiento continuo y la evolución de Internet.

### 1.1. Mejoras y Características de IPv6

* **Rendimiento Mejorado**: Ofrece un rendimiento optimizado gracias a encabezados de paquetes simplificados.
* **Soporte de Calidad de Servicio (QoS)**: Permite una mejor gestión del tráfico para aplicaciones sensibles al retardo.
* **IPsec Obligatorio**: Incluye cifrado IPsec (IP Security) de forma obligatoria, lo que proporciona una capa de seguridad integrada por defecto. Esto significa que, en teoría, las comunicaciones IPv6 están más protegidas contra la interceptación y la manipulación.
* **Direccionamiento Directo**: Facilita un direccionamiento más directo y eficiente de los dispositivos.
* **Evolución Continua**: IPv6 es un estándar en constante evolución, con cada vez más redes que lo adoptan. Su finalidad principal es proporcionar el máximo número de direcciones públicas de Internet y se enfoca en el diseño y la securización de redes, siendo muy útil en entornos empresariales por sus mejoras en seguridad.

### 1.2. Tipos de Direcciones IPv6

A diferencia de IPv4, IPv6 presenta diferentes tipos de direcciones con propósitos específicos:

* **Unicast**: Facilita la comunicación **uno a uno** al identificar una única interfaz de dispositivo, soportando vastas direcciones únicas con su esquema de 128 bits.
* **Multicast**: Permite que un solo paquete sea enviado a **múltiples destinos simultáneamente**, reduciendo el tráfico de red para aplicaciones como la transmisión de medios (`streaming media`).
* **Anycast**: Direcciones asignadas a **múltiples interfaces en diferentes dispositivos**. Los paquetes dirigidos a una dirección Anycast son enrutados a la interfaz más cercana, optimizando el balanceo de carga y mejorando la resiliencia de la red.

### 1.3. Desafíos y Consideraciones de Seguridad en IPv6

Aunque IPv6 ofrece características de seguridad por diseño (como IPsec por defecto), su implementación por sí sola no garantiza que una red sea completamente segura.

* **SLAAC (Stateless Address Autoconfiguration)**:
    * **Funcionamiento**: SLAAC es un método para la asignación automática de direcciones IP en IPv6 sin la necesidad de un servidor como DHCP. Cuando un dispositivo se conecta a una red IPv6, escucha los **Router Advertisements (RAs)** que incluyen un prefijo de red. El dispositivo genera su propia dirección IP combinando este prefijo con un identificador único, a menudo derivado de su dirección MAC.
    * **Riesgos de Seguridad**: Aunque facilita la configuración, SLAAC puede llevar a la pérdida de control sobre la red. Exponer la dirección MAC del dispositivo, utilizada para generar la dirección IP, también representa un riesgo de seguridad. Para mitigar esto, se pueden usar técnicas que generen direcciones más aleatorias.
* **Múltiples Direcciones por Host**: Es posible que un mismo host tenga varias direcciones, como las suministradas por DHCPv6, SLAAC o incluso direcciones IPv4 en configuraciones Dual Stack.
* **Modelo Dual Stack**: Muchas empresas operan con un modelo **Dual Stack**, utilizando tanto IPv4 como IPv6 en la misma infraestructura. Si bien esto facilita la transición, también puede ser un **vector de ataque** si no se gestiona correctamente, ya que los atacantes pueden buscar debilidades en cualquiera de los dos protocolos.

### 1.4. Consejos para la Integración Segura de IPv6

Para una integración segura de IPv6 en una organización, se recomienda un enfoque por fases:

1.  **Fase 1: Infraestructura Paralela Controlada**: Comenzar instalando una pequeña infraestructura paralela que asigne direcciones IPv6 a equipos y usuarios controlados. Esto permite familiarizarse con su funcionamiento y observar cualquier problema de conexión o seguridad.
2.  **Fase 2: Configuración Dual Stack en Elementos de Red**: Configurar IPv6 en los elementos de red dentro de la organización (routers, switches, etc.), aplicando el término **Dual Stack**. En esta fase es imprescindible revisar qué elementos conectan en la red y además son compatibles con este protocolo.
3.  **Fase 3: Acceso Completo a Internet por Defecto con IPv6**: Establecer por defecto el acceso ya completo a Internet con IPv6, es decir, todos los dispositivos de la infraestructura utilizarán este protocolo para sus comunicaciones tanto privadas como públicas. Este sería el último escenario, el ideal, donde todo funciona bajo IPv6.

## 2. Zero Trust: La Filosofía de Confianza Cero

**Zero Trust** (Confianza Cero) es una filosofía de seguridad que opera bajo el principio de **"nunca confiar, siempre verificar"**. En un modelo Zero Trust, ninguna entidad, ya sea interna o externa al perímetro de la red, es automáticamente confiable. En su lugar, todos los usuarios, dispositivos y aplicaciones deben ser **autenticados y autorizados** antes de acceder a los recursos.

* **Premisa**: Este enfoque asume que las amenazas pueden estar presentes tanto dentro como fuera de la red.
* **Enfoque**: Enfatiza la **monitorización continua** y los **controles de acceso estrictos** para prevenir accesos no autorizados y mitigar posibles brechas.
* **Objetivo**: Mejorar la postura de seguridad y proteger eficazmente los datos y activos sensibles.
* **Eficacia**: Es la estrategia más efectiva para contrarrestar los posibles **movimientos laterales** en caso de un acceso no autorizado a la red.

### 2.1. Principios Clave de Implementación de Zero Trust

La implementación de Zero Trust se basa en la aplicación de técnicas de segmentación ya conocidas, añadiendo una capa extra de protección mediante la creación de **microperímetros**.

* **Microsegmentación**: Añade granularidad al diseño, creando pequeños perímetros de seguridad que aíslan al atacante, utilizando por ejemplo métodos de autenticación y de autorización.
* **Identificación del Usuario**: Zero Trust considera a todos los usuarios no confiables. Por este motivo, si alguno intenta realizar alguna tarea sospechosa, este estará controlado en todo momento.
* **Control de Acceso (Principio de Mínimo Privilegio)**: Es un método para aplicar los menos privilegios posibles. Un usuario empezaría con el menor de los privilegios y se le iría añadiendo en función de que lo fuera solicitando o le fuera necesario dentro de su trabajo habitual.

El caso más práctico y útil donde Zero Trust pone en práctica es en un caso de **amenazas internas (Insider Threats)**, donde tanto empleados como un atacante que haya podido acceder podrían ver mitigado su ataque.

## 3. Fail2ban: Protección Activa contra Ataques de Fuerza Bruta

Para aplicar un enfoque de seguridad proactivo y ejemplificar los principios de Zero Trust, se utiliza una herramienta llamada **Fail2ban**.

**Fail2ban** es una herramienta de **prevención de intrusos** que escanea los archivos de registro del sistema y banea aquellas IP que muestran signos maliciosos o demasiados intentos de inicio de sesión fallidos. Esto de las sesiones fallidas suele ser normalmente utilizado por scripts de **fuerza bruta** para intentar acceder a una ubicación. El objetivo de limitar el número de accesos a un servicio o a un servidor es evitar sobre todo ataques de fuerza bruta o evitar que haya muchas peticiones a la vez que provoquen una **denegación de servicio (DoS)**, por ejemplo.

### 3.1. Práctica: Baneo de IP con Fail2ban

Este ejercicio práctico demuestra cómo configurar Fail2ban en un servidor (máquina víctima) para proteger el servicio SSH de intentos repetidos de acceso, utilizando otra máquina como atacante.

**Escenario**:

* **Máquina Víctima (Servidor)**: Una máquina Linux (ej. Ubuntu) donde se instalará y configurará Fail2ban. Su dirección IP en el ejemplo es `10.211.55.14`.
* **Máquina Atacante**: Otra máquina Linux con una terminal de color diferente (para distinguirlas en los pantallazos), que intentará conectarse por SSH al servidor. Su dirección IP en el ejemplo es `10.211.55.15`.

#### 3.1.1. Configuración de la Máquina Víctima (Servidor)

**Paso 1: Instalación de Fail2ban**

Primero, se instala Fail2ban.

* **Comando**: `sudo apt install fail2ban`
* **Sintaxis**:
    * `sudo`: Ejecuta el comando con privilegios de superusuario, lo cual es necesario para instalar paquetes.
    * `apt`: Es el gestor de paquetes para distribuciones basadas en Debian/Ubuntu.
    * `install`: La acción para instalar un paquete.
    * `fail2ban`: El nombre del paquete a instalar.
* **Explicación**: Descarga e instala el paquete `fail2ban` y sus dependencias en el sistema.
* **Objetivo**: Preparar el sistema con la herramienta Fail2ban para la prevención de intrusos.

**Paso 2: Copiar y Editar el Fichero de Configuración de Fail2ban**

Es mejor trabajar con una copia del archivo de configuración para personalizaciones.

* **Comando (Copia)**: `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`
* **Sintaxis**:
    * `sudo cp`: Copia un archivo con privilegios de superusuario.
    * `/etc/fail2ban/jail.conf`: Ruta al archivo de configuración original de Fail2ban.
    * `/etc/fail2ban/jail.local`: Ruta donde se creará la copia para personalizaciones.
* **Explicación**: Se copia el fichero `jail.conf` a `jail.local` para poder hacer cualquier tipo de personalización sin modificar el original.
* **Objetivo**: Crear una copia de trabajo del archivo de configuración para realizar modificaciones sin afectar el archivo original.

* **Comando (Editar)**: `sudo nano /etc/fail2ban/jail.local`
* **Sintaxis**:
    * `sudo nano`: Abre el editor de texto `nano` con privilegios de superusuario.
    * `/etc/fail2ban/jail.local`: Ruta al archivo de configuración que vamos a editar.
* **Explicación**: Se abre el fichero `jail.local` para modificar la configuración. Dentro de este, se buscará la sección que habla de SSHD.
* **Objetivo**: Personalizar las reglas de Fail2ban.

**Paso 3: Modificar la Configuración del Servicio SSH (Jail `sshd`)**

Dentro del archivo `jail.local`, en la sección `[sshd]`, se realizan las siguientes modificaciones:

* `enabled = true`:
    * **Explicación**: Activa el servicio, con lo cual va a monitorizar el puerto SSH estándar.
    * **Objetivo**: Habilitar la protección para el servicio SSH.
* `port = ssh`:
    * **Explicación**: Especifica que se monitorizará el puerto estándar de SSH.
    * **Objetivo**: Indicar a Fail2ban que monitoree los intentos de conexión al servicio SSH.
* `filter = sshd`:
    * **Explicación**: Utiliza el filtro `sshd` predefinido que se basa en un archivo de registro para detectar intentos fallidos de inicio de sesión SSH.
    * **Objetivo**: Especificar el patrón de búsqueda en los logs para identificar eventos de fuerza bruta en SSH.
* `logpath = /var/log/auth.log`:
    * **Explicación**: Indica a Fail2ban que lea los eventos de autenticación del archivo `/var/log/auth.log`.
    * **Objetivo**: Decir a Fail2ban dónde encontrar la información relevante para detectar los ataques.
* `maxretry = 3`:
    * **Explicación**: Define el número de intentos fallidos permitidos antes de banear la IP. Se cambió de 5 a 3 para que se active Fail2ban antes que la configuración interna de SSH.
    * **Objetivo**: Definir el umbral de tolerancia para los intentos de autenticación.
* `bantime = 600`:
    * **Explicación**: Define el tiempo en segundos (600 segundos = 10 minutos) en la que la IP será baneada.
    * **Objetivo**: Especificar por cuánto tiempo una IP será bloqueada del servicio.

**Paso 4: Reiniciar el Servicio Fail2ban**

Para que los cambios en la configuración surtan efecto, el servicio Fail2ban debe ser reiniciado.

* **Comando**: `sudo systemctl restart fail2ban`
* **Sintaxis**:
    * `sudo systemctl`: Comando para controlar el sistema y los servicios.
    * `restart`: Acción para reiniciar un servicio.
    * `fail2ban`: Nombre del servicio a reiniciar.
* **Explicación**: Reinicia el servicio de Fail2ban para que cargue la nueva configuración y comience a aplicar las reglas.
* **Objetivo**: Aplicar las nuevas reglas de baneo y monitorización configuradas.

**Paso 5: Verificar el Estado de Fail2ban**

Es importante confirmar que Fail2ban está funcionando correctamente y que la jaula `sshd` está activa.

* **Comando**: `sudo fail2ban-client status`
* **Sintaxis**:
    * `sudo fail2ban-client`: Herramienta de línea de comandos para interactuar con el demonio de Fail2ban.
    * `status`: Muestra un resumen del estado de Fail2ban, incluyendo el número de jaulas activas y sus nombres.
* **Explicación**: Al ejecutar este comando, se debe ver que el "Number of jail" es 1 y la "Jail list" incluye `sshd`, lo que confirma que está correcto.
* **Objetivo**: Confirmar que Fail2ban está corriendo y que el servicio `sshd` está siendo monitorizado.

#### 3.1.2. Ataque desde la Máquina Atacante

La máquina atacante, con IP `10.211.55.15`, intentará realizar un ataque de fuerza bruta SSH contra el servidor (`10.211.55.14`).

**Paso 1: Verificar Conectividad**

Antes del ataque, se verifica que hay conectividad de red entre las dos máquinas.

* **Comando (en máquina atacante)**: `ping 10.211.55.14`
* **Sintaxis**:
    * `ping`: Envía paquetes ICMP a una dirección IP de destino para probar la conectividad de red.
    * `10.211.55.14`: La dirección IP del servidor víctima.
* **Explicación**: Se envían paquetes `ping` para asegurarse de que la máquina atacante puede alcanzar el servidor. Si hay respuesta, la conectividad es exitosa.
* **Objetivo**: Confirmar que existe una ruta de red y comunicación básica entre el atacante y la víctima.

**Paso 2: Intentos de Ataque SSH de Fuerza Bruta**

Desde la máquina atacante, se intentan múltiples conexiones SSH con credenciales incorrectas.

* **Comando (en máquina atacante)**: `ssh usuario_ficticio@10.211.55.14`
* **Sintaxis**:
    * `ssh`: Cliente SSH para establecer conexiones seguras.
    * `usuario_ficticio`: Un nombre de usuario ficticio (inexistente).
    * `@10.211.55.14`: La dirección IP del servidor SSH al que se intenta conectar.
* **Explicación**: El atacante intentará repetidamente iniciar sesión SSH, introduciendo contraseñas incorrectas. Con `maxretry` configurado en 3 en Fail2ban, después del tercer intento fallido desde la misma IP, Fail2ban debería banear la dirección IP de la máquina atacante.
* **Objetivo**: Simular un ataque de fuerza bruta para activar las reglas de baneo de Fail2ban en el servidor. En un principio, el servicio SSH corta la conexión al cuarto intento por su propia configuración, pero al cambiar `maxretry` de Fail2ban a 3, se activará Fail2ban antes.

#### 3.1.3. Verificación del Baneo en la Máquina Víctima (Servidor)

Después de los intentos de ataque, se verifica si Fail2ban ha baneado la IP del atacante.

**Paso 1: Consultar el Estado de la Jaula `sshd`**

* **Comando**: `sudo fail2ban-client status sshd`
* **Sintaxis**:
    * `sudo fail2ban-client`: Herramienta de línea de comandos de Fail2ban.
    * `status sshd`: Muestra el estado detallado de la jaula específica `sshd`.
* **Explicación**: Este comando proporciona información granular sobre el servicio SSH monitorizado por Fail2ban, incluyendo el número de intentos fallidos (`Total failed`), las IPs actualmente baneadas (`Currently banned`), y la lista de IPs baneadas (`Banned IP List`). Se debe observar que hay una IP baneada, que es la `10.211.55.15`.
* **Objetivo**: Confirmar que Fail2ban ha detectado los intentos fallidos y ha baneado la dirección IP del atacante.

**Paso 2: (Opcional) Desbanear la Dirección IP**

Si se necesita restaurar el acceso para una IP baneada, se puede desbanear manualmente.

* **Comando**: `sudo fail2ban-client set sshd unbanip 10.211.55.15`
* **Sintaxis**:
    * `sudo fail2ban-client`: Herramienta de línea de comandos de Fail2ban.
    * `set sshd`: Indica que se va a modificar la configuración de la jaula `sshd`.
    * `unbanip`: La acción para desbanear una dirección IP.
    * `10.211.55.15`: La dirección IP específica a desbanear.
* **Explicación**: Este comando elimina la IP especificada de la lista de IPs baneadas por la jaula `sshd`, permitiéndole intentar conectar de nuevo.
* **Objetivo**: Revocar un baneo temporal o permanente para una dirección IP específica.

**Paso 3: (Opcional) Monitorizar los Logs de Fail2ban**

Para ver la actividad de Fail2ban en tiempo real, se puede monitorizar su archivo de log.

* **Comando**: `sudo tail -f /var/log/fail2ban.log`
* **Sintaxis**:
    * `sudo tail`: Muestra las últimas líneas de un archivo.
    * `-f`: Sigue el archivo, mostrando nuevas líneas a medida que se añaden (útil para monitoreo en tiempo real).
    * `/var/log/fail2ban.log`: Ruta al archivo de log principal de Fail2ban.
* **Explicación**: Este comando permite observar cómo Fail2ban detecta los intentos fallidos (`Found`), aplica el baneo (`Ban`), y revoca el baneo (`Unban`) en tiempo real, proporcionando una visión clara de su funcionamiento.
* **Objetivo**: Depurar y entender la lógica de detección y acción de Fail2ban.

## Conclusión sobre IPv6, Zero Trust y Fail2ban

Estos componentes son un excelente ejemplo de lo que constituye una **arquitectura Zero Trust**.

* **IPv6** representa un avance significativo en la seguridad de redes gracias a características como **IPsec integrado** y encabezados de paquetes simplificados, lo que ofrece mayor protección contra ataques y violaciones de datos.
* Sin embargo, para garantizar una seguridad completa de toda la información, es fundamental implementar una filosofía de **Zero Trust o confianza cero**. Este enfoque implica que **ninguna entidad, ya sea interna o externa a la red, debe ser confiada por defecto**, requiriendo una verificación continua de identidad y autorización para acceder a recursos de red.
* Al adoptar los principios de Zero Trust, las organizaciones pueden mitigar eficazmente amenazas internas y externas, reducir el riesgo de **brechas de seguridad** y proteger los **datos sensibles** frente a posibles ataques. Herramientas como Fail2ban encarnan este principio al aplicar límites de acceso estrictos: incluso si las IPs están dentro del sistema o bajo el control de la intranet, si superan un límite de intentos fallidos, se banearán, eliminando la confianza por defecto.

En resumen, la combinación de protocolos de red modernos, filosofías de seguridad rigurosas y herramientas de defensa activa crea una postura de ciberseguridad robusta y resiliente, esencial en el entorno de amenazas actual.