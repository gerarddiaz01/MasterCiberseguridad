from datetime import datetime, timedelta, timezone
import uuid
import time
import jwt

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
print(
    f"iat (Emitido en): {datetime.fromtimestamp(iat_timestamp, tz=timezone.utc).isoformat()}")
print(
    f"nbf (Válido a partir de): {datetime.fromtimestamp(nbf_timestamp, tz=timezone.utc).isoformat()}")
print(
    f"exp (Expira en): {datetime.fromtimestamp(exp_timestamp, tz=timezone.utc).isoformat()}")

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
    "roles": custom_roles,  # Ejemplo de claim personalizado
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
    decoded_payload_nbf_test = jwt.decode(
        encoded_jwt, SECRET_KEY, algorithms=["HS256"])
    print("¡ERROR INESPERADO! Decodificación exitosa antes de nbf. Payload:")
    print(decoded_payload_nbf_test)
except jwt.InvalidTokenError as e:
    # Captura jwt.InvalidTokenError que incluye "The token is not yet valid"
    print(
        f"ÉXITO: Error de validación esperado por 'nbf'. El token aún no es válido: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# --- Prueba 2: Esperar 5 minutos + 1 segundo para que 'nbf' sea válido ---
print("\n--- Prueba 2: Esperando 5 minutos para que el token sea válido ('nbf')... ---")
time.sleep(301)  # Pausa la ejecución por 301 segundos (5 minutos y 1 segundo)

# --- Prueba 3: Intentar decodificar después de que 'nbf' sea válido (debería ser exitoso) ---
print("\n--- Prueba 3: Intentando decodificar después de 'nbf' cumplido (debería ser exitoso) ---")
try:
    decoded_payload_valid_test = jwt.decode(
        encoded_jwt, SECRET_KEY, algorithms=["HS256"])
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
remaining_time_to_expire = (
    exp_time - datetime.now(timezone.utc)).total_seconds()
if remaining_time_to_expire > 0:
    time.sleep(remaining_time_to_expire + 1)
else:
    print("El token ya expiró antes de esta prueba (simulación previa muy larga).")

# --- Prueba 5: Intentar decodificar después de la expiración (debería fallar por 'exp') ---
print("\n--- Prueba 5: Intentando decodificar después de la expiración (debería fallar por 'exp') ---")
try:
    decoded_payload_exp_test = jwt.decode(
        encoded_jwt, SECRET_KEY, algorithms=["HS256"])
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
    decoded_tampered_payload = jwt.decode(
        tampered_jwt, SECRET_KEY, algorithms=["HS256"])
    print("¡ERROR INESPERADO! Decodificación exitosa de token manipulado.")
    print(decoded_tampered_payload)
except jwt.InvalidSignatureError:
    # Esta excepción se lanza cuando la firma no coincide.
    print("ÉXITO: Error de validación esperado. La firma es inválida (InvalidSignatureError). El token fue manipulado.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
