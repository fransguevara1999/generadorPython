import mysql.connector

prueba="pruebaMuestraBD"
# Conectarse a la base de datos existente
existing_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mysql_docker"
)

# Conectarse a la nueva base de datos
new_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)

# Crear una nueva base de datos
cursor = new_db.cursor()
cursor.execute(f"CREATE DATABASE {prueba}")

# Obtener todas las tablas de la base de datos existente
cursor = existing_db.cursor()
cursor.execute("SHOW TABLES")

for table in cursor:
    table_name = table[0]

    # Crear una tabla con el mismo nombre en la nueva base de datos
    cursor.execute(f"CREATE TABLE nueva_base_de_datos.{table_name} LIKE tu_base_de_datos.{table_name}")

    # Copiar los datos de la tabla existente a la nueva tabla
    cursor.execute(f"INSERT INTO nueva_base_de_datos.{table_name} SELECT * FROM tu_base_de_datos.{table_name}")

# Confirmar los cambios
new_db.commit()