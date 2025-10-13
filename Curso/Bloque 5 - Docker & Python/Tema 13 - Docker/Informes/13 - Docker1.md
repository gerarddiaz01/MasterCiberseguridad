## Informe Técnico: Arquitectura, Instalación, Comandos y Optimización de Docker para Ciberseguridad

### Documentos de Referencia: "DCKR - Docker-1.pdf"

### 1\. Resumen Ejecutivo

Este informe técnico consolida y reestructura el conocimiento fundamental sobre la tecnología de **Docker**, su arquitectura, métodos de instalación, y las mejores prácticas para la construcción y gestión de imágenes seguras. Se detalla la diferencia entre la contenerización y la virtualización tradicional, se explican los componentes clave (Cliente y Daemon), y se subraya la importancia de los **Contextos** y el sistema de **Capas** para optimizar el rendimiento y reducir la superficie de ataque, conceptos esenciales para la seguridad y el desarrollo moderno.

### 2\. Conceptos Fundamentales

#### 2.1. Tecnología de Contenerización y Arquitectura

  * **Tecnología de Contenerización:** Docker es la plataforma líder que implementa la contenerización. Permite el uso y manejo de contenedores, ofreciendo un método estandarizado, eficiente, y altamente portable para empaquetar, distribuir, y ejecutar aplicaciones.
  * **Contenedor vs. Máquina Virtual (VM):** A diferencia de las VMs, los contenedores no empaquetan un sistema operativo completo, sino solo la aplicación y todas sus dependencias (librerías, binarios y archivos de configuración).
      * **Contenedor Docker:** Es un proceso aislado en el *host*. No depende de tener su propio sistema operativo completo, tiene su propio sistema de ficheros con las binarios/librerías (Bins/Libs) necesarias, pero **utiliza y comparte el núcleo del sistema operativo del *host*** (físico o virtual).
      * **Máquina Virtual (VM):** Cada VM incluye un **Sistema Operativo completo**, incluyendo su propio núcleo, lo que consume más recursos y tarda más en iniciarse.
  * **Mecanismos de Aislamiento en Linux:** La capacidad de aislamiento se basa en dos características fundamentales del **núcleo de Linux**:
      * **Namespaces (Espacios de Nombres):** Introducida en 2006, asigna a un proceso su propio espacio o sistema de ficheros, garantizando que el proceso solo "vea" los recursos que le han sido asignados.
      * **Cgroups (Control Groups - Grupos de Control):** Introducida en 2008, permite **restringir el uso de recursos** a un proceso o grupo de procesos, limitando CPU, memoria y ancho de banda de red.
  * **Arquitectura Cliente-Servidor:** La arquitectura de Docker se basa en un modelo Cliente-Servidor.
      * **Docker Daemon (Servidor/Motor):** Es un servicio de larga ejecución que gestiona todos los objetos de Docker (imágenes, contenedores, volúmenes, redes, etc.). Recibe las peticiones del cliente y las procesa.
      * **Cliente Docker:** Es la interfaz principal con el usuario (generalmente `docker` CLI). Se comunica con el Daemon mediante una API (normalmente REST) para enviar comandos como `docker run` o `docker build`.
  * **Registro (*Registry*):** Un componente esencial para la arquitectura extendida. Es un sistema de **almacenamiento y distribución** para imágenes de Docker, siendo **Docker Hub** el más conocido.

#### 2.2. Modelo de Capas y Caching

  * **Estructura de la Imagen:** Una imagen de Docker se construye a partir de una serie de **capas apiladas de solo lectura**. Cada capa es el resultado de una instrucción en el Dockerfile.
  * **Sistema Copy-on-Write (COW):** Docker utiliza el mecanismo COW (ej. OverlayFS) para permitir que las capas compartan archivos comunes, optimizando el almacenamiento. Cuando un contenedor modifica un archivo, se crea una nueva copia de los bloques de datos afectados en la **capa de escritura** superior, dejando el original inalterado.
  * **Caché de Construcción:** Docker evalúa las instrucciones del Dockerfile secuencialmente. Si una instrucción y su contexto asociado (archivos a copiar) no han cambiado desde la última compilación, Docker **reutiliza** la capa previamente construida de la caché.
  * **Invalidación de la Caché:** Si una instrucción o el contexto cambia, Docker **invalida la caché** para esa capa y **todas las instrucciones subsecuentes**. A partir de ese punto, todas las capas deben ser reconstruidas desde cero.

### 3\. Procedimientos Prácticos

#### 3.1. Instalación Nativa y Gestión de Permisos en Linux

