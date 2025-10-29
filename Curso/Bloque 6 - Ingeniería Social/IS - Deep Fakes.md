## Informe Técnico: Deepfakes y Ciberseguridad

Documentos de Referencia: "IS - Deep Fakes.pdf"

---

### 1. Resumen Ejecutivo

Este informe técnico analiza en detalle el fenómeno de las **deepfakes** y su impacto en el ámbito de la **ciberseguridad**. Una deepfake se define como una técnica de manipulación digital muy avanzada que emplea **Inteligencia Artificial (IA)**, específicamente redes neuronales, para generar contenido multimedia (vídeos, imágenes, audios o textos) que parece auténtico a pesar de ser completamente falso. La tecnología plantea serias amenazas a la **desinformación**, la **privacidad** y la **confianza pública**. Se exploran las diversas técnicas de creación, como el *face swapping* y la *síntesis de voz*, la arquitectura de las **Redes Generativas Antagónicas (GANs)**, y el doble rol crucial de los **autoencoders**. Además, se detallan metodologías de detección basadas en la búsqueda de inconsistencias sutiles, como la **Relación de Aspecto del Ojo (EAR)** para el análisis de parpadeo y el uso de **Credenciales Verificables (VC)** como una solución criptográfica para mitigar el fraude en procesos como **KYC (Know Your Customer)**.

---

### 2. Conceptos Fundamentales

Los siguientes conceptos definen el panorama de las deepfakes y su relación con las amenazas de seguridad digital:

* **Deepfake:** Técnica de manipulación digital de contenido multimedia (vídeos, imágenes, audios o textos) que emplea **Inteligencia Artificial (IA)**, particularmente **redes neuronales**, para crear contenido falso con una apariencia extremadamente realista. Implican acciones como la inserción de caras o la modificación de expresiones faciales.
* **Red Generativa Antagónica (GAN):** Arquitectura base en la creación de deepfakes, donde dos redes neuronales interactúan:
    * **Red Generadora (Generator Network):** Su objetivo es crear nuevos datos (imágenes, vídeos, etc.) que imiten a los datos reales, buscando que sean indistinguibles de los auténticos.
    * **Red Discriminadora (Discriminator Network):** Actúa como un "juez," evaluando si el contenido creado por la Generadora es real o generado, y proporciona retroalimentación para la mejora continua del Generador.
* **Autoencoder:** Componente crucial en la generación de deepfakes y en ciberseguridad. Aprenden representaciones densas o codificadas de los datos, lo cual es vital para capturar características subyacentes como los rasgos faciales.
    * **Encoder:** Reduce la dimensionalidad de los datos originales, extrayendo solo las características esenciales y facilitando la manipulación de los datos con menor demanda computacional.
    * **Decoder:** Utiliza capas de *upsampling* para aumentar la dimensionalidad y reconstruir el contenido.
* **Face Swapping (Intercambio de Rostros):** Técnica que reemplaza el rostro de una persona en una imagen o vídeo por el de otra, manteniendo la sincronización de movimientos y expresiones de forma realista.
* **Síntesis de Voz (Voice Cloning):** Generación de habla artificial que imita las características vocales de una persona específica, utilizando algoritmos de IA que modelan patrones de voz a partir de muestras de audio.
* **Ingeniería Social:** Las deepfakes transforman las tácticas de ingeniería social al permitir la creación de contenido falso y muy convincente que facilita la manipulación y el fraude, amplificando el potencial de robo de identidad y *phishing*.
* **Credenciales Verificables (Verifiable Credentials - VC):** Solución criptográfica que cambia el paradigma de verificación de identidad, basándose en la prueba criptográfica de la información subyacente en lugar de la imagen o biometría. Se utilizan para mitigar el fraude en procesos **KYC**.

---

### 3. Procedimientos Prácticos

Se describen dos procedimientos prácticos clave para la detección de deepfakes y un enfoque de mitigación basado en criptografía:

#### 3.1. Detección de Deepfakes por Análisis de Parpadeo (Eye Blinking)

Esta técnica se centra en monitorizar la frecuencia y naturalidad del parpadeo, ya que las falsificaciones a menudo fallan al replicar estos sutiles movimientos humanos. El proceso se lleva a cabo en un entorno de programación y utiliza la **Relación de Aspecto del Ojo (EAR)** como indicador clave.

