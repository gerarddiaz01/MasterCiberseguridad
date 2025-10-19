
# 📄 Ejemplo práctico completo: Análisis de textos con manejo de errores

Veamos ahora un ejemplo integral para aplicar todo lo anterior. Supongamos que queremos hacer un pequeño analizador de textos: nuestro programa va a leer varios archivos de texto y contar cuántas palabras tiene cada uno, y al final dar un total de palabras procesadas. Este escenario nos permitirá ver manejo de excepciones con archivos (por si algún archivo no existe) y la decisión de reportar o no ciertos errores al usuario.

Imaginemos que tenemos una lista de nombres de archivos de texto (podrían ser archivos de libros obtenidos de Project Gutenberg u otra fuente). Algunos archivos pueden existir y otros no, para simular distintos casos. Queremos que el programa procese todos los archivos que pueda y no se detenga si uno falla. Aquí está una posible implementación:

```python
archivos = ["texto1.txt", "texto2.txt", "novela.txt", "inexistente.txt"]
total_palabras = 0
for archivo in archivos:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"Advertencia: el archivo {archivo} no se encontró. Se omitirá.")
        continue
    except Exception as e:
        print(f"No se pudo procesar {archivo} por un error inesperado:", e)
        continue
    # Si llegamos aquí, la lectura fue exitosa
    palabras = contenido.split()
    print(f"{archivo}: {len(palabras)} palabras")
    total_palabras += len(palabras)
print("Total de palabras procesadas:", total_palabras)
```

**Explicación del código:**

- Definimos una lista `archivos` con cuatro nombres. Supongamos que "inexistente.txt" no existe en el directorio, para ver qué pasa.
- Recorremos cada nombre en la lista. Para cada archivo, intentamos abrirlo en modo lectura ("r") con codificación UTF-8 (para soportar acentos, etc.), utilizando un bloque `with`. Usamos `with open(..., "r") as f` porque es una forma recomendada que automáticamente cerrará el archivo al terminar de usarlo.
- Si el archivo no existe, `open` lanza `FileNotFoundError` y saltamos al bloque `except FileNotFoundError`. Allí imprimimos una advertencia amigable al usuario, indicando que ese archivo se omitirá. Luego `continue` hace que pasemos al siguiente archivo de la lista sin ejecutar lo que queda del bucle para el archivo actual.
- También incluimos un `except Exception as e` genérico. Esto capturará cualquier otra excepción que pueda ocurrir durante la lectura (por ejemplo, si no tuviéramos permiso de leer el archivo, Python lanzaría `PermissionError`, que caería aquí). En tal caso, informamos que no se pudo procesar ese archivo por un error inesperado, mostramos el mensaje `e` para detalles técnicos, y continuamos con el siguiente archivo.
- Si el `with open` tiene éxito (no hubo excepción), pasamos a la siguiente parte del bucle: contamos las palabras del contenido. Utilizamos `str.split()` sin argumentos para separar por espacios en blanco (espacios, saltos de línea, tabs) y obtenemos una lista de palabras, luego `len` para contar cuántas hay.
- Imprimimos el resultado parcial: cuántas palabras tenía el archivo procesado.
- Acumulamos el conteo en `total_palabras`.
- Después del bucle, imprimimos el total de palabras contadas entre todos los archivos procesados exitosamente.

**Salida esperada:**

```
texto1.txt: 1200 palabras
texto2.txt: 950 palabras
novela.txt: 53400 palabras
Advertencia: el archivo inexistente.txt no se encontró. Se omitirá.
Total de palabras procesadas: 55550
```

Observa que:
- Procesó los tres primeros archivos y mostró sus conteos.
- Al llegar a `inexistente.txt`, lanzó la advertencia pero no se detuvo el programa; simplemente no sumó nada de ese archivo.
- Al final dio el total solo de los archivos que sí pudo leer.
- Gracias al manejo de excepciones, ningún error detuvo el programa por completo. Sin `try/except`, el programa habría crasheado en el intento de abrir `inexistente.txt` y nunca habría mostrado los resultados de los otros archivos.

