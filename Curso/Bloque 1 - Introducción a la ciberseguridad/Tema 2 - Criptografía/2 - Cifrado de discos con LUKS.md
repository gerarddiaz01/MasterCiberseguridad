# Cifrado de Discos en Linux con LUKS: Guía Completa Paso a Paso

Como profesionales de la ciberseguridad, la protección de la información es una de nuestras prioridades fundamentales. En sistemas Linux, LUKS (Linux Unified Key Setup) se ha convertido en el estándar de facto para el cifrado de discos completos, ofreciendo una capa robusta de seguridad a nivel de partición. Esta guía te llevará paso a paso a través del proceso de creación y cifrado de una nueva partición en tu terminal de Linux.

## 1\. Comprendiendo LUKS y su Importancia

LUKS no es solo una herramienta de cifrado; es una especificación que define un formato en el disco para almacenar metadatos de cifrado y múltiples claves, permitiendo una gestión flexible y segura.

**¿Por qué es especial LUKS?**

  * **Seguridad Robusta:** Utiliza algoritmos de cifrado potentes como AES y Serpent, garantizando que tus datos estén protegidos incluso si el dispositivo cae en manos no autorizadas.
  * **Flexibilidad:** Permite crear múltiples contenedores cifrados y gestionar diferentes niveles de acceso con contraseñas individuales, lo que es ideal para proteger distintos conjuntos de datos.
  * **Gestión de Claves:** Una de sus características más destacadas es la capacidad de tener múltiples "slots" (ranuras) para contraseñas. Esto significa que puedes tener varias contraseñas válidas para descifrar la misma partición, y puedes añadir o eliminar contraseñas según sea necesario sin descifrar y volver a cifrar los datos.

En la práctica, LUKS utiliza el comando `cryptsetup` para inicializar y gestionar dispositivos cifrados. Una vez configurado, el dispositivo cifrado se comporta como cualquier otro dispositivo de almacenamiento, pero con una protección adicional.

## 2\. Identificación y Preparación del Disco

Antes de cifrar, es crucial identificar el disco correcto y asegurarse de que no contenga datos importantes, ya que el proceso de formateo **borrará permanentemente toda la información existente en la partición seleccionada**.

### Paso 1: Listar Discos y Particiones

Para identificar el disco que vamos a utilizar, podemos usar el comando `ls /dev/sd*` o `fdisk -l`.

**Comando:**

```bash
ls /dev/sd*
```

**Explicación:**

  * `ls`: Lista el contenido de un directorio.
  * `/dev/sd*`: Este patrón busca dispositivos de bloque que comiencen con `sd` (típicamente discos SATA o SCSI) seguidos de una letra (`a`, `b`, `c`, etc.) y opcionalmente un número para las particiones (ej: `sda1`, `sdb2`).
      * `sda`: Suele ser el disco principal del sistema.
      * `sdb`, `sdc`, etc.: Son otros discos conectados.
  * **Repercusión:** Esta salida nos ayuda a identificar los nombres de nuestros discos, como `sda` (nuestro disco principal con particiones) y `sdb` (un nuevo disco sin particiones en este ejemplo).

**Comando (alternativo y más detallado):**

```bash
sudo fdisk -l
```

**Explicación:**

  * `sudo`: Ejecuta el comando con privilegios de superusuario, lo cual es necesario para interactuar con dispositivos de disco.
  * `fdisk`: Utilidad para manipular tablas de particiones de disco.
  * `-l`: Lista las tablas de particiones de los discos disponibles.
  * **Repercusión:** Esta salida nos dará información más detallada sobre cada disco, incluyendo su tamaño y las particiones existentes. Observaremos que `sdb` no tiene particiones, lo que lo convierte en un candidato ideal para nuestro ejercicio.

### Paso 2: Desmontar el Disco (si estuviera montado)

Antes de crear o modificar particiones, es fundamental que el disco o la partición no estén montados. Puedes verificar esto con `df` y desmontarlo con `umount`.

**Comando (verificar montajes):**

```bash
df -h
```

**Explicación:**

  * `df`: Muestra el espacio en disco usado y disponible.
  * `-h`: Muestra el tamaño en formato legible para humanos (MB, GB).
  * **Repercusión:** Si `sdb` (o el disco que elijas) aparece listado aquí, significa que está montado y debes desmontarlo. En nuestro ejemplo, `sdb` no aparece montado, lo que es ideal.

**Comando (desmontar si es necesario, ejemplo para `sdb1`):**

