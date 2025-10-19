# Principios SOLID

## Principios SOLID y Repaso de POO en Python

### Repaso a la Programación Orientada a Objetos (POO)

La **programación orientada a objetos (POO)** es un paradigma de desarrollo de software basado en el concepto de "objetos". Un objeto representa una entidad del mundo real con datos (**atributos** o **propiedades**) y comportamientos (**métodos** o **funciones**). En lugar de estructurar el código en funciones y datos separados, la POO organiza el programa en torno a objetos que interactúan entre sí. Esto permite modelar sistemas complejos de forma más natural, ya que pensamos en términos de objetos (p.ej., un **Coche**, un **Usuario**, un **Pedido**) con sus propias características y acciones.

## Clases y objetos

Una **clase** es una plantilla o modelo a partir del cual se crean objetos. Define los **atributos** (datos) y **métodos** (comportamientos) que tendrán los objetos de ese tipo. Podemos imaginar una clase como un molde y cada objeto como una instancia concreta salida de ese molde. Por ejemplo, podríamos tener una clase **Perro** con atributos como nombre y edad, y métodos como `ladrar()`; cada objeto creado de esa clase (`mi_perro = Perro("Fido", 3)`) sería un perro específico con su nombre y edad propios.

Dentro de la arquitectura de una clase en Python encontramos varios elementos:

- **Atributos:** Son las variables que mantienen el estado de un objeto. Pueden ser atributos de instancia (propios de cada objeto, definidos normalmente en el método `__init__`) o atributos de clase (compartidos por todas las instancias de la clase, definidos directamente en la clase).
- **Métodos de instancia:** Funciones definidas dentro de la clase que operan sobre una instancia particular. Siempre reciben `self` como primer parámetro, que representa al propio objeto. A través de `self` el método puede acceder y modificar los atributos del objeto.
- **Métodos de clase:** Son métodos que atañen a la clase en sí más que a instancias individuales. Se definen con el decorador `@classmethod` y reciben `cls` (la clase) como primer parámetro en lugar de `self`. Suelen usarse para acciones que involucran a la clase completa o para construir instancias de formas alternativas.
- **Métodos estáticos:** Se definen con `@staticmethod` y no reciben ni `self` ni `cls`. Son funciones dentro de la clase que conceptualmente pertenecen a la clase (porque están relacionadas con ella) pero no operan directamente sobre la instancia ni la clase. Sirven como funciones utilitarias agrupadas dentro del espacio de nombres de la clase.

En Python, crear una instancia (objeto) de una clase se realiza llamando a la clase como si fuera una función, lo que invoca al método constructor `__init__` definido en la clase. Por ejemplo, `perro = Perro("Fido", 3)` creará un nuevo objeto Perro ejecutando el código de `Perro.__init__` para inicializar los atributos nombre y edad de ese objeto.

> **Instancia vs Objeto:** En la práctica cotidiana, llamamos "objeto" a cualquier instancia de una clase. Una instancia es, estrictamente, el resultado de crear (instanciar) una clase, es decir, un objeto en particular. Ambos términos suelen usarse como sinónimos. Podemos decir: "mi_coche es un objeto de la clase Coche, es decir, una instancia de Coche."

Para ilustrar estos conceptos, veamos un ejemplo sencillo de clase en Python:

```python
# Ejemplo de clase Persona y herencia
class Persona:
    poblacion = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.poblacion += 1
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
    @classmethod
    def total_personas(cls):
        return cls.poblacion
    @staticmethod
    def definicion():
        print("Una persona es un ser humano.")

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera
    def saludar(self):
        print(f"Hola, soy {self.nombre} y estudio {self.carrera}")
```

En el código anterior, la clase **Persona** define un atributo de clase `poblacion` (que cuenta cuántas personas se han creado), un atributo de instancia `nombre`, un método de instancia `saludar()`, un método de clase `total_personas()` y un método estático `definicion()`. Luego definimos **Estudiante** como subclase de Persona usando la sintaxis `class Estudiante(Persona)`. Estudiante hereda los atributos y métodos de Persona, pero añade su propio atributo `carrera` y sobreescribe el método `saludar()` para personalizarlo.

Veamos cómo funciona en la práctica:

```python
p1 = Persona("Ana")
p2 = Estudiante("Juan", "Ingeniería")
p1.saludar()  # Hola, soy Ana
p2.saludar()  # Hola, soy Juan y estudio Ingeniería
print(Persona.total_personas())  # 2
Estudiante.definicion()  # Una persona es un ser humano.
```

En este ejemplo, `p1` es una instancia de Persona y `p2` es una instancia de Estudiante. La llamada `p1.saludar()` ejecuta el método definido en Persona, mientras que `p2.saludar()` ejecuta el método sobreescrito en Estudiante. Observa que, gracias a la herencia, un Estudiante es una Persona: por eso, al hacer `Estudiante("Juan", "Ingeniería")`, se invoca internamente el constructor de Persona para inicializar el nombre. Además, Estudiante hereda el atributo de clase `poblacion` y el método `total_personas()` de Persona – no tuvimos que redefinirlos en Estudiante. Esto demuestra la reutilización de código que aporta la herencia.

Por otro lado, el método de clase `Persona.total_personas()` devuelve la cuenta de instancias creadas (utiliza `cls.poblacion` para referirse al atributo de clase). El método estático `Persona.definicion()` imprime una definición general y no depende de ninguna instancia ni de la clase en sí.

## Abstracción

La **abstracción** consiste en identificar las características y comportamientos fundamentales de un objeto, separándolos de los detalles más específicos. En términos prácticos, abstraemos cuando definimos una clase enfocándonos en qué hace un objeto en lugar de cómo lo hace. Esto implica diseñar una interfaz pública clara (conjunto de métodos) que represente las acciones esenciales, ocultando la complejidad interna.

En otras palabras, una abstracción se concentra en la visión externa de un objeto: expone solo lo necesario para usarlo e ignora los pormenores internos. Por ejemplo, un objeto **Coche** puede ofrecer métodos como `acelerar()` o `frenar()` (lo que hace), sin que quien lo use necesite saber detalles de cómo el motor incrementa la velocidad o cómo funcionan exactamente los frenos. La abstracción nos permite tratar con conceptos de alto nivel y despreocuparnos de la implementación interna, lo que simplifica la resolución de problemas complejos al manejar solo las características relevantes.

## Encapsulación

La **encapsulación** es el principio de ocultar los detalles internos de un objeto y controlar el acceso a sus datos. Esto se logra agrupando los atributos (datos) y métodos que manipulan esos datos dentro de la misma unidad (la clase), y restringiendo el acceso directo a los atributos. En Python, podemos usar convenciones (como prefijos `_` o `__`) para indicar que ciertos atributos o métodos son privados y no deberían usarse desde fuera de la clase, aunque la accesibilidad real es por convención. Al aplicar encapsulación, un objeto maneja sus propios datos internamente y expone una interfaz pública mediante métodos (por ejemplo, getters y setters) que validan y controlan el acceso a esos datos. De este modo, protegemos la consistencia del estado interno del objeto y evitamos que otras partes del código dependan de su representación específica.

## Polimorfismo

El **polimorfismo** significa "muchas formas". En POO, se refiere a la capacidad de diferentes clases de ser usadas de forma intercambiable a través de una misma interfaz común, produciendo resultados adaptados a su tipo específico. Dicho de forma simple: distintos objetos pueden responder al mismo mensaje (misma llamada de método) de maneras distintas.

Existen dos manifestaciones clásicas del polimorfismo:

- **Polimorfismo mediante herencia (sobreescritura):** Ocurre cuando una superclase define un método y varias subclases lo sobreescriben con comportamientos diferentes. Luego, si se invoca ese método sobre una referencia del tipo de la superclase, en tiempo de ejecución se ejecutará la versión correspondiente a la subclase real del objeto. Por ejemplo, supongamos una clase base **Animal** con un método `hacer_sonido()`. Podemos tener subclases **Perro**, **Gato** y **Vaca** que implementen `hacer_sonido()` de forma distinta (el perro ladra, el gato maúlla, la vaca muge). Si tenemos una lista de **Animal** que en realidad contiene perros, gatos y vacas, al iterar y llamar `animal.hacer_sonido()`, cada objeto ejecutará su propia versión del método. Este es el polimorfismo típico de las jerarquías de herencia.
- **Polimorfismo por interfaces o duck typing:** En lenguajes estáticos se refiere a varias clases no relacionadas por herencia pero que implementan la misma interfaz (conjunto de métodos), pudiendo ser tratadas uniformemente a través de esa interfaz. En Python, gracias a su naturaleza dinámica, esto sucede de forma natural a través del duck typing: "si camina como pato y suena como pato, es un pato". Es decir, no importa de qué clase provenga un objeto; si tiene los métodos o atributos adecuados, podemos usarlo en cierto contexto. Por ejemplo, dos clases no relacionadas podrían ambas tener un método `guardar()`; podemos escribir código que llame a `obj.guardar()` sin preocuparse de la clase exacta de `obj`. Mientras el objeto tenga ese método, el llamado funcionará. Este tipo de polimorfismo no requiere herencia, sólo que los objetos cumplan con la interfaz esperada (aunque sea de manera informal).

