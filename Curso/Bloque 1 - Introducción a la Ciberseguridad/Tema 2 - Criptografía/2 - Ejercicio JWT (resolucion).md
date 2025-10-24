# JSON Web Tokens (JWT): Creación, Gestión de Claims y Manejo de Errores en Python

En esta sesión, exploraremos en detalle la creación de **JSON Web Tokens (JWT)**, la importancia de sus "claims" (declaraciones o piezas de información), cómo configurarlos para controlar la seguridad de nuestros datos y cómo manejar los errores comunes en el código Python.

## 1\. Claims en JWT: La Información Esencial

Como recordatorio, los "claims" son las piezas de información encapsuladas dentro de un JWT. Son cruciales para representar atributos del usuario, roles, permisos y cualquier otro dato relevante que una aplicación necesite para personalizar la experiencia o autorizar el acceso a recursos. Al estar protegidos por una firma digital, los claims aseguran que la información es confiable y no ha sido alterada.

Existen tres tipos de claims:

  * **Claims Registrados**: Estándares definidos en la especificación JWT (como `iss`, `sub`, `aud`, `iat`, `exp`, `nbf`, `jti`).
  * **Claims Públicos**: Usos comunes pero no estándar (ej. nombre, email).
  * **Claims Privados**: Personalizados para una aplicación específica.

Para la seguridad y el control de la validez, los **claims registrados** son fundamentales.

### Claims Registrados Clave para el Control de Tiempo

  * **`iat` (Issued At - Emitido En)**: Indica el momento en que el token fue generado. Es un **Unix Timestamp** (segundos desde la época Unix UTC). Esencial para verificar la "frescura" del token.
  * **`nbf` (Not Before - No Válido Antes De)**: Indica el momento a partir del cual el token debe considerarse válido. También es un Unix Timestamp. Permite que un token no sea procesado si se recibe antes de este tiempo.
  * **`exp` (Expiration Time - Tiempo de Expiración)**: Indica el momento en que la validez del token expira. Es un Unix Timestamp. Limita la vida útil del token y es crucial para prevenir el uso indebido después de un tiempo determinado.
  * **`sub` (Subject - Sujeto)**: Identifica al usuario o entidad a la que se refiere el token. Puede ser un ID único de usuario.
  * **`jti` (JWT ID - ID de JWT)**: Proporciona un identificador único para el token. Útil para revocar tokens o evitar su reutilización (ataques de *replay*).

## 2\. Resolución del Ejercicio: Creación de un JWT con Requisitos de Tiempo

El ejercicio propuesto nos desafía a crear un JWT en Python con la librería `PyJWT` que cumpla las siguientes condiciones de validez temporal:

1.  **El token no será válido hasta 5 minutos después de su emisión.**
2.  **El token no será válido después de 30 minutos desde su emisión.**

Esto implica que el token tendrá una ventana de validez efectiva de 25 minutos, comenzando 5 minutos después de su creación. También exploraremos la inclusión de los claims `sub` y `jti`.

### 2.1. Preparación del Entorno: Instalación de PyJWT

Antes de escribir el código, debemos asegurarnos de tener la librería `PyJWT` instalada. Abre tu terminal (o símbolo del sistema) y ejecuta el siguiente comando:

```bash
pip install pyjwt
```

  * **`pip`**: Es el gestor de paquetes estándar de Python.
  * **`install`**: Subcomando para instalar librerías.
  * **`pyjwt`**: Es el nombre del paquete de la librería que nos permite trabajar con JWT en Python.

Si necesitas trabajar con algoritmos asimétricos (como **RSA** o **ECDSA**), puedes instalar las dependencias criptográficas adicionales con: `pip install pyjwt[crypto]`. Para este ejercicio, con `pyjwt` básico es suficiente.

### 2.2. Implementación del Código Python Paso a Paso

Crearemos un script de Python que genere el JWT, configure los claims de tiempo y demuestre su validación, incluyendo el manejo de errores.

#### Paso 1: Importar Módulos Necesarios

Necesitaremos `jwt` para la creación y validación del token, `datetime` y `timedelta` para manejar las fechas y tiempos, y `uuid` para generar identificadores únicos.

```python
import jwt
from datetime import datetime, timedelta, timezone
import uuid
import time # Usado para simular el paso del tiempo
```

  * `jwt`: La librería principal para JWT.
  * `datetime`, `timedelta`, `timezone`: Módulos nativos de Python para la manipulación de fechas y tiempos. Es crucial usar `timezone.utc` para garantizar que los timestamps sean UTC, como lo requiere la especificación JWT.
  * `uuid`: Genera identificadores únicos universales, perfectos para el claim `jti`.
  * `time`: Permite pausar la ejecución del script para simular el paso del tiempo, útil para probar los claims `nbf` y `exp`.

