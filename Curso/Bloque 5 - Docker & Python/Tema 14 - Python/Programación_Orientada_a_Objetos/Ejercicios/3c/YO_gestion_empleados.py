'''SISTEMA DE GESTIÓN DE EMPLEADOS
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
- Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
- Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
- Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados'''

class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
    
    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Salario base: {self.salario} €"
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario, bono_anual):
        super().__init__(nombre, apellido, salario)
        self.bono_anual = bono_anual
    
    def calcular_salario(self):
        # Sobrescribe calcular_salario para incluir el bono anual en el cálculo del salario mensual
        salario_total = self.salario + (self.bono_anual / 12)
        return salario_total
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Salario mensual con bono: {self.calcular_salario():.2f} €"

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario, horas_semanales):
        super().__init__(nombre, apellido, salario)
        self.horas_semanales = horas_semanales
    
    def calcular_salario(self):
        # Sobrescribe calcular_salario para calcular el salario en función de las horas trabajadas por semana
        salario_total = (self.salario / 40) * self.horas_semanales
        return salario_total
    
    def __str__(self):
         return f"{self.nombre} {self.apellido}, Salario mensual (parcial): {self.calcular_salario():.2f} €"


# Creamos empleados a tiempo completo
empleado1 = EmpleadoTiempoCompleto("Juan", "Pérez", 2000, 6000)  # Bono anual de 6000 €
empleado2 = EmpleadoTiempoCompleto("Ana", "Gómez", 2500, 8000)  # Bono anual de 8000 €

# Creamos empleados a tiempo parcial
empleado3 = EmpleadoTiempoParcial("Carlos", "López", 1600, 20)  # 20 horas semanales
empleado4 = EmpleadoTiempoParcial("María", "Fernández", 1600, 30)  # 30 horas semanales

# Mostramos la información de los empleados y sus salarios totales
empleados = [empleado1, empleado2, empleado3, empleado4]

for empleado in empleados:
    print(empleado)
    print(f"Salario total: {empleado.calcular_salario():.2f} €\n")