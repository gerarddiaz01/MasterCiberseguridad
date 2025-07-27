# JSON Web Tokens (JWT): Ejercicio Práctico de Implementación

## 1. Ejercicio Práctico: Generación y Validación de un JWT con PyJWT

El objetivo de esta actividad práctica es entender cómo funcionan, se generan y se validan los JSON Web Tokens, y cómo configurar claims específicos para controlar su expiración y validez.

### 1.1. Requisitos del Ejercicio

Debemos generar un JWT que cumpla las siguientes condiciones de validez:

  * **No será válido hasta 5 minutos después de su emisión.**
  * **No será válido después de 30 minutos desde su emisión.**

Además de estos claims de tiempo, exploraremos la inclusión de otros claims como la identificación del sujeto (`sub`) y la identificación del token (`jti`).

### 1.2. Paso a Paso para la Resolución del Ejercicio

Para la realización de este ejercicio, utilizaremos **Python** con la librería `PyJWT`, que es ampliamente documentada y fácil de usar.

#### Paso 1: Instalación de la Librería PyJWT

Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando para instalar `PyJWT`:

```bash
pip install pyjwt
```

  * **Sintaxis del Comando**:
      * `pip`: Es el gestor de paquetes estándar de Python, utilizado para instalar y administrar librerías.
      * `install`: Subcomando de `pip` para instalar un paquete.
      * `pyjwt`: Es el nombre del paquete de la librería que permite trabajar con JSON Web Tokens en Python.

#### Paso 2: Importar las Librerías Necesarias en Python

En tu script de Python, necesitarás importar el módulo `jwt` para trabajar con los tokens y el módulo `datetime` para gestionar las fechas y horas.

```python
import jwt
from datetime import datetime, timedelta, timezone
import uuid # Para generar un jti único
```

  * `jwt`: Proporciona las funciones para codificar (crear) y decodificar (validar) JWT.
  * `datetime`: Permite trabajar con objetos de fecha y hora, esenciales para los claims de tiempo (`iat`, `nbf`, `exp`).
  * `timedelta`: Utilizado para realizar operaciones con fechas, como sumar o restar minutos.
  * `timezone`: Para trabajar con zonas horarias y obtener la hora UTC (necesaria para `datetime.now(timezone.utc)`).
  * `uuid`: Utilizado para generar un identificador único universal para el claim `jti`.

#### Paso 3: Definir la Clave Secreta

La clave secreta es crucial para firmar el token. Debe ser **robusta y mantenerse en secreto** en el lado del servidor para garantizar la integridad del JWT.

```python
# Clave secreta para firmar el token (debe ser robusta y secreta)
SECRET_KEY = "TuClaveSecretaSuperSeguraParaJWTs"
```

#### Paso 4: Calcular los Claims de Tiempo

Los claims de tiempo (`iat`, `nbf`, `exp`) se basan en **Unix Timestamps** (segundos desde el 1 de enero de 1970 UTC).

```python
# Obtener el tiempo actual en UTC como objeto datetime
now = datetime.now(timezone.utc)

# iat (Issued At): Momento de emisión del token
# Convertir datetime a Unix timestamp
iat_timestamp = int(now.timestamp())
print(f"Issued At (iat): {iat_timestamp} ({now.isoformat()})")

# nbf (Not Before): Token no válido hasta 5 minutos después de su emisión
# Sumar 5 minutos al tiempo actual
nbf_time = now + timedelta(minutes=5)
nbf_timestamp = int(nbf_time.timestamp())
print(f"Not Before (nbf): {nbf_timestamp} ({nbf_time.isoformat()})")

# exp (Expiration Time): Token no válido después de 30 minutos desde su emisión
# Sumar 30 minutos al tiempo actual
exp_time = now + timedelta(minutes=30)
exp_timestamp = int(exp_time.timestamp())
print(f"Expiration Time (exp): {exp_timestamp} ({exp_time.isoformat()})")
```

  * `datetime.now(timezone.utc)`: Obtiene la fecha y hora actual en la Zona Horaria Universal Coordinada (UTC), que es el estándar para los timestamps de JWT.
  * `.timestamp()`: Convierte el objeto `datetime` a un Unix Timestamp (número de segundos desde la época). Se convierte a `int` para asegurar que sea un entero.
  * `timedelta(minutes=X)`: Crea un objeto de duración que se puede sumar o restar a `datetime` para calcular fechas futuras/pasadas.

