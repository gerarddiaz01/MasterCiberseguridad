# Configuración de VLANs con Cisco Packet Tracer: Un Enfoque Práctico para la Segmentación Segura

La **segmentación de red** mediante **VLANs (Virtual Local Area Networks)** es una piedra angular de la ciberseguridad moderna. Permite aislar lógicamente el tráfico de diferentes grupos de usuarios o servicios dentro de una misma infraestructura física, lo que mejora la seguridad, el rendimiento y la capacidad de gestión. En esta sesión, exploraremos cómo configurar VLANs utilizando **Cisco Packet Tracer**, una herramienta de simulación que nos permite construir y probar arquitecturas de red.

El objetivo principal es crear una pequeña arquitectura de prueba, configurar switches Cisco utilizando su **CLI (Command Line Interface)** basada en **IOS Cisco**, establecer puertos **trunk** para la interconexión de switches, asignar direcciones IP a las máquinas y, finalmente, verificar el aislamiento de las VLANs para asegurar un **hardening** adecuado.

## 1\. Introducción a Cisco Packet Tracer

**Cisco Packet Tracer** es una aplicación excepcional que funciona muy bien para montar desde un armario rack hasta cualquier tipo de arquitectura de red utilizando dispositivos de la marca Cisco. Es un simulador muy bueno para ejecutar todo tipo de implementaciones de seguridad en una arquitectura de red y, además, es gratuito. Ofrece una variedad enorme de funcionalidades.

  * **Acceso y Descarga**: Se puede acceder buscando "Cisco Packet Tracer" en Google, que redirige a la página de Cisco Networking Academy. La descarga es gratuita y viene asociada con cursos tutoriales para aprender a usar la aplicación.
  * **Utilidad**: Permite practicar redes, IoT y ciberseguridad en un entorno virtual sin necesidad de hardware real, lo que lo convierte en una herramienta vital para realizar pruebas de todo tipo de configuraciones sin afectar una red de producción.

## 2\. Diseño de la Arquitectura en Packet Tracer

Para este ejercicio, construiremos una topología de red simple pero efectiva que nos permitirá demostrar el funcionamiento de las VLANs.

### 2.1. Componentes de la Arquitectura

Necesitaremos los siguientes dispositivos en nuestro espacio de trabajo de Packet Tracer:

  * **2 Switches Gestionados**: Se recomienda el modelo **Cisco 2960-24TT** o similar, ya que soportan la configuración de VLANs.
  * **4 Máquinas (PCs)**: Se utilizarán 4 PCs genéricos (PC0, PC1, PC2, PC3).

### 2.2. Disposición Inicial de los Elementos

Arrastra los dos switches y los cuatro PCs al lienzo de Packet Tracer. La disposición conceptual será dos PCs conectados a cada switch.

  * Si colocamos el cursor sobre un dispositivo, podemos ver una configuración básica, incluyendo que, por defecto, los puertos del switch están en la **VLAN 1**.

## 3\. Configuración de Switches con Cisco IOS CLI

La configuración de los switches se realiza a través de su interfaz de línea de comandos (CLI), que utiliza el sistema operativo **IOS (Internetwork Operating System)** de Cisco.

### 3.1. Acceso a la CLI del Switch

1.  **Seleccionar el Switch**: En Packet Tracer, haz doble clic en el switch que deseas configurar.
2.  **Pestaña CLI**: En el panel de configuración del dispositivo, selecciona la pestaña "CLI".
3.  **Modo de Usuario EXEC**: Inicialmente, verás el prompt `Switch>`.

### 3.2. Habilitar el Modo Privilegiado EXEC

Para realizar configuraciones, necesitamos acceder al modo privilegiado EXEC.

  * **Comando**: `enable`
  * **Sintaxis**: `Switch>enable`
  * **Explicación**: Este comando eleva los privilegios del usuario, permitiendo ejecutar comandos de visualización y gestión más avanzados. Es el comando clave para comenzar a configurar cualquier dispositivo.
  * **Objetivo**: Obtener acceso a comandos de configuración y monitoreo más potentes.
  * **Resultado Esperado**: El prompt cambiará a `Switch#`.

### 3.3. Entrar al Modo de Configuración Global

Desde el modo privilegiado, entramos al modo de configuración global para realizar cambios en el switch.

  * **Comando**: `configure terminal` (o `conf t` como abreviatura)
  * **Sintaxis**: `Switch#configure terminal`
  * **Explicación**: Este comando nos lleva al modo donde podemos crear VLANs, configurar interfaces, etc..
  * **Objetivo**: Acceder al modo donde se pueden modificar las configuraciones del switch.
  * **Resultado Esperado**: El prompt cambiará a `Switch(config)#`.

