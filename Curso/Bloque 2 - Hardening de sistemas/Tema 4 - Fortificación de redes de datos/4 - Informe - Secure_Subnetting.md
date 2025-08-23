# Informe Detallado: Ejercicio de Secure Subnetting con `ipcalc` y Hardening de Sistemas

## Objetivo del Ejercicio

El propósito de este ejercicio es dividir una red existente, `192.168.1.0/24`, en subredes más pequeñas. Cada una de estas nuevas subredes debe tener la capacidad de alojar un mínimo de **30 hosts utilizables**. Para lograr esto, se plantean tres objetivos principales:

1.  **Determinar la máscara de subred** necesaria que permita al menos 30 hosts por subred.
2.  **Calcular el número de subredes posibles** que se pueden crear con la máscara de subred determinada.
3.  **Obtener el rango de direcciones IP** para la primera de estas subredes.

## Resolución Paso a Paso: Análisis Manual

Para resolver el ejercicio, el primer paso es comprender la red actual y aplicar los principios matemáticos del subnetting.

### 1. Entendiendo la Red Original (`192.168.1.0/24`) y el Requisito

* **Dirección de Red**: `192.168.1.0`
* **Notación CIDR `/24`**: Indica que los primeros 24 bits de la dirección IP (`192.168.1`) corresponden a la **porción de red**. Esto significa que los $32 - 24 = 8$ bits restantes (el último octeto) están disponibles para los hosts en la red original.
* **Máscara de Subred por Defecto para `/24`**: `255.255.255.0`. En binario, esto se representa como `11111111.11111111.11111111.00000000`.
* **Requisito de Hosts**: La clave del ejercicio es que cada nueva subred debe soportar **al menos 30 hosts**.

### 2. Determinando la Máscara de Subred Necesaria para 30 Hosts (Objetivo 1)

Para encontrar la máscara de subred adecuada, necesitamos determinar cuántos bits de host (`n`) son requeridos. La fórmula para calcular el número de **hosts utilizables** en una subred es $2^n - 2$. El "menos 2" se debe a que dos direcciones están reservadas: una para la **dirección de red** (la primera dirección de la subred) y otra para la **dirección de broadcast** (la última dirección de la subred).

Probamos valores para `n` (número de bits de host):

* Si `n = 4`: $2^4 - 2 = 16 - 2 = 14$ hosts. (Insuficiente para 30).
* Si `n = 5`: $2^5 - 2 = 32 - 2 = 30$ hosts. (¡Este valor cumple exactamente el requisito de "al menos 30 hosts"!).

Por lo tanto, necesitamos **5 bits para la porción de host** en cada nueva subred.

Ahora, calculamos la nueva longitud de la porción de red (el nuevo prefijo CIDR):
* Total de bits en una dirección IPv4 = 32 bits.
* Bits de red = Total de bits - Bits de host = $32 - 5 = 27$ bits.

Esto nos da una nueva notación **CIDR de `/27`**.

Finalmente, convertimos la notación `/27` a la máscara de subred decimal:
Una máscara `/27` significa que los primeros 27 bits son '1' y los últimos 5 bits son '0'.
* En binario: `11111111.11111111.11111111.11100000`
* Convertimos a decimal: `255.255.255.224`.

La **máscara de subred necesaria** es `255.255.255.224`.

### 3. Calculando el Número de Subredes Posibles (Objetivo 2)

La red original era `/24` (24 bits de red) y nuestra nueva subred es `/27` (27 bits de red). La diferencia entre estos dos números nos indica cuántos bits "hemos tomado prestados" de la porción de host original para usarlos en la creación de subredes.

* Bits prestados para subredes = Nueva longitud de prefijo - Longitud de prefijo original = $27 - 24 = 3$ bits.

El número de subredes posibles se calcula con la fórmula $2^m$, donde `m` es el número de bits prestados.

* Número de subredes = $2^3 = 8$ subredes.

### 4. Obteniendo el Rango de Direcciones IP para la Primera Subred (Objetivo 3)

Para determinar el rango de direcciones, primero calculamos el "tamaño del bloque" o el incremento de direcciones entre una subred y la siguiente. Este se obtiene restando el valor decimal del último octeto de la nueva máscara de subred de 256.

* Tamaño del bloque (incremento) = $256 - 224 = 32$.
    (Alternativamente, es $2^{\text{bits de host}} = 2^5 = 32$).

Esto significa que cada subred tendrá un rango de 32 direcciones IP, y las subredes comenzarán con múltiplos de 32 en el último octeto.

Ahora, definamos el rango para la **primera subred** con la máscara `/27`:

* **Dirección de Red**: `192.168.1.0/27`. Esta es la dirección que identifica la subred.
* **Primera Dirección IP Utilizable (HostMin)**: Es la dirección de red + 1. `192.168.1.1`. Esta es la primera dirección que se puede asignar a un dispositivo.
* **Última Dirección IP Utilizable (HostMax)**: Es la dirección de broadcast - 1. En este caso, `192.168.1.30`. Esta es la última dirección que se puede asignar a un dispositivo.
* **Dirección de Broadcast**: La última dirección dentro de la subred. Como la siguiente subred comienza en `.32`, la dirección anterior es el broadcast. Por lo tanto, `192.168.1.31`.