El polimorfismo aumenta la flexibilidad del código. Podemos escribir funciones o métodos que operen con objetos abstractos (por ejemplo, cualquier **Figura** que tenga método `area()`), y esas funciones podrán trabajar con nuevas clases de objetos en el futuro sin modificarse, siempre que las nuevas clases respeten la interfaz esperada.

> **Ejemplo de polimorfismo:**

```python
class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")
class Vaca(Animal):
    def hacer_sonido(self):
        print("Muu!")

animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    animal.hacer_sonido()
```

Cada iteración llamará a `hacer_sonido()` del objeto actual en la lista. Gracias al polimorfismo, el resultado será diferente según si el objeto es **Perro**, **Gato** o **Vaca**, pero `presentar_animal` no necesita saberlo; trata a todos simplemente como **Animal**. Esto demuestra cómo objetos de clases distintas pueden ser tratados de manera uniforme a la vez que actúan de forma distinta internamente.

---

## Herencia vs Composición

A la hora de diseñar la estructura de un programa orientado a objetos, dos mecanismos muy importantes para reutilizar código y estructurar funcionalidades son la **herencia** y la **composición**. Ambos permiten construir sistemas complejos a partir de componentes más simples, pero funcionan de manera distinta y es crucial saber escoger cuál conviene en cada situación.

### Herencia

Como vimos, es una relación de tipo "es un/una". Una clase hija extiende (especializa) a una clase padre. Esto implica una relación jerárquica entre clases. Por ejemplo, un **EmpleadoGerente** podría heredar de **Empleado** porque conceptualmente es un empleado, pero con características adicionales. Mediante la herencia, la subclase hereda atributos y métodos, pudiendo reutilizar código y sobrescribir comportamiento.

#### Ventajas de la herencia:

- **Reutilización de código:** La herencia permite definir funcionalidades comunes en la clase padre y heredarlas automáticamente en múltiples subclases, evitando duplicación. Por ejemplo, si varios tipos de usuarios comparten métodos, se pueden colocar en una superclase **Usuario** en lugar de implementarlos en cada subclase.
- **Polimorfismo:** Las subclases pueden ser tratadas como instancias de la superclase, lo que habilita el polimorfismo. Un código que funcione con la clase base podrá trabajar con cualquier subclase sin modificaciones, aprovechando la sobreescritura de métodos. (Ej.: una función que procesa un **Empleado** podrá recibir un **EmpleadoGerente** o **EmpleadoTemporal** sin saberlo, y gracias al polimorfismo ejecutará el comportamiento específico de cada uno).
- **Sobreescritura de métodos:** La herencia hace posible que una subclase adapte o extienda comportamientos definidos en la superclase. Esto proporciona un mecanismo claro para personalizar la funcionalidad: se mantiene la interfaz (el método se llama igual) pero se cambia la implementación interna en la subclase.
- **Desarrollo guiado por un modelo establecido:** Al utilizar herencia, especialmente en entornos de frameworks, a veces la estructura de clases base guía el desarrollo de las subclases. Por ejemplo, un framework puede proveer clases base que uno hereda y llena con lógica específica, siguiendo un esquema predefinido. Esto puede hacer el desarrollo más rápido al estar "guiado" por esa estructura (se sabe qué métodos sobreescribir, etc.).

#### Desventajas de la herencia:

- **Menor flexibilidad en cambios ágiles:** La herencia crea una conexión fuerte entre la subclase y la superclase. Si la superclase cambia, las subclases pueden verse afectadas. En proyectos ágiles con requisitos cambiantes, una jerarquía de herencia rígida puede dificultar refactors o nuevos requerimientos que no encajan en la jerarquía existente.
- **“Fiesta de los overrides”:** Si la jerarquía no está bien diseñada o se abusa de la herencia, puedes terminar con numerosas subclases sobreescribiendo métodos de formas muy variadas. Esto dificulta seguir la lógica del programa, ya que el comportamiento final depende de cuál subclase se esté usando y cómo haya sobreescrito los métodos. Puede volverse confuso (de ahí la metáfora de una "fiesta" descontrolada de métodos sobreescritos).
- **Herencias demasiado profundas (análoga a "herencia de 7 niveles"):** Cuando las jerarquías de clases son muy profundas (muchos niveles de herencia), el código se vuelve difícil de entender y de mantener. Un cambio en un nivel alto puede tener efectos colaterales en múltiples niveles inferiores. Además, para comprender una subclase en el nivel 7, hay que entender todo lo que ocurre en sus 6 ancestros también. Las buenas prácticas suelen recomendar mantener las jerarquías relativamente planas (pocos niveles) y favorecer composición para evitar esto.

### Composición

Es una relación de tipo "tiene un". En lugar de extender funcionalidad mediante una subclase, la **composición** consiste en que un objeto contiene a otros objetos como parte de su estado interno, delegando en ellos ciertas tareas. Por ejemplo, una clase **Coche** puede tener un objeto **Motor** en lugar de heredar de Motor (¡un coche no es un motor, sino que tiene un motor!). La composición permite construir funcionalidad compleja ensamblando objetos más simples que colaboran.

#### Ventajas de la composición:

- **Versatilidad y modularidad:** La composición permite construir objetos complejos combinando comportamientos de otros más simples. Es fácil de extender o modificar funcionalidad cambiando qué objetos componentes se usan. Además, puedes reutilizar las mismas clases componentes en contextos totalmente diferentes. Por ejemplo, una clase **GraficoBarras** y **GraficoTarta** podrían ambos usar un objeto **CalculadorEstadisticas** común internamente; ese componente estadístico es reutilizable sin herencia.
- **Creación/destrucción dinámica de componentes:** Con composición, un objeto puede decidir en tiempo de ejecución qué componentes usar, e incluso reemplazarlos o eliminarlos durante la ejecución. La herencia, en cambio, fija el comportamiento en tiempo de definición de la clase. La composición brinda más flexibilidad en tiempo de ejecución. Por ejemplo, un objeto **Robot** podría contener un objeto **Comportamiento** que se intercambia por otro sobre la marcha para cambiar la estrategia del robot, sin cambiar la clase Robot en sí.
- **Polimorfismo mediante interfaces (comportamientos intercambiables):** Si los objetos que se contienen comparten una interfaz común, es fácil intercambiar uno por otro. Esto se ve en patrones de diseño como **Strategy** o **State**, donde la clase principal delega cierta funcionalidad en un subobjeto que cumple cierta interfaz. Cambiando ese subobjeto (que podría ser de distintas clases concretas), cambia el comportamiento. Esto se logra sin heredar múltiples variantes de la clase principal; simplemente se configura con diferentes componentes. En otras palabras, la composición va de la mano con usar interfaces específicas: se puede componer el objeto con cualquier clase que implemente la interfaz esperada.

#### Desventajas de la composición:

- La composición a veces implica escribir código delegador adicional (métodos que simplemente llaman al método del componente). Esto puede agregar algo de verbosidad.
- Puede haber una ligera sobrecarga en gestionar referencias a objetos internos, especialmente si la composición es muy granular. Sin embargo, estas desventajas suelen ser menores comparadas con los beneficios en flexibilidad.

### ¿Cuándo usar composición?

Algunas señales claras de que conviene la composición:

- No existe una relación "es un" fuerte y permanente: Si un objeto no es conceptualmente un tipo especializado de otro, mejor no forzar una herencia. Por ejemplo, un **ArchivoCSV** no es un **AnalizadorDeTexto**, aunque un analizador pueda usar un archivo; aquí usar composición (un analizador tiene un archivo) tiene más sentido.
- Necesidad de flexibilidad y cambios: Si anticipamos que ciertas funcionalidades podrían cambiar o necesitar alternarse, la composición permite intercambiar componentes fácilmente. Por ejemplo, si un programa debe poder desacoplar y reutilizar componentes (como diferentes algoritmos, motores de base de datos, estrategias de cálculo), conviene diseñar componentes intercambiables en vez de jerarquías monolíticas.
- Implementar comportamientos intercambiables: Como mencionamos, cuando tenemos variantes de cierta funcionalidad (p.ej., estrategias de ordenamiento, formatos de exportación, distintos métodos de pago), es más limpio encapsular cada variante en su propia clase (componente) y que la clase principal las utilice de forma polimórfica. Así agregamos nuevos comportamientos sin tocar el código existente.
- Relación tipo "tiene un": Si una clase lógica está compuesta de varias partes (un todo con componentes), modelarlo con composición es lo natural. Ej: una **Casa** tiene **Habitaciones**; una **Computadora** tiene una **CPU**, **RAM**, **DiscoDuro**, etc. La herencia aquí no tendría sentido.
## ¿Cuándo usar herencia? Criterios comunes para optar por herencia:

