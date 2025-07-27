Aquí tienes el informe completo sobre la configuración de Squid y SquidGuard en PFSense para hardening de redes, estructurado de forma clara y exhaustiva para estudiantes, basado en los apuntes y las imágenes proporcionadas.

---

# Hardening de Redes con PFSense: Configuración de Proxy Transparente con Squid y Filtrado de Contenido con SquidGuard

Este informe detalla cómo utilizar **PFSense** para implementar técnicas avanzadas de **hardening de redes**, centrándose en la configuración de un **proxy transparente** con **Squid** y la gestión de **listas blancas (Whitelists)** y **listas negras (Blacklists)** con **SquidGuard**. Comprender estas prácticas es crucial para proteger a los usuarios de sitios peligrosos, controlar el acceso a contenido web y optimizar el rendimiento de la red en un entorno empresarial o doméstico.

## 1. Introducción al Proxy Transparente, Blacklists y Whitelists

El **hardening de una red de datos** que involucra clientes, usuarios y servicios a menudo incluye la implementación de dos acciones clave:

1.  **Uso de un Proxy Transparente**: Para redirigir todo el tráfico web a través de un punto centralizado sin que el usuario final tenga conocimiento de este redireccionamiento.
2.  **Uso de Blacklists y Whitelists**: Listas negras y blancas de acceso para permitir o bloquear el acceso a determinadas páginas web o categorías de sitios web.

Estas acciones son típicas en el **hardening empresarial** para:
* Evitar que los usuarios accedan a sitios peligrosos que puedan poner en riesgo tanto la máquina como la red de la empresa.
* Controlar a qué se accede desde la red, principalmente con el objetivo de protegerla.

Para implementar esto en PFSense, se utilizan **Squid** (como proxy con opción de proxy transparente) y **SquidGuard** (para gestionar Blacklists y Whitelists).

## 2. Instalación de Squid y SquidGuard en PFSense

El primer paso es asegurarse de que Squid y SquidGuard estén instalados en tu instancia de PFSense.

1.  **Acceso al Gestor de Paquetes**: Navega en la interfaz web de PFSense a **System > Package Manager**.
2.  **Búsqueda e Instalación**:
    * Si no los tienes instalados, dirígete a la pestaña **"Available Packages"** (Paquetes Disponibles).
    * Busca "Squid" y "SquidGuard" en la barra de búsqueda.
    * Haz clic en "Install" (o "Install Package") junto a cada uno de ellos para iniciar la instalación.
3.  **Verificación**: Una vez instalados, aparecerán en la sección **Services** del menú principal.

## 3. Configuración del Proxy Transparente con Squid

**Squid** es un *proxy* que optimiza el acceso a Internet al guardar en memoria local el contenido web que se usa con frecuencia, reduciendo la carga de la conexión y ahorrando ancho de banda. Para configurarlo como proxy transparente en PFSense:

1.  **Acceso a la Configuración de Squid**: Navega a **Services > Squid Proxy Server > General**.

### 3.1. Pestaña "General Settings"

* **Habilitar Proxy**: Marca la opción **"Enable Squid Proxy"**. Esto activa el servicio de proxy.
* **Proxy Interfaces**: Especifica la interfaz de red donde Squid escuchará las peticiones de los clientes. Selecciona la interfaz **LAN**.
* **Proxy Port**: El puerto por defecto para Squid es **3128**, pero se puede cambiar si es necesario.
* **Transparent Proxy Settings**:
    * Marca la opción **"Transparent HTTP Proxy"**. Esto redirigirá automáticamente todo el tráfico HTTP del puerto 80 al proxy sin configuración adicional en el cliente.
    * Asegúrate de que la interfaz seleccionada para el modo transparente sea la **LAN**.