## Verificación con `ipcalc` en la Terminal de Linux

El proceso de subnetting puede ser propenso a errores manuales, por lo que herramientas como `ipcalc` son esenciales para verificar los cálculos y realizar la operación de manera efectiva y precisa.

### 1. Instalación de `ipcalc`

Antes de usar `ipcalc`, es necesario instalarlo en el sistema.

* **Comando**: `sudo apt install ipcalc`
* **Sintaxis**:
    * `sudo`: Permite ejecutar el comando con privilegios de superusuario, lo cual es necesario para instalar paquetes en sistemas basados en Debian/Ubuntu.
    * `apt`: Es el gestor de paquetes de Debian/Ubuntu.
    * `install`: La acción para instalar un paquete.
    * `ipcalc`: El nombre del paquete a instalar.
* **Objetivo**: Instalar la utilidad `ipcalc` en el sistema para poder realizar cálculos de red.
* **Resultado Esperado**: El sistema descargará e instalará el paquete `ipcalc`, confirmando la instalación exitosa.

### 2. Ejecución de `ipcalc` para el Ejercicio

Una vez instalado, podemos ejecutar `ipcalc` para verificar nuestros cálculos manuales.

* **Comando**: `ipcalc 192.168.1.0/24 -s 30`
* **Sintaxis**:
    * `ipcalc`: El nombre de la herramienta.
    * `192.168.1.0/24`: La dirección de red original junto con su máscara CIDR actual. `ipcalc` la utilizará como base para la subdivisión.
    * `-s 30`: Este argumento le indica a `ipcalc` que queremos subredes que puedan soportar **al menos 30 hosts**. La herramienta calculará automáticamente la máscara de subred más eficiente para cumplir con este requisito.
* **Objetivo**: Verificar los cálculos manuales de la máscara de subred, el número de subredes posibles y el rango de direcciones para la primera subred, basándose en el requisito de hosts.
* **Resultado de la Salida de `ipcalc`**:
    La salida de `ipcalc` se divide en varios bloques informativos.

    * **Primer Bloque (Información de la red original)**:
        * `Address`: `192.168.1.0`
        * `Netmask`: `255.255.255.0` (`/24`)
        * `Hosts/Net`: `254` (Número de hosts utilizables en la red original).
        * `Class`: `C, Private Internet`.
        * `HostMin`: `192.168.1.1`.
        * `HostMax`: `192.168.1.254`.
        * `Broadcast`: `192.168.1.255`.
        * Esta sección confirma la información inicial de la red y su capacidad antes de la subdivisión.

    * **Segundo Bloque (Subredes Requeridas para 30 Hosts)**:
        * `Requested size`: `30 hosts`.
        * `Needed size`: `32 addresses` (esto incluye la dirección de red y la de broadcast, lo que resulta en 30 hosts utilizables).
        * `Netmask`: `255.255.255.224` (`/27`). Esto coincide perfectamente con nuestro cálculo manual.
        * `Network`: `192.168.1.0` (La dirección de la primera subred).
        * `HostMin`: `192.168.1.1`.
        * `HostMax`: `192.168.1.30`.
        * `Broadcast`: `192.168.1.31`.
        * `Hosts/Net`: `30` (confirmando el número de hosts utilizables por subred).
        * Este bloque muestra el resultado del cálculo de `ipcalc` para cumplir con el requisito de 30 hosts, validando nuestros cálculos manuales. También confirma que la división de la red original resulta en 8 subredes posibles (`2^3`).

    * **Tercer Bloque (Subredes no utilizadas)**:
        * `Unused`: Aquí `ipcalc` puede mostrar las subredes que no se han utilizado o que tienen un tamaño diferente a la requerida si la solicitud fuera para un número exacto de subredes, o si la división no aprovecha toda la red original con la misma máscara. En este caso, muestra las direcciones de las subredes que siguen a la primera calculada: `192.168.1.32/27`, `192.168.1.64/26`, `192.168.1.128/25`. Esto es una representación de cómo la red podría ser subdividida con diferentes máscaras, indicando una mayor cantidad de direcciones para subred con una máscara numéricamente menor.

## Importancia del Subnetting para el Hardening de Sistemas

La **segmentación de redes** mediante subnetting es una práctica crítica en la gestión y, sobre todo, en la seguridad de redes. Va mucho más allá de la mera organización de direcciones IP; es una estrategia fundamental para el **hardening de sistemas** y la **resiliencia de la infraestructura**.

### 1. Mejora de la Seguridad y Reducción del Riesgo

