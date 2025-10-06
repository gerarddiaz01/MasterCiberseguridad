## Informe Técnico: Implementación y Seguridad de Large Language Models (LLM) Locales

Documentos de Referencia: "IAC - LLMs and Cybersecurity.pdf"

-----

### 1\. Resumen Ejecutivo

Este informe aborda la importancia crítica de los **Large Language Models (LLM)** de **código abierto** (*Open Source*) y su ejecución en entornos **locales**. Esta estrategia mitiga el riesgo de **privacidad de datos** asociado a las APIs públicas y permite una personalización avanzada. El informe detalla el funcionamiento, las vulnerabilidades intrínsecas y las aplicaciones de los LLM en ciberseguridad, y presenta la plataforma **Ollama** como solución central para desplegar modelos como Llama 2 y Mistral, finalizando con la construcción de un **chatbot local** (*Copilot*) utilizando **Gradio**.

-----

### 2\. Conceptos Fundamentales

#### 2.1. Fundamentos y Flujo de Trabajo de los LLM

Los LLM representan un avance significativo en la IA, siendo capaces de entender y crear texto con un nivel de complejidad similar al del ser humano. Se entrenan con enormes volúmenes de texto, lo que les permite predecir la palabra o frase siguiente en un contexto dado.

  * **Principio de Operación:** Los LLM operan bajo el principio de **predicción de texto**, analizando grandes cantidades de datos para determinar cuál es la secuencia más probable que sigue a una entrada dada.
  * **Ciclo de Interacción:** El proceso de interacción con un LLM sigue un flujo de trabajo estructurado:
    1.  **Procesamiento de Texto:** Limpieza, corrección de errores ortográficos o normalización para estandarizar la entrada.
    2.  **Tokenización:** El texto se divide en unidades más pequeñas llamadas *tokens* (palabras, subpalabras o caracteres de puntuación), lo cual es vital para que el modelo lo procese eficientemente.
    3.  **Codificación (*Encoding*):** Cada *token* se convierte en un **vector numérico** (aprovechando modelos de *embedding* preentrenados) que el LLM puede usar para realizar cálculos.
    4.  **Inferencia al Modelo:** El LLM predice la secuencia de salida más probable.
    5.  **Decodificación (*Decoding Output*):** La salida del modelo (en forma de vectores o *tokens*) se traduce de nuevo a texto legible.
    6.  **Post-Procesamiento:** La salida puede requerir ajustes adicionales como correcciones automáticas o filtros.
    7.  **Presentación de Resultados:** Los resultados procesados se presentan al usuario.

\<IMAGEN del workflow de las LLM\>

#### 2.2. Riesgos de Seguridad y Vulnerabilidades

La seguridad de los LLM es crítica debido al manejo de información sensible y a la exposición a ataques específicos.

  * **Autenticación y Autorización:** Se requiere una autenticación y autorización efectivas, asegurando que solo los usuarios autorizados puedan acceder y utilizar estas herramientas. La implementación de sistemas robustos de control de acceso, como la autenticación de dos factores y la gestión detallada de permisos, es crucial para prevenir el uso indebido.
  * **Privacidad de Datos (Riesgo de Reentrenamiento):** La privacidad de los datos es una preocupación primordial, especialmente al manejar información personal o sensible.
      * **Riesgo de Infracción de GDPR/Normativa:** Subir información privada (como IPs o direcciones de correo) a servicios de API de LLM puede infringir la normativa, ya que esa información puede ser utilizada para **reentrenar el modelo** y, potencialmente, ser expuesta a otros usuarios en el futuro.
  * **Integridad de Datos:** Es fundamental mantener la integridad de los datos para asegurar que la información procesada y generada sea **precisa y confiable**. Se necesitan mecanismos para detectar y prevenir alteraciones no autorizadas y manipulaciones maliciosas.
  * **Vulnerabilidades Específicas:** Los LLM se enfrentan a vulnerabilidades específicas que pueden ser explotadas:
      * **Inyección de *Prompting* (*Prompt Injection*):** Un agente malicioso podría atacar inyectando código en el *prompt* para que el LLM ejecute acciones o devuelva información sensible que no estaba predeterminada en la pregunta inicial.
      * **Ingeniería de *Prompting* (*Prompt Engineering*):** Aunque es una técnica para obtener mejores salidas, también puede utilizarse para modificar o malinterpretar la salida del LLM y obtener información sensible.

#### 2.3. Modelos *Open Source* y Justificación de Ejecución Local

Los LLM de código abierto y portables son fundamentales para la **privacidad** y la **personalización**.

  * **Ventajas *Open Source***:
      * **Acceso y Portabilidad:** Facilitan el acceso a tecnologías avanzadas sin ataduras a contratos costosos o fallos del proveedor.
      * **Personalización:** Permiten ajustar y personalizar los modelos para necesidades específicas.
      * **Ética y Reproducibilidad:** Hacen posible que los investigadores examinen el código y los datos de entrenamiento para asegurar la robustez y abordar preocupaciones éticas relacionadas con el consentimiento informado y la privacidad.
  * **Modelos Destacados:** **Llama 2 (Meta)**, que se centra en la seguridad y la minimización de sesgos, y **Mistral 7B**, optimizado para el entrenamiento y la inferencia rápida.

-----

### 3\. Procedimientos Prácticos: Ollama y Chatbots Locales

**Ollama** es la plataforma clave para facilitar la configuración y ejecución de LLMs de código abierto (como Llama 2, Mistral, Gemma) en **dispositivos locales**, resolviendo el problema de la privacidad al eliminar la dependencia de la nube.

