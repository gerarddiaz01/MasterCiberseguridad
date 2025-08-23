# Simulación de Firewall con Cisco Packet Tracer: Control de Tráfico entre Redes

La implementación de un **firewall** es una medida de seguridad esencial en cualquier arquitectura de red. Permite controlar el flujo de tráfico entre diferentes segmentos, protegiendo los recursos internos y limitando la propagación de posibles ataques. En esta sesión, exploraremos cómo utilizar **Cisco Packet Tracer** para simular la configuración de un firewall básico utilizando un router Cisco, estableciendo reglas de acceso específicas entre dos redes.

Aunque nos enfocaremos en el entorno Cisco Packet Tracer, los principios y comandos son aplicables a otros tipos de firewalls y entornos reales, dado que Cisco es uno de los fabricantes más utilizados en la industria.

## 1\. Diseño de la Arquitectura de Red en Packet Tracer

Para esta práctica, crearemos un escenario simple con dos redes distintas y un router que actuará como firewall entre ellas.

### 1.1. Componentes de la Arquitectura

Necesitaremos los siguientes dispositivos en nuestro espacio de trabajo de Packet Tracer:

  * **1 Router Cisco**: Utilizaremos un modelo de router Cisco (ej. ISR4331) que ofrece funcionalidades básicas de firewall a través de su IOS. Este será el dispositivo central que actuará como cortafuegos.
  * **2 Switches**: Modelos Cisco 2960-24TT. Cada uno conectará un PC a su respectiva red.
  * **2 PCs**: Representarán los dispositivos finales en cada red.

### 1.2. Definición de las Redes

Configuraremos dos redes distintas:

  * **Red A (LAN / Intranet)**:
      * Dirección IP: `192.168.1.0/24`
      * Conectada al router por la interfaz `GigabitEthernet0/0/0`.
      * Contendrá un PC (`PC0`).
  * **Red B (DMZ)**:
      * Dirección IP: `192.168.2.0/24`
      * Conectada al router por la interfaz `GigabitEthernet0/0/1`.
      * Contendrá un PC (`PC1`).

### 1.3. Objetivo de la Configuración del Firewall

El objetivo principal es configurar el router para que actúe como un firewall con las siguientes reglas:

  * **Permitir** todo el tráfico iniciado desde la **Red A (LAN)** hacia la **Red B (DMZ)**.
  * **Bloquear** todo el tráfico iniciado desde la **Red B (DMZ)** hacia la **Red A (LAN)**.

Este comportamiento es típico de una **DMZ (Zona Desmilitarizada)**, donde los sistemas externos (o en la DMZ) pueden comunicarse con los servicios públicos, pero no pueden iniciar comunicación hacia la red interna.

### 1.4. Disposición de los Elementos en Packet Tracer

1.  Arrastra un **Router** al centro del lienzo.
2.  Arrastra dos **Switches** a cada lado del router.
3.  Arrastra dos **PCs** (PC0 y PC1) y conéctalos a sus respectivos switches.
4.  **Conecta los PCs a los Switches**: Utiliza cables "Copper Straight-Through" (cable de cobre directo).
      * `PC0` a `Switch0` (ej. `FastEthernet0/1`).
      * `PC1` a `Switch1` (ej. `FastEthernet0/1`).
5.  **Conecta los Switches al Router**: Utiliza cables "Copper Straight-Through".
      * `Switch0` (Red A) a `Router` (ej. `GigabitEthernet0/0/0`).
      * `Switch1` (Red B) a `Router` (ej. `GigabitEthernet0/0/1`).

## 2\. Configuración Básica del Router (Cisco IOS CLI)

Accederemos a la interfaz de línea de comandos (CLI) del router para configurarlo.

### 2.1. Acceso a la CLI del Router

1.  Haz doble clic en el Router en Packet Tracer.
2.  Ve a la pestaña "CLI".
3.  Cuando pregunte si deseas entrar en el modo de configuración inicial, escribe `no` y presiona `Enter`.