- **Existe una relación "es un" clara y estable en el tiempo:** La herencia es apropiada si el modelo de dominio realmente tiene una jerarquía natural. Por ejemplo, en un sistema de geometría, un **Cuadrado** es un tipo especial de **Rectángulo**. Si la relación es permanente y conceptual (no circunstancial), la herencia es válida.
- **Reutilización de código y comportamiento común:** Cuando varias clases comparten lógica o datos, y esa comunalidad refleja una relación conceptual, extraer una superclase puede reducir duplicación. Por ejemplo, si tienes clases **Circulo**, **Rectangulo**, **Triangulo** que todas necesitan un método `area()`, podría haber una clase abstracta **Figura** que defina la interfaz común.
- **Necesitas polimorfismo "clásico":** Si vas a tener colecciones de objetos de tipos derivados que deben ser tratados uniformemente mediante métodos sobreescritos, la herencia es el camino. Esto es típico en frameworks GUI: un contenedor maneja una lista de **ComponentesVisuales** abstractos, que pueden ser botones, textos, etc. Todos derivan de una clase base común y sobrescriben, por ejemplo, el método `dibujar()` de forma diferente. El contenedor no necesita saber los detalles: solo llama `component.dibujar()` y obtiene el resultado polimórfico adecuado.
- **Modelar el dominio con jerarquías:** A veces el propio problema a resolver se presta a una taxonomía. En biología, podrías tener clase **Animal** -> **Mamifero** -> **Canino** -> **Perro** reflejando clasificación real. En software de negocio, podrías modelar empleados -> subtipos de empleados, etc., si sus comportamientos difieren pero guardan relación jerárquica.

> En general, una recomendación común es "favorecer la composición por sobre la herencia" cuando se puede. La composición tiende a generar sistemas menos acoplados: las clases se comunican mediante interfaces bien definidas, en lugar de depender fuertemente de una estructura de herencia. La herencia, por su parte, es poderosa pero puede llevar a sistemas rígidos si no se diseña con cuidado. Por supuesto, la elección depende del contexto y ambas herramientas pueden (y suelen) coexistir en un mismo sistema.

## Ejemplo comparativo: Herencia vs Composición

Supongamos que queremos modelar algo relacionado con vehículos y motores. Tenemos una clase **Motor** con sus funcionalidades, y queremos que los coches "usen" un motor. Podríamos caer en la tentación de hacer que **Coche** herede de **Motor** para "reutilizar" sus métodos, pero conceptualmente es incorrecto. Veamos ambas aproximaciones en código simplificado:

```python
# Mal uso: herencia
class Motor:
    def encender(self):
        print("Motor encendido")
    def reparar_valvulas(self):
        print("Válvulas reparadas")
class CocheHeredandoMotor(Motor):
    def conducir(self):
        print("Conduciendo coche")

# Buen uso: composición
class Motor:
    def encender(self):
        print("Motor encendido")
    def reparar_valvulas(self):
        print("Válvulas reparadas")
class CocheConMotor:
    def __init__(self, motor):
        self.motor = motor
    def arrancar(self):
        self.motor.encender()
        print("Conduciendo coche")
```

En ambos casos logramos arrancar el motor y conducir el coche. Sin embargo, con la herencia, **CocheHeredandoMotor** es un **Motor**, lo cual no tiene sentido conceptual (un coche no es un motor). Además, **CocheHeredandoMotor** hereda cualquier otro método o atributo de **Motor** incluso si no corresponde. Por ejemplo, si **Motor** tuviera un método `reparar_valvulas()`, nuestro coche heredado también lo tendría, aunque quizás un coche debería delegar eso a su motor y no tener la lógica él mismo.

Con la composición, **CocheConMotor** tiene su propio objeto **Motor** y lo utiliza. La relación es clara: el coche contiene un motor y lo opera cuando es necesario. El código es más flexible: podríamos cambiar el tipo de motor (por ejemplo, a **MotorElectrico** o **MotorCombustion**) sin modificar la clase **CocheConMotor**, solo pasando un objeto de motor distinto o cambiando la instancia que asignamos. Con herencia, cambiar la "implementación" del motor implicaría modificar la jerarquía de herencia (quizás usar herencia múltiple o cambiar la superclase), lo cual es más engorroso.

## Principios de diseño: Cohesión y Acoplamiento

Antes de introducir los principios **SOLID** (que son principios de diseño orientado a objetos), conviene entender dos conceptos fundamentales en diseño de software: **cohesión** y **acoplamiento**. Estos conceptos nos ayudan a evaluar qué tan bien estructurado está nuestro código.

- **Cohesión:** Se refiere al grado en que las responsabilidades de un módulo (por módulo entendemos una clase, método o componente) están relacionadas entre sí y enfocadas en una tarea o propósito específico. Una clase con alta cohesión realiza una sola tarea o un grupo de tareas muy relacionadas; todos sus métodos y atributos tienen que ver con esa finalidad común. Por el contrario, una clase con baja cohesión hace muchas cosas diferentes (es "multifunción"), lo cual suele ser indeseable. La alta cohesión es buena porque significa que el módulo es claro, entendible y modificable sin afectar temas fuera de su ámbito. Idealmente, cada clase o método debería tener una responsabilidad bien definida (esto va muy ligado al primer principio SOLID que veremos pronto).

- **Acoplamiento:** Es el grado de interdependencia entre módulos de un sistema. Decimos que dos clases están fuertemente acopladas si conocen muchos detalles una de la otra, si una depende fuertemente de la implementación interna de la otra, o si cambiar una probablemente obliga a cambiar la otra. Por el contrario, un bajo acoplamiento significa que las clases se comunican a través de interfaces bien definidas, con el mínimo conocimiento necesario. El bajo acoplamiento es deseable porque facilita cambiar o reemplazar componentes del sistema sin que todo se rompa en cadena. Por ejemplo, si tenemos una clase **ProcesadorPagos** acoplada fuertemente a una clase **PayPalAPI** (porque dentro del código se crean objetos PayPal, se llaman métodos específicos de PayPal, etc.), reemplazar PayPal por otra plataforma de pago implicaría grandes cambios. Si en cambio **ProcesadorPagos** dependiera solo de una interfaz genérica **PasarelaPago**, podríamos cambiar la implementación de esa interfaz (PayPal, Stripe, etc.) con impacto mínimo.

> Buen diseño generalmente busca **alta cohesión** y **bajo acoplamiento**. Es decir, cada componente con una misión clara, y componentes lo más independientes posible entre sí. Los principios de diseño (como SOLID) nos dan guías para lograr esto.

**En resumen de esta clase:**
- Usa herencia cuando exista una relación "es un" legítima, para compartir código común y habilitar polimorfismo.
- Usa composición para construir funcionalidades combinando componentes, especialmente cuando necesitas flexibilidad o no hay una jerarquía natural.
- Mantén tus clases cohesivas (una responsabilidad principal) y desacopladas de los detalles de otras (comunicándose a través de abstracciones, no con su lógica interna).

---
# Introducción a SOLID

A partir de esta clase, vamos a estudiar los principios **SOLID**, un conjunto de cinco principios de diseño orientado a objetos formulados por Robert C. Martin (conocido como "Uncle Bob") a finales de los años 90. Estos principios son pautas que ayudan a escribir código más mantenible, extensible y robusto. En particular, están enfocados en lograr sistemas con alta cohesión y bajo acoplamiento, como discutimos anteriormente.

**SOLID** es un acrónimo que corresponde a cinco principios:
- **S** – Single Responsibility Principle (Principio de Responsabilidad Única)
- **O** – Open/Closed Principle (Principio Abierto/Cerrado)
- **L** – Liskov Substitution Principle (Principio de Sustitución de Liskov)
- **I** – Interface Segregation Principle (Principio de Segregación de Interfaces)
- **D** – Dependency Inversion Principle (Principio de Inversión de Dependencias)

Estos principios fueron introducidos por primera vez por el famoso ingeniero de software Robert J. Martin, con el objetivo de crear código comprensible, legible y comprobable en el que muchos desarrolladores puedan trabajar en colaboración. No son reglas absolutas, sino guías que, de aplicarse, tienden a producir diseños de clases más limpios y adaptables a cambios. Muchas metodologías de desarrollo ágil y buenas prácticas modernas recomiendan seguirlos.

Antes de entrar al primero de ellos, recordemos brevemente: cohesión y acoplamiento. Los principios **SOLID**, en conjunto, buscan aumentar la cohesión (cada módulo con responsabilidad clara) y reducir el acoplamiento (mínimas dependencias innecesarias entre módulos). Veremos que el **SRP** está directamente relacionado con mantener alta cohesión, el **DIP** con reducir acoplamiento, etc.

# Principio de Responsabilidad Única (Single Responsibility Principle – SRP)

El **Principio de Responsabilidad Única** establece que "una clase debe tener una, y solo una, razón para cambiar". Dicho de otro modo, cada clase (o módulo) debería encargarse de una sola responsabilidad o funcionalidad dentro del sistema.

Este principio aboga por la claridad de propósito de las clases:
- Si una clase se dedica exclusivamente a una cosa, cualquier cambio en esa área de funcionalidad resultará en modificaciones a esa clase (lo cual es lógico). Y solo debería modificarse si hay cambios en esa responsabilidad.
- Si en cambio una clase hace dos o más cosas diferentes, podríamos tener múltiples motivos independientes para alterarla, rompiendo el principio. Por ejemplo, imaginemos una clase **GestorInforme** que calcula datos y además escribe esos datos a un archivo. Son dos responsabilidades distintas (cálculo y persistencia). Un cambio en el formato de archivo afectaría a la clase, aunque no tenga que ver con el cálculo, y viceversa.

