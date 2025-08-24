Documentos de Referencia: "RE - SMB enumeration.pdf"

# Informe Técnico: Enumeración de SMB

## 1. Resumen Ejecutivo

Este informe técnico explora la **enumeración SMB** (Server Message Block), un proceso de ciberseguridad para recopilar información sobre recursos compartidos, usuarios, y grupos en una red. Se destaca la importancia de este proceso para identificar vulnerabilidades y puntos de entrada. El documento detalla el uso de herramientas especializadas como **enum4Linux**, **nbtscan**, y **smbmap**. Se explican los procedimientos prácticos para el descubrimiento de hosts, la enumeración de usuarios y recursos compartidos, y la ejecución de comandos de forma remota. El informe también subraya la importancia de aplicar medidas de seguridad sólidas para mitigar los riesgos asociados a la exposición de esta información sensible.

---

## 2. Conceptos Fundamentales

* **SMB (Server Message Block):** Protocolo de red fundamental para compartir archivos, impresoras y otros recursos entre nodos en una red, especialmente en entornos empresariales. Su uso generalizado lo convierte en un objetivo atractivo para actores maliciosos.
* **Enumeración SMB:** Proceso de recopilar información detallada sobre recursos compartidos, usuarios, grupos y otros datos de una red que utiliza el protocolo SMB. Esta técnica puede revelar información sensible sobre la arquitectura de la red, incluyendo nombres de usuarios y permisos de archivos, lo que es útil para trazar un mapa de la infraestructura y planificar ataques.
* **Riesgos de Seguridad asociados:** La enumeración SMB puede llevar a varias vulnerabilidades. Por ejemplo, al descubrir un nombre de usuario válido, un atacante puede intentar un ataque de fuerza bruta. La identificación de recursos compartidos con permisos inadecuados también puede exponer datos confidenciales.
* **NetBIOS (Network Basic Input/Output System):** Una API de software que permite a las aplicaciones en diferentes computadoras comunicarse en una red local. NetBIOS es un objetivo de enumeración porque sus servicios pueden revelar nombres de equipos, usuarios y configuraciones de recursos compartidos, lo que puede ser el primer paso para ataques como el robo de credenciales.
* **NBT (NetBIOS over TCP/IP):** Una implementación de NetBIOS sobre el protocolo TCP/IP, que permite la comunicación de sistemas compatibles con NetBIOS a través de redes. Utiliza puertos clave:
    * **UDP 137:** Para el Servicio de Nombres (NBT Name Service).
    * **UDP 138:** Para el Servicio de Datagramas (NBT Datagram Service).
    * **TCP 139:** Para el Servicio de Sesiones (NBT Session Service).
* **Medidas de Mitigación:** Para protegerse contra la enumeración SMB, es crucial implementar una política de seguridad robusta, mantener los sistemas y aplicaciones actualizadas con los últimos parches de seguridad, y monitorear continuamente la red para identificar actividades sospechosas.

---

## 3. Procedimientos Prácticos

El documento describe el uso de tres herramientas principales para la enumeración de SMB en un entorno controlado (Kali Linux): `nbtscan`, `enum4Linux` y `smbmap`.

### 3.1. Descubrimiento de Hosts con `nbtscan`

`nbtscan` es una herramienta de línea de comandos diseñada para el escaneo rápido a través de NetBIOS. Su propósito es descubrir máquinas en la red a través de su nombre NetBIOS.

* **Comando Básico:** `nbtscan 192.168.1.0/24`.
    * **Propósito:** Este comando escanea el rango de direcciones IP especificado para encontrar máquinas que responden con nombres NetBIOS.
    * **Resultado Esperado:** La herramienta devuelve una tabla que muestra la dirección IP, el nombre NetBIOS, si el host es un servidor y su dirección MAC. Como se muestra en la captura de pantalla del terminal, se pueden identificar las máquinas activas en la red y sus nombres de NetBIOS.

* **Comando con Verbose:** `nbtscan -v 192.168.1.0/24`.
    * **Propósito:** Este comando proporciona información más detallada, como la tabla de nombres de NetBIOS para cada host, incluyendo el servicio asociado y el tipo.
    * **Resultado Esperado:** La salida detalla los nombres del host y el grupo de trabajo, como se aprecia en las capturas de pantalla.

### 3.2. Enumeración con `enum4Linux`

`enum4Linux` es un script de Perl que actúa como un envoltorio para las herramientas del paquete Samba de Linux, simplificando el proceso de enumeración de SMB.