* **SSL Man In the Middle Filtering (HTTPS/SSL Interception)**:
    * Para interceptar tráfico **HTTPS**, debes habilitar la opción **"Enable SSL filtering"**.
    * **Advertencia**: Esto requiere tener un **Certificado de Autoridad (CA)** instalado en los clientes para que no aparezcan errores de seguridad en el navegador. PFSense creará uno por defecto (generalmente llamado `Squid-CA` o similar) que deberás exportar e importar en los navegadores de tus clientes.
    * **SSL/MITM Mode**:
        * **Splice All**: Esta es la opción recomendada si vas a usar SquidGuard para el filtrado web. Significa que todas las conexiones SSL serán "spliceadas" (el proxy actúa como un túnel pasivo sin descifrar el tráfico) y SquidGuard podrá denegar o permitir destinos según sus reglas, tal como lo hace con HTTP. No se necesita instalar el certificado CA en los clientes si se usa solo para denegar, pero si quieres inspeccionar el tráfico cifrado, el CA es necesario.
        * *Splice Whitelist, Bump Otherwise*: Las conexiones a destinos en la *Whitelist* se *splicean*, el resto se "bump", es decir, se descifran, inspeccionan y se vuelven a cifrar. Esto requiere el CA en los clientes.
    * **CA**: Selecciona el Certificado de Autoridad (CA) que se utilizará para la intercepción SSL (ej. `Squid-CA`).
* **Logging Settings**:
    * Marca **"Enable Access Logging"** para habilitar el registro de accesos.
    * La opción **"Real Time"** (en la parte superior de la página de logs de Squid) permite ver en tiempo real qué máquinas se están conectando y hacia dónde. Es útil para una vista rápida de la actividad de la red.

### 3.1. Pestaña "Local Cache"

Esta sección es crítica para el rendimiento óptimo del sistema, ya que la caché local almacena el contenido de sitios web que ya se han solicitado previamente.

* **Ventajas del Caching Local**:
    * **Reduce el tiempo de carga**: Cuando un usuario solicita el contenido de nuevo, Squid lo sirve directamente desde la caché en lugar de volver a cargarlo de Internet.
    * **Ahorro de ancho de banda**: Al servir contenido desde la caché, se reduce la necesidad de conectar con servidores externos.
    * **Mejora la experiencia del usuario**: Las páginas se cargan más rápido.
* **Configuración por defecto**: Las opciones por defecto suelen ser suficientes.

### 3.1. Pestaña "Access Control" (ACLs)

Squid permite una gestión exhaustiva de las listas de acceso. Aquí se pueden definir reglas basadas en direcciones IP, subredes o nombres de *host*.

* **Permitted Subnets**: Define las subredes permitidas.
* **Unrestricted IPs**: IPs que no están sujetas a restricciones del proxy.
* **Banned Hosts/Addresses**: IPs o *hosts* que tienen prohibido el paso a través del proxy.
* **Whitelisted Hosts**: Direcciones que no pasarán por el *proxy* (se saltan sus reglas).
* **Authenticated Users**: Posibilidad de configurar que los usuarios deban autenticarse directamente contra el *proxy* para navegar, lo cual ofrece un control absoluto y es ideal para entornos con **Directorio Activo** o **LDAP**.

### 3.1. Pestaña "Antivirus"

Squid también incluye una opción para integrar un antivirus, como **ClamAV**, que puede chequear en tiempo real todo el tráfico de ficheros que el usuario descarga o sube a Internet. Aunque tiene un coste computacional, es una alternativa útil para la seguridad.

Una vez realizadas las configuraciones, cualquier usuario dentro de la red pasará por el proxy transparente y todo su tráfico será interceptado.

## 4. Filtrado de Contenido con SquidGuard (Blacklists y Whitelists)

**SquidGuard** es un paquete adicional para Squid que permite activar y gestionar **Blacklists (listas negras)** y **Whitelists (listas blancas)** para el filtrado de contenido web. Proporciona un filtrado de contenido robusto, permitiendo a los administradores aplicar políticas de acceso y proteger contra sitios web maliciosos, mejorando la seguridad y la productividad de la red.

1.  **Acceso a la Configuración de SquidGuard**: Navega a **Services > SquidGuard Proxy Filter**.

### 4.1. Pestaña "General Settings"

* **Habilitar Blacklist**: Es fundamental marcar la opción para **"Enable blacklist"**.
* **Opciones LDAP**: Permite integrar con un servicio LDAP para autenticación.
* **Opciones de Logging**: Habilita el registro de accesos para SquidGuard.

### 4.1. Pestaña "Blacklist"

