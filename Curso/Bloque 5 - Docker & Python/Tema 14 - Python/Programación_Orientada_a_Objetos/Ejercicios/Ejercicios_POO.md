# Ejercicios Prácticos

Para afianzar todo lo aprendido, a continuación se proponen algunos ejercicios prácticos de programación orientada a objetos. Cada ejercicio incluye el enunciado, una sugerencia de cómo estructurar la solución y la solución resuelta con explicaciones paso a paso. Se recomienda intentar resolver el enunciado por tu cuenta antes de mirar la solución, de ese modo pondrás a prueba tu comprensión de clases, atributos y métodos. ¡Manos a la obra!

## Ejercicio 1: Clase Persona

**Enunciado:**
Crea una clase Persona que tenga como atributos nombre y edad. Añade un método saludar que imprima un saludo incluyendo el nombre, y otro método cumplir_anio que aumente en 1 la edad de la persona. Prueba crear una instancia de Persona y utiliza sus métodos, mostrando antes y después la edad para verificar que el método cumplir_anio funciona correctamente.

**Estructura sugerida:**
- La clase deberá definirse con un `__init__` que reciba nombre y edad, asignándolos a atributos con self.
- El método `saludar(self)` no requiere parámetros adicionales, simplemente accederá a `self.nombre` (y quizá `self.edad` si quieres incluirla en el saludo).
- El método `cumplir_anio(self)` tampoco requiere parámetros externos, solo incrementará `self.edad`.
- Para probar, crea un objeto Persona con un nombre y edad inicial, llama a `saludar()`, luego a `cumplir_anio()`, y de nuevo a `saludar()` o imprime la edad para ver el cambio.

**Solución:**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def cumplir_anio(self):
        self.edad += 1
```

**Explicación paso a paso:**
- Paso 1: Definimos la clase Persona con su método `__init__`. Este método toma el nombre y la edad proporcionados al instanciar y los asigna a `self.nombre` y `self.edad` respectivamente. De este modo, cada objeto Persona almacenará esos valores.
- Paso 2: Definimos el método `saludar(self)`. Al llamarlo, accederá a los atributos del objeto (`self.nombre` y `self.edad`) y mostrará un saludo formateado. Usamos una f-string para incrustar los valores en el mensaje.
- Paso 3: Definimos el método `cumplir_anio(self)`, que simplemente incrementa en uno el atributo `self.edad`. No imprime nada ni retorna valor; su efecto es modificar el estado interno del objeto.
- Paso 4: Creamos una instancia `persona = Persona("Carlos", 29)`. Esto llama a `__init__` con nombre "Carlos" y edad 29, inicializando el objeto.
- Paso 5: Llamamos `persona.saludar()`. Internamente, Python pasa persona como self, y el método imprime "Hola, mi nombre es Carlos y tengo 29 años." utilizando los atributos de persona.
- Paso 6: Llamamos `persona.cumplir_anio()`. Esto accede a `persona.edad` (que era 29) y le suma 1, cambiando su valor a 30.
- Paso 7: Volvemos a saludar con `persona.saludar()`. Ahora el mensaje refleja la nueva edad: "Hola, mi nombre es Carlos y tengo 30 años." Confirmamos así que el atributo edad se actualizó correctamente tras usar el método.

Con este ejercicio, practicamos la definición de atributos, métodos y la mutación de atributos a través de métodos.

## Ejercicio 2: Clase Coche

**Enunciado:**
Implementa una clase Coche con los siguientes atributos: marca, combustible (en litros, por ejemplo) y consumo (litros por kilómetro, que indica cuánto combustible gasta por km). Incluye un método conducir que reciba una distancia en kilómetros y reduzca el combustible según el consumo, imprimiendo cuántos litros consumió y cuántos le quedan. Si no hay suficiente combustible para la distancia indicada, debe indicar que el coche no puede conducir tanto. Añade también un método repostar que reciba una cantidad de litros y aumente el combustible en esa cantidad, imprimiendo el nuevo nivel de combustible. Prueba creando un objeto Coche y utilizando sus métodos en distintos escenarios (suficiente combustible, combustible insuficiente, repostaje, etc.).

**Estructura sugerida:**
- `__init__` deberá inicializar marca, combustible y consumo con los valores proporcionados (o podrías dar un valor por defecto al consumo, ej. 0.1 l/km).
- `conducir(self, distancia)`: calcular cuántos litros se necesitan: `litros_necesarios = distancia * self.consumo`. Si `litros_necesarios <= self.combustible`, se resta ese consumo de `self.combustible` y se informa del viaje. Si es mayor, se avisa que no hay suficiente combustible.
- `repostar(self, litros)`: simplemente suma esa cantidad a `self.combustible` y notifica el nuevo estado.
- Asegúrate de formatear los mensajes indicando la marca para identificar el coche, y los litros con una cantidad razonable de decimales si es decimal.

**Solución:**

```python
class Coche:
    def __init__(self, marca, combustible, consumo):
        self.marca = marca
        self.combustible = combustible
        self.consumo = consumo
    def conducir(self, distancia):
        litros_necesarios = distancia * self.consumo
        if litros_necesarios <= self.combustible:
            self.combustible -= litros_necesarios
            print(f"{self.marca} ha conducido {distancia} km, consumiendo {litros_necesarios:.2f} L. Combustible restante: {self.combustible:.2f} L.")
        else:
            print(f"{self.marca} no tiene suficiente combustible para recorrer {distancia} km. Combustible actual: {self.combustible:.2f} L, se necesitan {litros_necesarios:.2f} L.")
    def repostar(self, litros):
        self.combustible += litros
        print(f"{self.marca} ha repostado {litros:.2f} L. Combustible total ahora: {self.combustible:.2f} L.")
