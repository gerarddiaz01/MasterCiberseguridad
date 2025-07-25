# Informe: Ejercicio Práctico de Neighbor Spoofing en Redes IPv6

## 1\. Contexto y Objetivo del Ejercicio

Este ejercicio práctico se centró en la comprensión y ejecución del ataque de **Neighbor Spoofing** (o envenenamiento de vecinos) en un entorno de red IPv6. El objetivo principal fue aprender a manipular el Protocolo de Descubrimiento de Vecinos (NDP) para redirigir el tráfico entre dos máquinas víctimas a través de una máquina atacante, simulando un ataque de **Hombre en el Medio (Man-in-the-Middle - MitM)**.

Para la realización de este ejercicio, se utilizó un entorno de laboratorio virtual compuesto por tres máquinas virtuales:

  * **Máquina Atacante: Kali Linux VM**

      * Interfaz: `eth0`
      * Dirección IPv6 Link Local: `fe80::a00:27ff:fe2e:c1a9`
      * Rol: Ejecutar las herramientas de ataque (`thc-ipv6`) y capturar el tráfico (`Wireshark`).

  * **Víctima 1: Ubuntu Server Lab VM**

      * Interfaz: `enp0s3`
      * Dirección IPv6 Link Local: `fe80::a00:27ff:fea8:ffc0`
      * Rol: Primera víctima del ataque, cuyo tráfico sería interceptado.

  * **Víctima 2: Ubuntu Server Lab II VM**

      * Interfaz: `enp0s3`
      * Dirección IPv6 Link Local: `fe80::a00:27ff:fed2:2e90`
      * Rol: Segunda víctima del ataque, cuyo tráfico también sería interceptado.

El ejercicio planteó las siguientes directrices:

  * Configurar los dispositivos en la misma red IPv6.
  * Instalar y configurar el THC IPv6 toolkit en la máquina atacante.
  * Identificar la dirección IPv6 de las máquinas víctimas.
  * Utilizar el módulo de envenenamiento de vecinos (`parasite6`) del THC IPv6 toolkit para forjar mensajes NS o NA y engañar a las víctimas.
  * Capturar y analizar el tráfico de red con Wireshark para verificar la redirección del tráfico.

**Podemos hacer el ejercicio de dos maneras, o usamos el comando `sudo atk6-parasite6 eth0 <IP_Victima_1> <IP_Victima_2>` para engañar a las victimas y hacer creer que nuestro MAC es el MAC de la otra victima para que nos envien a nosotros la información. O podemos usar el comando `sudo atk6-parasite6 eth0` para primero identificar los hosts presentes en el servidor (como haría el comando `atk6-alive6`) y luego empezar a enviar una inundación continua de mensajes Neighbor Advertisement (NA) falsificados, para anunciarse a sí misma (la MAC del atacante) como poseedora de las direcciones IPv6 de los hosts descubiertos, y también actuar como un interceptor general para mensajes Neighbor Solicitation (NS) que escuche en la interfaz, respondiendo a ellos con NAs forjados. La diferencia entre ambos comandos es que el primer es más específico entre dos maquinas en concreto y el segundo es más amplio y puede afectar a múltiples hosts en el segmento.**

## 2\. Desarrollo del Ejercicio Paso a Paso

El ejercicio se llevó a cabo siguiendo una serie de pasos que incluyeron la configuración de la red virtual, la instalación de herramientas y la ejecución del ataque.

### 2.1. Configuración de la Red Host-Only para Todas las VMs

Para asegurar un entorno de laboratorio aislado y fiable donde la comunicación Link Local IPv6 fuera consistente, las tres máquinas virtuales fueron configuradas para utilizar una **"Red solo-anfitrión" (Host-only Network)** en VirtualBox. Esto es crucial, ya que las direcciones Link Local (`fe80::`) solo son válidas dentro del mismo segmento de red local y no se enrutan.

  * **Acciones Realizadas:**
    1.  **Apagado de VMs:** Todas las VMs (`Kali Linux`, `Ubuntu Server Lab`, `Ubuntu Server Lab II`) fueron completamente apagadas.
    2.  **Configuración de Red Host-only:** En el **VirtualBox Manager**, se verificó/creó una "Red solo-anfitrión" (ej., `vboxnet0`) en `Archivo > Preferencias > Red`. Se aseguró que el servidor DHCP de esta red estuviera **deshabilitado**.
    3.  **Asignación a VMs:** Para **cada una de las tres VMs**, en `Configuración > Red > Adaptador 1`, se configuró "Conectado a:" como **"Red solo-anfitrión"**, se seleccionó `vboxnet0` en el campo "Nombre:", y se estableció "Modo promiscuo:" en "Permitir todo". Se aseguró que no hubiera otros adaptadores habilitados para evitar interferencias.

