from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
import models
import datetime

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


class Venta(BaseModel):
    venta_id: int
    fecha: datetime.datetime
    producto_id: int
    cantidad: int
    precio_unitario: float
    cliente_id: int
    sucursal_id: int
    total: float

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()  # Converts datetime to ISO format when converting to JSON
        }

class Logistica(BaseModel):
    envio_id: int
    venta_id: int
    fecha_envio: datetime.datetime
    proveedor_id: int
    estado_envio: str

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()  # Converts datetime to ISO format when converting to JSON
        }


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

    if cliente_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente does not exist")

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

    if producto_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto does not exist")

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

    if proveedor_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proveedor does not exist")

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

######################## METHODS VENTAS
@app.get('/ventas', response_model=List[Venta], status_code=200)
def get_all_ventas():
    ventas = db.query(models.Sale).all()
    return ventas


@app.get('/ventas/{venta_id}', response_model=Venta, status_code=status.HTTP_200_OK)
def get_a_venta(venta_id:int):
    venta = db.query(models.Sale).filter(models.Sale.venta_id == venta_id).first()
    if venta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta does not exist")
    return venta


@app.post('/ventas', response_model=Venta, status_code=status.HTTP_201_CREATED)
def create_venta(venta:Venta):
    db_venta = db.query(models.Sale).filter(models.Sale.venta_id == venta.venta_id).first()

    if db_venta is not None:
        raise HTTPException(status_code=400, detail="Venta already exists")

    new_venta = models.Sale(
        venta_id = venta.venta_id,
        fecha = venta.fecha,
        producto_id = venta.producto_id,
        cantidad = venta.cantidad,
        precio_unitario = venta.precio_unitario,
        cliente_id = venta.cliente_id,
        sucursal_id = venta.sucursal_id,
        total = venta.total
    )

    db.add(new_venta)
    db.commit()
    return new_venta


@app.put('/ventas/{venta_id}', response_model=Venta, status_code=status.HTTP_200_OK)
def update_venta(venta_id:int, venta:Venta):
    venta_to_update = db.query(models.Sale).filter(models.Sale.venta_id == venta_id).first()

    if venta_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta does not exist")

    venta_to_update.fecha = venta.fecha
    venta_to_update.producto_id = venta.producto_id
    venta_to_update.cantidad = venta.cantidad
    venta_to_update.precio_unitario = venta.precio_unitario
    venta_to_update.cliente_id = venta.cliente_id
    venta_to_update.sucursal_id = venta.sucursal_id
    venta_to_update.total = venta.total

    db.commit()
    return venta_to_update


@app.delete('/ventas/{venta_id')
def delete_venta(venta_id:int):
    venta_to_delete = db.query(models.Sale).filter(models.Sale.venta_id == venta_id).first()

    if venta_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta does not exist")

    db.delete(venta_to_delete)
    db.commit()

    return venta_to_delete

######################## METHODS LOGISTICA
@app.get('/logistica', response_model=List[Logistica], status_code=200)
def get_all_logistica():
    logistica = db.query(models.Logistic).all()
    return logistica


@app.get('/logistica/{envio_id}', response_model=Logistica, status_code=status.HTTP_200_OK)
def get_a_logistica(envio_id:int):
    logistica = db.query(models.Logistic).filter(models.Logistic.envio_id == envio_id).first()
    if logistica is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Envio does not exist")
    return logistica


@app.post('/logistica', response_model=Logistica, status_code=status.HTTP_201_CREATED)
def create_logistica(logistica:Logistica):
    db_logistica = db.query(models.Logistic).filter(models.Logistic.envio_id == logistica.envio_id).first()

    if db_logistica is not None:
        raise HTTPException(status_code=400, detail="Envio already exists")

    new_logistica = models.Logistic(
        envio_id = logistica.envio_id,
        venta_id = logistica.venta_id,
        fecha_envio = logistica.fecha_envio,
        proveedor_id = logistica.proveedor_id,
        estado_envio = logistica.estado_envio
    )

    db.add(new_logistica)
    db.commit()
    return new_logistica


@app.put('/logistica/{envio_id}', response_model=Logistica, status_code=status.HTTP_200_OK)
def update_logistica(envio_id:int, logistica:Logistica):
    logistica_to_update = db.query(models.Logistic).filter(models.Logistic.envio_id == envio_id).first()

    if logistica_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Envio does not exist")

    logistica_to_update.venta_id = logistica.venta_id
    logistica_to_update.fecha_envio = logistica.fecha_envio
    logistica_to_update.proveedor_id = logistica.proveedor_id
    logistica_to_update.estado_envio = logistica.estado_envio

    db.commit()
    return logistica_to_update


@app.delete('/logistica/{envio_id}')
def delete_logistica(envio_id:int):
    logistica_to_delete = db.query(models.Logistic).filter(models.Logistic.envio_id == envio_id).first()

    if logistica_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Envio does not exist")

    db.delete(logistica_to_delete)
    db.commit()

    return logistica_to_delete