### ¿Por qué es beneficioso el SRP? Varias razones:
- **Más fácil de entender:** Si una clase tiene una sola responsabilidad, su nombre y sus métodos deben reflejar claramente esa tarea. Es más fácil para un desarrollador leerla y entender qué hace.
- **Mantenimiento más sencillo:** Los cambios en requisitos tienden a estar aislados. Si se altera la lógica de negocio de cierta funcionalidad, solo debería requerir cambios en la clase encargada de esa funcionalidad. No habrá efectos colaterales inesperados en otras partes, porque esas otras partes están en clases separadas.
- **Mayor cohesión:** El SRP prácticamente define la cohesión alta. Al cumplir SRP, estamos asegurando que la clase agrupa funcionalidades altamente relacionadas (de hecho, una funcionalidad).
- **Reutilización de código:** Clases pequeñas y enfocadas pueden reutilizarse o reubicarse en diferentes contextos más fácilmente que clases monolíticas. Por ejemplo, una clase que solo formatea informes podría usarse en distintos proyectos si está desacoplada de otras cuestiones.

En resumen, aplicar SRP significa evitar las clases tipo "navaja suiza" o "Dios" (God objects) que hacen de todo un poco, y en su lugar tener muchas clases, cada una experta en su cometido.

### Un ejemplo concreto (violación vs. cumplimiento del SRP):

Imaginemos una situación sencilla: necesitamos generar un informe a partir de unos datos y guardar ese informe en un archivo. Podemos hacerlo de dos maneras:
- **Clase única que hace todo (viola SRP):** Una clase que tome los datos, genere el contenido del informe y además escriba ese contenido en un archivo.
- **Dos clases separadas (cumple SRP):** Una clase que se encargue de la generación de contenido del informe, y otra clase que se ocupe de la tarea de guardar/exportar contenidos a archivos. Así, cada una tiene su responsabilidad.

Primero veamos el diseño 1 (violando SRP):

```python
class GestorInforme:
    def __init__(self, datos):
        self.datos = datos
    def calcular_total(self):
        return sum(self.datos)
    def guardar_archivo(self, nombre_archivo):
        total = self.calcular_total()
        with open(nombre_archivo, "w") as f:
            f.write(str(total))
```

En este diseño, la clase **GestorInforme** hace dos cosas: formatea el informe (calculando el total) y también sabe cómo escribirlo en un archivo. ¿Qué problemas puede traer? Si mañana decidimos guardar el informe en formato PDF en lugar de texto plano, habría que modificar esta clase (responsabilidad de guardado). Si por otro lado cambia la manera de calcular el total o el contenido del informe, también habría que modificarla (responsabilidad de generación). **GestorInforme** tiene entonces dos razones distintas para cambiar, incumpliendo SRP. Además, la parte de guardado a archivo quizá podría ser útil para otras clases (por ejemplo, para guardar otro tipo de reportes o exportar datos), pero ahora está acoplada al cálculo específico de informes de ventas.

Veamos el diseño 2 (aplicando SRP):

```python
class InformeVentas:
    def __init__(self, datos):
        self.datos = datos
    def generar(self):
        return sum(self.datos)

class ExportadorArchivos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    def guardar(self, contenido):
        with open(self.nombre_archivo, "w") as f:
            f.write(str(contenido))
```

Ahora tenemos dos clases:
- **InformeVentas** que se encarga solo de la lógica de generación del informe (sumar los datos y devolver el total).
- **ExportadorArchivos** que se encarga solo de la lógica de guardar contenido en un archivo (no sabe nada de qué contiene la cadena, puede ser un informe de ventas u otra cosa).

Cada clase tiene una única responsabilidad y, por ende, una razón para cambiar. Si queremos cambiar el formato del informe, modificamos **InformeVentas**. Si queremos cambiar la forma de persistir archivos (por ejemplo, usar codificación UTF-8 distinta, o guardar en la nube en vez de disco), modificamos **ExportadorArchivos**. Notemos también que **ExportadorArchivos** es potencialmente reutilizable: podríamos usarlo para guardar cualquier texto en archivo (no solo informes de ventas), lo cual ejemplifica la ventaja de reutilización gracias a SRP.

**Beneficios observados:** Más cohesión (cada clase es experta en lo suyo) y menos acoplamiento (la generación de informes no depende de detalles de archivos, y el exportador no depende de cómo se calculan los datos).

### Ventajas del SRP:
1. **Claridad de la responsabilidad:** Al tener una clase un objetivo claro, es más fácil nombrarla, documentarla y entenderla.
2. **Facilita el mantenimiento:** Los cambios se localizan. Un cambio = una clase a modificar, idealmente.
3. **Promueve la cohesión:** La clase concentra funciones afines. (De hecho, SRP y cohesión van de la mano: cumplir SRP implica alta cohesión).
4. **Facilita la reutilización del código:** Clases pequeñas y bien enfocadas pueden integrarse en diferentes programas o contextos sin depender de cosas extrañas. En el ejemplo, podríamos usar **ExportadorArchivos** en otro proyecto que necesite guardar textos, sin llevarnos lógica de informes que no aplica.

---

# Principio Abierto/Cerrado (Open/Closed Principle – OCP)

El **Principio Abierto/Cerrado** establece que “un artefacto de software (clase, módulo, función, etc.) debe estar abierto para su extensión, pero cerrado para su modificación”. En términos prácticos, significa que deberíamos diseñar nuestras clases y módulos de tal forma que podamos agregar nuevas funcionalidades sin tener que cambiar el código ya existente en esas clases/módulos.

Este principio suena un poco paradójico al inicio, ¿cómo es posible extender algo sin modificarlo? La clave suele estar en usar abstracciones y mecanismos como la herencia, el polimorfismo, la composición o la inyección de dependencias, de modo que el comportamiento pueda ampliarse creando nuevos componentes, en lugar de alterando los ya probados.

**Ejemplo intuitivo:** Supongamos que tenemos una clase que procesa pagos y originalmente solo soporta pagos con tarjeta. Si luego queremos soportar pagos con PayPal, idealmente no deberíamos tener que abrir la clase original y modificar su código (riesgo de introducir bugs en funcionalidad que ya funcionaba). En vez de eso, la solución OCP sería hacer que la clase de pagos acepte alguna interfaz genérica de "método de pago" e introducir un nuevo componente (clase) que implemente esa interfaz para PayPal. La clase de pagos original se mantiene intocada (cerrada a modificación), pero el sistema en conjunto admite ahora un método de pago nuevo (extensión).

```python
class Pago:
    def procesar_pago(self, monto):
        pass
class PagoPayPal(Pago):
    def procesar_pago(self, monto):
        # Lógica para procesar pago con PayPal
        pass
class PagoTarjetaCredito(Pago):
    def procesar_pago(self, monto):
        # Lógica para procesar pago con tarjeta de crédito
        pass
```

#### Beneficios del Principio Abierto/Cerrado

- **Facilita el mantenimiento y la evolución a largo plazo:** Si añadimos nuevas características extendiendo en lugar de modificando, evitamos romper el código existente. El núcleo original permanece estable y probado funcional.
- **Mejora la modularidad y reutilización:** Las extensiones suelen venir en forma de nuevas clases o funciones que implementan cierta interfaz o derivan de cierta clase base. Esto favorece un diseño modular donde cada nueva funcionalidad está encapsulada en un módulo separado. Además, el código existente (estable) se puede reutilizar tal cual, sin alterarlo.
- **Reduce el riesgo de errores al modificar código existente:** Cada vez que tocamos código ya escrito (especialmente si estaba funcionando bien), existe el riesgo de introducir regresiones (bugs). Al seguir OCP, minimizamos ese riesgo porque las mejoras se realizan añadiendo nuevo código. El código existente permanece "congelado".
- **Promueve un diseño más flexible y extensible:** Desde el momento de concebir una clase, pensar en OCP nos lleva a estructurarla para la extensión. Por ejemplo, usar métodos abstractos, interfaces, comprobar tipos de manera polimórfica en lugar de condicionales rígidos, etc. Esto hace que el sistema esté preparado para crecer en funcionalidades sin necesidad de reescrituras grandes.

## Técnicas para lograr OCP en Python

Python, al ser dinámico, nos da mucha flexibilidad, pero a nivel de diseño orientado a objetos aplicamos OCP principalmente de las siguientes maneras:

- **Herencia y Polimorfismo:** Diseñar clases base (abstractas o concretas) que definan comportamientos genéricos, y luego permitir que las subclases sobreescriban o implementen detalles específicos. El código que usa la clase base (o referencias de ese tipo) no necesita cambiar cuando se introducen nuevas subclases. Ejemplo: una clase base `Figura` con método `area()`. Podemos agregar nuevas formas (`Círculo`, `Triángulo`, etc. como subclases) sin modificar la clase `Figura` ni el código que la utiliza, porque cada nueva subclase sabe calcular su área.
- **Composición y Estrategia:** Definir clases que trabajen con interfaces o clases abstractas para cierta funcionalidad interna, permitiendo inyectar diferentes implementaciones. Por ejemplo, una clase `Ordenador` que tenga un atributo `estrategia_ordenamiento` de tipo interfaz `AlgoritmoOrdenamiento`. Si inicialmente usamos Burbuja, y luego queremos Quicksort, simplemente creamos una clase `QuickSort` que implemente la interfaz y la asignamos; la clase `Ordenador` en sí no cambia.
- **Funciones de orden superior o parámetros configurables:** En Python podríamos pasar funciones como parámetros para alterar comportamientos, en lugar de hacer condicionales dentro del método. Esto es una forma de extensión también (pasar un callback, por ejemplo, sin cambiar la función contenedora).

