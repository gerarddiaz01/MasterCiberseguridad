## Informe Técnico: Persistencia de Datos en Contenedores Docker: Seguridad y Almacenamiento

### Documentos de Referencia: "DCKR - Docker-2.pdf"

### 1\. Resumen Ejecutivo

Este informe aborda la gestión de la **persistencia de datos** en contenedores Docker, un aspecto crítico para la seguridad y la fiabilidad de las aplicaciones. Dado que los datos generados por un contenedor son, por defecto, volátiles y se pierden al ser eliminados, es esencial comprender y aplicar mecanismos de almacenamiento externo. Se detallan las tres opciones principales: la capa volátil del contenedor, los montajes de enlace (*bind mounts*) y los **Volúmenes de Docker** (la solución preferida), analizando sus características, sintaxis y las implicaciones de seguridad que cada uno conlleva.

### 2\. Conceptos Fundamentales

#### 2.1. El Problema de la Persistencia y la Capa de Contenedor

  * **Volatilidad por Defecto:** La estructura inmutable de la imagen de Docker implica que los datos generados por un contenedor en ejecución son, por defecto, volátiles.
  * **Capas de la Imagen:** Las imágenes se componen de múltiples capas apiladas que son **inmutables (solo lectura - R/O)**.
  * **Capa del Contenedor:** Al arrancar un contenedor, Docker añade una capa superior que es **mutable (Lectura/Escritura - R/W)**. Todos los cambios y datos de *runtime* (archivos creados, *logs*) ocurren en esta capa.
  * **Pérdida de Datos:** Si se elimina el contenedor (`docker rm`), esta capa R/W desaparece, y con ella, todos los datos almacenados.
  * **Aislamiento:** Los datos almacenados en la capa R/W de un contenedor están aislados y **no se pueden compartir** con otros contenedores.

#### 2.2. Mecanismos de Persistencia Externa

Para la persistencia a largo plazo, los datos deben almacenarse en el sistema de archivos del *host* mediante mecanismos gestionados. El esquema ilustra las tres opciones de almacenamiento en un *Host*: *bind mount*, *volume* y *tmpfs mount*.

**\<IMAGEN image\_7a65de.png\>**

  * **Montajes de Enlace (*Bind Mounts*):**

      * **Definición:** Permiten montar un archivo o directorio **existente y arbitrario** del sistema de archivos del *host* directamente dentro de un contenedor.
      * **Persistencia:** Los datos persisten en el sistema de archivos del *host*.
      * **Uso:** Principalmente utilizados para el **desarrollo** y la **programación**, facilitando que los cambios de código del *host* se reflejen al instante en el contenedor.

  * **Volúmenes de Docker (*Volumes*):**

      * **Definición:** Es la **forma preferida y más segura** de persistir datos. Se almacenan en una sección del *Filesystem* del *host* etiquetada como "**Docker area**".
      * **Gestión:** Son gestionados directamente por el *daemon* de Docker, no por el usuario, lo que ofrece mejor rendimiento y fiabilidad que los *bind mounts*.
      * **Compartición:** Pueden ser **compartidos y reutilizados** entre múltiples contenedores.
      * **Tipos:**
          * **Volúmenes Nombrados (*Named Mounts*):** Se crean con un nombre explícito (ej. `vol1`).
          * **Volúmenes Sin Nombre/Anónimos (*Unnamed/Anonymous Mounts*):** Docker les asigna un ID aleatorio y largo.

  * **Montajes Tmpfs (*Tmpfs Mounts*):**

      * **Definición:** Se utilizan para almacenar datos solo en la **Memoria RAM** del *host*.
      * **Volatilidad:** Son completamente volátiles; los datos se pierden inmediatamente cuando el contenedor se detiene o se elimina.
      * **Uso:** Ideal para datos temporales muy sensibles o caché que nunca deben tocar el disco.

### 3\. Procedimientos Prácticos

#### 3.1. Diagnóstico de Cambios Volátiles (`docker diff`)

Para demostrar la volatilidad de la capa R/W, se inspeccionan los cambios.

1.  **Arrancar y Nombrar el Contenedor:** Se ejecuta un contenedor en modo *detached* (`-d`) y se le asigna un nombre para referenciarlo.
    ```
    docker run -d --name layer nginx
    ```