### 2.2. Verificación de la Conectividad IPv6 Link Local

Una vez configurada la red solo-anfitrión, se inició cada VM y se verificaron sus direcciones IPv6 Link Local y la conectividad cruzada.

  * **Identificación de Direcciones IPv6 Link Local:**

      * En cada VM, se ejecutó `ip -6 address show` para obtener la dirección `fe80::` y el nombre de la interfaz principal.
          * **Kali Linux VM:** `eth0` - `fe80::a00:27ff:fe2e:c1a9`
          * **Ubuntu Server Lab VM:** `enp0s3` - `fe80::a00:27ff:fea8:ffc0`
          * **Ubuntu Server Lab II VM:** `enp0s3` - `fe80::a00:27ff:fed2:2e90`

  * **Realización de Pings Cruzados:**

      * Se ejecutaron pings `ping -6 -c 3 <IP_Destino>%<Interfaz_Origen>` desde cada VM hacia las otras dos. Todos los pings resultaron en **0% de pérdida de paquetes**, confirmando la conectividad total Link Local entre las tres máquinas en la red aislada.

### 2.3. Instalación del THC IPv6 Toolkit en Kali Linux VM

Dado que Kali Linux VM estaba ahora en una red aislada sin acceso a Internet, la instalación del THC IPv6 toolkit requería un método alternativo.

  * **Acciones Realizadas:**
    1.  **Descarga en Anfitrión:** Se descargó el paquete `.deb` de `thc-ipv6` (ej., `thc-ipv6_2.8.1-2_amd64.deb`) en la máquina anfitriona Ubuntu (que sí tenía Internet).
    2.  **Configuración de Carpeta Compartida:** En VirtualBox, se configuró una "Carpeta Compartida" entre el Ubuntu Anfitrión y la Kali Linux VM. Se seleccionó la carpeta en el anfitrión que contenía el archivo `.deb` (ej., `~/Downloads`), se le dio un nombre (ej., `sf_kali_shared`), y se marcó "Automontar" y "Hacer permanente".
    3.  **Acceso y Montaje en Kali:** Dentro de Kali Linux VM, el archivo `.deb` se hizo visible en `/media/sf_kali_shared/`.
    4.  **Instalación del Toolkit:** En la terminal de Kali, se navegó a la carpeta compartida y se instaló el paquete:
        ```bash
        sudo dpkg -i thc-ipv6_*.deb
        ```
          * `sudo dpkg -i`: Instala paquetes `.deb` directamente.
    5.  **Verificación de Instalación:** Se verificó que las herramientas `atk6-parasite6` y `atk6-alive6` estaban disponibles:
        ```bash
        which atk6-parasite6
        which atk6-alive6
        ```
        Ambos comandos devolvieron sus rutas de ejecución (ej., `/usr/bin/atk6-parasite6`), confirmando la instalación.

### 2.4. Habilitación de IP Forwarding en Kali Linux VM

Para que el atacante (Kali) pueda redirigir el tráfico una vez interceptado (evitando una denegación de servicio), es necesario habilitar el reenvío de paquetes IPv6 en su kernel.

  * **Comando:**
    ```bash
    sudo sysctl -w net.ipv6.conf.all.forwarding=1
    ```
      * `sudo sysctl -w`: Modifica los parámetros del kernel.
      * `net.ipv6.conf.all.forwarding=1`: Establece el reenvío de paquetes IPv6 a `1` (habilitado) para todas las interfaces.

### 2.5. Ejecución de `atk6-alive6` para Identificar Objetivos

