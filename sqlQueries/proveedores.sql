-- Create Table
CREATE TABLE proveedores (
    proveedor_id SERIAL PRIMARY KEY,
    nombre_proveedor TEXT NOT NULL,
    contacto TEXT NOT NULL,
    ubicacion TEXT NOT NULL
);

-- Index for nombre_proveedor
CREATE INDEX idx_proveedores_nombre_proveedor ON proveedores(nombre_proveedor);

-- Index for contacto
CREATE INDEX idx_proveedores_contacto ON proveedores(contacto);