#### Paso 2: Definir la Clave Secreta

Esta es la clave que el servidor usa para firmar y verificar el token. Debe ser una cadena de caracteres robusta y, en un entorno de producción, debe gestionarse de forma segura (nunca codificada directamente en el código).

```python
SECRET_KEY = "mi_super_clave_secreta_y_segura_para_jwt"
```

#### Paso 3: Calcular los Claims de Tiempo (`iat`, `nbf`, `exp`)

Calculamos los *timestamps* Unix para los claims `iat`, `nbf` y `exp` según los requisitos del ejercicio.

```python
# Obtener el tiempo actual en UTC
now = datetime.now(timezone.utc)

# Claim 'iat': Tiempo de emisión (Issued At)
iat_timestamp = int(now.timestamp())

# Claim 'nbf': No válido antes de 5 minutos desde la emisión
nbf_time = now + timedelta(minutes=5)
nbf_timestamp = int(nbf_time.timestamp())

# Claim 'exp': Expira 30 minutos después de la emisión
exp_time = now + timedelta(minutes=30)
exp_timestamp = int(exp_time.timestamp())

print(f"Hora actual (UTC): {now}")
print(f"iat (Emitido en): {datetime.fromtimestamp(iat_timestamp, tz=timezone.utc)}")
print(f"nbf (Válido a partir de): {datetime.fromtimestamp(nbf_timestamp, tz=timezone.utc)}")
print(f"exp (Expira en): {datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)}")
```

  * `datetime.now(timezone.utc)`: Obtiene la fecha y hora actual en el formato `datetime` y en la zona horaria UTC.
  * `int(now.timestamp())`: Convierte el objeto `datetime` a un Unix Timestamp (número de segundos desde el 1 de enero de 1970 UTC), y lo convierte a entero.
  * `timedelta(minutes=X)`: Objeto que representa una duración, permitiendo sumar o restar minutos a un objeto `datetime`.

#### Paso 4: Definir Otros Claims (`sub`, `jti` y opcionales)

Además de los claims de tiempo, incluimos el sujeto y un identificador único para el token.

```python
# Claim 'sub': Sujeto (identificador de usuario)
user_id = "usuario_ejemplo_123"

# Claim 'jti': ID del JWT (identificador único para este token específico)
token_id = str(uuid.uuid4()) # Genera un UUID aleatorio y lo convierte a cadena

# Otros claims opcionales (ejemplo)
custom_roles = ["admin", "developer"]
issuer_url = "https://tuaplicacion.com"
audience = "api.tuaplicacion.com"
```

  * `uuid.uuid4()`: Genera un UUID (Universally Unique Identifier) de versión 4, que es un número aleatorio.
  * `str(...)`: Convierte el objeto UUID a una cadena de texto.

#### Paso 5: Construir el Payload del JWT

Todos los claims se agrupan en un diccionario de Python, que será el `payload` del JWT.

```python
# Construir el payload
payload = {
    "sub": user_id,
    "jti": token_id,
    "iat": iat_timestamp,
    "nbf": nbf_timestamp,
    "exp": exp_timestamp,
    "roles": custom_roles, # Claim personalizado
    "iss": issuer_url, # Claim 'iss'
    "aud": audience # Claim 'aud'
}

print("\nPayload del JWT a codificar:")
print(payload)
```

#### Paso 6: Codificar (Generar) el JWT

Se utiliza la función `jwt.encode()` para generar la cadena JWT final.

```python
# Codificar el JWT usando HS256 (HMAC SHA-256)
# HS256 es un algoritmo de firma simétrico, por lo que usa la misma SECRET_KEY para firmar y verificar.
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("\nJWT Generado:")
print(encoded_jwt)
```

  * `jwt.encode(payload, SECRET_KEY, algorithm="HS256")`:
      * `payload`: El diccionario de claims.
      * `SECRET_KEY`: La clave secreta para la firma.
      * `algorithm="HS256"`: Especifica el algoritmo de firma. `HS256` es un algoritmo de *Message Authentication Code* (MAC) que utiliza una clave secreta para firmar el token, asegurando su integridad.

#### Paso 7: Decodificar (Validar) el JWT y Manejo de Errores

La función `jwt.decode()` es clave para la validación. Automáticamente verifica la firma y los claims de tiempo. Es crucial usar bloques `try-except` para manejar las posibles excepciones.