¿Debemos reportar todos los errores al usuario? Depende del caso de uso:
- Si el usuario sabía qué archivos debían procesarse (por ejemplo, porque él mismo nos dio la lista), seguramente espera o agradece saber que 'inexistente.txt' no se pudo analizar y por qué. Así puede corregir el nombre o añadir el archivo que falta.
- Pero si la lista de archivos es interna del programa y el usuario solo espera un resultado global, tal vez podríamos optar por no mostrar un mensaje por cada archivo faltante y simplemente al final indicar "Algunos archivos no pudieron ser leídos" o incluso no mencionar nada si no es crucial. Esto para no abrumar con detalles innecesarios.

En nuestro ejemplo imprimimos un mensaje de advertencia con cada archivo omitido, lo cual está bien para transparencia en muchos casos. Lo importante es tomar una decisión consciente sobre la comunicación de errores: brindar información útil, pero no saturar al usuario con mensajes que no le sirven. Siempre que se omite un error (errores silenciosos), hazlo porque no afecta al propósito principal desde la perspectiva del usuario. Si afecta, entonces debe saberse.



# 🏋 Ejercicios de práctica (con enunciado y solución explicada)

A continuación te proponemos una serie de ejercicios para practicar el manejo de excepciones en Python. Cada ejercicio incluye un enunciado (el problema a resolver), una posible estructura o pista para ayudarte a encaminar la solución, y finalmente una solución propuesta con explicación. ¡No dudes en intentar resolverlos por tu cuenta primero antes de ver la solución! 💪

## Ejercicio 1: División segura

**Enunciado:**

Escribe un programa que solicite al usuario dos números (un numerador y un denominador) y muestre el resultado de la división del numerador por el denominador. Si el usuario ingresa un valor que no es numérico, el programa debe detectar el error y avisar con un mensaje sin terminar abruptamente. Si el denominador es cero, el programa no debe intentar dividir (ya que causaría un error); en su lugar, debe imprimir un mensaje indicando que la división por cero no es posible.

**Pista (Estructura sugerida):**

Necesitarás usar `input()` para obtener los valores, convertirlos a tipo numérico (por ejemplo `int` o `float`), y usar un bloque `try/except` para englobar la operación de división. Debes manejar al menos dos tipos de excepción: una para el caso en que la conversión de entrada a número falle (`ValueError`) y otra para la división por cero (`ZeroDivisionError`). El flujo podría ser:

- Pedir numerador y denominador al usuario.
- Intentar convertirlos a número y dividir.
- Si ocurre un `ValueError` en la conversión, notificar al usuario que la entrada no era válida.
- Si ocurre `ZeroDivisionError` en la división, notificar sobre división por cero.
- Si todo sale bien, mostrar el resultado.

**Solución propuesta:**

```python
try:
    num = float(input("Numerador: "))
    den = float(input("Denominador: "))
    resultado = num / den
except ValueError:
    print("❌ Debes ingresar un número válido.")
except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre cero.")
else:
    print(f"✅ Resultado: {resultado}")
```

**Explicación:**

En este código, englobamos toda la secuencia de leer entradas, convertir a float y dividir dentro de un `try`. Esto porque tanto la conversión a float como la división pueden producir excepciones. Manejos implementados:

- Si el usuario ingresa algo que no puede convertirse a número (ej: "abc" o "5,3" con coma en vez de punto decimal), la conversión a float lanza `ValueError`. Capturamos ese error y mostramos un mensaje indicándolo. De este modo, el programa no se cierra abruptamente con un traceback feo, sino que informa elegantemente del problema.
- Si la conversión va bien pero luego el denominador resulta ser 0, la operación numerador / denominador lanza `ZeroDivisionError`. Nuestro segundo bloque except captura ese caso y avisa del error específico de división por cero.
- Usamos un bloque `else` después de los except: esto se ejecutará solo si no hubo ninguna excepción. En ese caso, significa que la división se realizó con éxito, así que mostramos el resultado normalmente.
- Los iconos (❌ y ✅) en los mensajes son opcionales, solo para hacer más claro visiblemente qué es error y qué es éxito.
- Si quisiéramos, podríamos pedir los números en un loop hasta que ingrese datos correctos; pero aquí, con un solo intento, ilustramos el manejo básico de errores. Siempre podrías envolver esto en un `while True` para repetir la pregunta en caso de error, saliendo del loop (`break`) solo cuando logre obtener un resultado (usando el bloque `else` como indicador de éxito).

