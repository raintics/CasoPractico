-- create table
CREATE TABLE clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    genero TEXT NOT NULL,
    ubicacion TEXT NOT NULL
);

-- index to query by name
CREATE INDEX idx_clientes_nombre ON clientes(nombre);
