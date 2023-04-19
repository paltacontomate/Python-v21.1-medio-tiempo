class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado==True:
            self.precio *+cambio_porcentaje
        else:
            self.precio *-cambio_porcentaje
            return self

    def print_info(self):
        print(f"Informacion Del Producto:{self.nombre} {self.precio} {self.categoria}")