## 2\. Configuración de Red IPv6 en Windows

La configuración y visualización de redes IPv6 en sistemas operativos Windows es un proceso relativamente sencillo, accesible tanto desde la interfaz gráfica como desde la línea de comandos. Para una correcta configuración global, es fundamental que el enrutador principal soporte IPv6 y que el proveedor de servicios de Internet (ISP) asigne la dirección correcta (ya sea por SLAAC o DHCPv6).

### 2.1. Verificación y Configuración Gráfica (Interfaz Moderna)

1.  **Acceso a la Interfaz de Red**: Dirígete a la configuración de red de Windows. Puedes hacerlo buscando "Estado de la red" en el menú de inicio o accediendo a la "Configuración" del sistema y luego a la sección "Red e Internet".

2.  **Selección del Adaptador**: Pincha sobre el adaptador de red que tienes conectado a Internet (por ejemplo, "Ethernet" o "Wi-Fi").

3.  **Visualización de Propiedades**: Se visualizará la información del perfil de red. Desplázate hacia abajo hasta la sección de "Configuración de dirección IP". Aquí podrás ver tu dirección IPv4 y, si está configurada, una **dirección IPv6 del tipo *link-local***, que típicamente comienza por `fe80` seguida de varios ceros y una dirección única.

4.  **Edición de Configuración IP**: Para modificar o ver la configuración de autoconfiguración, haz clic en "Editar" en la sección de "Asignación de IP". Por defecto, suele estar configurado en **DHCP (Automático)**.

5.  **Configuración Manual o Automática**:

      * **Automática (DHCP)**: Si el router cuenta con un servidor DHCPv6, se rellenarán automáticamente todos los campos. Si se configura por **SLAAC**, solo se configurará la dirección IP a través de los mensajes de anuncio del router, pero los DNS deberán rellenarse manualmente.
      * **Manual**: Al cambiar a "Manual", podrás configurar manualmente las direcciones IPv6, incluyendo:
          * **Dirección IP**: La dirección IPv6 específica para el dispositivo.
          * **Prefijo de Subred**: La longitud del prefijo de la subred.
          * **Puerta de Enlace (Gateway)**: La dirección del router en la red IPv6.
          * **DNS IPv6 preferido y alternativo**.

    **Nota**: Si solo tienes configurada una dirección *link-local* (que comienza con `fe80`), solo podrás comunicarte con otras máquinas IPv6 dentro de la misma red local.

### 2.2. Verificación y Configuración Gráfica (Interfaz Antigua - Panel de Control)

También puedes acceder a la configuración de red desde el "Panel de Control", que ofrece una interfaz más tradicional.

1.  **Acceder a Conexiones de Red**: Abre el "Panel de Control", navega a "Redes e Internet" y luego a "Centro de redes y recursos compartidos". Haz clic en "Cambiar configuración del adaptador" en el panel izquierdo.

2.  **Propiedades del Adaptador**: Haz clic derecho sobre tu adaptador de red (ej., "Ethernet" o "Wi-Fi") y selecciona **"Propiedades"**.

3.  **Protocolo de Internet versión 6 (TCP/IPv6)**: En la lista de elementos, desplázate hasta encontrar **"Protocolo de Internet versión 6 (TCP/IPv6)"** y selecciónalo. Luego haz clic en **"Propiedades"**.

4.  **Ajustar Propiedades**: Aquí encontrarás opciones similares a la interfaz moderna para configurar la dirección IP y los servidores DNS, ya sea de forma automática u manual.

### 2.3. Verificación de IPv6 por Línea de Comandos (Netsh)

La herramienta `netsh` en Windows permite gestionar las interfaces de red y ver información detallada de IPv6.

1.  **Abrir Símbolo del Sistema (CMD) como Administrador**: Busca "cmd" en el menú de inicio, haz clic derecho y selecciona "Ejecutar como administrador".

2.  **Ejecutar el comando `netsh`**:

    ```cmd
    netsh interface ipv6 show address
    ```

      * **`netsh`**: Es una utilidad de línea de comandos que permite configurar y monitorear componentes de red de Windows.
      * **`interface`**: Subcontexto para comandos relacionados con interfaces de red.
      * **`ipv6`**: Especifica que los comandos se aplicarán a IPv6.
      * **`show address`**: Muestra las direcciones IPv6 configuradas en las interfaces de red.

    **Objetivo**: Este comando mostrará todas las direcciones IPv6 configuradas en tu sistema.
    **Resultado**: Verás la **dirección de *loopback*** (`::1`), y las direcciones *link-local* (que empiezan con `fe80`) para tus adaptadores de red. Si tu router asigna una dirección *global unicast*, también aparecerá aquí.

