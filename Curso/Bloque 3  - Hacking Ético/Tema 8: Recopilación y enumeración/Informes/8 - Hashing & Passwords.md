Documentos de Referencia: "RE - Hashing & Passwords.pdf"

# Informe Técnico: Hashing y Cracking de Contraseñas

## 1. Resumen Ejecutivo
Este informe examina en profundidad los **ataques de fuerza bruta**, una técnica de ciberseguridad que involucra el envío de múltiples intentos de contraseñas con la esperanza de encontrar la correcta. Se describen sus objetivos y los límites teóricos que justifican la importancia de contraseñas fuertes. Se detallan los diferentes tipos de ataques de fuerza bruta, como los simples, de diccionario, híbridos, inversos y `credential stuffing`. Se presenta un análisis de herramientas como **Hydra**, **Medusa**, **Crunch** y **Cupp**, demostrando su uso práctico para atacar servicios como **SSH**, **FTP** y formularios web. Finalmente, se discuten las contramedidas esenciales para protegerse de este tipo de ataques.

---

## 2. Conceptos Fundamentales

### 2.1. Funciones Hash
Una **función hash** es un algoritmo matemático que toma una entrada de longitud variable y produce una cadena de caracteres de longitud fija. La salida, conocida como hash o digest, parece aleatoria pero no lo es. Como se muestra en el ejemplo del documento, una entrada "Hello world" a través de un algoritmo MD5 produce un hash, mientras que una entrada "Hello world!" produce un hash completamente diferente.

* **Propiedades Clave:** Una función hash de calidad debe ser:
    * **Determinista:** Para una misma entrada, siempre genera el mismo hash.
    * **Eficiente:** No debe ser costosa de realizar y debe generarse de forma rápida.
    * **Irreversible:** Debe ser casi imposible recuperar la entrada original a partir del valor hash.
    * **Uniforme:** Evita patrones predecibles en la salida, de manera que un cambio mínimo en la entrada altere drásticamente el hash resultante.
    * **Universal:** La probabilidad de colisión (dos entradas distintas que generan el mismo hash) debe ser lo más baja posible, idealmente siguiendo la función $y=1/x$.
* **Objetivos del Hashing:** El hashing tiene un amplio rango de aplicaciones.
    * **Integridad de datos y detección de errores:** Para garantizar que los datos no han sido modificados, como en el caso de los `checksums`.
    * **Seguridad criptográfica:** Se usa para el `hashing` de contraseñas y para firmas digitales.
    * **Recuperación de datos:** En estructuras como las `hash tables` para búsquedas eficientes.
    * **Deduplicación de datos:** Para evitar el almacenamiento de archivos idénticos.
    * **Generación de números aleatorios**.

### 2.2. Hashing de Contraseñas y Salting
El `hashing` de contraseñas es el uso de una función hash para almacenar contraseñas de forma segura en una base de datos. En lugar de guardar la contraseña en texto plano, se guarda su hash, lo que permite verificar la autenticación sin conocer la contraseña real.

* **Password Salting:** Es una técnica para aumentar la resistencia de las contraseñas a los ataques de fuerza bruta y `rainbow tables`. Consiste en añadir una cadena aleatoria de datos llamada **Salt** a la contraseña antes de hashearla. De esta forma, incluso si dos usuarios tienen la misma contraseña, el hash resultante será diferente. El `salt` y el hash se almacenan juntos en la base de datos.
* **Funciones de Derivación de Claves (KDF):** Algoritmos como **scrypt** y **PBKDF2** son KDF que se utilizan para hashear contraseñas de forma segura. Están diseñados para ser computacionalmente costosos, lo que ralentiza significativamente los ataques de fuerza bruta, incluso con hardware especializado.

