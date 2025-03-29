-- Create table
CREATE TABLE ventas (
    venta_id SERIAL PRIMARY KEY,
    fecha TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario NUMERIC NOT NULL,
    cliente_id INTEGER NOT NULL,
    sucursal_id INTEGER NOT NULL,
    total NUMERIC NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

-- Index for producto_id
CREATE INDEX idx_ventas_producto_id ON ventas(producto_id);

-- Index for cliente_id
CREATE INDEX idx_ventas_cliente_id ON ventas(cliente_id);

-- Index for sucursal_id
CREATE INDEX idx_ventas_sucursal_id ON ventas(sucursal_id);


-- PROCESS: add cliente_id as foreign key to table ventas
-- 1. Search entries with cliente_id that do not exist in clientes table
SELECT * FROM ventas
WHERE cliente_id NOT IN (SELECT cliente_id FROM clientes);

-- 2. Create new table to store non compliant entries
CREATE TABLE archivo_ventas_clientes AS
SELECT * FROM ventas
WHERE cliente_id NOT IN (SELECT cliente_id FROM clientes);

DELETE FROM ventas
WHERE cliente_id NOT IN (SELECT cliente_id FROM clientes);

-- 3. Add constraint for cliente_id as foreign key
ALTER TABLE ventas
ADD CONSTRAINT fk_cliente
FOREIGN KEY (cliente_id)
REFERENCES clientes (cliente_id);


-- PROCESS: add producto_id as foreign key to table ventas
-- 1. Search entries with producto_id that do not exist in productos table
SELECT * FROM ventas
WHERE producto_id NOT IN (SELECT producto_id FROM productos);

-- 2. Create new table to store non compliant entries
CREATE TABLE archivo_ventas_producto AS
SELECT * FROM ventas
WHERE producto_id NOT IN (SELECT producto_id FROM productos);

DELETE FROM ventas
WHERE producto_id NOT IN (SELECT producto_id FROM productos);

-- 3. Add constraint for producto_id as foreign key
ALTER TABLE ventas
ADD CONSTRAINT fk_producto
FOREIGN KEY (producto_id)
REFERENCES productos (producto_id);
