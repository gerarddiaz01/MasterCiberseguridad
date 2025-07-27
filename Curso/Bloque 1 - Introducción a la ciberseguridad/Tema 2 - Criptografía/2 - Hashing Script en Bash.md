# Generación de Hashes con Bash: Guía Detallada

Esta guía te enseñará a crear y utilizar un script de Bash para generar hashes de diferentes tipos (MD5, SHA1, SHA256, SHA512) a partir de un archivo de palabras. Aprenderás desde la creación básica del script hasta la comprensión de los comandos utilizados y la lógica detrás de ellos.

## 1\. ¿Qué es un Hash?

Un hash es una función matemática que toma una entrada (como un archivo o una cadena de texto) y produce una cadena de caracteres de tamaño fijo, única para esa entrada específica. Es como una "huella digital" del dato. Si incluso un solo bit de la entrada cambia, el hash resultante será completamente diferente. Esto es útil para:

  * **Verificación de integridad:** Asegurarse de que un archivo no ha sido alterado.
  * **Almacenamiento seguro de contraseñas:** Guardar hashes de contraseñas en lugar de las contraseñas reales.
  * **Identificación rápida de datos:** Comparar hashes en lugar de comparar archivos completos.

Los algoritmos de hashing mencionados (MD5, SHA1, SHA256, SHA512) son diferentes tipos de funciones hash, cada una con características de seguridad y longitud de salida distintas.

## 2\. Preparando el Entorno: Creando un Archivo de Palabras

Necesitaremos un archivo de texto que contenga las palabras a las que queremos generarles un hash. Lo crearemos usando `nano`, un editor de texto simple para la terminal.

### Paso 1: Abrir el editor `nano`

Abre tu terminal y escribe el siguiente comando:

```bash
nano words
```

Esto abrirá el editor `nano` y te permitirá crear un nuevo archivo llamado `words`. Si el archivo ya existe, lo abrirá para editarlo.

### Paso 2: Introducir el contenido

Dentro de `nano`, escribe una palabra por línea. Por ejemplo:

```
bird
dog
cat
python
turtles
```

### Paso 3: Guardar y salir de `nano`

  * Para guardar el archivo, presiona `Ctrl + O` (la tecla Control y la letra O al mismo tiempo). `nano` te preguntará el nombre del archivo, que ya debería ser `words`. Presiona `Enter`.
  * Para salir de `nano`, presiona `Ctrl + X`.

¡Felicidades\! Has creado tu primer archivo de palabras.

## 3\. Entendiendo los Comandos de Hashing en Bash

Antes de crear el script, es fundamental entender cómo funcionan los comandos de hashing individuales. Usaremos `md5sum`, `sha1sum`, `sha256sum` y `sha512sum`.

### Concepto clave: `echo` y `pipe` (`|`)

  * `echo`: Este comando simplemente imprime texto en la terminal. Por ejemplo, `echo "Hola mundo"` mostrará "Hola mundo".
  * `pipe` (`|`): El símbolo de pipe toma la salida de un comando y la "pasa" como entrada al siguiente comando. Es muy útil para encadenar operaciones.

### Hashing de una cadena de texto

Vamos a generar el hash de la palabra "hola" usando diferentes algoritmos.

#### Hash MD5

**Comando:**

```bash
echo -n "hola" | md5sum
```

**Explicación:**

  * `echo -n "hola"`: Imprime la palabra "hola" en la terminal. El `-n` es crucial aquí porque evita que `echo` añada un salto de línea al final de la palabra. Si no usas `-n`, el hash se calculará incluyendo ese salto de línea invisible, lo que producirá un hash diferente.
      * **Importante:** La diferencia entre `echo "hola"` y `echo -n "hola"` radica en si se incluye un carácter de salto de línea al final de la cadena. Para obtener el hash correcto de una palabra o frase sin caracteres adicionales, siempre usa `-n`.
  * `| md5sum`: La salida de `echo -n "hola"` (que es solo "hola") se envía como entrada al comando `md5sum`, que calcula el hash MD5.

**Salida esperada:**

```
4d186321c1a7f0f354b297e8914ab240  -
```

Verás el hash seguido de un guion `-` y un espacio. El guion indica que la entrada provino de la entrada estándar (el pipe), no de un archivo.

#### Eliminando el espacio y guion (`cut`)

Para quedarnos solo con el hash, podemos usar el comando `cut`. `cut` extrae secciones de líneas de texto.