### 3.4. Creación de VLANs

Crearemos la VLAN 10 para HR y la VLAN 20 para IT (en el transcript se usan VLAN 1 y VLAN 2 para el ejemplo, pero para mantener la claridad y la separación departamental, usaremos 10 y 20).

  * **Comando (para VLAN 10 - HR)**: `vlan 10`

  * **Sintaxis**:

    ```
    Switch(config)#vlan 10
    Switch(config-vlan)#name HR
    ```

  * **Explicación**:

      * `vlan 10`: Crea la VLAN con ID 10 y nos sitúa en su modo de configuración.
      * `name HR`: Asigna un nombre descriptivo a la VLAN.

  * **Objetivo**: Definir la VLAN 10 para el departamento de Recursos Humanos.

  * **Resultado Esperado**: El prompt cambiará a `Switch(config-vlan)#` y se confirmará el nombre.

  * **Comando (para VLAN 20 - IT)**: `vlan 20`

  * **Sintaxis**:

    ```
    Switch(config)#vlan 20
    Switch(config-vlan)#name IT
    ```

  * **Explicación**: Similar al anterior, pero para la VLAN 20.

  * **Objetivo**: Definir la VLAN 20 para el departamento de Tecnología de la Información.

Repite estos pasos para **ambos switches** (Switch0 y Switch1).

### 3.5. Asignación de Puertos de Acceso a VLANs

Ahora, asignaremos los puertos físicos del switch a las VLANs correspondientes. Es crucial una buena fase de planificación y localización física de los usuarios.

**En Switch0:**

  * **PC0 (VLAN 10)**: Conectar a `FastEthernet 0/1`

  * **PC1 (VLAN 20)**: Conectar a `FastEthernet 0/2`

  * **Comando (para FastEthernet 0/1 - PC0/HR)**:

    ```
    Switch(config)#interface FastEthernet 0/1
    Switch(config-if)#switchport mode access
    Switch(config-if)#switchport access vlan 10
    Switch(config-if)#exit
    ```

  * **Explicación**:

      * `interface FastEthernet 0/1`: Entra al modo de configuración de la interfaz específica.
      * `switchport mode access`: Configura el puerto para que opere en modo de acceso, lo que significa que solo transportará tráfico para una única VLAN.
      * `switchport access vlan 10`: Asigna la interfaz a la VLAN 10.
      * `exit`: Sale del modo de configuración de interfaz.

  * **Objetivo**: Aislar el tráfico del PC conectado a este puerto en la VLAN 10.

  * **Comando (para FastEthernet 0/2 - PC1/IT)**:

    ```
    Switch(config)#interface FastEthernet 0/2
    Switch(config-if)#switchport mode access
    Switch(config-if)#switchport access vlan 20
    Switch(config-if)#exit
    ```

  * **Explicación**: Asigna el puerto a la VLAN 20.

  * **Objetivo**: Aislar el tráfico del PC conectado a este puerto en la VLAN 20.

**En Switch1:**

  * **PC2 (VLAN 10)**: Conectar a `FastEthernet 0/1`
  * **PC3 (VLAN 20)**: Conectar a `FastEthernet 0/2`

Repite los comandos anteriores en el **Switch1** para asignar `FastEthernet 0/1` a la VLAN 10 (para PC2) y `FastEthernet 0/2` a la VLAN 20 (para PC3).

### 3.6. Configuración de Puertos Trunk

Los puertos **trunk** son vitales para interconectar los switches y permitir que el tráfico de múltiples VLANs circule entre ellos. Utilizaremos el puerto `GigabitEthernet 0/1` en ambos switches para esta conexión troncal.

**En Switch0 (ej. GigabitEthernet 0/1):**

  * **Comando**:
    ```
    Switch(config)#interface GigabitEthernet 0/1
    Switch(config-if)#switchport mode trunk
    Switch(config-if)#switchport trunk allowed vlan 10,20
    Switch(config-if)#exit
    ```
  * **Sintaxis**:
      * `interface GigabitEthernet 0/1`: Entra al modo de configuración de la interfaz.
      * `switchport mode trunk`: Configura el puerto para operar en modo troncal, permitiendo el paso de tráfico de múltiples VLANs.
      * `switchport trunk allowed vlan 10,20`: Especifica qué VLANs están permitidas para circular por este trunk. Es una buena práctica de seguridad limitar las VLANs permitidas en un trunk.
  * **Explicación**: Estos comandos configuran el enlace entre los switches para que el tráfico etiquetado de la VLAN 10 y la VLAN 20 pueda fluir entre ellos. Recordad que antes usamos `switchport mode access` para los puertos de acceso.
  * **Objetivo**: Establecer un enlace troncal seguro y eficiente entre los switches para la comunicación inter-VLAN.

