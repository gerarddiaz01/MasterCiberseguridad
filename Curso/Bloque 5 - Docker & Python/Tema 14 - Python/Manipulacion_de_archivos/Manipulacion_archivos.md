# Manipulación de Archivos en Python (Avanzado)

## Introducción

Trabajar con archivos permite almacenar y recuperar datos para que los programas sean más útiles. Por ejemplo, podemos guardar preferencias de usuario, analizar grandes cantidades de datos desde archivos externos, mantener registros de errores o pausar y reanudar la ejecución de un script en otro momento. A continuación, se explica detalladamente cómo leer y escribir archivos en Python, los diferentes modos de apertura, métodos para leer línea por línea, el manejo de archivos JSON y cómo leer/escribir datos numéricos con NumPy. Se incluyen ejemplos de código, buenas prácticas y advertencias comunes para reforzar el aprendizaje.

## Lectura y escritura de archivos con `open()`

En Python la forma básica de trabajar con archivos es usando la función incorporada `open()`, que devuelve un objeto de archivo (file object). Este objeto nos permite leer o escribir en el archivo según corresponda. Los pasos típicos son:

1. Abrir el archivo con `open()`, indicando el nombre o ruta del archivo y el modo (lectura, escritura, etc.).
2. Operar con el archivo: leer su contenido o escribir datos en él mediante métodos del objeto archivo.
3. Cerrar el archivo cuando ya no se necesite, para liberar el recurso.

Por ejemplo, abrir un archivo de texto llamado `datos.txt` para leer su contenido:

```python
f = open('datos.txt', 'r')  # Abrir archivo en modo lectura
contenido = f.read()        # Leer todo el contenido del archivo
print(contenido)            # Usar el contenido (por ejemplo, imprimirlo)
f.close()                   # Cerrar el archivo
```

Es muy importante cerrar el archivo después de usarlo, pues garantiza que el sistema escriba cualquier cambio pendiente en disco y libera el archivo para que otros programas puedan usarlo. En el ejemplo anterior usamos `f.close()` al final.

**Consejo:** En Python se recomienda usar la sintaxis `with open(...) as f:` para gestionar archivos. Esta construye un contexto donde el archivo se abre al entrar y se cierra automáticamente al salir, incluso si ocurre alguna excepción. Reescribiendo el ejemplo con esta forma más segura:

```python
with open('datos.txt', 'r') as f:
    contenido = f.read()
    # ... (aquí se puede procesar el contenido) ...
# Al salir del bloque with, el archivo se cierra automáticamente
```

Usando `with`, evitamos tener que llamar a `close()` manualmente y nos aseguramos de no olvidar cerrar el archivo.

## Rutas de archivo (paths) relativas y absolutas

Al abrir archivos, podemos especificar la ruta (path) al archivo. Si el archivo está en el directorio actual del programa, basta con el nombre del archivo o una ruta relativa. Una ruta relativa indica la ubicación respecto al directorio actual. Por ejemplo:

