from database import Base
from sqlalchemy import Column, Integer, Text, Numeric

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
