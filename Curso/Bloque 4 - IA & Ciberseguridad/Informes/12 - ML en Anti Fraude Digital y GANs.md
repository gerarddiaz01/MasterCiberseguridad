# Informe Técnico: Redes Generativas Antagónicas (GANs) y Detección de Fraude en la Nube

**Documentos de Referencia:** "IAC - ML en el Anti Fraude Digital, GANs.pdf"

---

## 1. Resumen Ejecutivo

Este informe detalla la integración de la **Inteligencia Artificial (IA)** y la **Computación en la Nube** como estrategia central para combatir el **fraude digital**. El documento explora dos aplicaciones fundamentales: el uso de servicios cognitivos en la nube (Azure Cognitive Services) para la **detección de fraude basada en el análisis de sentimiento** en transacciones, y el estudio de las **Redes Generativas Antagónicas (GANs)**. Se analiza la arquitectura de las GANs (Generador y Discriminador), se documenta su implementación práctica usando TensorFlow/Keras para replicar el *dataset* MNIST, y se discuten sus implicaciones duales (ataque y defensa) en el ámbito de la ciberseguridad, especialmente en la evasión de CAPTCHAs.

---

## 2. Conceptos Fundamentales

### Detección de Fraude con *Machine Learning* (ML) y la Nube
La detección de fraude digital se basa en el análisis de datos complejos y voluminosos para identificar **patrones anómalos**. Los algoritmos de *Machine Learning* distinguen de manera eficiente transacciones legítimas de las sospechosas.

* **Ventajas de la Implementación en la Nube:**
    * **Escalabilidad y Flexibilidad:** Permite ajustar los recursos de computación en función de la demanda en tiempo real.
    * **Actualización Continua:** Mantiene los sistemas de detección de fraude actualizados con las últimas técnicas de ML.
    * **Adaptación Continua:** Los sistemas aprenden de diferentes fraudes a medida que van apareciendo.
    * **Ingestión en Tiempo Real:** Logra la ingestión, procesamiento y análisis de datos de transacción en tiempo real.

### Redes Generativas Antagónicas (GANs)
Las GANs son un enfoque de *Deep Learning* diseñado para **generar datos sintéticos** que son prácticamente indistinguibles de los reales. Se basan en un ciclo de **aprendizaje adversario** constante.

* **Arquitectura de las GANs:**
    * **Generador:** Su tarea es crear datos que imiten a los reales, tomando como entrada un **Ruido Aleatorio** (*Random Noise*).
    * **Discriminador:** Su responsabilidad es evaluar los datos, intentando distinguir entre los **Datos Generados (Falsos)** y los **Datos Reales (Auténticos)**.

* **Proceso Adversario:** Durante el entrenamiento, el Generador aprende a producir datos más convincentes, y el Discriminador mejora su capacidad para detectar falsificaciones. El éxito de uno mejora al oponente, llevando a un avance gradual en ambos.

---

## 3. Procedimientos Prácticos

### 3.1. Detección de Fraude Basada en Sentimiento con Azure Cognitive Services

Este ejemplo utiliza servicios de IA preentrenados de Azure Text Analytics para evaluar el sentimiento en comentarios de transacciones, identificando indicadores de fraude sin requerir modelado desde cero.

El proceso comienza con la instalación del paquete de Python necesario para Azure (`!pip install azure-ai-textanalytics`). Una vez instalado, se procede con la **Autenticación**, donde se configuran las variables de `key` y `endpoint` necesarias para las credenciales, y se importan las clases `TextAnalyticsClient` y `AzureKeyCredential`. La **Función `authenticate_client`** crea un objeto `AzureKeyCredential` y lo usa para inicializar y devolver el `TextAnalyticsClient`, la interfaz principal con el servicio.

La **Función `analyze_transaction_comments`** está diseñada para analizar el sentimiento de los comentarios de las transacciones. Llama a `client.analyze_sentiment` e imprime el sentimiento general del documento (Positivo, Neutral o Negativo), así como las puntuaciones de confianza asociadas (positiva, neutral, negativa). También itera sobre las oraciones para imprimir el sentimiento de cada frase individual.

Finalmente, el **Uso de Ejemplo** define el cliente y una lista de documentos de ejemplo que simulan comentarios de transacciones, como "Unexpected large withdrawal from my account noticed at 2 AM." y "Confirmation of wire transfer to international account completed successfully."

La **Interpretación del Output** revela que el Documento 1 (Retirada Inesperada) es clasificado como **Negativo**, con una alta puntuación de confianza negativa, debido a términos como "Unexpected" y "large withdrawal", sirviendo como alerta de fraude. El Documento 2 (Transferencia Internacional) es clasificado como **Neutral**, al ser una frase objetiva, pero el contexto sugiere que debería activar un indicador de riesgo en un sistema de monitoreo de fraude.

### 3.2. Implementación y Entrenamiento de una GAN (Dataset MNIST)

