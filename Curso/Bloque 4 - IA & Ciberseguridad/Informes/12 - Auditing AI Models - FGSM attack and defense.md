## Informe Técnico: Auditoría de Modelos de IA y Detección de Ataques Adversarios (FGSM)

Documentos de Referencia: "IAC - Auditing AI Models - FGSM attack and defense.pdf"

-----

### 1\. Resumen Ejecutivo

Este informe aborda la auditoría de modelos de **Inteligencia Artificial (IA)** con un enfoque en la ciberseguridad, destacando la necesidad de **transparencia** y **responsabilidad** en los sistemas de *Machine Learning* (ML). Se detalla el proceso estructurado de auditoría, desde la revisión ética de los datos hasta las pruebas de robustez. El núcleo del informe es un ejercicio práctico que simula la **detección de *phishing*** mediante Regresión Logística y expone la vulnerabilidad de la IA ante **Ataques Adversarios** como el método **FGSM** (*Fast Gradient Sign Method*). Finalmente, se implementa una estrategia de **defensa basada en la detección de anomalías de predicción**.

-----

### 2\. Conceptos Fundamentales

#### 2.1. El Marco de la Auditoría de IA

La auditoría es vital para garantizar la **eficacia e integridad** de los modelos de IA en la detección de amenazas y ataques.

  * **Transparencia y Responsabilidad:** La **transparencia** implica la apertura sobre el proceso de toma de decisiones del modelo, mientras que la **responsabilidad** exige que los creadores y usuarios sean responsables de sus resultados.
  * **Detección de Sesgos y Equidad:** Es esencial auditar para garantizar que los modelos **no perpetúen o amplifiquen las injusticias sociales**. Los sesgos en los datos de entrenamiento pueden conducir a decisiones discriminatorias.
  * **Fiabilidad y Consistencia:** La auditoría se enfoca en mantener la **precisión** y la **consistencia** del modelo a lo largo del tiempo, algo vital para un uso efectivo y confiable en la detección de amenazas.

#### 2.2. Ataques Adversarios (FGSM)

Un ataque adversario es la **manipulación intencionada** de la entrada de un modelo de *Machine Learning* con el fin de **engañarlo** y provocar una clasificación o predicción incorrecta.

  * **Naturaleza del Ataque:** Los ejemplos adversarios son entradas especializadas, casi **indistinguibles para el ojo humano**, pero que provocan que la red neuronal falle por completo al identificar el contenido de la imagen.
  * **Ataque de Caja Blanca (*White Box Attack*):** Supone que el atacante tiene **conocimiento completo** de la arquitectura, los parámetros y los gradientes del modelo. El método **FGSM** (*Fast Gradient Sign Method*) es un ejemplo de ataque de caja blanca.
  * **Mecanismo del FGSM:** El ataque utiliza el **signo del gradiente** de error del modelo para determinar la dirección en la que deben moverse los píxeles para **maximizar el error de predicción**. Al añadir esta perturbación mínima, se consigue que la imagen adversaria sea clasificada incorrectamente con una confianza muy alta.
  * **Impacto en la Ciberseguridad:** Los ataques adversarios no solo son teóricos; han sido documentados en el mundo físico, como la manipulación de **señales de tráfico** mediante pegatinas tipo píxeles para engañar a los modelos de visión por ordenador en coches autónomos.

-----

### 3\. Procedimientos Prácticos: Auditoría y Defensa contra FGSM

#### 3.1. Fase Teórica: El *Pipeline* de Auditoría

La auditoría de un modelo de IA se realiza a través de un *pipeline* estructurado en varias fases:

