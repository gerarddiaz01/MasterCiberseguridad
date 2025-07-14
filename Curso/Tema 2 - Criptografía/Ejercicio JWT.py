from datetime import datetime, timedelta, timezone
import uuid  # Para generar un id único
import jwt

# 1- Definir la clave secreta para firmar el token (debe ser robusta y secreta)
SECRET_KEY = "gerard1234gerard1234"

# 2- Calcular los Claims de Tiempo
# Los claims de tiempo (iat, nbf y exp) se basan en Unix Timestamps

# Obtener el tiempo actual en UTC como objeto datetime
now = datetime.now(timezone.utc)

# iat (Issued At): Momento de emisión del token
# Convertir datetime a Unix timestamp (usamos isoformat para obtener las fechas en un formato legible)
iat_timestamp = int(now.timestamp())
print(f"Issued At (iat): {iat_timestamp} ({now.isoformat()})")

# nbf (Not Before): Token no válido hasta 5 minutos después de su emisión
# Sumar 5 minutos al tiempo actual
nbf_time = now + timedelta(minutes=5)
nbf_timestamp = int(nbf_time.timestamp())
print(f"Not Before (nbf): {nbf_timestamp} ({nbf_time.isoformat()})")

# exp (Expiration Time): Token no válido después de 30 minutos después de su emisión
# Sumar 30 minutos al tiempo actual
exp_time = now + timedelta(minutes=30)
exp_timestamp = int(exp_time.timestamp())
print(f"Expiration Date (exp): {exp_timestamp} ({exp_time.isoformat()})")

""" 
datetime.now(timezone.utc): Obtiene la fecha y hora actual en la Zona Horaria Universal Coordinada (UTC), que es el estándar para los timestamps de JWT.
.timestamp(): Convierte el objeto datetime a un Unix Timestamp (número de segundos desde la época). Se convierte a int para asegurar que sea un entero.
timedelta(minutes=X): Crea un objeto de duración que se puede sumar o restar a datetime para calcular fechas futuras/pasadas. 
"""

# 3- Definir Otros Claims
# Además de los claims de tiempo, incluimos sub y jti para identificar al sujeto y al token de manera única

# sub (Subject): Identificador del usuario o sujeto del token
subject_id = "user123"

# jti (JWT ID): Identificador único del token (para evitar repeticiones/listas negras), OJO PyJWT no soporta los claims jti OJO!!
# uuid.uuid4().hex genera una cadena hexadecimal única aleatoria
jwt_id = str(uuid.uuid4())

print(f"Subject (sub): {subject_id}")
print(f"JWT ID (jti): {jwt_id}")

# 4- Construir el payload del JWT
# El payload es un diccionario de Python que contiene todos los claims que deseamos incluir en el token

payload = {
    "sub": subject_id,
    "jti": jwt_id,
    "iat": iat_timestamp,
    "nbf": nbf_timestamp,
    "exp": exp_timestamp,
}

print("\nPayload del token:")
print(payload)

# 5- Codificar (Generar) el JWT
# Ahora usamos la función jwt.encode() para crear el JWT, se le pasa como argumentos el payload, la clave secreta y el algoritmo de firma

# Usamos HS256 (HMAC SHA-256) como algoritmo de firma simétrico
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# 6- Decodificar (Validar) el JWT
# Para verificar que el token se generó correctamente y que la validación de los claims funciona, intentaremos decodificarlo

try:
    # Es crucial especificar el algoritmo usado para la decodificación
    decoded_payload = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("\nToken JWT decodificado (validación exitosa)")
    print(decoded_payload)
except jwt.ExpiredSignatureError:
    print("\n¡Error en la validación!: El token ha expirado (ExpiredSignatureError).")
except jwt.InvalidTokenError as e:
    print(f"\n¡Error de validación!: Token inválido ({e}).")
except Exception as e:
    print(f"\nOcurrió un error inesperado durante la decodificación: {e}")

