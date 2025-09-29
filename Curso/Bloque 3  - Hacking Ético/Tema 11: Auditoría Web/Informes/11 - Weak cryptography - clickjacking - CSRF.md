## Informe Técnico: Cifrado Débil, Clickjacking y Cross-Site Request Forgery (CSRF)

Documentos de Referencia: "AWEB - Weak Cryptography - Clickjacking - CSRF.pdf"

### 1\. Resumen Ejecutivo

Este informe técnico aborda un conjunto de vulnerabilidades críticas en aplicaciones web: el **Cifrado Débil**, el ataque de **Clickjacking (o UI Redress Attack)**, y el **Cross-Site Request Forgery (CSRF)**. El contenido se centra en la importancia de asegurar los datos en tránsito mediante protocolos robustos, las consecuencias de explotar las fallas de percepción del usuario (Clickjacking), y la explotación de la confianza implícita del servidor en el navegador del usuario (CSRF). Se detallan los fundamentos teóricos, los mecanismos de explotación visuales y los procedimientos prácticos esenciales para detectar y mitigar estos riesgos en un entorno profesional de auditoría de ciberseguridad.

-----

### 2\. Conceptos Fundamentales

#### Cifrado Débil (Weak Cryptography)

El cifrado débil se define como la implementación inadecuada o insuficiente de medidas criptográficas, lo que compromete la **seguridad de la información sensible**. Estos fallos se alinean con la categoría de **Fallos Criptográficos** en el *ranking* OWASP Top 10.

  * **Naturaleza de los Fallos:** Generalmente, no son errores de programación, sino fallos de **configuración del servidor** o de la arquitectura de la aplicación web.
  * **Objetivo de la Protección:** El cifrado robusto busca proteger la **confidencialidad** y la **integridad** de los datos sensibles, aplicando esta protección en dos estados fundamentales:
      * **En almacenamiento (At Rest):** Datos guardados en bases de datos o archivos.
      * **En tránsito (In Transit):** Datos transmitidos a través de la red entre el navegador y el servidor.
  * **Protocolos Clave:** La protección de datos *en tránsito* se basa en dos configuraciones cruciales: el uso de **HTTPS** y la correcta implementación del **método POST**.

#### HTTPS y el Uso Adecuado del Método POST

  * **HTTPS (Hypertext Transfer Protocol Secure):** Es la versión segura de HTTP. Su objetivo es asegurar la confidencialidad e integridad de los datos transmitidos entre el cliente y el servidor.
      * **Mecanismo:** Combina HTTP con una capa de seguridad basada en **SSL/TLS**.
      * **Puertos:** Utiliza por defecto el **puerto 443**.
      * **Mitigación:** Previene ataques de red como **Man-in-the-Middle (MITM)** y **Eavesdropping (Escucha Clandestina)**.
  * **Método POST:** Es el método de petición HTTP utilizado para **crear o actualizar recursos** y enviar datos sensibles al servidor.
      * **Diferencia con GET:** En `GET`, los parámetros se adjuntan en la URL (*Query String*) y son visibles y menos seguros. En `POST`, los parámetros se envían en el **cuerpo de la petición HTTP**, lo que ofrece mayor seguridad.
      * **Ventajas de Seguridad:** Los datos no son visibles en la URL, no se almacenan en *logs* o historial, y el cuerpo de la petición está cifrado en combinación con HTTPS.

#### Clickjacking (UI Redress Attack)

El Clickjacking es un ataque de **ingeniería social** basado en el **engaño visual**.

  * **Concepto:** Consiste en engañar al usuario para que haga clic en un elemento **invisible** de una aplicación legítima, creyendo que está interactuando con otra cosa. Esto provoca que sus acciones tengan efectos perjudiciales en la aplicación legítima.
  * **Mecanismo:** Utiliza capas HTML, predominantemente la etiqueta `<iframe>`. Una **web maliciosa (capa visible)** se superpone a una **web legítima (capa invisible o transparente)**. El clic pasa a través de la capa visible y activa la acción en la capa invisible.
  * **Contramedida:** Proteger la aplicación para **evitar que la página legítima sea cargada dentro de un *iframe* externo**. Esto se logra mediante la configuración de las cabeceras `X-Frame-Options` o `Content-Security-Policy`.

