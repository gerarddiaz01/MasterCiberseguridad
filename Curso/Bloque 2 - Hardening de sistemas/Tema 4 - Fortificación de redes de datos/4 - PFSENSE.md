Aquí tienes el informe completo sobre PFSense, su configuración y uso, estructurado de forma clara y exhaustiva para estudiantes, basado en los apuntes proporcionados.

-----

# PFSense: Una Plataforma Abierta para el Hardening de Redes y la Seguridad

Este informe introduce **PFSense**, una potente plataforma de *routing* y *firewall* de código abierto, ideal para comprender y practicar conceptos avanzados de **hardening de redes**. Se explorarán sus características, el entorno de laboratorio recomendado para su despliegue como máquina virtual, los requisitos de configuración, y las funcionalidades clave de su interfaz, destacando su flexibilidad y escalabilidad.

## 1\. ¿Qué es PFSense?

**PFSense** es una plataforma de *routing* y *firewall* de **código abierto** basada en **FreeBSD**. Está diseñada para proporcionar funcionalidades avanzadas de seguridad y gestión de redes. Es una herramienta excelente para entender y practicar conceptos de **hardening de redes** debido a su:

  * **Flexibilidad**: Se adapta a diversas configuraciones y necesidades.
  * **Escalabilidad**: Puede crecer con las demandas de una red.
  * **Amplia gama de características de seguridad**: Ofrece numerosas funcionalidades para proteger la infraestructura.
  * **Comunidad Open Source**: Cuenta con una gran comunidad detrás de su desarrollo.
  * **Soporte de Netgate**: Una empresa que respalda el proyecto y ofrece soluciones *enterprise*.

PFSense puede ser desplegado en dispositivos *hardware* dedicados, y muchos dispositivos de red lo llevan como parte integral de su sistema.

## 2\. Configuración del Entorno de Laboratorio con VirtualBox

Para realizar pruebas y aprender sobre PFSense, se recomienda el uso de un hipervisor gratuito como **VirtualBox**. Esto permite crear un laboratorio virtualizado para experimentar sin afectar una red real.

### 2.1. Arquitectura del Laboratorio

Un laboratorio típico para practicar con PFSense incluye:

  * **Una máquina virtual (VM) para PFSense**: Basada en FreeBSD.
  * **Varias máquinas virtuales con Linux (Ubuntu Desktop)**: Para simular la red interna y realizar pruebas. En el ejemplo propuesto, se utilizan cinco máquinas Ubuntu Desktop.

### 2.2. Obtención de la Imagen ISO de PFSense

1.  **Buscar en Google**: Escribe "pfsense" en el buscador y accede a la página oficial.
2.  **Sección de Descarga**: Navega a la sección de descargas.
3.  **Seleccionar Arquitectura**: Elige la arquitectura **AMD64 (64-bit)**, que es la más común.
4.  **Formato de Descarga**: Selecciona la opción de **imagen ISO** para facilitar el despliegue en VirtualBox.
5.  **Zona de Descarga**: Elige la región más cercana para la descarga (ej., Europa - Frankfurt).
6.  **Iniciar Descarga**: Haz clic en "Download" para comenzar la descarga de la imagen ISO.

### 2.3. Requisitos de la Máquina Virtual para PFSense en VirtualBox

Las características de la VM para PFSense no son muy exigentes, lo que facilita su despliegue:

  * **Memoria RAM**: 1 GB es suficiente para pruebas básicas.
  * **Procesador (vCPU)**: 2 núcleos para un rendimiento más fluido, aunque 1 núcleo también puede ser suficiente.
  * **Espacio en Disco**: Un disco pequeño de 15 GB, 20 GB o 30 GB es más que suficiente para evitar problemas de espacio.

### 2.4. Configuración Crítica de Adaptadores de Red

