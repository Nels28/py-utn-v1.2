import peewee

db = peewee.SqliteDatabase("baseDatos.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Productos(BaseModel):
    nombreProducto = peewee.CharField(max_length=20)
    categoria = peewee.CharField(max_length=20)
    precio = peewee.IntegerField()
    stock = peewee.BooleanField(default=True)


db.connect()
db.create_tables([Productos])


class abmcProductos:
    def alta(self, nombre, categoria, precio, stock=bool):
        producto = Productos()
        producto.nombreProducto = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock
        producto.save()

    def consulta(self):
        return Productos.select()

    def baja(self, id):
        borrar = Productos.get(Productos.id == id)
        borrar.delete_instance()

    def modificar(self, id, nombre, categoria, precio, stock):
        update = Productos.update(nombreProducto=nombre, categoria=categoria,
                                  precio=precio, stock=stock).where(Productos.id == id)
        update.execute()
