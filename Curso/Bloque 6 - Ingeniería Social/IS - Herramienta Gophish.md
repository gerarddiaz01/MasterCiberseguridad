## Informe Técnico: Construcción de una Campaña de Phishing Ético con Gophish

Documentos de Referencia: "IS - Gophish.pdf"

-----

### 1\. Resumen Ejecutivo

Gophish: Despliegue y Configuración Inicial para Campañas de Phishing Ético.

Este informe detalla la metodología práctica y los componentes esenciales para la creación y gestión de una campaña de *phishing* simulado utilizando la herramienta *open source* **Gophish**. Gophish es una plataforma "todo en uno" diseñada para la **concienciación** y la medición de la susceptibilidad de los empleados ante ataques de Ingeniería Social. Se desglosan los seis módulos de configuración necesarios, y se resuelve un ejercicio de prueba de concepto centrado en la **clonación del portal de *login* de GitHub** para capturar credenciales en texto plano. El objetivo principal es la verificación de la captura de datos y la comprensión del proceso de *tracking*.

-----

### 2\. Conceptos Fundamentales

Gophish se basa en la unión de varios componentes metodológicos y técnicos para simular de forma precisa el ciclo de vida de un ataque de *phishing* dirigido.

  * **Gophish (*Social Engineering Framework*):** Es una herramienta *open source* y **multiplataforma** desarrollada en Python, diseñada para simplificar el lanzamiento y el rastreo de campañas de *phishing*. Destaca por su **interfaz web intuitiva** y su funcionalidad "todo en uno," que integra todas las fases del ataque simulado en un único panel de administración.
  * **Funcionalidad "Todo en Uno":** Se refiere a la capacidad de Gophish para gestionar el **envío de correos** (*Sending Profiles*), el **diseño del cebo** (*Landing Pages* y *Email Templates*), la **selección de víctimas** (*Users & Groups*) y el **monitoreo de resultados** en tiempo real (*Campaigns*).
  * ***Tracking* y Métricas Clave:** La herramienta centraliza la recopilación de datos de comportamiento en tiempo real, lo que permite al analista monitorear el impacto de la Ingeniería Social. Las métricas incluyen:
      * **Correos Enviados:** El total de mensajes lanzados.
      * **Correos Abiertos:** Número de víctimas que han abierto el correo.
      * **Clics en el Enlace:** Número de víctimas que han hecho clic en el *link* de *phishing*.
      * **Datos Recibidos (*Data Submitted*):** Número de víctimas que han introducido sus credenciales en la *landing page*.
      * **Captura de Datos:** La capacidad de ver los nombres de usuario y las contraseñas específicos reportados por las víctimas.
  * **Contraseña de Aplicación (Gmail/2FA):** Es una contraseña generada dentro de la configuración de seguridad de la cuenta de Google, necesaria cuando la autenticación de dos factores (**2FA**) está activa. Esta cadena alfanumérica debe usarse en lugar de la contraseña de la cuenta real en el **Sending Profile** para que la autenticación SMTP sea exitosa.

-----

### 3\. Procedimientos Prácticos

La metodología práctica para una campaña de *phishing* se divide en la instalación de Gophish y la configuración precisa de sus seis módulos para garantizar la captura de credenciales en texto plano.

#### A. Instalación y Ejecución del *Framework*

Gophish se instala a partir de un archivo comprimido sin necesidad de gestores de paquetes complejos.

1.  **Descarga del Binario:** Descargar el archivo `.zip` correspondiente al sistema operativo (ej., `gophish-vX.X.X-linux-64bit.zip` para Kali Linux) desde su repositorio.
2.  **Preparación del Directorio:** Crear un directorio, mover el archivo `.zip` y extraer el contenido:
    ```bash
    mkdir gophish
    mv gophish.zip gophish/
    cd gophish
    unzip gophish.zip
    ```
3.  **Asignación de Permisos:** Otorgar permisos de ejecución al binario (`gophish`).
    ```bash
    chmod +x gophish
    ```
      * **Sintaxis y Propósito:** El comando `chmod` (change mode) con el parámetro `+x` (ejecución) asigna el permiso de lanzamiento al archivo binario, permitiendo que el sistema lo ejecute como un programa.
4.  **Ejecución y Acceso Inicial:** Ejecutar el binario en el directorio actual.
    ```bash
    ./gophish
    ```
      * **Propósito:** El `.` indica que el binario se ejecuta en el directorio actual, lanzando el servidor de Gophish y el servicio de la interfaz web.
      * **Logs y Credenciales:** La terminal emitirá mensajes (`logs`), incluyendo la **contraseña aleatoria temporal** para el primer acceso y la dirección del panel de administración (`https://localhost:3333`).
      * **Primer Acceso:** El usuario inicial es **`admin`**. Tras el *login*, la plataforma obliga a **resetear la contraseña** por motivos de seguridad.

#### B. Configuración de los Componentes de la Campaña (*Spear Phishing*)

La simulación de un *spear phishing* requiere la configuración precisa de los cuatro módulos que la integran.

