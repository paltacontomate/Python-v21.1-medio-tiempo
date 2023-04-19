from tienda import Tienda
from producto import Producto 

tienda1 = Tienda("elian")


producto1 = Producto("Camisa", 20, "pantalones")
producto2 = Producto("Televisor", 500, "Electrónica")
producto3 = Producto("Libro", 10, "Libros")


tienda1.agregar_producto(producto1).agregar_producto(producto2).agregar_producto(producto3)

tienda1.imprimir_productos()
"""
producto1.print_info()
producto1.print_info()
producto1.print_info()
"""