2.  **Realizar Cambios:** Se accede al contenedor con `docker exec` y se hacen modificaciones en el sistema de archivos.
    ```
    docker exec -it layer bash
    # Dentro de la shell:
    touch newfile
    rm /usr/share/nginx/html/50x.html
    exit
    ```
3.  **Inspeccionar la Capa R/W:** Se utiliza el comando de gestión `docker diff` para ver el sistema de archivos de unión.
    ```
    docker diff layer
    ```
    *Resultado esperado:* La salida mostrará el archivo añadido (`A /newfile`) y el archivo borrado (`D /usr/share/nginx/html/50x.html`). Los directorios modificados aparecerán como `C`.

#### 3.2. Uso de Montajes de Enlace (`Bind Mounts`) para Desarrollo

Se utiliza el *bind mount* para compartir código entre el *host* y el contenedor.

1.  **Ejecutar Contenedor con Montaje:** Se utiliza la opción `-v` para montar el directorio actual del *host* (`.`) en una ruta del contenedor (`/app`).
    ```
    docker run -it -v .:/app python:3.10 bash
    ```
    *Sintaxis:* La opción `-v` separa la ruta del *host* de la ruta del contenedor mediante dos puntos.
2.  **Verificación:** Una vez dentro del contenedor, se accede a `/app` y se ejecuta el código (ej. `python3 main.py`). Cualquier cambio realizado en el archivo en el *host* se refleja inmediatamente en el contenedor.

#### 3.3. Uso Compartido de Volúmenes Nombrados (Opción Recomendada)

Se demuestra cómo los volúmenes permiten la persistencia de datos y la compartición entre contenedores.

1.  **Crear Volumen Nombrado:**
    ```
    docker volume create vol1
    ```
2.  **Montar Volumen en Contenedor 1:** Se monta el volumen en el directorio `/data` de un contenedor Ubuntu.
    ```
    docker run -it -v vol1:/data ubuntu
    # Dentro del contenedor: touch /data/file1
    ```
3.  **Montar Volumen en Contenedor 2:** Se monta el **mismo volumen** en un contenedor Alpine, pero en un directorio distinto (`/mydata`).
    ```
    docker run -it -v vol1:/mydata alpine
    ```
4.  **Verificación:** Al listar el contenido de `/mydata` en el segundo contenedor, se observa el archivo `file1` creado por el primer contenedor.
    *Resultado:* La compartición de datos es instantánea. Si ambos contenedores se eliminan, el volumen `vol1` y sus datos persisten.

#### 3.4. Creación de Volúmenes Anónimos

Los volúmenes anónimos se crean sin un nombre especificado por el usuario.

1.  **Mediante Línea de Comandos:** Se especifica solo el directorio de montaje. Docker genera un ID aleatorio.
    ```
    docker run -it -v /data2 ubuntu
    ```
2.  **Mediante Dockerfile:** Utilizando la instrucción `VOLUME`.
    ```dockerfile
    FROM ubuntu
    VOLUME /data3
    ```
    *Al construir esta imagen y ejecutarla, Docker crea automáticamente un volumen anónimo para la ruta `/data3`.*

### 4\. Conclusiones y Puntos Clave

  * **Contenedores y Volatilidad:** La capa de contenedor es volátil y solo es útil para datos temporales, *logs*, o datos que se pueden perder.
  * **Riesgo de Seguridad (*Bind Mounts*):** Los *bind mounts* son útiles para el desarrollo, pero suponen un **riesgo de seguridad significativo** ya que un contenedor comprometido podría acceder o comprometer el sistema de archivos del *host*. Por esta razón, su uso debe ser limitado y controlado.
  * **Volúmenes Nombrados (Recomendación):** Los **Volúmenes de Docker** son la mejor práctica de persistencia. Al ser gestionados por Docker y no exponer una ruta arbitraria del *host* al contenedor, ofrecen un equilibrio superior entre **seguridad, fiabilidad y compartición de datos**.
  * **Ventaja de Rendimiento:** La gestión de volúmenes por parte de Docker a menudo proporciona un mejor rendimiento que los *bind mounts*.