1.  **Sending Profile (Perfil de Envío):**

      * **Función:** Se accede al perfil existente (o se crea uno nuevo) para configurar el **Host SMTP** (ej., `smtp.gmail.com:587`) y el **usuario/contraseña** real que enviará el correo.
      * **Suplantación:** Se define la identidad que verá la víctima (ej., `Support GitHub <suppport@githuub.com>`). Es una práctica de simulación común añadir **errores tipográficos** (ej., `suppport`) en el correo suplantado para testear la atención del empleado.
      * **Verificación:** Utilizar **Send Test Mail** para confirmar la funcionalidad del SMTP, asegurándose de usar una **Contraseña de Aplicación** si se emplea Gmail con 2FA.

2.  **Landing Page (Página de Aterrizaje - Clonación de GitHub):**

      * **Acción:** Se utiliza la funcionalidad **Import Site** para clonar el portal de *login* de GitHub (ej., `https://github.com/login`).
      * **Configuración Crítica para la Captura (Texto Claro):** Para que Gophish capture las credenciales en texto plano (el objetivo crítico), se debe:
          * **Action Vacío:** El atributo `action` del formulario (`<form action="...">`) debe estar **vacío** (`action=""`) para que Gophish intercepte los datos antes de la redirección real.
          * **Método POST:** El formulario debe usar el método **`method="post"`**.
          * **Nombres de Campos:** Los campos de usuario y contraseña (`<input>`) deben usar nombres que Gophish pueda reconocer (ej., `name="username"` y `name="password"`).
      * **Configuración de Captura:** Marcar las casillas **Capture Submitted Data** y **Capture Passwords**.
      * **Redirección:** Configurar la redirección a la **página original** de GitHub para que la víctima piense que se equivocó de credenciales, sin sospechar del engaño.

3.  **Email Template (Plantilla de Correo):**

      * **Pretexting:** Se crea un mensaje que genere **urgencia y miedo**. El *pretexting* simula un **bloqueo de cuenta** por razones de seguridad (ej., "Your GitHub account has been locked...") y requiere que la víctima cambie la contraseña.
      * **Enlace (*Link*):** Se inserta el enlace (`<a href="...">`) que apunta a la **variable de *tracking*** de Gophish, la cual dirige a la *Landing Page* clonada.
      * ***Tracking*:** Activar la opción **Add Tracking Image** para detectar si la víctima simplemente ha abierto el correo.

4.  **Campaign (Lanzamiento):**

      * **Asignación:** Se crea la campaña asignando el *Email Template* de GitHub, la *Landing Page* de GitHub, el *Sending Profile* y el **Grupo Víctimas** (que contiene al analista para la prueba).
      * **Simulación y Captura:** La víctima recibe el correo, hace clic en el enlace, introduce las credenciales (ej., `Username: 0xword`, `Password: MyPublicInbox`) y es redirigida. Gophish registra los eventos en el *timeline*.

#### C. Verificación de la Captura en Texto Claro

  * **View Details:** Acceder al módulo **Campaigns** y seleccionar **View Details** en la víctima que envió datos.
  * **Resultado:** El resultado exitoso (el objetivo crítico) es que la contraseña se muestre en **texto plano** (ej., `Password: MyPublicInbox`), confirmando que el formulario HTML fue configurado correctamente y Gophish interceptó los datos sin cifrar.

-----

### 4\. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

Gophish demuestra la **facilidad** y la **eficacia** con la que se pueden orquestar ataques de *spear phishing* básicos. El uso de esta herramienta en auditorías de concienciación es invaluable, ya que permite:

  * **Centralización del *Tracking*:** Gophish centraliza el *tracking* y la recopilación de datos de forma visual, lo que es esencial para presentar resultados claros a la dirección de una organización.
  * **Medición de la Susceptibilidad:** Permite medir la **susceptibilidad** real de los empleados ante una amenaza dirigida, identificando al "eslabón más débil".

#### Puntos de Aprendizaje Clave

  * **La Captura en Texto Plano:** La clave del éxito de la campaña reside en la configuración de la *Landing Page* con el atributo `action=""` y el método `method="post"` para garantizar la intercepción de credenciales en **texto claro**.
  * **Ciclo de Vida del *Phishing*:** Se refuerza la comprensión de cómo los cuatro componentes clave (Perfiles, Páginas, Plantillas, Grupos) se unen para simular el ciclo de vida del ataque.
  * **El *Pretexting* Funcional:** La urgencia (bloqueo de cuenta) genera la emoción necesaria para que la víctima haga clic y envíe sus datos.

#### Relevancia Técnica

  * **Conocimiento de HTML:** Para lograr el éxito total, el analista debe poseer **conocimientos de HTML** para inspeccionar y modificar manualmente el código fuente del formulario y sus atributos (`action`, `method`, `name`), superando las imprecisiones de la clonación automatizada.
  * **Desafíos en Producción:** Para un uso profesional y evitar ser bloqueado, se debe ser consciente de las **cabeceras de Gophish** que pueden ser identificadas por los sistemas de defensa de correo electrónico. Esto requiere la **personalización** de configuraciones internas y el uso de **servidores SMTP de *hosting* limpios** para evadir la detección.