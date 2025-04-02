# Caso Práctico
 Caso práctico nexolutions 2025


Contenido:
pythonScripts - contiene código de Python para primera fase de ETL para los datos recibidos
sqlQueries - contiene código de SQL para creación de tablas con modelo relacional, indexación y segunda fase de ETL
postSQLData - contiene datos resultantes después de modificación en PostgreSQL
steamlit_dashboard - contiene código para generación de dashboard interactivo en streamlit, cargando los datos desde PostgreSQL
modeloML - contiene código para modelo de machine learning con scikit


Metodología

1. Se subieron los archivos CSV con la información a una carpeta en Google Drive.

2. Usando Python, se leyeron los archivos desde Google Drive. 
Después, la información se cargó a data frames usando la librería pandas para poder modificarla. 
Por último, se usó pandas para hacer la primera ronda de limpieza y estandarización. 
Específicamente se hizo lo siguiente para todas las tablas:
Se borraron entradas vacías y duplicados
Se estandarizaron tipos de datos de las columnas

3. Usando PostgreSQL, se cargaron los datos a tablas para generar un modelo relacional y adicionalmente:
Se agregaron indexaciones para agilizar consultas en columnas que se consideraron más probables de ser consultadas
Se agregaron relaciones entre tablas mediante el uso de llaves externas
Se crearon tablas adicionales para archivar entradas que no permitían implementar relaciones entre tablas, específicamente entradas que referencian identificadores que no existen en la tabla externa. 
Después de crear las tablas externas con las entradas archivadas, se eliminaron de las tablas originales para poder crear las relaciones entre tablas.


3. Se creó un dashboard interactivo usando streamlit con la información de Postgres, mostrando diferentes queries de manera gráfica. Se usó una página para cada tabla, mostrando información pertinente de cada una.

4. Se creó un modelo de ML usando regresión lineal con scikit, usando la información de la tabla ventas.