* **Aislamiento de Zonas**: Cada subred actúa como una **zona aislada**. Esto significa que si un segmento de la red se ve comprometido (por un ataque de **Malware**, un **Exploit**, o un **Insider** malicioso), el impacto se limita a esa subred específica, dificultando la propagación lateral del ataque al resto de la infraestructura. Por ejemplo, los servidores críticos, bases de datos o sistemas de administración pueden ubicarse en subredes separadas con políticas de seguridad más estrictas.
* **Reducción del Dominio de Broadcast**: Al dividir una red grande en subredes más pequeñas, se reduce el **dominio de broadcast**. Esto minimiza la cantidad de tráfico de difusión en la red, lo que no solo mejora el rendimiento sino que también reduce la superficie de ataque para ciertos tipos de ataques que dependen del tráfico de broadcast, como el **ARP Spoofing**.
* **Control Granular de Acceso**: La segmentación facilita la implementación de **políticas de seguridad diferenciadas**. Esto permite un **control más granular del acceso** y los recursos. Por ejemplo, se pueden aplicar **firewall rules** específicas entre subredes para permitir solo el tráfico necesario entre ellas, implementando el principio de **mínimo privilegio**.

### 2. Rendimiento y Gestión Mejorados

* **Optimización del Rendimiento**: Al reducir el tráfico de broadcast y crear redes más pequeñas y manejables, se optimiza el rendimiento general de la red, disminuyendo la congestión.
* **Facilita la Gestión y Resolución de Problemas**: Un plan de subnetting bien diseñado facilita la gestión de recursos y la resolución de problemas. La identificación de dispositivos y la aplicación de políticas es más sencilla en segmentos más pequeños.

### 3. Defensa Contra Amenazas

El subnetting es una herramienta crucial para mejorar la seguridad de las redes al reducir los dominios de difusión y limitar el impacto de posibles ataques. Es fundamental para proteger la **integridad y confidencialidad de los datos** en redes empresariales, proporcionando una sólida defensa contra intrusiones y amenazas.

## Cómo los Agentes Maliciosos Podrían Explotar Debilidades

Una **topología de red mal diseñada** o una **asignación deficiente de direcciones IP y subredes** introduce serias vulnerabilidades que los agentes maliciosos (**Threat Actors**) pueden explotar.

* **Falta de Segmentación (Red Plana)**:
    * **Explotación**: Si toda la red es una sola subred grande (una "red plana"), un atacante que logre acceder a un solo dispositivo (por ejemplo, a través de **Phishing**, un **Exploit** o un **Malware**) tendrá acceso directo a *todos* los demás dispositivos en esa red.
    * **Impacto**: Esto permite un **movimiento lateral** fácil y rápido dentro de la infraestructura, lo que facilita la escalada de privilegios, el robo de datos (**Data Leaks**), la propagación de **Ransomware** o la preparación de ataques de **DDoS internos** o la búsqueda de información crítica sin impedimentos.
* **Direccionamiento IP Confuso o Indocumentado**:
    * **Explotación**: Una asignación de IP desorganizada sin un plan claro dificulta la identificación de activos críticos. Los atacantes pueden escanear la red de manera más efectiva para descubrir servicios y dispositivos sin ser detectados si no hay una segregación lógica clara.
    * **Impacto**: Retrasa la detección de intrusiones y la respuesta a incidentes, ya que es difícil determinar qué dispositivos están comprometidos o dónde se originan los problemas.
* **Puntos Únicos de Fallo (Single Points of Failure) no Protegidos**:
    * **Explotación**: En topologías como la estrella, si el dispositivo central (switch, router) no está adecuadamente fortificado (hardening deficiente, credenciales débiles, falta de monitorización), su compromiso puede paralizar toda la red.
    * **Impacto**: Un atacante podría lanzar un **DDoS** contra este dispositivo, o tomar su control para redirigir tráfico, espiar comunicaciones o deshabilitar la conectividad, causando una denegación de servicio masiva.
* **Ataques de Denegación de Servicio (DoS)**:
    * **Dominio de Broadcast Grande**: En redes no segmentadas, un ataque de **broadcast storm** o un **DHCP Starvation Attack** puede agotar rápidamente los recursos de la red o los servidores de servicios críticos, afectando a un gran número de dispositivos simultáneamente debido al amplio dominio de difusión.
    * **Impacto**: Interrupción de servicios críticos, inaccesibilidad de recursos y pérdida de productividad.
* **Falta de Políticas de Seguridad Diferenciadas**:
    * **Explotación**: Sin subredes, es más difícil aplicar listas de control de acceso (ACLs) granulares o reglas de firewall para restringir el tráfico entre diferentes tipos de dispositivos o departamentos. Esto significa que un servidor web en la misma subred que la base de datos de producción podría tener rutas de comunicación innecesariamente abiertas, aumentando el riesgo.
    * **Impacto**: Mayor superficie de ataque, permitiendo que atacantes se muevan fácilmente entre diferentes capas de la aplicación o entre sistemas con diferentes niveles de confianza.

En resumen, el subnetting no es solo una optimización de red, sino una estrategia esencial para securizar redes de datos y garantizar su eficiencia y confiabilidad en el mundo real. Al prevenir las debilidades mencionadas, se refuerza la eficiencia operativa y se mantiene una postura de seguridad robusta.