#### Paso 5: Definir Otros Claims (Opcional pero recomendado)

Además de los claims de tiempo, incluimos `sub` y `jti` para identificar al sujeto y al token de manera única.

```python
# sub (Subject): Identificador del usuario o sujeto del token
subject_id = "user123"

# jti (JWT ID): Identificador único del token (para evitar repeticiones/listas negras)
# uuid.uuid4().hex genera una cadena hexadecimal única aleatoria
jwt_id = str(uuid.uuid4())
print(f"Subject (sub): {subject_id}")
print(f"JWT ID (jti): {jwt_id}")
```

#### Paso 6: Construir el Payload del JWT

El payload es un diccionario de Python que contiene todos los claims que deseamos incluir en el token.

```python
# Construir el payload con todos los claims
payload = {
    "sub": subject_id,
    "jti": jwt_id,
    "iat": iat_timestamp,
    "nbf": nbf_timestamp,
    "exp": exp_timestamp,
    # Otros claims opcionales, ej. "roles": ["admin", "user"]
}
print("\nPayload del token:")
print(payload)
```

#### Paso 7: Codificar (Generar) el JWT

Ahora usamos la función `jwt.encode()` para crear el JWT. Se le pasa el payload, la clave secreta y el algoritmo de firma.

```python
# Codificar el JWT
# Usamos HS256 (HMAC SHA-256) como algoritmo de firma simétrico
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("\nToken JWT codificado:")
print(encoded_jwt)
```

  * `jwt.encode()`: Esta función toma el diccionario `payload`, la `SECRET_KEY` y el `algorithm` de firma.
  * `algorithm="HS256"`: Indica que se usará el algoritmo HMAC con SHA-256 para firmar el token. Este es un algoritmo de firma simétrico.

#### Paso 8: Decodificar (Validar) el JWT

Para verificar que el token se generó correctamente y que la validación de los claims funciona, intentaremos decodificarlo.

```python
try:
    # Decodificar el JWT para verificarlo
    # Es crucial especificar el algoritmo usado para la decodificación
    decoded_payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("\nToken JWT decodificado (validación exitosa):")
    print(decoded_payload)
except jwt.ExpiredSignatureError:
    print("\n¡Error de validación!: El token ha expirado (ExpiredSignatureError).")
except jwt.InvalidTokenError as e:
    print(f"\n¡Error de validación!: Token inválido ({e}).")
except Exception as e:
    print(f"\nOcurrió un error inesperado durante la decodificación: {e}")
```

  * `jwt.decode()`: Esta función toma el `encoded_jwt`, la `SECRET_KEY` (la misma que se usó para codificar) y una lista de `algorithms` permitidos.
  * La función `decode()` automáticamente verifica la firma y los claims de tiempo (`exp`, `nbf`, `iat`) por nosotros.
  * **Manejo de Excepciones**: Se utilizan bloques `try-except` para capturar errores comunes de validación:
      * `jwt.ExpiredSignatureError`: Se lanza si el token ha expirado (el tiempo actual es mayor que `exp`).
      * `jwt.InvalidTokenError`: Se lanza por otras razones de invalidez, como una firma incorrecta o un token utilizado antes de `nbf`.

#### Paso 9: Demostrar la Validez y Expiración (`nbf` y `exp`)

Para ver los efectos de `nbf` y `exp`, podemos simular el tiempo o esperar. En un entorno real, la librería `PyJWT` se encargará de esto automáticamente al intentar decodificar el token.

**Demostración de `nbf` (Not Before)**:

Si intentamos decodificar un token cuya `nbf` está en el futuro, `PyJWT` lanzará una excepción `jwt.InvalidTokenError` (específicamente `BeforeFailsValidation`).

