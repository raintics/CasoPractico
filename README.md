# CasoPractico
 Caso practico nexolutions 2025

Metodologia

1. Se subieron los archivos csv con la informacion a una carpeta en google drive.

2. Usando python, se leyeron los archivos desde google drive. 
Despues, la informacion se cargo a data frames usando la libreria pandas para poder modificarla. 
Por ultimo, se uso pandas para hacer la primera ronda de limpieza y estandarizacion. 
Especificamente se hizo lo siguiente para todas las tablas:
Se borraros entradas vacias y duplicados
Se estandarizaron tipos de datos de las columnas

3. Usando PostgreSQL, se cargaron los datos a tablas para generar un modelo relacional y adicionalmente:
Se agregaron indexaciones para agilizar consultas en columnas que se consideraron mas probables de ser consultadas
Se agregaron relaciones entre tablas mediante el uso de llaves externas
Se crearon tablas adicionales para archivar entradas que no permitian implementar relaciones entre tablas, especificamente entradas que referencian identificadores que no existen en la tabla externa. 
Despues de crear las tablas externas con las entradas archivadas, se eliminaron de las tablas originales para poder crear las relaciones entre tablas.