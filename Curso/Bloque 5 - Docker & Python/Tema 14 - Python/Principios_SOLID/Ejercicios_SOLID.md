# Ejercicios prácticos

## Ejercicio 1: POO
Crea una clase `Circulo` que represente un círculo. La clase debe inicializarse con el radio del círculo y deberá tener:
  - Un atributo de clase que cuente cuántos círculos se han creado en total.
  - Un método de instancia `area()` que calcule el área del círculo (usa `math.pi * radio^2`).
  - Un método de instancia `perimetro()` que calcule el perímetro (longitud de la circunferencia) del círculo (usa `2 * math.pi * radio`).
  - Un método de clase `total_circulos()` que devuelva cuántos círculos se han creado (basado en el atributo de clase).

Pista: Utiliza `import math` para obtener el valor de π (`math.pi`). Incrementa el contador de círculos en el constructor (`__init__`).

**Estructura sugerida:**

```python
class Circulo:
    total_creados = 0
    def __init__(self, radio):
        self.radio = radio
        Circulo.total_creados += 1
    def area(self):
        pass
    def perimetro(self):
        pass
    @classmethod
    def total_circulos(cls):
        pass
```

**Solución:**

```python
import math
class Circulo:
    total_creados = 0
    def __init__(self, radio):
        self.radio = radio
        Circulo.total_creados += 1
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio
    @classmethod
    def total_circulos(cls):
        return cls.total_creados
# Ejemplo de uso
c1 = Circulo(2)
c2 = Circulo(3)
print(c1.area(), c1.perimetro())
print(Circulo.total_circulos())
```

Explicación: Definimos la clase **Circulo** con un atributo de clase `total_creados` que se incrementa en el constructor cada vez que se instancia un nuevo círculo. Los métodos `area()` y `perimetro()` utilizan el atributo de instancia `radio` junto con constantes matemáticas (`math.pi`) para calcular los resultados. El método de clase `total_circulos()` retorna el contador de instancias creadas. Al final, instanciamos un par de círculos (`c1` y `c2`) y comprobamos que los métodos funcionan correctamente y que el contador de instancias se actualiza.

## Ejercicio 2: POO
- Implementa un modelo de herencia simple. Crea una clase base `Vehiculo` con un atributo `marca` y un método `describir()` que imprima un mensaje con la marca. Luego crea una subclase `Coche` que herede de `Vehiculo`, agregue un atributo `modelo` y sobrescriba el método `describir()` para incluir también el modelo en el mensaje. Por último, comprueba que al instanciar un `Coche` puedas acceder al atributo `marca` (heredado) y que su método `describir()` muestre ambos datos.

Pista: Recuerda llamar al constructor de la clase padre desde `Coche.__init__` para asignar la marca. La función `super()` te será útil. Al sobreescribir `describir()` en `Coche`, puedes optar por reusar el método del padre (llamando a `super().describir()`) y luego agregar más información, o construir el mensaje completo en el método hijo.

**Estructura sugerida:**

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    def describir(self):
        pass
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    def describir(self):
        pass
```

**Solución:**

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
    def describir(self):
        print(f"Marca: {self.marca}")
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    def describir(self):
        super().describir()
        print(f"Modelo: {self.modelo}")
# Ejemplo de uso
c = Coche("Toyota", "Corolla")
c.describir()
```

Explicación: La clase **Vehiculo** define el atributo `marca` y un método `describir()`. La clase **Coche** hereda de Vehiculo, por lo que no necesita redeclarar `marca`; solo añade `modelo`. En el constructor de Coche usamos `super().__init__(marca)` para que la clase base se encargue de inicializar la marca. Luego en `describir()`, construimos un mensaje que incluye tanto la marca (heredada) como el modelo. La prueba muestra que Coche puede usar tanto atributos heredados (`c.marca`) como su propio atributo (`c.modelo`), y que su método sobreescrito proporciona la información combinada.

Con estos ejercicios, has practicado los conceptos fundamentales de POO: definición de clases, creación de objetos, encapsulación (al usar atributos de instancia y controlar su acceso a través de métodos), herencia (extendiendo Vehiculo en Coche), y polimorfismo a través de la sobreescritura de métodos (`describir` se comporta distinto en Vehiculo y Coche). En las próximas clases profundizaremos en principios de diseño que nos ayudarán a crear clases y jerarquías más sólidas, mantenibles y flexibles.