* **Comando Básico:** `enum4linux 192.168.1.113`.
    * **Propósito:** Si no se proporcionan opciones, la herramienta ejecuta una enumeración simple que intenta obtener la información más básica posible, como el grupo de trabajo y los usuarios conocidos. La salida del comando muestra los usuarios conocidos (como `administrator`, `guest`, etc.) y el grupo de trabajo (como `WORKGROUP`).
* **Enumeración con Credenciales:** `enum4linux -u alvaro -p alvaro 192.168.1.113`.
    * **Propósito:** Este comando permite realizar una enumeración utilizando un nombre de usuario y una contraseña conocidos.
    * **Resultado Esperado:** La herramienta confirma que la sesión se puede usar con las credenciales proporcionadas y, si se combina con opciones de enumeración específicas, puede revelar más información.

* **Enumeración de Usuarios:** `enum4linux -u alvaro -p alvaro -U 192.168.1.113`.
    * **Propósito:** La opción `-U` se utiliza para obtener una lista de usuarios en el sistema remoto.
    * **Resultado Esperado:** La herramienta enumera los usuarios que existen en la máquina, como `Administrator`, `alvaro` y `guest`, como se ve en la captura de pantalla.

* **Enumeración Agresiva:** `enum4linux -u alvaro -p alvaro -a 192.168.1.113`.
    * **Propósito:** La opción `-a` ejecuta una enumeración simple completa, incluyendo usuarios, grupos y políticas de contraseñas.
    * **Resultado Esperado:** La salida es mucho más extensa y, como se muestra en la captura, puede incluir información sobre el SO (`Windows 2008R2`), políticas de contraseñas (como la longitud mínima), grupos (como `Administrators` y `Users`), y los miembros de esos grupos.

### 3.3. Interacción con `smbmap`

`smbmap` es una herramienta de enumeración SMB más avanzada que permite interactuar con el sistema de archivos de un host remoto.

* **Ejecución de Comando Remoto:** `smbmap -u vagrant -p vagrant -H 192.168.1.104 -x "ipconfig"`.
    * **Propósito:** La opción `-x` se utiliza para ejecutar un comando en el sistema remoto.
    * **Resultado Esperado:** La herramienta devuelve la salida del comando `ipconfig` ejecutado en la máquina víctima, mostrando la configuración de red como la dirección IPv4.

* **Listar Contenido de Directorio:** `smbmap -u vagrant -p vagrant -H 192.168.1.104 -x 'dir C:\Users\'`.
    * **Propósito:** Permite listar el contenido de un directorio en el sistema remoto.
    * **Resultado Esperado:** El comando muestra el listado del directorio `C:\Users` en la máquina Windows 2008R2, incluyendo subdirectorios y archivos.

* **Subida de Archivos:** `smbmap -u vagrant -p vagrant -H 192.168.1.104 --upload "test.txt" "C:\$\Users\prueba.txt"`.
    * **Propósito:** La opción `--upload` se utiliza para subir un archivo local al sistema remoto.
    * **Resultado Esperado:** La herramienta confirma que el archivo `test.txt` ha sido subido exitosamente al directorio `C:\Users` de la máquina víctima, como se muestra en la captura de pantalla.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad

La **enumeración SMB** es un aspecto fundamental de la seguridad informática que, aunque a menudo se subestima, puede revelar información altamente sensible. Al comprender las implicaciones de la enumeración, se pueden implementar medidas proactivas como políticas de seguridad robustas, actualizaciones regulares y monitorización de la red para proteger la infraestructura y los datos sensibles de la organización.

### 4.2. Puntos de Aprendizaje Clave

* La enumeración SMB es crucial para evaluar la postura de seguridad de una red, ya que ayuda a identificar posibles puntos de entrada.
* Herramientas como `nbtscan`, `enum4Linux` y `smbmap` son esenciales para la fase de reconocimiento, permitiendo descubrir hosts, usuarios, grupos y recursos compartidos.
* `smbmap` es una herramienta particularmente poderosa y flexible, con la capacidad de realizar acciones avanzadas como la ejecución remota de comandos, la enumeración de permisos y la interacción con archivos (subir, descargar, eliminar).
* Estas funcionalidades pueden ser utilizadas tanto por defensores para fortalecer la seguridad de una red, como por posibles atacantes para identificar debilidades.

### 4.3. Relevancia Técnica

Los procedimientos demostrados en este informe son de vital importancia en el campo de la ciberseguridad. La capacidad de utilizar herramientas como `nbtscan` y `smbmap` de manera efectiva para recopilar información crítica y evaluar la postura de seguridad de una red es una habilidad indispensable para cualquier profesional. Estos conocimientos prácticos son aplicables en evaluaciones de seguridad y pruebas de penetración, permitiendo identificar configuraciones inadecuadas y vulnerabilidades que podrían ser explotadas.