Como parte de la fase de reconocimiento, se utilizó `atk6-alive6` para descubrir activamente los vecinos en la red interna.

  * **Acciones Realizadas:**
    1.  Se inició una **nueva captura en Wireshark** en la interfaz `eth0` de Kali Linux VM.
    2.  En la terminal de Kali, se ejecutó:
        ```bash
        sudo atk6-alive6 eth0
        ```
          * `atk6-alive6`: Herramienta de descubrimiento de hosts vivos en IPv6 (envía ICMPv6 Echo Request, NS, etc.).
    3.  La salida de la terminal de `atk6-alive6` confirmó la detección de las dos Ubuntu Server VMs: `Alive: fe80::a00:27ff:fed2:2e90` y `Alive: fe80::a00:27ff:fea8:ffc0`.
    4.  En Wireshark, se observó el tráfico `ICMPv6 Echo Request/Reply` y `Neighbor Solicitation/Advertisement` generado por `atk6-alive6` como parte del proceso de descubrimiento.

### 2.6. Ejecución del Ataque de Neighbor Spoofing con `atk6-parasite6`

Este es el paso central del ejercicio, donde se simula el ataque de Hombre en el Medio. `atk6-parasite6` forzará a cada víctima a creer que la IP de la otra víctima corresponde a la MAC del atacante.

  * **Comando:**

    ```bash
    sudo atk6-parasite6 eth0 fe80::a00:27ff:fea8:ffc0 fe80::a00:27ff:fed2:2e90
    ```

      * `atk6-parasite6`: Herramienta para realizar Neighbor Spoofing.
      * `eth0`: Interfaz de ataque de Kali.
      * `fe80::a00:27ff:fea8:ffc0`: IP de Víctima 1.
      * `fe80::a00:27ff:fed2:2e90`: IP de Víctima 2.
      * **Objetivo del Neighbor Spoofing:** Posicionar al atacante (Kali) como un MitM. Esto se logra enviando `Neighbor Advertisement` (NA) falsificados de forma continua. Cada NA falsificado anuncia la IP de una víctima, pero con la MAC del atacante. Así, cuando la Víctima A quiere enviar tráfico a la Víctima B, envía los paquetes a la MAC del atacante, pensando que es la MAC de B.

  * **Repercusión Hipotética en la Terminal de Kali:** Tras ejecutar el comando, la terminal de Kali hubiera mostrado mensajes continuos como "Started ICMPv6 Neighbor Solicitation Interceptor (Press Control-C to end) ..." y luego "Spoofed packet to fe80::...".

-----

## 3\. Análisis de los Resultados (Escenario Hipotético Exitoso)

A continuación, se detalla lo que hubiese ocurrido y lo que se hubiese observado en las víctimas y en Wireshark si el ataque de Neighbor Spoofing hubiera sido completamente exitoso.

### 3.1. Verificación del Envenenamiento en la Caché de Vecinos (`ip -6 neigh show` en las Víctimas)

Mientras `atk6-parasite6` estuviera ejecutándose en Kali:

  * **En la terminal de Ubuntu Server Lab VM (Víctima 1):**

      * **Comando:** `ip -6 neigh show`
      * **Salida Hipotética Esperada:**
        ```
        fe80::a00:27ff:fed2:2e90 dev enp0s3 lladdr 08:00:27:2e:c1:a9 REACHABLE
        # ... otras entradas ...
        ```
      * **Análisis:** La entrada para la IP de la Víctima 2 (`fe80::a00:27ff:fed2:2e90`) **hubiera mostrado la MAC del Atacante (Kali: `08:00:27:2e:c1:a9`)** en lugar de la MAC real de la Víctima 2. Esto confirmaría el envenenamiento de la caché de Víctima 1.

  * **En la terminal de Ubuntu Server Lab II VM (Víctima 2):**

      * **Comando:** `ip -6 neigh show`
      * **Salida Hipotética Esperada:**
        ```
        fe80::a00:27ff:fea8:ffc0 dev enp0s3 lladdr 08:00:27:2e:c1:a9 REACHABLE
        # ... otras entradas ...
        ```
      * **Análisis:** La entrada para la IP de la Víctima 1 (`fe80::a00:27ff:fea8:ffc0`) **hubiera mostrado la MAC del Atacante (Kali: `08:00:27:2e:c1:a9`)** en lugar de la MAC real de la Víctima 1. Esto confirmaría el envenenamiento de la caché de Víctima 2.