```python
# --- Prueba de decodificación inmediata (debería fallar por nbf) ---
print("\n--- Intentando decodificar el token inmediatamente (debería fallar por 'nbf') ---")
try:
    decoded_payload_nbf_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Decodificación exitosa (¡inesperado!). Payload:")
    print(decoded_payload_nbf_test)
except jwt.InvalidTokenError as e:
    print(f"¡Error de validación esperado por 'nbf'! El token aún no es válido: {e}")
except jwt.ExpiredSignatureError:
    print("¡Error inesperado de expiración!")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Simular el paso del tiempo para que el token sea válido (pasar 5 minutos) ---
print("\n--- Esperando 5 minutos para que el token sea válido ('nbf') ---")
time.sleep(301) # Esperamos 5 minutos y 1 segundo (300 segundos + 1)

# --- Prueba de decodificación después de 'nbf' ---
print("\n--- Intentando decodificar el token después de 5 minutos (debería ser exitoso) ---")
try:
    decoded_payload_valid_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Decodificación exitosa después de 'nbf' cumplido. Payload:")
    print(decoded_payload_valid_test)
except jwt.InvalidTokenError as e:
    print(f"¡Error inesperado!: Token inválido: {e}")
except jwt.ExpiredSignatureError:
    print("¡Error inesperado!: El token ha expirado prematuramente.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Simular el paso del tiempo hasta la expiración (pasar 30 minutos desde el inicio) ---
print("\n--- Esperando el tiempo restante hasta la expiración ('exp') ---")
# Calculamos cuánto falta desde los 5 minutos pasados hasta los 30 minutos totales
remaining_time_to_expire = (exp_time - (now + timedelta(minutes=5))).total_seconds()
if remaining_time_to_expire > 0:
    time.sleep(remaining_time_to_expire + 1) # Esperamos el tiempo restante + 1 segundo
else:
    print("El token ya expiró desde la simulación inicial de nbf.")

# --- Prueba de decodificación después de 'exp' ---
print("\n--- Intentando decodificar el token después de 30 minutos (debería fallar por 'exp') ---")
try:
    decoded_payload_exp_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Decodificación exitosa (¡inesperado!). Payload:")
    print(decoded_payload_exp_test)
except jwt.ExpiredSignatureError:
    print("¡Error de validación esperado por 'exp'!: El token ha expirado (ExpiredSignatureError).")
except jwt.InvalidTokenError as e:
    print(f"¡Error inesperado!: Token inválido: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Demostración de Invalid Signature (token modificado o clave incorrecta) ---
print("\n--- Demostrando 'Invalid Signature' ---")
tampered_jwt = encoded_jwt + "X" # Modificamos el token para romper la firma

try:
    decoded_tampered_payload = jwt.decode(tampered_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Decodificación exitosa (¡inesperado!):")
    print(decoded_tampered_payload)
except jwt.InvalidSignatureError:
    print("¡Error de validación esperado!: La firma es inválida (InvalidSignatureError). El token fue manipulado.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

  * `jwt.decode(token, key, algorithms=[...])`: Esta función es central.
      * `token`: La cadena JWT codificada que queremos validar.
      * `key`: La clave secreta (para algoritmos simétricos) o la clave pública (para asimétricos) necesaria para verificar la firma.
      * `algorithms`: Una lista de algoritmos de firma que la función *debe* aceptar. Es crucial especificarlo por seguridad; de lo contrario, podría haber ataques de *algoritmo de ninguno* (`alg: "none"`).
  * **Manejo de Excepciones**:
      * `jwt.InvalidTokenError`: Una excepción genérica para problemas de validación del token. Cuando el `nbf` no se ha cumplido, `PyJWT` lanza un `InvalidTokenError` con un mensaje específico como "The token is not yet valid".
      * `jwt.ExpiredSignatureError`: Esta excepción se lanza específicamente cuando el claim `exp` del token indica que ya ha expirado.
      * `jwt.InvalidSignatureError`: Se lanza cuando la firma del token no coincide, lo que indica que el token fue manipulado o que la clave secreta utilizada para la verificación es incorrecta.
      * Usar `try-except` permite que nuestra aplicación reaccione de forma controlada a estas situaciones, por ejemplo, devolviendo un error 401 Unauthorized en una API.
  * `time.sleep(segundos)`: Pausa la ejecución del script por la cantidad de segundos especificada. Se usa aquí para simular el paso del tiempo y probar los claims `nbf` y `exp` en diferentes momentos.

### 2.3. Código Final Consolidado del Ejercicio

```python
import jwt
from datetime import datetime, timedelta, timezone
import uuid
import time

