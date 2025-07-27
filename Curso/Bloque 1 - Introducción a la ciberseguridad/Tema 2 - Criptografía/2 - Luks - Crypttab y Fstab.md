# Configuración Avanzada de Cifrado con LUKS: Montaje Automático al Inicio

Como expertos en ciberseguridad, sabemos que cifrar un disco es solo el primer paso. Para que los datos cifrados sean accesibles de forma eficiente y segura al inicio del sistema, debemos integrar la configuración de LUKS con los mecanismos de arranque de Linux. Este ejercicio práctico se centrará en cómo utilizar los archivos `crypttab` y `fstab` para lograr el descifrado y montaje automático de una partición LUKS.

## Objetivo del Ejercicio

El objetivo principal de este ejercicio es configurar una partición cifrada con LUKS para que se descifre automáticamente al arrancar el sistema y se monte en un punto específico. Esto nos permitirá tener nuestros datos protegidos, pero accesibles sin intervención manual (más allá de la contraseña inicial si no se usa un archivo de clave).

Para lograrlo, trabajaremos con dos archivos de configuración clave en sistemas Linux:

1.  **`/etc/crypttab`**: Este archivo se encarga de definir los dispositivos cifrados que deben ser preparados durante el arranque del sistema.
2.  **`/etc/fstab`**: Este archivo es responsable de especificar los sistemas de archivos que deben montarse automáticamente al iniciar o reiniciar el sistema.

Vamos a desglosar el proceso paso a paso.

## 1\. Pre-requisitos: Partición LUKS ya Creada y Cerrada

Para este ejercicio, asumimos que ya tienes una partición cifrada con LUKS (por ejemplo, `/dev/sdb1`). Es crucial que esta partición esté **cerrada** y **desmontada** antes de empezar a modificar `crypttab` y `fstab`.

Puedes verificar si está cerrada con `ls /dev/mapper/` (no debería aparecer el nombre de mapeo, como `unidad_cifrada`). Si no lo está, ciérrala con:

```bash
sudo cryptsetup close <nombre_mapeo_anterior>
```

Y asegúrate de que no esté montada con `df -h`. Si lo está, desmonta:

```bash
sudo umount /dev/mapper/<nombre_mapeo_anterior>
```

## 2\. Configurando `/etc/crypttab`

El archivo `/etc/crypttab` (ubicado en `/etc/crypttab`) describe los dispositivos de bloque cifrados que se configurarán durante el arranque del sistema.

Cada línea en `crypttab` describe un dispositivo cifrado y sigue un formato específico con cuatro campos, de los cuales los dos primeros son obligatorios y los dos últimos opcionales: `nombre_volumen dispositivo_cifrado clave_cifrado opciones_cifrado`.

### Estructura de una línea en `/etc/crypttab`

1.  **`nombre_volumen` (Obligatorio):**

      * Este es el nombre que se asignará al volumen descifrado en `/dev/mapper/`. Por ejemplo, si usas `mis_datos`, el dispositivo descifrado será `/dev/mapper/mis_datos`.
      * Debe ser un nombre descriptivo y sin espacios.

2.  **`dispositivo_cifrado` (Obligatorio):**

      * La ruta al dispositivo de bloque real que contiene el cifrado LUKS (por ejemplo, `/dev/sdb1`).
      * **Recomendación:** Es muy recomendable usar el **UUID** (Universally Unique Identifier) del dispositivo LUKS en lugar de su nombre (`/dev/sdb1`). Esto evita problemas si el orden de los discos cambia en el sistema (por ejemplo, si `/dev/sdb1` se convierte en `/dev/sdc1` después de añadir o quitar hardware).
          * Para obtener el UUID de tu partición LUKS (`/dev/sdb1`), usa el comando:
            ```bash
            sudo cryptsetup luksUUID /dev/sdb1
            ```
            *Sintaxis:* `cryptsetup luksUUID <dispositivo>`
            *Explicación:* Este comando consulta el encabezado LUKS del dispositivo y devuelve su UUID único.
            *Repercusión:* Verás una cadena larga como `0a364741-deaf-4092-8dc-59922458041`. Usarás `UUID=<tu_uuid>` en el campo.

3.  **`clave_cifrado` (Opcional):**

      * Especifica la ruta a un archivo que contiene la contraseña de cifrado.
      * Si este campo no se especifica (se deja vacío o con `-`), el usuario será consultado interactivamente para teclear la contraseña al arrancar el sistema.
      * Para este ejercicio, si quieres que se pida la contraseña en el arranque, déjalo vacío (`-`). Si prefieres un archivo de clave (más avanzado y con implicaciones de seguridad si el archivo no está bien protegido), podrías poner su ruta aquí.

4.  **`opciones_cifrado` (Opcional):**

      * Una lista de opciones separadas por comas.
      * Para LUKS, la opción principal es `luks` para forzar que el dispositivo se trate como un volumen LUKS.
      * Otras opciones útiles pueden ser `discard` (para SSDs, mejora el rendimiento pero tiene implicaciones de seguridad), o `nofail` (si no quieres que el sistema falle al arrancar si el dispositivo no se puede abrir).