## 3\. Configuración de Red IPv6 en Linux (Ubuntu)

En sistemas operativos Linux, como Ubuntu, la verificación y configuración de IPv6 se puede realizar tanto a través de la interfaz gráfica como, de forma más potente y detallada, mediante la línea de comandos.

### 3.1. Verificación y Configuración Gráfica (Ajustes de Red)

1.  **Acceso a Ajustes de Red**: Dirígete a la sección de "Ajustes" o "Settings" de tu sistema. Luego, selecciona la opción "Red" o "Network".

2.  **Selección del Adaptador**: Haz clic en la interfaz de red que estás utilizando (ej., "Wired" o "Wi-Fi").

3.  **Detalles de la Interfaz**: En la sección de configuración, encontrarás la **dirección IPv4** y también la **dirección IPv6**. De nuevo, es común ver una dirección de enlace local (`fe80::...`).

4.  **Configuración de IPv6**: Busca la pestaña o sección de "IPv6". Aquí verás las opciones para cómo obtener la dirección IPv6:

      * **Automático (DHCP / SLAAC)**: Para que se asigne automáticamente cualquier dirección global unicast si el router lo proporciona.
      * **Solo enlace local (Link-Local Only)**: Para usar únicamente direcciones *link-local*.
      * **Deshabilitar (Disable)**: Para desactivar IPv6 en la interfaz.
      * **Manual**: Para asignar una dirección IPv6 *global unicast* de forma manual, si conoces la dirección.

### 3.2. Verificación de IPv6 por Línea de Comandos (IP Command)

El comando `ip` en Linux es una herramienta muy potente y versátil para gestionar y ver información relativa a las interfaces de red.

1.  **Abrir la Terminal**: Puedes hacerlo con `Ctrl + Alt + T` o buscando "Terminal" en tus aplicaciones.

2.  **Ejecutar el comando `ip -6 address`**:

    ```bash
    ip -6 address
    ```

      * **`ip`**: Es un comando de Linux que muestra y manipula dispositivos de enrutamiento, políticas de enrutamiento y túneles. Es el reemplazo moderno de `ifconfig`.
      * **`-6`**: Esta opción se utiliza para especificar que queremos que el comando `ip` muestre únicamente la información relativa al **protocolo IPv6**. Si no se usa, mostrará tanto IPv4 como IPv6.
      * **`address`** (o `addr` o `a`): Es el **objeto** con el que queremos interactuar. En este caso, le estamos diciendo a `ip` que muestre información sobre las **direcciones de red** configuradas en las interfaces.

    **Objetivo**: El objetivo de este comando es obtener una lista detallada de todas las direcciones IPv6 configuradas en cada una de las interfaces de red del sistema, incluyendo sus propiedades como el *scope* (alcance), *valid lifetime* y *preferred lifetime*.

    **Resultado**:

      * Verás la **dirección de *loopback*** (`::1/128`), que es constante en todos los sistemas y se utiliza para la comunicación interna del dispositivo.
      * Para cada interfaz de red (ej., `eth0`), verás su dirección *link-local* (que empieza con `fe80::`).
      * Si tu router o servidor DHCPv6 ha asignado una dirección *global unicast*, también la verás listada aquí.

    **Sintaxis completa del comando `ip`**:
    `ip [OPTIONS] OBJECT { COMMAND | help }`

      * `OPTIONS`: Modifican el comportamiento del comando. `-6` es una de ellas.
      * `OBJECT`: El tipo de recurso de red con el que queremos trabajar (ej., `address`, `link`, `route`, `neighbor`).
      * `COMMAND`: La acción que queremos realizar sobre el objeto (ej., `show`, `add`, `del`). `show` es el predeterminado si no se especifica.
      * `help`: Muestra la ayuda para el objeto o comando.

    Este comando es muy útil para diagnosticar problemas de conectividad IPv6 y verificar la configuración de red de un vistazo.

## 4\. Conclusión

Configurar y verificar IPv6 en diferentes sistemas operativos es una tarea directa gracias a las herramientas integradas. Tanto la asignación automática de direcciones mediante **SLAAC** o **DHCPv6**, como la configuración manual de direcciones y otros parámetros de red IPv6, son opciones viables y accesibles para administradores de red y usuarios finales en diversas plataformas. Esto permite a los usuarios asegurarse de que sus sistemas estén preparados para la conectividad global a través de este protocolo moderno.

-----