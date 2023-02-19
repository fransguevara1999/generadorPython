import mysql.connector

# Conexión a la base de datos origen
mydb_origin = mysql.connector.connect(
  host="hostname_origin",
  user="username_origin",
  password="password_origin",
  database="database_name_origin"
)

# Conexión a la base de datos destino
mydb_destination = mysql.connector.connect(
  host="hostname_destination",
  user="username_destination",
  password="password_destination"
)

# Crear cursor
mycursor = mydb_origin.cursor()

# Exportar base de datos
mysql.utilities.copy_db.copy_db(mydb_origin, mydb_destination, 'database_name_origin')

print("Database exported successfully")