---

## Ejercicio 2: Lectura de archivo con reintento

**Enunciado:**

Crea un programa que le pida al usuario el nombre de un archivo de texto a abrir. Intenta abrir el archivo y leer su contenido. Si el archivo no existe (`FileNotFoundError`), el programa debe informar al usuario y darle otra oportunidad de ingresar un nombre de archivo, en lugar de terminar con error. Si el archivo se abre correctamente, muestra en pantalla la primera línea del archivo (o todo su contenido, como prefieras) y termina.

**Pista (Estructura sugerida):**

Aquí es útil usar un bucle para seguir preguntando mientras falle. Por ejemplo:

- Mientras True (bucle infinito):
    - Pedir al usuario el nombre de archivo.
    - Intentar abrir el archivo dentro de un try.
    - Si se abre con éxito, quizás usar un break para salir del bucle.
    - Si lanza `FileNotFoundError`, informar y el loop continúa, solicitando de nuevo.
- Después del loop, si salimos porque logramos abrir (habrás hecho un break), entonces procede a leer del archivo y mostrar lo requerido.

**Solución propuesta:**

```python
while True:
    nombre = input("Ingrese el nombre del archivo: ")
    try:
        with open(nombre, "r") as archivo:
            lineas = archivo.readlines()
        break
    except FileNotFoundError:
        print("Archivo no encontrado, intenta nuevamente.")
    except Exception as e:
        print("Error al abrir el archivo:", e)
        print("Intenta nuevamente.")

# Si llegamos aquí, significa que `lineas` tiene el contenido leído con éxito
if lineas:
    print("Primera línea:", lineas[0].strip())
else:
    print("El archivo está vacío.")
```

**Explicación:**

- Usamos un bucle `while True` para permitir múltiples intentos de ingreso.
- Dentro del `try`, usamos `with open(..., "r") as archivo:` para intentar abrir el nombre dado en modo lectura. Si el archivo no existe, saltaremos al `except FileNotFoundError` antes de llegar a leer.
- Si `open` falla por archivo no encontrado, informamos al usuario y usamos `continue` para volver a la cabecera del `while` y pedir otro nombre. Esto seguirá hasta que el `open` funcione.
- También agregamos un `except Exception as e` general, por si ocurre algún otro error al intentar abrir (por ejemplo, un problema de permisos, `PermissionError`, o un error de decodificación de caracteres). En tal caso, también informamos y permitimos reintentar. (Dependiendo del caso, se podría manejar distintos tipos de error por separado, pero para mantenerlo simple cualquier otro error inesperado también provoca un nuevo intento).
- Si el archivo se abre correctamente, el código dentro del `with` se ejecuta: leemos todas las líneas con `archivo.readlines()`. Luego salimos del bloque `with` (lo que cierra el archivo automáticamente) y procedemos al `break` fuera de los except, que rompe el bucle porque ya tuvimos éxito.
- Después del bucle, estamos seguros de que `lineas` tiene las líneas del archivo (porque la única forma de salir del loop es habiendo ejecutado `break` tras una lectura exitosa). Entonces revisamos: si `lineas` no está vacío, imprimimos la primera línea (quitando el salto de línea final con `.strip()` para estética). Si `lineas` está vacío, significa que el archivo existía pero estaba vacío, así que informamos eso.

Este programa le permite al usuario intentar varios nombres hasta dar con uno válido. Si hubiéramos no usado el loop y dejado que el programa termine en caso de error, sería menos interactivo. Aquí aplicamos control de flujo usando excepciones para mejorar la experiencia de uso.

---

## Ejercicio 3: Excepción personalizada (contraseña segura)

**Enunciado:**