El proceso para crear una GAN capaz de replicar los dígitos de MNIST se divide en varias fases.

El primer paso es la **Configuración y Normalización del Dataset**. Se importan `tensorflow`, `layers`, `plt`, y `time`, y se definen hiperparámetros como `BUFFER_SIZE = 60000` (para el *shuffling*) y `BATCH_SIZE = 256` (para los lotes). Se carga el *dataset* MNIST, se da formato a las imágenes a (imágenes, 28, 28, 1) para añadir el canal de color, y se convierten a `float32`. Las imágenes se **normalizan** al rango **[-1, 1]** mediante la fórmula `(train_images - 127.5) / 127.5`. Finalmente, las imágenes se transforman en un objeto `tf.data.Dataset` aplicando el *shuffling* y el *batching* para un entrenamiento eficiente.

La **Arquitectura del Modelo Generador** (`make_simple_generator_model`) utiliza una capa **Densa** de entrada que expande el vector de ruido de dimensión 100 a un tamaño de $7\times7\times256$. Luego, una capa **Reshape** lo convierte a formato 3D. A continuación, varias capas **Conv2DTranspose** aumentan progresivamente la resolución de la imagen. Los *strides* de $(2, 2)$ duplican la resolución en cada etapa (a $14\times14$ y finalmente a $28\times28$). La capa de salida final usa `activation='tanh'` para escalar los valores de los píxeles al rango [-1, 1].

La **Arquitectura del Modelo Discriminador** (`make_simple_discriminator_model`) se basa en capas **Conv2D** para reducir progresivamente las dimensiones, utilizando *strides* de $(2, 2)$ en cada capa para reducir la imagen a la mitad. Se usan capas **LeakyReLU** y **Dropout** (con 0.3) para estabilización y regularización. La capa **Flatten** convierte el tensor 3D en un vector 1D, y la capa **Densa** de salida produce la predicción escalar (logit) de que la imagen sea real.

Para el **Ciclo de Entrenamiento**, se define la función de pérdida `cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)` y dos optimizadores **Adam** separados (con tasa de aprendizaje $\text{1e-4}$). La función principal, `train_step`, utiliza `tf.GradientTape()` para registrar y calcular los gradientes del Generador y el Discriminador por separado, y los optimizadores los aplican para actualizar los pesos. Finalmente, la función `train(train_dataset, EPOCHS)` orquesta el bucle completo, registrando la pérdida cada 100 lotes.

El entrenamiento se ejecuta con `EPOCHS = 50` en la nube (como Google Colab) para aprovechar las **GPUs/TPUs**, reduciendo drásticamente el tiempo. Tras el entrenamiento, la función `visualize_results(generator)` se utiliza para generar y mostrar imágenes sintéticas, confirmando que el Generador ha aprendido las características estructurales de los dígitos de MNIST.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
La **IA y la Nube** son cruciales para la ciberseguridad, permitiendo el procesamiento en tiempo real de grandes volúmenes de datos y la **adaptación continua** a nuevas tácticas de fraude. El análisis de sentimiento con servicios cognitivos (como Azure) permite identificar alertas tempranas de fraude en las descripciones de las transacciones.

### Puntos de Aprendizaje Clave
* **Diferencia GAN: Generador vs. Discriminador:** Ambos modelos mejoran mutuamente en un proceso adversario. El Generador intenta minimizar la pérdida (engañar), y el Discriminador intenta minimizar su pérdida (clasificar correctamente).
* **Uso Adversario de GANs:** La capacidad de replicar MNIST es una plantilla directa para crear **gestores anti-CAPTCHAs** que evadan controles de autenticación basados en imágenes. También se pueden usar para crear *malware* indetectable.
* **Propósito de las Capas:** En el Generador, las capas `Conv2DTranspose` aumentan progresivamente la resolución. En el Discriminador, `Conv2D` y `strides=(2, 2)` reducen las dimensiones espaciales, y `Dropout` previene el *overfitting*.
* **Normalización Tanh:** El Generador utiliza `activation='tanh'` para escalar la salida a [-1, 1], lo que coincide con la normalización aplicada a las imágenes reales de MNIST.
* **Optimizadores Separados:** Es fundamental usar optimizadores separados (Adam) para el Generador y el Discriminador debido a sus objetivos de entrenamiento opuestos.

### Relevancia Técnica
* **tf.data.Dataset:** Su uso garantiza una manipulación y un procesamiento en lotes eficiente (Batching) y un buen mezclado (Shuffling) de los datos, reduciendo el riesgo de *overfitting*.
* **Aceleración con `@tf.function`:** El decorador compila la función `train_step` a un grafo de TensorFlow, mejorando el rendimiento y acelerando el entrenamiento.
* **Eficiencia en la Nube:** La ejecución en Google Colab con hardware de alta potencia (GPU/TPU) es una práctica esencial para el entrenamiento de modelos de *Deep Learning*, ya que **reduce drásticamente el tiempo** y los recursos de cómputo.