1.  **URL de Blacklist**: Introduce una dirección web de donde descargar las *blacklists*. Existen varias publicaciones y sitios que ofrecen listados de categorías predefinidas (ej. "Shalla's Blacklists" o "Université Toulouse Capitole blacklist"). Al hacer clic en "Download", la *blacklist* se instalará y se integrará con Squid y SquidGuard para bloquear servicios y páginas web.
    * Una *blacklist* es un listado de categorías y accesos a Internet que no se desea que los usuarios puedan acceder. Las categorías pueden incluir redes sociales, videojuegos, alcohol, drogas, etc..

### 4.1. Pestaña "Common ACL" (Listas de Acceso Comunes)

Aquí se gestionan las políticas de acceso para las categorías de la *blacklist* y las *whitelists*.

* **Reglas por Categoría**: Para cada categoría de la *blacklist* cargada (ej., "socialmed", "news", "shopping", "alcohol", "chatting", "dating", "drugs"), puedes definir una acción:
    * **Allow**: Permite el acceso a toda la categoría.
    * **Deny**: Bloquea el acceso a toda la categoría.
    * **Whitelist**: Permite especificar un fichero o listado de URLs permitidas dentro de esa categoría, mientras que el resto se bloquea.
    * Si se ve un guion ("-") en una categoría, significa que aplicará la regla general por defecto (que suele ser "Allow").
* **Ejemplo de Aplicación**: Puedes configurar `socialmed` (redes sociales) como **Deny**. Esto sobreescribirá la regla general y bloqueará el acceso a sitios como Facebook. Sin embargo, si `News` está en `Allow` (o por defecto), las páginas de noticias como "elmundo.es" se abrirán sin problema.

### 4.1. Integración con Certificados (para HTTPS)

Para que el *proxy* pueda interceptar el tráfico HTTPS y aplicar el filtrado (especialmente si no se usa el modo *Splice All*), es necesario que el certificado CA que usa Squid (ej., `Squid-CA`) se exporte desde PFSense y se importe en los navegadores de los clientes.

* **Exportar CA**: Desde **System > Certificates > CAs**, selecciona el CA de Squid y expórtalo.
* **Importar en el Navegador**: En el navegador del cliente (ej., Firefox), ve a la configuración de seguridad e importa el certificado exportado.

Esto permite al *proxy* inspeccionar el tráfico HTTPS, lo cual es vital para el **hardening** de redes de datos, ya que proporciona un control significativo sobre el tráfico de los usuarios.

## 5. Consideraciones Finales y Alternativas

* **Discontinuación de Squid y SquidGuard**: Es importante destacar que Squid y SquidGuard han sido descontinuados para nuevas versiones de PFSense desde 2022.
* **Alternativas**: Existen alternativas en PFSense para las funcionalidades de proxy y filtrado:
    * **HAProxy**: Puede utilizarse como alternativa directa a Squid Proxy.
    * **PFBlockerNG**: Un paquete de PFSense que permite filtrar y bloquear IPs y dominios.
    * **DNSBL**: Una forma de bloquear dominios directamente a nivel de DNS.
    * **PFSense Plus**: La versión comercial de PFSense, que incluye características avanzadas de filtrado de contenido y seguridad a nivel de usuario.

Aunque estas alternativas pueden ser más complejas de instalar, Squid sigue siendo funcional para pruebas y aprendizaje.

## 6. Conclusión

La implementación de **Squid** y **SquidGuard** en PFSense ofrece una mejora significativa en el almacenamiento temporal de datos web y el filtrado de contenido, lo que se traduce en un aumento tanto en la eficiencia de la red como en su seguridad.

* **Squid** agiliza el acceso a Internet al guardar en memoria local el contenido usado con frecuencia, disminuyendo la carga de la conexión.
* **SquidGuard** permite establecer políticas de acceso personalizadas y bloquear sitios web no deseados o peligrosos, lo que fortalece la protección de la red y promueve un entorno de trabajo más seguro y productivo.

PFSense se consolida como una herramienta base invaluable para practicar y configurar dispositivos de red casi reales, permitiendo experimentar con funcionalidades como *routing*, **NAT**, direccionamiento y *gateways*.

---