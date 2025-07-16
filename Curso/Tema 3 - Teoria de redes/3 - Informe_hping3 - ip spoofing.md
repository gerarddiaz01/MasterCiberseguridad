# Informe del Ejercicio Práctico: Generación y Análisis de Tráfico de Red con hping3 y Wireshark

## Contexto y Objetivo del Ejercicio

Este ejercicio práctico se enmarcó en el ámbito de la ciberseguridad, con el objetivo de comprender y manipular el tráfico de red a un nivel fundamental. El propósito principal fue aprender a generar diferentes tipos de paquetes de red utilizando la herramienta `hping3` y, simultáneamente, capturar y analizar dicho tráfico con `Wireshark`, verificando la composición y el comportamiento de los paquetes enviados.

Para llevar a cabo este ejercicio, se utilizaron dos máquinas virtuales (VMs) activas en un entorno virtualizado:

  * **Kali Linux VM (Atacante/Generador de Tráfico):**

      * Dirección IP: `192.168.1.240`
      * Rol: Máquina desde la cual se generaron los paquetes con `hping3` y donde se ejecutó `Wireshark` para la captura y el análisis.

  * **Ubuntu Server VM (Objetivo):**

      * Dirección IP: `192.168.1.241`
      * Rol: Máquina receptora de los paquetes generados por Kali Linux, actuando como objetivo para las pruebas de tráfico.

El objetivo específico del ejercicio, utilizando estas máquinas, fue:

  * Generar paquetes TCP.
  * Generar paquetes UDP.
  * Generar un ICMP Echo Request.
  * Modificar la dirección IP de origen (IP Spoofing) en un paquete TCP/UDP.
  * Capturar todo el tráfico generado con Wireshark y analizarlo para verificar las características de los paquetes.

## Pasos Seguidos para Realizar el Ejercicio

A continuación, se detallan los pasos para configurar el entorno y ejecutar las tareas del ejercicio.

### Fase 1: Configuración de la Conectividad entre VMs

Para que Kali Linux y Ubuntu Server pudieran comunicarse, se aseguraron de que ambos estuvieran en la misma red y tuvieran direcciones IP compatibles.

1.  **Configuración de Adaptadores de Red en VirtualBox:**

      * Ambas VMs (Kali y Ubuntu Server) fueron configuradas con el modo de red **"Adaptador Puente" (Bridged Adapter)** en VirtualBox.
      * En ambos casos, se seleccionó el **mismo adaptador de red físico activo** de la máquina anfitriona (por ejemplo, el adaptador Wi-Fi principal) y el **"Modo Promiscuo" se estableció en "Permitir todo" (Allow All)**.

2.  **Asignación de IPs Estáticas a las VMs:**
    Dado que el DHCP no funcionaba consistentemente en las VMs, se asignaron direcciones IP estáticas en la misma subred:

      * **En Kali Linux VM:**
          * Se configuró la IP `192.168.1.240` para la interfaz `eth0` mediante edición manual del archivo de configuración de red o a través de la interfaz de instalación.
      * **En Ubuntu Server VM:**
          * Se configuró la IP `192.168.1.241` para la interfaz `enp0s3` (el nombre de su interfaz principal) editando el archivo `/etc/netplan/00-installer-config.yaml`.
          * **Comando y Sintaxis:**
            ```bash
            sudo nano /etc/netplan/00-installer-config.yaml
            ```
              * `sudo`: Ejecuta el comando con privilegios de superusuario.
              * `nano`: Editor de texto de línea de comandos.
              * `/etc/netplan/00-installer-config.yaml`: Ruta al archivo de configuración de red de Netplan.
              * **Contenido del archivo (con 2 espacios de indentación):**
                ```yaml
                network:
                  ethernets:
                    enp0s3:
                      dhcp4: no
                      addresses: [192.168.1.241/24]
                      routes:
                        - to: default
                          via: 192.168.1.1 # IP de tu router
                      nameservers:
                        addresses: [8.8.8.8, 8.8.4.4]
                  version: 2
                ```
              * **Repercusión:** Se desactiva DHCP (`dhcp4: no`), se asigna una IP estática (`addresses`), se define la ruta por defecto (`routes`) y los servidores DNS (`nameservers`).
          * **Corrección de Permisos:** Se cambiaron los permisos del archivo YAML para mayor seguridad.
            ```bash
            sudo chmod 600 /etc/netplan/00-installer-config.yaml
            ```
              * `chmod`: Cambia los permisos.
              * `600`: Otorga permisos de lectura y escritura solo al propietario del archivo (`root`).
          * **Aplicar Configuración de Red:**
            ```bash
            sudo netplan apply
            ```
              * `netplan apply`: Aplica los cambios en la configuración de red definidos en los archivos `.yaml`.
          * **Verificar IP:**
            ```bash
            ip a
            ```
              * `ip a`: Muestra las direcciones IP y el estado de las interfaces de red. Confirma que la IP asignada es `192.168.1.241`.