```

**Explicación paso a paso:**
- Paso 1: Definimos la clase Coche con `__init__` que recibe marca, combustible inicial y consumo. Asignamos esos valores a los atributos del objeto. Por ejemplo, `consumo = 0.2` podría indicar que el coche gasta 0.2 litros por cada kilómetro recorrido.
- Paso 2: Definimos el método `conducir(self, distancia)`. Calculamos `litros_necesarios` multiplicando la distancia por el consumo por km. Luego comparamos `litros_necesarios` con el combustible disponible (`self.combustible`):
    - Si hay suficiente o igual combustible, reducimos `self.combustible` restándole `litros_necesarios` (simulando el gasto de combustible). Luego imprimimos un mensaje indicando la marca del coche, la distancia recorrida, litros consumidos y lo que queda de combustible. Usamos formato `:.2f` para mostrar los números con dos decimales, típico en cantidades de litros.
    - Si no hay suficiente combustible, no modificamos nada y simplemente informamos de que no se puede conducir esa distancia, mostrando cuánto combustible hay y cuánto se necesitaría.
- Paso 3: Definimos el método `repostar(self, litros)`. Este método aumenta `self.combustible` en la cantidad dada (simulando echar gasolina al tanque) y luego imprime un mensaje con la marca y el nuevo nivel de combustible. También aquí formateamos con dos decimales por claridad.
- Paso 4: Creamos un objeto `mi_coche = Coche("Toyota", 5.0, 0.2)`. Esto significa un coche Toyota con 5.0 litros en el tanque y un consumo de 0.2 L/km.
- Paso 5: Llamamos `mi_coche.conducir(10)`. Cálculo: 10 km * 0.2 = 2.0 L necesarios. Como tiene 5.0 L, es posible. El método resta 2.0 del combustible, quedando 3.0 L, e imprime algo como: "Toyota ha conducido 10 km, consumiendo 2.00 L. Combustible restante: 3.00 L."
- Paso 6: Llamamos `mi_coche.conducir(20)`. Cálculo: 20 * 0.2 = 4.0 L necesarios. Combustible actual es 3.0 L, insuficiente. El método detecta que 4.0 > 3.0 y por tanto imprime: "Toyota no tiene suficiente combustible para recorrer 20 km. Combustible actual: 3.00 L, se necesitan 4.00 L." (El combustible permanece en 3.0 L porque no se pudo hacer el viaje).
- Paso 7: Llamamos `mi_coche.repostar(10)`. Esto suma 10.0 L al combustible, pasando de 3.0 L a 13.0 L. Imprime: "Toyota ha repostado 10.00 L. Combustible total ahora: 13.00 L."
- Paso 8: Nuevamente `mi_coche.conducir(20)`. Ahora con 13.0 L disponibles, 4.0 L necesarios no son problema. Se consume 4.0 L, quedando 9.0 L. El mensaje indicará consumo y restante correctamente.

Con este ejercicio, practicamos la lógica dentro de métodos, usando y modificando múltiples atributos, y manejando condiciones (suficiente/insuficiente combustible) para decidir acciones dentro de un método.

## Ejercicio 3: Clase CuentaBancaria

**Enunciado:**
Desarrolla una clase CuentaBancaria que modele una cuenta simple. Debe tener un atributo de saldo. Implementa un método depositar(cantidad) que incremente el saldo, y un método retirar(cantidad) que disminuya el saldo solo si hay suficiente dinero (si no hay suficiente, que imprima un mensaje de error indicando saldo insuficiente). Además, agrega un método consultar_saldo() que imprima el saldo actual. Demuestra su funcionamiento creando una cuenta, realizando depósitos y retiros válidos e inválidos.

**Estructura sugerida:**
- `__init__` inicializa el saldo, posiblemente a 0 si no se indica otro valor.
- `depositar(self, cantidad)`: suma la cantidad al saldo e idealmente informa del nuevo saldo o cantidad depositada.
- `retirar(self, cantidad)`: verifica si `cantidad <= self.saldo`. Si sí, resta y notifica cuánto se retiró y el saldo restante; si no, notifica que no es posible y quizás indica el saldo disponible.
- `consultar_saldo(self)`: imprime (o retorna) el saldo actual. Si retornas el valor, podrías usarlo en un print externo; si lo imprimes directamente dentro, es más sencillo para este ejercicio.
- Maneja que la cantidad a depositar o retirar no sea negativa (podrías ignorar ese caso asumiendo entradas válidas, o manejarlo imprimiendo que no tiene sentido).
- En la prueba, muestra el saldo inicial, luego tras un depósito, luego tras un retiro válido, y tras un retiro inválido.

**Solución:**

```python
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Has depositado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            print(f"No es posible retirar ${cantidad:.2f}. Saldo insuficiente (${self.saldo:.2f}).")
    def consultar_saldo(self):
        print(f"Saldo disponible: ${self.saldo:.2f}.")