**Comando:**

```bash
echo -n "hola" | md5sum | cut -f1 -d' '
```

**Explicación:**

  * `cut -f1`: Le decimos a `cut` que queremos el primer "campo" (`-f1`).
  * `-d' '`: Especificamos que el delimitador entre campos es un espacio (`-d' '`). Como el `md5sum` separa el hash del guion con un espacio, `cut` puede dividir esa línea.

**Salida esperada (solo el hash):**

```
4d186321c1a7f0f354b297e8914ab240
```

Este mismo principio aplica para SHA1, SHA256 y SHA512, solo cambiando el comando `md5sum` por `sha1sum`, `sha256sum`, o `sha512sum` respectivamente.

## 4\. Creando el Script de Hashing en Bash

Ahora vamos a construir el script que automatizará este proceso para cada palabra en nuestro archivo `words`.

### Paso 1: Abrir el editor para el script

Abre un nuevo archivo en `nano` para tu script. Lo llamaremos `hash_words.sh`.

```bash
nano hash_words.sh
```

### Paso 2: Escribir el script

Copia y pega el siguiente contenido en el editor `nano`. Explicaremos cada parte en detalle.

```bash
#!/bin/bash

### usage: ./hash_words.sh <param1=words.txt> <param2=hashes.txt>

# Validar el número de argumentos
if test "$#" -ne 2
then
    echo "Usage: ./hash_words.sh <param1=words.txt> <param2=hashes.txt>"
    exit 1
fi

# Asignar los argumentos a variables para facilitar su uso
input_file="$1"
output_file="$2"

# Vaciar o crear el archivo de salida
> "$output_file"

# Bucle para leer cada línea del archivo de entrada y generar hashes
while IFS= read -r line
do
    # Generar hash MD5
    md5=$(echo -n "$line" | md5sum | cut -f1 -d' ')

    # Generar hash SHA1
    sha1=$(echo -n "$line" | sha1sum | cut -f1 -d' ')

    # Generar hash SHA512 (puedes añadir sha256 también)
    sha512=$(echo -n "$line" | sha512sum | cut -f1 -d' ')

    # Escribir la palabra original y los hashes en el archivo de salida, separados por comas
    echo "$line:$md5,$sha1,$sha512" >> "$output_file"

done < "$input_file"

echo "Proceso completado. Hashes guardados en $output_file"
```

### Paso 3: Guardar y salir

  * Guarda el archivo: `Ctrl + O`, `Enter`.
  * Sale de `nano`: `Ctrl + X`.

### Paso 4: Dar permisos de ejecución al script

Para que puedas ejecutar el script como un programa, necesitas darle permisos de ejecución.

**Comando:**

```bash
chmod u+x hash_words.sh
```

  * `chmod`: Comando para cambiar permisos de archivos.
  * `u+x`: Añade el permiso de ejecución (`x`) al usuario (`u`) propietario del archivo.
  * `hash_words.sh`: El nombre de nuestro script.

## 5\. Explicación Detallada del Script

Vamos a desglosar cada parte del script `hash_words.sh` para que entiendas su funcionamiento.

### `#!/bin/bash`

Esta es la línea conocida como "shebang". Indica al sistema operativo qué intérprete de comandos debe usar para ejecutar el script. En este caso, le decimos que use `bash`.

### `### usage: ./hash_words.sh <param1=words.txt> <param2=hashes.txt>`

Esto es un comentario. Las líneas que empiezan con `#` son ignoradas por Bash y se utilizan para añadir notas y explicaciones al código. Aquí, es una guía para el usuario sobre cómo usar el script.

### `if test "$#" -ne 2`

Esta es la primera parte de una estructura condicional `if...then...fi`.

  * `if`: Inicia la condición.
  * `test "$#" -ne 2`: Aquí se evalúa una condición:
      * `$#`: Es una variable especial en Bash que contiene el número de argumentos (parámetros) que se le pasaron al script.
      * `-ne`: Es un operador de comparación que significa "no es igual a".
      * `2`: Estamos verificando si el número de argumentos es diferente de 2. El script espera dos argumentos: el archivo de entrada y el archivo de salida.
  * `then`: Si la condición es verdadera (es decir, el número de argumentos no es 2), se ejecutan los comandos que siguen a `then`.

### `echo "Usage: ./hash_words.sh <param1=words.txt> <param2=hashes.txt>"`