3.  **Verificación de Conectividad entre VMs:**

      * Desde Kali Linux VM, se hizo ping a Ubuntu Server VM para confirmar la comunicación bidireccional.

    <!-- end list -->

    ```bash
    ping 192.168.1.241
    ```

      * `ping`: Envía paquetes ICMP Echo Request para probar la conectividad.

### Fase 2: Generación y Análisis de Paquetes con hping3 y Wireshark

Para cada tarea, se siguió una secuencia estándar: iniciar captura en Wireshark, ejecutar hping3, detener captura, analizar en Wireshark.

#### Tarea 1: Generar Paquetes TCP

Los paquetes TCP (Transmission Control Protocol) son orientados a la conexión, fiables y garantizan la entrega de datos. Un "paquete" TCP es más precisamente un "segmento".

  * **Comando hping3 para TCP SYN:**
    ```bash
    sudo hping3 -S -p 80 192.168.1.241 -c 1
    ```
      * No especificamos que sea TCP porqué ya viene por defecto en hping3.
      * `-S`: Bandera SYN. Indica un intento de establecer una conexión.
      * `-p 80`: Puerto de destino 80 (HTTP).
      * `192.168.1.241`: IP del Ubuntu Server VM (objetivo).
      * `-c 1`: Envía un solo paquete. Sino se pone envía continuamente paquetes hasta detenerlo con CTRL C (stop) o CTRL Z (suspend).
  * **Análisis en Wireshark:**
      * **Filtro:** `tcp.flags.syn == 1 and tcp.port == 80 and ip.src == 192.168.1.240 and ip.dst == 192.168.1.241`
      * **Sintaxis del Filtro:** Los filtros de Wireshark utilizan una sintaxis de expresión. `tcp.flags.syn == 1` busca paquetes TCP donde la bandera SYN esté activada. `tcp.port == 80` busca el puerto TCP 80. `ip.src` e `ip.dst` filtran por direcciones IP de origen y destino. `and` combina las condiciones.
      * **Verificación:** Se confirmó que el paquete tenía `Source IP: 192.168.1.240`, `Destination IP: 192.168.1.241`, `Protocol: TCP`, y `Flags: SYN Set`. También se observó una respuesta RST/ACK de `192.168.1.241`, indicando que el puerto 80 estaba cerrado en el objetivo, lo cual es un comportamiento normal.

#### Tarea 2: Generar Paquetes UDP

Los paquetes UDP (User Datagram Protocol) son un protocolo sin conexión, no fiable y de baja latencia. Los datos se envían como "datagramas".

  * **Comando hping3 para UDP:**
    ```bash
    sudo hping3 -2 -p 53 192.168.1.241 -c 1
    ```
      * `-2`: Indica que se genere un paquete UDP, también se puede usar `--udp`.
      * `-p 53`: Puerto de destino 53 (DNS), también se puede usar `--baseport 53`, aunque va después de la ip de destino.
      * Podemos usar `--data` para indicar el tamaño en bytes del paquete.
  * **Análisis en Wireshark:**
      * **Filtro:** `udp.port == 53 and ip.src == 192.168.1.240 and ip.dst == 192.168.1.241`
      * **Verificación:** Se confirmó `Protocol: UDP`, `Source IP: 192.168.1.240`, `Destination IP: 192.168.1.241`, y `Destination Port: 53`. Se observó una respuesta ICMP "Port Unreachable" de `192.168.1.241`, indicando que no había un servicio UDP en el puerto 53 en el objetivo, un comportamiento normal.