#### Cross-Site Request Forgery (CSRF)

El CSRF, o **Falsificación de Petición en Sitios Cruzados**, explota la **confianza del servidor** en las *cookies* de sesión de un usuario.

  * **Concepto:** La víctima es forzada por el atacante a **enviar una petición HTTP** a una aplicación en la que previamente **está autenticada**, sin ser consciente de ello. El servidor ejecuta la petición creyendo que es legítima.
  * **Diferencia Clave con Clickjacking:** El CSRF requiere que el usuario esté **autenticado** en el sitio atacado; Clickjacking ataca la percepción visual.
  * **Mecanismo de Ataque:** Implica cuatro pasos:
    1.  El atacante aloja código malicioso en una **Aplicación B**.
    2.  La **Víctima** inicia sesión en la **Aplicación A** (legítima).
    3.  El atacante engaña a la Víctima para que visite la Aplicación B.
    4.  El código malicioso fuerza al navegador a enviar una petición a la Aplicación A, adjuntando automáticamente la *cookie* de sesión. El servidor ejecuta la petición.
  * **Mitigación:** La solución estándar es la implementación de **Tokens Anti-CSRF**.

-----

### 3\. Procedimientos Prácticos

#### A. Auditoría de Seguridad de Cifrado Débil (Método POST)

El objetivo es verificar que las funcionalidades sensibles utilicen el método `POST` y no `GET` para evitar la exposición de datos en la URL.

**Procedimiento de Revisión con Proxy (Ejemplo de Login):**

1.  **Configuración:** Configurar un *proxy* de intercepción (como Burp Suite) y activar la intercepción.
2.  **Acción:** Intentar iniciar sesión o realizar una acción sensible en la aplicación web.
3.  **Captura y Análisis:**
      * La captura del *proxy* muestra la petición. La **Línea 1** debe mostrar el método `POST`.
      * **Análisis de Cabeceras:** Revisar la cabecera `Content-Type` y `Content-Length`. La `Cookie` (PHPSESSID) muestra el *token* de sesión, un dato muy sensible.
      * **Análisis del Cuerpo:** Los datos sensibles (`username=admin&password=password`) deben viajar en el **Cuerpo de la Petición (Línea 15)**, no en la URL.
      * *Nota Crítica:* Si la petición fuera `GET`, los datos viajarían visibles en la URL, lo que representa una **vulnerabilidad de cifrado débil** si la acción es sensible.

#### B. Detección Manual de Clickjacking

El objetivo es determinar si una página web puede ser cargada dentro de un `iframe` externo, lo que indica una falta de protección de cabeceras (`X-Frame-Options` o `Content-Security-Policy`).

**Procedimiento de Detección (Creación de Archivo HTML):**

1.  **Creación del Código:** Crear un archivo de texto con el siguiente código HTML de prueba:
    ```html
    <html>
    <head>
        <title>Clickjack page</title>
    </head>
    <body>
        <iframe src="http://www.target.site" width="700" height="700"></iframe>
    </body>
    </html>
    ```
2.  **Guardado:** Guardar el archivo en el escritorio con la extensión `.html` (ej., `clickjacking.html`).
3.  **Modificación del Target:** Copiar la URL del dominio a auditar (ej., `0xword.com` o `mypublicinbox.com`) y reemplazar el marcador `http://www.target.site` en el atributo `src` del `<iframe>`.
4.  **Ejecución y Análisis:** Abrir el archivo `clickjacking.html` localmente en el navegador.
      * **Resultado Vulnerable:** Si la web se **carga exitosamente** dentro del *iframe*, la aplicación es **VULNERABLE**. El servidor no está bloqueando la incrustación. *Ejemplo: 0xword.com y mypublicinbox.com se cargan y son vulnerables*.
      * **Resultado Protegido:** Si aparece un cuadro en blanco, significa que la aplicación está protegida por cabeceras de seguridad.