## Ejercicio 3: Herencia VS Composición
Tienes una clase **Rueda** y quieres crear una clase **Coche**. Decide cómo relacionarlas:
  - Opción A: Coche hereda de Rueda.
  - Opción B: Coche tiene instancias de Rueda.

¿Cuál crees que es correcta y por qué? Luego, implementa la solución elegida:

La clase **Rueda** puede tener un atributo `diametro` (por ejemplo, 16 pulgadas) y quizás un método `rodar()` que imprima algo como "Rueda rodando...". La clase **Coche** debe, en su constructor, crear 4 objetos **Rueda** (asígnalos a una lista o a atributos como `rueda1`, `rueda2`, ...). Añade un método `mover()` en **Coche** que haga que sus ruedas rueden (llamando al método correspondiente de cada rueda) y que imprima "Coche avanzando...".

Pista: La relación lógica es "un coche tiene cuatro ruedas", no "un coche es una rueda". Piensa cómo usar la composición para reflejar eso.

**Solución:**

```python
class Rueda:
    def __init__(self, diametro):
        self.diametro = diametro
    def rodar(self):
        print("Rueda rodando...")

class Coche:
    def __init__(self):
        self.ruedas = [Rueda(16) for _ in range(4)]
    def mover(self):
        for rueda in self.ruedas:
            rueda.rodar()
        print("Coche avanzando...")
# Ejemplo de uso
mi_coche = Coche()
mi_coche.mover()
```

**Explicación:** Aquí **Coche** no hereda de **Rueda** (lo cual sería ilógico), sino que crea internamente 4 ruedas en su construcción. Al llamar `mi_coche.mover()`, el coche delega la acción a cada una de sus ruedas (`rueda.rodar()`) y luego imprime su propio mensaje. Este diseño tiene alta cohesión (la clase **Rueda** se encarga solo de rodar, la clase **Coche** se encarga de coordinar sus ruedas y representar el vehículo) y bajo acoplamiento (podríamos modificar la implementación de **Rueda** o reemplazarla por otra clase de ruedas sin tener que cambiar la clase **Coche**, mientras siga teniendo el método `rodar()`). También es flexible: podríamos tener distintos tipos de ruedas (invierno, verano, etc., quizás subclases de **Rueda**) e instalarlas en el coche sin modificar la clase **Coche**. Este es un ejemplo claro de composición ganándole a una herencia inapropiada.

## Ejercicio 4: Principio de Responsabilidad Única

Observa el siguiente código:

```python
class Pedido:
    def __init__(self, items):
        self.items = items
    def calcular_total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items)
    def enviar_confirmacion(self, email):
        total = self.calcular_total()
        mensaje = f"Su pedido por un total de {total} fue recibido."
        print(f"Enviando correo a {email}: {mensaje}")
```

La clase **Pedido** tiene dos responsabilidades claras: calcular el total del pedido y manejar el envío de un correo de confirmación. Esto infringe el SRP. Se te pide refactorizar el diseño de la siguiente manera:
- Deja a **Pedido** solo la responsabilidad de manejar la lista de ítems y el cálculo del total.
- Crea una nueva clase, por ejemplo **Notificador**, con la responsabilidad de enviar mensajes de confirmación (podría ser correo electrónico u otro medio en un caso real, pero bastará con que simulemos un envío).
- Haz que **Pedido** use a **Notificador** en lugar de enviar correos directamente.

Pista: El método `enviar_confirmacion` no pertenece realmente a los datos del pedido, sino a un servicio externo de notificación. Piensa cómo podrías "inyectar" ese servicio en la clase **Pedido** (por ejemplo, pasando un objeto notificador al método o al constructor).

**Solución:**

```python
class Pedido:
    def __init__(self, items):
        self.items = items
    def calcular_total(self):
        return sum(item['precio'] * item['cantidad'] for item in self.items)

class Notificador:
    @staticmethod
    def enviar_confirmacion(pedido, email):
        total = pedido.calcular_total()
        mensaje = f"Su pedido por un total de {total} fue recibido."
        print(f"Enviando correo a {email}: {mensaje}")
# Ejemplo de uso
pedido = Pedido([{'precio': 100, 'cantidad': 2}, {'precio': 50, 'cantidad': 1}])
Notificador.enviar_confirmacion(pedido, "cliente@example.com")
```

