# JSON Web Tokens (JWT): Autenticación y Autorización Segura en la Web

## 1. Introducción a los JSON Web Tokens (JWT)

Los **JSON Web Tokens (JWT)** son un estándar abierto (RFC 7519) que define un formato compacto y autocontenido para transferir información de forma segura entre dos partes, encapsulada en un objeto JSON. Su principal uso se encuentra en la autenticación y autorización en aplicaciones web y servicios API.

Los JWT permiten verificar la identidad de un usuario y otorgarle acceso a recursos de manera segura, eliminando la necesidad de almacenar el estado de la sesión en el servidor, lo que mejora la escalabilidad de las arquitecturas.

### 1.1. Estructura de un JWT

Un JWT se compone de tres partes diferenciadas, codificadas generalmente en formato Base64URL y separadas por puntos (`.`):

1.  **Header (Cabecera)**: Contiene metadatos sobre el token.
    * **Tipo de Token**: Suele ser `JWT`.
    * **Algoritmo de Cifrado (alg)**: Indica el algoritmo de firma utilizado, que puede ser simétrico (como **HMAC**) o asimétrico (como **RSA**). Esta sección es crucial para saber cómo interpretar y verificar el token.
    * **Ejemplo decodificado**: `{"alg":"HS256","typ":"JWT"}`

2.  **Payload (Carga Útil)**: Es donde reside la información útil o "claims" (declaraciones) sobre la identidad del usuario y otros datos relevantes para la aplicación.
    * **Claims**: Pueden incluir el nombre de usuario, roles (administrador, permisos de lectura/escritura), o información personalizada como la fecha de emisión del token (`iat`).
    * **Importante**: Aunque el Payload puede decodificarse fácilmente (ya que está en Base64), **no debe contener información sensible o credenciales**, porque no está cifrado. Su propósito es ser legible y ser validado por el receptor.
    * **Ejemplo decodificado**: `{"sub":"1234567890","name":"John Doe","iat":1516239022}`

3.  **Signature (Firma)**: Es una firma digital que asegura la **integridad y autenticidad** del token, garantizando que no ha sido alterado durante su transmisión.
    * **Generación**: Se crea combinando el Header codificado, el Payload codificado y una **clave secreta** que solo conoce el servidor (o las partes involucradas en el caso de claves asimétricas).
    * **Verificación**: El servidor utiliza la misma clave secreta (o la clave pública en caso de RSA) para verificar la firma. Si la firma no coincide, significa que el token ha sido manipulado.

**Representación codificada**: Los tres componentes se representan como cadenas codificadas en Base64URL, separadas por puntos. A simple vista, parecen cadenas aleatorias, pero son fácilmente decodificables para inspeccionar su contenido.

## 2. Proceso de Creación y Verificación de un JWT

El ciclo de vida de un JWT implica una interacción clave entre el servidor y el cliente:

1.  **Generación del JWT en el Servidor**:
    * El servidor combina el Header y el Payload.
    * Firma el token utilizando una **clave secreta** (conocida solo por el servidor o partes autorizadas). Esta firma única garantiza la autenticidad del token.

2.  **Envío del JWT al Cliente**:
    * Una vez generado, el servidor envía el JWT al cliente, usualmente como parte de una respuesta HTTP (por ejemplo, en el encabezado `Authorization` o como una cookie `HttpOnly`).
    * El cliente recibe y almacena el token para futuras solicitudes.

3.  **Verificación y Decodificación del JWT en el Servidor (con cada solicitud subsecuente)**:
    * Cuando el cliente realiza una solicitud posterior a recursos protegidos, incluye el JWT en el encabezado de autorización.
    * El servidor recibe el token y, en primer lugar, **verifica su integridad** volviendo a calcular la firma usando la misma clave secreta que utilizó para generarlo.
    * Si la firma es **válida**, el servidor procede a **decodificar el Payload** del JWT para acceder a los `claims` (información del usuario, roles, etc.).
    * Con la información decodificada, el servidor puede realizar las acciones correspondientes, como autenticar al usuario o autorizar el acceso a recursos específicos.

Este proceso simple pero efectivo establece una comunicación segura y sin estado entre el servidor y el cliente.

## 3. Casos de Uso Comunes de los JWT

Los JWT son herramientas versátiles con diversas aplicaciones en ciberseguridad:

* **Autenticación de Usuarios en Aplicaciones Web y APIs**: Permiten autenticar usuarios de forma segura sin mantener un estado de sesión activo en el servidor, lo que mejora la escalabilidad y simplifica la arquitectura.
* **Autorización y Control de Acceso a Recursos**: Los JWT pueden contener información de autorización (roles, permisos) que se utiliza para controlar el acceso a recursos protegidos dentro de una aplicación o API, permitiendo implementar políticas de acceso granular.
* **Single Sign-On (SSO) y Federación de Identidad**: Facilitan la implementación de SSO, donde un usuario inicia sesión una vez y accede a múltiples servicios sin tener que volver a autenticarse en cada uno, mejorando la experiencia del usuario y reduciendo la carga de gestión.
* **Transferencia Segura de Información entre Servicios**: Dado que la información dentro del token está firmada (y opcionalmente cifrada), se puede confiar en que no ha sido alterada durante la transferencia entre diferentes servicios, lo que los hace ideales para integraciones seguras.

## 4. Mejores Prácticas y Consideraciones de Seguridad al usar JWT

Para garantizar la seguridad al trabajar con JWT, es fundamental aplicar ciertas buenas prácticas:

* **Algoritmos de Cifrado Recomendados**:
    * Para **firmas simétricas** (basadas en una clave secreta compartida), se recomienda usar algoritmos como **HS256 (HMAC SHA-256)**.
    * Para **firmas asimétricas** (basadas en pares de claves pública/privada), se aconseja el uso de algoritmos **RS256 (RSA SHA-256)**.
    * Estos algoritmos son robustos y ampliamente aceptados en la industria.
* **Manejo Seguro de Claves Secretas**:
    * Es crucial manejar las claves secretas (o las claves privadas en el caso de RSA) con extremo cuidado.
    * Deben almacenarse de forma segura y protegerse contra accesos no autorizados.
    * Se recomienda la **rotación periódica** de estas claves para reducir el riesgo de compromiso a largo plazo.
* **Expiración y Renovación de JWTs**:
    * Establecer **fechas de expiración (exp)** en los tokens es vital para limitar la ventana de oportunidad de posibles ataques en caso de compromiso.
    * Es recomendable implementar mecanismos de **renovación automática** de tokens antes de su expiración para mantener una experiencia de usuario fluida sin comprometer la seguridad.
* **Mitigación de Ataques Comunes**:
    * Incluir **información adicional en el Payload** para validar la solicitud.
    * **Verificar la audiencia (aud)** del token para asegurar que solo sea utilizado por el destinatario previsto.
    * Estar al tanto de posibles vulnerabilidades y ataques específicos contra JWT (ej. ataques de "alg none", falsificación de algoritmos).

## 5. Demostración Práctica con un Debugger JWT Online

Un *debugger* de JWT online, como el disponible en `jwt.io`, permite comprender de forma visual cómo funcionan los JWT y cómo se verifica su firma.

### 5.1. Estructura Visual del Debugger

La herramienta divide un JWT codificado en sus tres partes (Header, Payload, Signature), mostrándolas en diferentes colores y permitiendo decodificarlas para inspeccionar su contenido en formato JSON.

* **Header (Rojo)**: Muestra el algoritmo y el tipo de token.
* **Payload (Lila)**: Contiene los *claims*.
* **Signature (Azul)**: Muestra la firma, y más abajo, el estado de verificación de la firma.

### 5.2. Interactividad con el Debugger

1.  **Cambio de Algoritmo**: Se puede seleccionar el tipo de algoritmo (simétrico o asimétrico). Al cambiar entre, por ejemplo, **HS256** y **RS256**, se observa cómo la interfaz solicita la clave secreta o un par de claves pública/privada, respectivamente.
2.  **Decodificación del Header y Payload**: Si se copia la sección del Header (o Payload) codificada en Base64 y se pega en una herramienta de decodificación Base64 (como `base64decode.org`), se puede observar su contenido legible en formato JSON. Esto demuestra que la información del Header y Payload es visible públicamente y, por lo tanto, no debe contener datos sensibles.
3.  **Demostración de Integridad (Firma)**:
    * Al modificar cualquier carácter en el **Header** o **Payload** decodificado en el *debugger*, la **firma se invalida** (`Invalid Signature`). Esto ocurre porque la firma se calcula sobre el contenido original de Header y Payload. Cualquier cambio en estos invalida la firma, y el servidor (que conoce la clave secreta original) detectaría la manipulación.
    * Para que la firma sea válida de nuevo, se necesitaría la clave secreta original para recalcularla con el contenido modificado, o bien volver al contenido original que generó la firma válida.
    * **Verificación Manual de la Firma (HMAC-SHA256)**:
        * La firma se calcula aplicando el algoritmo HMAC-SHA256 al string `[Base64UrlEncoded(Header)].[Base64UrlEncoded(Payload)]` utilizando la **clave secreta**.
        * **Ejemplo**: Si el *string* a firmar es `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ` y la clave secreta es `prueba jwt`, al calcular el HMAC-SHA256 de ese *string* con esa clave, el resultado (codificado en Base64URL) debería coincidir con la firma del JWT. Esto demuestra que sin la clave secreta, es imposible generar una firma válida que coincida con el contenido del token.