### 3.2. Verificación de la Redirección del Tráfico con Pings y Wireshark

Mientras `atk6-parasite6` se ejecutara y Wireshark capturara en la interfaz `eth0` de Kali:

  * **Tráfico Generado:** Desde la terminal de Ubuntu Server Lab VM (Víctima 1), se ejecutaría un ping a Ubuntu Server Lab II VM (Víctima 2):

    ```bash
    ping -6 -c 3 fe80::a00:27ff:fed2:2e90%enp0s3
    ```

      * **Resultado Hipotético:** Estos pings **hubieran funcionado y recibido respuestas (`0% packet loss`)**, ya que el atacante (Kali) estaría reenviando el tráfico.

  * **Observación y Análisis en Wireshark (en Kali Linux VM):**

      * **Filtro Wireshark:** `icmpv6 and ipv6.addr == fe80::a00:27ff:fea8:ffc0 and ipv6.addr == fe80::a00:27ff:fed2:2e90`

      * **Análisis Hipotético (Traza del Paquete Man-in-the-Middle en Wireshark):**
        En Wireshark, se hubieran observado los mensajes `ICMPv6 Echo Request` y `Echo Reply` del ping pasando por Kali, revelando la redirección en la capa 2 (Ethernet), mientras que las IPs de la capa 3 (IPv6) permanecerían inalteradas.

        1.  **Paquete 1 (ICMPv6 Echo Request - Víctima 1 -\> Atacante -\> Víctima 2):**

              * **De Víctima 1 a Atacante (Primera parte del paquete):**
                  * `Ethernet II Source MAC`: MAC REAL de Víctima 1 (`08:00:27:a8:ff:c0`)
                  * `Ethernet II Destination MAC`: MAC del Atacante (`08:00:27:2e:c1:a9`) (Debido a la caché envenenada de Víctima 1).
                  * `Internet Protocol Version 6 Source IP`: IP de Víctima 1 (`fe80::a00:27ff:fea8:ffc0`)
                  * `Internet Protocol Version 6 Destination IP`: IP de Víctima 2 (`fe80::a00:27ff:fed2:2e90`)
                  * `ICMPv6 Type`: `Echo (ping) request (128)`
              * **Del Atacante a Víctima 2 (Segunda parte del paquete, reenviado por Kali):**
                  * `Ethernet II Source MAC`: MAC del Atacante (`08:00:27:2e:c1:a9`)
                  * `Ethernet II Destination MAC`: MAC REAL de Víctima 2 (`08:00:27:d2:2e:90`) (Kali conoce la MAC real de Víctima 2).
                  * `Internet Protocol Version 6 Source IP`: IP de Víctima 1
                  * `Internet Protocol Version 6 Destination IP`: IP de Víctima 2
                  * `ICMPv6 Type`: `Echo (ping) request (128)`

        2.  **Paquete 2 (ICMPv6 Echo Reply - Víctima 2 -\> Atacante -\> Víctima 1):** (Proceso inverso)

              * **De Víctima 2 a Atacante:**
                  * `Ethernet II Source MAC`: MAC REAL de Víctima 2 (`08:00:27:d2:2e:90`)
                  * `Ethernet II Destination MAC`: MAC del Atacante (`08:00:27:2e:c1:a9`) (Debido a la caché envenenada de Víctima 2).
                  * `Internet Protocol Version 6 Source IP`: IP de Víctima 2
                  * `Internet Protocol Version 6 Destination IP`: IP de Víctima 1
                  * `ICMPv6 Type`: `Echo (ping) reply (129)`
              * **Del Atacante a Víctima 1:**
                  * `Ethernet II Source MAC`: MAC del Atacante (`08:00:27:2e:c1:a9`)
                  * `Ethernet II Destination MAC`: MAC REAL de Víctima 1 (`08:00:27:a8:ff:c0`)
                  * `Internet Protocol Version 6 Source IP`: IP de Víctima 2
                  * `Internet Protocol Version 6 Destination IP`: IP de Víctima 1
                  * `ICMPv6 Type`: `Echo (ping) reply (129)`

        **Análisis de la Traza Hipotética:** La clave del éxito del ataque de "Hombre en el Medio" se hubiera revelado en la **manipulación de las direcciones MAC de la Capa 2**. Observaríamos que, para el tráfico entre las víctimas, la dirección MAC de destino en los paquetes que se envían *hacia* el atacante es siempre la MAC del atacante, y la dirección MAC de origen en los paquetes que el atacante reenvía *desde sí mismo* es también la suya. Esto confirmaría que la Kali VM está interceptando y redirigiendo el tráfico con éxito.


