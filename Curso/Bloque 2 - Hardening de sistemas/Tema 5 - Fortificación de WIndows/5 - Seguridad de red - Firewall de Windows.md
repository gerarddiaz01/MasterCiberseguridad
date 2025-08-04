# Informe Detallado de Seguridad de Red y Firewall de Windows

**Documentos de Referencia:** "5-10 Seguridad en la Red.pdf", "5-11 Ejercicio de seguridad de red.pdf", "FSW Clase 10 – Seguridad de Red.pdf"

La seguridad de un dispositivo no se limita solo a su sistema operativo, sino que también depende de una configuración de red robusta. Para lograrlo, es fundamental verificar y comprender una serie de elementos clave, siendo el firewall de Windows una pieza central en esta estrategia.

## Elementos Clave en la Configuración de Seguridad de Red

Para poder entender la seguridad de un dispositivo es esencial verificar la configuración de los adaptadores de red, los elementos compartidos, las zonas de seguridad del navegador y los servicios del sistema.

### Configuración del Adaptador de Red

El primer paso para una seguridad de red efectiva es revisar la configuración del adaptador o adaptadores de red. Esto asegura que no haya configuraciones inadecuadas o extrañas. Dentro de la configuración de red y Ethernet, se pueden gestionar aspectos como el tipo de red (pública o privada), la autenticación para protocolos como IEX, la asignación de IP a través de DHCP, y los servicios DNS. También se puede copiar información sobre la configuración del adaptador de red.

Las opciones avanzadas de red permiten renombrar el adaptador o editar directamente sus propiedades. Desde aquí, es posible inspeccionar y configurar protocolos fundamentales como **TCP/IP IPv4** y **TCP/IP IPv6**, así como los servicios **DNS** y **WINS**.

### Recursos Compartidos y sus Implicaciones de Seguridad

Los recursos compartidos, como impresoras o carpetas, son necesarios en una red privada para la comunicación entre dispositivos o servidores. Sin embargo, estos mismos elementos, si se mantienen abiertos fuera del entorno de una red empresarial o local, pueden representar un serio peligro de seguridad.

Es crucial tener en cuenta:
* Qué se está compartiendo.
* Qué características del sistema operativo están habilitadas para buscar recursos compartidos en la red.
* Si esos elementos deben estar configurados o aprobar conexiones en función de la ubicación del dispositivo.

Esto cobra especial importancia en dispositivos portátiles (laptops, tablets, móviles) que se mueven geográficamente. Si estos dispositivos tienen servicios de búsqueda de recursos compartidos abiertos mientras están conectados a una red pública (hotel, aeropuerto, cafetería), se genera un riesgo de seguridad importante.

En Windows, las opciones de recursos compartidos se gestionan por perfil. Por ejemplo, en un perfil de **red pública**, las opciones de compartir archivos o impresoras y el descubrimiento de red suelen estar deshabilitadas. En **redes privadas**, el descubrimiento de red puede estar habilitado, pero los servicios de compartir archivos e impresoras deberían estar desactivados hasta que sean necesarios para una función específica.

### Zonas de Seguridad de Internet

Windows permite personalizar el funcionamiento del navegador basándose en zonas de seguridad. Estas zonas asignan automáticamente todos los sitios web a una de las siguientes categorías:
* **Internet:** Para sitios web generales de Internet, excluyendo los de sitios de confianza y restringidos.
* **Intranet local:** Para la red interna.
* **Sitios de confianza:** Sitios web que no se consideran una amenaza para la seguridad del equipo o sus archivos.
* **Sitios restringidos:** Sitios web que podrían ser maliciosos.

Cada una de estas zonas se puede configurar con un nivel de seguridad diferente, lo que determina el tipo de contenido que se bloqueará. Esto incluye la capacidad de ejecutar **JavaScript**, complementos (**ActiveX**), descargar ciertos elementos o permitir el funcionamiento de software y aplicaciones. La configuración adecuada puede ser la diferencia entre que una web maliciosa logre o no ejecutar un ataque en el dispositivo.

Las propiedades de Internet, accesibles desde las opciones de red, permiten personalizar manualmente cada complemento para decidir qué se permite habilitar cuando el navegador detecta que está en una zona de confianza o en la zona de Internet.

### Servicios de Windows