# --- 1. Definir la Clave Secreta ---
# ¡IMPORTANTE: En un entorno de producción, esta clave debe ser compleja,
# generada de forma segura y almacenada en un lugar muy protegido (ej. variables de entorno, Key Vault)!
SECRET_KEY = "TuClaveSecretaSuperSeguraParaJWTs"

# --- 2. Calcular los Claims de Tiempo ---
# Obtener el tiempo actual en UTC. La especificación JWT usa Unix Timestamps en UTC.
now = datetime.now(timezone.utc)

# Claim 'iat': Tiempo de emisión del token (Issued At)
# Representa el momento exacto en que el token fue creado.
iat_timestamp = int(now.timestamp())

# Claim 'nbf': Token no válido antes de 5 minutos desde su emisión (Not Before)
# Esto significa que el token será rechazado si se presenta antes de este tiempo.
nbf_time = now + timedelta(minutes=5)
nbf_timestamp = int(nbf_time.timestamp())

# Claim 'exp': Token no válido después de 30 minutos desde su emisión (Expiration Time)
# Esto define la vida útil máxima del token.
exp_time = now + timedelta(minutes=30)
exp_timestamp = int(exp_time.timestamp())

print("--- Tiempos de los Claims ---")
print(f"Hora actual (UTC): {now.isoformat()}")
print(f"iat (Emitido en): {datetime.fromtimestamp(iat_timestamp, tz=timezone.utc).isoformat()}")
print(f"nbf (Válido a partir de): {datetime.fromtimestamp(nbf_timestamp, tz=timezone.utc).isoformat()}")
print(f"exp (Expira en): {datetime.fromtimestamp(exp_timestamp, tz=timezone.utc).isoformat()}")

# --- 3. Definir Otros Claims (sub y jti) ---
# 'sub': Identificador del sujeto (generalmente un ID de usuario único).
user_id = "usuario_ejemplo_ciberseguridad_456"

# 'jti': Identificador único del JWT (para seguimiento o revocación).
token_id = str(uuid.uuid4())

# Claims personalizados adicionales, si es necesario
custom_roles = ["estudiante", "observador"]
issuer_url = "https://ciberseguridad.com"
audience_api = "https://api.ciberseguridad.com"

# --- 4. Construir el Payload del JWT ---
# El payload es un diccionario Python que contiene todos los claims.
payload = {
    "sub": user_id,
    "jti": token_id,
    "iat": iat_timestamp,
    "nbf": nbf_timestamp,
    "exp": exp_timestamp,
    "roles": custom_roles, # Ejemplo de claim personalizado
    "iss": issuer_url,     # Claim 'issuer'
    "aud": audience_api    # Claim 'audience'
}

print("\n--- Payload del JWT ---")
print(payload)

# --- 5. Codificar (Generar) el JWT ---
# Se utiliza el algoritmo HS256 (HMAC-SHA256) para firmar el token.
# HS256 es un algoritmo de firma simétrico que usa la SECRET_KEY.
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("\n--- JWT Generado ---")
print(encoded_jwt)

# --- 6. Demostración de Validación y Manejo de Errores ---

# --- Prueba 1: Decodificación inmediata (Debería fallar por 'nbf') ---
print("\n--- Prueba 1: Intentando decodificar inmediatamente (debería fallar por 'nbf') ---")
try:
    # La librería PyJWT valida automáticamente 'nbf', 'exp' y la firma.
    decoded_payload_nbf_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("¡ERROR INESPERADO! Decodificación exitosa antes de nbf. Payload:")
    print(decoded_payload_nbf_test)