### 2.2. Habilitar el Modo Privilegiado EXEC

  * **Comando**: `enable`
  * **Sintaxis**:
    ```
    Router>enable
    ```
  * **Explicación**: Este comando eleva los privilegios del usuario, permitiendo ejecutar comandos de configuración y monitoreo.
  * **Objetivo**: Obtener acceso a comandos administrativos.
  * **Resultado Esperado**: El prompt cambiará a `Router#`.

### 2.3. Entrar al Modo de Configuración Global

  * **Comando**: `configure terminal` (o `conf t`)
  * **Sintaxis**:
    ```
    Router#configure terminal
    ```
  * **Explicación**: Nos lleva al modo donde se pueden realizar cambios en la configuración global del router.
  * **Objetivo**: Acceder al modo de configuración.
  * **Resultado Esperado**: El prompt cambiará a `Router(config)#`.

### 2.4. Configurar las Interfaces del Router

Asignaremos direcciones IP a las interfaces del router que conectan con cada red y las activaremos.

  * **Interfaz para la Red A (LAN)**: `GigabitEthernet0/0/0`

      * **Comando**:
        ```
        Router(config)#interface GigabitEthernet0/0/0
        Router(config-if)#ip address 192.168.1.1 255.255.255.0
        Router(config-if)#no shutdown
        Router(config-if)#exit
        ```
      * **Explicación**:
          * `interface GigabitEthernet0/0/0`: Entra al modo de configuración de la interfaz `GigabitEthernet0/0/0`.
          * `ip address 192.168.1.1 255.255.255.0`: Asigna la dirección IP `192.168.1.1` y la máscara de subred `255.255.255.0` a esta interfaz. Esta será la puerta de enlace (gateway) para la Red A.
          * `no shutdown`: Activa la interfaz. Por defecto, las interfaces de los routers Cisco están deshabilitadas (`shutdown`).
          * `exit`: Vuelve al modo de configuración global.
      * **Objetivo**: Configurar la interfaz del router para la Red A y activarla.
      * **Resultado Esperado**: El enlace en Packet Tracer se pondrá verde.

  * **Interfaz para la Red B (DMZ)**: `GigabitEthernet0/0/1`

      * **Comando**:
        ```
        Router(config)#interface GigabitEthernet0/0/1
        Router(config-if)#ip address 192.168.2.1 255.255.255.0
        Router(config-if)#no shutdown
        Router(config-if)#exit
        ```
      * **Explicación**: Similar a la anterior, pero para la Red B. La IP `192.168.2.1` será el gateway para la Red B.
      * **Objetivo**: Configurar la interfaz del router para la Red B y activarla.
      * **Resultado Esperado**: El enlace en Packet Tracer se pondrá verde.

### 2.5. Guardar la Configuración del Router

  * **Comando**: `end`
  * **Comando**: `copy running-config startup-config` (o `wr`)
  * **Sintaxis**:
    ```
    Router(config)#end
    Router#copy running-config startup-config
    Destination filename [startup-config]? (Presionar Enter)
    ```
  * **Explicación**: `end` sale del modo de configuración y `copy running-config startup-config` guarda la configuración actual (en RAM) en la memoria no volátil (NVRAM) para que persista después de un reinicio.
  * **Objetivo**: Asegurar que la configuración del router no se pierda.

## 3\. Configuración de las Direcciones IP en los PCs

Cada PC debe tener una dirección IP de su respectiva red y apuntar al router como su gateway.

  * **PC0 (Red A - LAN)**:

    1.  Haz clic en `PC0`.
    2.  Ve a la pestaña `Desktop`.
    3.  Haz clic en `IP Configuration`.
    4.  Selecciona `Static`.
    5.  Configura:
          * `IP Address`: `192.168.1.2`
          * `Subnet Mask`: `255.255.255.0`
          * `Default Gateway`: `192.168.1.1` (la IP de la interfaz del router en la Red A).

  * **PC1 (Red B - DMZ)**:

    1.  Haz clic en `PC1`.
    2.  Ve a la pestaña `Desktop`.
    3.  Haz clic en `IP Configuration`.
    4.  Selecciona `Static`.
    5.  Configura:
          * `IP Address`: `192.168.2.2`
          * `Subnet Mask`: `255.255.255.0`
          * `Default Gateway`: `192.168.2.1` (la IP de la interfaz del router en la Red B).