Imagina que estás creando un sistema de registro de usuarios y necesitas verificar la fortaleza de una contraseña. Escribe una función `verificar_contraseña(password)` que verifique si la contraseña cumple ciertos criterios, por ejemplo uno básico: al menos 8 caracteres. Si la contraseña es muy corta, la función debería lanzar una excepción personalizada llamada `ContraseñaCortaError`. Si la contraseña cumple con el criterio, la función puede devolver `True` (o simplemente no lanzar nada). Luego, escribe código que use dicha función dentro de un bloque `try/except` para probarla: pide al usuario una contraseña, la validas con `verificar_contraseña` y capturas la excepción `ContraseñaCortaError` para notificar al usuario en caso de que falle la validación. Si no hay excepción, felicita al usuario por una contraseña válida.

**Pista:**

Para crear la excepción personalizada, define una clase heredando de `Exception` con el nombre `ContraseñaCortaError`. Dentro de la función, puedes verificar la longitud con `len(password)`. Para lanzar la excepción usa `raise ContraseñaCortaError("tu mensaje")`. En el uso, rodea la llamada en `try`, y en `except` especifica `ContraseñaCortaError as e` para capturarla. Puedes también agregar más criterios (mayúsculas, números, etc.) si lo deseas, pero para el ejercicio nos centramos en la longitud.

**Solución propuesta:**

```python
# Definir la excepción personalizada
class ContraseñaCortaError(Exception):
    """Excepción lanzada cuando la contraseña es demasiado corta."""
    pass

# Función de verificación
def verificar_contraseña(password):
    if len(password) < 8:
        raise ContraseñaCortaError(f"tu contraseña solo tiene {len(password)} caracteres, requieren al menos 8 caracteres.")
    return True

# Programa principal
try:
    pwd = input("Introduce una contraseña: ")
    verificar_contraseña(pwd)
except ContraseñaCortaError as e:
    print("Contraseña no válida:", e)
else:
    print("Contraseña válida. ¡Registro exitoso!")
```

**Explicación:**

- Primero definimos la clase `ContraseñaCortaError` heredando de `Exception`. No tiene más contenido que un docstring explicativo, pero podríamos extenderla si quisiéramos (por ejemplo, almacenar la longitud requerida como atributo).
- La función `verificar_contraseña` chequea la longitud de la cadena `password`. Si es menor que 8, usamos `raise` para lanzar una nueva instancia de `ContraseñaCortaError` con un mensaje. Ese mensaje incluye la longitud actual para información.
- Si la contraseña tiene 8 o más caracteres, la función retorna `True` (en realidad podríamos no retornar nada específico y simplemente salir sin excepción, que equivale a éxito; aquí retornamos `True` explícitamente por claridad).
- En el programa principal, pedimos al usuario una contraseña. Luego llamamos a `verificar_contraseña(pwd)` dentro de un `try`.
- Si la contraseña es suficientemente larga, la función devuelve `True` y no lanza excepción. Pasamos entonces el bloque `try` exitosamente y mostramos "Contraseña válida".
- Si la contraseña es corta, la función lanza `ContraseñaCortaError`. Inmediatamente se interrumpe el flujo normal y saltamos al `except ContraseñaCortaError as e`. Allí, capturamos la excepción en la variable `e` y mostramos un mensaje de error al usuario, incluyendo el mensaje original de la excepción (que habíamos definido al hacer `raise`, indicando cuán corta era).
- Observa que estamos capturando específicamente `ContraseñaCortaError`. Si ocurriera alguna otra excepción no prevista (por ejemplo, un `TypeError` porque pasamos un objeto no `str` a `len`, caso poco probable aquí), no la capturamos, lo cual está bien porque no la anticipamos; se propagará fuera del `try` (en un programa real podríamos añadir un `except Exception` general para no romper, pero en este contexto de prueba nos enfocamos en nuestra excepción).
- El uso de excepciones personalizadas hace el código más claro: lanzamos `ContraseñaCortaError` cuando esa condición específica falla, en lugar de reutilizar, digamos, un `ValueError` genérico. Así, en el bloque que llama a la función, queda muy explícito qué estamos intentando capturar.