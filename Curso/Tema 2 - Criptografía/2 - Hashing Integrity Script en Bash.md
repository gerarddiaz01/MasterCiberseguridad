# Monitoreo de Integridad de Archivos con Bash y Hashing

Este informe detalla cómo construir un script de Bash capaz de monitorear un directorio en busca de cambios en sus archivos, utilizando algoritmos de hashing para verificar su integridad. Esta técnica es fundamental en sistemas de detección de intrusiones basados en el host (HIDS) para identificar anomalías.

## 1\. Concepto de Integridad de Archivos

La integridad de un archivo se refiere a la garantía de que el archivo no ha sido modificado, dañado o alterado de manera no autorizada desde su creación o desde un punto de referencia conocido. Los algoritmos de hashing (como MD5, SHA1, SHA256, SHA512) juegan un papel crucial en esto. Al calcular el hash de un archivo en un momento dado, se obtiene una "huella digital" única. Si el archivo cambia (incluso un pequeño cambio), su hash también cambiará, lo que indica una alteración.

Nuestro script creará un "observador" (watcher) que:

1.  Leerá un directorio.
2.  Calculará el hash de todos los archivos en ese directorio.
3.  Almacenará estos hashes iniciales como referencia.
4.  Periódicamente, recalculará los hashes de los archivos y los comparará con los hashes de referencia.
5.  Si un hash ha cambiado, generará una alerta.

## 2\. Creando el Entorno de Prueba: Un Directorio y Archivos

Antes de escribir el script, necesitamos un directorio con algunos archivos para monitorear.

### Paso 1: Crear un directorio de prueba

Abre tu terminal y crea un nuevo directorio, por ejemplo, `poc_dir`:

```bash
mkdir poc_dir
```

### Paso 2: Crear algunos archivos dentro del directorio

Utiliza `nano` para crear archivos de texto simples dentro de `poc_dir`.

Crea el primer archivo `poc_dir/poc`:

```bash
nano poc_dir/poc
```

Dentro de `nano`, escribe `hiworld!` y guarda (`Ctrl+O`, `Enter`) y sal (`Ctrl+X`).

Crea un segundo archivo `poc_dir/p2`:

```bash
nano poc_dir/p2
```

Dentro de `nano`, escribe `hi!` y guarda (`Ctrl+O`, `Enter`) y sal (`Ctrl+X`).

Ahora, puedes verificar los archivos dentro del directorio:

```bash
ls poc_dir
```

Deberías ver `p2` y `poc` listados.

## 3\. Construyendo el Script de Monitoreo (`watcher.sh`)

Vamos a crear el script paso a paso, explicando cada sección.

### Paso 1: Crear el archivo del script

Abre un nuevo archivo en `nano` para tu script. Lo llamaremos `watcher.sh`.

```bash
nano watcher.sh
```

### Paso 2: El Shebang y Comentarios Iniciales

Agrega las siguientes líneas al principio del archivo:

```bash
#!/bin/bash

### usage: ./watcher.sh <param1=directory>
```

  * `#!/bin/bash`: Esto le dice al sistema que el script debe ejecutarse usando el intérprete Bash.
  * `### usage: ./watcher.sh <param1=directory>`: Este es un comentario que describe cómo se debe usar el script. Es una buena práctica documentar el uso.

### Paso 3: Validación del Número de Argumentos

El script espera un único argumento: la ruta del directorio a monitorear. Vamos a añadir una verificación para asegurar que el usuario lo proporcione correctamente.

```bash
if test "$#" -ne 1
then
    echo "Usage: ./watcher.sh <param1=directory>"
    exit 1
fi
```

  * `if test "$#" -ne 1`: Esta línea inicia una estructura condicional.
      * `test`: Comando para evaluar condiciones.
      * `"$#"`: Es una variable especial en Bash que representa el número total de argumentos pasados al script.
      * `-ne`: Es un operador de comparación que significa "no es igual a".
      * `1`: Estamos verificando si el número de argumentos no es exactamente 1.
  * `then`: Si la condición es verdadera (es decir, el número de argumentos no es 1), se ejecutan los comandos dentro de este bloque.
  * `echo "Usage: ./watcher.sh <param1=directory>"`: Imprime un mensaje de uso correcto si el número de argumentos es incorrecto.
  * `exit 1`: Termina la ejecución del script con un código de error (1 indica un fallo).

### Paso 4: Declaración de Variables y Tabla Hash

Necesitaremos una variable para almacenar la ruta del directorio y una "tabla hash" (en Bash, un array asociativo) para guardar los hashes de referencia.

```bash
directory="$1"
declare -A hashes=() # hashtable for file hashes
```

  * `directory="$1"`: Asigna el primer argumento (`$1`), que es la ruta del directorio a monitorear, a la variable `directory`. Las comillas dobles son importantes si la ruta pudiera contener espacios.
  * `declare -A hashes=()`: Declara un array asociativo llamado `hashes`. En este array, la clave será el nombre del archivo y el valor será su hash MD5. Esencialmente, es como un diccionario.