**Explicación:** Ahora **Pedido** solo conoce sus ítems y puede calcular su total. La clase **Notificador** es la encargada de formatear y "enviar" el mensaje de confirmación. Fíjate que `Notificador.enviar_confirmacion` recibe un objeto pedido y un email. Así, construye el mensaje apoyándose en `pedido.calcular_total()`. Siguiendo SRP, cada clase hace lo suyo: si necesitamos cambiar cómo se envían las confirmaciones (por ejemplo, usar un servicio real de email), iremos a la clase **Notificador**. Si cambia la forma de calcular el total (impuestos, descuentos, etc.), tocaremos la clase **Pedido**. Además, podríamos tener distintos tipos de notificador (email, SMS, etc.) sin tocar **Pedido** para nada – lo cual apunta hacia el principio de abierto/cerrado que veremos en la siguiente clase. Observa también que **Pedido** y **Notificador** están poco acoplados: comparten solo lo necesario (el notificador llama a un método público de **Pedido**). Este ejercicio refuerza cómo SRP nos guía a separar lógicamente el código para mejorar mantenibilidad y claridad.

## Ejercicio: OCP
Supongamos que estás diseñando una calculadora básica. Iniciaste con una función que recibe dos números y una operación en texto, realizando así la operación. Por ejemplo:

```python
def calcular(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    # ...
```

Esta función viola OCP: si quisieras agregar multiplicación, división, etc., tendrías que modificarla agregando más `elif`. Vamos a refactorizar usando OCP:

- Crea una clase abstracta (o una interfaz informal) `Operacion` con un método `calcular(a, b)`.
- Implementa varias subclases: `Suma`, `Resta` (y opcionalmente `Multiplicacion`, `Division`), que cada una implemente el método para realizar la operación correspondiente.
- Escribe una nueva función `calcular_operacion(a, b, operacion_obj)` donde `operacion_obj` es una instancia de alguna de esas clases (por ejemplo, un objeto `Suma`). Esta función llamará a `operacion_obj.calcular(a, b)` internamente. No uses if/elif para distinguir la clase; confía en el polimorfismo.
- Muestra cómo agregar una nueva operación (por ejemplo, Potenciación) requerirá agregar solo una nueva clase `Potenciacion` sin cambiar el código existente.

> **Pista:** Puedes usar clases con herencia del ABC de Python para formalizar la interfaz `Operacion`, o simplemente usar clases normales sabiendo que todas implementarán `calcular`. Lo importante es el concepto.

**Solución:**

```python
from abc import ABC, abstractmethod
class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass
class Suma(Operacion):
    def calcular(self, a, b):
        return a + b
class Resta(Operacion):
    def calcular(self, a, b):
        return a - b
class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b
class Division(Operacion):
    def calcular(self, a, b):
        return a / b if b != 0 else None
class Potenciacion(Operacion):
    def calcular(self, a, b):
        return a ** b
def calcular_operacion(a, b, operacion_obj):
    return operacion_obj.calcular(a, b)
# Ejemplo de uso
print(calcular_operacion(5, 3, Suma())) # 8
print(calcular_operacion(5, 3, Resta())) # 2
print(calcular_operacion(5, 3, Multiplicacion())) # 15
print(calcular_operacion(5, 3, Division())) # 1.666...
print(calcular_operacion(2, 3, Potenciacion())) # 8
```

**Explicación:** Hemos definido una interfaz (abstracta) `Operacion` con el método `calcular(a, b)`. Cada subclase implementa la operación matemática correspondiente. La función de alto nivel `calcular_operacion` recibe un objeto operación y simplemente delega la lógica llamando a `operacion_obj.calcular(a, b)`. Esto es flexible y extensible:

Para agregar cualquier nueva operación, solo creamos una nueva subclase de `Operacion` (como hicimos con `Potenciacion`). No necesitamos modificar la función `calcular_operacion` ni tocar las clases existentes. El código cliente puede operar con la nueva clase inmediatamente: por ejemplo, podríamos llamar `calcular_operacion(2, 8, Potenciacion())` sin cambiar nada más.

