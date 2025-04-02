from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()

######################## CLASSES

class Cliente(BaseModel):
    cliente_id: int
    nombre: str
    edad: int
    genero: str
    ubicacion: str

    class Config:
        orm_mode = True


class Producto(BaseModel):
    producto_id: int
    nombre_producto: str
    categoria: str
    precio_base: float

    class Config:
        orm_mode = True


class Proveedor(BaseModel):
    proveedor_id: int
    nombre_proveedor: str
    contacto: str
    ubicacion: str

    class Config:
        orm_mode = True


######################## METHODS CLIENTES
@app.get('/clientes', response_model=List[Cliente], status_code=200)
def get_all_clientes():
    clientes = db.query(models.Client).all()
    return clientes


@app.get('/clientes/{cliente_id}', response_model=Cliente, status_code=status.HTTP_200_OK)
def get_a_cliente(cliente_id:int):
    cliente = db.query(models.Client).filter(models.Client.cliente_id == cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente does not exist")
    return cliente


@app.post('/clientes', response_model=Cliente, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente:Cliente):
    db_cliente = db.query(models.Client).filter(models.Client.cliente_id == cliente.cliente_id).first()

    if db_cliente is not None:
        raise HTTPException(status_code=400, detail="Cliente already exists")

    new_cliente = models.Client(
        cliente_id = cliente.cliente_id,
        nombre = cliente.nombre,
        edad = cliente.edad,
        genero = cliente.genero,
        ubicacion = cliente.ubicacion
    )

    db.add(new_cliente)
    db.commit()
    return new_cliente


@app.put('/clientes/{cliente_id}', response_model=Cliente, status_code=status.HTTP_200_OK)
def update_cliente(cliente_id:int, cliente:Cliente):
    cliente_to_update = db.query(models.Client).filter(models.Client.cliente_id == cliente_id).first()
    cliente_to_update.nombre = cliente.nombre
    cliente_to_update.edad = cliente.edad
    cliente_to_update.genero = cliente.genero
    cliente_to_update.ubicacion = cliente.ubicacion

    db.commit()
    return cliente_to_update


@app.delete('/clientes/{cliente_id}')
def delete_cliente(cliente_id:int):
    cliente_to_delete = db.query(models.Client).filter(models.Client.cliente_id == cliente_id).first()
    if cliente_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente does not exist")

    db.delete(cliente_to_delete)
    db.commit()

    return cliente_to_delete


######################## METHODS PRODUCTOS
@app.get('/productos', response_model=List[Producto], status_code=200)
def get_all_productos():
    productos = db.query(models.Product).all()
    return productos


@app.get('/productos/{producto_id}', response_model=Producto, status_code=status.HTTP_200_OK)
def get_a_producto(producto_id:int):
    producto = db.query(models.Product).filter(models.Product.producto_id == producto_id).first()
    if producto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto does not exist")
    return producto


@app.post('/productos', response_model=Producto, status_code=status.HTTP_201_CREATED)
def create_producto(producto:Producto):
    db_producto = db.query(models.Product).filter(models.Product.producto_id == producto.producto_id).first()

    if db_producto is not None:
        raise HTTPException(status_code=400, detail="Producto already exists")

    new_producto = models.Product(
        producto_id = producto.producto_id,
        nombre_producto = producto.nombre_producto,
        categoria = producto.categoria,
        precio_base = producto.precio_base
    )

    db.add(new_producto)
    db.commit()
    return new_producto


@app.put('/productos/{producto_id}', response_model=Producto, status_code=status.HTTP_200_OK)
def update_producto(producto_id:int, producto:Producto):
    producto_to_update = db.query(models.Product).filter(models.Product.producto_id == producto_id).first()
    producto_to_update.nombre_producto = producto.nombre_producto
    producto_to_update.categoria = producto.categoria
    producto_to_update.precio_base = producto.precio_base

    db.commit()
    return producto_to_update


@app.delete('/productos/{producto_id}')
def delete_producto(producto_id:int):
    producto_to_delete = db.query(models.Product).filter(models.Product.producto_id == producto_id).first()

    if producto_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto does not exist")

    db.delete(producto_to_delete)
    db.commit()

    return producto_to_delete

######################## METHODS PROVEEDORES
@app.get('/proveedores', response_model=List[Proveedor], status_code=200)
def get_all_proveedores():
    proveedores = db.query(models.Provider).all()
    return proveedores


@app.get('/proveedores/{proveedor_id}', response_model=Proveedor, status_code=status.HTTP_200_OK)
def get_a_proveedor(proveedor_id:int):
    proveedor = db.query(models.Provider).filter(models.Provider.proveedor_id == proveedor_id).first()
    if proveedor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor does not exist")
    return proveedor


@app.post('/proveedores', response_model=Proveedor, status_code=status.HTTP_201_CREATED)
def create_proveedor(proveedor:Proveedor):
    db_proveedor = db.query(models.Provider).filter(models.Provider.proveedor_id == proveedor.proveedor_id).first()

    if db_proveedor is not None:
        raise HTTPException(status_code=400, detail="Proveedor already exists")

    new_proveedor = models.Provider(
        proveedor_id = proveedor.proveedor_id,
        nombre_proveedor = proveedor.nombre_proveedor,
        contacto = proveedor.contacto,
        ubicacion = proveedor.ubicacion
    )

    db.add(new_proveedor)
    db.commit()
    return new_proveedor


@app.put('/proveedores/{proveedor_id}', response_model=Proveedor, status_code=status.HTTP_200_OK)
def update_proveedor(proveedor_id:int, proveedor:Proveedor):
    proveedor_to_update = db.query(models.Provider).filter(models.Provider.proveedor_id == proveedor_id).first()
    proveedor_to_update.nombre_proveedor = proveedor.nombre_proveedor
    proveedor_to_update.contacto = proveedor.contacto
    proveedor_to_update.ubicacion = proveedor.ubicacion

    db.commit()
    return proveedor_to_update


@app.delete('/proveedores/{proveedor_id}')
def delete_proveedor(proveedor_id:int):
    proveedor_to_delete = db.query(models.Provider).filter(models.Provider.proveedor_id == proveedor_id).first()

    if proveedor_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor does not exist")

    db.delete(proveedor_to_delete)
    db.commit()

    return proveedor_to_delete