El motor y cliente de Docker se instalan de forma nativa en Linux, lo que ofrece mayor eficiencia al no requerir una VM.

1.  **Configurar Repositorios:**
      * Actualizar paquetes e instalar `ca-certificates` y `curl`.
        ```
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        ```
      * Crear el directorio seguro para las claves GPG (`keyrings`).
        ```
        sudo install -m 0755 -d /etc/apt/keyrings
        ```
      * Descargar y asegurar la clave GPG de Docker para verificar la firma de los paquetes.
        ```
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
        sudo chmod a+r /etc/apt/keyrings/docker.asc
        ```
      * Añadir el repositorio de Docker a las fuentes de `apt`.
      * Actualizar el índice de paquetes nuevamente para incluir el nuevo repositorio.
2.  **Instalar Docker:**
      * Instalar el motor (`docker-ce`), el cliente (`docker-ce-cli`), el *runtime* (`containerd.io`), y los *plugins* clave.
        ```
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        ```
3.  **Gestión de Permisos (Evitar `sudo`):**
      * Inicialmente, el Daemon se ejecuta como *root*, requiriendo `sudo` para ejecutar comandos Docker.
      * Docker crea un grupo de sistema llamado **`docker`**.
      * Añadir el usuario actual al grupo `docker`.
        ```
        sudo usermod -aG docker $USER
        ```
      * Aplicar el nuevo grupo (sin reiniciar).
        ```
        newgrp docker
        ```

#### 3.2. Instalación y Dualidad de Contextos con Docker Desktop

Docker Desktop instala una **VM de Linux** con el Daemon dentro.

1.  **Comprobación del Contexto Nativo:** Antes de arrancar Desktop, el cliente apunta al motor nativo.
2.  **Activación de Docker Desktop:** Al arrancar Desktop, este inicia su VM y cambia **automáticamente el contexto** del cliente al Daemon que se ejecuta dentro de la VM.
3.  **Problema de Dualidad:** Los recursos (imágenes, contenedores) creados en el contexto del motor de la VM **no están disponibles** en el contexto del motor nativo, y viceversa. Es crucial saber con qué contexto se está trabajando para evitar errores de recursos no encontrados.

#### 3.3. Creación de una Imagen Personalizada (Dockerfile)

Se utiliza un **Dockerfile** (un fichero de texto con instrucciones secuenciales) para crear una imagen.

1.  **Ejecución de Contenedor Base (Nginx):** Se utiliza `docker run` para crear y arrancar un contenedor.
    ```
    docker run -it -p 8080:80 nginx
    ```
      * `-it`: Combina **`-i`** (interactivo) y **`-t`** (asigna pseudo-TTY).
      * `-p 8080:80`: Mapea el puerto **`8080` del host** al puerto **`80` del Contenedor**.
      * `nginx`: La imagen base a utilizar.
2.  **Creación del Dockerfile:** Se define el código base y la operación de copia.
    ```dockerfile
    FROM nginx
    COPY index.html /usr/share/nginx/html
    ```
      * `FROM nginx`: Define la **imagen base**.
      * `COPY index.html /usr/share/nginx/html`: Copia el fichero `index.html` del contexto de construcción al destino dentro de la imagen.
3.  **Construcción de la Imagen:**
    ```
    docker build -t my-first-image .
    ```
      * `docker build`: Comando para iniciar la construcción.
      * `-t my-first-image`: Etiqueta (`tag`) la nueva imagen con un nombre legible.
      * `.`: Indica el **Contexto de Construcción** (el directorio actual). Todo el contexto se envía al Daemon de Docker.

#### 3.4. Optimización con `WORKDIR`, `RUN` y Caché

1.  **Establecer Directorio de Trabajo:**
      * **`WORKDIR /ruta/al/directorio`**: Si el directorio no existe, Docker lo crea. Define la ruta predeterminada para instrucciones subsiguientes (`COPY`, `RUN`, etc.).
2.  **Ejecutar Comandos de Instalación:**
      * **`RUN <comando>`**: Ejecuta comandos de *shell* (ej. `apt install`, `pip install`) durante la construcción de la imagen. Cada `RUN` crea una nueva capa.
3.  **Optimización de Caché y Dependencias:** Para evitar reinstalar dependencias (baja frecuencia de cambio) cada vez que cambia el código (`app.py`, alta frecuencia), se separa la copia:
    ```dockerfile
    FROM python:3.10  # Usar imagen oficial para reducir RUNs innecesarios
    WORKDIR /app

    COPY requirements.txt .        # Capa 1: Copia solo el fichero de dependencias.
    RUN pip install -r requirements.txt # Capa 2: Se cachea si requirements.txt no cambia.

    COPY . .  # Capa 3: Se invalida si el código de la app cambia.
    CMD ["python3", "app.py"]
    ```