## 4\. Configuración del Firewall (Access Control List - ACL) en el Router

Ahora, configuraremos las reglas de acceso en el router para que actúe como firewall. Utilizaremos una **ACL numerada estándar** (números del 1 al 99 o 1300 al 1999) o **extendida** (números del 100 al 199 o 2000 al 2699). Para este ejercicio, se utiliza una ACL extendida (número 100) para controlar el tráfico basado en origen y destino.

### 4.1. Crear la Access List (ACL 100)

  * **Comando (Permitir tráfico de Red A a Red B)**:

    ```
    Router(config)#access-list 100 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255
    ```

  * **Sintaxis**:

    ```
    Router(config)#access-list 100 permit ip 192.168.1.0 0.0.0.255 192.168.2.0 0.0.0.255
    ```

  * **Explicación**:

      * `access-list 100`: Inicia la configuración de la ACL con el número 100.
      * `permit`: La acción a tomar (permitir el tráfico).
      * `ip`: Indica que la regla se aplica a todos los protocolos IP.
      * `192.168.1.0 0.0.0.255`: Define la red de origen. `192.168.1.0` es la dirección de red, y `0.0.0.255` es la **wildcard mask**. La wildcard mask es lo opuesto a la máscara de subred; los ceros indican bits que deben coincidir exactamente, y los unos indican bits que pueden ser cualquier valor. `0.0.0.255` en este contexto significa "cualquier IP en la red `192.168.1.0/24`".
      * `192.168.2.0 0.0.0.255`: Define la red de destino. Significa "cualquier IP en la red `192.168.2.0/24`".

  * **Objetivo**: Crear una regla que permita que cualquier dispositivo de la Red A se comunique con cualquier dispositivo de la Red B.

  * **Comando (Denegar tráfico de Red B a Red A)**:

    ```
    Router(config)#access-list 100 deny ip 192.168.2.0 0.0.0.255 192.168.1.0 0.0.0.255
    ```

  * **Sintaxis**:

    ```
    Router(config)#access-list 100 deny ip 192.168.2.0 0.0.0.255 192.168.1.0 0.0.0.255
    ```

  * **Explicación**:

      * `deny`: La acción a tomar (denegar el tráfico).
      * `192.168.2.0 0.0.0.255`: Origen es la Red B.
      * `192.168.1.0 0.0.0.255`: Destino es la Red A.

  * **Objetivo**: Crear una regla que deniegue cualquier comunicación iniciada desde la Red B hacia la Red A.

  * **Comando (Permitir el resto del tráfico - Implícito `deny any any`)**:

    ```
    Router(config)#access-list 100 permit ip any any
    ```

  * **Sintaxis**:

    ```
    Router(config)#access-list 100 permit ip any any
    ```

  * **Explicación**:

      * `permit ip any any`: Esta regla es crucial. Las ACLs tienen un `deny any any` implícito al final. Si no se añade esta regla `permit ip any any`, todo el tráfico que no coincida con las reglas anteriores (incluido el tráfico de la Red A a Internet, por ejemplo) sería denegado. Al añadirla, permitimos todo lo demás que no haya sido explícitamente denegado por las reglas anteriores.

  * **Objetivo**: Asegurar que el tráfico no especificado por las reglas anteriores sea permitido, evitando bloqueos no deseados.

### 4.2. Aplicar la Access List a la Interfaz del Router