1.  **Obtención de Datos de Entrenamiento:** Recopilar el *dataset* y asegurarse de que haya sido recopilado de **forma ética** y que cumpla con las **regulaciones de privacidad** aplicables.
2.  **Identificación de Modelos:** Documentar los detalles sobre la **arquitectura del modelo**, los hiperparámetros utilizados y las versiones de las librerías empleadas.
3.  **Pruebas de Robustez y Seguridad (*Red Team*):** Evaluar la resistencia a manipulaciones maliciosas (*Adversarial Attack Evaluation*). También se realizan **pruebas de estrés** (*Stress Testing*) para forzar el modelo bajo cargas de trabajo inusuales.
4.  **Validación de Resultados:** Comparar el rendimiento del modelo con **métricas de referencia** y utilizar la **Validación Cruzada** (*Cross Validation*) para garantizar que el modelo generaliza correctamente y no tiene sobreajuste (*overfitting*).

#### 3.2. Práctica 1: Auditoría de Clasificación de *Phishing*

Se simula la auditoría de un modelo de Regresión Logística entrenado para clasificar correos electrónicos como *Spam* o *Non-Spam*, utilizando un *dataset* desequilibrado.

##### A. Carga, Inspección y Preprocesamiento de Datos

1.  **Carga e Inspección Inicial:** El proceso inicia con la carga del *dataset* (`emails_auditing.csv`) en un DataFrame de **Pandas** (`pd.read_csv`). El método **`.info()`** confirma la integridad de los datos (ej., $957$ entradas sin valores nulos).
2.  **Verificación de Desequilibrio (*Bias*):** La ejecución de **`emails_df['Label'].value_counts().plot(kind='bar')`** genera un gráfico de barras que revela un **fuerte desequilibrio de clases**. La clase **`Non-Spam`** es la clase mayoritaria (más de $800$ ocurrencias), mientras que la clase **`Spam`** es minoritaria (aproximadamente $120$ ocurrencias).
      * **Implicación de Auditoría:** Este desequilibrio es un **hallazgo crítico**. Un modelo entrenado con estos datos podría lograr una alta precisión (*Accuracy*) simplemente prediciendo 'Non-Spam' todo el tiempo, lo que enmascararía un rendimiento deficiente en la detección real de *phishing*.
3.  **Preparación del Texto:**
      * **Codificación de Etiquetas (*LabelEncoder*):** Se utiliza **`LabelEncoder`** de Scikit-learn para convertir las etiquetas de texto (`Spam`, `Non-Spam`) en valores numéricos (`1`, `0`), un requisito para los algoritmos de *Machine Learning*.
      * **Vectorización TFIDF:** El texto se convierte en una matriz numérica de características mediante el **`TfidfVectorizer`**. Esta técnica pondera las palabras por su frecuencia en un documento y su rareza en todo el *dataset*, resaltando palabras informativas. Se excluyen *stopwords* y se limita el vocabulario a $1.000$ términos.

##### B. Entrenamiento, Evaluación y Análisis de la Precisión

1.  **Entrenamiento:** Se entrena un modelo de **Regresión Logística** simple utilizando los datos vectorizados con TFIDF.
2.  **Medición de la Precisión (*Accuracy*):** El modelo logra una precisión del **$90.1\%$**.
      * **Contexto de Auditoría:** A pesar de que el $90\%$ es alto, esta métrica es **engañosa** debido al desequilibrio de clases.

##### C. Auditoría Profunda con Métricas Clave

Para obtener una visión precisa, se audita el modelo utilizando la **Matriz de Confusión** y el **Informe de Clasificación**.

  * **Matriz de Confusión:**
      * **Verdaderos Positivos (8):** Correos *Spam* clasificados correctamente como *Spam*.
      * **Falsos Negativos (19):** Correos *Spam* **incorrectamente** clasificados como *Non-Spam*. Este número es una **alerta de seguridad**, ya que son correos de *phishing* que el modelo no detectó.
      * **Verdaderos Negativos (165):** Correos *Non-Spam* clasificados correctamente.
      * **Falsos Positivos (0):** Correos *Non-Spam* clasificados incorrectamente como *Spam*.
  * **Informe de Clasificación (Clase Minoritaria - *Spam*):**
      * **Recall (0.30):** Solo el **$30\%$** de los correos *Spam* reales fueron detectados. Esto confirma los $19$ Falsos Negativos.
      * **Precisión (1.00):** El $100\%$ de los correos que el modelo clasificó como *Spam* eran realmente *Spam*, ya que no hubo Falsos Positivos.
      * **F1 Score (0.46):** Este valor es **bajo** y refleja la falta de equilibrio entre *Precision* y *Recall*.
  * **Conclusión de la Auditoría:** El modelo es excelente para identificar la clase mayoritaria (*Non-Spam*), pero su capacidad para detectar *phishing* real (*Recall* para clase $1$) es muy pobre. Esto significa que es un **sistema de seguridad no fiable** para la detección de *phishing* en producción, ya que dejaría pasar al menos $7$ de cada $10$ ataques.

