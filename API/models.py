from database import Base
from sqlalchemy import Column, Integer, Text, Numeric, TIMESTAMP, ForeignKey


class Client(Base):
    __tablename__ = 'clientes'

    cliente_id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(Text, index=True, nullable=False)
    edad = Column(Integer, nullable=False)
    genero = Column(Text, nullable=False)
    ubicacion = Column(Text, nullable=False)


class Product(Base):
    __tablename__ = 'productos'

    producto_id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre_producto = Column(Text, index=True, nullable=False)
    categoria = Column(Text, index=True, nullable=False)
    precio_base = Column(Numeric, nullable=False)


class Provider(Base):
    __tablename__ = 'proveedores'

    proveedor_id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre_proveedor = Column(Text, index=True, nullable=False)
    contacto = Column(Text, index=True, nullable=False)
    ubicacion = Column(Text, nullable=False)


class Sale(Base):
    __tablename__ = 'ventas'

    venta_id = Column(Integer, primary_key=True, index=True, nullable=False)
    fecha = Column(TIMESTAMP, nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.producto_id'))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.cliente_id'))
    sucursal_id = Column(Integer, index=True, nullable=False)
    total = Column(Numeric, nullable=False)


class Logistic(Base):
    __tablename__ = 'logistica'

    envio_id = Column(Integer, primary_key=True, index=True, nullable=False)
    venta_id = Column(Integer, ForeignKey('ventas.venta_id'))
    fecha_envio = Column(TIMESTAMP, nullable=False)
    proveedor_id = Column(Integer, ForeignKey('proveedores.proveedor_id'))
    estado_envio = Column(Text, nullable=False)