### Paso 1: Editar `/etc/crypttab`

Abre el archivo `/etc/crypttab` con un editor de texto con privilegios de superusuario:

```bash
sudo nano /etc/crypttab
```

### Paso 2: Añadir la Entrada para tu Partición LUKS

Añade una nueva línea al final del archivo con la siguiente estructura (reemplaza `<tu_uuid>` con el UUID real de tu partición LUKS):

```
# <nombre_volumen_mapeado> <UUID_o_ruta_dispositivo> <clave_cifrado> <opciones>
mis_datos    UUID=<tu_uuid>    -    luks
```

**Ejemplo Práctico:**
Si tu UUID es `0a364741-deaf-4092-8dc-59922458041`, la línea sería:

```
mis_datos    UUID=0a364741-deaf-4092-8dc-59922458041    -    luks
```

Guarda los cambios (`Ctrl+O`, `Enter`) y sal de `nano` (`Ctrl+X`).

## 3\. Configurando `/etc/fstab`

Una vez que `crypttab` prepara el dispositivo cifrado (es decir, lo descifra y lo hace disponible como `/dev/mapper/nombre_volumen`), necesitamos decirle al sistema que lo monte en un punto específico. Esto se hace a través de `/etc/fstab` (ubicado en `/etc/fstab`).

El archivo `fstab` contiene información descriptiva sobre los sistemas de archivos que el sistema puede montar. Cada sistema de archivos se describe en una línea separada, con campos delimitados por espacios o tabulaciones.

### Estructura de una línea en `/etc/fstab`

Una línea en `/etc/fstab` tiene seis campos: `dispositivo_a_montar punto_montaje tipo_sistema_archivos opciones_montaje dump passno`.

1.  **`dispositivo_a_montar`:**

      * Aquí especificaremos el dispositivo descifrado por LUKS, que aparecerá como `/dev/mapper/<nombre_volumen_de_crypttab>`.
      * **Recomendación:** Aunque podríamos usar el UUID de la partición LUKS aquí también, para `fstab` es el UUID del **sistema de archivos** *dentro* del volumen LUKS lo más recomendado, o el nombre de mapeo si es más simple para este ejercicio.
          * Para obtener el UUID del sistema de archivos (ext4, etc.) de tu volumen descifrado (`/dev/mapper/mis_datos`), primero asegúrate de que el volumen esté abierto (usando `sudo cryptsetup open /dev/sdb1 mis_datos` si lo cerraste) y luego usa:
            ```bash
            sudo blkid /dev/mapper/mis_datos
            ```
            *Sintaxis:* `blkid <dispositivo>`
            *Explicación:* Este comando muestra los atributos de los dispositivos de bloque, incluyendo el UUID del sistema de archivos.
            *Repercusión:* Verás una salida como `UUID="<tu_uuid_fs>" TYPE="ext4"`. Usaremos `UUID=<tu_uuid_fs>`.

2.  **`punto_montaje`:**

      * La ruta absoluta del directorio donde se montará la partición (por ejemplo, `/mnt/mis_datos`).
      * Asegúrate de que este directorio exista. Si no existe, créalo antes de reiniciar:
        ```bash
        sudo mkdir /mnt/mis_datos
        ```

3.  **`tipo_sistema_archivos`:**

      * El tipo de sistema de archivos de la partición (por ejemplo, `ext4`). Este es el formato que le diste al dispositivo de mapeo con `mkfs.ext4`.

4.  **`opciones_montaje`:**

      * Opciones de montaje separadas por comas.
      * `defaults`: Es la opción más común y suele incluir `rw` (lectura/escritura), `suid`, `dev`, `exec`, `auto`, `nouser`, `async`.
      * `_netdev`: Si el dispositivo está en red, asegura que la red esté disponible antes de intentar el montaje. No aplica para este caso.
      * `noauto`: Evita el montaje automático al arranque. **No usar esta opción** si quieres montaje automático.

5.  **`dump` (Copia de seguridad):**

      * Utilizado por el comando `dump` para determinar qué sistemas de archivos necesitan ser respaldados.
      * `0`: No hacer copia de seguridad (valor más común para particiones no críticas o que se gestionan de otra forma).

6.  **`passno` (Verificación `fsck`):**

      * Utilizado por `fsck` (utilidad de comprobación de la consistencia del sistema de archivos) para determinar el orden de las comprobaciones al arrancar.
      * `0`: No comprobar el sistema de archivos (común para particiones que no son del sistema).
      * `1`: La partición raíz (`/`) debe tener este valor.
      * `2`: Otras particiones (que no sean la raíz) pueden tener este valor para ser comprobadas después.

### Paso 1: Abrir el Volumen LUKS y Obtener el UUID del Sistema de Archivos

Asegúrate de que tu volumen LUKS está abierto. Si lo has cerrado, ábrelo de nuevo (reemplaza `unidad_cifrada` por el nombre que elegiste en `crypttab`):

```bash
sudo cryptsetup open /dev/sdb1 unidad_cifrada
```

Luego, obtén el UUID del sistema de archivos dentro de esa partición descifrada:

```bash
sudo blkid /dev/mapper/unidad_cifrada
```