### Ejemplo: Cálculo de áreas de figuras geométricas

**Enfoque no OCP:**

```python
def calcular_area(figura):
    if figura['tipo'] == 'circulo':
        return math.pi * figura['radio'] ** 2
    elif figura['tipo'] == 'rectangulo':
        return figura['base'] * figura['altura']
# Agregando nueva figura viola OCP
figuras = [
    {'tipo': 'circulo', 'radio': 5},
    {'tipo': 'rectangulo', 'base': 4, 'altura': 3}
]
for f in figuras:
    print(calcular_area(f))
```

Este diseño funciona para círculos y rectángulos. Pero violemos OCP agregando una nueva figura:

```python
figuras.append({'tipo': 'triangulo', 'base': 3, 'altura': 4})
for f in figuras:
    print(calcular_area(f)) # La función 'calcular_area' tendría que modificarse.
```

Cada nueva clase figura obliga a modificar el código existente (la función `calcular_area`). Esto puede introducir errores en casos ya manejados (¿y si en una edición accidental rompo el caso de rectángulo?), además de no escalar: la función crece en complejidad con cada caso. Está cerrada a extensión (no puedo añadir fácilmente nuevas figuras sin modificarla).

**Cumpliendo OCP (diseño orientado a objetos polimórfico):**

```python
from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        import math
        return math.pi * self.radio ** 2
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
def imprimir_area(figura: Figura):
    print(figura.area())
# Uso
fig1 = Circulo(5)
fig2 = Rectangulo(4, 3)
imprimir_area(fig1) # llama a Circulo.area()
imprimir_area(fig2) # llama a Rectangulo.area()
```

En este diseño, la clase base abstracta `Figura` declara el método `area()`. Las clases concretas lo implementan. La función `imprimir_area` no tiene lógica condicional, simplemente confía en el polimorfismo: sabe que cualquier `Figura` tiene un método `area()`.

Ahora, cuando agregamos `Triangulo`, no tocamos ni `Figura` ni las otras clases ni la función `imprimir_area`. El código existente permanece cerrado a modificaciones. `Triangulo` extiende el sistema añadiendo un nuevo tipo de figura, y todo sigue funcionando. Hemos logrado extensión sin modificación.

> Nota: Este ejemplo muestra herencia y polimorfismo, pero podríamos haberlo hecho con composición o estrategias en otros contextos. Lo importante es evitar los códigos monolíticos con múltiples if/elif que delatan violación de OCP.

Otro ejemplo que suele citarse para OCP es el de estrategias algorítmicas: por ejemplo, algoritmos de ordenamiento (burbuja, merge sort, quicksort, etc.). Un diseño no-OCP tendría quizás un método `ordenar(lista, algoritmo)` con un gran if según algoritmo. Un diseño OCP definiría una interfaz `EstrategiaOrdenamiento` con un método `ordenar(lista)` y implementaciones separadas para cada algoritmo; el código que usa una estrategia no necesita saber cuál es, solo la invoca. Para agregar un nuevo algoritmo, se crea una nueva clase que implementa la interfaz, sin modificar el código existente. Esto es precisamente el patrón Strategy, muy alineado con OCP.

> **Ventaja colateral:** Adherirse a OCP a menudo mejora también DIP e ISP (principios que veremos luego), porque para lograr extensión sin modificar, uno tiende a programar contra abstracciones. En el ejemplo, `imprimir_area` acepta un `Figura` abstracto (interfaz), no una lista de tipos concretos; eso es DIP (depender de abstracción, no de detalles). Y en el caso de las estrategias, definimos interfaces específicas (ISP) para cada familia de comportamiento.


# Principio de Sustitución de Liskov (Liskov Substitution Principle – LSP)

El Principio de Sustitución de Liskov (LSP), enunciado por la profesora Barbara Liskov en 1987, se puede resumir así: “Si S es un subtipo de T, entonces los objetos de tipo T en un programa pueden ser reemplazados por objetos de tipo S sin alterar ninguna de las propiedades deseables del programa (correctitud, realización de la tarea, etc.)”.

En términos más coloquiales: cualquier clase hija debe poder usarse en lugar de su clase padre sin que el programa falle. O, dicho de otro modo, las subclases deben cumplir con las expectativas que el código tiene sobre la superclase. Si se viola esta regla, la herencia está mal utilizada o la subclase no es verdaderamente un subtipo del padre en cuanto a comportamiento.

Cuando Liskov habla de "propiedades deseables del programa" se refiere a que al sustituir un objeto por otro de subtipo, el programa debería seguir funcionando correctamente, manteniendo invariantes, resultados esperados, etc. No basta con que "no lance error": debe realmente comportarse de manera consistente con lo que se espera del tipo base.

**Ejemplo básico:** Supongamos que tenemos una función pensada para trabajar con objetos de la clase base `Animal`, que llama al método `moverse()` de ese animal asumiendo que lo hará de cierta forma. Si pasamos un objeto de una subclase `AnimalMarino` que en lugar de moverse por tierra, intenta buscar agua y lanza excepción si no la hay, es probable que esa sustitución rompa el programa. Esa subclase no está cumpliendo el contrato esperado de `Animal.moverse()` en el contexto general. Podríamos decir que `AnimalMarino` no es totalmente un `Animal` en el sentido de Liskov, porque su comportamiento no es intercambiable sin problemas.

Cumplir LSP se trata en gran medida de diseñar correctamente las jerarquías de herencia y las sobrescrituras de métodos:

- Una subclase no debe reforzar restricciones o precondiciones más que la superclase. (Por ejemplo, si la superclase acepta cualquier número positivo en un método, la subclase no debería limitarlo solo a números pares; si lo hace, el código que espera poder pasar cualquier positivo fallaría con la subclase).
- Una subclase no debe debilitar postcondiciones que garantiza la superclase. (Si la superclase asegura que un método devuelve una cadena no vacía, la subclase debería respetar eso y también devolver cadena no vacía, no de repente devolver una cadena vacía o None sin avisar).
- En general, la subclase puede añadir funcionalidades, pero no cambiar la esencia del comportamiento definido por la superclase de forma que sorprenda al código cliente.

**Beneficios de cumplir LSP:**

- Reutilización del código polimórfico: Si todas las subclases pueden sustituir al padre transparentemente, entonces podemos escribir código una vez (usando referencias del tipo padre) y estar seguros de que funcionará con cualquier subtipo. Esto es la base del polimorfismo confiable.
- Mantenimiento del código: Si LSP se viola, suele implicar que hay excepciones o verificaciones tipo `if isinstance(obj, SubClaseProblemática)` en el código, lo cual complica el mantenimiento. Cumpliendo LSP, el código es más uniforme y limpio.
- Polimorfismo seguro: LSP es casi la definición formal de polimorfismo correcto. Garantiza que no habrá sorpresas al usar subclases polimórficamente.
- Correctitud: Se mantiene la corrección del programa al cambiar subtipos; uno puede refactorizar internamente usando subclases y tener confianza en que nada "se rompe".

### Ejemplo clásico – Cuadrado vs Rectángulo

Este es un ejemplo muy famoso en la discusión de LSP. Imaginemos una clase `Rectangulo` con métodos `set_ancho(w)`, `set_alto(h)` y `get_area()`.

Intuitivamente, uno podría pensar "un Cuadrado es un Rectángulo con ancho == alto, así que herede Rectangulo". Pero veamos qué pasa si lo hacemos.

```python
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def set_ancho(self, w):
        self.ancho = w
    def set_alto(self, h):
        self.alto = h
    def get_area(self):
        return self.ancho * self.alto
class Cuadrado(Rectangulo):
    def set_ancho(self, w):
        self.ancho = w
        self.alto = w
    def set_alto(self, h):
        self.ancho = h
        self.alto = h
def duplicar_ancho(rect):
    ancho_actual = rect.ancho
    rect.set_ancho(ancho_actual * 2)
```

Pensemos como código cliente:

- Si pasamos un Rectangulo normal de 2x3 (ancho 2, alto 3, área 6):

```python
rect = Rectangulo(2, 3)
duplicar_ancho(rect) # Ahora es 4x3, área = 12 (efectivamente el doble que 6).
```

- Si pasamos un Cuadrado de lado 2 (que hereda de Rectangulo):

```python
cuadrado = Cuadrado(2, 2)
duplicar_ancho(cuadrado) # Nuestra implementación cuadrada pondrá ancho=4 y alto=4.
```

Ahora el cuadrado tiene área 4x4 = 16, que no es el doble del área original (que era 4). Es 4 veces mayor. El método `duplicar_ancho` en presencia de un `Cuadrado` no cumplió lo que implícitamente se esperaba (duplicar el área). El cuadrado se comportó de forma inesperada para el código que trabajaba con "Rectangulos".

Este comportamiento rompe LSP: un `Cuadrado` no puede ser sustituido por `Rectangulo` sin alterar propiedades del programa. El programador del método `duplicar_ancho` hizo supuestos válidos para rectángulos generales (que cambiar solo el ancho no afectaba el alto; y que el área se escalaba linealmente con cambios de un lado manteniendo el otro constante). `Cuadrado` rompe esos supuestos.

