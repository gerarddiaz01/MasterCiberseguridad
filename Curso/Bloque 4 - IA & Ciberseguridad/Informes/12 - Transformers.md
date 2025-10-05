# Informe Técnico: Arquitectura Transformer, Evaluación de Modelos y Análisis de Logs de Seguridad

**Documentos de Referencia:** "IAC - Transformers.pdf"

---

## 1. Resumen Ejecutivo

Este informe aborda dos pilares fundamentales del *Machine Learning* aplicado a la ciberseguridad: la arquitectura **Transformer** y las metodologías de **evaluación de modelos**. Se explora en detalle el **Mecanismo de Atención** y el diseño **Codificador-Decodificador** del Transformer, destacando su aplicación en la detección de *malware* y el análisis de *logs* de seguridad. Además, se documenta la importancia de métricas como **Precisión**, **Recall**, y **AUC-ROC**, junto con técnicas de validación robustas como la **Validación Cruzada (*Cross-Validation*)**, para garantizar que los modelos de IA sean eficientes, justos y capaces de generalizar amenazas en entornos de producción.

---

## 2. Conceptos Fundamentales

### Arquitectura Transformer y Mecanismo de Atención
El Transformer es una arquitectura fundamental de *Deep Learning* que revolucionó el procesamiento de datos secuenciales al sustituir las redes recurrentes (RNNs) por el mecanismo de atención.

* **Mecanismo de Autoatención (*Self-Attention*):** Permite al modelo enfocarse en diferentes partes de una secuencia de entrada, asignando niveles variables de importancia a distintos elementos para capturar dependencias a largo plazo.
    * **Consulta (*Query*):** Representa la posición actual que se está evaluando, la "pregunta" que el modelo intenta entender.
    * **Clave (*Key*):** Representa la información descriptiva asociada con todas las posiciones de la secuencia.
    * **Valor (*Value*):** Representa el contenido de información real, que se suma y se pondera para crear la salida final contextualizada.
* **Codificación Posicional (*Positional Encoding*):** Es un mecanismo crucial para inyectar información sobre la **posición u orden** de los datos en la secuencia. Esto es necesario porque el Transformer procesa la secuencia completa en paralelo, perdiendo inherentemente la información de orden.
    * **Codificación de Posición Absoluta:** Asigna un vector único que codifica la posición exacta del *token*.
    * **Codificación de Posición Relativa:** Captura la relación de distancia entre los *tokens*.

### Métricas Clave de Evaluación de Modelos
La evaluación de modelos de clasificación requiere métricas que vayan más allá de la simple precisión (*Accuracy*).

* **Precisión (*Precision*):** Mide la proporción de predicciones positivas correctas entre todas las instancias que el modelo clasificó como positivas. Se centra en la calidad de las predicciones positivas.
* **Sensibilidad (*Recall*):** Mide la proporción de instancias positivas correctas que el modelo identificó, entre todas las instancias positivas reales presentes en el *dataset*. Se centra en la capacidad del modelo para capturar todos los casos positivos.
* **Puntuación F1 (*F1 Score*):** Es la media armónica que combina la Precisión y el Recall en un solo valor, proporcionando una métrica equilibrada.
* **AUC-ROC (*Area Under the Curve*):** Mide la capacidad de discriminación del modelo, representando la relación entre la tasa de verdaderos positivos (Recall) y la tasa de falsos positivos en diferentes umbrales. Un valor más cercano a 1 indica un mejor rendimiento para distinguir entre clases.
* **Robustez (*Robustness*):** Capacidad de un modelo para manejar bien los datos nuevos o inesperados sin que su utilidad se vea afectada.
* **Eficiencia (*Efficiency*):** Uso óptimo de los recursos computacionales, incluyendo tiempo de entrenamiento y predicción, memoria y potencia de cómputo.
* **Justicia (*Fairness*) y Ausencia de Sesgo (*Bias Absence*):** Es fundamental para asegurar que los modelos no perpetúen ni introduzcan sesgos indeseados en los resultados.

---

## 3. Procedimientos Prácticos

### 3.1. Arquitectura Transformer: Diseño Codificador-Decodificador
La arquitectura del Transformer se compone de dos módulos principales interconectados, como se ilustra en el esquema:

#### Bloque Codificador (Encoder)
El Codificador procesa la secuencia de entrada (*Input Data*) para extraer características y generar una representación contextual rica (*Encoded Output*).

1.  **Entrada:** Los datos se convierten en *Embeddings* y se combinan con la **Codificación Posicional** para inyectar información sobre el orden de la secuencia.
2.  **Self-Attention Mechanism:** La capa central permite que cada elemento de la secuencia se compare con todos los demás para calcular su relevancia contextual.
3.  **Add & Norm:** La salida de la auto-atención se suma a la entrada (conexión residual) y se aplica una **Normalización de Capa (*Layer Normalization*)** para estabilizar el entrenamiento.
4.  **Feed-Forward Network:** Una red *Feed-Forward* aplica una transformación idéntica a cada posición del vector, introduciendo no-linealidad. Este flujo de adición y normalización se repite antes de generar el *Encoded Output*.