#### 3.5. Uso de `ENTRYPOINT` y `CMD`

Los comandos definen el **Comando Final** que se ejecutará al arrancar el contenedor.

| Comando | Propósito Principal | Recomendación |
| :--- | :--- | :--- |
| **`ENTRYPOINT`** | Define el **ejecutable principal** (la puerta de entrada inmutable). | **Modo Ejecutable:** `ENTRYPOINT ["exec", "param1"]`. |
| **`CMD`** | Proporciona los **argumentos por defecto** para el `ENTRYPOINT` o el comando principal si no hay `ENTRYPOINT`. | **Argumentos para `ENTRYPOINT`:** `CMD ["param1", "param2"]`. |

  * **Combinación Recomendada (Columna 3 de la tabla):** Si `ENTRYPOINT` está en modo ejecutable, `CMD` se añade como argumentos.
      * `ENTRYPOINT ["exe", "pe1"]` + `CMD ["pc1", "pc2"]` $\implies$ `exe pe1 pc1 pc2`.
      * Los argumentos pasados en la CLI sobrescriben completamente el `CMD`.
  * **Sobreescritura del `ENTRYPOINT`:** El `ENTRYPOINT` puede ser sobrescrito en tiempo de ejecución con `--entrypoint` (una técnica de *debugging* y seguridad).
    ```
    docker run -it --entrypoint bash mi_imagen
    ```

#### 3.6. Interacción Avanzada y Forense

1.  **Ejecución Desligada:** Para procesos de servidor, se usa `-d` para ejecutarlos en segundo plano.
    ```
    docker run -d -e MYSQL_ROOT_PASSWORD=mysecret mysql
    ```
2.  **Ejecutar Comandos Externos:** `docker exec` ejecuta comandos adicionales dentro de un contenedor *running*.
    ```
    docker exec -it [NOMBRE] bash
    ```
3.  **Copia de Ficheros:** `docker cp` copia archivos o directorios entre el contenedor y el host.
      * **Extracción (Forense):** `docker cp [NOMBRE]:/etc/nginx/nginx.conf .`
4.  **Exportación Completa:** `docker export` extrae todo el sistema de ficheros del contenedor a un archivo `.tar` (útil para el análisis forense).
    ```
    docker export -o nginx-forense.tar [NOMBRE]
    ```

### 4\. Conclusiones y Puntos Clave

#### 4.1. Importancia y Beneficios de Seguridad

  * **Reducción de la Superficie de Ataque:** La práctica más importante es el uso de **Imágenes Multifase** para excluir herramientas de *build* (compiladores, SDKs) y, si es posible, la *shell* de la imagen final (usando imágenes *Distroless* o `Alpine`). Esto minimiza las vulnerabilidades explotables.
  * **Aislamiento:** Docker proporciona aislamiento a nivel de proceso (`Namespaces` y `Cgroups`), que es superior a la ejecución directa en el *host* y previene el "caos" de dependencias.
  * **Seguridad de Red:** El uso de redes **`bridge` personalizadas** con `docker network create` permite la **microsegmentación** de aplicaciones, aislando componentes críticos (ej. base de datos) del *frontend* o de otros servicios menos sensibles, limitando el movimiento lateral de un atacante.

#### 4.2. Puntos de Aprendizaje Clave

  * **Gestión de Contextos:** Es la forma correcta y conveniente de trabajar con múltiples *Docker Daemons* (locales o remotos).
  * **Separación de Configuración:** Utilizar variables de entorno (`-e` o `--env-file`) para la configuración y nunca incluir datos sensibles en el **Dockerfile (`ENV`)** o en la línea de comandos.
  * **Optimización del *Build*:** El orden estratégico de las instrucciones en el Dockerfile es crucial para aprovechar la caché y reducir el tiempo de construcción.

#### 4.3. Relevancia Técnica

  * **Distribución Estándar:** La distribución de imágenes siempre debe realizarse a través de un **Registro de Docker** (ej. Docker Hub), y la imagen debe llevar una etiqueta (`tag`) descriptiva (evitando `latest`).
  * **Consistencia de Imagen:** El patrón `ENTRYPOINT` (como *script wrapper*) y `CMD` (como argumentos por defecto) es el estándar técnico para crear imágenes robustas y flexibles que permiten la **sobrescritura** en tiempo de ejecución.
  * **Eficiencia:** La reducción de capas mediante la agrupación de comandos `RUN` mejora el rendimiento del contenedor al reducir la sobrecarga del sistema de archivos.