```bash
sudo umount /dev/sdb1
```

**Explicación:**

  * `sudo umount`: Desmonta un sistema de archivos.
  * `/dev/sdb1`: La ruta de la partición a desmontar.
  * **Repercusión:** Si la partición está en uso, recibirás un error. Asegúrate de que ningún programa esté accediendo a ella.

## 3\. Creando una Partición con `fdisk`

Ahora crearemos una nueva partición en el disco `sdb` usando `fdisk`.

**Comando:**

```bash
sudo fdisk /dev/sdb
```

**Explicación:**

  * `sudo fdisk /dev/sdb`: Inicia la utilidad `fdisk` en modo interactivo para el disco `sdb`.

**Pasos Interactivos dentro de `fdisk`:**

1.  **Presiona `m` y `Enter`:** Esto mostrará el menú de ayuda con las opciones disponibles.
2.  **Presiona `p` y `Enter`:** Imprime la tabla de particiones actual. Verás que no hay ninguna partición definida en `sdb`.
3.  **Presiona `n` y `Enter`:** Crea una nueva partición.
      * **Tipo de partición (p/e):** Te preguntará si quieres una partición `p` (primaria) o `e` (extendida). Para este ejercicio, elige `p` para primaria (opción por defecto). Presiona `Enter`.
      * **Número de partición (1-4):** Presiona `Enter` para aceptar el número de partición por defecto (generalmente `1`).
      * **Primer sector (First sector):** Presiona `Enter` para aceptar el valor por defecto, que es el sector más bajo disponible.
      * **Último sector (Last sector) / Tamaño:** Presiona `Enter` para aceptar el valor por defecto (utilizar todo el espacio restante del disco). Esto creará una única partición que abarque todo el disco.
      * **Repercusión:** Verás un mensaje como "Created a new partition 1 of type Linux and of size 51 MiB" (el tamaño puede variar).
4.  **Presiona `p` y `Enter` (opcional):** Vuelve a imprimir la tabla de particiones para confirmar que `sdb1` ha sido creada.
5.  **Presiona `w` y `Enter`:** **¡MUY IMPORTANTE\!** Este comando escribe los cambios a la tabla de particiones del disco y sale de `fdisk`. Si no lo haces, los cambios no se guardarán.
      * **Repercusión:** Verás mensajes como "The partition table has been altered." y "Syncing disks."

Ahora, si ejecutas `ls /dev/sd*`, deberías ver `/dev/sdb1` listado.

## 4\. Formateando la Partición con un Sistema de Archivos

Antes de cifrar con LUKS, daremos un formato inicial a la partición. Este formato será sobreescrito por LUKS, pero es un paso intermedio en la práctica.

### Paso 1: Aplicar formato `ext4`

**Comando:**

```bash
sudo mkfs.ext4 /dev/sdb1
```

**Explicación:**

  * `sudo mkfs.ext4`: Comando para crear un sistema de archivos `ext4` (un tipo común de sistema de archivos en Linux).
  * `/dev/sdb1`: La partición a la que se le aplicará el formato.
  * **Repercusión:** Verás mensajes indicando la creación del sistema de archivos, la asignación de tablas de grupo, etc. Es posible que tu entorno gráfico reconozca automáticamente el nuevo volumen y lo "monte" para ti temporalmente, mostrando una ventana emergente.

### Paso 2: Desmontar la Partición de Nuevo

Es crucial que la partición esté desmontada antes de aplicar el formato LUKS. Si el sistema la montó automáticamente, debes desmontarla.

**Comando:**

```bash
sudo umount /dev/sdb1
```

**Explicación:**

  * `sudo umount /dev/sdb1`: Desmonta la partición `/dev/sdb1`.
  * **Repercusión:** Si el `df -h` ya no muestra `sdb1` montada, el desmontaje fue exitoso.

## 5\. Cifrando la Partición con LUKS (cryptsetup luksFormat)

Este es el paso donde realmente aplicamos el cifrado LUKS a la partición.

**Comando:**