##### D. Auditoría de la Interpretabilidad y Robustez

1.  **Análisis de Importancia de Características (*Feature Importance*):** Se audita la plausibilidad del modelo analizando los coeficientes del modelo de Regresión Logística.
      * **Resultado:** Palabras como **`free`**, **`stop`**, **`claim`**, **`www`**, **`mobile`** y **`cash`** aparecen con los valores de importancia más altos.
      * **Validación:** La alta consistencia de estos términos con el lenguaje típico de los anuncios y el *phishing* valida que el modelo ha aprendido patrones **razonables y plausibles**.
2.  **Validación Cruzada (*Cross Validation*):** Se utiliza **`cross_val_score`** con $cv=5$ para evaluar la capacidad de generalización del modelo.
      * **Resultado:** Las puntuaciones de precisión se mantuvieron consistentes (entre $88.2\%$ y $88.9\%$) a lo largo de las $5$ iteraciones.
      * **Conclusión de Robustez:** Esta consistencia es una señal positiva que sugiere que el modelo es **estable** y posee una **buena capacidad de generalización**, demostrando ser relativamente insensible a variaciones específicas en las muestras de datos.
3.  **Curva ROC y AUC:** Se calcula la Curva ROC utilizando las probabilidades predichas (`model.predict_proba`).
      * **Resultado:** Se obtiene un valor de **AUC de $0.99$**.
      * **Significado:** Un AUC de $0.99$ es excepcional e indica una **robusta habilidad del modelo para distinguir** entre correos legítimos y *phishing*. Sin embargo, esta métrica no debe ser el único criterio y debe complementarse con las métricas de *Recall* y *F1 Score*.

#### 3.3. Práctica 2: Ataque y Detección FGSM

Se aplica el ataque **FGSM** a un modelo de visión por ordenador preentrenado (**MobileNetV2**) para simular la auditoría de la robustez.

##### A. La Lógica del Ataque FGSM

1.  **Carga y Preprocesamiento:** La imagen objetivo (ej., un gato astronauta) se carga con una función `load_image` que **redimensiona** la imagen a $224 \times 224$ píxeles, la convierte a un *array* de NumPy, añade una **dimensión de *batch***, y aplica el **preprocesamiento específico de MobileNetV2** (normalización al rango $[-1, 1]$).
2.  **Cálculo del Gradiente:** El código utiliza **`tf.GradientTape()`** (la cinta de gradiente) para calcular el **gradiente de la pérdida** con respecto al tensor de la imagen. La función **`tf.one_hot`** define una etiqueta objetivo (que puede ser incorrecta) para maximizar el error. Este gradiente indica la dirección exacta en la que se deben modificar los píxeles para confundir al modelo.
3.  **Función de Ataque FGSM:** La función **`fgsm_attack`** implementa la lógica. La línea clave es la suma de la imagen original con la perturbación escalada por **épsilon** ($\epsilon$):
    ```python
    perturbed_image = image + epsilon * sign_of_grad
    ```
      * **`tf.sign(data_grad)`** calcula el signo del gradiente, indicando la dirección del error máximo.
      * **$\epsilon$ (Épsilon):** Controla la **magnitud** o la fuerza del ruido. Se utiliza **`tf.clip_by_value`** para asegurar que los valores de píxeles se mantengan en el rango $[-1, 1]$.