"""
jwt.decode(): Esta función toma el encoded_jwt, la SECRET_KEY (la misma que se usó para codificar) y una lista de algorithms permitidos.
La función decode() automáticamente verifica la firma y los claims de tiempo (exp, nbf, iat) por nosotros.
Manejo de Excepciones: Se utilizan bloques try-except para capturar errores comunes de validación:
    jwt.ExpiredSignatureError: Se lanza si el token ha expirado (el tiempo actual es mayor que exp).
    jwt.InvalidTokenError: Se lanza por otras razones de invalidez, como una firma incorrecta o un token utilizado antes de nbf. 
"""

# 7- Demostrar la validez y expiración (nbf, exp)
# Para ver los efectos de nbf y exp, podemos simular el tiempo o esperar. EN un entorno real, la librería PyJWT se encargará de esto automáticamente al intentar decodificar el token

# Demostración de nbf
# Si intentamos decodificar un token cuya nbf está en el futuro, PyJWT lanzará una excepción jwt.InvalidTokenError (específicamente BeforeFailsValidation)

# Simular un token que es válido 5 minutos en el futuro
future_nbf_payload = payload.copy()
# Ajustar iat y exp para que nbf sea lo único que falle al instante
future_nbf_payload["iat"] = int(
    (now - timedelta(minutes=10)).timestamp())  # Asegurar que iat no falle
future_nbf_payload["exp"] = int(
    (now + timedelta(minutes=60)).timestamp())  # Asegurar que exp no falle
future_nbf_payload["nbf"] = int(
    (now + timedelta(seconds=10)).timestamp())  # 10 segundos en el futuro

print("\n--- Demostrando validación 'Not Before' (nbf) ---")
print(
    f"Token válido a partir de: {datetime.fromtimestamp(future_nbf_payload["nbf"], tz=timezone.utc).isoformat()}")

encoded_future_nbf_jwt = jwt.encode(
    future_nbf_payload, SECRET_KEY, algorithm="HS256")
try:
    decoded_future_nbf_payload = jwt.decode(
        encoded_future_nbf_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto no debería ocurrir si nbf está en el futuro inmediato)")
except jwt.InvalidTokenError as e:
    print(
        f"¡Error de validación esperado!: {e} (token no válido antes de su 'nbf').")

""" Puedes esperar 10-15 segundos y volver a intentar decodificar para que pase.
import time
time.sleep(15)
try:
    decoded_future_nbf_payload = jwt.decode(encoded_future_nbf_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito después de esperar el tiempo de nbf.")
except Exception as e:
    print(f"Error después de esperar: {e}") """

# Demostración de exp (Expiration Time):
# Si el tiempo actual es posterior a la marca de tiempo exp del token, PyJWT lanzará una excepción jwt.ExpiredSignatureError

# Simular un token que ya ha expirado
expired_payload = payload.copy()
expired_payload["iat"] = int(
    (now - timedelta(minutes=40)).timestamp())  # Emitido hace 40 minutos
# Válido desde hace 35 minutos
expired_payload["nbf"] = int((now - timedelta(minutes=35)).timestamp())
expired_payload["exp"] = int(
    (now - timedelta(minutes=10)).timestamp())  # Expiró hace 10 minutos

print("\n--- Demostrando validación 'Expiration Time' (exp) ---")
print(
    f"Token expiró en: {datetime.fromtimestamp(expired_payload['exp'], tz=timezone.utc).isoformat()}")

encoded_expired_jwt = jwt.encode(
    expired_payload, SECRET_KEY, algorithm="HS256")
try:
    decoded_expired_payload = jwt.decode(
        encoded_expired_jwt, SECRET_KEY, algorithms=["HS256"])
    print("Token decodificado con éxito (esto no debería ocurrir si exp ya pasó).")
except jwt.ExpiredSignatureError:
    print("¡Error de validación esperado!: El token ha expirado (ExpiredSignatureError).")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
