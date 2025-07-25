# Criptografía y Hashing: Fundamentos para la Protección de la Información

## 1. Introducción a la Criptografía

La criptografía es el estudio y la práctica de técnicas para **proteger la información**. Su objetivo principal es convertir información legible (texto plano) en información ilegible (cifrado) de manera que solo los usuarios autorizados puedan volver a hacerla legible (descifrado).

* **Rol en Ciberseguridad**: Es una de las bases fundamentales de la ciberseguridad, crucial para garantizar la **confidencialidad** y la **integridad** de la información, tanto cuando está almacenada como cuando está en tránsito. No aborda directamente la **disponibilidad**, que es la tercera pata de la tríada de seguridad.
* **Definición**: Es el arte y la ciencia de proteger la información mediante su transformación en un formato que no puede ser entendido por personas no autorizadas. A diferencia de la codificación o la ocultación de información (esteganografía), la criptografía implica procedimientos matemáticos complejos para hacer la información ilegible.
* **Importancia**: La información es un activo crítico para las organizaciones y su protección es esencial. La criptografía permite asegurar la información en diversos escenarios:
    * **Almacenamiento**: Cifrado de datos en discos duros, memoria o bases de datos (ej. BitLocker, VeraCrypt, GPG para archivos/carpetas).
    * **Tránsito**: Protección de comunicaciones a través de canales inseguros mediante túneles criptográficos (ej. **HTTPS**, **VPN**, SSH).

### 1.1. Breve Historia de la Criptografía

La necesidad de ocultar información es milenaria:

* **Antigüedad (4000 a.C.)**: Jeroglíficos egipcios, considerados en ocasiones como elementos criptográficos iniciales.
* **Antigua Roma**: Origen de cifrados clásicos como el **Cifrado César** (o cifrado ROT), que consiste en rotar las letras un número fijo de posiciones.
* **Renacimiento (Francia)**: Trabajos como los de Blaise de Vigenère, que introdujeron técnicas más avanzadas para su época.
* **Modernización (Siglo XX)**: Trabajos como los de Claude Shannon que transformaron la criptografía en un campo de **matemáticas avanzadas**, añadiendo robustez y complejidad computacional a los algoritmos. Esto sentó las bases para la criptografía moderna (ej. RSA).

### 1.2. Objetivos de la Criptografía

Los objetivos de la criptografía se agrupan principalmente en dos áreas:

**A. Protección de la Información:**

* **Confidencialidad**: Asegurar que solo los usuarios autorizados puedan acceder y entender la información. La información se vuelve ilegible para quienes no poseen la clave o capacidad criptográfica para descifrarla.
* **Integridad**: Garantizar que la información no ha sido manipulada ni modificada (ni en tránsito ni en almacenamiento). Mecanismos como la **firma digital** o los **hashes** permiten verificar cualquier alteración del mensaje o archivo.

**B. Verificación de Usuarios:**

* **No Repudio**: Proporcionar mecanismos criptográficos que demuestren que un usuario realizó una acción, de modo que no pueda negar haberla llevado a cabo.
* **Autenticidad**: Verificar que un usuario es quien dice ser (ej. mediante certificados digitales para autenticación gubernamental).

## 2. Tipos de Criptografía

Existen dos tipos principales de criptografía, cada uno con sus propias características y usos:

### 2.1. Criptografía Simétrica

Utiliza la **misma clave** tanto para cifrar como para descifrar la información.

* **Conceptos Clave**:
    * **Clave de Cifrado**: Debe ser robusta y es la base de la seguridad del cifrado. Se usa para transformar información legible en ilegible y viceversa.
    * **Algoritmo**: El proceso matemático paso a paso que el sistema realiza para proteger la información.
* **Funcionamiento**: Un usuario cifra la información con una clave, y esa misma clave es la única que permite descifrarla y acceder al contenido.
* **Ejemplo de Algoritmos**:
    * **DES (Data Encryption Standard)**: Un algoritmo más antiguo.
    * **AES (Advanced Encryption Standard)**: El estándar actual, muy robusto y ampliamente utilizado (ej. AES de 128 bits). Otros incluyen IDEA, Blowfish.
* **Uso Principal**: Protección de la información almacenada o para cifrar grandes volúmenes de datos en canales una vez que las claves se han intercambiado de forma segura. Es generalmente **más rápida** que la criptografía asimétrica.

### 2.2. Criptografía Asimétrica (Criptografía de Clave Pública)

Utiliza **dos claves diferentes pero matemáticamente relacionadas**: una **clave pública** y una **clave privada**. Lo que se cifra con una, solo se puede descifrar con la otra.

* **Conceptos Clave**:
    * **Clave Pública**: Puede ser compartida libremente y se utiliza para cifrar información o verificar firmas.
    * **Clave Privada**: Debe mantenerse en secreto por su propietario y se utiliza para descifrar información cifrada con la clave pública correspondiente o para crear firmas digitales.
* **Solución al Problema de Distribución de Claves**: La criptografía asimétrica resuelve un problema fundamental de la criptografía simétrica: ¿cómo intercambiar de forma segura una clave secreta a través de un canal no seguro? Se utiliza la clave pública de un extremo para cifrar la clave simétrica, que luego es descifrada por la clave privada en el otro extremo.
* **Funcionamiento (Ejemplo HTTPS)**:
    1.  Un navegador se conecta a un servidor **HTTPS**.
    2.  El servidor envía su **certificado digital**, que contiene su **clave pública**.
    3.  El navegador utiliza esta clave pública para cifrar la comunicación (o una clave simétrica que generará).
    4.  El servidor utiliza su **clave privada** (que solo él posee) para descifrar la información enviada por el navegador.
    5.  Una vez establecida la conexión segura inicial, se suele generar una **clave simétrica** que se intercambia de forma segura (gracias al cifrado asimétrico) y se usa para el resto de la comunicación, ya que es más rápida para grandes volúmenes de datos.