except jwt.InvalidTokenError as e:
    # Captura jwt.InvalidTokenError que incluye "The token is not yet valid"
    print(f"ÉXITO: Error de validación esperado por 'nbf'. El token aún no es válido: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# --- Prueba 2: Esperar 5 minutos + 1 segundo para que 'nbf' sea válido ---
print("\n--- Prueba 2: Esperando 5 minutos para que el token sea válido ('nbf')... ---")
time.sleep(301) # Pausa la ejecución por 301 segundos (5 minutos y 1 segundo)

# --- Prueba 3: Intentar decodificar después de que 'nbf' sea válido (debería ser exitoso) ---
print("\n--- Prueba 3: Intentando decodificar después de 'nbf' cumplido (debería ser exitoso) ---")
try:
    decoded_payload_valid_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("ÉXITO: Decodificación exitosa. Token válido. Payload:")
    print(decoded_payload_valid_test)
except jwt.InvalidTokenError as e:
    print(f"¡ERROR INESPERADO! Token inválido: {e}")
except jwt.ExpiredSignatureError:
    print("¡ERROR INESPERADO! El token ha expirado prematuramente.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Prueba 4: Esperar el tiempo restante hasta la expiración ('exp') ---
print("\n--- Prueba 4: Esperando el tiempo restante hasta la expiración ('exp')... ---")
# Calculamos el tiempo que queda desde que 'nbf' fue válido hasta 'exp', más 1 segundo extra.
# Si la ejecución de las pruebas anteriores tomó más tiempo, ajustamos esto.
remaining_time_to_expire = (exp_time - datetime.now(timezone.utc)).total_seconds()
if remaining_time_to_expire > 0:
    time.sleep(remaining_time_to_expire + 1)
else:
    print("El token ya expiró antes de esta prueba (simulación previa muy larga).")

# --- Prueba 5: Intentar decodificar después de la expiración (debería fallar por 'exp') ---
print("\n--- Prueba 5: Intentando decodificar después de la expiración (debería fallar por 'exp') ---")
try:
    decoded_payload_exp_test = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("¡ERROR INESPERADO! Decodificación exitosa después de la expiración. Payload:")
    print(decoded_payload_exp_test)
except jwt.ExpiredSignatureError:
    print("ÉXITO: Error de validación esperado. El token ha expirado (ExpiredSignatureError).")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# --- Prueba 6: Demostración de 'Invalid Signature' (token manipulado o clave incorrecta) ---
print("\n--- Prueba 6: Demostrando 'Invalid Signature' ---")
# Creamos un token que parece válido pero está alterado (ej. añadimos un carácter al final)
tampered_jwt = encoded_jwt + "X"

try:
    decoded_tampered_payload = jwt.decode(tampered_jwt, SECRET_KEY, algorithms=["HS256"])
    print("¡ERROR INESPERADO! Decodificación exitosa de token manipulado.")
    print(decoded_tampered_payload)
except jwt.InvalidSignatureError:
    # Esta excepción se lanza cuando la firma no coincide.
    print("ÉXITO: Error de validación esperado. La firma es inválida (InvalidSignatureError). El token fue manipulado.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

### 2.4. Análisis del Código y su Importancia para la Seguridad

El código anterior demuestra cómo los JWT, junto con la correcta configuración de los claims y un manejo de errores robusto, son fundamentales para la seguridad:

  * **Control Preciso de la Vida Útil del Token**: Los claims `iat`, `nbf` y `exp` permiten establecer un periodo de validez exacto para el token. Esto reduce la ventana de oportunidad para ataques si un token es interceptado.
      * El `nbf` (Not Before) evita que un token sea usado antes de tiempo, útil en escenarios donde un token se emite para un evento futuro.
      * El `exp` (Expiration Time) garantiza que un token no pueda ser usado indefinidamente, forzando la reautenticación o renovación periódica y limitando el daño de un token comprometido.
  * **Integridad y Autenticidad**: La firma del token (generada con la `SECRET_KEY` y verificada por `jwt.decode()`) es la garantía principal de que el token no ha sido manipulado. Si un atacante intenta alterar el `payload` (los datos del usuario, roles, etc.), la firma se romperá, y `jwt.decode()` lanzará una `InvalidSignatureError`.
  * **Identificación y Trazabilidad**: Claims como `sub` y `jti` son cruciales.
      * `sub` vincula el token a un usuario específico.
      * `jti` proporciona un identificador único que puede usarse para:
          * Prevenir ataques de *replay* (reutilización de un token).
          * Mantener listas negras de tokens revocados (ej. si un usuario cierra sesión o se detecta un compromiso, se puede invalidar un token específico antes de su `exp`).
  * **Robustez de la Aplicación**: Los bloques `try-except` alrededor de la decodificación de JWT son vitales en aplicaciones reales. Permiten a la aplicación manejar de forma controlada escenarios como tokens expirados, inválidos o manipulados, en lugar de crashear o procesar datos maliciosos. Esto es esencial para la **resiliencia** y la seguridad de los servicios.
  * **Uso de Estándares**: La librería `PyJWT` implementa el estándar **RFC 7519**, asegurando la interoperabilidad con otros sistemas que también utilicen JWT.

En resumen, la configuración meticulosa de los claims, especialmente los de tiempo, y la implementación de un manejo de errores adecuado al decodificar y validar los JWT, son pilares fundamentales para construir sistemas de autenticación y autorización seguros y robustos en el desarrollo web y de APIs.