**En Switch1 (ej. GigabitEthernet 0/1):**

Repite los mismos comandos para el puerto `GigabitEthernet 0/1` en el **Switch1** para configurar el otro extremo del enlace troncal.

### 3.7. Guardar la Configuración

Es vital guardar la configuración para que no se pierda si el switch se reinicia.

  * **Comando (desde cualquier modo de configuración)**: `end`
  * **Comando (desde modo privilegiado EXEC)**: `copy running-config startup-config` (o `wr` para abreviar)
  * **Sintaxis**:
    ```
    Switch(config-if)#end
    Switch#copy running-config startup-config
    Destination filename [startup-config]? (Presionar Enter)
    ```
  * **Explicación**:
      * `end`: Sale del modo de configuración actual y vuelve al modo privilegiado EXEC (`Switch#`).
      * `copy running-config startup-config`: Copia la configuración activa en la memoria RAM (running-config) a la memoria no volátil (startup-config).
  * **Objetivo**: Persistir la configuración en la memoria del switch.

## 4\. Conexión Física de los Dispositivos en Packet Tracer

Una vez configurados lógicamente los switches, procedemos a realizar las conexiones físicas en el lienzo de Packet Tracer.

1.  **Conectar PCs a Switches**:

      * Selecciona el icono de "Connections" (el rayo).
      * Elige el cable "Copper Straight-Through" (cable directo de cobre).
      * Haz clic en un PC (ej. PC0), selecciona su interfaz `FastEthernet0`.
      * Haz clic en el Switch0 y selecciona el puerto `FastEthernet 0/1` (el puerto asignado a la VLAN 10).
      * Repite este proceso para PC1 (Fa0/2 de Switch0), PC2 (Fa0/1 de Switch1) y PC3 (Fa0/2 de Switch1).

2.  **Conectar Switches entre sí (Trunk)**:

      * Con el mismo cable "Copper Straight-Through".
      * Haz clic en el Switch0, selecciona su puerto `GigabitEthernet 0/1` (el puerto trunk).
      * Haz clic en el Switch1 y selecciona su puerto `GigabitEthernet 0/1` (el puerto trunk).

## 5\. Asignación de Direcciones IP a las Máquinas

Para que las máquinas puedan comunicarse dentro de sus respectivas VLANs, necesitan direcciones IP que pertenezcan a los rangos de esas VLANs. Asignaremos direcciones IP **estáticas** a cada PC.

  * **VLAN 10 (HR)**: Utilizaremos IPs del rango `192.168.10.0/24`.
  * **VLAN 20 (IT)**: Utilizaremos IPs del rango `192.168.20.0/24`.

**Proceso para cada PC:**

1.  **Seleccionar el PC**: Haz clic en el PC (ej. PC0).

2.  **Pestaña Desktop**: Navega a la pestaña "Desktop".

3.  **Icono IP Configuration**: Haz clic en el icono "IP Configuration".

4.  **Configuración Estática**: Selecciona "Static" y configura los siguientes parámetros:

      * **PC0 (VLAN 10 - HR - Conectado a Switch0 Fa0/1)**:
          * `IP Address`: `192.168.10.10`
          * `Subnet Mask`: `255.255.255.0`
          * (`Default Gateway`: No es necesario para pruebas de VLAN dentro de la misma subred, pero si hubiera un router inter-VLAN, sería `192.168.10.1`)
      * **PC1 (VLAN 20 - IT - Conectado a Switch0 Fa0/2)**:
          * `IP Address`: `192.168.20.10`
          * `Subnet Mask`: `255.255.255.0`
      * **PC2 (VLAN 10 - HR - Conectado a Switch1 Fa0/1)**:
          * `IP Address`: `192.168.10.11`
          * `Subnet Mask`: `255.255.255.0`
      * **PC3 (VLAN 20 - IT - Conectado a Switch1 Fa0/2)**:
          * `IP Address`: `192.168.20.11`
          * `Subnet Mask`: `255.255.255.0`

<!-- end list -->

  * **Verificación Rápida**: Puedes pasar el cursor sobre cada PC en el lienzo de Packet Tracer para ver su dirección IP asignada.

