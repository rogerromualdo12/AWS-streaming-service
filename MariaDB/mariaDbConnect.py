import mariadb
import sys

try:
    conn = mariadb.connect(
        user = "admin",
        password = "Mariadb.2023",
        host = "retail-db.cfwzwyspx0si.us-east-1.rds.amazonaws.com",
        port = 3306,
        database = "retail-db"
    )
except mariadb.Error as e:
    print(f"Error conectando a MariaDB: {e}")
    sys.exit(1)

ciudad = "Brownsville"