### Paso 5: Obtener la Lista Inicial de Archivos y sus Hashes

Ahora vamos a recorrer el directorio inicial para calcular y almacenar el hash de cada archivo.

```bash
files=$(ls "$directory")

for file in $files
do
    # Asegúrate de que solo procesas archivos y no directorios dentro del directorio monitoreado
    if [ -f "$directory/$file" ]; then
        hashes["$file"]=$(md5sum "$directory/$file" | cut -f1 -d' ')
    fi
done
```

  * `files=$(ls "$directory")`: Ejecuta el comando `ls` en el directorio especificado y guarda su salida (la lista de archivos y subdirectorios) en la variable `files`.
  * `for file in $files`: Inicia un bucle `for` que iterará sobre cada elemento (nombre de archivo o subdirectorio) en la variable `files`. En cada iteración, el elemento actual se asigna a la variable `file`.
  * `if [ -f "$directory/$file" ]; then ... fi`: Esto es una verificación importante para asegurarnos de que solo estamos intentando calcular hashes de archivos regulares y no de subdirectorios.
      * `-f "$directory/$file"`: Es un operador de prueba que verifica si la ruta combinada (`$directory/$file`) apunta a un archivo regular existente.
  * `hashes["$file"]=$(md5sum "$directory/$file" | cut -f1 -d' ')`: Esta es la línea clave para calcular y almacenar el hash.
      * `hashes["$file"]`: Accede al array asociativo `hashes` usando el nombre del archivo (`$file`) como clave.
      * `$(...)`: Sustitución de comando. El comando dentro de los paréntesis se ejecuta y su salida se asigna a `hashes["$file"]`.
      * `md5sum "$directory/$file"`: Calcula el hash MD5 del archivo completo, especificando su ruta completa.
      * `| cut -f1 -d' '`: Envía la salida de `md5sum` a `cut` para extraer solo el valor del hash (el primer campo, delimitado por un espacio).

### Paso 6: Previsualizar los Hashes Iniciales (Opcional, para depuración)

Puedes añadir un bucle para ver los hashes que se han almacenado inicialmente. Esto es útil para depuración.

```bash
# preview file hashes
echo "Hashes iniciales:"
for i in "${!hashes[@]}"
do
    echo "$i: ${hashes[$i]}"
done
```

  * `for i in "${!hashes[@]}"`: Este bucle itera sobre las *claves* (nombres de archivo) del array asociativo `hashes`.
  * `echo "$i: ${hashes[$i]}"`: Imprime la clave (nombre del archivo) y su valor asociado (el hash).

### Paso 7: Implementar el "Watcher" (Bucle de Monitoreo Continuo)

Esta es la parte que verifica continuamente la integridad.

```bash
# watcher
while true
do
    # Obtener una nueva lista de archivos en caso de que se hayan añadido o eliminado
    current_files=$(ls "$directory")

    for file in $current_files
    do
        if [ -f "$directory/$file" ]; then
            # Calcular el hash actual del archivo
            current_hash=$(md5sum "$directory/$file" | cut -f1 -d' ')

            # Comprobar si el archivo existe en nuestra tabla de hashes iniciales
            if [[ -v hashes["$file"] ]]; then
                # Si el hash actual es diferente al hash almacenado
                if [ "$current_hash" != "${hashes[$file]}" ]; then
                    # Generar alerta
                    echo "ALERTA: ¡El archivo $file ha cambiado!"
                    echo "  Hash antiguo: ${hashes[$file]}"
                    echo "  Hash nuevo: $current_hash"
                fi
            else
                # Alerta si hay un archivo nuevo en el directorio monitoreado
                echo "ALERTA: ¡Nuevo archivo detectado: $file!"
                # Puedes optar por añadirlo a la tabla de hashes o solo alertar
                # hashes["$file"]="$current_hash"
            fi
        fi
    done

    # Dormir por un tiempo antes de la próxima verificación
    echo "Durmiendo por 5 segundos..."
    sleep 5
done
```

  * `while true`: Crea un bucle infinito. El script se ejecutará continuamente hasta que se detenga manualmente (por ejemplo, con `Ctrl+C`).
  * `current_files=$(ls "$directory")`: Dentro del bucle, volvemos a listar los archivos del directorio. Esto es importante para detectar si se han añadido o eliminado archivos.
  * `for file in $current_files`: Otro bucle `for` para procesar cada archivo en el directorio monitoreado en la iteración actual.
  * `if [ -f "$directory/$file" ]; then ... fi`: Verifica si el elemento actual es un archivo regular.
  * `current_hash=$(md5sum "$directory/$file" | cut -f1 -d' ')`: Calcula el hash MD5 del archivo actual.
  * `if [[ -v hashes["$file"] ]]; then`: Esta es una nueva condición.
      * `-v hashes["$file"]`: Verifica si una clave (el nombre del archivo) existe en el array asociativo `hashes`. Esto nos permite diferenciar entre archivos existentes que han cambiado y archivos completamente nuevos.
  * `if [ "$current_hash" != "${hashes[$file]}" ]; then`: Compara el `current_hash` (el hash recién calculado) con el hash almacenado inicialmente para ese archivo (`${hashes[$file]}`).
      * `!=`: Operador de comparación "no es igual a".
      * `echo "ALERTA: ..."`: Si los hashes son diferentes, se imprimen mensajes de alerta en la terminal, mostrando el archivo, el hash antiguo y el nuevo.
  * `else`: Si el archivo no existía en nuestra tabla de hashes iniciales (es decir, es un archivo nuevo).
  * `echo "ALERTA: ¡Nuevo archivo detectado: $file!"`: Alerta sobre la detección de un nuevo archivo.
  * `echo "Durmiendo por 5 segundos..."`: Muestra un mensaje para indicar que el script pausará.
  * `sleep 5`: Pausa la ejecución del script por 5 segundos. Esto evita que el script consuma demasiados recursos del sistema y permite que se detecten cambios de forma periódica. Puedes ajustar este valor (20, 30 segundos, 1 minuto, etc.) según tus necesidades.