```python
# Simular un token que es válido 5 minutos en el futuro
future_nbf_payload = payload.copy()
# Ajustar iat y exp para que nbf sea lo único que falle al instante
future_nbf_payload["iat"] = int((now - timedelta(minutes=10)).timestamp()) # Asegurar que iat no falle
future_nbf_payload["exp"] = int((now + timedelta(minutes=60)).timestamp()) # Asegurar que exp no falle
future_nbf_payload["nbf"] = int((now + timedelta(seconds=10)).timestamp()) # 10 segundos en el futuro

print("\n--- Demostrando validación 'Not Before' (nbf) ---")
print(f"Token válido a partir de: {datetime.fromtimestamp(future_nbf_payload['nbf'], tz=timezone.utc).isoformat()}")

encoded_future_nbf_jwt = jwt.encode(future_nbf_payload, SECRET_KEY, algorithm="HS256")
try:
    decoded_future_nbf_payload = jwt.decode(encoded_future_nbf_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto no debería ocurrir si nbf está en el futuro inmediato)")
except jwt.InvalidTokenError as e:
    print(f"¡Error de validación esperado!: {e} (token no válido antes de su 'nbf').")

# Puedes esperar 10-15 segundos y volver a intentar decodificar para que pase.
# import time
# time.sleep(15)
# try:
#     decoded_future_nbf_payload = jwt.decode(encoded_future_nbf_jwt, SECRET_KEY, algorithms=["HS256"])
#     print("Token decodificado con éxito después de esperar el tiempo de nbf.")
# except Exception as e:
#     print(f"Error después de esperar: {e}")
```

**Demostración de `exp` (Expiration Time)**:

Si el tiempo actual es posterior a la marca de tiempo `exp` del token, `PyJWT` lanzará una excepción `jwt.ExpiredSignatureError`.

```python
# Simular un token que ya ha expirado
expired_payload = payload.copy()
expired_payload["iat"] = int((now - timedelta(minutes=40)).timestamp()) # Emitido hace 40 minutos
expired_payload["nbf"] = int((now - timedelta(minutes=35)).timestamp()) # Válido desde hace 35 minutos
expired_payload["exp"] = int((now - timedelta(minutes=10)).timestamp()) # Expiró hace 10 minutos

print("\n--- Demostrando validación 'Expiration Time' (exp) ---")
print(f"Token expiró en: {datetime.fromtimestamp(expired_payload['exp'], tz=timezone.utc).isoformat()}")

encoded_expired_jwt = jwt.encode(expired_payload, SECRET_KEY, algorithm="HS256")
try:
    decoded_expired_payload = jwt.decode(encoded_expired_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto no debería ocurrir si exp ya pasó).")
except jwt.ExpiredSignatureError:
    print("¡Error de validación esperado!: El token ha expirado (ExpiredSignatureError).")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

### 2.3. Código Completo del Ejercicio

Aquí tienes el código Python completo para el ejercicio, que puedes ejecutar para ver cómo se generan los JWT con los claims de tiempo y cómo se validan.

```python
import jwt
from datetime import datetime, timedelta, timezone
import uuid

# --- Paso 3: Definir la Clave Secreta ---
SECRET_KEY = "TuClaveSecretaSuperSeguraParaJWTs" # ¡En un entorno real, usa una clave más compleja y segura!

# --- Paso 4: Calcular los Claims de Tiempo ---
# Obtener el tiempo actual en UTC como objeto datetime
now = datetime.now(timezone.utc)

# iat (Issued At): Momento de emisión del token
iat_timestamp = int(now.timestamp())
print(f"Issued At (iat): {iat_timestamp} ({now.isoformat()})")

# nbf (Not Before): Token no válido hasta 5 minutos después de su emisión
nbf_time = now + timedelta(minutes=5)
nbf_timestamp = int(nbf_time.timestamp())
print(f"Not Before (nbf): {nbf_timestamp} ({nbf_time.isoformat()})")

# exp (Expiration Time): Token no válido después de 30 minutos desde su emisión
exp_time = now + timedelta(minutes=30)
exp_timestamp = int(exp_time.timestamp())
print(f"Expiration Time (exp): {exp_timestamp} ({exp_time.isoformat()})")

# --- Paso 5: Definir Otros Claims (Opcional pero recomendado) ---
# sub (Subject): Identificador del usuario o sujeto del token
subject_id = "usuario_ejemplo_123"