```

**Explicación paso a paso:**
- Paso 1: Definimos la clase CuentaBancaria con un `__init__` que acepta un saldo_inicial opcional (por defecto 0 si no se proporciona). Asignamos `self.saldo = saldo_inicial` para que cada nueva cuenta comience con ese saldo.
- Paso 2: Definimos `depositar(self, cantidad)`. Este método aumenta el saldo en la cantidad dada (`self.saldo += cantidad`). Luego imprime un mensaje confirmando la acción y mostrando el nuevo saldo. Formateamos la cantidad como dinero con 2 decimales.
- Paso 3: Definimos `retirar(self, cantidad)`. Comprobamos si la cantidad a retirar es menor o igual al saldo disponible. Si lo es, disminuimos el saldo (`self.saldo -= cantidad`) y confirmamos la transacción con un mensaje que incluye el nuevo saldo. Si no hay suficiente saldo (`cantidad > self.saldo`), no alteramos el saldo y emitimos un mensaje de error indicando que no es posible retirar esa cantidad y mostrando el saldo actual para referencia.
- Paso 4: Definimos `consultar_saldo(self)`. Este método simplemente imprime el saldo actual de la cuenta, formateado con dos decimales.
- Paso 5: Creamos una instancia `cuenta = CuentaBancaria(100.00)`. Esto invoca `__init__` con `saldo_inicial=100.00`, por lo que `self.saldo` comienza en 100 dólares.
- Paso 6: Llamamos `cuenta.consultar_saldo()`. Debería mostrar "Saldo disponible: $100.00." confirmando el saldo inicial.
- Paso 7: Llamamos `cuenta.depositar(50.25)`. Internamente suma 50.25 al saldo, que pasa de 100.00 a 150.25. Imprime "Has depositado $50.25. Saldo actual: $150.25."
- Paso 8: Llamamos `cuenta.retirar(20)`. Como hay $150.25, retirar $20 es posible. El saldo se reduce a $130.25. Mensaje: "Has retirado $20.00. Saldo actual: $130.25."
- Paso 9: Llamamos `cuenta.retirar(200)`. Ahora el saldo es $130.25, intentar retirar $200 no es posible. La condición falla, así que imprime "No es posible retirar $200.00. Saldo insuficiente ($130.25)." El saldo sigue siendo $130.25.
- Paso 10: Finalmente `cuenta.consultar_saldo()` nuevamente para verificar que el saldo final es $130.25, mostrando "Saldo disponible: $130.25."

Este ejercicio nos ayuda a dominar el concepto de mantener y cambiar estado dentro de un objeto, además de condicionales en métodos para validar operaciones. Nótese cómo cada método (`depositar`, `retirar`) usa y actualiza el atributo `self.saldo` de la instancia adecuada, manteniendo la lógica encapsulada en la clase.

## Ejercicio 4: Herencia y sobrescritura de métodos

**Enunciado:**
Crea una clase Persona con atributos nombre y edad, y un método saludar() que imprima un saludo genérico incluyendo esos datos. Luego crea una clase Estudiante que herede de Persona. Estudiante debe tener además un atributo universidad (por ejemplo, "UNAM", "MIT", etc.), y su método saludar() debe sobreescribir al de Persona para incluir la información de la universidad. Finalmente, crea una instancia de Estudiante y verifica que puede usar tanto el saludo personalizado como los atributos heredados de Persona.

**Estructura sugerida:**
- Definir la clase Persona con `__init__` para nombre y edad, y el método `saludar()`.
- Definir la clase `Estudiante(Persona)` que extienda Persona. Su `__init__` debe llamar a `super().__init__` para inicializar nombre y edad, y luego definir el atributo propio universidad.
- Sobreescribir `saludar()`.
- Crear un objeto Estudiante y probar sus métodos y atributos.

**Solución:**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)
        self.universidad = universidad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio en {self.universidad}.")
```

