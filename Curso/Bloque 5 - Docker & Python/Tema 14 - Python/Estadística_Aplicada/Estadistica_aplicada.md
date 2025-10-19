# Estadística Aplicada: Introducción a la Estadística

## Introducción a la Estadística

### Importancia de la Estadística en IA y Redes Neuronales

La estadística es una herramienta fundamental para el desarrollo de la inteligencia artificial (IA), ya que proporciona:

* Métodos para analizar datos
* Herramientas para validar modelos
* Inferencia estadística para tomar decisiones
* Manejo de la incertidumbre
* Optimización de algoritmos

**Aplicaciones comunes:**

* Modelos predictivos
* Análisis exploratorio
* Selección de variables (reducción de dimensiones)
* Evaluación del rendimiento de modelos

###  ¿Qué es la estadística?

Es la rama de las matemáticas encargada de recolectar, organizar, analizar, interpretar y presentar datos. Se divide principalmente en dos ramas:

#### Estadística Descriptiva

* Describe y resume datos.
* Herramientas: media, mediana, moda, desviación estándar, histogramas, boxplots.

#### Estadística Inferencial

* Realiza generalizaciones sobre una población a partir de una muestra.
* Herramientas: intervalos de confianza, pruebas de hipótesis, regresión, ANOVA.

---

## Estadística Descriptiva: Medidas

### Medidas de Tendencia Central

#### Media aritmética

Promedio de los valores
Fórmula: $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$

**Ejemplo:**
Datos: 5, 7, 8, 10
$\bar{x} = (5 + 7 + 8 + 10)/4 = 7.5$

#### Mediana

Valor que ocupa la posición central al ordenar los datos.

* Si $n$ es impar: valor en posición $(n+1)/2$
* Si $n$ es par: promedio entre las posiciones $n/2$ y $n/2 + 1$

**Ejemplo:**
Datos: 4, 6, 9, 11, 15 → Mediana = 9

#### Moda

Valor que más se repite.
Puede haber más de una (multimodal) o ninguna (amodal).

**Ejemplo:**
Datos: 3, 3, 4, 5, 6, 6, 6 → Moda = 6

### Medidas de Dispersión

#### Rango

Diferencia entre el máximo y mínimo.
Fórmula: $R = x_{max} - x_{min}$

**Ejemplo:**
Datos: 5, 10, 15 → Rango = 15 - 5 = 10

#### Varianza

Mide la dispersión respecto a la media.
Fórmula poblacional: $\sigma^2 = \frac{1}{N} \sum (x_i - \bar{x})^2$

#### Desviación Estándar

Raíz cuadrada de la varianza.
Facilita la interpretación porque está en las mismas unidades que los datos.

**Ejemplo:**
Datos: 2, 4, 4, 4, 5, 5, 7, 9
Media = 5
Varianza = 4
Desviación estándar = 2

#### Percentiles

* Dividen el conjunto ordenado en 100 partes
* P25 (1er cuartil), P50 (mediana), P75 (3er cuartil)

**Uso:**

* Analizar distribución
* Identificar outliers (por debajo del P5 o por encima del P95)

---

## Medidas de Forma

### Asimetría

Mide la simetría de la distribución

**Tipos:**

* Positiva (cola a la derecha)
* Negativa (cola a la izquierda)
* Simétrica (asimetría ≈ 0)

**Ejemplo:**

* Ingresos (asimétrica positiva)
* Edad de jubilación (asimétrica negativa)

### Curtosis

Mide la forma del pico y el grosor de las colas

**Tipos:**

* Mesocúrtica: curtosis = 0 (normal)
* Leptocúrtica: > 0, colas pesadas (más outliers)
* Platicúrtica: < 0, colas ligeras (menos outliers)

**Ejemplo:**

* Datos financieros con valores extremos: leptocúrtica
* Datos homogéneos como temperatura: platicúrtica

---

## Dataset de Trabajo

**Fuente:** Kaggle - Annual Salary Reports

* 100,000 registros: 50k hombres, 50k mujeres
* Variables: salario, años de experiencia, edad, ubicación, educación, etc.
* Propósito: explorar la relación entre factores y el salario

---

## Ejercicios Prácticos (para programar en Python)

* Calcular la media, mediana y moda de un conjunto de datos de salarios
* Obtener la varianza y desviación estándar
* Visualizar histograma y boxplot para detectar outliers
* Comparar percentiles entre hombres y mujeres
* Medir la asimetría y curtosis de los salarios

---

## Conclusión

La estadística descriptiva es el primer paso fundamental en cualquier análisis de datos. Permite conocer el comportamiento general de los datos, detectar valores atípicos y preparar el terreno para aplicar estadística inferencial. Dominar estas herramientas es clave en ciencia de datos, inteligencia artificial y múltiples disciplinas.