### 2.3. Tipos de Algoritmos Hash
* **MD5:** Desarrollado en 1991, produce un hash de 128 bits (16 caracteres). Se considera **débil** y es fácilmente rompible.
* **SHA-1:** Creado por la NSA en 1993, genera un hash de 160 bits (20 caracteres). Aunque es más robusto que MD5, también tiene debilidades frente a ataques de colisión.
* **SHA-2 (SHA-256 y SHA-512):** Ambos son de alta seguridad y pertenecen a la familia SHA-2. SHA-256 produce un hash de 256 bits (32 caracteres) y SHA-512 genera uno de 512 bits (64 caracteres).
* **LM Hash:** Un método obsoleto de Windows de los años 80. Convertía las contraseñas a mayúsculas, las limitaba a 14 caracteres y las rellenaba con caracteres `NULL` si eran más cortas. La contraseña se dividía en dos partes de 7 caracteres para cifrar una cadena constante ("KGS!@#$%") con un algoritmo, y los resultados se combinaban. Este diseño lo hace extremadamente vulnerable a ataques de fuerza bruta y `rainbow tables`.
* **NTLM Hash:** Introducido como una mejora del LM Hash. Aunque permitía contraseñas más largas y diferencia entre mayúsculas y minúsculas, también se ha demostrado que es vulnerable y se considera inseguro hoy en día. Ambos hashes han sido reemplazados por algoritmos más seguros como NTLMv2 o SHA256.

### 2.4. Cracking de Contraseñas
El `cracking` de contraseñas es el proceso de adivinar o recuperar una contraseña a partir de su hash. Las técnicas principales son:
* **Fuerza Bruta:** Probar cada combinación posible de caracteres. Es lento pero potencialmente efectivo contra contraseñas cortas y simples.
* **Ataque de Diccionario:** Usar una lista de palabras comunes para adivinar la contraseña. Es más rápido que la fuerza bruta, pero está limitado a las contraseñas que se encuentran en la lista.
* **Ataque Híbrido:** Combina diccionarios con fuerza bruta, haciendo variaciones de las palabras del diccionario. Es más efectivo que los ataques individuales pero también más lento y consume más recursos.
* **Tablas Arcoíris (`Rainbow Tables`):** Utiliza tablas precalculadas para buscar rápidamente la contraseña que corresponde a un hash. Es rápido y efectivo contra contraseñas débilmente cifradas, pero requiere mucho espacio de almacenamiento y no es efectivo contra contraseñas fuertes o salteadas.

---

## 3. Procedimientos Prácticos

### 3.1. Hashing de Contraseñas con Python y Werkzeug
El documento demuestra cómo utilizar la librería **Werkzeug.security** para generar y verificar hashes de contraseñas de forma segura en una máquina Kali Linux.

1.  **Instalación:** Se instala la librería con el comando `pip install werkzeug`.
2.  **Generación de Hash:** Se utiliza la función `generate_password_hash()` en un script de Python. La salida sigue un formato como `scrypt:N:r:p$salt$hash` o `pbkdf2:sha256:260000$salt$hash`, donde se incluyen el método, los parámetros del algoritmo, el salt y el hash resultante.
3.  **Verificación de Hash:** Se utiliza la función `check_password_hash()` que toma el hash almacenado y la contraseña de texto plano. La función extrae el método y el salt del hash para verificar la coincidencia y devuelve `True` o `False`.

### 3.2. Herramientas de Cracking de Contraseñas
Se utilizan hashes previamente calculados de tipo MD5, SHA1 y LM para demostrar el `cracking`.

1.  **Identificación de Hash:** La herramienta **`hash-identifier`** se usa en Kali Linux para determinar el algoritmo de un hash desconocido.
2.  **CrackStation (Online):** Es una plataforma para descifrar hashes de forma rápida. Permite pegar hasta 20 hashes no salteados por línea. El documento muestra el ejemplo de un hash SHA1 que se resuelve a "admin123" y otro hash LM que se resuelve a "cheese" en varias combinaciones de mayúsculas y minúsculas.
3.  **Hashcat (Offline):** Es una potente herramienta de `cracking` de contraseñas de código abierto. Soporta una amplia variedad de algoritmos y tipos de ataque, como fuerza bruta y diccionario. En el ejemplo, se usa `hashcat -a 3 -m 3000 "<hash>" ?a?a?a?a?a?a` para un ataque de fuerza bruta contra un hash LM, resolviendo la contraseña `QWERTY` en segundos.
4.  **John The Ripper (Offline):** Otra herramienta de `cracking` muy utilizada. John requiere que el hash se guarde en un archivo de texto. El documento demuestra dos ataques:
    * **Ataque de diccionario:** Se utiliza el comando `john --format=raw-md5 --wordlist="/usr/share/wordlists/rockyou.txt" temporal.txt` para descifrar un hash MD5.
    * **Ataque de fuerza bruta:** Se usa `john --format=lm --incremental --max-length=6 temporal.txt` para descifrar un hash LM mediante fuerza bruta, limitando la longitud máxima a 6 caracteres.

