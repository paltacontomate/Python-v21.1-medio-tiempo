class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.producto = []
        
    def agregar_producto(self, nuevo_producto):
        if nuevo_producto != None:
            self.producto.append(nuevo_producto)
        return self
    def imprimir_productos(self):
        for x in self.producto:
            x.print_info()
        return self