#### Tarea 3: Generar un ICMP Echo Request

Los mensajes ICMP (Internet Control Message Protocol) no son paquetes de datos en sí, sino mensajes de control y error. Un "Echo Request" es el mensaje de ping.

  * **Comando hping3 para ICMP Echo Request:**
    ```bash
    sudo hping3 -1 192.168.1.241 -c 1
    ```
      * `-1`: Indica que se genere un paquete ICMP (por defecto, Echo Request). También se puede usar `--icmp`.
  * **Análisis en Wireshark:**
      * **Filtro:** `icmp and ip.addr == 192.168.1.240 and ip.addr == 192.168.1.241`
      * **Verificación:** Se encontró `Protocol: ICMP`, `Source IP: 192.168.1.240`, `Destination IP: 192.168.1.241`, y `Type: 8 (Echo (ping) request)`. También se verificó una respuesta `ICMP Echo Reply` (Type: 0) desde el objetivo, confirmando la conectividad.

#### Tarea 4: Modificar la IP de Origen (IP Spoofing) en un Paquete

El "spoofing" de IP implica falsificar la dirección IP de origen en un paquete para que parezca que proviene de una fuente diferente. Los paquetes son las unidades de datos a nivel de la capa de red (Capa 3 del modelo OSI).

  * **Comando hping3 para IP Spoofing (TCP SYN):**
    ```bash
    sudo hping3 -S -p 80 192.168.1.241 -a 192.168.1.10 -c 1
    ```
      * `-a 192.168.1.10`: Esta opción (`--spoof`) especifica la dirección IP de origen falsificada (`192.168.1.10` en este caso, que no es la IP real de Kali).
      * Hemos puesto una ip específica pero podemos poner una ip source random con `--rand-source`.
  * **Análisis en Wireshark:**
      * **Filtro:** `tcp.flags.syn == 1 and ip.src == 192.168.1.10 and ip.dst == 192.168.1.241`
      * **Verificación:** Se confirmó que el `Source Address` del paquete IP era `192.168.1.10`, validando que el IP spoofing funcionó. El paquete TCP SYN fue enviado al objetivo `192.168.1.241`.
      * Cómo es un TCP (más seguro que UDP) con un handshake de SYN, SYN/ACK, ACK al cambiar la ip sólo se envia un SYN continuamente pero no se captura la respuesta (SYN/ACK) porque el servidor no reconoce la ip que envía el SYN.

## Importancia de lo Aprendido en el Ejercicio

Entender y practicar la generación y el análisis de paquetes de red como lo hicimos en este ejercicio es fundamental en ciberseguridad por varias razones:

1.  **Fundamentos de Redes:** Permite comprender cómo los datos viajan a través de la red a un nivel muy básico. Conocer las capas TCP/IP, los encabezados de los paquetes y las banderas es esencial.
2.  **Diagnóstico de Problemas de Red:** La capacidad de usar herramientas como Wireshark para capturar y analizar el tráfico es invaluable para diagnosticar problemas de conectividad, rendimiento o aplicación en una red.
3.  **Auditoría de Seguridad y Pruebas de Penetración:**
      * `hping3` permite simular diversos ataques (escaneo de puertos avanzado, inundaciones SYN) y probar la robustez de firewalls y sistemas de detección de intrusiones.
      * `Wireshark` es la herramienta estándar para entender qué está sucediendo realmente en la red, identificar tráfico malicioso, y analizar el comportamiento de aplicaciones y sistemas.