1. Definimos Persona con su constructor que inicializa nombre y edad, y un método saludar() que imprime un mensaje usando esos atributos.
2. Definimos Estudiante como subclase de Persona. En su `__init__`, usamos `super().__init__(nombre, edad)` para que Persona inicialice esos atributos (así evitamos duplicar código). Luego añadimos el atributo universidad.
3. En `Estudiante.saludar()`, escribimos un nuevo mensaje que incluye también la universidad. Este método sobreescribe al `saludar()` heredado de Persona.
4. Creamos una instancia de Persona (`persona1`) y una de Estudiante (`estudiante1`) para probar.
5. Al llamar `persona1.saludar()`, se ejecuta el método de Persona. Al llamar `estudiante1.saludar()`, se ejecuta el método de Estudiante (el sobreescrito). `estudiante1` conserva el atributo nombre heredado y añade el atributo universidad propio. Lo demostramos imprimiéndolos.

**Salida esperada:**
- `persona1.saludar()` podría imprimir: "Hola, me llamo Ana y tengo 30 años."
- `estudiante1.saludar()` podría imprimir: "Hola, me llamo Ana, tengo 30 años y estudio en UNAM."

Observa cómo el método `saludar()` se comporta diferente para Persona y Estudiante (polimorfismo mediante sobreescritura). Además, Estudiante hereda atributos como nombre y define los suyos propios como universidad.

## Ejercicio 5: Composición de clases

**Enunciado:**
Vamos a modelar un sistema sencillo de dispositivos. Crea una clase Bateria con un atributo carga (porcentaje de 0 a 100) y métodos `usar(energia)` (que reduzca la carga en cierto porcentaje, sin bajar de 0) y `recargar()` (que la ponga al 100%). Luego crea una clase Telefono con atributos marca y modelo. El teléfono debe tener una Bateria (instancia de Bateria). Agrega un método `usar_app(tiempo)` en Telefono que simule el uso de una aplicación por X minutos, reduciendo la batería (por ejemplo, 1% por minuto de uso). Finalmente, crea un objeto Telefono con su batería, úsalo por algunos minutos y muestra la carga de la batería antes y después de usarlo.

**Estructura sugerida:**
- Definir clase Bateria con `__init__(carga_inicial)`, método `usar(energia)` y método `recargar()`.
- Definir clase Telefono con atributos marca y modelo, y un atributo bateria (instancia de Bateria). Podemos inicializar la batería dentro de Telefono (p. ej. con carga 100 por defecto).
- Método `usar_app(tiempo)` en Telefono que llame a `self.bateria.usar(consumo)` con el porcentaje a consumir (si asumimos 1% por minuto, consumo = tiempo).
- Mostrar el nivel de batería con `telefono.bateria.carga` antes y después del uso.

**Solución:**

```python
class Bateria:
    def __init__(self, carga_inicial=100):
        # Aseguramos que la carga inicial esté entre 0 y 100
        self.carga = max(0, min(100, carga_inicial))
    def usar(self, energia):
        self.carga -= energia
        if self.carga < 0:
            self.carga = 0
        print(f"Energía consumida: {energia}%. Carga restante: {self.carga}%.")
    def recargar(self):
        self.carga = 100
        print("Batería recargada al 100%.")

class Telefono:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = Bateria()
    def usar_app(self, minutos):
        consumo = minutos # 1% de batería por minuto de uso
        self.bateria.usar(consumo)
```

