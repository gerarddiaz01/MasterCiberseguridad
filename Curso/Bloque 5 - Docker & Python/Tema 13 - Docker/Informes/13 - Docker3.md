## Informe Técnico: Estrategias de Limpieza y Recuperación de Espacio en Docker

### Documentos de Referencia: "DCKR - Docker-3.pdf"

### 1\. Resumen Ejecutivo

Este informe aborda la importancia crítica de la **limpieza periódica** (*cleanup*) en la administración de entornos Docker. La constante descarga de imágenes, la ejecución de contenedores y la acumulación de la caché de construcción consumen rápidamente el espacio en disco del *host*, impactando la disponibilidad y el rendimiento. Se detallan las estrategias y comandos modulares (`prune`) y agresivos (`system prune`) para recuperar espacio de manera eficiente y asegurar la estabilidad del sistema anfitrión.

-----

### 2\. Conceptos Fundamentales

#### 2.1. Artefactos de Docker y Consumo de Espacio

Cada operación de Docker almacena artefactos en el sistema de ficheros del *host*. Es vital entender qué consume espacio para limpiarlo correctamente.

  * **Imágenes y Capas:** Son los artefactos que consumen más espacio. Las imágenes están compuestas de múltiples capas inmutables.
  * **Contenedores Detenidos:** Se acumulan en el sistema, pero no suelen ocupar mucho espacio a menos que generen muchos datos en su capa de escritura (capa R/W).
  * **Capas Huérfanas (*Dangling Images*):** Son capas que ya no están referenciadas por ninguna imagen etiquetada, típicamente porque fueron invalidadas por un cambio en un Dockerfile.
  * **Caché de Construcción:** La caché utilizada por Docker para acelerar el proceso de *build* consume un espacio considerable en disco.
  * **Volúmenes:** Son artefactos persistentes que, dependiendo de los datos guardados, pueden ocupar mucho espacio.

#### 2.2. Principios de Limpieza

  * **Propósito del `prune`:** El comando `prune` se utiliza para la **limpieza automatizada** de recursos que **no estén siendo utilizados**.
  * **Regla de Negocio (Imágenes):** Una imagen **no puede ser eliminada** (`rm`) si hay un contenedor asociado a ella, incluso si ese contenedor está parado. Primero se debe eliminar el contenedor.

-----

### 3\. Procedimientos Prácticos

La limpieza en Docker se realiza mediante comandos modulares enfocados en cada grupo de recursos, o mediante un comando agresivo de sistema.

#### 3.1. Limpieza de Contenedores

La opción más sencilla es borrar todos los contenedores que han finalizado su ejecución y están detenidos.

1.  **Listar Contenedores (Todos los Estados):** Se utiliza el *flag* `-a` (all) para ver los contenedores que están *running* y los que están detenidos.

    ```
    docker container ls -a
    # o su alias
    docker ps -a
    ```

2.  **Eliminar Contenedores Detenidos:** El comando `prune` elimina todos los contenedores que han sido parados.

    ```
    docker container prune
    ```

    *Propósito:* Borra todos los contenedores que están parados en el sistema. La CLI pedirá confirmación y luego reportará el espacio liberado.

3.  **Eliminar Contenedor Individual:**

    ```
    docker container rm [NOMBRE_O_ID]
    ```

#### 3.2. Limpieza de Imágenes

Las imágenes consumen la mayor cantidad de espacio.

1.  **Eliminar Capas Huérfanas (*Dangling Images*):** El comando `prune` sin argumentos borra todas las capas no referenciadas (`<none>`).

    ```
    docker image prune
    ```

    *Propósito:* Elimina las capas que quedaron sin asignar tras la invalidación de la caché de un *build*.

2.  **Eliminar Imágenes No Usadas (Todas):** Se utiliza el *flag* `-a` (all) para borrar imágenes que no están asociadas a ningún contenedor existente.

    ```
    docker image prune -a
    ```

    *Propósito:* Esto elimina tanto las capas huérfanas como las imágenes etiquetadas que no están en uso, lo que libera una cantidad considerable de espacio.

#### 3.3. Limpieza de Redes y Volúmenes

1.  **Limpiar Redes No Usadas:**

    ```
    docker network prune
    ```

    *Propósito:* Elimina las redes creadas (ej. creadas por `docker compose`) que no están asociadas a contenedores. Las redes por defecto (`null`, `host`, `bridge`) se mantienen.

2.  **Limpiar Volúmenes Anónimos No Usados:**

    ```
    docker volume prune
    ```

    *Propósito:* Borra los volúmenes sin nombre (anónimos) que no tienen contenedores asociados.

3.  **Eliminar Volúmenes Nombrados Específicos:**

    ```
    docker volume rm [NOMBRE_VOLUMEN]
    ```

#### 3.4. Resumen y Limpieza Total del Sistema

El comando `docker system` permite una gestión de alto nivel de los recursos de Docker.

1.  **Resumen del Uso de Disco:**

    ```
    docker system df
    ```

    *Propósito:* Proporciona una visión general del espacio ocupado por imágenes, contenedores, volúmenes locales y el **tamaño de la caché de construcción**.

2.  **Limpieza Agresiva del Sistema (Incluye Caché):**

    ```
    docker system prune -a
    ```

    *Propósito:* Es la forma más agresiva y completa de limpiar el sistema, consolidando todas las operaciones de `prune`. Utilizando el *flag* `-a`, se recupera la mayor cantidad de espacio posible, ya que se eliminan **todos los artefactos de la caché de construcción**, además de los contenedores parados, redes no usadas e imágenes sin contenedores.

-----

### 4\. Conclusiones y Puntos Clave

#### 4.1. Importancia y Beneficios de Seguridad

  * **Disponibilidad del Host:** La limpieza es crítica para el **mantenimiento, el rendimiento y la disponibilidad** del sistema anfitrión, ya que la acumulación de artefactos puede consumir rápidamente el espacio en disco.
  * **Recuperación Masiva de Espacio:** El espacio reclamado puede ser considerable, especialmente si se elimina la **caché de construcción**.

#### 4.2. Puntos de Aprendizaje Clave

  * **Identificación de Consumo:** Los principales consumidores de espacio son las imágenes y la caché de construcción.
  * **Diferencia `rm` vs. `prune`:** `rm` elimina recursos específicos, mientras que `prune` realiza una limpieza automatizada de recursos no utilizados en masa.
  * **Volúmenes Persistentes:** Los volúmenes persisten y deben eliminarse de forma explícita (`docker volume rm`) o a través de un `prune` específico, ya que no se borran al eliminar los contenedores.
  * **Agresividad del Sistema:** El comando **`docker system prune -a`** es la solución definitiva para el *cleanup* periódico y la recuperación de la caché.

#### 4.3. Relevancia Técnica

  * **Mantenimiento Esencial:** Es crucial añadir la limpieza y algún tipo de monitorización al proceso operativo para mantener el sistema lo más limpio posible.
  * **Gestión de Ciclo de Vida:** La correcta gestión de los artefactos es una extensión de la buena práctica de control del ciclo de vida de las aplicaciones.