Notemos que `calcular_operacion` no tiene ni un if. Está totalmente abierta a extensión (puedo pasarle instancias de nuevas clases `Operacion`) sin tener ningún caso cerrado por tipo.

Este ejercicio refleja OCP: la calculadora queda preparada para admitir nuevas funcionalidades matemáticas sin editar el código ya escrito. Además, el diseño es más limpio y sigue otros principios: cada operación está encapsulada en su clase (SRP), y `calcular_operacion` depende de la abstracción `Operacion` en lugar de conocer detalles concretos (DIP).

## Ejercicio: LSP
Analicemos la siguiente jerarquía y su uso, detectando violaciones de LSP y corrigiéndolas.

Tenemos una clase base Ave con un método volar(). Dos subclases: Golondrina y Pinguino. La golondrina vuela, pero el pingüino no puede volar.

Código inicial:
```python
class Ave:
    def volar(self):
        print("El ave vuela")


class Golondrina(Ave):
    pass


class Pinguino(Ave):
    def volar(self):
        print("El pingüino intenta volar... pero no puede :-(")
```

Ahora un código cliente:
```python
def prueba_vuelo(ave: Ave):
    # Esta función espera que el ave vuele de alguna forma
    ave.volar()
    print("Vuelo completado.\n")

aves = [Golondrina(), Pinguino()]
for ave in aves:
    prueba_vuelo(ave)
```
Pregunta 1: ¿Se cumple LSP? ¿Qué problema ves con la clase Pinguino al usarla polimórficamente como Ave?

Pregunta 2: ¿Cómo arreglarías el diseño? (Pista: hay varias opciones: podrías eliminar o modificar el método volar de Ave, segregar interfaces, o redefinir la jerarquía).

Explica tu respuesta y propone una solución en código.

**Solución:**

Respuesta 1: En la jerarquía dada, Pinguino hereda de Ave y por tanto es tratable como un Ave. Sin embargo, conceptualmente un pingüino no puede volar. En la implementación propuesta, Pinguino.volar() imprime un mensaje indicando que no vuela (lo cual es una forma suave de violar LSP, al menos no rompe el código, pero sí contradice la expectativa). El código prueba_vuelo asume que cualquier Ave "vuela" efectivamente. Si bien aquí solo imprime mensajes, imagina que prueba_vuelo calculase tiempo de vuelo, distancia, etc. Con un pingüino, esos cálculos no tendrían sentido.

Esto es una violación del Principio de Sustitución de Liskov: un Pinguino no cumple con las mismas "propiedades" que otros Ave (no puede realizar la acción volar realmente). Aunque aquí no hay un fallo catastrófico en tiempo de ejecución, sí hay una ruptura del contrato: Ave.volar implica la capacidad de volar, Pinguino no la tiene. Hemos forzado una relación de herencia inapropiada.

Respuesta 2: Existen varias formas de corregir el diseño, dependiendo de cómo queramos modelar la realidad:
- Opción A: Segregar interfaces (ISP aplicado). Podemos reconocer que no todas las aves vuelan. Crear una interfaz (clase base abstracta) separada para aves voladoras. Por ejemplo, tener class Ave sin método volar, y luego class AveVoladora(Ave) con método abstracto volar(). Golondrina hereda de AveVoladora, pingüino hereda de Ave directamente o de una posible AveNoVoladora sin volar. En código:
```python
class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        raise NotImplementedError


class Golondrina(AveVoladora):
    def volar(self):
        print("La golondrina vuela bajo las nubes")


class Pinguino(Ave):
    def nadar(self):
        print("El pingüino nada en el agua")
```
- Aquí ya no hacemos Pinguino.volar(). La función prueba_vuelo debería tiparse para AveVoladora en vez de Ave, así nunca se le pasaría un pingüino. Esto cumple LSP porque todas las AveVoladora pueden volar, y un pingüino ya ni siquiera tiene volar() en su interfaz.
- Opción B: Composición en lugar de herencia para comportamientos. Podríamos mantener Ave con un atributo que denote su estrategia de movimiento (volar, nadar, correr). Por ejemplo, un pingüino podría tener una estrategia de "no vuela / camina y nada", mientras una golondrina tiene estrategia de "volar". Así, la clase Ave podría llamar a su estrategia de movimiento. Esto se parece a Strategy pattern y también solucionaría el problema separando el comportamiento en objetos distintos.
- Opción C: Herencia múltiple / mixins (no muy necesario aquí): Python permitiría hacer algo como class Volador: def volar(): ... y luego class Pinguino(Ave): pass y class Golondrina(Ave, Volador): .... Pero esto se complica y realmente es similar a la opción A conceptualmente.