- Ruta relativa en Linux/Mac: `carpeta/archivo.txt` abre el archivo `archivo.txt` dentro de la subcarpeta `carpeta` del directorio actual.
- Ruta relativa en Windows: `carpeta\archivo.txt` (usando `\` para separar directorios) hace lo mismo en entornos Windows.

Si el archivo está en otra ubicación, se usa una ruta absoluta, que comienza desde la raíz del sistema de archivos. Por ejemplo:

- Ruta absoluta en Linux/Mac: `/home/usuario/documentos/datos.txt`
- Ruta absoluta en Windows: `C:\Users\Usuario\Documentos\datos.txt`

**Nota:** En Python, para rutas de Windows con backslash `\` conviene usar doble backslash `\\` (porque `\` es un carácter de escape en strings) o prefijar el string con `r` para hacer una raw string (cadena cruda) que ignore escapes, por ejemplo `r"C:\Users\Usuario\Documents\datos.txt"`. Alternativamente, puedes usar barras normales `/` en rutas Windows, ya que Python las interpreta correctamente en la mayoría de los casos. Para manejar rutas de forma portátil entre sistemas operativos, la librería estándar ofrece utilidades como `os.path` o `pathlib`, pero eso queda fuera de este alcance.

⚠ **Precaución:** Al abrir un archivo en modo lectura, es necesario que el archivo exista en la ruta especificada. Si no existe, Python lanzará un error (`FileNotFoundError`). En secciones siguientes veremos cómo ciertos modos de apertura pueden crear el archivo si no existe.

## Escritura de datos en un archivo

La función `open()` también permite escribir en archivos. Para ello debemos abrir el archivo en un modo de escritura (por ejemplo `'w'` para escritura normal o `'a'` para agregar contenido; los modos se explican en la siguiente sección). Luego podemos usar métodos como `write()` para enviar texto al archivo. Por ejemplo, para crear un archivo nuevo y escribirle algunas líneas de texto:

```python
with open('salida.txt', 'w') as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")
```

En este código se abre (o crea) `salida.txt` en modo escritura, se escriben dos líneas de texto, y al terminar el bloque `with` el archivo se cierra automáticamente guardando los cambios. Observa que incluimos manualmente `\n` al final de cada línea para insertar saltos de línea, ya que `write()` no agrega saltos por sí mismo. Si quisiéramos agregar más contenido al mismo archivo sin sobrescribir lo anterior, usaríamos el modo `'a'` (append, ver detalles más adelante) en lugar de `'w'`.

⚠ **Precaución:** Cuando abrimos un archivo en modo escritura `'w'`, se borrará cualquier contenido previo que tuviera el archivo, empezando de cero. Si se quiere conservar el contenido existente y añadir al final, se debe usar `'a'` (anexar) en lugar de `'w'`. Más adelante detallamos las diferencias de modos.

## Modos de apertura de archivos (`r`, `w`, `a`, `x`, `r+`, `w+`, etc.)

La función `open()` acepta un segundo argumento opcional indicando el modo de apertura. Este modo es un string (cadena) con una o dos letras, donde la primera indica la operación principal (lectura, escritura, etc.) y la segunda (opcional) indica si es texto o binario, u otros modificadores. Los modos más comunes son:

- `r` – Lectura (read). Abre el archivo solo para leer. El archivo debe existir. Es el modo predeterminado de `open()` (si no especificas modo, asume `'r'` y texto).
- `w` – Escritura (write). Abre el archivo solo para escribir. Sobrescribe el archivo si ya existe, truncándolo (dejándolo vacío antes de escribir), y si no existe, lo crea nuevo.
- `a` – Añadir (append). Abre el archivo para escritura añadiendo al final. Los datos nuevos se escribirán al final del contenido existente (sin borrar lo previo). Si el archivo no existe, se crea.
- `x` – Creación exclusiva. Abre el archivo para escribir solo si no existe. Si el archivo ya existe, falla lanzando `FileExistsError`. Esto sirve para evitar sobrescribir archivos accidentalmente.
- `b` – Binario (binary). Modo que indica que el archivo se manejará como datos binarios (bytes) en lugar de texto. Se usa junto con otros modos, por ejemplo `'rb'` (lectura binaria) o `'wb'` (escritura binaria). En modo binario, no se realiza decodificación de texto ni conversión de caracteres de fin de línea; se leen/escriben bytes puros. Úsalo para archivos no textuales (imágenes, audio, etc.).
- `t` – Texto (text). Modo de texto (es el predeterminado). También se combina con otros, por ejemplo `'rt'` o `'wt'`, aunque normalmente no es necesario especificar `'t'` ya que si no pones `'b'`, Python asume modo texto automáticamente. En modo texto, Python decodifica/encode los datos según un encoding (por defecto UTF-8 en Python 3) y convierte saltos de línea al formato estándar `'\n'` interno.

Además de los modos básicos anteriores, existen modos combinados para leer y escribir a la vez:

- `r+` – Lectura y escritura. Abre el archivo para actualizarlo: permite tanto leer como escribir. El archivo debe existir, ya que no lo crea si falta (similar a `'r'`). El puntero de archivo se ubica al inicio, por lo que si escribes inmediatamente sobrescribirá desde el principio (no trunca todo el archivo, solo sobreescribe sobre los datos existentes desde el comienzo, a menos que muevas el puntero).
- `w+` – Lectura y escritura, pero con comportamiento de creación/truncado. Si el archivo existe, al abrir en `'w+'` se borra todo su contenido (como `'w'`) y queda listo para escribir desde el inicio; si no existe, lo crea. Básicamente es "escribir (limpiando) y luego leer si se quiere".
- `a+` – Lectura y escritura en modo append. Si el archivo no existe, lo crea; si existe, permite agregar al final. El puntero inicialmente se posiciona al final del archivo (como `'a'`), de modo que las escrituras añaden al final. Aún es posible leer el contenido existente, pero ojo: dado que al abrir el puntero está al final, para leer desde el principio del archivo primero debes mover el puntero al inicio (por ejemplo con `f.seek(0)`) antes de usar `read` o `readline`. En resumen, `'a+'` permite leer el archivo completo y además seguir escribiendo al final sin borrar lo previo.

Ejemplos de uso de modos:

- Si queremos leer un archivo existente: `open('data.txt', 'r')`.
- Para crear un archivo nuevo o sobrescribir uno existente con datos: `open('log.txt', 'w')`.
- Para añadir texto al final de un archivo sin borrar su contenido: `open('log.txt', 'a')`.
- Para asegurarnos de no sobreescribir un archivo existente al crearlo: `open('config.ini', 'x')`.
- Para leer un archivo binario (por ejemplo, una imagen): `open('foto.jpg', 'rb')`. La lectura (`f.read()`) devolverá datos tipo bytes. De forma similar, `open('audio.mp3', 'wb')` abre en binario para escritura.
- Para leer y escribir dentro de un mismo archivo (actualización): `open('datos.csv', 'r+')` si queremos modificar contenido existente sin perder todo; `open('datos.csv', 'w+')` si queremos empezar desde cero cada vez; `open('datos.csv', 'a+')` si queremos mantener el archivo y solo anexar pero pudiendo leerlo también.

**Consejo:** Es buena práctica especificar el modo explícitamente incluso si es el predeterminado. Por ejemplo, usar `open('archivo.txt', 'r')` en lugar de confiar en el default, así el propósito queda claro en el código (lectura en este caso). También es útil indicar el encoding si es relevante (e.g. `open('datos.txt', 'r', encoding='utf-8')`), especialmente cuando trabajamos con texto en distintos idiomas o sistemas, para evitar problemas de caracteres no reconocidos.

**Advertencias comunes sobre modos:**

- Abrir en modo lectura `'r'` un archivo que no existe genera un error. Si no estás seguro, comprueba la existencia con `os.path.exists` o maneja la excepción con `try/except`.
- Nunca abras en modo `'w'` un archivo que no quieras modificar/borrar, ya que Python truncará el archivo inmediatamente al abrirlo, antes incluso de escribir nada. Si solo quieres leer, asegúrate de usar `'r'`.
- En modo `'a'`, ten en cuenta que todo lo que escribas irá siempre al final, aunque muevas el puntero al inicio; `'a'` fuerza cualquier operación de escritura a colocarse al final.
- Los modos binarios `'rb'`, `'wb'`, `'ab'`, etc., trabajan con objetos de tipo bytes. Para escribir datos que no sean cadenas, tendrás que convertirlos a bytes (por ejemplo, usando el método `.encode('utf-8')` en una cadena de texto para obtener su representación en bytes). Al leer en modo binario obtendrás bytes; conviértelos a cadena con `.decode('utf-8')` si realmente contienen texto y necesitas interpretarlos como tal.
- Si utilizas un modo de lectura/escritura combinado (`+`), recuerda controlar la posición del puntero (`f.tell()` para obtenerla, `f.seek(offset)` para moverla) según lo que necesites hacer a continuación (p.ej., después de escribir, quizás necesites `f.seek(0)` antes de volver a leer).

## Lectura línea por línea: métodos `read()`, `readline()` y `readlines()`

Una vez que tenemos un archivo abierto en modo lectura, existen distintos métodos para leer su contenido. Cada método tiene utilidades diferentes según lo que necesitemos:

- `f.read(size=-1)`: Lee todo el contenido del archivo en una sola cadena de texto (o hasta `size` bytes/caracteres si se proporciona el parámetro `size`). Si no se especifica `size` (o se pasa -1), leerá hasta el final del archivo. Es útil para archivos relativamente pequeños, que caben cómodamente en memoria, ya que retorna el contenido completo. Por ejemplo:

    ```python
    texto = f.read()  # Leer todo el contenido de poema.txt
    ```

    Aquí `texto` contendrá todo lo que haya en `poema.txt`. Ten en cuenta que si el archivo es muy grande, `f.read()` podría consumir mucha memoria y tiempo, por lo que en esos casos conviene leer por partes o línea a línea.

- `f.readline(size=-1)`: Lee una línea del archivo cada vez que se invoca. Retorna una cadena con la siguiente línea completa, incluyendo el carácter de nueva línea `\n` al final (a menos que sea la última línea y no termine en newline). Si opcionalmente se pasa un número `size`, leerá hasta esa cantidad de caracteres de la línea, pudiendo retornar una línea parcial si no cabe completa en ese número. Usar repetidamente `readline()` nos permite procesar el archivo línea a línea bajo control explícito. Ejemplo básico:

    ```python
    f = open('poema.txt', 'r')
    while True:
        linea = f.readline()
        if linea == '':
            break
        print(linea, end='')
    f.close()
    ```

    Cada llamada va avanzando el puntero del archivo. Cuando el archivo se termina, `readline()` devuelve una cadena vacía `""` para indicar que no hay más datos. Un patrón común es usar un bucle para leer línea por línea hasta fin de archivo:

    ```python
    # Patrón común para leer todas las líneas con readline()
    while True:
        linea = f.readline()
        if not linea:
            break
        # procesar la linea...
    ```

    En este ejemplo, usamos `while` y comprobamos `linea != ''` para continuar hasta llegar al final. Dentro del bucle podemos procesar cada línea (aquí simplemente se imprime). Notar el `end=''` en `print` para no introducir saltos adicionales porque `linea` ya incluye el `\n`.

- `f.readlines()`: Lee todas las líneas del archivo y devuelve una lista de cadenas, donde cada elemento es una línea completa (con su `\n` excepto posiblemente la última). Es una forma rápida de obtener todas las líneas de una vez:

    ```python
    lineas = f.readlines()
    ```

    Esto podría dar algo como: `["Érase una vez...\n", "En un lugar de... \n", "...\n"]` etc., dependiendo del contenido. Luego podríamos iterar sobre la lista `lineas` para procesarlas:

    ```python
    for lin in lineas:
        # procesar lin
    ```

    Sin embargo, cuidado: `readlines()` carga todo el contenido en memoria como una lista, por lo que para archivos muy grandes no es eficiente. En la práctica, una de las maneras más comunes y eficientes de leer un archivo línea por línea es iterar directamente sobre el objeto archivo en un bucle `for`. El objeto `file` es iterable, y al iterarlo devuelve cada línea secuencialmente sin cargar todo el archivo a la vez en memoria:

    ```python
    for linea in f:
        # procesar linea
    ```

    Este enfoque es equivalente a usar `readline()` en cada iteración hasta EOF, pero es más pythónico y eficiente en cuanto a memoria. Además, es más conciso.

**Nota:** Después de leer hasta el final (ya sea con `read()`, múltiples `readline()` o iterando), el puntero del archivo queda al final. Cualquier intento de volver a leer devolverá cadena vacía o lista vacía. Si por alguna razón necesitas releer el archivo, puedes usar `f.seek(0)` para mover el puntero nuevamente al inicio. También puedes abrir el archivo de nuevo en otra variable.

## Escribir línea por línea y otros métodos de escritura

Para escribir en archivos, el método fundamental es `f.write(cadena)`, que escribe la cadena dada en la posición actual del archivo y devuelve el número de caracteres escritos. No agrega saltos de línea u otros separadores por sí solo. Si deseas escribir varias líneas, puedes incluir `\n` en la cadena o invocar `write()` varias veces. Python ofrece también `f.writelines(iterable_de_cadenas)` que toma una lista (u otro iterable) de cadenas y las escribe secuencialmente en el archivo (tal cual se proporcionan). Ojo: `writelines()` no añade separadores ni saltos de línea automáticamente entre los elementos; debes incluirlos en las cadenas si los necesitas. Por ejemplo:

```python
lineas = ["Línea A\n", "Línea B\n", "Línea C\n"]
with open('multi.txt', 'w') as f:
    f.writelines(lineas)
```

Esto creará `multi.txt` con tres líneas. Muchas veces es casi igual de sencillo usar un bucle:

```python
with open('multi.txt', 'w') as f:
    for lin in lineas:
        f.write(lin)
```

El resultado es el mismo, y queda claro dónde van los saltos de línea (en cada elemento de la lista). Finalmente, mencionar que también se puede utilizar la función `print()` para escribir en archivos pasando el parámetro `file`. Por ejemplo:

```python
with open('log.txt', 'w') as f:
    print("Mensaje de log", file=f)
```

Hará que la salida de `print` vaya al archivo en vez de a la consola, agregando por defecto un salto de línea al final. Es útil para formatear texto de manera rápida en archivos.

## Uso de archivos JSON en Python (`json.load` y `json.dump`)

Muchas veces necesitamos almacenar datos estructurados (como diccionarios, listas, configuraciones, etc.) de forma persistente en un archivo, para recuperarlos después. Un formato muy popular para esto es JSON (JavaScript Object Notation). JSON es un formato de texto ligero para representar datos estructurados, originalmente derivado de JavaScript, pero ahora ampliamente usado en muchos lenguajes (incluido Python). En JSON, los datos se representan con sintaxis similar a los diccionarios y listas de Python: por ejemplo, un diccionario Python `{"nombre": "Ana", "edad": 25}` en JSON se ve como `{"nombre": "Ana", "edad": 25}` (muy parecido, solo que en JSON las comillas siempre deben ser dobles, y ciertos valores como `None` se representan como `null`, `True` como `true`, etc.).

¿Por qué JSON? Porque nos permite guardar la información en un archivo de texto de forma estructurada. Un ejemplo típico es guardar las preferencias o configuraciones de un usuario: durante la ejecución del programa mantenemos esos datos en estructuras Python (listas, diccionarios), y al salir los guardamos en un archivo JSON para no perderlos. Al reiniciar el programa, podemos leer ese JSON y restaurar las preferencias.

Python proporciona el módulo estándar `json` para trabajar con este formato. Los dos métodos principales que utilizaremos son:

- `json.dump(obj, archivo)` – Toma un objeto de Python (`obj`) y lo serializa en formato JSON, escribiéndolo directamente en un archivo abierto. Es decir, "dumpea" el objeto en el archivo en formato JSON. Por ejemplo, si `obj` es un diccionario, al usar `json.dump` se convierte a texto JSON y se escribe esa cadena en el archivo.
- `json.load(archivo)` – Lee el contenido JSON de un archivo y lo deserializa, devolviendo el equivalente en Python (listas, diccionarios, etc.). Por ejemplo, si el archivo contiene `{"nombre": "Ana", "edad": 25}`, `json.load` retornará un diccionario `{"nombre": "Ana", "edad": 25}` en Python.

Veamos un ejemplo práctico completo. Supongamos que tenemos un diccionario con configuraciones de una aplicación:

```python
config = {
    "usuario": "alice",
    "tema": "oscuro"
}
with open('config.json', 'w') as f:
    json.dump(config, f)
```

El archivo `config.json` que se crea contendrá algo como:

```json
{"usuario": "alice", "tema": "oscuro"}
```

(Todo en una sola línea por defecto). Si queremos que el JSON se guarde "bonito" con indentaciones, podemos pasar el parámetro `indent` a `json.dump`, por ejemplo `json.dump(config, f, indent=4)`.

Más adelante, en otro momento del programa, podemos leer ese archivo y cargar los datos:

```python
with open('config.json', 'r') as f:
    config_cargado = json.load(f)
print("Usuario:", config_cargado["usuario"])
print("Tema:", config_cargado["tema"])
```

Esto imprimirá los valores que se habían guardado (p.ej., "Usuario: alice", "Tema: oscuro"). Ahora `config_cargado` es un diccionario Python con el mismo contenido que tenía `config` en el momento de guardarlo.

**Detalles y buenas prácticas con JSON:**

- Asegúrate de abrir el archivo en el modo correcto: `'w'` para escritura con `json.dump` (crea/sobrescribe el archivo), `'r'` para lectura con `json.load` (el archivo debe existir y contener JSON válido).
- El módulo `json` maneja los tipos básicos de Python: diccionarios, listas, strings, números, `True`/`False` y `None` (que se convierten a `true`/`false` y `null` en JSON). No puede serializar directamente objetos personalizados, como instancias de clases, a menos que se transformen a tipos básicos (por ejemplo, convirtiéndolos a dicts). Intentar hacer `json.dump(objeto_personalizado, f)` dará error a menos que especifiques un manejador especial.
- Si necesitas simplemente obtener el string JSON de un objeto (sin escribirlo en archivo), usa `json.dumps(obj)` que devuelve la cadena JSON, en lugar de `json.dump` que escribe en archivo. De forma inversa, `json.loads(cadena_json)` toma una cadena JSON y devuelve los datos Python, sin leer de archivo.
- JSON es un formato de texto legible, por lo que los archivos JSON se pueden abrir con un editor de texto y comprobar o modificar manualmente si es necesario. Esto es útil para archivos de configuración.
- Un error común es suponer que `json.dump` y `json.load` funcionan con cadenas directamente; recuerda que requieren un objeto archivo abierto. Si ya tienes el texto JSON en una cadena y quieres convertirlo, usa `json.loads`; si quieres obtener una cadena JSON de un objeto sin archivo, usa `json.dumps`. Pero cuando trabajes con archivos en disco, `dump/load` son los apropiados.
- En cuanto a encoding, `json.dump` escribe texto Unicode. Por defecto, `open()` en modo texto usará UTF-8, así que se manejarán correctamente caracteres especiales (ñ, tildes, etc.) en las cadenas. Si necesitas un encoding diferente, especifícalo en `open()`, tanto al leer como al escribir (pero UTF-8 suele ser la elección adecuada).
- Si el archivo JSON tiene un formato incorrecto (por ejemplo, comas de más, comillas simples en lugar de dobles, etc.), `json.load` lanzará una excepción (`json.JSONDecodeError`). En esos casos, verifica que el archivo sea válido o rodéalo con un `try/except` para manejar errores de parseo.

## Lectura y escritura con NumPy (`loadtxt`, `savetxt`, `genfromtxt`)

Cuando trabajamos con datos numéricos tabulares o matrices, el módulo NumPy proporciona funciones eficientes para leer y escribir estos datos directamente entre archivos de texto y arrays numéricos. Estas funciones son útiles para cargar conjuntos de datos (por ejemplo, desde archivos CSV o TXT con columnas de números) en forma de arrays de NumPy para su procesamiento, o para guardar resultados computacionales en archivos de texto.

### Leer datos numéricos desde texto con `numpy.loadtxt` y `numpy.genfromtxt`

- `numpy.loadtxt(fname, ...)`: Esta función carga datos de un archivo de texto y los devuelve en un `numpy.ndarray` (array de NumPy). Por defecto asume que el archivo contiene datos numéricos organizados en filas y columnas separados por espacios. Puedes especificar parámetros como `delimiter` (delimitador, por ejemplo `','` para CSV), `dtype` (tipo de dato, por defecto `float`), `skiprows` (número de filas iniciales a saltar, útil si hay encabezados) o `usecols` (para leer solo algunas columnas).

    Ejemplo: Supongamos un archivo `datos.txt` con el siguiente contenido (una matriz 2x3):

    ```
    1  2  3
    4  5  6
    ```

    Podemos cargarlo así:

    ```python
    import numpy as np
    data = np.loadtxt('datos.txt')
    ```

    Esto produciría un array 2x3 con tipo `float`:

    ```python
    print(data)
    # [[1. 2. 3.]
    #  [4. 5. 6.]]
    ```

    Ahora `data` es un `numpy.ndarray` y podemos usar operaciones de NumPy con él (sumas, medias, indexing, etc.). Podemos especificar opciones: si el mismo archivo fuera `datos.csv` con comas, usaríamos `np.loadtxt('datos.csv', delimiter=',')`. Si sabemos que los datos son enteros, podríamos usar `dtype=int` para obtener un array de enteros en vez de floats.

- `numpy.genfromtxt(fname, ...)`: Es similar a `loadtxt` pero más flexible para casos complicados. Por ejemplo, `genfromtxt` puede manejar valores faltantes, diferentes tipos de datos por columna, comentarios incrustados, etc. Si `loadtxt` falla porque el archivo no es perfectamente limpio (por ejemplo, algunos números faltan o hay campos no numéricos), `genfromtxt` puede ser la solución.

    Por defecto, los valores faltantes los interpreta como `nan` (si el `dtype` es numérico flotante). Tiene parámetros adicionales como `missing_values` (para indicar qué representaciones en el archivo cuentan como faltantes), `filling_values` (para proporcionar un valor por defecto si falta alguno), y soporta `dtype=None` para intentar inferir tipos de datos de cada columna (lo que puede devolver un array estructurado con distintos tipos por columna). Ejemplo: Supongamos `datos2.csv` contiene:

    ```yaml
    2020,5.0
    2021,
    2022,6.5
    ```

    Aquí la fila de 2021 tiene un valor faltante. `np.loadtxt` no podría leerlo directamente (no todos los campos son números). En cambio:

    ```python
    data2 = np.genfromtxt('datos2.csv', delimiter=',')
    ```

    Esto podría dar un array 3x2 (asumiendo `dtype float` por defecto) donde la posición faltante se convierte en `nan` (Not a Number):

    ```python
    print(data2)
    # [[2020.     5. ]
    #  [2021.     nan]
    #  [2022.     6.5]]
    ```

    Ahora podemos manejar ese `nan` como consideremos (por ejemplo, ignorarlo en cálculos o reemplazarlo). Si quisiéramos que la primera columna fuera enteros (años) y la segunda floats, podríamos usar `dtype=[('anio', 'int'), ('valor','float')]` en `genfromtxt` para obtener un array estructurado con campos nombrados.

    En general, usa `np.loadtxt` para archivos simples y limpios (todos números, formato consistente). Si el archivo tiene detalles adicionales (cabeceras, comentarios, distintos tipos), considera `np.genfromtxt`. Ambos son para texto; si necesitas eficiencia máxima y no necesitas legibilidad, NumPy también tiene formatos binarios propios (ver nota al final). Ambos `loadtxt` y `genfromtxt` pueden aceptar no solo nombres de archivo sino también cualquier objeto similar a archivo (por ejemplo, un objeto `StringIO` con contenido simulado), pero típicamente les pasamos la ruta del archivo. Tras la lectura, generalmente obtendrás un array de 2 dimensiones si el archivo tenía varias filas y columnas. Puedes comprobar `data.shape` para ver dimensiones, y `data.dtype` para ver el tipo de dato.

**Precauciones al leer con NumPy:**

- Asegúrate de que los datos en el archivo son numéricos o especifica un `dtype` apropiado. Si hay texto inesperado (como cadenas donde esperas números), puede haber errores de conversión. `genfromtxt` intentará manejarlo (por ejemplo, convirtiendo texto vacío a `nan`), pero en algunos casos necesitarás proporcionar un conversor personalizado mediante el parámetro `converters`.
- Si el archivo contiene un encabezado (nombres de columnas en la primera línea) u otras líneas no numéricas, usa `skip_header` (o `skiprows` en `loadtxt`) para saltarlas.
- Los delimitadores correctos: `loadtxt` por defecto separa por espacios en blanco. Para comas, tabulaciones u otros separadores, usa el argumento `delimiter=','` (o `'\t'` para tabulaciones, etc.).
- Recuerda que tanto `loadtxt` como `genfromtxt` devuelven todo el dataset de una vez. Si el archivo es extremadamente grande (varios GB de texto), podría ser lento o consumir mucha memoria. En esos casos, puede ser mejor usar lectura por partes o utilizar otras herramientas (por ejemplo, la librería `pandas` es útil para CSV grandes, o usar los formatos binarios de NumPy descritos abajo).

### Guardar arrays en texto con `numpy.savetxt`

Para escribir datos desde un array de NumPy a un archivo de texto, usamos `numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', ...)`. Esta función toma un array `X` (puede ser 1D o 2D) y lo vuelca en un archivo de texto cuyo nombre es `fname`. Podemos especificar el formato de cada valor con `fmt` (por defecto notación científica con 18 decimales, lo cual es excesivo en muchos casos, así que a menudo especificamos algo más sencillo como `%d` para enteros o `%.2f` para floats con 2 decimales). También podemos elegir el delimitador (espacio por defecto). Ejemplo: tenemos un array de enteros y queremos guardarlo:

```python
import numpy as np
X = np.array([[1, 2, 3],
              [4, 5, 6]])
np.savetxt('matriz.txt', X, delimiter=',', fmt='%d')
```

Esto creará un archivo `matriz.txt` donde cada fila del array es una línea, y los valores separados por comas:

```
1,2,3
4,5,6
```

Si luego abrimos ese archivo con `np.loadtxt('matriz.txt', delimiter=',', dtype=int)`, obtendríamos de vuelta el mismo array de números enteros.

Consejos al usar `savetxt`:

- Escoge el `fmt` adecuado para tus datos. `%d` para enteros, `%.3f` por ejemplo para floats con 3 decimales, etc. También puedes pasar una lista de formatos si quieres formatear columnas de manera distinta, o incluso una sola cadena de formato que incluya separadores. Por ejemplo, `fmt='%10.5f'` alinea en un campo de 10 caracteres con 5 decimales.
- Incluye la extensión apropiada en el nombre del archivo (como `.txt` o `.csv`). `savetxt` no añade automáticamente una extensión, simplemente crea el nombre tal cual lo pasas. Si llamas `np.savetxt('datos', X)`, generará un archivo llamado "datos" sin extensión. Por claridad, es mejor darle extensión.
- Puedes agregar una línea de encabezado o comentarios usando los parámetros `header` y `comments`. Por ejemplo: `np.savetxt('datos.csv', X, delimiter=',', header="col1,col2,col3", comments='')` escribirá los nombres de columna en la primera línea. El `comments=''` evita que NumPy preceda el header con un carácter `#` (por defecto lo trata como comentario).
- Ten presente que al guardar en texto, se pierde algo de información de tipo: todo se convierte en texto plano. Si necesitas almacenar datos con su tipo original exacto, muchas cifras decimales, o estructuras más complejas, tal vez prefieras un formato binario (ver nota abajo).

⚠ **Nota:** NumPy también ofrece funciones binarias para I/O, como `numpy.save` / `numpy.load` (que guardan y cargan en un formato binario propietario `.npy`) y `numpy.savez`/`load` (para múltiples arrays en un `.npz` comprimido). Estas son aún más eficientes para almacenar y recuperar arrays grandes, conservando tipos exactos y sin problemas de formato. Sin embargo, esos archivos no son legibles directamente por humanos ni por otras herramientas sin usar NumPy. En contexto de intercambio de datos con otros, el texto (CSV/TSV) es más universal, mientras que para uso interno y eficiencia, `.npy` es excelente. Dependiendo de la situación, decide cuál conviene. En esta sección nos centramos en las funciones de texto `loadtxt`, `genfromtxt` y `savetxt` porque permiten interactuar fácilmente con datos legibles y editables.

# Manejo de Excepciones

## Introducción a las excepciones en Python

En Python (y en muchos lenguajes), una excepción es un evento anormal que ocurre durante la ejecución de un programa y altera el flujo normal de las instrucciones. En términos simples, una excepción es un error en tiempo de ejecución. Cuando ocurre una excepción y no es manejada, nuestro programa termina abruptamente (crashea), mostrando un mensaje de error. El objetivo de manejar excepciones es precisamente evitar esos crashes y controlar adecuadamente las situaciones inesperadas.

¿Por qué necesitamos manejar excepciones?  Imagina un programa que intenta abrir un archivo que no existe, o dividir por cero, o convertir una cadena no numérica a número. Todos estos casos producirán errores en tiempo de ejecución. Si no anticipamos y manejamos esos errores, el programa se detendrá inesperadamente. La gestión de excepciones permite que nuestros programas sean más robustos y estables, añadiendo solidez a nuestro código al contemplar distintos casos de fallo. En resumen, manejando los errores conseguimos que nuestros programas no se cierren ante situaciones inesperadas, sino que actúen de forma controlada (por ejemplo, mostrando un mensaje de error amigable al usuario y continuando con la ejecución) .

Excepción vs error común: En Python, las excepciones son objetos especiales que representan condiciones de error. Se crean automáticamente cuando Python no puede realizar la operación solicitada. Por ejemplo, al intentar dividir por cero, Python crea un objeto de excepción de tipo `ZeroDivisionError` indicando el problema. Es importante destacar que las excepciones son errores en tiempo de ejecución. Errores de sintaxis (como olvidar dos puntos en un `if` o mal indentado) no son excepciones; esos deben corregirse antes de ejecutar el programa. Las excepciones ocurren mientras el programa corre, por causas como operaciones inválidas, recursos faltantes, etc.

En resumen, una excepción es señalada por Python cuando algo inusual sucede (archivo no encontrado, índice fuera de rango, división por cero, etc.). Nuestro trabajo como desarrolladores es indicarle a Python cómo manejar esas situaciones, en lugar de simplemente dejar que el programa termine con un mensaje críptico. A continuación, veremos los tipos de excepciones más comunes y cómo podemos manejarlas con las estructuras `try` y `except`.

**Tipos comunes de excepciones en Python**

Existen muchas excepciones integradas en Python. Aquí listamos algunas de las más comunes, junto con la situación típica en que se producen:

- `ZeroDivisionError` – Ocurre cuando intentamos dividir un número por cero. Ejemplo: `10 / 0` provocará esta excepción, ya que matemáticamente la división por cero no está definida.
- `FileNotFoundError` – Se lanza cuando intentamos abrir un archivo que no existe en la ruta especificada. Ejemplo: `open("archivo_que_no_existe.txt")` dará `FileNotFoundError` si el archivo no se encuentra.
- `ValueError` – Surge cuando una función recibe un argumento de tipo correcto pero valor inapropiado. Por ejemplo, intentar convertir la cadena `"abc"` a entero con `int("abc")` produce `ValueError` (la cadena no tiene formato numérico).
- `TypeError` – Indica que se ha utilizado un tipo de dato inapropiado en una operación o función. Ejemplo: `5 + "hola"` provoca `TypeError` porque estamos intentando sumar un número entero con una cadena.
- `IndexError` – Se lanza al intentar acceder a una posición índice que no existe en una secuencia (lista, tupla, etc.). Ejemplo: `lista = [1, 2, 3]; lista[5]` dará `IndexError` ya que el índice 5 está fuera del rango de la lista.
- `KeyError` – Similar al anterior, ocurre al intentar acceder a una clave que no existe en un diccionario. Ejemplo: `dic = {"a": 1}; dic["b"]` dará `KeyError` porque la clave "b" no está en el diccionario.
- `NameError` – Ocurre cuando el código referencia a una variable o nombre que no ha sido definido. Ejemplo: usar `valor = x + 10` sin haber definido `x` previamente lanza un `NameError`.
- `AttributeError` – Se lanza cuando intentamos acceder o llamar un atributo/método que no existe para cierto objeto. Ejemplo: `numero = 5; numero.append(3)` produce `AttributeError` porque un entero (`int`) no tiene el método `append`.

Estos son solo algunos ejemplos. Python tiene una jerarquía completa de excepciones (todas derivan de la clase base `Exception` o sus subclases). Saber el tipo exacto de la excepción que puede ocurrir nos permite prepararnos para manejarla. En la siguiente sección, veremos cómo capturar y manejar estas excepciones usando bloques `try/except`.

Nota: No todas las situaciones de error generan excepciones que podamos manejar. Por ejemplo, los errores de sintaxis o de indentación (ej. olvidarse de un paréntesis o una comilla) ocurren antes de la ejecución y Python los reporta sin posibilidad de manejarlos con un `try/except`. Asegúrate de que tu código esté libre de errores de sintaxis; luego utiliza excepciones para manejar condiciones anómalas en tiempo de ejecución.

## Uso básico de `try` y `except` con ejemplos

Para manejar excepciones en Python utilizamos los bloques `try` y `except`. La sintaxis básica es:

```python
try:
    # código que puede lanzar excepciones
except TipoDeExcepcion1:
    # manejar excepción TipoDeExcepcion1
except TipoDeExcepcion2:
    # manejar excepción TipoDeExcepcion2
else:
    # código que se ejecuta si no hubo ninguna excepción
finally:
    # código que se ejecuta siempre, ocurra o no la excepción
```

El flujo de ejecución es el siguiente:

1. Python ejecuta las instrucciones dentro del bloque `try`.
2. Si no ocurre ninguna excepción durante la ejecución del bloque `try`, Python ignora todas las secciones `except` asociadas y continúa con el código que sigue después del bloque.
3. Si ocurre una excepción dentro del bloque `try`, Python inmediatamente salta al bloque `except` que corresponda al tipo de excepción ocurrida, ejecuta ese bloque `except` y luego continúa después del bloque `try/except`.
4. Durante este salto, el resto de líneas que quedaban por ejecutar en el bloque `try` se saltan por completo.
5. Si tenemos múltiples bloques `except` encadenados para distintos tipos de error, Python elegirá automáticamente el primero que coincida con el tipo de la excepción lanzada.
6. Si la excepción ocurrida no coincide con ningún `except` especificado, la excepción propaga hacia fuera del bloque (es decir, no fue manejada en ese `try`). En ese caso, si hay un `try` más externo, se puede capturar allí; si no se captura en ningún lado, finalmente el programa terminará mostrando el error.

Veamos un ejemplo sencillo. En este caso dividimos dos números, capturando el error de división por cero:

```python
try:
    a = float(input("Ingresa el numerador: "))
    b = float(input("Ingresa el denominador: "))
    resultado = a / b
except ValueError:
    print("❌ Debes ingresar un número válido.")
except ZeroDivisionError:
    print("❌ Error! No se puede dividir entre cero.")
else:
    print(f"✅ Resultado: {resultado}")
```

Salida: ¡Error! No se puede dividir entre cero.

En este ejemplo, como `b` es 0, la línea `resultado = a / b` lanza una excepción `ZeroDivisionError`. Python inmediatamente abandona el bloque `try` en ese punto y busca un bloque `except` que maneje `ZeroDivisionError`. Lo encuentra y ejecuta la instrucción dentro del `except`, que imprime el mensaje de error personalizado. Después de eso, el programa continúa (no hay más código después del `try/except` en este ejemplo, así que simplemente termina de forma controlada). Si `b` hubiera sido distinto de 0, el bloque `except` se habría ignorado por completo y hubiéramos visto el resultado de la división.

Podemos asociar múltiples `except` a un mismo `try` para manejar distintos tipos de excepciones por separado. Por ejemplo, combinemos dos posibles errores: división por cero y error de tipo (intentaremos convertir una entrada a entero). Supongamos un programa que pide dos números al usuario y realiza la división:

```python
try:
    num = int(input("Número entero: "))
    den = int(input("Divisor entero: "))
    resultado = num / den
except ValueError:
    print("Debes ingresar un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("Resultado:", resultado)
```

¿Qué está pasando aquí?

En el bloque `try` intentamos convertir las entradas a enteros y luego realizar la división.

Si el usuario ingresa algo que no es número (por ejemplo "abc"), la conversión `int(input())` lanzará una excepción `ValueError`. Python saltará al bloque `except ValueError` correspondiente y mostrará "Debes ingresar un número válido.". En ese caso ni siquiera intenta la división porque el error ocurrió antes.

Si el usuario ingresa números pero el segundo es 0, la excepción se lanzará en la línea de la división, saltando al bloque `except ZeroDivisionError` y mostrando el mensaje de división por cero.

Si no ocurre ninguna excepción (es decir, se ingresa correctamente dos números y el segundo no es 0), se imprimirá el resultado y ninguno de los `except` se ejecutará.

También es posible usar un `except` general (sin especificar tipo) para capturar cualquier excepción. Por ejemplo:

```python
try:
    # código que puede fallar
except Exception as e:
    print("Ocurrió un error inesperado:", e)
```

Sin embargo, usar `except Exception` (o peor, un `except:` genérico sin ni siquiera `Exception`) no siempre es buena idea – hablaremos de esto en Prácticas recomendadas. Lo útil es que existe la posibilidad de capturar en un solo bloque errores diversos, por ejemplo para loguearlos o tratarlos de forma común.

Por último, Python ofrece también las cláusulas opcionales `else` y `finally` en la estructura de excepciones:

- El bloque `else` (colocado después de todos los `except`) se ejecuta solo si no ocurrió ninguna excepción en el `try`. Sirve para poner código que debe correr cuando todo va bien, separándolo del bloque `try` principal por legibilidad.
- El bloque `finally` se ejecuta siempre, haya o no excepción. Generalmente se usa para acciones de limpieza (cleanup), como cerrar archivos, liberar recursos, etc., asegurando que ocurran pase lo que pase (incluso si no se capturó una excepción).

Un ejemplo breve ilustrando `else` y `finally`:

```python
try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    print("No se encontró el archivo.")
else:
    contenido = archivo.read()
    archivo.close()
    print("Archivo leído con éxito.")
finally:
    print("Fin de la operación.")
```

En este código, si el archivo se abre correctamente no hay excepción, entonces se ejecuta el bloque `else` (leemos y cerramos el archivo, e indicamos éxito). Independientemente de lo anterior, el bloque `finally` imprimirá "Fin de la operación." al final. Si el archivo no existe, entra al `except FileNotFoundError` y luego igual pasa por `finally`. (Si existe, entra al `else` y luego al `finally`).

El uso de `else` y `finally` no es obligatorio, pero puede ayudar a hacer nuestro código de manejo de errores más claro y seguro.

### 🛠 Manejo de errores personalizados: mensajes y uso de `except Exception as e`

Cuando capturamos excepciones, a menudo queremos proporcionar mensajes de error personalizados para el usuario, más descriptivos o amigables que el mensaje de error por defecto de Python. Ya vimos un ejemplo: en lugar de permitir que Python muestre su mensaje estándar (en inglés) "division by zero", imprimimos "El denominador no puede ser 0 (división por cero)." en español, que es más claro para el usuario final.

Hay dos formas comunes de personalizar la información que damos sobre un error:

1. Mensaje fijo personalizado: Escribir directamente con `print()` un mensaje explicativo en el bloque `except`. Por ejemplo, ante un `FileNotFoundError`, podemos hacer:

    ```python
    try:
        datos = open("config.cfg", "r")
    except FileNotFoundError:
        print("Archivo de configuración no encontrado, se usarán valores por defecto.")
        datos_por_defecto()
    ```

    Aquí, si el archivo no existe, informamos al usuario con un mensaje claro de lo ocurrido y posiblemente cómo el programa va a reaccionar (usar valores por defecto).

2. Usar el objeto de excepción (`Exception as e`): Python nos permite capturar la excepción en una variable para inspeccionarla. La sintaxis es `except TipoDeError as e:`. Ese objeto `e` contiene información sobre el error ocurrido, incluyendo el mensaje original de Python. Podemos imprimirlo o usarlo en nuestro mensaje. Ejemplo:

    ```python
    try:
        import biblioteca_no_instalada
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
    ```

    Si el módulo no está instalado, esto imprimirá algo como "Ocurrió un error inesperado: No module named 'biblioteca_no_instalada'". Estamos combinando un texto nuestro con la información del sistema (el mensaje de la excepción real). Esto es útil para depuración o para casos donde no sabemos exactamente qué tipo de error puede ocurrir pero queremos mostrar su detalle.

Al usar `except Exception as e` sin especificar un tipo más concreto, estamos capturando cualquier excepción que sea instancia de `Exception` (lo que abarca prácticamente todas las excepciones típicas). Es una manera conveniente de atrapar lo que sea y, por ejemplo, loguearlo o mostrarlo. Pero ten cuidado: si lo usas de manera muy general, podrías terminar capturando excepciones que no esperabas y quizás ocultando errores de programación. Siempre que sea posible, captura excepciones específicas que sepas manejar; utiliza un catch-all genérico solo como respaldo para imprevistos, y preferiblemente en combinación con un re-lanzamiento o registro del error (para no silenciarlo completamente, más sobre esto en Prácticas recomendadas).

Otro aspecto avanzado es la posibilidad de definir nuestras propias excepciones (excepciones personalizadas). Python nos permite crear nuevas clases de excepción derivando de `Exception` (o alguna subclase). Esto es útil cuando estamos desarrollando módulos o aplicaciones en las que queremos señalar situaciones de error específicas de nuestra lógica, con su propio tipo. Por ejemplo, podríamos definir:

```python
class DatosInvalidosError(Exception):
    """Excepción lanzada cuando los datos no cumplen ciertos criterios."""
    pass
```

En este snippet, creamos una excepción `DatosInvalidosError`. La función `procesar_datos` lanzaría (raise) esta excepción si la validación falla. En otro lugar del código, podemos envolver la llamada a `procesar_datos` en un `try/except DatosInvalidosError` para manejar esa situación particular. Al hacer esto, estamos personalizando el tipo de error (dándole un nombre propio) y proporcionando un mensaje descriptivo. Por supuesto, podríamos simplemente lanzar una excepción genérica existente como `ValueError` con un mensaje personalizado (`raise ValueError("mensaje")`), y eso muchas veces es suficiente. Definir una clase de excepción nueva se suele reservar para cuando tenemos un escenario de error que realmente sea distinto a los predefinidos, o para distinguirlo claramente en bloques `except`.

Resumen de esta sección: Podemos y debemos adaptar la forma en que reportamos los errores:

- Escribir mensajes de error comprensibles para el usuario (y en su idioma) usando `print` en los bloques `except`.
- Usar `except ... as e` para obtener el mensaje original del sistema si es útil (por ejemplo, para registro de logs o para incluir detalles técnicos).
- Incluso crear y lanzar nuestras propias excepciones en casos especiales para hacer el código más claro y controlable.

Lo importante es no dejar que excepciones imprevistas rompan el programa sin más. Más bien, manejarlas o al menos detectarlas para poder informar o terminar el programa elegantemente.

## Prácticas recomendadas en el manejo de excepciones

Manejar excepciones es un arte 🎨: hay que encontrar el equilibrio entre capturar los errores que podemos anticipar y no abusar capturando todo y ocultando problemas. A continuación, algunas prácticas recomendadas y consideraciones al trabajar con excepciones en Python:

- Captura solo las excepciones que sabes manejar: Si sabes que en cierto bloque puede ocurrir, por ejemplo, `FileNotFoundError` y quieres reaccionar a eso (crear el archivo, avisar al usuario, etc.), captura específicamente `FileNotFoundError`. No hagas un `except Exception:` gigantesco envolviendo todo tu código "por si acaso". Capturar excepciones muy genéricas puede atrapar errores que no esperabas y dificultar detectar errores lógicos en tu programa.
- No silencies las excepciones sin necesidad: Un error común es hacer `except Exception: pass` (o un `except` específico y dejarlo vacío). Esto hará que el programa continúe como si nada, lo cual puede ser peligroso: el código puede seguir ejecutándose en un estado inconsistente. Siempre maneja la excepción de alguna forma: al menos loguéala o informa al usuario de que algo salió mal. Ignorarla por completo suele ser mala idea, a menos que realmente estés seguro de que no importa (casos raros).
- Informar al usuario adecuadamente: Decide qué nivel de detalle necesita el usuario. Dar demasiada información técnica puede ser contraproducente. Por ejemplo, si tu programa intenta procesar 100 archivos y 5 no se pueden abrir, podrías:
    - Informar de cuáles 5 no se abrieron (si el usuario proporcionó esos nombres, le será útil saber qué falló y por qué).
    - O simplemente ignorarlos y quizás al final decir "Algunos archivos no pudieron procesarse" sin abrumar con detalles, si el usuario ni sabía qué archivos debían estar.
    
    Dar información que el usuario no necesita puede confundir o alarmar innecesariamente, reduciendo la utilidad percibida de tu programa. Por otro lado, ocultar por completo un problema puede llevar a resultados inesperados sin explicación. ¡Equilibrio! ⚖
- No uses excepciones para flujo normal si puedes evitarlo: En Python existe el principio "Es más fácil pedir perdón que permiso" (EAFP, Easier to Ask Forgiveness than Permission), que anima a usar excepciones para manejar condiciones en lugar de chequear todo manualmente antes. Ejemplo: es más conciso hacer `try/except FileNotFoundError` al abrir un archivo que primero usar `os.path.exists`. Sin embargo, no caigas en el extremo de usar excepciones para lógica esperada muy frecuente, ya que manejar excepciones tiene un costo. Si algo es parte del flujo normal (no una situación excepcional), a veces es mejor un condicional.
- Utiliza `finally` o context managers para limpieza: Si abres recursos externos (archivos, conexiones de red, etc.), asegúrate de cerrarlos. El bloque `finally` es tu amigo para garantizar que, ocurra o no una excepción, ciertos pasos se ejecuten. Una alternativa aún más limpia es usar gerentes de contexto (la cláusula `with` en Python) que automáticamente cierran recursos al salir del bloque. Por ejemplo, en lugar de abrir un archivo y cerrarlo en un `finally`, podrías hacer:

    ```python
    with open('datos.txt', 'r') as f:
        contenido = f.read()
    # aquí el archivo ya está cerrado automáticamente
    ```

    Aquí, pase lo que pase, el archivo se cerrará al salir del `with`, incluso si hubo excepción o si fue manejada.
- Errores de programación vs condiciones excepcionales: Si tu código tiene un bug (por ejemplo un índice fuera de rango por un cálculo mal hecho), idealmente quieres descubrirlo y corregirlo, no esconderlo tras un `except IndexError` que haga como si nada. En pruebas y desarrollo, es útil dejar que esas excepciones "bug" exploten para que puedas arreglar el código. Solo captura excepciones que esperes en situaciones correctas. Un código bien escrito y probado será propenso a muy pocos errores lógicos inesperados 😉. En cambio, las excepciones que provienen de factores externos (entradas de usuarios, archivos, red, dispositivos, etc.) son las que deberías anticipar y manejar.

Posibles fuentes de error a considerar: siempre que tu programa dependa de factores externos, hay potencial de excepción. Por ejemplo:

- Datos proporcionados por el usuario (pueden tener formato incorrecto, tipos erróneos, valores fuera de rango...).
- La existencia y accesibilidad de un archivo o directorio (puede no existir, no tener permisos, estar en uso, etc.).
- Disponibilidad de una conexión de red o de un recurso externo (puede fallar la conexión, URL inválida, servidor caído...).

En cada caso, piensa: "Si ocurre X, ¿qué debería hacer mi programa?". Si la respuesta es "simplemente terminar porque no hay nada que hacer", quizá ni siquiera necesitas capturar esa excepción (deja que suba y termine el programa con un mensaje de error estándar). Pero si puedes recuperar la situación (pedir un dato de nuevo, intentar un archivo alternativo, notificar al usuario y seguir, usar un valor por defecto, etc.), entonces implementa un bloque `try/except` apropiado.

Resumiendo las mejores prácticas:

- Maneja las excepciones esperadas de forma explícita.
- No ocultes errores inesperados (al menos regístralos para depuración).
- Proporciona información útil pero no abrumadora al usuario final.
- Limpia recursos en un `finally` o usando `with` para evitar efectos secundarios.

Y, por supuesto, prueba tu código con diferentes escenarios para asegurarte de que tus manejos de excepción funcionan correctamente.