**Soluciones:** Reconocer que matemáticamente un cuadrado es un rectángulo, pero en diseño OOP no es un subtipo adecuado si la interfaz de `Rectangulo` permite modificar ancho y alto independientemente. Una solución sería no hacer `Cuadrado` subclase de `Rectangulo`, sino hacerlas hermanas bajo una superclase común `Figura` o `RectanguloBase` que no tenga setters separables. Otra solución más refinada es restringir la mutabilidad: por ejemplo, hacer `Rectangulo` y `Cuadrado` inmutables después de construcción; así un cuadrado no podría cambiar solo un lado sin afectar al otro.

Veamos este ejemplo en código para clarificar:
```python
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto

    def get_area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def set_ancho(self, ancho):
        # Al asignar un lado en el cuadrado, ambos lados cambian
        super().set_ancho(ancho)
        super().set_alto(ancho)

    def set_alto(self, alto):
        super().set_ancho(alto)
        super().set_alto(alto)
```
Ahora probemos la función que duplica el ancho mencionada:
```python
def duplicar_ancho(rect):
    # Duplica el ancho de un rectángulo dado
    ancho_inicial = rect.ancho
    rect.set_ancho(ancho_inicial * 2)
    print("Área original:", ancho_inicial * rect.alto,
          "Área nueva:", rect.get_area())

# Caso 1: Rectángulo normal
r = Rectangulo(2, 3)
duplicar_ancho(r)  # Área original: 6, Área nueva: 12 (correcto, se duplicó)

# Caso 2: Cuadrado usado como Rectángulo
s = Cuadrado(2)
duplicar_ancho(s)  # Área original: 4, Área nueva: 16 (¡no se duplicó, se cuadruplicó!)
```
Output:
```python
Área original: 6 Área nueva: 12
Área original: 4 Área nueva: 16
```
Vemos el fallo en el segundo caso. Este es un claro incumplimiento de LSP. El código que esperaba duplicar el área no funciona para la subclase Cuadrado. Conclusión: la jerarquía está mal diseñada respecto a LSP.

**Qué hacer en este caso?** Una de las recomendaciones es preferir composición a herencia cuando la relación de subtipo no cumpla LSP. Por ejemplo, podríamos hacer que Rectangulo no tenga setters separados y ofrecer un método set_dimensiones(ancho, alto) para reconfigurarlo entero; y hacer que Cuadrado lance excepción si alguien intenta cambiarlo a un rectángulo (no suena muy bien), o directamente no dar opción de cambiar lado una vez creado (inmutabilidad). Pero en muchos materiales concluyen: no hagas que Cuadrado herede de Rectangulo en sistemas orientados a objetos que permitan modificar dimensiones; en su lugar, trata a Cuadrado y Rectangulo como figuras distintas. Por ejemplo, podríamos tener una interfaz FiguraConArea que ambos implementen, pero no forzar una relación de herencia directa.

**Otro ejemplo de violación de LSP**: Subclases que implementan métodos lanzando excepciones no esperadas. Por ejemplo, una clase Coleccion con método agregar(item) y una subclase ColeccionSoloLectura que hereda pero sobreescribe agregar lanzando UnsupportedOperationException. Si alguien tratara polimórficamente una ColeccionSoloLectura como Coleccion y llamara a agregar, reventará. Entonces, quizás ColeccionSoloLectura no debería heredar de Coleccion si no puede cumplir su contrato; podría mejor usar composición (tener internamente una Coleccion pero no exponer métodos de modificación). Este es un caso típico mencionado en literatura: clases que no soportan ciertos métodos de su base rompen LSP.

**Cómo asegurarse de cumplir LSP?**
- Diseñar con contratos claros: Documenta qué hace cada método de la clase base (precondiciones, postcondiciones, invariantes). Las subclases deben adherirse a ese contrato.
- Evitar excepciones para casos normales: Si un método en la base promete hacer algo, la subclase no debería, por diseño, tener que invalidarlo o lanzar excepción. Si descubres que tu subclase no puede implementar correctamente algo definido en la base, reconsidera la herencia.
- **Principio de sustitución contravariante/covariante de tipos:** Es un tema avanzado, pero básicamente, si la superclase acepta un parámetro de tipo muy general, la subclase no debería restringirlo a un subtipo más específico (precondición más fuerte). Y si la superclase retorna algo, la subclase podría retornar un subtipo (lo cual es más permisivo, eso está bien en LSP porque es covariante con tipos de retorno).

En pocas palabras, LSP nos recuerda que la herencia implica un contrato que va más allá de la sintaxis: las subclases deben comportarse de forma coherente con lo esperado.


# Principio de Segregación de Interfaces (Interface Segregation Principle – ISP)

## Introducción al ISP

El Principio de Segregación de Interfaces (Interface Segregation Principle, ISP) es otro de los principios SOLID que busca mejorar la calidad del diseño orientado a objetos. ISP establece que:

**"Los clientes no deben verse obligados a depender de interfaces que no utilizan."**

En otras palabras, una clase no debería verse forzada a implementar métodos de una interfaz que no necesita. Este principio es especialmente relevante en lenguajes como Python, donde la verificación de tipos y la existencia de métodos se controlan en tiempo de ejecución.

### Problemas que aborda el ISP

El ISP busca evitar los problemas que surgen cuando una interfaz grande y monolítica obliga a las clases a implementar métodos que no utilizan. Esto puede llevar a:

- **Clases con métodos innecesarios:** Las clases terminan teniendo métodos que no usan, simplemente porque la interfaz los incluye.
- **Implementaciones vacías o excepciones:** Para cumplir con la interfaz, las clases se ven obligadas a implementar métodos que no tienen sentido para su comportamiento, lo que puede llevar a excepciones en tiempo de ejecución.
- **Dificultad para entender el código:** Las interfaces grandes hacen que sea más difícil para los desarrolladores entender qué métodos son realmente relevantes para una clase en particular.

En otras palabras, si una clase no utiliza algunos métodos o atributos de una interfaz, entonces dicha interfaz está mal diseñada. Debemos segregar (dividir) esas funcionalidades en interfaces más específicas para que cada clase implemente solo lo que realmente necesita. Así logramos interfaces más pequeñas y enfocadas, alineadas con un único propósito o rol.

### ¿Qué es una interfaz en POO?

En programación orientada a objetos, una interfaz define el conjunto de métodos que un objeto debe tener para cumplir una determinada función en el sistema. Dicho de otra manera, una interfaz especifica cómo se comporta un objeto y qué operaciones se pueden realizar con él, sin entrar en los detalles de implementación. Las interfaces permiten describir contratos: cualquier clase que implemente la interfaz se compromete a proporcionar esas funciones.

En Python, formalmente no existe la palabra clave `interface` como en Java u otros lenguajes. Sin embargo, el concepto se puede lograr mediante clases abstractas o protocolos (veremos esto más adelante). Es importante destacar que las interfaces deben diseñarse pensando en el consumidor: cada cliente debería ver una interfaz adaptada a sus necesidades específicas. Esto es lo que significa la frase "las interfaces pertenecen a los clientes, no a las jerarquías": no crear una interfaz enorme solo porque una jerarquía de clases la comparta, sino crear varias interfaces más pequeñas para distintos tipos de clientes.

### Interfaz informal vs. interfaz formal

- **Interfaz informal:** En Python hablamos de "interfaz informal" cuando definimos un conjunto de métodos esperados sin usar mecanismos estrictos de enforcement (sin obligar su implementación mediante el lenguaje). Python es un lenguaje de tipado dinámico con duck typing, lo que significa que no necesitamos una declaración explícita de que una clase implementa una interfaz; basta con que proporcione ciertos métodos. Por ejemplo, si una clase define el método `__len__`, entonces se comporta como una secuencia o colección medible (implementa "informalmente" la interfaz de secuencia en lo referente a la longitud). Otro ejemplo: si creamos una clase que tiene métodos `write()` y `read()`, cualquier código que espere un "objeto archivo" podría aceptarla aunque no herede de ninguna clase base `Archivo`. Esta es una interfaz informal: nuestro objeto sigue un protocolo esperado (tiene métodos con ciertos nombres), y por convención o documentación decimos que cumple esa interfaz.

**Ventaja:** Las interfaces informales aprovechan la flexibilidad de Python. Podemos definir clases ligeras sin necesidad de una jerarquía compleja. Cualquier objeto que cumpla con la interfaz esperada (es decir, tenga los métodos necesarios) puede usarse en su lugar. Este estilo sigue el principio "Duck Typing" ("si camina como pato y suena como pato, es un pato").

**Desventaja:** No hay una verificación automática por parte del lenguaje. Si a un objeto le falta un método esperado, el error solo se descubrirá en tiempo de ejecución (cuando se intente usar). Además, al leer el código no es obvio qué interfaz "informal" espera una función o método, más allá de la documentación o convenciones de nombres.

- **Interfaz formal:** Se refiere a la definición explícita de interfaces mediante clases abstractas (por ejemplo, usando el módulo `abc` de Python). Aquí, declaramos métodos abstractos que deben ser implementados por las subclases. Si una clase no implementa estos métodos, no puede ser instanciada. Este enfoque es más rígido y asegura que ciertas estructuras y métodos existan en las clases derivadas.

**Ejemplo de interfaz formal con `abc`:**