La opción A es la más alineada con ISP/LSP: no todas las aves vuelan, así que no todas deben ofrecer ese método.

Veamos cómo implementar la opción A:
```python
from abc import ABC, abstractmethod

class Ave(ABC):
    def comer(self):
        print("El ave come")


class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass


class Golondrina(AveVoladora):
    def volar(self):
        print("La golondrina vuela alto en el cielo")


class Pinguino(Ave):
    def nadar(self):
        print("El pingüino nada veloz bajo el agua")
```
Y ajustamos la función de prueba:
```python
def prueba_vuelo(ave: AveVoladora):
    ave.volar()
    print("Vuelo completado.\n")

aves_voladoras = [Golondrina()]
for ave in aves_voladoras:
    prueba_vuelo(ave)


# Si queremos probar al pingüino, tendría su propia función de prueba quizá
def prueba_nado(pinguino: Pinguino):
    pinguino.nadar()
    print("Nado completado.\n")

pingu = Pinguino()
prueba_nado(pingu)
```
Resultado:
```python
La golondrina vuela alto en el cielo
Vuelo completado.

El pingüino nada veloz bajo el agua
Nado completado.
```
Ahora sí, la jerarquía respeta LSP: cualquier objeto pasado a prueba_vuelo es de tipo AveVoladora y ciertamente vuela. Un Pinguino ni siquiera puede ser pasado a prueba_vuelo porque no es subtipo de AveVoladora. Hemos segregado las interfaces de Ave en dos: las que vuelan y las que no (o al menos no nos interesa su vuelo).

Con este rediseño:
- Cohesión: Mejor, cada clase tiene solo los métodos que puede cumplir.
- Acoplamiento: prueba_vuelo solo conoce la abstracción AveVoladora.
- LSP: Cumplido, ninguna subclase rompe las expectativas. Golondrina reemplaza a AveVoladora correctamente. Pingüino nunca promete volar, así que no rompe nada.
- ISP: Cumplido también, ya que no forzamos a Pingüino a implementar un método que no usa.
- 
Este ejercicio muestra cómo detectar una violación de LSP (un subtipo que no puede cumplir el contrato del supertipo) y refactorizar el modelo para corregirlo. En general, si te encuentras escribiendo subclases que anulan métodos con comportamientos "vacíos" o contrarios a lo esperado (e.g., lanzando excepciones, o imprimiendo "no puedo hacer X"), es una señal de alarma de LSP/ISP: quizá la jerarquía de herencia no es adecuada y debes reconsiderar tu diseño.

## Ejercicio: ISP
Supongamos que estás diseñando un sistema de gestión de documentos. Tienes una clase `Documento` que tiene métodos para `imprimir`, `guardar_en_pdf` y `enviar_por_email`. Sin embargo, no todos los documentos necesitan ser enviados por email, y algunos podrían necesitar ser guardados en otros formatos.

1. Identifica si hay violaciones a SRP e ISP en este diseño.
2. Propón una solución que cumpla con SRP e ISP.

**Solución propuesta:**

```python
class Documento:
    def __init__(self, contenido):
        self.contenido = contenido
class Impresora:
    def imprimir(self, documento: Documento):
        pass
class GuardarComoPDF:
    def guardar(self, documento: Documento):
        pass
class EnviarPorEmail:
    def enviar(self, documento: Documento, destinatario):
        pass
```

**Explicación de la solución:** 

- Separamos las responsabilidades: `Documento` solo maneja contenido. `Impresora`, `GuardarComoPDF` y `EnviarPorEmail` manejan acciones específicas.
- Cada clase tiene una única razón para cambiar. Por ejemplo, si solo cambia el formato de PDF, solo se modifica `GuardarComoPDF`.
- Cumplimos con ISP porque nadie está obligado a implementar métodos que no necesita. Si alguien quiere enviar documentos por email, solo usa `EnviarPorEmail`.

Este ejercicio refleja los principios de SRP e ISP al tener clases con responsabilidades bien definidas y evitando interfaces monolíticas.

---