* **Uso Principal**: Protección de canales de comunicación (establecimiento inicial de **VPNs**, **HTTPS**), firmas digitales, autenticación y gestión segura de claves simétricas. Es generalmente **más lenta** que la criptografía simétrica para el cifrado masivo de datos.
* **Ejemplo de Algoritmos**: RSA (Rivest-Shamir-Adleman) es el algoritmo más conocido.

## 3. Hashing: Verificación de la Integridad de la Información

El **hashing** es un procedimiento criptográfico que permite obtener un **resumen de una información** (un texto, un fichero, un binario, etc.). Este resumen es un conjunto de caracteres hexadecimales de longitud fija, conocido como **hash**.

* **Propiedades Clave**:
    * **Unidireccionalidad**: Es fácil obtener el hash a partir de los datos originales, pero es **computacionalmente muy complejo (impráctico)** revertir el proceso y obtener los datos originales a partir del hash. Esto es clave para su robustez.
    * **Sensibilidad al Cambio**: Incluso un cambio mínimo (un solo bit o carácter) en los datos de entrada produce un hash completamente diferente y radicalmente distinto. Esto permite detectar manipulaciones.

* **Objetivo**: El hashing se utiliza principalmente para **verificar la integridad de los datos**. Si se envía un fichero con su hash, el receptor puede recalcular el hash del fichero recibido. Si ambos hashes coinciden, se garantiza que el fichero no ha sido modificado en tránsito o almacenamiento.

* **Aplicaciones del Hashing**:
    * **Verificación de Integridad de Archivos**: Confirmar que un archivo descargado (ej. una ISO, un binario) es idéntico al original publicado por el creador.
    * **Detección de Manipulación**: Saber si un texto, un mensaje (ej. un email firmado digitalmente) o cualquier dato ha sido alterado.
    * **Almacenamiento Seguro de Contraseñas**: Las contraseñas no se almacenan directamente en bases de datos. En su lugar, se guarda su hash. Cuando un usuario introduce su contraseña, el sistema calcula su hash y lo compara con el almacenado. Esto evita que, en caso de una **data leak** de la base de datos, las contraseñas reales sean expuestas. Si los hashes coinciden, la contraseña es correcta.

* **Tipos de Algoritmos de Hashing**: La robustez de un algoritmo de hashing se mide por la dificultad de encontrar colisiones (dos entradas diferentes que producen el mismo hash). Cuanto más larga la salida del hash, menor es la probabilidad de colisiones, lo que aumenta su robustez.
    * **MD5**: Produce salidas de 16 bytes hexadecimales. Actualmente **no se considera seguro** debido a la facilidad para encontrar colisiones.
    * **SHA-1**: Produce salidas de 20 bytes hexadecimales. Tampoco se considera seguro hoy en día por problemas de colisión. Aunque puede usarse como algoritmo de soporte (segunda opinión), no debe ser el único.
    * **SHA-2 (ej. SHA-256, SHA-512)**:
        * **SHA-256**: Produce salidas de 32 bytes.
        * **SHA-512**: Produce salidas de 64 bytes hexadecimales. Son algoritmos **robustos y muy utilizables** actualmente debido a la alta dificultad para generar colisiones.
    * **Combinación de Algoritmos**: Utilizar dos algoritmos de hashing diferentes (ej. MD5 y SHA-512) para el mismo dato aumenta drásticamente la seguridad, ya que la probabilidad de que un atacante genere una colisión para ambos algoritmos simultáneamente es ínfima.

* **Ejemplo Práctico de Hashing (con `hi world!`)**:

    | Comando            | Hash (Salida)                                  | Longitud (bytes) |
    | :----------------- | :--------------------------------------------- | :--------------- |
    | `echo "hi world!" | md5sum`      | `1a7667b0afdef7323d68e291e0315ac1`               | 16               |
    | `echo "hi world!" | sha1sum`     | `4a8f78cdfd9592cb424110acbc6390b4946a5865`       | 20               |
    | `echo "hi world!" | sha256sum`   | `233117b9ef42649bb7c26a67529be93b3ee8eef4ddd7a1900f8b0f` | 32 |
    | `echo "hi world!" | sha512sum`   | `ce6fe372575251e2ffe4281d624517c54c6f2d1a7b8866ddf2f450fcb40edda3200ca4d2065a963df9166f38e3c8a06d7fcae5c08495965f6e79b2bc2e7` | 64 |

    * Como se observa, a medida que el algoritmo es más complejo (ej. SHA-512), la longitud del hash es significativamente mayor, lo que implica una mayor robustez.

* **Demostración de Integridad**:
    * Si se toma un archivo con el contenido "hi world!" y se calcula su hash (ej. con `md5sum text`), se obtiene un valor específico.
    * Si se modifica el archivo, por ejemplo, cambiando "hi world!" a "hi world?", y se recalcula el hash, el nuevo hash será completamente diferente al original, demostrando que el archivo ha sido alterado.