```bash
sudo cryptsetup luksFormat /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup`: El comando principal para gestionar dispositivos cifrados con LUKS.
  * `luksFormat`: Subcomando de `cryptsetup` que inicializa los metadatos de LUKS en el dispositivo, borrando cualquier formato existente y preparándolo para el cifrado.
  * `/dev/sdb1`: La partición a la que se aplicará el formato LUKS.
  * **Repercusión:**
      * **Advertencia de Sobreescritura:** Recibirás una advertencia de que este comando sobrescribirá permanentemente todos los datos existentes en `/dev/sdb1`. ¡Asegúrate de que estás en el disco correcto\!
      * **Confirmación:** Deberás escribir `YES` (en mayúsculas) y presionar `Enter` para confirmar.
      * **Contraseña:** Se te pedirá que introduzcas y verifiques una nueva contraseña (passphrase) para la partición LUKS. Esta es la contraseña principal que se utilizará para abrir el volumen cifrado. **No la olvides.** Mientras escribes, no verás caracteres.
      * El proceso puede tardar un poco dependiendo del tamaño del disco.
  * **Resultado:** Después de este paso, tu disco `sdb1` estará cifrado con LUKS, pero aún no estará accesible para almacenar archivos.

## 6\. Abriendo y Accediendo a la Partición Cifrada (cryptsetup open)

Para poder usar la partición LUKS, primero debemos "abrirla" usando su contraseña. Esto creará un dispositivo de mapeo en `/dev/mapper/`.

**Comando:**

```bash
sudo cryptsetup open /dev/sdb1 unidad_cifrada
```

**Explicación:**

  * `sudo cryptsetup open`: Abre un dispositivo LUKS.
  * `/dev/sdb1`: El dispositivo físico cifrado que queremos abrir.
  * `unidad_cifrada`: Este es un nombre que tú eliges. Será el "nombre de mapeo" para el dispositivo descifrado. Un nuevo dispositivo aparecerá en `/dev/mapper/` con este nombre (ej: `/dev/mapper/unidad_cifrada`).
  * **Repercusión:**
      * **Solicitud de Contraseña:** Se te pedirá la contraseña (passphrase) que definiste durante `luksFormat`.
      * **Dispositivo de Mapeo:** Una vez que la contraseña es correcta, se creará el dispositivo de mapeo. Puedes verificar su existencia con `ls /dev/mapper/`. Deberías ver `unidad_cifrada`.
      * **¡Importante\!** Abrir el dispositivo con `cryptsetup open` **no monta la unidad**. Solo la descifra y la hace accesible como un nuevo dispositivo de bloque en `/dev/mapper/`.

## 7\. Formateando la Partición Descifrada y Montándola

El dispositivo en `/dev/mapper/unidad_cifrada` está ahora descifrado, pero aún no tiene un sistema de archivos utilizable (como `ext4`). Debemos formatearlo nuevamente y luego montarlo.

### Paso 1: Formatear el Dispositivo de Mapeo

**Comando:**

```bash
sudo mkfs.ext4 /dev/mapper/unidad_cifrada
```

**Explicación:**

  * `sudo mkfs.ext4`: Formatea el dispositivo especificado con el sistema de archivos `ext4`.
  * `/dev/mapper/unidad_cifrada`: El dispositivo descifrado (la capa superior de LUKS) al que se le aplicará el sistema de archivos.
  * **Repercusión:** Este paso creará un sistema de archivos utilizable dentro del contenedor LUKS.

### Paso 2: Montar la Partición Descifrada

Ahora que el dispositivo de mapeo tiene un sistema de archivos, puedes montarlo en un punto de montaje para acceder a él.

**Comando:**

```bash
sudo mount /dev/mapper/unidad_cifrada /mnt/prueba
```

**Explicación:**

  * `sudo mount`: Comando para montar un sistema de archivos.
  * `/dev/mapper/unidad_cifrada`: El dispositivo de bloque descifrado.
  * `/mnt/prueba`: El punto de montaje donde quieres que el contenido del disco sea accesible. Asegúrate de que este directorio exista (puedes crearlo con `sudo mkdir /mnt/prueba` si no lo tienes).
  * **Repercusión:** Ahora, si ejecutas `df -h`, deberías ver `/dev/mapper/unidad_cifrada` montado en `/mnt/prueba`. ¡Ya puedes almacenar archivos en tu partición cifrada\!

## 8\. Gestión de Claves LUKS Adicionales

Una de las grandes ventajas de LUKS es su capacidad para gestionar múltiples claves.

### a) Añadir una Nueva Contraseña (`luksAddKey`)

Puedes añadir una contraseña adicional para descifrar la misma partición.

**Comando:**

```bash
sudo cryptsetup luksAddKey /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup luksAddKey`: Añade una nueva clave al volumen LUKS.
  * `/dev/sdb1`: La partición LUKS a la que se le añadirá la clave.
  * **Repercusión:**
      * **Contraseña Existente:** Te pedirá que ingreses una contraseña *existente* para la partición LUKS.
      * **Nueva Contraseña:** Luego, te pedirá que introduzcas y verifiques la *nueva* contraseña que deseas añadir.
      * Ahora, ambas contraseñas serán válidas para abrir la partición.