4.  **Desarrollo de Herramientas:** Comprender la estructura de los paquetes es crucial para desarrollar scripts o herramientas de red propias.
5.  **Defensa de Redes:** Para defender una red, se debe entender cómo operan los ataques a nivel de paquete y cómo identificarlos.

## IP Spoofing: Conceptos Clave

El IP Spoofing es la técnica de modificar la dirección IP de origen de un paquete de red para que parezca que proviene de una fuente diferente.

  * **Cómo se utiliza:**

      * **Ocultar la identidad:** Un atacante puede usarlo para ocultar su dirección IP real.
      * **Evadir filtros de firewall:** Si un firewall confía en una IP de origen específica, un atacante podría falsificar esa IP para pasar a través de reglas de filtrado.
      * **Ataques de denegación de servicio (DoS/DDoS):** Los atacantes pueden falsificar IPs de origen para dificultar la mitigación de la inundación de tráfico y para que las respuestas del objetivo no lleguen al atacante real, sino a las IPs falsificadas (amplificación).
      * **Secuestro de sesión:** En algunos contextos, se puede intentar falsificar la IP de una sesión válida para tomar el control.
      * **Confianza basada en IP:** Si un sistema confía en las IPs de origen (ej., listas blancas), el spoofing puede explotar esa confianza.

  * **Consecuencias:**

      * **Anonimato para el atacante:** Dificulta el rastreo.
      * **Ampliación de ataques:** Los ataques de reflexión y amplificación utilizan spoofing para redirigir tráfico masivo.
      * **Interrupción del servicio:** Ataques DoS/DDoS.
      * **Confusión de logs:** Los registros de auditoría pueden mostrar IPs falsas, dificultando la investigación forense.

  * **Cómo Detectarlo:**

      * **Análisis de paquetes:** Wireshark es la herramienta principal. Observa si la IP de origen en un paquete sospechoso no coincide con la IP de la máquina que lo envió (si la conoces).
      * **Anomalías en el tráfico:** Flujos de tráfico inusuales, respuestas a paquetes que no fueron enviados por el host real, o respuestas a una IP de origen que no está realmente en la red.
      * **Verificación de TTL/ID:** Los valores de Time-To-Live (TTL) o el ID de fragmentación en los encabezados IP a menudo tienen patrones predecibles para un sistema operativo dado. Una IP falsificada podría mostrar valores de TTL/ID que no concuerdan con los del sistema que supuestamente la envió.
      * **Tráfico unidireccional:** Si ves tráfico saliendo de una IP pero nunca ves respuestas llegar a esa misma IP, podría ser un indicio de spoofing (especialmente si es un protocolo orientado a la conexión).

  * **Cómo Prevenirlo:**

      * **Filtrado de Entrada (Ingress Filtering):** La prevención más efectiva. Los proveedores de servicios de Internet (ISPs) y las organizaciones deben implementar filtros en sus routers perimetrales para asegurarse de que los paquetes que entran a su red tienen una dirección IP de origen que pertenece a su propio bloque de direcciones o al de sus clientes legítimos. Si un paquete llega a un router con una IP de origen que no corresponde a la subred desde la que debería provenir, se descarta. Esto previene que los paquetes falsificados salgan a Internet desde esa red.
      * **Filtrado de Salida (Egress Filtering):** Similar al filtrado de entrada, pero aplicado a los paquetes que salen de una red. Una organización filtra el tráfico saliente para asegurarse de que las IPs de origen coincidan con sus propios activos.
      * **Uso de TCP:** Los ataques de spoofing son más difíciles contra TCP debido al "three-way handshake" (el atacante no recibe el SYN-ACK). Sin embargo, aún es posible en algunos escenarios.
      * **Autenticación y Cifrado:** No depender solo de la IP de origen para la confianza. Utilizar protocolos de autenticación fuerte (como IPsec, TLS) y cifrado.
      * **Listas de control de acceso (ACLs) en routers y firewalls:** Configurar reglas que solo permitan tráfico de IPs de confianza y denieguen el resto.

Este ejercicio te ha proporcionado una base sólida para entender la red a bajo nivel y sus implicaciones en la ciberseguridad.