## 6\. Verificación del Aislamiento de VLANs (Pruebas de Hardening)

Una vez que todos los dispositivos están configurados y conectados, es hora de verificar que las VLANs están funcionando correctamente y que la segmentación proporciona el **hardening** esperado.

### 6.1. Pruebas de Conectividad dentro de la Misma VLAN

Las máquinas dentro de la misma VLAN (aunque conectadas a switches diferentes) deberían poder comunicarse.

1.  **Abrir Command Prompt**: En un PC (ej. PC0 - VLAN 10).
2.  **Comando**: `ping <dirección_IP_de_otro_PC_en_misma_VLAN>`
      * **Ejemplo**: Desde **PC0 (192.168.10.10)**, haz `ping 192.168.10.11` (PC2).

<!-- end list -->

  * **Sintaxis**: `ping 192.168.10.11`
  * **Explicación**: El comando `ping` envía paquetes de solicitud de eco ICMP al destino y espera respuestas. Si se reciben respuestas, hay conectividad.
  * **Objetivo**: Verificar que los dispositivos que pertenecen a la misma VLAN pueden comunicarse, incluso si están conectados a switches diferentes, gracias a la configuración del puerto trunk.
  * **Resultado Esperado**: Deberías ver respuestas de `ping` exitosas, indicando que hay conectividad entre PC0 y PC2. Lo mismo debería ocurrir entre PC1 y PC3.

### 6.2. Pruebas de Aislamiento entre Diferentes VLANs

Las máquinas en diferentes VLANs **no deberían poder comunicarse** directamente, demostrando el aislamiento lógico.

  * **Ejemplo**: Desde **PC0 (192.168.10.10)**, haz `ping 192.168.20.10` (PC1).

  * **Sintaxis**: `ping 192.168.20.10`

  * **Explicación**: Se intenta enviar paquetes entre dos VLANs distintas sin un dispositivo de Capa 3 (router) que realice el enrutamiento inter-VLAN.

  * **Objetivo**: Confirmar que las VLANs están correctamente aisladas y que el tráfico no puede fluir entre ellas sin una ruta explícita.

  * **Resultado Esperado**: Deberías ver "Request timed out" o "Destination host unreachable", indicando que la comunicación está bloqueada. Esto valida el **hardening** proporcionado por la segmentación de VLANs.

  * **Conectividad entre VLAN 20**: Repite el proceso desde PC1 (`192.168.20.10`) haciendo `ping 192.168.20.11` (PC3). Deberías obtener respuestas exitosas.

**¿Qué hacer si queremos que ambas VLANs se comuniquen?**
Para permitir la comunicación entre diferentes VLANs, necesitaríamos un **router**. Este dispositivo de Capa 3 sería el encargado de enrutar el tráfico entre las VLANs, aplicando las políticas de seguridad necesarias.

## 7\. Relevancia de las VLANs en el Hardening de Sistemas

La configuración de VLANs es un elemento básico y crítico para la **protección** de cualquier arquitectura de red de datos. Su importancia en el **hardening de sistemas** radica en varios puntos clave:

  * **Aislamiento y Contención**: Las VLANs permiten aislar lógicamente segmentos de la red. Si un atacante (un **Insider**, o alguien que ha logrado un acceso inicial a través de **Phishing** o un **Exploit**) compromete un dispositivo en una VLAN, el impacto del ataque queda **contenido** dentro de ese segmento. Esto dificulta enormemente el **movimiento lateral** hacia otras subredes críticas (ej. servidores de bases de datos con **Data Leaks** potenciales o sistemas de administración).
  * **Reducción de la Superficie de Ataque**: Al segmentar la red, los dispositivos solo son "visibles" y accesibles para aquellos dentro de su misma VLAN o a través de rutas explícitamente permitidas por un router de Capa 3. Esto minimiza la superficie de ataque que un atacante puede escanear o explotar.
  * **Control de Acceso Granular**: Las VLANs facilitan la implementación de **políticas de seguridad diferenciadas**. Se pueden aplicar **ACLs (Access Control Lists)** o reglas de firewall más estrictas a los enlaces entre VLANs, permitiendo solo el tráfico necesario y adhiriéndose al **Principio de Mínimo Privilegio**. Por ejemplo, la VLAN de invitados puede tener acceso solo a Internet, mientras que la VLAN de servidores de producción tiene restricciones muy fuertes.
  * **Mitigación de Ataques de Broadcast**: Cada VLAN es un dominio de broadcast separado. Esto significa que los ataques que abusan del tráfico de difusión (como las **broadcast storms** o ciertos tipos de **DDoS**) quedan confinados a la VLAN afectada, evitando que impacten a toda la red.
  * **Mejora de la Auditoría y Monitorización**: La segmentación facilita la monitorización del tráfico, ya que se puede enfocar en segmentos específicos. Esto ayuda a detectar anomalías, intrusiones o movimientos sospechosos de manera más eficiente.
  * **Optimización del Rendimiento**: Al limitar los dominios de broadcast, las VLANs reducen la congestión de la red y optimizan su rendimiento.

