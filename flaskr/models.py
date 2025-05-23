class Usuario:
    def __init__(self, id, nombre, correo, activo=True):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.activo = activo

# Para las tarjetas del producto
class Producto:
    def __init__(self, id, marca, modelo, imagen, precio, stock):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.imagen = imagen
        self.precio = precio
        self.stock = stock
        
# Para Detalles completos o editar producto
class ProductoEditar:
    def __init__(self, id, marca, modelo, descripcion, id_categoria, imagen, precio, stock, recomendado):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.id_categoria =id_categoria
        self.imagen = imagen
        self.precio = precio
        self.stock = stock
        self.recomendado = recomendado

class ProductoAuxiliar:
    def __init__(self, id, marca, modelo, imagen, precio):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.imagen = imagen
        self.precio = precio

class ElementoCarrito:
    def __init__(self, id, marca, modelo, precio, cantidad, stock):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad = cantidad
        self.stock = stock