Los servicios son otro elemento fundamental para la seguridad de red, especialmente en servidores, pero también en equipos cliente. Se pueden ver los servicios en funcionamiento y los que están "a la escucha" utilizando el comando `sc list` o a través de la consola de servicios (`services.msc`), accesible desde el Administrador de Tareas.

La consola de servicios ofrece información detallada, incluyendo:
* Descripción del servicio.
* Estado: Si está detenido (`stopped`) o iniciado (`running`).
* Modo de inicio: Automático, manual o deshabilitado.
* Cuenta utilizada para ejecutar el servicio (`Log On As`): Esto es vital, ya que no todas las cuentas tienen los mismos privilegios. Por ejemplo, `Local System` tiene todos los privilegios sobre el sistema, mientras que `LocalService` o `Network Service` tienen menos.
Se aconseja controlar la ejecución de servicios y deshabilitar aquellos que no sean necesarios, o verificar que no se pueda acceder a ellos cuando el dispositivo está en una red no confiable.

## El Firewall de Windows con Seguridad Avanzada

El **Firewall de Windows** es un componente de seguridad crítico que trabaja bajo tres perfiles de conexión diferentes: **Dominio**, **Privado** y **Público**. Cada perfil aplica diferentes reglas de restricción de tráfico según el entorno de red asignado.

* **Red de Dominio:** Configuración de reglas para un entorno empresarial, donde el firewall puede gestionarse centralmente mediante objetos de política de grupo (**GPO**).
* **Red Privada:** Diseñada para entornos de confianza (como el hogar). Es menos restrictiva y permite la apertura de ciertos puertos para recursos compartidos o conexiones a impresoras.
* **Red Pública:** Configuración para conexiones en redes desconocidas. Debe ser lo más restrictiva posible, cerrando puertos que en otros perfiles podrían estar abiertos.

La clave es que, al configurar el firewall, se deben aplicar las reglas adecuadas al perfil correcto. Por ejemplo, permitir solicitudes de ping o accesos a carpetas compartidas en una red privada o de dominio tiene sentido, pero no en una red pública, donde nadie debería necesitar verificar la conexión o buscar recursos compartidos en el dispositivo.

### Reglas de Tráfico (Entrada y Salida)

El Firewall de Windows con Seguridad Avanzada permite configurar reglas para permitir o restringir el tráfico tanto de entrada como de salida.
* **Reglas de Entrada:** Controlan las conexiones que llegan al equipo.
* **Reglas de Salida:** Controlan las conexiones que salen del equipo. Son fundamentales para prevenir que el **malware** se comunique con servidores externos o descargue componentes adicionales.

Además, el firewall permite:
* Exportar e importar reglas, facilitando su despliegue y respaldo.
* Habilitar notificaciones cuando bloquea una nueva aplicación. Esto permite al usuario crear una excepción rápidamente si es necesario para una aplicación legítima.

### Reglas de Seguridad de Conexión

Las **Reglas de Seguridad de Conexión** son una de las características más interesantes y potentes del Firewall de Windows. Permiten definir cómo se conectan los dispositivos entre sí (uno a uno, uno a muchos, muchos a uno, o muchos a muchos).
Estas reglas permiten configurar:
* **Autenticación:** Si se requiere autenticación en uno o ambos extremos de la comunicación. La autenticación puede ser a través de **IPSec**, **Kerberos**, **NTLM**, certificados o una clave compartida. Se pueden añadir múltiples factores de autenticación.
* **Cifrado:** Si la comunicación debe estar cifrada.
* **Protección con IPSec:** Permiten habilitar **reglas de túnel** que funcionan con **IPSec** y utilizan cifrados como **DES**, **3DES** o **AES**, añadiendo una capa adicional de seguridad, especialmente dentro de la red interna. Esto dificulta que un atacante que esté analizando o capturando el tráfico en la red pueda acceder a la información.

### Configuración Práctica del Firewall de Windows y las Reglas de Conexión

Para acceder a las opciones avanzadas del firewall, se puede hacer desde la configuración avanzada de red.

**Creación de una Regla de Seguridad de Conexión (Ejemplo):**
1. En el Firewall de Windows con Seguridad Avanzada, selecciona **"Reglas de seguridad de conexión"** y luego **"Nueva regla..."**.
2. Elige el tipo de regla **"Personalizada"** y haz clic en "Siguiente".
3. Define el **origen y destino** de la comunicación. Esto puede ser:
    * Una dirección IP específica.
    * Un rango de red (ej. `192.168.1.0/24`).
    * Un grupo de servidores.