### Paso 8: Guardar el Script

Guarda el archivo `watcher.sh` en `nano`: `Ctrl+O`, `Enter`, y luego sal: `Ctrl+X`.

### Paso 9: Dar Permisos de Ejecución

Haz que el script sea ejecutable:

```bash
chmod u+x watcher.sh
```

## 4\. Ejecutando el Script y Probando la Integridad

Ahora que el script está listo, podemos probarlo.

### Paso 1: Ejecutar el script

```bash
./watcher.sh poc_dir
```

El script comenzará a ejecutarse. Primero mostrará los hashes iniciales de los archivos en `poc_dir` y luego entrará en el bucle de monitoreo, mostrando "Durmiendo por 5 segundos..." repetidamente.

**Salida Inicial Esperada:**

```
Hashes iniciales:
p2: 679cbee9a4b608d3535c1c146efda1e8
poc: 656537254dfa6a3f06e49c10ecaa4f36
Durmiendo por 5 segundos...
Durmiendo por 5 segundos...
...
```

### Paso 2: Modificar un Archivo para Disparar una Alerta

Mientras el script está corriendo en una terminal, abre *otra* terminal.

Ve al directorio `poc_dir`:

```bash
cd poc_dir
```

Edita uno de los archivos, por ejemplo, `p2`:

```bash
nano p2
```

Cambia el contenido de `hi!` a `hi!2` o cualquier otra cosa. Guarda (`Ctrl+O`, `Enter`) y sal (`Ctrl+X`).

Vuelve a la terminal donde se está ejecutando `watcher.sh`. Después de unos segundos (cuando termine su ciclo de `sleep`), verás una alerta:

**Salida de Alerta Esperada:**

```
...
Durmiendo por 5 segundos...
ALERTA: ¡El archivo p2 ha cambiado!
  Hash antiguo: 679cbee9a4b608d3535c1c146efda1e8
  Hash nuevo: 77fca7be9fe4dbab8c0ffd04f7ed0b2
Durmiendo por 5 segundos...
ALERTA: ¡El archivo p2 ha cambiado!
  Hash antiguo: 679cbee9a4b608d3535c1c146efda1e8
  Hash nuevo: 77fca7be9fe4dbab8c0ffd04f7ed0b2
Durmiendo por 5 segundos...
...
```

El script continuará alertando porque el hash de `p2` ha cambiado y el hash de referencia (`hashes["p2"]`) no se actualiza, lo cual es el comportamiento deseado para un sistema de monitoreo de integridad: detectar cambios y no "aceptarlos" automáticamente.

### Paso 3: Añadir un Nuevo Archivo

En la segunda terminal, crea un nuevo archivo en `poc_dir`:

```bash
nano poc_dir/new_file
```

Escribe algo como `This is new.` y guarda/sal.

Vuelve a la terminal de `watcher.sh`. En la próxima verificación, el script detectará el nuevo archivo:

**Salida de Alerta por Nuevo Archivo:**

```
...
Durmiendo por 5 segundos...
ALERTA: ¡Nuevo archivo detectado: new_file!
Durmiendo por 5 segundos...
...
```

### Paso 4: Detener el script

Para detener el script, presiona `Ctrl+C` en la terminal donde se está ejecutando `watcher.sh`.

## 5\. Conclusiones

Este script de Bash proporciona un ejemplo práctico y comprensible de cómo implementar un monitoreo básico de integridad de archivos. Al utilizar algoritmos de hashing, podemos detectar de forma efectiva cualquier modificación, adición o eliminación de archivos en un directorio monitoreado.

Aunque este es un ejemplo simplificado, los principios son la base de soluciones de monitoreo de integridad de archivos más complejas utilizadas en la seguridad informática, como los sistemas HIDS. La capacidad de detectar estas anomalías es crucial para identificar posibles intrusiones o actividades maliciosas en un sistema. La flexibilidad de Bash permite adaptar y mejorar este script para incluir funcionalidades adicionales como el registro de eventos (syslog), notificaciones por correo electrónico, o la monitorización de otros atributos de los archivos además del hash.