#### C. Explotación y Replicación del Ataque CSRF (DVWA)

El objetivo es demostrar cómo se explota un formulario que utiliza el método `GET` para una acción sensible (cambio de contraseña).

**Procedimiento de Explotación (Creación de Formulario de Engaño):**

1.  **Análisis de Falla:** Identificar la URL vulnerable y los parámetros que acepta el formulario (`password_new`, `password_conf`, `Change`). El fallo es el uso de `method="GET"` para un cambio de estado.
2.  **Construcción del Código de Ataque:** Crear el archivo HTML malicioso (`csrf.html`) basado en el formulario original, pero modificado para automatizar y ocultar la petición:
      * **`action`:** Se define la URL completa de la funcionalidad vulnerable (ej., `http://192.168.111.142/vulnerabilities/csrf/?`).
      * **`type="hidden"`:** Se establece este atributo en los campos de contraseña, inyectando la nueva contraseña deseada por el atacante (`value="0xword"`).
3.  **Ejecución de Ataque:** Con la víctima autenticada en la aplicación (DVWA), el atacante la engaña para que haga clic en el botón **"Participar"** de su página maliciosa.
4.  **Resultado:** El clic lanza la petición `GET` completa (`/vulnerabilities/csrf/?password_new=0xword&password_conf=0xword...`), y el servidor, al validar la *cookie* de sesión de la víctima, ejecuta el cambio de contraseña de forma transparente.

-----

### 4\. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

  * **Protección Criptográfica:** La configuración correcta del cifrado no es opcional, sino un **deber de conciencia** para desarrolladores y auditores. El objetivo es prevenir el *sniffing* y el MITM forzando **HTTPS** y peticiones **POST** en todas las acciones sensibles.
  * **Riesgo de CSRF:** El riesgo de explotación de CSRF es **muy elevado** si se cumplen las condiciones de autenticación, pudiendo llevar a acciones indeseadas como robos de cuentas o impacto monetario.
  * **Impacto de Clickjacking:** Aunque su impacto directo es menor, el Clickjacking afecta gravemente a la **confianza del usuario** en la aplicación.

#### Puntos de Aprendizaje Clave

  * **CSRF vs. Clickjacking:** CSRF ataca la **confianza del sitio** en el usuario autenticado; Clickjacking ataca la **confianza del usuario** en la interfaz visual.
  * **Mitigación de CSRF:** La mejor defensa es el uso de **Tokens Anti-CSRF** (aleatorios y asociados a la sesión) en todas las funcionalidades críticas, así como la configuración del atributo `SameSite=Strict` en las *cookies*.
  * **Mitigación de Clickjacking:** La solución más rápida (de 30 segundos a 2 minutos) es la implementación de las cabeceras `X-Frame-Options: DENY` o `Content-Security-Policy: frame-ancestors 'none'`.

#### Relevancia Técnica

Los procedimientos aprendidos son herramientas estándar y eficientes en la auditoría profesional:

  * **Detección de Protocolos:** Herramientas como **SSL Labs**, **testssl.sh**, y **sslyze** permiten al auditor comparar y validar la configuración criptográfica desde múltiples fuentes.
  * **Análisis de Vulnerabilidades:** La revisión se enfoca en protocolos obsoletos (SSLv2/v3, TLSv1.0/v1.1) y en *suites de cifrado* débiles (ej., las que usan **CBC** o **Diffie-Hellman** en TLSv1.2).
  * **Detección Rápida de Clickjacking:** La creación del archivo `.html` de prueba es el método visual más rápido y directo para detectar la vulnerabilidad.