## Informe Técnico: Exposición Avanzada de Aplicaciones y Enrutamiento con Kubernetes Ingress

### Documentos de Referencia: "DCKR - Docker-3.pdf"

### 1\. Resumen Ejecutivo

Este informe detalla el uso de **Ingress** en Kubernetes, la herramienta preferida para gestionar el acceso externo a las aplicaciones HTTP y HTTPS. A diferencia de los Servicios tradicionales que exponen puertos directamente en los Nodos, Ingress proporciona enrutamiento avanzado en la Capa 7 (Aplicación), permitiendo el despliegue de escenarios complejos como la exposición de múltiples versiones de una aplicación (ej., `/v1` y `/v2`) bajo un único punto de entrada (*host*). Se explica la arquitectura de los controladores, el requisito de integrar Ingress con Servicios **ClusterIP** y los procedimientos para auditar y aplicar reglas de enrutamiento basadas en *path*.

-----

### 2\. Conceptos Fundamentales

#### 2.1. El Objeto Ingress

Un **Ingress** es un objeto de la API de Kubernetes que gestiona el acceso HTTP y HTTPS externo a los Servicios dentro de un clúster.

  * **Función Principal:** Actúa como un punto de entrada que proporciona **enrutamiento basado en nombre de *host*** y **rutas (*paths*)**.
  * **Limitación de Protocolo:** Ingress está limitado al tráfico **HTTP** y **HTTPS**. Si se necesita exponer otro tipo de protocolo (ej., TCP crudo o UDP), se deben utilizar servicios **LoadBalancer** o **NodePort**.
  * **Integración Requerida:** Ingress debe dirigir el tráfico a un **Servicio** de Kubernetes. Es una buena práctica utilizar servicios del tipo **ClusterIP** como *backend*.
  * **Balanceo de Carga (Capa 7):** Proporciona enrutamiento avanzado en la capa de aplicación, lo que permite dirigir el tráfico basándose en atributos HTTP, a diferencia de los Services que balancean en la Capa 4 (transporte).
  * **Terminación de TLS:** Puede manejar el cifrado/descifrado del tráfico HTTPS entrante antes de dirigirlo a los *backends*.

#### 2.2. El Controlador de Ingress

El objeto Ingress es una **declaración de reglas**; el trabajo de enrutamiento real lo realiza un componente llamado **Controlador de Ingress** (un *proxy* inverso real, como Nginx, HAProxy o Traefik).

  * **Minikube:** El controlador de Ingress por defecto en Minikube (Nginx) se habilita mediante un *addon*.
  * **Análisis de Reglas:** El controlador es el encargado de aplicar las reglas definidas en el Ingress (ej., reescribir la URL o manejar el TLS).

-----

### 3\. Procedimientos Prácticos

El siguiente ejemplo demuestra la capacidad de **enrutamiento basado en *path***, un patrón utilizado para escenarios de *Blue/Green deployment* o APIs versionadas.

#### 3.1. Preparación del Entorno (Pods y Servicios Internos)

Antes de crear el Ingress, se requiere un *backend* estable (Pods) y un *frontend* estable (Servicios ClusterIP).

1.  **Habilitación del Controlador:** Se activa el *addon* de Ingress de Minikube.
    ```bash
    minikube addons enable ingress
    ```
2.  **Despliegue de Aplicaciones (V1 y V2):** Se crean dos Pods que exponen el puerto 8080 y que se diferencian únicamente en su etiqueta **`ver`** y la imagen utilizada.
      * **Pod V1:** Etiqueta `ver: "1"`, imagen `v1`.
      * **Pod V2:** Etiqueta `ver: "2"`, imagen `v2`.
3.  **Despliegue de Servicios ClusterIP:** Se crean dos Servicios ClusterIP (`service-v1` y `service-v2`), cada uno con un selector de etiquetas que coincide con una única versión del Pod.
      * **`service-v1`:** Selector `ver: "1"`.
      * **`service-v2`:** Selector `ver: "2"`.
4.  **Aplicar Recursos:**
    ```bash
    kubectl apply -f clusteripv1.yaml -f clusteripv2.yaml -f demoappv1.yaml -f demoappv2.yaml
    ```
5.  **Verificación de Endpoints:** Se comprueba que cada servicio ha enlazado correctamente al Pod que coincide con su selector (Endpoint).

#### 3.2. Definición y Enrutamiento del Ingress

El Ingress define una única regla de *host* (`demoapp.lab.local`) con múltiples reglas de *path* para dirigir el tráfico.

1.  **Estructura del Ingress:**

      * **`kind: Ingress`**, `apiVersion: networking.k8s.io/v1`.
      * **Anotación de Reescribura:** Se utiliza la anotación específica de Nginx: `nginx.ingress.kubernetes.io/rewrite-target: /$1`. Esto es vital para que el *proxy* elimine la ruta de versión (`/v1` o `/v2`) antes de enviar la petición al servicio *backend*, asegurando que el *backend* reciba la petición en su ruta raíz (`/`).

2.  **Regla de Enrutamiento V1 (Establecimiento de Base):**

      * La regla inicial se establece en el *path* **/v1** para dirigir el tráfico al **`service-v1`**. Esto establece el **enrutamiento base** para la aplicación.
      * **Demostración de Necesidad:** Una petición sin *path* (`curl ...`) fallaría con "no encontrado" porque el Ingress no tiene una regla definida para la raíz (`/`).

3.  **Expansión para Soporte Multi-Versión:**

      * Se añade la segunda regla de *path* **/v2** para dirigir el tráfico al **`service-v2`**.
      * **Razón Estratégica:** Este patrón es crucial para **escenarios profesionales**:
          * **Despliegues Blue/Green o Canary:** Permite mantener versiones estables (`/v1`) y versiones en prueba (`/v2`) activas simultáneamente, para dirigir el tráfico de forma controlada y segmentada.
          * **APIs Versionadas** o *A/B Testing*.

4.  **Aplicar la Configuración Final:**

    ```bash
    kubectl apply -f ingress.yaml
    ```

5.  **Prueba de Enrutamiento Final:** Se utiliza `curl` con la cabecera `Host` para probar la regla de enrutamiento y la reescritura de la URL.

    ```bash
    # Prueba Versión 1
    curl -H "Host: demoapp.lab.local" $(minikube ip)/v1
    # Prueba Versión 2
    curl -H "Host: demoapp.lab.local" $(minikube ip)/v2
    ```

-----

### 4\. Conclusiones y Puntos Clave

  * **Ingress es el Estándar:** Ingress es la **forma ideal** de exponer aplicaciones HTTP/HTTPS que requieren enrutamiento avanzado, simplificando la gestión de múltiples *backends* bajo un único *endpoint* público.
  * **Requisito del Servicio (ClusterIP):** Ingress siempre debe dirigir el tráfico a un **Servicio** (idealmente **ClusterIP**). El uso de ClusterIP es preferible a NodePort, ya que evita abrir puertos adicionales e innecesarios en los Nodos.
  * **Controladores Potentes:** Aunque el controlador por defecto es Nginx, existen otros controladores más potentes y flexibles con más opciones de *routing* y configuración.
  * **Patrón de Despliegue:** El enrutamiento por *path* (ej., `/v1` y `/v2`) es una técnica clave para gestionar despliegues *Canary* y la exposición de APIs versionadas.