#### Bloque Decodificador (Decoder)
El Decodificador toma el *Encoded Output* del Codificador y genera la secuencia de salida (*Output Data*).

1.  **Entrada:** Comienza con *Embedding* y *Positional Encoding* de la secuencia de salida inicial.
2.  **Self-Attention Enmascarado:** Utiliza una forma enmascarada de auto-atención que obliga al modelo a **solo atender a las posiciones ya generadas**, manteniendo la causalidad.
3.  **Cross-Attention Mechanism:** Es el punto de conexión. La **Query** proviene del *Self-Attention* del Decodificador, y la **Key** y **Value** provienen del *Encoded Output* del Codificador. Esto permite al Decodificador enfocarse en las partes más relevantes de la *entrada* para generar la *salida*.
4.  **Feed-Forward Network:** Sigue una red *Feed-Forward* y capas de *Add & Norm*.

### 3.2. Evaluación de Modelo con Métricas y Validación Cruzada

#### Entrenamiento y Medición de Métricas (Regresión Logística)
El proceso utiliza un conjunto de datos generado artificialmente de $1.000$ muestras y $20$ características para clasificar entre $2$ clases.

1.  **División y Entrenamiento:** Los datos se dividen con `train_test_split` (80% entrenamiento, 20% prueba). Se inicializa un modelo de `LogisticRegression` y se mide el tiempo de ejecución del entrenamiento con `time.time()`.
2.  **Predicción y Cálculo:** Se usa `model.predict(X_test)` para obtener las predicciones. Luego, se utilizan las funciones de `sklearn.metrics` (`precision_score`, `recall_score`, `f1_score`, `roc_auc_score`) para comparar las predicciones con las etiquetas verdaderas (`y_test`).
3.  **Análisis de Resultados (Ejemplo):** Los resultados de muestra indican un rendimiento sólido:
    * **Precisión:** $\approx 0.915$. El $91.5\%$ de las predicciones positivas fueron correctas.
    * **Recall:** $\approx 0.804$. El $80.4\%$ de todos los casos positivos reales fueron capturados por el modelo.
    * **F1 Score:** $\approx 0.856$. Indica un buen equilibrio entre precisión y recall.
    * **AUC-ROC:** $\approx 0.859$. Muestra una sólida capacidad de discriminación entre clases.
4.  **Visualización:** Los resultados se presentan en un gráfico de barras utilizando Matplotlib, donde se visualiza la Puntuación de cada métrica en un eje Y normalizado de 0 a 1.

#### Validación Cruzada (*Cross-Validation*)
La validación cruzada es una técnica avanzada que divide el *dataset* en $K$ subconjuntos (*folds*), rotando qué *fold* se usa para la prueba y cuáles para el entrenamiento.

1.  **Proceso:** El ejemplo usa el *dataset* Iris y la función `cross_val_score(model, X, y, cv=5)` para realizar la validación con $5$ *folds*.
2.  **Resultado:** El *output* muestra las $5$ puntuaciones de precisión obtenidas en cada iteración. El promedio (`Mean CV Score`) es la estimación final, demostrando la capacidad del modelo para generalizar.

---

## 4. Conclusiones y Puntos Clave

### Importancia y Beneficios de Seguridad
Los **Transformers** son una arquitectura clave para la ciberseguridad, ya que su mecanismo de **Auto-Atención** permite a los modelos enfocarse en secuencias clave de datos, sin importar la distancia, lo cual es crucial para:
* **Detección de *Malware***: Identificar relaciones entre APIs separadas en el código binario que indican una carga útil maliciosa.
* **Análisis de *Logs***: Dar un alto peso de atención a eventos críticos ocurridos hace horas (ej., un inicio de sesión fallido) que son relevantes para el evento actual (ej., una escalada de privilegios).
* **Detección de *Phishing***: Identificar la relación crítica entre el texto del cuerpo de un correo (ej., que sugiere "urgencia") y la URL del remitente.

### Puntos de Aprendizaje Clave
* **Métricas en Clasificación:** La **Precisión** se centra en la calidad de las predicciones positivas, mientras que el **Recall** se centra en la cobertura de todos los casos positivos reales. El **F1 Score** proporciona un equilibrio entre ambas.
* **Generalización del Modelo:** La **Validación Cruzada** asegura que el modelo sea robusto y utilice todos los datos disponibles para obtener una estimación general del rendimiento, previniendo el sobreajuste. El **Test Set** (conjunto de pruebas) es la prueba final con datos no vistos.
* **Mantenimiento Continuo:** La evaluación de un modelo no termina con su despliegue. La **Monitorización** continua es esencial para detectar la deriva de datos (*drift*) y determinar cuándo se necesita reentrenar o ajustar los modelos.

### Relevancia Técnica
El uso de la **API de inferencia de Hugging Face** permite a los desarrolladores implementar soluciones de ciberseguridad avanzadas (como la clasificación de URLs maliciosas) de forma rápida, sin necesidad de infraestructura pesada (GPUs) ni largos procesos de entrenamiento local. Esto optimiza los recursos del equipo de seguridad y acelera la protección contra amenazas emergentes.