La configuración más importante para la VM de PFSense son sus adaptadores de red, ya que actuará como **pasarela y *router***. Necesita dos tarjetas de red:

  * **Adaptador 1 (WAN - Wide Area Network)**: Apuntando hacia la **red de Internet**. Configúralo como **NAT** en VirtualBox para que tenga una conexión directa a Internet.
  * **Adaptador 2 (LAN - Local Area Network)**: Apuntando hacia la **red interna**. Configúralo como **Red Interna** en VirtualBox, y puedes asignarle un nombre para identificarla.

**Importante**: El resto de las máquinas virtuales del laboratorio (ej., Ubuntu Desktop) deben configurarse con **un solo adaptador de red** apuntando exclusivamente a la **Red Interna**. De esta manera, todo su tráfico hacia Internet será gestionado por la máquina virtual con PFSense. Para las VMs de Ubuntu Desktop, se recomienda asignar 2 GB de RAM y 2 vCPU para un funcionamiento fluido, con aproximadamente 30 GB de espacio en disco.

## 3\. Instalación e Interfaz de Consola de PFSense

La instalación de PFSense es un proceso sencillo. Una vez que la ISO está mapeada en la VM y la máquina virtual se inicia, se siguen los pasos del asistente de instalación.

### 3.1. Pantalla de Consola de PFSense

Después de la instalación, la máquina virtual de PFSense mostrará una pantalla de consola con varias opciones. Aunque la mayoría de la gestión se realiza desde la interfaz web, esta consola es vital para ciertas operaciones más complejas y como registro de *logs*.

| Opción        | Descripción                                                                                         |
| :------------ | :-------------------------------------------------------------------------------------------------- |
| **0) Logout** | Cierra la sesión si se ha accedido vía SSH (no aplica para acceso directo desde el hipervisor).      |
| **1) Assign Interfaces** | **Muy importante**. Permite asignar y configurar las interfaces de red (WAN y LAN). Si se configuraron dos adaptadores en VirtualBox (NAT y Red Interna), PFSense los asignará automáticamente como WAN y LAN. Permite modificar parámetros asociados a las tarjetas de red. |
| **2) Set Interface(s) IP Address** | Configura las direcciones IP de las interfaces de red.                                       |
| **3) Reset webConfigurator password** | Restablece la contraseña de administrador para la interfaz web de PFSense.                   |
| **4) Reset to factory defaults** | Restablece PFSense a la configuración de fábrica.                                             |
| **5) Reboot system** | Reinicia el sistema PFSense. Útil para aplicar actualizaciones o resolver bloqueos.           |

**Nota**: La pantalla de consola también actúa como un registro de *logs*, mostrando en detalle los procesos y cambios que ocurren en la máquina PFSense, incluso si se realizan desde el *dashboard* web remoto.

## 4\. Gestión de PFSense a Través de la Interfaz Web (Dashboard)

La mayor parte de la configuración y gestión de PFSense se realiza a través de su interfaz web (*Dashboard*) desde una máquina remota de la red interna. En mi caso, al hacer las pruebas en maquinas virtuales, tuve que poner los adaptadores de red de la maquina de pfsense en NAT para la conexión a internet (WAN) y en red interna el segundo adaptador (LAN) para que la máquina de ubuntu desktop pueda acceder a pfsense. Luego en la maquina de ubuntu desktop con conexión a pfsense le puse sólo un adaptador de red en red interna, la misma LAN que pfsense, y pfsense da internet a dicho ubuntu directamente.

### 4.1. Acceso al Dashboard

1.  **Obtener la IP de la Interfaz LAN de PFSense**: Esta IP es la que actúa como gestor y punto de enrutamiento para toda la información. Se puede ver en la consola de PFSense o es la IP que asigna por defecto a la interfaz LAN. Normalmente es 192.168.1.1
2.  **Acceder desde el Navegador**: Abre un navegador web en una de las máquinas virtuales Linux (Ubuntu Desktop) de la red interna y escribe la dirección IP de la interfaz LAN de PFSense.
3.  **Credenciales Iniciales**: La contraseña por defecto para el acceso web es `pfsense`. Se recomienda cambiarla inmediatamente después del primer acceso.