### 5.3. Conclusión de la Sesión

Los JWT ofrecen una forma segura y eficiente de transferir información en sistemas distribuidos. Comprender su estructura (Header, Payload, Firma), su proceso de creación y verificación, y las mejores prácticas de seguridad es fundamental para su correcta implementación en aplicaciones y servicios. La seguridad de los algoritmos y el manejo adecuado de las claves secretas son cruciales para garantizar la integridad y confidencialidad de los JWT.

## 1. Claims en JWT: La Información dentro del Token

Los "claims" son piezas de información clave que se incluyen dentro de un **JSON Web Token (JWT)**. Desempeñan un papel fundamental en la representación de la información del usuario, la autorización y la seguridad general del sistema.

### 1.1. Importancia de los Claims

  * **Representación de Información**: Los claims permiten transmitir datos como el nombre de usuario, roles, permisos y otros atributos relevantes de forma segura y estructurada. Esto es esencial para personalizar la experiencia del usuario y autorizar el acceso a recursos protegidos.
  * **Base para la Autorización**: Son la base para que los servidores validen y restrinjan el acceso a recursos basándose en los roles y permisos del usuario. Sin claims, sería extremadamente difícil determinar quién tiene acceso a qué.
  * **Contribución a la Seguridad**: Al estar incluidos en el cuerpo del token y protegidos por una firma digital, los claims garantizan que la información transmitida es confiable y no ha sido manipulada durante la transmisión, añadiendo una capa de seguridad.

### 1.2. Tipos de Claims en JWT

Existen tres tipos principales de claims que ofrecen flexibilidad y personalización en la transmisión de información:

#### A. Claims Registrados (Registered Claims)

Estos claims están definidos en la especificación del JWT (RFC 7519) y proporcionan información estándar necesaria para la autenticación y autorización. Son una base sólida para la interoperabilidad entre sistemas.

  * **`iss` (Issuer - Emisor)**: Indica la entidad que emitió el token JWT, por ejemplo, la URL de la aplicación (`https://miaplicacion.com`). Es esencial para que los sistemas receptores validen la procedencia del token.
  * **`sub` (Subject - Sujeto)**: Identifica al sujeto del token, que generalmente es el usuario al que se refiere. Puede ser un identificador interno único del usuario (ej. un ID de base de datos como `12345`). Crucial para la personalización y autorización de solicitudes.
  * **`aud` (Audience - Audiencia)**: Indica para qué audiencia (servicio o aplicación) está destinado el token. Puede ser una URL específica (`https://miaplicacion.com`) o un array de valores que representen múltiples audiencias (`["https://miaplicacion.com", "https://otraaplicacion.com"]`). Permite verificar si el token está destinado al sistema receptor.
  * **`exp` (Expiration Time - Fecha de Expiración)**: Indica el momento en el que expira la validez del token. Se representa en **segundos desde la época Unix (Unix Timestamp)**. Garantiza que los tokens tengan una vida útil limitada, aumentando la seguridad del sistema.
  * **`nbf` (Not Before - No Válido Antes de)**: Indica el momento a partir del cual el token es válido. También se representa en segundos desde la época Unix. Permite especificar un momento futuro a partir del cual el token puede ser considerado válido, proporcionando flexibilidad en la gestión de la validez.
  * **`iat` (Issued At - Fecha de Emisión)**: Indica el momento en el que el token fue emitido o generado. Se representa en segundos desde la época Unix. Es esencial para verificar la "frescura" del token y determinar si ha sido emitido recientemente.
  * **`jti` (JWT ID - Identificador de JWT)**: Proporciona un identificador único para el token. Generalmente es un ID aleatorio generado por el servidor al emitir el token. Es útil para evitar la repetición de tokens y para realizar un seguimiento de los mismos, mejorando la seguridad y la gestión de sesiones (ej. para implementar listas negras de tokens revocados que aún no han expirado).

#### B. Claims Públicos (Public Claims)

Estos claims no están definidos en la especificación del JWT, pero son de uso común en otras aplicaciones. Deben ser listados en el registro de JSON Web Token para evitar colisiones. Ejemplos incluyen el nombre de usuario, dirección de correo electrónico o roles específicos de una aplicación.

#### C. Claims Privados (Private Claims)

Son claims personalizados y específicos para una aplicación o servicio en particular. No están definidos en la especificación de JWT ni son de uso común en otras aplicaciones. Se utilizan para información específica que no necesita ser compartida con otros, permitiendo mantener cierta información de forma privada y segura dentro del token.

Para una gestión básica como el control de roles o tiempo, el uso de los claims registrados es suficiente.
