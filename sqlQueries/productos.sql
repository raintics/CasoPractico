-- create table
CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,
    nombre_producto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio_base NUMERIC NOT NULL
);

-- Index for nombre_producto
CREATE INDEX idx_productos_nombre_producto ON productos(nombre_producto);

-- Index for categoria
CREATE INDEX idx_productos_categoria ON productos(categoria);