Aquí tienes la información detallada sobre el modo de operación de `atk6-parasite6` sin especificar las IPs de las víctimas, formateada como una sección Markdown, pero **sin citas ni referencias a las fuentes**, tal como lo has solicitado.

---

### Modo de Operación Específico de `atk6-parasite6` (Sin Direcciones IPv6 de Víctima)

Durante la resolución del ejercicio, el profesor demostró la ejecución del ataque de Neighbor Spoofing utilizando el comando `sudo atk6-parasite6 eth0`, sin especificar las direcciones IPv6 de las máquinas víctima. Esta observación es crucial, ya que revela una forma de operación más amplia y automatizada de la herramienta, distinta al ataque más dirigido que habíamos intentado previamente.

1.  **Comportamiento de `atk6-parasite6 <interface>` (Modo Automático/Indiscriminado):**
    Cuando `atk6-parasite6` se ejecuta únicamente con el nombre de la interfaz (ej., `eth0`), la herramienta opera en un modo más generalizado de envenenamiento o interceptación.
    * **Descubrimiento Automático:** En este modo, `atk6-parasite6` primero identifica activamente los hosts IPv6 presentes en el segmento de red local.
    * **Inundación General de `Neighbor Advertisement` (NA) Falsificados:** Una vez que ha descubierto los hosts activos (incluidas las víctimas y potencialmente el router), `atk6-parasite6` comienza a enviar una inundación continua de mensajes `Neighbor Advertisement` (NA) falsificados. Sin especificar IPs de víctimas, la herramienta a menudo:
        * Se anuncia a sí misma (la MAC del atacante) como poseedora de las direcciones IPv6 de los hosts descubiertos. Esto puede incluir las IPs de las víctimas, la IP del router, o cualquier otra IP activa en el segmento.
        * Puede, adicionalmente, actuar como un interceptor general para mensajes `Neighbor Solicitation` (NS) que escuche en la interfaz, respondiendo a ellos con NAs forjados.
    * **Diferencia clave:** A diferencia de nuestro intento anterior, que buscaba un ataque "dirigido" entre dos hosts específicos, este modo es más amplio y puede afectar a múltiples hosts en el segmento.

2.  **Por qué este Modo Permite Capturar Pings entre Víctimas (sin Especificar IPs):**
    El éxito de este modo radica en su capacidad para envenenar de forma generalizada las cachés de vecinos en el segmento de red local.
    * **Envenenamiento Generalizado:** Si `atk6-parasite6` logra inundar el segmento con NAs falsificados que asocian las IPs de ambas víctimas con la MAC del atacante, las cachés de vecinos de ambas víctimas serán envenenadas.
    * **Redirección del Tráfico:** Cuando la Víctima 1 intenta hacer `ping` a la Víctima 2, buscará la MAC de la Víctima 2 en su caché de vecinos. Al estar envenenada, encontrará la MAC del Atacante. Por lo tanto, enviará el paquete ICMPv6 Echo Request a la MAC del Atacante. El Atacante (con el reenvío de IP habilitado) recibirá este paquete y lo reenviará a la MAC real de la Víctima 2. El proceso se repite en la respuesta de la Víctima 2 a la Víctima 1.
    * **Confirmación en Wireshark:** Al capturar el tráfico en la interfaz del Atacante, se observarían tanto las solicitudes como las respuestas de `ping` entre las víctimas pasando por ella, confirmando el "Hombre en el Medio".

