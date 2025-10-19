'''TIENDA ONLINE
Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.'''

# Definimos la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        # Inicializamos los atributos del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad_en_stock = cantidad_en_stock  # Cantidad disponible en stock

# Definimos la clase Tienda
class Tienda:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los productos
        self.productos = []
    
    def agregar_producto(self, nuevo_producto):
        # Agregamos un producto a la lista de productos
        self.productos.append(nuevo_producto)
        # Mostramos un mensaje indicando que el producto fue agregado
        print(f"Producto '{nuevo_producto.nombre}' agregado al inventario.")
    
    def mostrar_inventario(self):
        # Mostramos todos los productos en el inventario
        print("Inventario de la tienda:")
        # Recorremos la lista de productos y mostramos sus detalles
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio} €, Cantidad en stock: {producto.cantidad_en_stock}")
    
    def realizar_compra(self):
        # Pedimos al usuario el nombre del producto que desea comprar
        nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
        # Pedimos al usuario la cantidad que desea comprar
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        
        # Recorremos la lista de productos para buscar el producto solicitado
        for producto in self.productos:
            if producto.nombre == nombre_producto:  # Si encontramos el producto...
                if producto.cantidad_en_stock >= cantidad:  # Verificamos si hay suficiente stock
                    # Reducimos la cantidad en stock
                    producto.cantidad_en_stock -= cantidad
                    # Mostramos el total a pagar
                    print(f"Compra realizada. Total a pagar: {producto.precio * cantidad} €")
                else:
                    # Si no hay suficiente stock, mostramos un mensaje de error
                    print("No hay suficiente stock.")
                return # para terminar la ejecución del método una vez que se ha completado una acción
        # Si no encontramos el producto (si se recorre el bucle hasta el final), mostramos un mensaje de error
        print("Producto no encontrado.") # como hacemos return antes el bucle for se para antes de llegar a este punto

# Creamos una instancia de la tienda
tienda1 = Tienda()

# Creamos productos
producto1 = Producto("Camisa", 20, 10)  # Producto: Camisa, Precio: 20 €, Stock: 10
producto2 = Producto("Pantalón", 30, 5)  # Producto: Pantalón, Precio: 30 €, Stock: 5
producto3 = Producto("Zapatos", 50, 2)  # Producto: Zapatos, Precio: 50 €, Stock: 2

# Agregamos productos a la tienda
tienda1.agregar_producto(producto1)
tienda1.agregar_producto(producto2)
tienda1.agregar_producto(producto3)

# Mostramos el inventario inicial
tienda1.mostrar_inventario()

# Realizamos una compra
tienda1.realizar_compra()
# Mostramos el inventario después de la compra
tienda1.mostrar_inventario()

# Realizamos otra compra
tienda1.realizar_compra()
# Mostramos el inventario después de la segunda compra
tienda1.mostrar_inventario()