Ahora, probemos estas clases:

```python
mi_tel = Telefono("Xiaomi", "Mi 11")
print(mi_tel.bateria.carga) # salida: 100 (porcentaje inicial)
mi_tel.usar_app(30)         # usa 30% de la batería
print(mi_tel.bateria.carga) # salida: 70
mi_tel.usar_app(50)         # usa otros 50%, debería quedar 20%
print(mi_tel.bateria.carga) # salida: 20
mi_tel.bateria.recargar()   # recarga al 100%
print(mi_tel.bateria.carga) # salida: 100
```

Vemos que el teléfono contiene un objeto Bateria y delega en él el manejo de la carga. Esta es la composición en acción: un Telefono tiene una Bateria.

## Ejercicio 6: Métodos especiales y polimorfismo

**Enunciado:**
Construye una clase Libro con atributos titulo y autor. Implementa los métodos especiales `__str__` y `__repr__` para que las instancias se muestren de forma legible. En particular, `__str__` debe devolver `"<titulo>" de <autor>` (por ejemplo, `"Cien años de soledad" de Gabriel García Márquez`), mientras que `__repr__` debe devolver `Libro(titulo='<titulo>', autor='<autor>')`. Añade también un método `citar()` que devuelva un texto simulando una cita del libro (por ejemplo: «Extracto de "titulo"...»). Luego, crea dos clases que hereden de Libro: Ebook y Audiolibro, que representen libros en formato electrónico y audiolibro respectivamente. Cada una debe sobreescribir el método `citar()` para reflejar su formato (por ejemplo, en `Audiolibro.citar()` la cita podría incluir que es narrada). Crea instancias de Ebook y Audiolibro y muestra sus representaciones (usando print y repr) y sus citas para verificar el polimorfismo.

**Estructura sugerida:**
- Clase Libro con método `__init__(titulo, autor)`, `__str__`, `__repr__` y `citar()`.
- Clases `Ebook(Libro)` y `Audiolibro(Libro)` que sobreescriban `citar()`.
- En `Ebook.citar()`, indicar que es un contenido digital (por ejemplo, añadir "(eBook)" en la cita).
- En `Audiolibro.citar()`, indicar que es una narración (por ejemplo, prefijar con "(Narración)...").
- Crear instancias y probar: imprimirlas (para ver `__str__`), hacer `repr()` y llamar a `citar()`.

**Solución:**

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f'"{self.titulo}" de {self.autor}'
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}')"
    def citar(self):
        return f'«Extracto de "{self.titulo}"...»'

class Ebook(Libro):
    def citar(self):
        return f'«Extracto de "{self.titulo}"...» (eBook)'

class Audiolibro(Libro):
    def citar(self):
        return f'(Narración) «Extracto de "{self.titulo}"...»'
```

Probemos estas clases:

```python
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
ebook1 = Ebook("Don Quijote de la Mancha", "Miguel de Cervantes")
audio1 = Audiolibro("Don Quijote de la Mancha", "Miguel de Cervantes")
# __str__ y __repr__
print(libro1)      # "Don Quijote de la Mancha" de Miguel de Cervantes
print(ebook1)      # "Don Quijote de la Mancha" de Miguel de Cervantes
print(audio1)      # "Don Quijote de la Mancha" de Miguel de Cervantes
print(repr(libro1))   # Libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes')
print(repr(ebook1))   # Libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes')
print(repr(audio1))   # Libro(titulo='Don Quijote de la Mancha', autor='Miguel de Cervantes')
# Citas (polimorfismo)
print(libro1.citar())     # «Extracto de "Don Quijote de la Mancha"..."
print(ebook1.citar())     # «Extracto de "Don Quijote de la Mancha"..." (eBook)
print(audio1.citar())     # (Narración) «Extracto de "Don Quijote de la Mancha"..."
```

Explicación:
- Las representaciones por `print(obj)` son amigables y comparten el formato definido en `Libro.__str__`.
- Las representaciones de `repr(obj)` muestran la estructura definida en `Libro.__repr__`.
- Las citas son diferentes dependiendo del tipo real del objeto, demostrando polimorfismo: la llamada `obj.citar()` ejecuta una función distinta según si es un Libro base, un Ebook o un Audiolibro.