| Librería Clave | Funcionalidad Principal |
| :--- | :--- |
| **Dlib (C++)** | Detección de rostros e identificación de **puntos de referencia faciales (facial landmarks)** para localizar los ojos. |
| **OpenCV** | Procesamiento de imágenes y vídeos. |
| **SciPy Spatial** | Proporciona el módulo de distancia para calcular la separación entre puntos, esencial para determinar la apertura de los ojos. |

**Proceso Detallado de Detección:**

1.  **Inicialización de Dlib:** Se inicializan dos detectores:
    * `dlib.get_frontal_face_detector()`: Identifica rostros orientados hacia la cámara, devolviendo una lista de rectángulos para cada cara detectada.
    * `dlib.shape_predictor`: Utiliza un modelo pre-entrenado para identificar 68 puntos de referencia faciales específicos, incluyendo los contornos de los ojos.
2.  **Procesamiento de Frames:** El vídeo se carga usando OpenCV y se procesa cuadro por cuadro (*frame*) dentro de un bucle. Cada cuadro se convierte a **escala de grises** para optimizar la eficiencia en la detección de rostros y *landmarks*.
3.  **Cálculo Dinámico del EAR:** Para cada rostro detectado, el predictor de Dlib se usa para encontrar los *landmarks* faciales.
    * Se extraen los puntos de referencia específicos de los ojos izquierdo y derecho.
    * Se calcula la **EAR** para ambos ojos y el promedio. Un valor de EAR menor indica que el ojo está más cerrado. La fórmula calcula el EAR como el promedio de las dos distancias verticales del ojo dividido por la distancia horizontal, proporcionando una medida normalizada.
4.  **Detección de Parpadeo:**
    * El valor de EAR se añade a una lista (`Earlist`).
    * Se mantiene un promedio de los últimos 10 datos (ej. `EAR AVG`) para establecer un **umbral dinámico** que se ajusta a variaciones de iluminación o de usuario.
    * Si el EAR está por debajo de este umbral, se incrementa un contador de *frames* (`frame_counter`).
    * Si el EAR sube por encima del umbral y el `frame_counter` es suficiente (ej. mayor o igual a 2 *frames*), se incrementa la cuenta total de parpadeos (`blincount`).
    * *Nota:* El sistema es sensible a la orientación frontal de la cara o a la correcta calibración de parámetros como el EAR o el número de *frames*.

#### 3.2. Detección de Deepfakes por Similitud de Audio (Voces Clonadas)

Este análisis es fundamental para detectar voces clonadas y crear una huella vocal para la verificación de oradores. Se basa en la comparación de parámetros extraídos de **espectrogramas**.

* **Espectrogramas:** Representaciones visuales de las características espectrales del sonido, que permiten aplicar técnicas de procesamiento de imágenes para identificar discrepancias sutiles entre voces.
* **Librería Clave:** Se utiliza **Librosa** para cargar archivos, calcular características espectrales y visualizar espectrogramas.

**Características Espectrales Clave para Comparación:**

| Característica | Descripción | Indicador de Discrepancia (Diferencia Alta) |
| :--- | :--- | :--- |
| **Centroide Espectral** | El "centro de masa" de la distribución de frecuencias. | Sugiere distribuciones de frecuencia distintas en el tiempo. |
| **Planitud Espectral** | Mide cuán "plano" es el espectrograma (similar a tono puro vs. ruido). | Sugiere variaciones en las características de tono o ruido. |
| **Roll-off Espectral** | Frecuencia por debajo de la cual se encuentra un porcentaje específico de la energía total del espectro. | Sugiere distribuciones de energía en frecuencia muy diferentes. |

**Cálculo de Similitud:** La suma de las diferencias absolutas medias en estas tres características genera una **puntuación de similitud**. Cuanto menor sea la puntuación, mayor es la similitud entre las voces. Esta técnica es una base para prevenir ataques de suplantación de identidad mediante clonación de voces.

#### 3.3. Mitigación de Fraude Deepfake en KYC con Credenciales Verificables (VC)

El enfoque tradicional de KYC (*Know Your Customer*) se basa en la verificación biométrica por imagen o vídeo (ej., *liveness check* mediante parpadeo o movimiento de cabeza). Un deepfake sofisticado puede superar el *liveness check* y corromper la entrada del sistema de verificación.

Las **Credenciales Verificables (VC)** representan una solución que neutraliza el ataque de deepfake al eliminar la dependencia de la imagen visual como prueba de identidad.

**Flujo de Proceso Detallado con VC:**