Si el usuario no proporciona exactamente dos argumentos, este comando imprimirá un mensaje de "Uso" en la terminal, indicando cómo debe ejecutar el script correctamente.

### `exit 1`

  * `exit`: Este comando termina la ejecución del script.
  * `1`: El número `1` es un código de salida que indica que el script terminó con un error. Un código de salida de `0` generalmente indica éxito.

### `input_file="$1"` y `output_file="$2"`

Estas líneas asignan los valores de los argumentos pasados al script a variables con nombres más descriptivos:

  * `$1`: Representa el primer argumento pasado al script (en nuestro caso, el nombre del archivo de palabras, por ejemplo, `words`).
  * `$2`: Representa el segundo argumento (el nombre del archivo donde se guardarán los hashes, por ejemplo, `hashes.txt`).
  * Las comillas dobles (`"`) alrededor de `$1` y `$2` son una buena práctica para manejar nombres de archivo que puedan contener espacios.

### `> "$output_file"`

Este comando vacía el archivo de salida (`hashes.txt` en nuestro ejemplo) si ya existe, o lo crea si no existe. Esto asegura que cada vez que se ejecute el script, el archivo de salida esté limpio antes de añadir nuevos hashes.

### `while IFS= read -r line`

Este es un bucle `while` que lee el archivo de entrada línea por línea.

  * `while`: Inicia el bucle.
  * `IFS=`: `IFS` (Internal Field Separator) es una variable especial en Bash que define qué caracteres se consideran "separadores de campo" al leer líneas. Al establecer `IFS=` (vacío), nos aseguramos de que no se eliminen espacios en blanco al principio o al final de cada línea al leerla.
  * `read -r line`:
      * `read`: Comando que lee una línea de la entrada.
      * `-r`: Evita que `read` interprete las barras invertidas (`\`) como secuencias de escape. Es una buena práctica usarlo cuando se leen archivos.
      * `line`: Es una variable donde se almacenará cada línea leída del archivo de entrada. El bucle se ejecutará para cada línea del archivo de entrada.

### `do ... done < "$input_file"`

  * `do ... done`: Encierra el bloque de comandos que se ejecutarán en cada iteración del bucle `while`.
  * `< "$input_file"`: Esta es una redirección de entrada. Le dice al bucle `while` que su entrada debe venir del archivo especificado por la variable `input_file` (nuestro archivo `words`). Así, `read line` leerá una línea de `words` en cada iteración.

### `md5=$(echo -n "$line" | md5sum | cut -f1 -d' ')`

Esta es la parte central del script, donde se calcula el hash MD5.

  * `md5=`: Estamos declarando una variable llamada `md5` para almacenar el hash resultante.
  * `$(...)`: Esto se llama "sustitución de comando". Lo que está dentro de los paréntesis se ejecuta como un comando separado, y su salida se usa como el valor de la variable `md5`.
  * `echo -n "$line"`: Imprime el contenido de la variable `line` (la palabra actual leída del archivo) sin añadir un salto de línea.
  * `| md5sum`: La salida de `echo` se pasa a `md5sum` para calcular el hash MD5.
  * `| cut -f1 -d' '`: La salida de `md5sum` se pasa a `cut` para extraer solo el hash (el primer campo, delimitado por un espacio).

Las líneas para `sha1` y `sha512` siguen exactamente la misma lógica, solo que utilizan los comandos `sha1sum` y `sha512sum` respectivamente. Puedes añadir una línea similar para `sha256sum` si lo deseas.

### `echo "$line:$md5,$sha1,$sha512" >> "$output_file"`

Esta línea se ejecuta en cada iteración del bucle para escribir la palabra original y sus hashes en el archivo de salida.

  * `echo "$line:$md5,$sha1,$sha512"`: Imprime la palabra original (`$line`), seguida de dos puntos (`:`), y luego los hashes MD5, SHA1 y SHA512, separados por comas.
  * `>> "$output_file"`: Esta es una redirección de salida. El `>>` (doble mayor que) significa "añadir a" o "redireccionar y adjuntar". La salida del `echo` se añade al final del archivo especificado por `output_file` (nuestro archivo `hashes.txt`). Si usáramos solo `>` (un solo mayor que), el archivo se sobrescribiría en cada iteración, y solo veríamos el hash de la última palabra.

### `echo "Proceso completado. Hashes guardados en $output_file"`

Una vez que el bucle `while` ha terminado de procesar todas las líneas del archivo de entrada, este comando final informa al usuario que el script ha terminado y dónde se pueden encontrar los resultados.

## 6\. Ejecutando el Script

Ahora que entiendes el script, es hora de ejecutarlo.

### Paso 1: Ejecutar el script (con argumentos correctos)

**Comando:**

```bash
./hash_words.sh words hashes
```

  * `./hash_words.sh`: Ejecuta el script que acabamos de crear. `./` es necesario porque el script no está en un directorio que esté en la variable de entorno `PATH`.
  * `words`: Este es el `$1` (primer argumento), nuestro archivo de palabras de entrada.
  * `hashes`: Este es el `$2` (segundo argumento), el nombre del archivo donde se guardarán los hashes.

Si todo va bien, no verás ninguna salida en la terminal, ya que el script redirige toda la salida al archivo `hashes`.

### Paso 2: Verificar el archivo de salida

Para ver el contenido del archivo `hashes` (o el nombre que le hayas dado), usa `cat`:

**Comando:**

```bash
cat hashes
```

**Ejemplo de Salida:**

```
bird:abaecf8ca3f98dc13eeecbac263cd3ed,cd92815bf6273acbaf834b9faed277c722068291,1a5bc0ade4e8d25092cae9bb5b387ca7387160e3aefa030880ed8df79000c0018febe9d1f310af5af216d2df6b17f6597e9098fdf0d5dfc24314a68e53dd40f1
dog:06d80eb0c50b49a509b49f2424e8c805,e49512524f47b4138d850c9d9d85972927281da0,3bbed9c106ceaea9e1d1f851b493a52582ae6f6deab8170da43da346a8710622b21d6c2ca14c6336bdc770f161673bef5edad6e65d86b05be62817bc9088d924
cat:d077f244def8a70e5ea758bd8352fcd8,9d989e8d27dc9e0ec3389fc855f142c3d40f0c50,4241b986a49591d445ebb840bc4b49c12b10b392b49222bc45dfd8b871cb3d0e742cdba152aa782e253026c7fc93fe8287b95c5fd0e22467e99c89501a502cd4
python:23eeeb4347bdd26bfc6b7ee9a3b755dd,4235227b51436ad86d07c7cf5d69bda2644984de,ecc579811643b170cbd88fd0d0e323d1e1acc7cef8f73483a70abea01a89afa8015295f617f27447ba05e928e47a0b3a46dc79e72f99d1333856e23eeff97d8b
turtles:35a5687255cbe15a5ac5316aebf5b758,e465b6f3d264569e1d1cedc84635cb003e6e8ead,f7b9e8efd5fac6ad52db80716e582ab839c6f9a31c17bd4c2a5738861e901bb307a9d852b4f2b5cc963499195040cdd8a638780c92f9947deef9ba188a92720d
```

Cada línea del archivo `hashes` contiene la palabra original, seguida de dos puntos, y luego sus hashes MD5, SHA1 y SHA512, separados por comas. Este formato es similar a un CSV (valores separados por comas) y es fácil de procesar en el futuro si necesitas analizar estos datos.

## 7\. Conceptos Adicionales

### Validación de Argumentos más profunda

El script actual solo verifica el *número* de argumentos. En un script más robusto, querrías verificar también si los argumentos son archivos válidos, si existen y si tienes permisos para leerlos o escribirlos. Bash ofrece operadores de prueba (como `-f` para verificar si es un archivo regular, `-e` si existe, `-r` si es legible, `-w` si es escribible) que se usan con el comando `test` o corchetes `[...]`. Esto se puede evaluar a través del comando `test` con los operadores unarios.

### Post-explotación y automatización

Los scripts de Bash son herramientas muy potentes para la automatización de tareas en sistemas Linux. En el contexto de la seguridad informática, son fundamentales para la fase de post-explotación, permitiendo a los atacantes automatizar tareas repetitivas o complejas. Este ejemplo, aunque básico, sienta las bases para tareas más avanzadas como el "cracking de contraseñas", donde se comparan hashes de un diccionario con hashes encontrados para intentar descubrir las contraseñas originales.

Con esta guía, ahora tienes una comprensión sólida de cómo generar hashes utilizando Bash y cómo construir un script para automatizar esta tarea, además de entender los comandos fundamentales involucrados.