3.  **Implicación Clave:**
    El hecho de que este modo funcione sin especificar objetivos directos demuestra que `atk6-parasite6` es muy efectivo para realizar un envenenamiento generalizado en el segmento Link Local y, por lo tanto, lograr la redirección del tráfico. Esto implica que la herramienta "descubre" los hosts y luego los "parasita" de forma automática.


## 4\. Importancia de Entender el Neighbor Spoofing para un Analista de Ciberseguridad

El ejercicio de Neighbor Spoofing, aunque simulado, ilustra un concepto de seguridad de red extremadamente importante. Un analista de ciberseguridad debe entender esto por varias razones:

1.  **Fundamentos de Protocolos (IPv6 y NDP):** Permite una comprensión profunda de cómo funciona la capa de enlace y red en IPv6. Saber que NDP (`Neighbor Solicitation` y `Neighbor Advertisement` mensajes) es esencial para la resolución de direcciones (`fe80::` a MAC) y el descubrimiento de vecinos (`alive6` lo usa) es vital. La manipulación de estos mensajes es la base del ataque.

2.  **Detección de Ataques MitM:** El Neighbor Spoofing es la base de muchos ataques de "Hombre en el Medio". Al entender cómo funciona el ataque y qué se ve en la red (cambios en la caché NDP, MACs incorrectas asociadas a IPs, tráfico inesperado pasando por un punto), un analista puede:

      * **Identificar anomalías:** Observar entradas `STALE` o `FAILED` inusuales en `ip -6 neigh show`, o detectar cambios inesperados de MAC para IPs críticas.
      * **Usar Wireshark para Forensia:** Si se sospecha un MitM, la captura de tráfico es la prueba definitiva. Filtrar por `icmpv6.type == 135 or icmpv6.type == 136` revelaría mensajes NS/NA sospechosos. La clave es ver si el `Source MAC` de un `Neighbor Advertisement` no coincide con la MAC real del host que posee la `Source IP`. Y lo más importante, verificar que el tráfico entre dos hosts está tomando un camino inesperado a través de una MAC de atacante en la capa 2, mientras las IPs de la capa 3 siguen siendo las originales.

3.  **Evaluación de la Seguridad de Red:** Un analista puede replicar este ataque (con autorización) para probar la vulnerabilidad de una red. Si el spoofing funciona, indica una debilidad en la configuración de seguridad de la red local.

4.  **Implementación de Defensas:** Conociendo este ataque, un analista puede recomendar e implementar medidas de mitigación:

      * **Autenticación de Mensajes NDP (SEND - Secure Neighbor Discovery):** Esto añade criptografía a los mensajes NDP, haciendo que el spoofing sea extremadamente difícil.
      * **Inspección Dinámica de ARP/NDP (DAI/NDP Snooping):** En switches gestionados, se pueden habilitar funciones que monitorean y validan las asociaciones IP-MAC, bloqueando mensajes falsificados.
      * **Segmentación de Red:** Limitar el tamaño de los dominios de difusión donde estos ataques pueden operar.
      * **Monitoreo Continuo:** Implementar sistemas IDS/IPS que detecten inundaciones de NAs o cambios rápidos en las cachés de vecinos.

5.  **Comprensión de las Tácticas de los Adversarios:** Los "malos" (hackers maliciosos) utilizan el Neighbor Spoofing como un paso fundamental para:

      * **Interceptar credenciales:** Si el tráfico (ej., HTTP sin cifrar) pasa por ellos, pueden ver nombres de usuario y contraseñas.
      * **Inyectar código:** Modificar el tráfico en tiempo real (ej., inyectar JavaScript en páginas web).
      * **Redirigir a sitios falsos (phishing):** Desviar a los usuarios a sitios maliciosos.
      * **Realizar ataques de Denegación de Servicio (DoS):** Simplemente descartando el tráfico interceptado.
      * **Realizar movimiento lateral:** Obtener información sobre otros hosts en la red.

Como analista de ciberseguridad, entender cómo funcionan estos ataques a bajo nivel y cómo se ven en el tráfico de red es crucial para proteger los sistemas de manera efectiva. No se trata solo de saber que existe el "spoofing", sino de poder diagnosticarlo y visualizarlo en la "vida real" a través de herramientas como Wireshark.