# jti (JWT ID): Identificador único del token (para evitar repeticiones/listas negras)
jwt_id = str(uuid.uuid4()) # Genera un UUID aleatorio
print(f"Subject (sub): {subject_id}")
print(f"JWT ID (jti): {jwt_id}")

# --- Paso 6: Construir el Payload del JWT ---
payload = {
    "sub": subject_id,
    "jti": jwt_id,
    "iat": iat_timestamp,
    "nbf": nbf_timestamp,
    "exp": exp_timestamp,
    # Puedes añadir otros claims personalizados aquí, ej: "roles": ["lector", "escritor"]
}
print("\nPayload del token:")
print(payload)

# --- Paso 7: Codificar (Generar) el JWT ---
# Usamos HS256 (HMAC SHA-256) como algoritmo de firma simétrico
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("\nToken JWT codificado:")
print(encoded_jwt)

# --- Paso 8: Decodificar (Validar) el JWT ---
# Este intento de decodificación debería fallar si nbf está en el futuro inmediato,
# o si exp ya pasó. En un flujo normal, este paso se realizaría cuando el token es válido.
print("\n--- Intentando decodificar el token generado ---")
try:
    # La librería PyJWT valida automáticamente los claims de tiempo
    decoded_payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token JWT decodificado (validación exitosa):")
    print(decoded_payload)
except jwt.ExpiredSignatureError:
    print("¡Error de validación!: El token ha expirado (ExpiredSignatureError).")
except jwt.InvalidTokenError as e:
    print(f"¡Error de validación!: Token inválido ({e}). Esto puede deberse a 'nbf' en el futuro.")
except Exception as e:
    print(f"Ocurrió un error inesperado durante la decodificación: {e}")

# --- Demostración adicional de validación 'Not Before' (nbf) ---
print("\n--- Demostrando validación 'Not Before' (nbf) ---")
# Creamos un token que será válido 10 segundos en el futuro para forzar el error de nbf
future_nbf_payload = payload.copy()
future_nbf_payload["iat"] = int((now).timestamp()) # Tiempo actual
future_nbf_payload["exp"] = int((now + timedelta(minutes=1)).timestamp()) # Expiración en 1 minuto (para que no falle por exp)
future_nbf_payload["nbf"] = int((now + timedelta(seconds=10)).timestamp()) # Válido 10 segundos en el futuro

print(f"Token válido a partir de: {datetime.fromtimestamp(future_nbf_payload['nbf'], tz=timezone.utc).isoformat()}")
encoded_future_nbf_jwt = jwt.encode(future_nbf_payload, SECRET_KEY, algorithm="HS256")

try:
    decoded_future_nbf_payload = jwt.decode(encoded_future_nbf_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto NO debería ocurrir si nbf está en el futuro inmediato).")
except jwt.InvalidTokenError as e:
    print(f"¡Error de validación esperado!: {e} (token no válido antes de su 'nbf').")

# Si esperas unos segundos (ej. time.sleep(15)) y lo vuelves a ejecutar, debería pasar la validación.

# --- Demostración adicional de validación 'Expiration Time' (exp) ---
print("\n--- Demostrando validación 'Expiration Time' (exp) ---")
# Creamos un token que ya ha expirado
expired_payload = payload.copy()
expired_payload["iat"] = int((now - timedelta(minutes=40)).timestamp()) # Emitido hace 40 minutos
expired_payload["nbf"] = int((now - timedelta(minutes=35)).timestamp()) # Válido desde hace 35 minutos
expired_payload["exp"] = int((now - timedelta(minutes=10)).timestamp()) # Expiró hace 10 minutos

print(f"Token expiró en: {datetime.fromtimestamp(expired_payload['exp'], tz=timezone.utc).isoformat()}")
encoded_expired_jwt = jwt.encode(expired_payload, SECRET_KEY, algorithm="HS256")

try:
    decoded_expired_payload = jwt.decode(encoded_expired_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto NO debería ocurrir si exp ya pasó).")
except jwt.ExpiredSignatureError:
    print("¡Error de validación esperado!: El token ha expirado (ExpiredSignatureError).")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

Este ejercicio te permite comprender la importancia de cada claim en la seguridad y funcionalidad de los JWT, y cómo las librerías los utilizan para la validación automática.