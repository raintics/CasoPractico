-- Create table
CREATE TABLE logistica (
    envio_id SERIAL PRIMARY KEY,
    venta_id INTEGER NOT NULL,
    fecha_envio TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    proveedor_id INTEGER NOT NULL,
    estado_envio TEXT NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas(venta_id),
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(proveedor_id)
);

-- Index for venta_id
CREATE INDEX idx_logistica_venta_id ON logistica(venta_id);

-- Index for proveedor_id
CREATE INDEX idx_logistica_proveedor_id ON logistica(proveedor_id);

-- Index for fecha_envio
CREATE INDEX idx_logistica_fecha_envio ON logistica(fecha_envio);


-- PROCESS: add venta_id as foreign key to table logistica
-- 1. Search entries with cliente_id that do not exist in clientes table
SELECT *
FROM logistica l
WHERE NOT EXISTS (
    SELECT 1
    FROM ventas v
    WHERE v.venta_id = l.venta_id
);

-- 2. Create new table to store non compliant entries
CREATE TABLE archivo_logistica_ventas AS
SELECT *
FROM logistica l
WHERE NOT EXISTS (
    SELECT 1
    FROM ventas v
    WHERE v.venta_id = l.venta_id
);

DELETE FROM logistica
WHERE NOT EXISTS (
    SELECT 1
    FROM ventas v
    WHERE v.venta_id = logistica.venta_id
);

-- 3. Add constraint for venta_id as foreign key
ALTER TABLE logistica
ADD CONSTRAINT fk_venta
FOREIGN KEY (venta_id)
REFERENCES ventas (venta_id);


-- PROCESS: add proveedor_id as foreign key to table logistica
-- 1. Search entries with cliente_id that do not exist in clientes table
SELECT *
FROM logistica l
WHERE NOT EXISTS (
    SELECT 1
    FROM proveedores p
    WHERE p.proveedor_id = l.proveedor_id
);

-- 2. Create new table to store non compliant entries
CREATE TABLE archivo_logistica_proveedores AS
SELECT *
FROM logistica l
WHERE NOT EXISTS (
    SELECT 1
    FROM proveedores p
    WHERE p.proveedor_id = l.proveedor_id
);

DELETE FROM logistica
WHERE NOT EXISTS (
    SELECT 1
    FROM proveedores p
    WHERE p.proveedor_id = logistica.proveedor_id
);

-- 3. Add constraint for proveedor_id as foreign key
ALTER TABLE logistica
ADD CONSTRAINT fk_proveedor
FOREIGN KEY (proveedor_id)
REFERENCES proveedores (proveedor_id);