### 3.3. Creación de Diccionarios
Se puede crear un diccionario personalizado para un objetivo específico.

* **Crunch:** Es una herramienta de línea de comandos para generar listas de palabras basadas en criterios como longitud, conjuntos de caracteres y patrones personalizados. Por ejemplo, `crunch 4 4 -t ,@@* -o output.txt` crea un diccionario de contraseñas de 4 caracteres que comienzan con una letra mayúscula, seguida de dos minúsculas y un símbolo.
* **Cupp:** El "Common User Passwords Profiler" es un script de Python de código abierto que genera diccionarios de contraseñas basándose en información personal de la víctima. Al ejecutar `python3 cupp.py -i`, la herramienta hace una serie de preguntas (nombre, fecha de nacimiento, etc.) y genera un diccionario único con una alta probabilidad de contener la contraseña de la víctima.

### 3.4. Ataques de Fuerza Bruta a Formularios Web
Se muestra cómo atacar un formulario de inicio de sesión de una aplicación web vulnerable (DVWA) con Hydra.

1.  **Análisis de Peticiones:** Utilizando las Herramientas de Desarrollador del navegador o Burp Suite, se analiza la petición HTTP del formulario. Esto permite identificar el path, los parámetros (`username`, `password`) y el mensaje de error que indica un fallo de inicio de sesión, como "Username and/or password incorrect".
2.  **Configuración del Ataque:** Se forma el comando Hydra con el protocolo `http-get-form`, se especifican el host (`localhost`), el puerto (`4280`), la ruta del formulario y se reemplazan los valores de usuario y contraseña con las palabras clave `^USER^` y `^PASS^`. Se añaden los headers de cookie para mantener la sesión y el mensaje de error para detectar los fallos.
3.  **Resultado:** Hydra prueba las contraseñas del diccionario `rockyou.txt` y encuentra que la contraseña para el usuario `admin` es "password", que es la cuarta contraseña en la lista.

---

## 4. Conclusiones y Puntos Clave

### 4.1. Importancia y Beneficios de Seguridad
El hashing es la piedra angular de la seguridad de contraseñas. Un entendimiento profundo de cómo funcionan los algoritmos, sus propiedades y sus vulnerabilidades es crucial para cualquier profesional de la ciberseguridad. La implementación de técnicas como el `password salting` y el uso de algoritmos modernos y computacionalmente costosos es fundamental para proteger los datos de los usuarios. Las contramedidas adecuadas y el uso de herramientas defensivas son la mejor forma de mitigar los riesgos de los ataques de fuerza bruta.

### 4.2. Puntos de Aprendizaje Clave
* Se ha comprendido la importancia de las propiedades de las funciones hash, como el determinismo, la irreversibilidad y la uniformidad.
* Se han identificado y diferenciado los tipos de ataques de `cracking` de contraseñas, desde los más sencillos (fuerza bruta, diccionario) hasta los más avanzados (híbridos, `rainbow tables`).
* Se ha aprendido a utilizar herramientas de desarrollo como la librería **Werkzeug.security** en Python para implementar de manera segura el `hashing` y el `salting` de contraseñas.
* Se ha demostrado el uso práctico de herramientas de `cracking` como **Hashcat** y **John The Ripper**, así como de herramientas de evaluación defensiva como **Have I Been Pwned** y **How Secure Is My Password**.
* Se ha destacado el valor de los gestores de contraseñas, como **Bitwarden** y **KeePass**, para fomentar el uso de contraseñas seguras y aleatorias.

### 4.3. Relevancia Técnica
El dominio de las herramientas y técnicas de fuerza bruta es una habilidad técnica fundamental. La capacidad de identificar y explotar vulnerabilidades de autenticación es crucial para las pruebas de penetración. Este conocimiento también es vital para los defensores, ya que les permite comprender las amenazas y aplicar contramedidas proactivas, como la implementación de políticas de contraseñas robustas, el uso de autenticación de dos factores y la monitorización de intentos de inicio de sesión sospechosos. Dominar estas habilidades es esencial para realizar auditorías de seguridad completas y efectivas, así como para diseñar y mantener sistemas seguros en el mundo real.