### 7.1. Asegurar la Configuración de VLANs frente a Agentes Maliciosos

Para asegurarnos de que las VLANs están bien configuradas y no son vulnerables a ataques de agentes maliciosos, debemos seguir buenas prácticas:

  * **No Usar la Configuración por Defecto**: Nunca dejar las configuraciones de VLANs (especialmente la VLAN de gestión y la nativa) en sus valores predeterminados (ej. VLAN 1 o VLAN 0).
  * **IDs de VLAN por Departamento/Tipo de Tráfico**: Crear VLANs específicas para cada departamento, tipo de tráfico (voz, datos, invitados) o nivel de criticidad (ej. VLAN con ID por departamento).
  * **Desconectar Puertos no Usados**: Deshabilitar físicamente (y lógicamente) todos los puertos del switch que no estén en uso. Esto previene que alguien pueda conectar un cable y obtener acceso no autorizado a una VLAN. Este es un problema asociado a la **seguridad física**.
  * **Desactivar Puertos Trunk no Usados**: Los puertos trunk son críticos; si no se utilizan, deben estar deshabilitados.
  * **Crear una VLAN de Gestión Separada**: Definir y utilizar una VLAN de gestión (Management VLAN) separada de la VLAN por defecto (VLAN 1/0). Esto asegura que los puertos de gestión del switch no estén expuestos al resto de usuarios de la red, lo que es una buena práctica de seguridad.
  * **Permitir Solo Acceso SSH a la VLAN de Gestión**: Configurar los puertos de la VLAN de gestión para que solo permitan acceso a través de protocolos seguros como **SSH** (Secure Shell), y no otros menos seguros como Telnet.
  * **Crear una VLAN para Invitados (`Guest VLAN`)**: No meter equipos que no están controlados por la organización dentro de la red corporativa. La VLAN de invitados debe tener un acceso a Internet muy limitado y ningún acceso a la red interna.
  * **Segmentación para VoIP**: Mantener el tráfico de Voz IP en una VLAN diferente a la de datos para asegurar rendimiento y reducir vectores de ataque.
  * **Filtrado de Puertos Estricto**: Utilizar solo los puertos que se necesitan en cada VLAN, ni uno más ni uno menos. Implementar listas de control de acceso (ACLs) para filtrar el tráfico en los puertos.
  * **Evitar Reglas "VLAN a VLAN" Generales**: Se debe evitar crear reglas de enrutamiento o filtrado que permitan tráfico indiscriminado entre VLANs completas, a menos que sea estrictamente necesario. Es preferible utilizar reglas más específicas del tipo **VLAN a Host** o **Host a VLAN**, lo que proporciona un control de acceso mucho más granular y reduce la superficie de ataque.
  * **Port Security**: Algunos switches pueden establecer políticas de seguridad asociadas al tipo de puerto (Port Security). Esto permite limitar el número de MACs que pueden circular por las VLANs, filtrarlas, activar la desconexión directa del puerto trunk si hay actividad extraña y enviar alertas (ej. usando SNMP).

## Conclusión

Este ejercicio práctico con Cisco Packet Tracer demuestra la facilidad y la potencia de configurar VLANs para segmentar una red. Hemos aprendido a crear VLANs, asignar puertos de acceso, configurar puertos trunk para la comunicación entre switches y verificar el aislamiento mediante pruebas de `ping`. Lo que hemos hecho en esta práctica se puede implementar directamente en un switch de un modelo concreto y funcionará en el mundo real.

En resumen, la implementación de VLANs es una estrategia esencial para securizar redes de datos y garantizar su eficiencia y confiabilidad en el mundo real. Al poder segmentar redes físicas en redes lógicas, las VLANs, gestionadas por switches adecuados, se convierten en una técnica crítica que debe utilizarse en cualquier arquitectura que pretenda alcanzar un alto nivel de seguridad. Esto proporciona una sólida defensa contra intrusiones y amenazas, contribuyendo a la integridad y confidencialidad de los datos de la organización.