4. Define la **acción de autenticación**:
    * **Solicitar autenticación:** Intentará autenticar pero no detendrá la comunicación si falla.
    * **Requerir autenticación:** Obligará el proceso de autenticación y cortará la comunicación si no se cumple.
5. Especifica el **método de autenticación** (IPSec, Kerberos, NTLM, certificados, clave compartida).
6. Define los **protocolos y puertos** específicos (ej. TCP, puerto 80 y 445).
7. Selecciona el **perfil** donde se aplicará la regla (privado, dominio, público).
8. Asigna un **nombre** a la regla y finaliza.

## Ejercicio: Configurar una Regla de Tráfico Entrante para Permitir sólo la Petición PING

Este ejercicio práctico demuestra cómo configurar una regla de firewall para permitir exclusivamente las solicitudes de eco (ping), crucial para realizar pruebas de conexión de forma controlada.

**Pasos a seguir:**
1. **Abrir el Firewall de Windows con seguridad avanzada:** Buscar "Firewall" en el menú de inicio y seleccionar **"Firewall de Windows con seguridad avanzada"**.
2. **Ir a "Reglas de entrada":** En el panel izquierdo, seleccionar **"Reglas de entrada"**.
3. **Crear una "Nueva regla...":** En el panel derecho, hacer clic en "Nueva regla...".
4. **Tipo de regla:** Seleccionar **"Personalizado"** y hacer clic en "Siguiente".
5. **Programa:** Seleccionar **"Todos los programas"** y hacer clic en "Siguiente".
6. **Protocolo y Puertos:**
    * En el menú desplegable "Tipo de protocolo:", seleccionar **"ICMPv4"** (Protocolo de mensaje de control de Internet).
    * Hacer clic en el botón **"Personalizar..."** junto a "Configuración de protocolo ICMP".
    * Dentro de la ventana "Personalizar configuración de ICMP", seleccionar **"Tipos ICMP específicos"** y marcar únicamente la casilla **"Solicitud de eco"**. Esto es crucial porque ICMP engloba muchos otros tipos y solo se desea permitir el ping. ICMP viene cerrado por defecto debido a ataques conocidos.
    * Hacer clic en "OK" y luego en "Siguiente".
7. **Ámbito (Scope):**
    * Aquí se puede especificar las direcciones IP locales y remotas a las que se aplica la regla.
    * Se puede elegir **"Cualquier dirección IP"** para permitir desde cualquier origen o **"Estas direcciones IP"** para restringir.
    * Es posible añadir una dirección IP o subred específica (ej., `192.168.1.0/24`) o un rango de direcciones IP. Esto permite, por ejemplo, que solo los administradores de TI puedan hacer ping al dispositivo.
    * Hacer clic en "Siguiente".
8. **Acción:** Seleccionar **"Permitir la conexión"**. También se pueden crear reglas para bloquear (`Denegar`) conexiones si se conoce un **malware** que utiliza puertos o protocolos específicos.
9. **Perfil:** Marcar los perfiles de red donde la regla estará activa. Para este ejercicio, se debe marcar **"Dominio"** y **"Privado"**. Es fundamental **no** seleccionar **"Público"**, ya que no tiene sentido permitir solicitudes de eco a un dispositivo en una red pública no confiable.
10. **Nombre:** Asignar un nombre a la regla (ej., "Permitir PING ICMPv4 para Red Interna") y hacer clic en "Finalizar".

De esta manera, se permite el ping al dispositivo desde una red específica solo cuando está en la red interna de la organización, pero no cuando utiliza una red pública.

### Conclusiones de la Seguridad de Red

Es esencial verificar las conexiones, empezando por revisar las propiedades del adaptador y la configuración de recursos compartidos. El Firewall de Windows es un excelente aliado para controlar las conexiones y añadir una capa adicional de seguridad a la red local. Asimismo, es necesario controlar la ejecución de servicios y otras aplicaciones que utilizan conexiones de red, ya que cualquiera de estos elementos podría ser una puerta para conexiones no autorizadas o **malware**.