Anota el `UUID="..."` que te devuelva.

### Paso 2: Crear el Punto de Montaje

Si no existe, crea el directorio donde se montará la partición cifrada. Por ejemplo:

```bash
sudo mkdir /mnt/mis_datos
```

### Paso 3: Editar `/etc/fstab`

Abre el archivo `/etc/fstab` con un editor de texto con privilegios de superusuario:

```bash
sudo nano /etc/fstab
```

### Paso 4: Añadir la Entrada para tu Partición Cifrada

Añade una nueva línea al final del archivo con la siguiente estructura (reemplaza `<UUID_del_fs>` con el UUID que obtuviste con `blkid` y `mis_datos` con el nombre de mapeo que elegiste en `crypttab`):

```
# <UUID_o_ruta_mapeo> <punto_montaje> <tipo_fs> <opciones> <dump> <passno>
UUID=<UUID_del_fs>    /mnt/mis_datos    ext4    defaults    0    2
```

**Ejemplo Práctico:**
Si tu UUID del sistema de archivos es `1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d` y tu nombre de mapeo es `mis_datos`, la línea sería:

```
UUID=1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d    /mnt/mis_datos    ext4    defaults    0    2
```

Guarda los cambios (`Ctrl+O`, `Enter`) y sal de `nano` (`Ctrl+X`).

## 4\. Probar la Configuración

Antes de reiniciar, es crucial realizar algunas pruebas para asegurarte de que la configuración es correcta.

### Paso 1: Desmontar el volumen (si está montado)

Si tu volumen `unidad_cifrada` está montado en `/mnt/mis_datos`, desmontalo:

```bash
sudo umount /mnt/mis_datos
```

### Paso 2: Cerrar el volumen LUKS

```bash
sudo cryptsetup close unidad_cifrada
```

### Paso 3: Intentar Montar con `mount -a`

Este comando intentará montar todos los sistemas de archivos listados en `fstab` que no estén ya montados. Al hacerlo, también activará las entradas de `crypttab`.

**Comando:**

```bash
sudo mount -a
```

**Explicación:**

  * `sudo mount -a`: Intenta montar todos los sistemas de archivos definidos en `/etc/fstab`.
  * **Repercusión:** Si todo está configurado correctamente en `crypttab` y `fstab`, se te pedirá la contraseña para tu volumen LUKS. Si la introduces correctamente, el volumen se descifrará y se montará en `/mnt/mis_datos` (o el punto de montaje que hayas elegido). Si hay errores en `crypttab` o `fstab`, el comando mostrará mensajes de error.

  NOTA: puede haber un error aqui, pero al hacer `sudo reboot` maybe funciona, try it out. Si con `sudo reboout` y `sudo mount -a` no funciona revisa el uuid de `/etc/crypttab`.

  Si se modifica /etc/fstab hay que hacer reload a la última versión con `sudo systemctl daemon-reload`

### Paso 4: Verificar el Montaje

```bash
df -h
```

Deberías ver `/dev/mapper/mis_datos` (o tu nombre de mapeo) montado en `/mnt/mis_datos` (o tu punto de montaje).

### Paso 5: Reiniciar el Sistema (Prueba Final)

Si los pasos anteriores funcionaron sin problemas, el paso final es reiniciar el sistema para verificar que el descifrado y montaje automático se producen al inicio.

**Comando:**

```bash
sudo reboot
```

**Repercusión:**

  * Durante el arranque, en algún punto, se te solicitará la contraseña para el volumen LUKS. Si la introduces correctamente, el sistema continuará el arranque y la partición se montará automáticamente.
  * Una vez que el sistema se inicie por completo, puedes verificar el montaje con `df -h` para confirmar que tu volumen cifrado está disponible.

## 5\. Notas Importantes y Consideraciones de Seguridad

  * **Contraseñas:** Si utilizas el método de introducir la contraseña interactivamente al arranque, asegúrate de que sea una contraseña fuerte.
  * **Archivos de Clave:** Si decides usar un archivo de clave (en el tercer campo de `crypttab`), este archivo debe estar extremadamente bien protegido (permisos restrictivos, idealmente en una unidad externa o partición no cifrada mínima). La seguridad de tu cifrado dependerá de la seguridad de ese archivo de clave.
  * **Errores en `fstab` o `crypttab`:** Un error en estos archivos puede impedir que tu sistema arranque. Siempre haz copias de seguridad de estos archivos antes de modificarlos:
    ```bash
    sudo cp /etc/crypttab /etc/crypttab.bak
    sudo cp /etc/fstab /etc/fstab.bak
    ```
    Si el sistema no arranca, a menudo puedes iniciar en modo de recuperación o desde un Live CD/USB para corregir los archivos.
  * **`fsck` y `dump`:** Los valores `0` o `2` en `passno` y `0` en `dump` son comunes para particiones de datos. Asegúrate de entender su propósito antes de modificarlos para la partición raíz o sistemas críticos.

Al completar este ejercicio, habrás dominado la configuración del descifrado y montaje automático de particiones LUKS, una habilidad esencial para la gestión segura de datos en entornos Linux.