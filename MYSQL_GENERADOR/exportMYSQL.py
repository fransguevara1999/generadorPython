import mysql.utilities
import argparse

# Crear un objeto de análisis de argumentos
parser = argparse.ArgumentParser()

# Agregar argumentos de entrada
parser.add_argument("--user", help="Nombre de usuario para conectarse a la base de datos")
parser.add_argument("--password", help="Contraseña para conectarse a la base de datos")
parser.add_argument("--database", help="Nombre de la base de datos")
parser.add_argument("--port", help="Puerto para conectarse a la base de datos", type=int)

# Leer argumentos de entrada
args = parser.parse_args()

# Crear una cadena de conexión a la base de datos
conn_string = f"{args.user}:{args.password}@localhost:{args.port}/{args.database}"

# Exportar tablas y datos a un archivo SQL
mysql.utilities.dump_tables.dump_tables(conn_string, args.database, './dump.sql')