#### 3.1. Instalación y Procedimiento CLI con Ollama

Para ejecutar LLMs localmente con eficiencia, se requiere hardware especializado como **GPUs** (tarjetas gráficas) o **Apple Silicon (M1, M2, M3)**.

1.  **Descarga e Instalación:** Tras la descarga de la versión de Ollama adecuada, se realiza la instalación.
2.  **Comandos Principales (CLI):**
      * **`ollama list`**: Muestra los modelos instalados localmente.
      * **`ollama pull [modelo]`**: Conecta con el repositorio de Ollama y descarga el modelo especificado (ej., `ollama pull mistral`) en la máquina local.
      * **`ollama run [modelo]`**: Ejecuta el modelo directamente en la terminal, abriendo el *prompting* para iniciar la inferencia.
3.  **Inferencia Local:** Al ejecutar `ollama run mistral`, el modelo se inicia localmente. El **tiempo de inferencia es extremadamente rápido**, y la conexión es local, ejecutándose sin necesidad de Internet. Esto funciona como tener un ChatGPT instalado en local.

#### 3.2. Personalización Avanzada con *System Prompt* (*Prompt Anchoring*)

Ollama permite personalizar el comportamiento del modelo utilizando un fichero de texto que define una base de *prompting* inicial, conocido como *system prompt* o *prompt anchoring*.

1.  **Creación del Fichero de Definición (Ejemplo: `david_mistral.py`):** El fichero contiene la configuración y las instrucciones de comportamiento:
    ```
    FROM mistral
    PARAMETER temperature 1
    SYSTEM """ You are David Lightman, a young cybersecurity hacker who knows how to access government systems. 
    Always answer with only one line. """
    ```
      * **`FROM mistral`**: Indica el modelo base a utilizar.
      * **`PARAMETER temperature 1`**: El parámetro *temperature* ajusta la creatividad. Un valor alto (ej., 1) lo hace más creativo e imaginativo; un valor bajo lo hace más coherente.
      * **`SYSTEM "..."`**: Define el *system prompt* que **ancla** la personalidad y las reglas del modelo.
2.  **Creación del Modelo Personalizado:** Se utiliza el comando `ollama create` para generar el modelo ajustado:
    ```bash
    ollama create david -f david_mistral.py
    ```
3.  **Ejecución del Modelo Personalizado:** Al ejecutar `ollama run david`, el modelo asume la personalidad definida y sigue las reglas de respuesta, permitiendo customizar el modelo con una infinidad de líneas y parámetros.

#### 3.3. Creación de un Chatbot Privado con Gradio

Para crear una interfaz de chat privada similar a ChatGPT, pero ejecutándose localmente, se utiliza el *framework* **Gradio**.

1.  **Instalación:** Se instala Gradio a través de *pip* (`pip install gradio`).
2.  **Lanzamiento del Servidor:** El código Python (*chat\_mistral.py*) define el *backend* y el *frontend*. Al ejecutar el fichero, se levanta un pequeño **servidor web local** (ej., `http://127.0.0.1:7860`).
3.  **Lógica del Chatbot (`chat_mistral.py`):**
      * **Configuración:** La `api_url` apunta a la API local de Ollama (`http://localhost:11434/api/generate`).
      * **`send_api_request`**: Envía la petición HTTP POST a la API de Ollama con el *prompt*.
      * **`append_to_chat_history`**: Mantiene la **memoria de la conversación** almacenando la entrada del usuario y la respuesta del modelo.
      * **`process_user_input`**: Recupera el historial completo, lo envía como *prompt* y, si la respuesta es $200$ OK, actualiza el historial y devuelve la respuesta. Esto asegura el **manejo del contexto**.
      * **Interfaz Gradio:** **`gr.Interface`** crea la interfaz gráfica (`GUI`) y **`interface.launch()`** inicia la aplicación web local.
4.  **Funcionamiento:** El LLM genera respuestas de ciberseguridad avanzada (ej., sugiriendo el uso de Hydra para ataques de fuerza bruta), demostrando que se tiene una herramienta poderosa y consultiva **instalada en local** y funcionando sin depender de Internet.

#### 3.4. CrewAI y la Conexión de Agentes

**CrewAI** es un *framework* que permite **crear agentes** (conectar diferentes modelos) para realizar funciones concretas, donde el *output* de uno se convierte en el *input* del siguiente.

  * **Agentes y Tareas:** Se pueden conectar modelos especializados (ej., uno para encontrar fallos de seguridad) con otro modelo (para generar código eficiente).
  * **Tools:** Los agentes pueden utilizar *tools* (herramientas) para buscar en la web o leer ficheros.
  * **Procesos:** Las conexiones pueden ser **jerárquicas** (un modelo manda y controla) o **secuenciales** (las tareas se ejecutan en un orden predefinido).

### 4\. Conclusiones

El uso de modelos LLM locales, especialmente en el ámbito de la ciberseguridad, es vital para crear herramientas más seguras y personalizadas. Permite responder a las amenazas sin depender de la conexión a Internet, lo que podría comprometer la seguridad de datos críticos y personales.

**Ollama** es una herramienta muy valiosa en este contexto, ya que facilita el despliegue y la gestión de modelos LLM de código abierto en entornos locales. Esto permite a los profesionales de la ciberseguridad experimentar con soluciones innovadoras adaptadas a cualquier tipo de necesidad, garantizando la **privacidad** y la **confianza**.