### b) Ver Información de los Slots de Claves (`luksDump`)

Para ver qué slots de claves están en uso y otra información sobre el cabecero LUKS.

**Comando:**

```bash
sudo cryptsetup luksDump /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup luksDump`: Muestra los metadatos y la configuración del cabecero LUKS del dispositivo.
  * `/dev/sdb1`: La partición LUKS.
  * **Repercusión:** Verás información detallada, incluyendo los "Keyslots" (ranuras de claves). Observarás que si añadiste una clave, ahora aparecerán dos slots utilizados (por ejemplo, Keyslot 0 y Keyslot 1).

### c) Cambiar una Contraseña Existente (`luksChangeKey`)

Si deseas modificar una de las contraseñas existentes.

**Comando:**

```bash
sudo cryptsetup luksChangeKey /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup luksChangeKey`: Cambia una contraseña existente en el volumen LUKS.
  * `/dev/sdb1`: La partición LUKS.
  * **Repercusión:**
      * **Contraseña a Cambiar:** Te pedirá la contraseña que deseas cambiar.
      * **Nueva Contraseña:** Luego, te pedirá la nueva contraseña y que la verifiques.

### d) Eliminar una Contraseña (`luksRemoveKey`)

Puedes eliminar una contraseña específica de la partición LUKS.

**Comando:**

```bash
sudo cryptsetup luksRemoveKey /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup luksRemoveKey`: Elimina una clave del volumen LUKS.
  * `/dev/sdb1`: La partición LUKS.
  * **Repercusión:** Te pedirá la contraseña (passphrase) que deseas eliminar. Una vez eliminada, esa contraseña ya no podrá usarse para abrir la partición. Si haces un `luksDump`, verás que el slot de esa clave ahora está vacío.

### e) Obtener el UUID de la Partición LUKS (`luksUUID`)

El UUID (Universally Unique Identifier) de la partición LUKS es un identificador único que puede ser útil para la configuración de montaje automático al inicio del sistema.

**Comando:**

```bash
sudo cryptsetup luksUUID /dev/sdb1
```

**Explicación:**

  * `sudo cryptsetup luksUUID`: Muestra el UUID de la partición LUKS.
  * `/dev/sdb1`: La partición LUKS.
  * **Repercusión:** Se mostrará una cadena de caracteres única que identifica tu volumen LUKS (ejemplo: `0a364741-deaf-4092-8dc-59922458041`).

## 9\. Cerrando la Partición Cifrada (`cryptsetup close`)

Cuando termines de usar la partición cifrada, es crucial cerrarla para proteger tus datos. Esto deshabilitará el dispositivo de mapeo y hará que la partición sea inaccesible hasta que se vuelva a abrir con la contraseña.

**Comando:**

```bash
sudo cryptsetup close unidad_cifrada
```

**Explicación:**

  * `sudo cryptsetup close`: Cierra un dispositivo de mapeo LUKS.
  * `unidad_cifrada`: El nombre de mapeo del dispositivo que creaste con `cryptsetup open`.
  * **Repercusión:**
      * Si la unidad está montada, el comando dará un error. Debes desmontarla primero con `sudo umount /mnt/prueba`.
      * Una vez cerrada, el dispositivo `/dev/mapper/unidad_cifrada` desaparecerá. Tus datos volverán a estar completamente cifrados y seguros.

## 10\. Consideraciones de Seguridad Finales

  * **Contraseñas Robustas:** La seguridad de tu cifrado LUKS depende directamente de la fortaleza de tu contraseña. Utiliza contraseñas largas, complejas y únicas.
  * **Copia de Seguridad de las Claves:** Aunque LUKS permite múltiples contraseñas, es vital tener una estrategia de copia de seguridad para tus claves de acceso, especialmente si pierdes tu contraseña principal.
  * **Automatización del Cifrado al Arranque:** Para uso en un sistema operativo, es común configurar LUKS para que las particiones se descifren automáticamente al inicio (con una contraseña) o que se soliciten las contraseñas necesarias. Esto implica modificar archivos del sistema como `/etc/crypttab` y `/etc/fstab`, lo cual es un tema más avanzado.

LUKS es una solución poderosa y versátil para proteger datos sensibles en sistemas Linux, brindando tranquilidad en entornos tanto empresariales como personales.