### 4.2. Visión General del Dashboard

El Dashboard de PFSense es personalizable y puede mostrar información útil del sistema, como:

  * **Información del Sistema**: Uso de CPU, memoria RAM, espacio en disco, etc.
  * **Traffic Graph**: Muestra el tráfico en tiempo real en las interfaces WAN y LAN. Esto permite visualizar cómo el tráfico entra y sale de las diferentes interfaces.
  * **Widgets/Gadgets**: Se pueden añadir diferentes *widgets* al *dashboard* y también se añaden automáticamente al instalar paquetes adicionales, que son una de las grandes ventajas de PFSense.

### 4.3. Configuración General (General Setup)

Dentro del menú "System" \> "General Setup", se pueden configurar parámetros básicos:

  * **Hostname**: Nombre del host de PFSense.
  * **Domain**: Nombre del dominio (si aplica).
  * **Servidores DNS**: Idealmente, en un entorno empresarial se usarían DNS propios, pero para pruebas se pueden usar DNS públicos (ej., los de Google).

### 4.4. Gestión de Paquetes (Package Manager)

PFSense permite instalar una gran cantidad de paquetes adicionales que extienden sus funcionalidades. Desde el "Package Manager" (Gestor de Paquetes), se puede ver una lista de paquetes instalados y disponibles. Esto permite adaptar PFSense a requisitos específicos (ej., instalar **Snort** para **IDS/IPS** o **Squid** para un *proxy*).

### 4.5. Funcionalidades de Configuración Web

PFSense ofrece una interfaz web intuitiva para gestionar una amplia gama de funciones:

  * **System**: Incluye opciones avanzadas, certificados, *setup wizard* (asistente de configuración inicial), actualización del sistema, gestión de usuarios y *logout*.
  * **Interfaces**: Permite definir y configurar los parámetros de las interfaces **WAN y LAN**.
  * **Firewall**: Incluye el *firewall* por defecto (normalmente `iptables`), donde se pueden definir reglas **NAT** y reglas de acceso. También se pueden gestionar con paquetes como Squid.
  * **Services**: Muestra los servicios en ejecución y permite gestionarlos. Si se instala un paquete (ej., DHCP server, Snort, Squid), aparecerá aquí con sus interfaces de configuración.
  * **VPN**: Una característica muy potente de PFSense es la capacidad de crear una **VPN** utilizando protocolos como **OpenVPN**, **IPSec** o **L2TP**. Esto es ideal para laboratorios y, con la configuración adecuada, puede usarse en entornos de producción.
  * **Status**: Proporciona una visión global del estado del sistema y de los servicios en ejecución (ej., portal cautivo, NTP, OpenVPN).
  * **Diagnostics**: Muy útil para resolver problemas, ya que ofrece varios comandos de diagnóstico para identificar fallos en la arquitectura.

PFSense también muestra iconos asociados a los servicios que permiten reiniciarlos o detenerlos, una funcionalidad importante al aplicar cambios o solucionar problemas.

## 5\. Conclusión

PFSense es una herramienta excelente para dominar elementos críticos de la seguridad de red, como *routers* y *firewalls*. Su facilidad de uso y la cantidad de funcionalidades avanzadas que proporciona la convierten en una plataforma muy práctica y flexible. Permite a los usuarios experimentar con diversas configuraciones de seguridad, incluyendo **VPNs**, **balanceo de carga**, **filtrado de contenido** y **configuración de *firewalls***.

Proporciona una base sólida para gestionar una red como si se tratara de un dispositivo de red real, lo que lo convierte en un recurso invaluable para estudiantes y profesionales que buscan fortalecer sus habilidades en **ciberseguridad**.

-----