1.  **Emisión de la Credencial:**
    * El usuario realiza un KYC inicial (una única vez) con un **Emisor** de confianza (ej. gobierno).
    * El Emisor, tras verificar la identidad, crea una VC que contiene **atributos matemáticos** (ej., "mayor de 18 años") en lugar de datos sensibles o imágenes.
    * El Emisor firma criptográficamente la credencial y se la envía al **Titular** (el usuario), quien la almacena en una *wallet* digital.
2.  **Verificación y Cero Conocimiento (Zero-Knowledge Proof - ZKP):**
    * Cuando el Titular quiere interactuar con un **Verificador** (ej., un banco para abrir una cuenta), este solicita una **Prueba de Cero Conocimiento** o una credencial específica.
    * El Titular crea una prueba criptográfica a partir de su VC, confirmando solo los atributos necesarios (ej., que "tiene un DNI válido") *sin revelar la credencial completa*. **No se transmite ninguna imagen, vídeo o documento**.
    * El Verificador recibe la prueba matemática y utiliza la clave pública del Emisor para validar su autenticidad e inalterabilidad.

**Mitigación de Fraude:** La clave es que el proceso se centra en la validez de una **firma digital emitida por una autoridad confiable**, no en la apariencia visual en tiempo real del usuario. Un atacante con un deepfake no puede generar una firma válida, ya que necesitaría la credencial original firmada criptográficamente por el Emisor o la capacidad de falsificar la clave privada del Emisor, lo cual es computacionalmente inviable.

---

### 4. Conclusiones y Puntos Clave

#### Importancia y Beneficios de Seguridad

El análisis de deepfakes subraya la necesidad de mejorar la **alfabetización digital** y establecer **medidas de seguridad sólidas** para combatir la desinformación y preservar la confiabilidad de los medios digitales.

* **Detección de Anomalías:** Las técnicas de detección basadas en artefactos, discrepancias faciales, patrones de parpadeo y sincronía audiovisual son fundamentales para identificar contenido manipulado. Los **autoencoders**, a pesar de su doble rol en la creación, son importantes herramientas en ciberseguridad para la detección de anomalías y la identificación de comportamientos inusuales.
* **Integridad de la Información y Seguridad Nacional:** La implementación de sistemas de vigilancia avanzados es crucial para garantizar la veracidad de la información y proteger la seguridad nacional frente a deepfakes que podrían manipular elecciones o incitar a conflictos sociales.
* **Protección Criptográfica (VC):** La adopción de **Credenciales Verificables** ofrece un método de verificación de identidad intrínsecamente seguro que invalida el vector de ataque basado en la manipulación de medios visuales, superando las vulnerabilidades del KYC tradicional.

#### Puntos de Aprendizaje Clave

* **Naturaleza Evolutiva de la Amenaza:** La tecnología de deepfakes avanza rápidamente, superando los marcos legales y dificultando la autenticación, lo que exige estrategias de detección y regulación adaptables.
* **Dualidad de la IA:** Herramientas de IA como los autoencoders tienen un doble rol: se usan tanto para crear deepfakes cada vez más convincentes como para detectarlos y mejorar la ciberseguridad.
* **Importancia del Liveness Check:** La irregularidad en patrones biométricos naturales como el parpadeo es un indicio significativo de falsificación, haciendo del análisis de parpadeo una técnica de defensa esencial.
* **Cambio de Paradigma en Verificación:** El futuro de la verificación de identidad se dirige hacia la **autenticación criptográfica** (VC/ZKP) en lugar de la prueba visual, debido a la facilidad con la que la biometría visual puede ser manipulada por la IA generativa.
* **Regulación y Ética:** Es crucial encontrar un equilibrio entre la regulación para proteger a las personas (como el **Acta de IA** en Europa) y la preservación de la libertad de expresión e innovación tecnológica.

#### Relevancia Técnica

Los procedimientos aprendidos tienen una alta relevancia técnica en un entorno profesional:

* **Desarrollo de Sistemas de Detección:** El conocimiento de librerías como Dlib, OpenCV y SciPy es fundamental para que los profesionales desarrollen y ajusten sistemas de detección biométrica basados en el análisis facial dinámico.
* **Análisis Forense Digital:** La comprensión de características espectrales clave (Centroide, Planitud, Roll-off) y el uso de herramientas como Librosa son esenciales para el análisis forense de audio y la identificación de voces clonadas.
* **Implementación de Soluciones Criptográficas:** La comprensión del modelo de **Credenciales Verificables** y la **Prueba de Cero Conocimiento (ZKP)** es clave para diseñar arquitecturas de seguridad que cumplan con regulaciones como el KYC y el Acta de IA, implementando un método de verificación de identidad inalterable y seguro.