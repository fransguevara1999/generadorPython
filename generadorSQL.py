import os
from pathlib import Path
from datetime import datetime

import mysql.connector
import logging

# Credenciales de la base de datos
db_user = "root"
db_password = "1234"
db_name = "prueba"
db_host = "localhost"
db_port = "33060"

# Tablas a exportar
tables_to_export = ["productos", "usuario"]

# Obtener la fecha actual
now = datetime.now()
current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# Archivo de salida
output_file = f"mi_base_de_datos_{current_time}.sql"

# Conexión a la base de datos
cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name, port=db_port)
cursor = cnx.cursor()

# Crear una lista de comandos de exportación de tablas
export_commands = []
ruta = Path.cwd()
constt = 0

for table in tables_to_export:
    export_commands.append(
        f"mysqldump -u {db_user} -p {db_password} -h {db_host} {db_name} {table} >> {output_file}")
    constt += 1
    # rutas = ruta +export_commands
    with open("text.txt", "w") as file:
        file.write(export_commands[constt])


print(Path.cwd())


# Cerrar la conexión a la base de datos
cursor.close()
cnx.close()