4.  **Visualización del Ruido:** Se calcula la **diferencia** entre la imagen perturbada y la original (`difference = perturbed_image - image`) para aislar y visualizar el ruido adversario. Este ruido, aunque estructurado, es un patrón de *pixels* aparentemente aleatorio.

##### B. Implementación de la Defensa y Detección

La **defensa** se implementa mediante un **Sistema de Detección de Anomalías** basado en la discrepancia de predicciones.

1.  **Función de Detección:** La función **`detect_fgsm_attack`** compara las probabilidades de predicción de la imagen original con la imagen perturbada.
      * **Cálculo de Discrepancia:** `prediction_difference = np.abs(original_prediction - perturbed_prediction)` calcula la diferencia absoluta entre las probabilidades.
      * **Verificación de Umbral:** `discrepancy = np.max(prediction_difference) > threshold` verifica si la diferencia máxima supera un **umbral** (ej., $0.5$). Si lo supera, se concluye que hay una discrepancia significativa, implicando que la imagen ha engañado al modelo.
2.  **Escenarios de Prueba (Variación de $\epsilon$):**
      * **Épsilon Alto ($\epsilon=0.40$):** La perturbación es visible y el *output* es **`FGSM attack detected.`**. La función identifica correctamente el ataque porque la predicción cambia drásticamente.
      * **Épsilon Bajo ($\epsilon=0.20$):** El ruido es sutil. El *output* es **`No FGSM attack detected.`**. Esto tiene dos posibles interpretaciones: el ruido no fue lo suficientemente fuerte para cambiar la predicción, o **el umbral es demasiado alto, creando un Falso Negativo** (un ataque existe, pero no se detecta).
3.  **Prueba de Control:** Al cargar la misma imagen en las variables original y perturbada, el sistema reporta correctamente **`No FGSM attack detected.`**, lo que valida que el algoritmo de detección no produce un falso positivo cuando las imágenes son idénticas.

-----

### 4\. Conclusiones y Puntos Clave

#### 4.1. Importancia y Beneficios de Seguridad

La auditoría de modelos de IA es un pilar fundamental para garantizar su fiabilidad, transparencia y cumplimiento de estándares éticos.

  * **Vulnerabilidad Resaltada:** El ejercicio práctico resalta la **fragilidad inherente** de los modelos de *Deep Learning* ante manipulaciones apenas perceptibles. Esto pone de manifiesto los riesgos en aplicaciones críticas como los vehículos autónomos o los sistemas de vigilancia.
  * **Detección Proactiva:** La implementación de modelos de detección de anomalías basados en la discrepancia de predicciones es un paso esencial hacia la creación de una IA más **robusta, confiable y segura**. La auditoría debe ser un **proceso continuo y cíclico** para garantizar que los modelos se mantengan efectivos.

#### 4.2. Puntos de Aprendizaje Clave

  * **Necesidad de Multi-Métricas:** En la auditoría, es fundamental balancear la **Precisión** con el rendimiento en **clases minoritarias** (el *Recall*) para evitar que la alta precisión de la clase mayoritaria oculte una baja detección de amenazas reales.
  * **Interpretabilidad:** El análisis de la **importancia de las características** (ej., palabras clave de *phishing* como 'free' o 'claim') es clave para validar que el modelo está aprendiendo patrones razonables.
  * **Defensa FGSM:** El objetivo de la defensa es encontrar el valor de épsilon ($\epsilon$) más bajo posible que **engañe al modelo** sin que la alteración sea notoria para un observador humano. Estrategias como el **Entrenamiento Adversario** y las **Transformaciones de Entrada** son vitales para mitigar el FGSM.
  * **División de Datos:** El uso de **Validación Cruzada** y de un conjunto de pruebas (*Test Set*) es crucial para confirmar la **robustez** y la capacidad de **generalización** del modelo.