Las ACLs deben aplicarse a una interfaz del router y en una dirección específica (inbound/outbound). Para nuestro objetivo, aplicaremos la ACL en la interfaz que conecta con la Red B (`GigabitEthernet0/0/1`), en dirección de salida (`out`). Esto controlará el tráfico que *sale* de la Red B hacia el router.

  * **Comando**:
    ```
    Router(config)#interface GigabitEthernet0/0/1
    Router(config-if)#ip access-group 100 out
    Router(config-if)#exit
    ```
  * **Sintaxis**:
    ```
    Router(config)#interface GigabitEthernet0/0/1
    Router(config-if)#ip access-group 100 out
    Router(config-if)#exit
    ```
  * **Explicación**:
      * `interface GigabitEthernet0/0/1`: Entra al modo de configuración de la interfaz conectada a la Red B.
      * `ip access-group 100 out`: Aplica la ACL número 100 a esta interfaz en la dirección de salida (`out`). Esto significa que las reglas de la ACL se aplicarán al tráfico *después* de que ha sido enrutado y está a punto de salir por esta interfaz.
  * **Objetivo**: Implementar las reglas de firewall definidas por la ACL 100 en el tráfico que sale de la Red B.

## 5\. Verificación del Firewall (Pruebas de Conectividad)

Una vez configurado el router y los PCs, es hora de verificar que las reglas del firewall funcionan como se espera.

### 5.1. Prueba de Conectividad de Red A a Red B (Debería Funcionar)

  * **Escenario**: Desde `PC0` (Red A - `192.168.1.2`) a `PC1` (Red B - `192.168.2.2`).
  * **Pasos**:
    1.  En `PC0`, ve a la pestaña `Desktop`.
    2.  Haz clic en `Command Prompt`.
    3.  **Comando**: `ping 192.168.2.2`
    <!-- end list -->
      * **Sintaxis**:
        ```
        ping 192.168.2.2
        ```
      * **Explicación**: `PC0` intenta comunicarse con `PC1`. Según nuestra ACL, el tráfico de la Red A a la Red B está permitido.
      * **Objetivo**: Confirmar que la regla `permit` de la ACL funciona.
      * **Resultado Esperado**: Deberías ver respuestas de `ping` exitosas (`Reply from 192.168.2.2...`).

### 5.2. Prueba de Conectividad de Red B a Red A (Debería Bloquearse)

  * **Escenario**: Desde `PC1` (Red B - `192.168.2.2`) a `PC0` (Red A - `192.168.1.2`).
  * **Pasos**:
    1.  En `PC1`, ve a la pestaña `Desktop`.
    2.  Haz clic en `Command Prompt`.
    3.  **Comando**: `ping 192.168.1.2`
    <!-- end list -->
      * **Sintaxis**:
        ```
        ping 192.168.1.2
        ```
      * **Explicación**: `PC1` intenta comunicarse con `PC0`. Según nuestra ACL, el tráfico de la Red B a la Red A está denegado.
      * **Objetivo**: Confirmar que la regla `deny` de la ACL funciona y que el tráfico está bloqueado en esta dirección.
      * **Resultado Esperado**: Deberías ver "Destination host unreachable" o "Request timed out", indicando que el ping no llega.

## Conclusión

Este ejercicio de simulación de firewall con Cisco Packet Tracer demuestra la capacidad de un router para actuar como un dispositivo de seguridad, controlando el flujo de tráfico entre diferentes redes utilizando **Access Control Lists (ACLs)**. Hemos configurado una arquitectura básica, asignado IPs y, lo más importante, hemos implementado reglas de acceso que permiten el tráfico en un sentido (Red A a Red B) pero lo bloquean en el sentido opuesto (Red B a Red A).

Esta práctica es fundamental para comprender cómo se implementan las políticas de seguridad a nivel de red, cómo se segmentan las redes y cómo se protege una intranet de una zona más expuesta como una DMZ. Packet Tracer es una herramienta invaluable para probar y configurar firewalls de Cisco y otros fabricantes, proporcionando un entorno fluido para la simulación y la experimentación que mejora la competencia y la preparación en seguridad de redes. Los comandos y principios aprendidos aquí son directamente aplicables en entornos de producción reales.