```python
from abc import ABC, abstractmethod
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        import math
        return math.pi * self.radio ** 2
```

En este ejemplo, `Forma` es una interfaz (clase abstracta) que obliga a las formas a implementar el método `area()`. `Circulo` es una clase concreta que cumple con este contrato.

### Ejemplo práctico de ISP

Imaginemos un sistema de notificaciones que puede enviar alertas por diferentes canales: email, SMS y push notifications. Si forzamos a una interfaz única para todas las notificaciones, podríamos terminar con métodos vacíos en algunas clases concretas, violando ISP.

**Interfaz no segregada (violando ISP):**

```python
class Notificacion:
    def enviar_email(self, destinatario, mensaje):
        pass
    def enviar_sms(self, numero, mensaje):
        pass
    def enviar_push(self, dispositivo_id, mensaje):
        pass
```

Una clase que solo quiere enviar SMS tendría que implementar métodos vacíos para email y push. Esto es una violación clara del ISP.

**Interfaz segregada (cumpliendo ISP):**

```python
class NotificacionEmail:
    def enviar_email(self, destinatario, mensaje):
        pass
class NotificacionSMS:
    def enviar_sms(self, numero, mensaje):
        pass
class NotificacionPush:
    def enviar_push(self, dispositivo_id, mensaje):
        pass
```

Ahora, cada clase de notificación implementa solo lo que necesita. Si alguien quiere enviar solo SMS, implementa `NotificacionSMS` y no tiene que preocuparse por los otros métodos.


## Ejemplo de mala práctica (violación de ISP)

Supongamos que queremos modelar animales y les definimos una interfaz común. Podríamos ingenuamente diseñar una clase base **Animal** con métodos para distintas capacidades:

```python
class Animal:
    def comer(self):
        pass
    def correr(self):
        pass
    def nadar(self):
        pass
class Perro(Animal):
    def comer(self):
        print("El perro come")
    def correr(self):
        print("El perro corre")
    def nadar(self):
        print("El perro nada")
class Pez(Animal):
    def comer(self):
        print("El pez come")
    def correr(self):
        raise NotImplementedError("Los peces no pueden correr")
    def nadar(self):
        print("El pez nada")
```

En este diseño, la interfaz **Animal** exige que todo animal pueda comer, correr y nadar. Ahora implementemos dos animales concretos:

- El perro puede realizar las tres acciones, hasta aquí todo bien.
- ¿Pero qué pasa con un pez? Aquí vemos el problema: la clase **Pez** se ve obligada a implementar `correr()` porque la interfaz **Animal** lo exige, pero los peces no corren. Hemos violado ISP: obligamos al cliente (en este caso, **Pez**) a depender de un método que no utiliza ni tiene por qué tener. Esto lleva a implementaciones vacías o excepciones como `NotImplementedError`, indicando un diseño deficiente.

Las consecuencias de esta mala práctica incluyen:

- Código confuso o frágil: **Pez** tiene un método que conceptualmente no le pertenece. Si alguien llama a `pez.correr()`, habrá una excepción en tiempo de ejecución.
- Dificultad para extender: ¿Qué pasa si luego añadimos **Ave** que vuela? ¿Añadiríamos `volar()` a **Animal**? Entonces ahora **Perro** y **Pez** tendrían otro método que no usan (perros no vuelan, peces tampoco). El problema se agrava.
- Clases con responsabilidades mezcladas: La interfaz **Animal** intenta abarcar demasiadas acciones diferentes.

## Ejemplo de buena práctica (aplicando ISP)

La solución es segregar la interfaz **Animal** en interfaces más pequeñas y específicas. Identifiquemos las capacidades distintas:

- Comer
- Correr
- Nadar

En lugar de una interfaz que contenga todo, crearemos tres interfaces (abstractas) independientes:

```python
from abc import ABC, abstractmethod
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass
class Corredor(ABC):
    @abstractmethod
    def correr(self):
        pass
class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass
class Perro(Comedor, Corredor, Nadador):
    def comer(self):
        print("El perro come")
    def correr(self):
        print("El perro corre")
    def nadar(self):
        print("El perro nada")
class Pez(Comedor, Nadador):
    def comer(self):
        print("El pez come")
    def nadar(self):
        print("El pez nada")
```

Ahora nuestras clases animales implementarán solo las interfaces que necesiten:

- **Pez** implementa **Comedor** y **Nadador** (come y nada) pero no implementa **Corredor** (no se ve forzado a tener un método `correr` sin sentido).
- Si en el futuro agregamos un **Ave**, podríamos tener interfaces como **Volador** para `volar()`, y el ave implementaría **Comedor** y **Volador**. Un perro no volaría, un pez no volaría, y no tendrían ese método en absoluto en su definición. Cada uno con lo suyo.

Este diseño segregado es más limpio y seguro:

- No hay métodos sin implementar o con implementaciones vacías.
- Las clases son más simples, enfocadas en lo que hacen.
- Si alguna funcionalidad cambia (por ejemplo la forma de nadar), solo afecta a las clases que realmente la usan (las que implementan **Nadador**), sin impacto en las demás.

# Principio de Inversión de Dependencias (Dependency Inversion Principle – DIP)

## Introducción al DIP

El Principio de Inversión de Dependencias (Dependency Inversion Principle) aborda cómo deben relacionarse los módulos o componentes de software entre sí para lograr un bajo acoplamiento. Su definición clásica dice:

- Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones.
- Las abstracciones no deberían depender de los detalles. Los detalles (implementaciones concretas) deberían depender de las abstracciones.

En otras palabras, tanto las clases/módulos de "nivel alto" como los de "nivel bajo" deben depender de un contrato abstracto común, y no directamente unos de otros. Además, las abstracciones (interfaces) deben ser independientes de los detalles de implementación; en su lugar, esas implementaciones concretas cumplirán con la abstracción.

### ¿Qué son módulos de alto nivel y bajo nivel?

- **Módulos de Alto Nivel:** se refiere a componentes que contienen la lógica de negocio más importante o las reglas de alto nivel de la aplicación. Son las partes de nuestro sistema que orquestan operaciones complejas, toman decisiones de negocio, coordinan tareas, etc. Su correcto funcionamiento es crucial para satisfacer los requisitos del usuario o del dominio. Ejemplo: Una clase `ProcesadorDePagos` que coordina el pago de una compra en un sitio web, o un `ControladorUsuario` que maneja el registro/login de usuarios. Estas clases de alto nivel idealmente no deberían conocer detalles de cómo se realizan tareas secundarias, solo deben saber que esas tareas se hacen a través de alguna interfaz abstracta.
- **Módulos de Bajo Nivel:** son componentes que se encargan de los detalles técnicos u operativos necesarios para que los de alto nivel funcionen. Suelen ser servicios concretos: acceso a base de datos, envío de correos, logueo de eventos, API externas, etc. Por sí solos no constituyen la lógica de negocio principal, pero proveen funcionalidades de soporte. Ejemplo: una clase `RepositorioMySQL` que realiza operaciones CRUD en una base de datos MySQL, un `ServicioEmail` que envía correos vía SMTP, o un `LogConsola` que simplemente imprime logs en pantalla. Son "de bajo nivel" en el sentido de que tratan con detalles específicos.

### ¿Qué problema resuelve DIP?

Tradicionalmente, sin DIP, un módulo de alto nivel podría instanciar o referenciar directamente a un módulo de bajo nivel. Por ejemplo, `ProcesadorDePagos` crea internamente un objeto de base de datos MySQL y lo usa. Esto introduce una dependencia fuerte: si quiero cambiar la base de datos a PostgreSQL o a un servicio web externo, tendría que modificar `ProcesadorDePagos`. Además, hace difícil probar `ProcesadorDePagos` en aislamiento (porque siempre usa la base de datos real, habría que simularla de alguna forma).

El DIP invierte esa relación: el módulo de alto nivel se diseña en función de una abstracción (por ejemplo, una interfaz `Repositorio` genérica). El módulo de bajo nivel (ej: `RepositorioMySQL`) implementa esa abstracción. De esta manera:

- El código de alto nivel no sabe nada de MySQL ni de detalles concretos, solo sabe que puede llamar, digamos, `repo.guardar(item)` según la interfaz `Repositorio`.
- Podemos tener múltiples implementaciones de `Repositorio` (MySQL, MongoDB, archivo plano, etc.) e intercambiarlas sin tocar el módulo de alto nivel.
- Para la prueba unitaria de `ProcesadorDePagos`, podemos crear un doble (stub o mock) de `Repositorio` que simule la base de datos, inyectándolo en `ProcesadorDePagos`. Esto hace las pruebas más simples y fiables.
- Los detalles de implementación (clase concreta) dependen de la abstracción en el sentido de que deben cumplir el contrato definido por la interfaz. Si la interfaz cambia (por ejemplo, se agrega un método), las implementaciones deben adaptarse. La dirección de dependencia está "invertida" respecto al diseño naive inicial.

### Definición formal del DIP

Retomando las frases clave del principio:

- “Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones.” – Esto significa que cualquier clase de alto nivel (más general) debería interactuar con otras a través de interfaces o clases abstractas, en lugar de acoplarse a clases concretas de nivel bajo. El alto nivel establece qué necesita en forma de abstracción (una serie de métodos), y espera que algún componente lo provea.
- “Las abstracciones no deberían depender de los detalles. Los detalles deberían depender de las abstracciones.” – Las interfaces o clases abstractas deben estar definidas en términos genéricos, sin conocer qué habrá debajo. Son las implementaciones concretas (detalles) las que se ajustan a la interfaz. En la práctica, esto suele implicar que la interfaz se define pensando en las necesidades del módulo de alto nivel, no al revés.

### Abstracciones como punto medio

Para aplicar DIP en código, el punto crítico es la creación de abstracciones (interfaces o clases abstractas) adecuadas que conecten alto nivel con bajo nivel. Estas abstracciones modelan el servicio o funcionalidad genérica que requiere el alto nivel.

Por ejemplo, siguiendo los ejemplos anteriores:
- Necesidad de alto nivel: notificar al usuario.
- Abstracción: definimos una interfaz `Notificador` con el método `enviar(destinatario, mensaje)`.
- Módulo de bajo nivel: implementa `EmailNotificador` (envía email), `SMSNotificador` (envía SMS), `PushNotificador` (notificaciones push), etc. en clases concretas como `EmailNotificador`, `SMSNotificador`, `PushNotificador`.

Otro ejemplo:
- Necesidad de alto nivel: almacenar datos.
- Abstracción: interfaz `Almacenamiento` con métodos `guardar(objeto)` y `recuperar(id)` (por ejemplo).
- Implementaciones de bajo nivel: `AlmacenamientoEnDisco`, `AlmacenamientoEnMemoria`, `AlmacenamientoEnNube`... todas cumplen `Almacenamiento`.

### Ejemplo concreto de DIP en Python

Supongamos un sistema de órdenes de compra que debe notificar al cliente cuando se confirma su pedido:

**Sin DIP (mala práctica):**

```python
class GestorPedidos:
    def __init__(self):
        self.email_service = ServicioEmail()
    def confirmar_pedido(self, pedido):
        mensaje = f"Pedido {pedido.id} confirmado."
        self.email_service.enviar(pedido.cliente_email, mensaje)
class ServicioEmail:
    def enviar(self, destinatario, mensaje):
        print(f"Enviando correo a {destinatario}: {mensaje}")
```

En este diseño, **GestorPedidos** (módulo de alto nivel que maneja la lógica de pedidos) depende directamente de **ServicioEmail** (módulo de bajo nivel que envía correos). Si mañana quisiéramos notificar por SMS o cambiar el mecanismo de email, tendríamos que modificar **GestorPedidos**. También es difícil de probar: en un test, siempre se ejecutaría el envío de email real (o habría que monkey-patchear **ServicioEmail**).

**Con DIP (buena práctica):**

```python
from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self, destinatario, mensaje):
        pass
class EmailNotificador(Notificador):
    def enviar(self, destinatario, mensaje):
        print(f"Enviando correo a {destinatario}: {mensaje}")
class SMSNotificador(Notificador):
    def enviar(self, destinatario, mensaje):
        print(f"Enviando SMS a {destinatario}: {mensaje}")
class GestorPedidos:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
    def confirmar_pedido(self, pedido):
        mensaje = f"Pedido {pedido.id} confirmado."
        self.notificador.enviar(pedido.cliente_email, mensaje)
```

En este rediseño:

- **Notificador** es la abstracción (interfaz) que define lo que significa notificar: un método `enviar(destinatario, mensaje)`.
- **EmailNotificador** y **SMSNotificador** son módulos de bajo nivel que dependen de la abstracción **Notificador** (la implementan). Cada cual sabe enviar por su medio específico.
- **GestorPedidos** ya no crea internamente un **ServicioEmail**, ni sabe nada de cómo funciona. En su constructor, recibe un notificador que cumpla la interfaz **Notificador**. Podríamos pasarle una instancia de **EmailNotificador**, de **SMSNotificador** u otra que surja (incluso una falsa para pruebas). **GestorPedidos** depende de la abstracción **Notificador** en su tipo de atributo.
- Cuando se confirma un pedido, utiliza `self.notificador.enviar(...)` sin preocuparse de si es email o SMS. Podemos cambiar el tipo de notificador desde fuera sin modificar **GestorPedidos**.

```python
# Ejemplo de uso
gestor = GestorPedidos(EmailNotificador())
gestor.confirmar_pedido(pedido) # Envia email
gestor_sms = GestorPedidos(SMSNotificador())
gestor_sms.confirmar_pedido(pedido) # Envia SMS
```

Para probar **GestorPedidos**, podríamos crear una clase dummy que implemente **Notificador** solo para test (que guarde el mensaje en una variable en lugar de enviarlo), y pasarla al constructor. Así verificamos que `GestorPedidos.confirmar_pedido` llama a `enviar` con los parámetros correctos sin enviar nada real. Esto antes era imposible sin modificar la clase o hacer trucos, porque **GestorPedidos** estaba acoplado a **ServicioEmail**.

Este ejemplo ilustra DIP: el módulo de alto nivel **GestorPedidos** y los de bajo nivel (**EmailNotificador** / **SMSNotificador**) dependen de la abstracción **Notificador**, en lugar de que el alto nivel dependa directamente de concretos. Además, la abstracción **Notificador** no depende de detalles (no importa si envía email, SMS, etc.), mientras que los detalles (por ejemplo, **EmailNotificador**) sí dependen de la abstracción (deben implementar `enviar` tal como está definido).

## Beneficios de aplicar DIP

Al igual que los demás principios SOLID, DIP aporta ventajas claras al diseño:

- **Reducción del acoplamiento:** Los componentes de alto nivel no conocen las particularidades de los de bajo nivel. Un cambio en la implementación de bajo nivel (por ejemplo, cambiar la librería de base de datos, o el servicio de email) no obliga a cambiar la lógica de alto nivel, mientras la interfaz se mantenga. Incluso si se cambia la interfaz, la afectación está controlada a las implementaciones y al código que la usa, pero no es una maraña de dependencias directas.
- **Mejora de la modularidad:** Podemos desarrollar y pensar en módulos de manera más aislada. El alto nivel define qué necesita en abstracto; los bajos niveles se implementan por separado. Se pueden agregar nuevas implementaciones de bajo nivel (nuevos "módulos de detalle") sin modificar el código existente de alto nivel, solo plug-and-play. Por ejemplo, agregar **PushNotificador** en el futuro y pasarlo a **GestorPedidos** sin tocar la clase.
- **Facilita el testing:** Como mencionamos, la inversión de dependencias habilita fácilmente el uso de dobles de prueba (mocks, stubs) para probar la lógica de negocio sin invocar código externo. Podemos simular bases de datos, servicios externos, etc., proporcionando implementaciones dummy de las abstracciones. Las pruebas unitarias se centran en la lógica de alto nivel, y podemos inyectar comportamientos controlados para las dependencias. Esto mejora drásticamente la capacidad de testeo de la aplicación.
- **Mantenibilidad y extensibilidad:** Un sistema construido con DIP suele ser más fácil de mantener en el tiempo. Si surgen nuevos requisitos, podemos extender el sistema agregando nuevas clases que implementen las abstracciones existentes o incluso nuevas abstracciones, en lugar de modificar código ya probado. La lógica de alto nivel permanece estable y comprensible al no estar mezclada con detalles de infraestructura. Además, si encontramos errores en un módulo de bajo nivel, lo arreglamos allí sin tocar a sus consumidores abstractos.

## DIP en relación con otros principios SOLID

El Principio de Inversión de Dependencias está íntimamente ligado a los demás principios SOLID e incluso los potencia:

- **SRP (Responsabilidad Única):** DIP ayuda a que las clases de alto nivel se mantengan enfocadas en su responsabilidad principal, delegando tareas específicas (como acceder a datos, enviar notificaciones) a otras clases. Al depender de abstracciones, cada cosa tiende a estar en su lugar.
- **OCP (Abierto/Cerrado):** Gracias a DIP, podemos extender el sistema añadiendo nuevas implementaciones de interfaces (nuevos módulos de bajo nivel) sin modificar los módulos de alto nivel existentes. Por ejemplo, agregar un nuevo tipo de notificador o un nuevo método de pago es cuestión de crear la clase correspondiente e implementarla, luego inyectarla, sin tocar la clase de alto nivel que usa la interfaz. Esto es precisamente estar "abierto a la extensión, cerrado a la modificación".
- **LSP (Sustitución de Liskov):** DIP prácticamente obliga a diseñar con interfaces claras, lo que facilita que las implementaciones concretas puedan sustituirse sin sorpresas. Si un **EmailNotificador** es un **Notificador**, también un **SMSNotificador** lo es, y **GestorPedidos** puede trabajar con cualquiera indistintamente. Esto es LSP en acción: las subclases cumplen el contrato de la superclase.
- **ISP (Segregación de Interfaces):** Al aplicar DIP normalmente se definen varias interfaces pequeñas (por cada necesidad del alto nivel). Esto encaja con ISP, ya que no estamos obligando a las clases a implementar métodos que no usarán; cada interfaz corresponde a un conjunto de comportamientos específicos.

En conclusión, DIP promueve un diseño donde las clases de alto nivel dependen de abstracciones, y las clases de bajo nivel las implementan. El código de alto nivel recibe sus dependencias externamente (inyección de dependencias) y se enfoca en su lógica principal, haciendo el sistema más flexible y testable.
